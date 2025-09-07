import json
import os
from datetime import datetime, timezone

import boto3

def lambda_handler(event, context):
    print("Received event:", json.dumps(event, indent=2, default=str))

    # Region of the event (fallback to function's region)
    region = event.get("region") or os.environ.get("AWS_REGION") or os.environ.get("AWS_DEFAULT_REGION")
    ec2 = boto3.client("ec2", region_name=region)

    instance_ids = []

    detail = event.get("detail", {})

    # Case 1: EventBridge rule for "EC2 Instance State-change Notification"
    # detail.instance-id + detail.state = pending/running/stopped/...
    if "instance-id" in detail:
        state = detail.get("state")
        # We tag on 'running' to ensure the instance exists and is ready
        if state in ("pending", "running") or state is None:
            instance_ids = [detail["instance-id"]]

    # Case 2: EventBridge rule for "AWS API Call via CloudTrail" with eventName=RunInstances
    # instance IDs are in responseElements.instancesSet.items[*].instanceId
    if not instance_ids and detail.get("eventName") == "RunInstances":
        try:
            items = detail["responseElements"]["instancesSet"]["items"]
            instance_ids = [item["instanceId"] for item in items if "instanceId" in item]
        except KeyError:
            pass

    if not instance_ids:
        # No instance IDs found in the event; surface it in logs for troubleshooting
        raise ValueError("No instance IDs found in event")

    # Build tags
    launch_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    custom_key = os.environ.get("CUSTOM_TAG_KEY", "Project")
    custom_val = os.environ.get("CUSTOM_TAG_VALUE", "AutoTag")

    tags = [
        {"Key": "LaunchedOn", "Value": launch_date},
        {"Key": custom_key,   "Value": custom_val}
    ]

    # Create tags (idempotent; updates value if key exists)
    ec2.create_tags(Resources=instance_ids, Tags=tags)

    msg = {"taggedInstances": instance_ids, "tags": tags, "region": region}
    print("Tagging complete:", json.dumps(msg))
    return msg
