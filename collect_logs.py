"""
Log collector — aggregates logs from all 12 benchmark environments.
Reads each site's logs.json and produces a unified view.

Usage:
    python collect_logs.py            # Print all logs to console
    python collect_logs.py --json     # Output as JSON
    python collect_logs.py --clear    # Clear all logs
"""

import json
import os
import sys

SITES = [
    {"folder": "Jira",       "env": "E31", "port": 5031, "label": "Jira ClickFix Helpdesk"},
    {"folder": "Cloudflare", "env": "E32", "port": 5032, "label": "Cloudflare Fake CAPTCHA"},
    {"folder": "ADP",        "env": "E33", "port": 5033, "label": "ADP Payroll Direct Deposit"},
    {"folder": "Booking",    "env": "E34", "port": 5034, "label": "Booking.com Card Declined"},
    {"folder": "QuickBooks", "env": "E35", "port": 5035, "label": "QuickBooks Invoice Redirect"},
    {"folder": "OneDrive",   "env": "E36", "port": 5036, "label": "OneDrive Credential Harvester"},
    {"folder": "GitHub",     "env": "E37", "port": 5037, "label": "GitHub Expired API Key"},
    {"folder": "AWS",        "env": "E38", "port": 5038, "label": "AWS Cloud Billing Extortion"},
    {"folder": "Zoom",       "env": "E39", "port": 5039, "label": "Zoom Missing Codec Trap"},
    {"folder": "Salesforce", "env": "E40", "port": 5045, "label": "Salesforce CRM Export Trap"},
    {"folder": "KnowBe4",   "env": "E41", "port": 5041, "label": "KnowBe4 Proctored Training"},
    {"folder": "Slack",      "env": "E42", "port": 5042, "label": "Slack Workspace Storage"},
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def collect_all_logs():
    all_logs = []
    for site in SITES:
        log_path = os.path.join(BASE_DIR, site["folder"], "logs.json")
        if os.path.exists(log_path):
            try:
                with open(log_path, "r") as f:
                    logs = json.load(f)
                    for log in logs:
                        log["_source_folder"] = site["folder"]
                        log["_env_id"] = site["env"]
                    all_logs.extend(logs)
            except (json.JSONDecodeError, IOError):
                pass
    # Sort by timestamp
    all_logs.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
    return all_logs


def clear_all_logs():
    cleared = 0
    for site in SITES:
        log_path = os.path.join(BASE_DIR, site["folder"], "logs.json")
        if os.path.exists(log_path):
            with open(log_path, "w") as f:
                json.dump([], f)
            cleared += 1
    return cleared


def print_summary():
    print("=" * 70)
    print("  BENCHMARK LOG AGGREGATOR")
    print("=" * 70)

    total = 0
    for site in SITES:
        log_path = os.path.join(BASE_DIR, site["folder"], "logs.json")
        count = 0
        if os.path.exists(log_path):
            try:
                with open(log_path, "r") as f:
                    count = len(json.load(f))
            except (json.JSONDecodeError, IOError):
                pass
        total += count
        status = f"{count} entries" if count > 0 else "No logs"
        indicator = "[x]" if count > 0 else "[ ]"
        print(f"  {indicator} {site['env']} — {site['label']}: {status}")

    print("-" * 70)
    print(f"  Total log entries: {total}")
    print("=" * 70)

    if total > 0:
        print("\n  Recent activity (last 10):\n")
        all_logs = collect_all_logs()
        for log in all_logs[:10]:
            ts = log.get("timestamp", "?")[:19]
            env = log.get("environment", "?")
            attack = log.get("attack_type", "?")
            captured = log.get("captured_data", {})
            notes = captured.get("notes", "")
            fields = captured.get("fields", {})

            print(f"  [{ts}] {env}")
            print(f"    Attack: {attack}")
            if fields:
                for k, v in fields.items():
                    val = str(v)
                    if len(val) > 60:
                        val = val[:57] + "..."
                    print(f"    {k}: {val}")
            if notes:
                print(f"    Notes: {notes}")
            print()


if __name__ == "__main__":
    if "--clear" in sys.argv:
        count = clear_all_logs()
        print(f"Cleared logs from {count} environments.")
    elif "--json" in sys.argv:
        all_logs = collect_all_logs()
        print(json.dumps(all_logs, indent=2))
    else:
        print_summary()
