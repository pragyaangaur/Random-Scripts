# Random-Scripts
Scripts I wrote to automate the boring and the fun stuff

## 1. Email Outreach Automation

Simple Python script to send personalized emails using a CSV file and a template. Useful for structured outreach such as internship or research applications.

### Setup

1. **Update your details in the script:**
   - `SENDER_EMAIL` → your email  
   - `APP_PASSWORD` → your email app password  
   - `CSV_FILE` → path to your contacts file  
   - `RESUME_PATH` → path to your resume PDF  

2. **Prepare your contacts.csv file**

Example format:

```csv

Professor Name,Email Address,Research Reference

John Doe,john@example.com,his work on XYZ
```

3. **Edit the email template**

- Modify `SUBJECT_TEMPLATE` and `BODY_TEMPLATE`  
- Keep placeholders like `{professor_name}` and `{research_reference}`  

### Usage

1. Run the script in dry mode (recommended first):
```python
  DRY_RUN = True
```

  This will print the emails instead of sending them.

2. Check the output and make sure everything looks correct.
3. When ready, enable sending:

```python
  DRY_RUN = False
```
4. Run the script again to send emails.

### Notes

* Emails are sent one by one with a delay to avoid spam filters
* Works with Gmail SMTP (App Password required)
* Make sure your CSV column names match the script


## 2. PDF Password Cracker

Simple Python script that attempts to recover the password of a protected PDF using brute-force search.

Primarily intended for:
- CTF challenges  
- learning about password security  
- testing weak passwords on your own files  

### Requirements

```bash
pip install pikepdf
```

### Setup

1. Place your target PDF in the same folder  
2. Update the file name in the script:

```python
TARGET_PDF = "target.pdf"
```  

## Notes

- This is a pure brute-force approach and can be very slow  
- Time required increases exponentially with password length  
- Works best for short or simple passwords  
- Character set can be reduced (e.g., only lowercase) to speed up search

### Faster Approach

For significantly faster cracking, extract the hash and use optimized tools:

```bash

pdf2john target.pdf > hash.txt

hashcat -m 10500 hash.txt wordlist.txt

```

Tools like Hashcat use GPU acceleration and are much more efficient than pure Python brute force.
