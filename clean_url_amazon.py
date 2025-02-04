import re
import requests
import sys
from urllib.parse import urlparse

# Colored text for terminal output
class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    RESET = "\033[0m"

# Fake User-Agent to bypass Amazon bot protection
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

def banner():
    """Display a fancy banner."""
    print(Colors.HEADER + "=" * 50)
    print(f"{Colors.BLUE}🚀 Amazon URL Cleaner - Terminal Edition 🚀{Colors.RESET}")
    print(Colors.HEADER + "=" * 50)

def get_amazon_url():
    """Prompt the user to enter an Amazon URL and validate it."""
    try:
        while True:
            url = input(f"{Colors.GREEN}🔗 Enter Amazon URL: {Colors.RESET}").strip()

            parsed_url = urlparse(url)
            print(f"{Colors.BLUE}🛠 Debug: Parsed URL -> Scheme: {parsed_url.scheme}, Netloc: {parsed_url.netloc}{Colors.RESET}")

            if not url:
                print(f"{Colors.FAIL}❌ Error: URL cannot be empty!{Colors.RESET}")
                continue

            if not parsed_url.scheme.startswith("http"):
                print(f"{Colors.FAIL}❌ Error: Invalid URL format!{Colors.RESET}")
                continue

            if "amazon." not in parsed_url.netloc:
                print(f"{Colors.FAIL}❌ Error: The URL is not from Amazon!{Colors.RESET}")
                continue
            
            return url
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}⚠️  Process interrupted by user. Exiting... 👋{Colors.RESET}")
        sys.exit(0)

def check_url_exists(url):
    """Check if the given URL is accessible by simulating a real browser."""
    try:
        response = requests.get(url, headers=HEADERS, allow_redirects=True, stream=True, timeout=5)
        print(f"{Colors.BLUE}🛠 Debug: HTTP Status Code: {response.status_code}{Colors.RESET}")
        return response.status_code < 400
    except requests.RequestException as e:
        print(f"{Colors.FAIL}❌ Error checking URL: {e}{Colors.RESET}")
        return False

def clean_amazon_url(url):
    """Clean an Amazon URL by extracting only the essential part with ASIN."""
    asin_match = re.search(r'/([A-Z0-9]{10})(?:[/?]|$)', url)
    
    if asin_match:
        asin = asin_match.group(1)
        parsed_url = urlparse(url)
        return f"https://{parsed_url.netloc}/dp/{asin}"
    
    return None

def main():
    """Main function to execute the URL cleaning process."""
    try:
        banner()
        
        while True:
            url = get_amazon_url()
            
            print(f"{Colors.BLUE}🔍 Checking if the URL exists...{Colors.RESET}")
            if not check_url_exists(url):
                print(f"{Colors.WARNING}⚠ Warning: The URL is not accessible (possible bot protection or incorrect URL). Try another one.{Colors.RESET}")
                continue  # No exit, allow user to enter another URL
            
            cleaned_url = clean_amazon_url(url)

            if cleaned_url:
                print(f"\n{Colors.GREEN}✅ Cleaned Amazon URL: {Colors.RESET}{cleaned_url}\n")
            else:
                print(f"{Colors.FAIL}❌ Error: Could not extract ASIN from the URL!{Colors.RESET}")
            
            break  # Exit loop after successful cleaning
    
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}⚠️  Process interrupted by user. Exiting... 👋{Colors.RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()
