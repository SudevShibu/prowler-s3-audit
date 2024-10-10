# S3 Bucket Audit Project

This project audits S3 buckets for public access and encryption status.

## Checks Performed
- Checks if S3 buckets have public access.
- Checks if S3 buckets are encrypted.

## Requirements
- Python 3.10 or higher
- Boto3 library

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/SudevShibu/prowler-s3-audit.git
2. Navigate into the directory:
   cd prowler-s3-audit
3. Install the required libraries:
   poetry install

  ## Running the Audit
To run the audit, execute the following command:
python s3_checks.py
