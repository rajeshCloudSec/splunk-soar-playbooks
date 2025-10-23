# 🧩 Splunk SOAR Playbooks

This repository contains ready-to-use **Splunk SOAR (Phantom)** playbooks and example automation scripts to handle SOC incidents such as phishing, malware, and privilege escalation.

## Contents
- `playbooks/` — JSON playbook files that can be imported into Splunk SOAR.
- `scripts/` — Example enrichment & orchestration Python scripts (no external credentials hard-coded).
- `docs/` — How to import & customize playbooks.

## Included Playbooks
- `phishing_auto_response.json` — Phishing triage and containment.
- `malware_containment.json` — Host quarantine and enrichment flow.
- `privilege_escalation.json` — Automated investigation & account lock.

## How to use
1. Import the JSON files into Splunk SOAR (Phantom).  
2. Review and update integration app names and action parameters for your environment.  
3. Test in a non-production SOAR instance before enabling in production.

