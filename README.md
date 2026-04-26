# Random-Scripts
Scripts I wrote to automate the boring and the fun stuff

## 1. Email Outreach Automation Script

Simple Python script to send personalized emails using a CSV file and a template. Useful for structured outreach such as internship or research applications.

### Setup

1. **Update your details in the script:**
   - `SENDER_EMAIL` → your email  
   - `APP_PASSWORD` → your email app password  
   - `CSV_FILE` → path to your contacts file  
   - `RESUME_PATH` → path to your resume PDF  

2. **Prepare your contacts.csv file**

Example format:

Name,Email Address,Research Reference  
John Doe,john@example.com,his work on XYZ  

3. **Edit the email template**

- Modify `SUBJECT_TEMPLATE` and `BODY_TEMPLATE`  
- Keep placeholders like `{professor_name}` and `{research_reference}`  

---

### Usage

1. Run the script in dry mode (recommended first):

  `DRY_RUN = True`

  This will print the emails instead of sending them.

2. Check the output and make sure everything looks correct.
3. When ready, enable sending:

  `DRY_RUN = False`

4. Run the script again to send emails.

### Notes

* Emails are sent one by one with a delay to avoid spam filters
* Works with Gmail SMTP (App Password required)
* Make sure your CSV column names match the script
