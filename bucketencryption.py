import boto3

def check_s3_encryption():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']

    findings = []

    for bucket in buckets:
        try:
            result = s3.get_bucket_encryption(Bucket=bucket['Name'])
            rules = result['ServerSideEncryptionConfiguration']['Rules']
            if rules:
                findings.append(f"S3 bucket {bucket['Name']} is encrypted.")
        except s3.exceptions.ClientError:
            findings.append(f"S3 bucket {bucket['Name']} is not encrypted.")
    
    return findings

