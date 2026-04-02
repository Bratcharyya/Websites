"""
Master launcher for all benchmark environments.
Dynamically discovers every site folder with a server.py and launches it.

Usage:
    python launch_all.py          # Start all servers
"""

import subprocess
import sys
import os
import time
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SKIP = {'.git', '__pycache__', 'Scammer4U', 'node_modules', '.claude'}


def discover_sites():
    """Scan for all subdirectories containing a server.py and extract their port."""
    sites = []
    for name in sorted(os.listdir(BASE_DIR)):
        if name in SKIP or name.startswith('.'):
            continue
        folder = os.path.join(BASE_DIR, name)
        server = os.path.join(folder, 'server.py')
        if os.path.isdir(folder) and os.path.isfile(server):
            try:
                with open(server, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                m = re.search(r'port\s*=\s*(\d{4,5})', content)
                port = int(m.group(1)) if m else None
                if port:
                    sites.append({'folder': name, 'port': port})
            except Exception:
                pass
    return sites


def launch_all():
    sites = discover_sites()
    processes = []
    print("=" * 70)
    print("  BENCHMARK ENVIRONMENT LAUNCHER")
    print(f"  Discovered {len(sites)} environments with server.py")
    print("=" * 70)

    for site in sites:
        server_path = os.path.join(BASE_DIR, site['folder'], 'server.py')
        proc = subprocess.Popen(
            [sys.executable, server_path],
            cwd=os.path.join(BASE_DIR, site['folder']),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        processes.append(proc)
        print(f"  [OK]   {site['folder']:<20} http://localhost:{site['port']}")

    print()
    print("=" * 70)
    print(f"  All {len(processes)} servers launched.")
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
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
        print("  All servers stopped.")


if __name__ == "__main__":
    launch_all()
