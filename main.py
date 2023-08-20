import requests, re, time
from urllib.parse import urlparse, parse_qs
from solveCaptcha import solveCaptcha
from gen_random import *

twocaptcha_key = ""
blockedDomains = ["qiott.com", "kzccv.com"]

def contains_blocked_domain(email, blocked_domains):
    for domain in blocked_domains:
        if domain in email:
            return True
    return False


def gen():
    emailrequest = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox", headers={"accept": "application/json"})

    email = str(emailrequest.json()[0])

    if contains_blocked_domain(email, blockedDomains):
        print("Email contains a blocked domain.")
        return
    else:
        print("Email does not contain blocked domains.")

    captcha = solveCaptcha(api_key=twocaptcha_key, site_key="4c672d35-0701-42b2-88c3-78380b0db560", url="https://www.discord.com/register")

    standard_headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://discord.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.51',
        'X-Track': 'eyJvcyI6IklPUyIsImJyb3dzZXIiOiJTYWZlIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKElQaG9uZTsgQ1BVIEludGVybmFsIFByb2R1Y3RzIFN0b3JlLCBhcHBsaWNhdGlvbi8yMDUuMS4xNSAoS0hUTUwpIFZlcnNpb24vMTUuMCBNb2JpbGUvMTVFMjQ4IFNhZmFyaS82MDQuMSIsImJyb3dzZXJfdmVyc2lvbiI6IjE1LjAiLCJvc192IjoiIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfZG9tYWluX2Nvb2tpZSI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOiJzdGFibGUiLCJjbGllbnRfZXZlbnRfc291cmNlIjoic3RhYmxlIn0',
    }

    response = requests.get('https://discord.com/api/v9/experiments', headers=standard_headers)
    if response.status_code == 200:
        data = response.json()
        fingerprint = data["fingerprint"]

    headers ={
        "authority": "discord.com",
        "method": "POST",
        "path": "/api/v9/auth/register",
        "scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "Content-Length": "316",
        "Content-Type": "application/json",
        "Origin": "https://discord.com",
        "Referer": "https://discord.com/register",
        "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "X-Captcha-Key": f"{captcha}",
        "X-Debug-Options": "bugReporterEnabled",
        "X-Discord-Locale": "de",
        "X-Discord-Timezone": "Europe/Berlin",
        "X-Fingerprint": f"{fingerprint}",
        "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlLURFIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE1LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmVfY3VycmVudCI6Imdvb2dsZSIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjIyMDI0NywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }

    username = random_username()
    global_username = username
    password = random_password(12)
    new_password = random_password(12)
    birthdate = random_geburtsdatum()

    ##################
    payload = {
        "fingerprint": f"{fingerprint}",
        "email": f"{email}",
        "username": f"{username}",
        "global_name": f"{global_username}",
        "password": f"{password}",
        "invite": None,
        "consent": True,
        "date_of_birth": f"{birthdate}",
        "gift_code_sku_id": None,
        "unique_username_registration": True
    }

    register = requests.post("https://discord.com/api/v9/auth/register", headers=headers, json=payload)
    print(register.status_code)
    print(register.text)

    if register.status_code == 201:
        # verify email
        login = email.split("@")[0]
        domain = email.split("@")[1]
        while True:
            verifyrequest = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}", headers={"accept": "application/json"})

            data = verifyrequest.json()

            target_subject = "Discord-Account aufgrund verdächtiger Aktivitäten deaktiviert"
            verify_subject = "Verifiziere deine E-Mail-Adresse für Discord"

            email_id = None

            for email__ in data:
                if email__["subject"] == target_subject:
                    email_id = email__["id"]
                    break

            if email_id is not None:
                print(f"Email ID: {email_id}")
            else:
                for email__ in data:
                    if email__["subject"] == verify_subject:
                        email_id = email__["id"]
                        break
                if email_id is not None:
                    print(f"Verify Email ID: {email_id}")
                else:
                    print("No matching emails found.")

            if email_id is not None:
                getEmailHTML1 = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={email_id}", headers={"accept": "application/json"})

                getEmailVerifyLink = getEmailHTML1.json()['textBody']

                # Regular expression to match URLs
                url_pattern = re.compile(r'https?://\S+')

                # Find all URLs in the text
                urls = re.findall(url_pattern, getEmailVerifyLink)

                if urls:
                    last_url = urls[-1]
                    print(last_url)
                else:
                    print("No URLs found in the text.")

                reset_pass = requests.get(last_url, headers=standard_headers, allow_redirects=True)
                print("Final URL after redirects:", reset_pass.url)

                parsed_url = urlparse(reset_pass.url)
                fragment = parsed_url.fragment

                token = parse_qs(fragment).get('token')

                if token:
                    print("Extracted Token:", token[0])
                else:
                    print("Token not found in URL.")

                payloadResetPW = {
                    "token": f"{token[0]}",
                    "password": f"{new_password}",
                    "source": "/reset"
                }
                print(token[0])

                resetPW = requests.post("https://discord.com/api/v9/auth/reset", headers=standard_headers, json=payloadResetPW)
                print(resetPW.status_code)
                if resetPW.status_code == 200:
                    print(resetPW.json()['token'])
                    with open("genned.txt", "a+") as file:
                        file.write(f"{email}:{new_password}:{resetPW.json()['token']}")
                    break
                else:
                    print(resetPW.text)
            time.sleep(1)
    elif register.status_code == 429:
        print("ratelimit")
    else:
        print("idk")

while True:
    gen()
