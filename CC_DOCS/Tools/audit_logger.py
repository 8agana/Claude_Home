#!/usr/bin/env python3
"""
Audit Logger for AI Operations
Tracks all significant actions for security and analysis
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
import hashlib
from typing import Dict, Any, Optional, List

class AuditLogger:
    def __init__(self, log_dir: str = "/Users/samuelatagana/Documents/mcp-servers/memory/audit"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.current_log = self.log_dir / f"audit_{datetime.now().strftime('%Y%m')}.jsonl"
        
    def log_action(self, 
                   actor: str,
                   action: str,
                   target: str,
                   result: str,
                   metadata: Optional[Dict[str, Any]] = None) -> str:
        """Log an auditable action"""
        
        # Create audit entry
        entry = {
            "id": self._generate_id(),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "actor": actor,
            "action": action,
            "target": target,
            "result": result,
            "metadata": metadata or {}
        }
        
        # Add security hash
        entry["hash"] = self._generate_hash(entry)
        
        # Append to log file
        with open(self.current_log, 'a') as f:
            f.write(json.dumps(entry) + '\n')
            
        # Check if critical action
        if self._is_critical(action):
            self._alert_critical(entry)
            
        return entry["id"]
    
    def query_logs(self,
                   actor: Optional[str] = None,
                   action: Optional[str] = None,
                   start_date: Optional[datetime] = None,
                   end_date: Optional[datetime] = None,
                   limit: int = 100) -> List[Dict[str, Any]]:
        """Query audit logs with filters"""
        
        results = []
        
        # Determine which log files to search
        log_files = self._get_log_files(start_date, end_date)
        
        for log_file in log_files:
            if not log_file.exists():
                continue
                
            with open(log_file, 'r') as f:
                for line in f:
                    try:
                        entry = json.loads(line.strip())
                        
                        # Apply filters
                        if actor and entry.get('actor') != actor:
                            continue
                        if action and entry.get('action') != action:
                            continue
                        if start_date and datetime.fromisoformat(entry['timestamp'][:-1]) < start_date:
                            continue
                        if end_date and datetime.fromisoformat(entry['timestamp'][:-1]) > end_date:
                            continue
                            
                        results.append(entry)
                        
                        if len(results) >= limit:
                            return results
                            
                    except json.JSONDecodeError:
                        continue
                        
        return results
    
    def generate_report(self, days: int = 7) -> Dict[str, Any]:
        """Generate audit report for specified period"""
        
        start_date = datetime.utcnow() - timedelta(days=days)
        logs = self.query_logs(start_date=start_date, limit=10000)
        
        report = {
            "period": f"Last {days} days",
            "total_actions": len(logs),
            "actors": {},
            "actions": {},
            "results": {"SUCCESS": 0, "FAILURE": 0, "PARTIAL": 0},
            "critical_events": [],
            "anomalies": []
        }
        
        for entry in logs:
            # Count by actor
            actor = entry['actor']
            if actor not in report['actors']:
                report['actors'][actor] = 0
            report['actors'][actor] += 1
            
            # Count by action
            action = entry['action']
            if action not in report['actions']:
                report['actions'][action] = 0
            report['actions'][action] += 1
            
            # Count by result
            result = entry['result']
            if result in report['results']:
                report['results'][result] += 1
                
            # Collect critical events
            if self._is_critical(action):
                report['critical_events'].append({
                    "timestamp": entry['timestamp'],
                    "actor": actor,
                    "action": action,
                    "target": entry['target']
                })
                
        # Detect anomalies
        report['anomalies'] = self._detect_anomalies(logs)
        
        return report
    
    def verify_integrity(self, start_date: Optional[datetime] = None) -> Dict[str, Any]:
        """Verify audit log integrity"""
        
        log_files = self._get_log_files(start_date)
        results = {
            "checked_files": len(log_files),
            "total_entries": 0,
            "valid_entries": 0,
            "tampered_entries": 0,
            "corrupted_entries": 0
        }
        
        for log_file in log_files:
            if not log_file.exists():
                continue
                
            with open(log_file, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    results['total_entries'] += 1
                    
                    try:
                        entry = json.loads(line.strip())
                        
                        # Verify hash
                        stored_hash = entry.get('hash', '')
                        entry_copy = entry.copy()
                        entry_copy.pop('hash', None)
                        calculated_hash = self._generate_hash(entry_copy)
                        
                        if stored_hash == calculated_hash:
                            results['valid_entries'] += 1
                        else:
                            results['tampered_entries'] += 1
                            print(f"Tampered entry in {log_file}:{line_num}")
                            
                    except json.JSONDecodeError:
                        results['corrupted_entries'] += 1
                        print(f"Corrupted entry in {log_file}:{line_num}")
                        
        return results
    
    def cleanup_old_logs(self, days: int = 90):
        """Remove audit logs older than specified days"""
        
        cutoff_date = datetime.utcnow() - timedelta(days=days)
        
        for log_file in self.log_dir.glob("audit_*.jsonl"):
            # Extract date from filename
            try:
                file_date = datetime.strptime(log_file.stem.split('_')[1], '%Y%m')
                if file_date < cutoff_date:
                    # Archive before deleting
                    archive_path = self.log_dir / "archive" / log_file.name
                    archive_path.parent.mkdir(exist_ok=True)
                    log_file.rename(archive_path)
                    print(f"Archived {log_file.name}")
            except (IndexError, ValueError):
                continue
    
    def _generate_id(self) -> str:
        """Generate unique audit entry ID"""
        timestamp = datetime.utcnow().isoformat()
        return hashlib.sha256(timestamp.encode()).hexdigest()[:16]
    
    def _generate_hash(self, entry: Dict[str, Any]) -> str:
        """Generate integrity hash for entry"""
        # Create deterministic string representation
        content = json.dumps(entry, sort_keys=True)
        return hashlib.sha256(content.encode()).hexdigest()
    
    def _is_critical(self, action: str) -> bool:
        """Determine if action is critical"""
        critical_actions = [
            "CONFIG_CHANGE",
            "PERMISSION_GRANT",
            "PERMISSION_REVOKE",
            "SYSTEM_RESTART",
            "DATA_DELETE",
            "SECURITY_EVENT",
            "AUDIT_TAMPER"
        ]
        return action in critical_actions
    
    def _alert_critical(self, entry: Dict[str, Any]):
        """Send alert for critical actions"""
        # In production, this would send actual alerts
        alert_file = self.log_dir / "critical_alerts.json"
        alerts = []
        
        if alert_file.exists():
            with open(alert_file, 'r') as f:
                alerts = json.load(f)
                
        alerts.append({
            "timestamp": entry['timestamp'],
            "entry_id": entry['id'],
            "actor": entry['actor'],
            "action": entry['action'],
            "target": entry['target']
        })
        
        with open(alert_file, 'w') as f:
            json.dump(alerts, f, indent=2)
    
    def _get_log_files(self, 
                       start_date: Optional[datetime] = None,
                       end_date: Optional[datetime] = None) -> List[Path]:
        """Get list of log files to search"""
        
        log_files = []
        
        for log_file in sorted(self.log_dir.glob("audit_*.jsonl")):
            # Extract date from filename
            try:
                file_date = datetime.strptime(log_file.stem.split('_')[1], '%Y%m')
                
                if start_date and file_date < start_date.replace(day=1):
                    continue
                if end_date and file_date > end_date:
                    continue
                    
                log_files.append(log_file)
                
            except (IndexError, ValueError):
                continue
                
        return log_files
    
    def _detect_anomalies(self, logs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Detect anomalous patterns in logs"""
        
        anomalies = []
        
        # Check for unusual activity patterns
        actor_actions = {}
        
        for entry in logs:
            actor = entry['actor']
            timestamp = datetime.fromisoformat(entry['timestamp'][:-1])
            
            if actor not in actor_actions:
                actor_actions[actor] = []
            actor_actions[actor].append(timestamp)
        
        # Detect rapid actions
        for actor, timestamps in actor_actions.items():
            timestamps.sort()
            rapid_actions = 0
            
            for i in range(1, len(timestamps)):
                if (timestamps[i] - timestamps[i-1]).total_seconds() < 1:
                    rapid_actions += 1
                    
            if rapid_actions > 10:
                anomalies.append({
                    "type": "RAPID_ACTIONS",
                    "actor": actor,
                    "count": rapid_actions,
                    "severity": "MEDIUM"
                })
        
        # Check for failed operations spike
        failure_count = sum(1 for entry in logs if entry['result'] == 'FAILURE')
        if failure_count > len(logs) * 0.1:  # More than 10% failures
            anomalies.append({
                "type": "HIGH_FAILURE_RATE",
                "rate": f"{(failure_count/len(logs)*100):.1f}%",
                "severity": "HIGH"
            })
        
        return anomalies


# Example usage and testing
if __name__ == "__main__":
    logger = AuditLogger()
    
    # Example: Log a memory write operation
    logger.log_action(
        actor="CC",
        action="MEMORY_WRITE",
        target="cc_memories",
        result="SUCCESS",
        metadata={
            "memory_count": 3,
            "categories": ["technical", "workflow"],
            "source": "conversation"
        }
    )
    
    # Example: Log a configuration change
    logger.log_action(
        actor="Desktop_Claude",
        action="CONFIG_CHANGE",
        target="access_control.json",
        result="SUCCESS",
        metadata={
            "change": "Added read permission for shared_knowledge",
            "approved_by": "Sam"
        }
    )
    
    # Generate a report
    report = logger.generate_report(days=7)
    print(json.dumps(report, indent=2))
    
    # Verify integrity
    integrity = logger.verify_integrity()
    print(f"\nIntegrity Check: {integrity}")