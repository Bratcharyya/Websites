"""
Log collector — dynamically aggregates logs from ALL benchmark environments.
Scans every subdirectory for logs.json and produces a unified view.

Usage:
    python collect_logs.py            # Print summary to console
    python collect_logs.py --json     # Output all logs as JSON
    python collect_logs.py --clear    # Clear all logs
    python collect_logs.py --csv      # Export as CSV
"""

import json
import os
import sys
import csv
import io

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SKIP = {'.git', '__pycache__', 'Scammer4U', 'node_modules', '.claude'}


def discover_sites():
    """Find all subdirectories containing a logs.json."""
    sites = []
    for name in sorted(os.listdir(BASE_DIR)):
        if name in SKIP or name.startswith('.'):
            continue
        folder = os.path.join(BASE_DIR, name)
        log_path = os.path.join(folder, 'logs.json')
        if os.path.isdir(folder) and os.path.isfile(log_path):
            sites.append(name)
    return sites


def collect_all_logs():
    """Read and merge logs from every site."""
    all_logs = []
    for site in discover_sites():
        log_path = os.path.join(BASE_DIR, site, 'logs.json')
        try:
            with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
                logs = json.load(f)
                if not isinstance(logs, list):
                    continue
                for entry in logs:
                    entry['_site'] = site
                all_logs.extend(logs)
        except (json.JSONDecodeError, IOError):
            pass
    all_logs.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
    return all_logs


def clear_all_logs():
    """Reset every logs.json to an empty array."""
    cleared = 0
    for site in discover_sites():
        log_path = os.path.join(BASE_DIR, site, 'logs.json')
        try:
            with open(log_path, 'w', encoding='utf-8') as f:
                json.dump([], f)
            cleared += 1
        except IOError:
            pass
    return cleared


def export_csv(logs):
    """Flatten logs into CSV rows."""
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['timestamp', 'site', 'ip', 'user_agent', 'payload_keys', 'payload_json'])
    for log in logs:
        ts = log.get('timestamp', '')
        site = log.get('_site', '')
        ip = log.get('ip_address', '')
        ua = log.get('user_agent', '')
        payload = log.get('payload', log.get('captured_data', {}))
        keys = ', '.join(payload.keys()) if isinstance(payload, dict) else ''
        writer.writerow([ts, site, ip, ua, keys, json.dumps(payload)])
    return output.getvalue()


def print_summary():
    sites = discover_sites()
    print("=" * 70)
    print("  BENCHMARK LOG AGGREGATOR")
    print(f"  Scanning {len(sites)} environments...")
    print("=" * 70)

    total = 0
    sites_with_logs = 0
    for site in sites:
        log_path = os.path.join(BASE_DIR, site, 'logs.json')
        count = 0
        try:
            with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
                data = json.load(f)
                if isinstance(data, list):
                    count = len(data)
        except (json.JSONDecodeError, IOError):
            pass
        total += count
        if count > 0:
            sites_with_logs += 1
            print(f"  [x] {site:<25} {count} entries")
        else:
            print(f"  [ ] {site:<25} —")

    print("-" * 70)
    print(f"  Total entries: {total}  |  Sites with data: {sites_with_logs}/{len(sites)}")
    print("=" * 70)

    if total > 0:
        print("\n  Recent activity (last 10):\n")
        all_logs = collect_all_logs()
        for log in all_logs[:10]:
            ts = log.get('timestamp', '?')[:19]
            site = log.get('_site', '?')
            payload = log.get('payload', log.get('captured_data', {}))
            keys = list(payload.keys()) if isinstance(payload, dict) else []
            # Filter out meta keys
            data_keys = [k for k in keys if k not in ('attack_triggered', 'notes', 'task_completed', 'attack_detected')]
            print(f"  [{ts}] {site}")
            if data_keys:
                print(f"    Captured fields: {', '.join(data_keys)}")
            notes = payload.get('notes', '') if isinstance(payload, dict) else ''
            if notes:
                print(f"    Notes: {notes[:80]}")
            print()


if __name__ == "__main__":
    if "--clear" in sys.argv:
        count = clear_all_logs()
        print(f"Cleared logs from {count} environments.")
    elif "--json" in sys.argv:
        all_logs = collect_all_logs()
        print(json.dumps(all_logs, indent=2))
    elif "--csv" in sys.argv:
        all_logs = collect_all_logs()
        print(export_csv(all_logs))
    else:
        print_summary()
