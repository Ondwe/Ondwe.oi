# Web Title Extractor

This Python script extracts the title and URL from a list of websites.

## Description

This project provides a simple yet effective way to retrieve the titles of web pages. It's built using Python's `requests` and `Beautiful Soup` libraries, making it easy to fetch and parse HTML content.

## Features

-   Extracts titles and URLs from a list of websites.
-   Handles potential errors during the extraction process.
-   Displays the results in a clear and organized format.
-   Uses a `noreply` email for committing to GitHub to protect privacy.

## Getting Started

### Prerequisites

-   Python 3.x
-   `requests` library (`pip install requests`)
-   `beautifulsoup4` library (`pip install beautifulsoup4`)

### Installation

1.  Clone the repository:

    ```bash
    git clone [https://github.com/Ondwe/Ondwe.oi.git](https://github.com/Ondwe/Ondwe.oi.git)
    cd Ondwe.oi
    ```

2.  Install the required libraries:

    ```bash
    pip install requests beautifulsoup4
    ```

### Usage

1.  Place the URLs you want to extract titles from in the `urls` list within the `extract_titles.py` script.
2.  Run the script:

    ```bash
    python extract_titles.py
    ```

3.  The script will display the titles and URLs of the websites.

## Example

```python
urls = [
    "[https://www.example.com](https://www.example.com)",
    "[https://www.iana.org/domains/example](https://www.iana.org/domains/example)",
    "[https://www.python.org](https://www.python.org)"
]

Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue to suggest improvements.
Author
 * Humbulani - Located in Thohoyandou, Limpopo, South Africa
 * Email: getfriendhumbulani30@gmail.com
License
MIT License
Copyright (c) 2024 Humbulani
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Acknowledgments
 * Thanks to the Python community for providing excellent libraries.
 * Special thanks to the open-source contributors who made this project possible.
Contact
 * Email: getfriendhumbulani30@gmail.com

**Explanation of Changes:**

* **Author Section:** Your name, location, and email are added.
* **License Section:**
    * The license is specified as "MIT License."
    * The copyright notice is added with your name and the current year.
    * The full MIT License text is included, ensuring it's clearly stated within your `README.md`.

**To use this `README.md`:**

1.  **Copy the content above.**
2.  **Replace the existing `README.md` in your repository** with this new content.
3.  **Commit and push** the changes to your GitHub repository.

Now your repository has a clear license and your information included.

