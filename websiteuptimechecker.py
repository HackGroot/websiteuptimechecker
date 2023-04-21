import requests
import time

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

if __name__ == "__main__":
    website_url = input("Enter the website URL to monitor: ")
    monitoring_interval = 60  # Set the monitoring interval in seconds

    while True:
        if check_website(website_url):
            print(f"{website_url} is up")
        else:
            print(f"{website_url} is down")

        time.sleep(monitoring_interval)
