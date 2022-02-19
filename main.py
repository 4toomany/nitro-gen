import requests
import random
import string
import time

sec = 1

while True:
    print("[SCRIPT] Starting section " + str(sec) + "...")
    with open("goodies.txt", "w", encoding='utf-8') as file:
        print("[SCRIPT] Generating codes...")

        while True:
            # generation algorithm
            code = "".join(random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase,
                k = 16
            ))

            nitro = "https://discord.gift/" + str(code)

            url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
            print("[SCRIPT] Checking code...")

            r = requests.get(url)

            if r.status_code == 200:
                print("[SCRIPT] Valid code found...")
                file.write(str(nitro) + "\n")
                break
            else:
                print("[SCRIPT] Invalid code found; passing...")
                pass
