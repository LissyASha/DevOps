import boto3
import json
from datetime import datetime, timezone, timedelta

# Initialize the S3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Change this to your bucket name
    bucket_name = "lissys3bucket"

    # Calculate the cutoff date (30 days ago)
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=30)

    deleted_files = []

    # List objects in the bucket
    response = s3_client.list_objects_v2(Bucket=bucket_name)

    if 'Contents' in response:
        for obj in response['Contents']:
            key = obj['Key']
            last_modified = obj['LastModified']

            # Check if object is older than 30 days
            if last_modified < cutoff_date:
                # Delete the object
                s3_client.delete_object(Bucket=bucket_name, Key=key)
                deleted_files.append(key)
                print(f"Deleted: {key}")

    else:
        print("No objects found in the bucket.")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "DeletedFiles": deleted_files,
            "Count": len(deleted_files)
        })
    }
