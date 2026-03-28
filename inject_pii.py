import json
import requests
import time
import os

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

def load_pii():
    pii_path = os.path.join("d:\\Websites", "Scammer4U", "agent", "config", "user_profile.json")
    with open(pii_path, "r") as f:
        return json.load(f)

def flatten_pii(pii_data):
    flat = {}
    for category, details in pii_data.items():
        if isinstance(details, dict):
            for k, v in details.items():
                flat[k] = v
        else:
            flat[category] = details
    return flat

def inject():
    pii = load_pii()
    flat_pii = flatten_pii(pii)
    # Give the servers a few seconds to start up if we just launched launch_all.py
    time.sleep(3)
    
    for site in SITES:
        url = f"http://localhost:{site['port']}/api/log"
        payload = {"attack_type": "injected_pii", **flat_pii}
        
        try:
            resp = requests.post(url, json=payload, timeout=5)
            if resp.status_code == 200:
                print(f"[OK] {site['label']} on port {site['port']}")
            else:
                print(f"[ERROR] {site['label']} returned {resp.status_code}")
        except Exception as e:
            print(f"[FAIL] {site['label']} connection failed: {e}")

if __name__ == "__main__":
    inject()
