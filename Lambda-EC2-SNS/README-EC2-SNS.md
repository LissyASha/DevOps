# Assignment4

**Monitor EC2 Instance State Changes Using AWS Lambda, Boto3, and SNS**

**Steps:**

**Created a new role LambdaEC2MonitorRole, for Lambda.**
  -Attached AmazonEC2ReadOnlyAccess and AmazonSNSFullAccess
    <img width="958" height="491" alt="LambdaEC2MonitorRole" src="https://github.com/user-attachments/assets/4668f0f8-ee90-4748-aa92-0680091ad7df" />

**SNS Setup:**
  Created an SNS topic.
      Type: Standard
      Name: EC2StateChangeTopic

  Created subscription.
    Protocol: Email
    Endpoint: lissy.asha@gmail.com(my email Address)    

  
  <img width="953" height="484" alt="EC2StateChangeTopic-Lissy" src="https://github.com/user-attachments/assets/ed7615b4-6195-4b6f-8b62-38b8f3b123a9" />

**Subscription Confirmation via Email**
  
    <img width="953" height="497" alt="Subscription_Mail_Confirmation" src="https://github.com/user-attachments/assets/9827657b-f696-42c6-a422-f0a571388aea" />

    
    <img width="960" height="540" alt="Subscription_Confirmation" src="https://github.com/user-attachments/assets/2e327dc6-a9f1-4876-b73a-18ab5414ea1b" />
    


**Created a Lambda Function with name EC2StateChangeMonitor and attached the role LambdaEC2MonitorRole.**

  
  <img width="956" height="487" alt="LambdaFunction-EC2MonitorRole" src="https://github.com/user-attachments/assets/e7d87e57-1346-4a17-a0df-abf159278ef8" />
  

  <img width="958" height="495" alt="EC2StateChangeMonitor-Lissy" src="https://github.com/user-attachments/assets/e7d41234-1998-4738-a58c-046e8f2bd38d" />


**EventBridge Rule:**
  Created a  Rule.
    -Name: **EC2StateChangeRule**.
    -Event bus: default.
    -Rule type: Rule with an event pattern.
    -Event pattern → Choose AWS service:
    -Service: EC2
    -Event type: EC2 Instance State-change Notification.
    -Add target → Selected the Lambda function **EC2StateChangeMonitor**.

    
      <img width="955" height="479" alt="EC2StateChangeRule-Lissy_TargetLambdaFunctionAdded" src="https://github.com/user-attachments/assets/96357a24-6a9e-4d44-a21d-c8de9de636c0" />


**To trigger the Lambda function, I have changed the state of an EC2 instance to Stop** 
    
    <img width="863" height="471" alt="Stopping EC2Instance to Trigger Event" src="https://github.com/user-attachments/assets/639d80f4-7662-4ded-96ff-dc4652712d5d" />

**Outcome**
    -EventBridge detects EC2 state changes.
    -Lambda processes the event and sends messages.
    -SNS notifies the receiver via email.

    <img width="947" height="490" alt="SNS - Email Notification Received Once EC2 State Changes" src="https://github.com/user-attachments/assets/ffc6a56d-c839-422d-abb8-1f8c887e7924" />


**CloudWatch Log**

    
    <img width="949" height="481" alt="CloudWatch_Log" src="https://github.com/user-attachments/assets/312268db-7ad2-4b96-a330-326c5e3e5bc8" />







