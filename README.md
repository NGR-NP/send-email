# Certificate Email Sender

## Why This Script Exists

After organizing a 7-day JavaScript workshop in collaboration with Digital Pathshala by Code for Change - Koshi, sending certificates to all participants became a hassle. We had a CSV list of attendees and used Canva’s bulk create feature to generate certificates, naming each file after the student’s email. To streamline the process, I used AI tools to create a personalized email template and wrote this script. It automatically matches each student’s email in the CSV to their certificate file and sends a personalized email with their certificate attached.

## Project Structure

```
README.md
send_certificates.py
students.csv
template.html
certificates/
    student1@example.com.png
    student2@example.com.png
```

- **send_certificates.py**: Main script for sending emails with certificates.
- **students.csv**: List of participants (`name,email`).
- **template.html**: HTML email template (uses `{name}` for personalization).
- **certificates/**: Certificate images named as `<email>.png`.

## How It Works

1. Reads participant info from `students.csv`.
2. Personalizes the email template for each recipient.
3. Checks if a certificate file exists for each email.
4. Sends the email with the certificate attached via Gmail SMTP.

## Usage

1. **Configure Email Credentials**
   - Edit `send_certificates.py` and set your Gmail address and app password:
     ```python
     EMAIL = "your_email@gmail.com"
     PASSWORD = "your_app_password"
     ```

2. **Prepare Certificates**
   - Place certificate images in the `certificates/` folder, named as each participant's email (e.g., `john@example.com.png`).

3. **Edit Participants List**
   - Update `students.csv` with participant names and emails.

4. **Customize Email Template**
   - Edit `template.html` as needed. Use `{name}` for personalization.

5. **Run the Script**
   ```
   python send_certificates.py
   ```

## Requirements

- Python 3.x
- Internet connection
- Gmail account with [App Password](https://support.google.com/accounts/answer/185833)

## Troubleshooting

- Ensure certificate files exist for each email.
- Use a valid Gmail App Password.
- Check for typos in `students.csv`.

##