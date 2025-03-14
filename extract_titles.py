import requests
from bs4 import BeautifulSoup

def extract_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.find("title").text.strip()
        return title
    except Exception as e:
        return f"Error: {e}"

def main():
    urls = [
    "https://www.example.com",
    "https://www.iana.org/domains/example",
    "https://www.python.org"  # Added URL
]


    results = []
    for url in urls:
        title = extract_title(url)
        results.append(f"{title} - {url}")
        print(f"{title} - {url}")

    # Save results to a file
    with open("titles.txt", "w") as f:
        for result in results:
            f.write(result + "\n")

if __name__ == "__main__":
    main()

