import smtplib
import csv
import time
import os
from email.message import EmailMessage

# 1. CONFIGURATION
SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_16_digit_app_password"
CSV_FILE = "contacts.csv"
RESUME_PATH = "Resume.pdf"

# Set to False when you are ready to actually send emails
DRY_RUN = True  

# 2. EMAIL TEMPLATE
SUBJECT_TEMPLATE = "Research Internship Query: {professor_name} | Visiting Student"

# Keep the {brackets} as they are. The script will replace them. Feel free to use your own template
BODY_TEMPLATE = """Dear Prof. {professor_name},

My name is [Your Name], an undergraduate student at [Your University] with a CGPA of [X.XX]. I am writing to inquire about a research internship in your group.

I have a strong background in {professor_research_field} and I have been following your work on {research_reference}.

I believe my background would allow me to contribute effectively to your ongoing research.

I have attached my resume for your consideration and would welcome the opportunity to discuss a potential project via a brief call.

Best regards,

[Your Name]
[Your Phone Number]
[Link to LinkedIn/Portfolio]
"""

# 3. THE MAILER ENGINE
def send_emails():
    # Check if resume exists
    if not os.path.exists(RESUME_PATH):
        print(f"Error: Could not find {RESUME_PATH}. Please check the filename.")
        return

    try:
        # If not a dry run, connect to the SMTP server
        if not DRY_RUN:
            print("Connecting to SMTP server...")
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD)
            print("Login successful. Starting email sequence...\n")

        with open(CSV_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                prof_name = row['Professor Name'].split()[-1] # Grabs just the last name
                prof_email = row['Email Address']
                research_ref = row['Research Reference']

                # Format the Subject and Body
                subject = SUBJECT_TEMPLATE.format(professor_name=prof_name)
                body = BODY_TEMPLATE.format(
                    professor_name=prof_name, 
                    research_reference=research_ref
                )

                # Create the EmailMessage object
                msg = EmailMessage()
                msg['Subject'] = subject
                msg['From'] = SENDER_EMAIL
                msg['To'] = prof_email
                msg.set_content(body)

                # Attach the Resume
                with open(RESUME_PATH, 'rb') as f:
                    pdf_data = f.read()
                    msg.add_attachment(pdf_data, maintype='application', subtype='pdf', filename=RESUME_PATH)

                # Send or Print
                if DRY_RUN:
                    print("--- DRY RUN ---")
                    print(f"To: {prof_email}")
                    print(f"Subject: {subject}\n")
                    print(body)
                    print("----------------\n")
                else:
                    server.send_message(msg)
                    print(f"Sent: {prof_email} (Prof. {prof_name})")
                    
                    # Sleep to avoid spam filters
                    time.sleep(60) 

    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        if not DRY_RUN:
            server.quit()
            print("Server disconnected. All emails sent.")

if __name__ == "__main__":
    if DRY_RUN:
        print("Starting DRY RUN. No emails will be sent.\n")
    send_emails()
