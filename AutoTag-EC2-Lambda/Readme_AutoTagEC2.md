# Assignment3

****Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3****

**Steps:**
 **Created a new role for Lambda and attached the `AmazonEC2FullAccess` policy to this role.**
  
  <img width="930" height="440" alt="IAM Role_Lambda" src="https://github.com/user-attachments/assets/7572080d-ca36-43f7-8c75-bbe7b5f48e19" />

**Created the Lambda function and implemented the code**
    --Retrieve the instance ID from the event.
    --Tag the new instance with the current date and another tag with the name Automation.

  <img width="956" height="493" alt="EC2-AutoTagging-Lissy" src="https://github.com/user-attachments/assets/d7ae78f2-6991-4b61-a98a-be26fecb3be1" />
  

  **Created a CloudWatch Event Rule to trigger the EC2 instance launch event.**
  
  <img width="956" height="483" alt="CloudWatch_Event_Rule " src="https://github.com/user-attachments/assets/795e71f8-b97a-4f55-ad71-366042959cea" />

  **Attached the Lambda function as the target**

  
  <img width="949" height="486" alt="Target_LambdaFunction" src="https://github.com/user-attachments/assets/4c6991dd-d15b-4826-84de-d8de6039228f" />

  **Launched an EC2 Instance to trigger the Event**
  
  <img width="960" height="540" alt="Lanching_EC2_Instance" src="https://github.com/user-attachments/assets/93392421-94a2-4b1e-9f3a-6cae53b56cfd" />

 **Tags are applied a few seconds later, during the EC2 state transition**

 
   <img width="957" height="483" alt="AutoTagged_EC2_StateChanges" src="https://github.com/user-attachments/assets/dbbe3e2b-483b-4008-b230-cfe7c5c43dc5" />

