# TED Talk Search Automation

Selenium script that searches TED Talks for a user-entered topic and opens a result in Chrome.

## Quickstart
Requirements: Python 3, Chrome, ChromeDriver (version must match Chrome), Selenium

Install:
pip install selenium

Run:
python main.py

ChromeDriver:
- Put `chromedriver` / `chromedriver.exe` on PATH, or set the driver path in `main.py` (the `PATH = "..."` line).

Notes:
- Start URL should be `https://www.ted.com/talks` (fix it if yours is malformed).
- TED's DOM/class names change; if you get `NoSuchElementException`, update the `By.NAME` / `By.CLASS_NAME` selectors.
- `time.sleep` is fragile; prefer `WebDriverWait` for real use.

Files: `main.py`
