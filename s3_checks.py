import boto3

def check_s3_public_access():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']

    findings = []

    for bucket in buckets:
        bucket_name = bucket['Name']
        result = s3.get_bucket_acl(Bucket=bucket_name)
        grants = result['Grants']

        for grant in grants:
            if grant['Grantee']['Type'] == 'Group' and 'AllUsers' in grant['Grantee']['URI']:
                findings.append(f"S3 bucket {bucket_name} has public access.")
    
    if findings:
        return findings
    else:
        return ["No public S3 buckets found."]

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

if __name__ == "__main__":
    public_access_findings = check_s3_public_access()
    encryption_findings = check_s3_encryption()

    # Combine findings for output
    all_findings = public_access_findings + encryption_findings
    for finding in all_findings:
        print(finding)







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
