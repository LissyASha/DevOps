# Assignment2
**Created an S3 Bucket and uploaded a few files on the back date.**

<img width="936" height="441" alt="S3Bucket_WitholdFiles" src="https://github.com/user-attachments/assets/8879644b-90aa-422e-a471-fb8fd8b80164" />

**Created a new I AM role for Lambda and attached the `AmazonS3FullAccess` policy to this role**
  
<img width="936" height="441" alt="AmazonS3FullAccess_Role" src="https://github.com/user-attachments/assets/886e9744-d03f-49a3-8da0-4d5e0baadfb8" />


**Created a Lambda Function to list out the objects in the specified bucket and delete objects older than 30 days.**



<img width="936" height="441" alt="S3_Cleanup_LambdaFunction" src="https://github.com/user-attachments/assets/8bf5de72-f295-4706-8628-2d666d73b685" />


**Triggered the Lambda function manually and added the screenshots with logs**


<img width="936" height="441" alt="Log" src="https://github.com/user-attachments/assets/5e8a9f33-33da-4389-9c64-71d4c394145f" />



<img width="936" height="441" alt="CloudWatch_Log" src="https://github.com/user-attachments/assets/5d1339f5-ee40-480f-afa6-76ed90799795" />


**After deleting the older files >30 days, the S3 bucket contains only the recently uploaded files**

<img width="936" height="441" alt="S3Bucket_DeletedOldFiles" src="https://github.com/user-attachments/assets/d83c491d-1f18-4e6c-845e-a2e01e1fa915" />



**Function Logs:**
START RequestId: be672ecc-6b3b-4aa2-8594-88e3eae0fd7a Version: $LATEST
Deleted: Complete Python & VS Code Installation Guide for DevOps (1).pdf
END RequestId: be672ecc-6b3b-4aa2-8594-88e3eae0fd7a
REPORT RequestId: be672ecc-6b3b-4aa2-8594-88e3eae0fd7a  Duration: 364.28 ms Billed Duration: 365 ms Memory Size: 128 MB Max Memory Used: 91 MB  Init Duration: 1169.77 ms

Request ID: be672ecc-6b3b-4aa2-8594-88e3eae0fd7a

