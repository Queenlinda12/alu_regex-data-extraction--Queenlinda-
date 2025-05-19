import re

# Sample text to test all patterns
sample_text = """
Contact: user@example.com, firstname.lastname@company.co.uk
Visit: https://www.example.com, https://subdomain.example.org/page
Call: (123) 456-7890, 123-456-7890, 123.456.7890
Cards: 1234 5678 9012 3456, 1234-5678-9012-3456
Times: 14:30, 2:30 PM
Tags: <p>, <div class="example">, <img src="image.jpg" alt="desc">
Hashtags: #example, #ThisIsAHashtag
Prices: $19.99, $1,234.56
"""

# Define all required regex patterns
patterns = {
    " Email Addresses": r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
    " URLs": r"https?://[^\s<>\"']+",
    " Phone Numbers": r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}",
    " Credit Card Numbers": r"\b(?:\d{4}[- ]?){3}\d{4}\b",
    " Time Formats": r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APMapm]{2})?\b",
    " Currency Amounts": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?",
}

# Run and print matches for each pattern
for label, pattern in patterns.items():
    matches = re.findall(pattern, sample_text)
    print(f"{label}:\n  {matches}\n")
