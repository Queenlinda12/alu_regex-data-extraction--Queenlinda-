# Regex Extractor Script

## Description

This is a Python script that uses regular expressions (regex) to extract common data types from text. It’s designed to help identify structured information in large or messy blocks of text.

---

## Features

The script extracts the following:

- Email addresses (e.g. `user@example.com`)
- URLs (e.g. `https://www.example.com`)
- Phone numbers (e.g. `(123) 456-7890`, `123-456-7890`)
- Credit card numbers (e.g. `1234-5678-9012-3456`)
- Time formats (e.g. `14:30`, `2:30 PM`)
- Currency amounts  (e.g. `$1,234.56`)

---

## How to Use

1. Make sure you have Python installed on your computer.
2. Open the terminal or command prompt in the folder containing `regex_extractor.py`.
3. Run the script using:

```bash
python regex_extractor.py
