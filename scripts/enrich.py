#!/usr/bin/env python3
"""Example enrichment helper for SOAR playbooks.
This script demonstrates how you might enrich indicators using public APIs.
Do NOT run against production without configuring API keys and handling secrets securely.
"""
import sys
def enrich(indicator):
    # Mock enrichment - replace with real API calls in production
    return {
        "indicator": indicator,
        "malicious": False,
        "confidence": 20,
        "sources": ["mock-enrich"]
    }

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: enrich.py <indicator>")
        sys.exit(1)
    result = enrich(sys.argv[1])
    print(result)
