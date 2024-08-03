import requests
from tabulate import tabulate
import time

# List of subdomains to check
subdomains = [
    "http://www.google.com",
    "http://www.youtube.com",
    "http://www.amazonindia.com",
    "http://www.amazon.in",
    "http://www.youtubeindia.com"
]

def check_status(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        return False

def main():
    while True:
        status_table = []
        for subdomain in subdomains:
            status = "Up" if check_status(subdomain) else "Down"
            status_table.append([subdomain, status])
        
        # Clear the screen before updating the table
        print("\033c", end="")
        
        # Print the status table
        print(tabulate(status_table, headers=["Subdomain", "Status"], tablefmt="grid"))

        # Wait for a minute before checking again
        print ("\nUpdating Status in next 60 seconds...\n")
        time.sleep(60)

if __name__ == "__main__":
    main()