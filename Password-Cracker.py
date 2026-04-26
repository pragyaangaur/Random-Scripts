import pikepdf
import itertools
import string
import time

def brute_force_pdf(pdf_path):
    # Define the character set: lowercase, uppercase, digits, and punctuation
    chars = string.ascii_letters + string.digits + string.punctuation
    # You can limit this to just string.ascii_lowercase if you know the password is simple
    
    attempts = 0
    start_time = time.time()

    print(f"Starting pure brute-force on {pdf_path}...")
    
    # Try passwords of increasing length (from 1 to 8 characters)
    for length in range(1, 9):
        print(f"Testing passwords of length: {length}")
        
        for guess in itertools.product(chars, repeat=length):
            password = "".join(guess)
            attempts += 1
            
            try:
                with pikepdf.open(pdf_path, password=password) as pdf:
                    end_time = time.time()
                    print(f"\n[+] Success! Password found: {password}")
                    print(f"[+] Total attempts: {attempts}")
                    print(f"[+] Time taken: {round(end_time - start_time, 2)} seconds")
                    
                    pdf.save(f"unlocked_{pdf_path}")
                    return
            except pikepdf.PasswordError:
                continue
            
            # Print a status update every 1000 attempts
            if attempts % 1000 == 0:
                print(f"Attempts: {attempts} | Current guess: {password}", end="\r")

if __name__ == "__main__":
    TARGET_PDF = "target.pdf"
    brute_force_pdf(TARGET_PDF)
