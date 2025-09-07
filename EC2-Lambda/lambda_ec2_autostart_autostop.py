import json
import boto3

# Create EC2 client
ec2_client = boto3.client('ec2', region_name='ca-central-1')  # Change region if needed

def lambda_handler(event, context):
    # Filter for instances with Auto-Stop or Auto-Start tags
    filters = [
        {
            'Name': 'tag:Action',
            'Values': ['Auto-Start', 'Auto-Stop']
        }
    ]

    response = ec2_client.describe_instances(Filters=filters)
    affected_instances = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}

            # If instance has Auto-Start tag and is stopped → start it
            if tags.get("Action") == "Auto-Start" and state == "stopped":
                print(f"Starting instance {instance_id}...")
                ec2_client.start_instances(InstanceIds=[instance_id])
                affected_instances.append({"InstanceId": instance_id, "ActionTaken": "Started"})

            # If instance has Auto-Stop tag and is running → stop it
            elif tags.get("Action") == "Auto-Stop" and state == "running":
                print(f"Stopping instance {instance_id}...")
                ec2_client.stop_instances(InstanceIds=[instance_id])
                affected_instances.append({"InstanceId": instance_id, "ActionTaken": "Stopped"})

    # Print/log affected instances
    if affected_instances:
        print("Affected Instances:")
        for entry in affected_instances:
            print(f"- {entry['InstanceId']} ({entry['ActionTaken']})")
    else:
        print("No instances required action.")

    return {
        "statusCode": 200,
        "body": json.dumps(affected_instances)
    }
