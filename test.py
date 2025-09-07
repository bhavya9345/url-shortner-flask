# test.py - A script to test all free and direct APIs from pyshorteners.
# This version uses a common variable for the URL.

import pyshorteners

# Create a single Shortener instance.
s = pyshorteners.Shortener()

# Define a common URL to test.
long_url = 'https://gemini.google.com/app/282e0f5a1bc7f388?is_sa=1&is_sa=1&android-min-version=301356232&ios-min-version=322.0&campaign_id=bkws&utm_source=sem&utm_source=google&utm_medium=paid-media&utm_medium=cpc&utm_campaign=bkws&utm_campaign=2024enIN_gemfeb&pt=9008&mt=8&ct=p-growth-sem-bkws&gclsrc=aw.ds&gad_source=1&gad_campaignid=20357620749&gbraid=0AAAAApk5BhnI_h-CDYCWaFw_u_wOdRbY2&gclid=CjwKCAjw2vTFBhAuEiwAFaScwp60kqqPrnMMDAeeRg8R9lKv8Bcu6myiKRgYFBj_bQQ3K-N3fVZ7MRoCHN8QAvD_BwE'
# Git.io requires a GitHub URL, so we'll use a separate variable for that specific test case.
github_url = 'https://github.com/microsoft/vscode'

print("--- Testing all free URL shortening APIs ---")
print(f"Original URL for most tests: {long_url}")
print("Note: If an API fails, it may be due to temporary downtime or bot-detection systems.")
print("---------------------------------------------")

# 1. Chilp.it
# This API may be blocked by Cloudflare, as seen in your traceback.
# The try/except block handles this gracefully.
try:
    print("\n--- Chilp.it ---")
    short_url = s.chilpit.short(long_url)
    print(f"Shortened: {short_url}")
except Exception as e:
    print(f"An error occurred with Chilp.it: {e}")
    print("This API is often blocked due to Cloudflare security.")

# 2. Clck.ru
try:
    print("\n--- Clck.ru ---")
    short_url = s.clckru.short(long_url)
    print(f"Shortened: {short_url}")
except Exception as e:
    print(f"An error occurred with Clck.ru: {e}")

# 3. Da.gd
try:
    print("\n--- Da.gd ---")
    short_url = s.dagd.short(long_url)
    print(f"Shortened: {short_url}")
except Exception as e:
    print(f"An error occurred with Da.gd: {e}")

# 4. Git.io (Note: Only works for GitHub URLs)
try:
    print("\n--- Git.io ---")
    short_url = s.gitio.short(github_url)
    print(f"Original: {github_url}")
    print(f"Shortened: {short_url}")
except Exception as e:
    print(f"An error occurred with Git.io: {e}")
    print("This API only works with valid GitHub URLs.")

# 5. Is.gd
try:
    print("\n--- Is.gd ---")
    short_url = s.isgd.short(long_url)
    print(f"Shortened: {short_url}")
except Exception as e:
    print(f"An error occurred with Is.gd: {e}")

# 6. NullPointer (0x0.st)
try:
    print("\n--- NullPointer (0x0.st) ---")
    short_url = s.nullpointer.short(long_url)
    print(f"Shortened: {short_url}")
except Exception as e:
    print(f"An error occurred with NullPointer: {e}")

# 7. Os.db
try:
    print("\n--- Os.db ---")
    short_url = s.osdb.short(long_url)
    print(f"Shortened: {short_url}")
except Exception as e:
    print(f"An error occurred with Os.db: {e}")

# 8. Ow.ly
try:
    print("\n--- Ow.ly ---")
    short_url = s.owly.short(long_url)
    print(f"Shortened: {short_url}")
except Exception as e:
    print(f"An error occurred with Ow.ly: {e}")

# 9. Qps.ru
try:
    print("\n--- Qps.ru ---")
    short_url = s.qpsru.short(long_url)
    print(f"Shortened: {short_url}")
except Exception as e:
    print(f"An error occurred with Qps.ru: {e}")

# 10. TinyURL.com
try:
    print("\n--- TinyURL.com ---")
    short_url = s.tinyurl.short(long_url)
    print(f"Shortened: {short_url}")
except Exception as e:
    print(f"An error occurred with TinyURL.com: {e}")
