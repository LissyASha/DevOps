# DevOps
# DevOps Assignments
****Assignment1- Automated Instance Management Using AWS Lambda and Boto3****
**Steps:**

**Created an Ec2 Instance with tag Name: Action, Value: Auto-Start**

  <img width="452" height="254" alt="Ec2 Instance1_AutoStart" src="https://github.com/user-attachments/assets/c54fdb16-bf93-4f58-a2e2-ae114a3453a8" />

**Created an Ec2 Instance with tag Name: Action, Value: Auto-Stop**

  <img width="452" height="254" alt="Ec2 Instance1_AutoStop" src="https://github.com/user-attachments/assets/3a32cdcc-e76d-47e1-bf20-d2636f54afe0" />

**Create a new I AM role for Lambda**
   - Attached the AmazonEC2FullAccess` policy to this role.

  <img width="452" height="254" alt="IAM Role_Lambda" src="https://github.com/user-attachments/assets/5eaf9565-eea0-4571-8fc1-7bbf9c04350a" />

**Create a Lambda Function with necessary permissions to describe, stop, and start EC2 instances.**

  <img width="452" height="254" alt="Lambda_Funtion " src="https://github.com/user-attachments/assets/e5b7a9ef-4b5b-470a-84c6-f1cbab855877" />

  
**Python Code With Ouput**

import json
import boto3
--Create EC2 client
ec2_client = boto3.client('ec2', region_name='ca-central-1')  # Change region if needed
def lambda_handler(event, context):
    --Filter for instances with Auto-Stop or Auto-Start tags
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

            --If instance has Auto-Start tag and is stopped → start it
            if tags.get("Action") == "Auto-Start" and state == "stopped":
                print(f"Starting instance {instance_id}...")
                ec2_client.start_instances(InstanceIds=[instance_id])
                affected_instances.append({"InstanceId": instance_id, "ActionTaken": "Started"})

            --If instance has Auto-Stop tag and is running → stop it
            elif tags.get("Action") == "Auto-Stop" and state == "running":
                print(f"Stopping instance {instance_id}...")
                ec2_client.stop_instances(InstanceIds=[instance_id])
                affected_instances.append({"InstanceId": instance_id, "ActionTaken": "Stopped"})

    --Print/log affected instances
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


**Output:**
**Response:**
{
  "statusCode": 200,
  "body": "[{\"InstanceId\": \"i-0c55e287b17ad6942\", \"ActionTaken\": \"Started\"}, {\"InstanceId\": \"i-0c677ba2ae9d0ab14\", \"ActionTaken\": \"Stopped\"}]"
}
Function Logs:
START RequestId: eb4d5c34-ceb8-4093-ac17-b16bb88e2bc7 Version: $LATEST
Starting instance i-0c55e287b17ad6942...
Stopping instance i-0c677ba2ae9d0ab14...
Affected Instances:
- i-0c55e287b17ad6942 (Started)
- i-0c677ba2ae9d0ab14 (Stopped)
END RequestId: eb4d5c34-ceb8-4093-ac17-b16bb88e2bc7
REPORT RequestId: eb4d5c34-ceb8-4093-ac17-b16bb88e2bc7	Duration: 1254.72 ms	Billed Duration: 1767 ms	Memory Size: 128 MB	Max Memory Used: 96 MB	Init Duration: 511.76 ms

Request ID: eb4d5c34-ceb8-4093-ac17-b16bb88e2bc7


  <img width="452" height="254" alt="TestLog" src="https://github.com/user-attachments/assets/ed8a52bb-0757-492e-8c31-fd0ca63354f7" />
  
  
  <img width="452" height="254" alt="AfterLambdaFunctionTriggered" src="https://github.com/user-attachments/assets/0b806fb2-6c82-418e-a6e0-e7ccb36a078a" />
