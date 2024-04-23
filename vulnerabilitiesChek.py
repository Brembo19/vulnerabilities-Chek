import os
import requests
from bs4 import BeautifulSoup

# Function to check for vulnerabilities in a given URL
def check_vulnerabilities(url):
    # You can implement your own vulnerability checks here
    # For simplicity, let's just check if the page contains the word "vulnerable"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        if "vulnerable" in soup.get_text().lower():
            save_vulnerability(url, "Vulnerable")
        else:
            save_ok_link(url)
            print(f"{url} is OK")
    except requests.RequestException as e:
        print(f"Error checking {url}: {str(e)}")

# Function to save a vulnerability to a text document
def save_vulnerability(url, vulnerability):
    with open("results/vulnerabilities.txt", "a") as file:
        file.write(f"Link: {url}\nVulnerability: {vulnerability}\n\n")

# Function to save an OK link to a file within the results folder
def save_ok_link(url):
    ok_links_file = "results/ok_links.txt"
    with open(ok_links_file, "a") as file:
        file.write(url + "\n")

# Main function
def main():
    if not os.path.exists("results"):
        os.makedirs("results")
    
    # Write additional information to the result file
    with open("results/vulnerabilities.txt", "w") as result_file:
        result_file.write("https://t.me/TeamLionPrivate % Hats Team  \n\n")
    
    link_document = input("Please enter the name of the link document: ")
    try:
        with open(link_document, "r") as file:
            links = file.readlines()
            links = [link.strip() for link in links]
    except FileNotFoundError:
        print("File not found.")
        return

    print("Checking links:")
    for link in links:
        print(f"Checking {link}...")
        check_vulnerabilities(link)

    print("\nVulnerabilities checked. Results saved to 'results/vulnerabilities.txt'.")

if __name__ == "__main__":
    main()
