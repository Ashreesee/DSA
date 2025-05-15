import boto3

aws_management_console = boto3.session.Session(profile_name="default")
ec2_client = aws_management_console.client(service_name="ec2")
ec2_resource = aws_management_console.resource(service_name="ec2")


#-----This will simply list the instances present---------
# result = ec2_client.describe_instances() ["Reservations"]
# print(result)


# --- 1️⃣ List EC2 instances ---
print("🖥️ Listing EC2 Instances...\n")
response = ec2_client.describe_instances()
reservations = response["Reservations"]

for reservation in reservations:
    for instance in reservation["Instances"]:
        instance_id = instance["InstanceId"]
        public_ip = instance.get("PublicIpAddress", "N/A")
        name = "N/A"
        if "Tags" in instance:
            for tag in instance["Tags"]:
                if tag["Key"] == "Name":
                    name = tag["Value"]
                    break
        print(f"🔹 ID: {instance_id}  🏷️ Name: {name}  🌐 Public IP: {public_ip}")

# --- 2️⃣ Create a new EC2 instance ---
print("\n🚀 Launching a new EC2 instance...")

new_instance = ec2_resource.create_instances(
    ImageId='ami-0e35ddab05955cf57',  # ✅ Amazon Linux 2 AMI (change as needed)
    InstanceType='t2.micro',           # ✅ Free tier eligible
    MinCount=1,
    MaxCount=1,
    KeyName='EC2A',      # 🔑 Replace with your key pair
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'demo'}]
        }
    ],
    SecurityGroupIds=['sg-0a01f14c474355e16'],   # 🔒 Replace with your SG ID
    SubnetId='subnet-0a147f7867d600826'         # 🌐 Replace with your Subnet ID
)

instance_id = new_instance[0].id
print(f"✅ Instance launched! ID: {instance_id}")

# --- 3️⃣ Trigger action (e.g., Stop the instance) ---
# Uncomment below to perform action
# ec2_client.stop_instances(InstanceIds=[instance_id])
# print(f"🛑 Instance {instance_id} stopped.")

# ec2_client.start_instances(InstanceIds=[instance_id])
# print(f"▶️ Instance {instance_id} started.")

# ec2_client.terminate_instances(InstanceIds=[instance_id])
# print(f"🔥 Instance {instance_id} terminated.")
