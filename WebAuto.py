import webbrowser as wb

def webauto():
    chrome_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe'

    URLS=(
        "youtube.com",
        "gmail.com",
        "google.com",
        "udemy.com",
    )
    wb.register('chrome', chrome_path)  # Register Chrome browser
    chrome = wb.get('chrome')  # Get the registered browser

    for url in URLS:
        print("opening:"+url)
        chrome.open(url)  # Use the registered browser to open the URL


webauto()
