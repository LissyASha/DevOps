import boto3
import json
import os

sns_client = boto3.client('sns')

# Replace with your SNS Topic ARN
SNS_TOPIC_ARN = "arn:aws:sns:ca-central-1:975050024946:EC2StateChangeTopic-Lissy"

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))

    # Extract EC2 instance details from EventBridge event
    detail = event['detail']
    instance_id = detail['instance-id']
    state = detail['state']

    # Create message
    message = f"EC2 Instance {instance_id} has changed state to: {state}"
    subject = f"EC2 State Change: {instance_id} → {state}"

    # Send notification
    sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject=subject
    )

    print(f"Notification sent: {message}")

    return {
        "statusCode": 200,
        "body": json.dumps({"message": message})
    }
