"""
Master launcher for all 12 benchmark environments.
Starts each Flask server in a separate subprocess on its own port.

Usage:
    python launch_all.py          # Start all servers
    python launch_all.py --stop   # Stop all servers
"""

import subprocess
import sys
import os
import time
import signal

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
    {"folder": "Salesforce", "env": "E40", "port": 5040, "label": "Salesforce CRM Export Trap"},
    {"folder": "KnowBe4",   "env": "E41", "port": 5041, "label": "KnowBe4 Proctored Training"},
    {"folder": "Slack",      "env": "E42", "port": 5042, "label": "Slack Workspace Storage"},
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def launch_all():
    processes = []
    print("=" * 70)
    print("  BENCHMARK ENVIRONMENT LAUNCHER")
    print("  Starting 12 social engineering benchmark servers...")
    print("=" * 70)

    for site in SITES:
        server_path = os.path.join(BASE_DIR, site["folder"], "server.py")
        if not os.path.exists(server_path):
            print(f"  [SKIP] {site['env']} — {site['label']} (server.py not found)")
            continue

        proc = subprocess.Popen(
            [sys.executable, server_path],
            cwd=os.path.join(BASE_DIR, site["folder"]),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        processes.append(proc)
        print(f"  [OK]   {site['env']} — {site['label']}")
        print(f"         http://localhost:{site['port']}")
        print(f"         Logs: http://localhost:{site['port']}/api/logs")

    print()
    print("=" * 70)
    print(f"  All {len(processes)} servers started successfully!")
    print(f"  View aggregated logs: python collect_logs.py")
    print("=" * 70)
    print()
    print("  Press Ctrl+C to stop all servers...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n  Stopping all servers...")
        for proc in processes:
            proc.terminate()
        for proc in processes:
            proc.wait(timeout=5)
        print("  All servers stopped.")


if __name__ == "__main__":
    launch_all()
