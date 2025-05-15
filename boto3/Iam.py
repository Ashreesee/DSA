import boto3

# S3 resource which is simpler 
s3_resource = boto3.resource('s3')

# IAM client (no resource interface available) it works and gives response as JSON IAM has no resource
iam_client = boto3.client('iam')

# Use resource to list S3 buckets
print("📦 S3 Buckets:")
for bucket in s3_resource.buckets.all():
    print(f" - {bucket.name}")

# Use client to create an IAM user
user_name = "ashree"
try:
    iam_client.create_user(UserName=user_name)
    print(f"✅ IAM User '{user_name}' created.")
except iam_client.exceptions.EntityAlreadyExistsException:
    print(f"⚠️ IAM User '{user_name}' already exists.")

# 🟡 Get current IAM user (based on credentials used)
response = iam_client.get_user()

# 🖨️ Print user details
user = response['User']
print(f"👤 UserName     : {user['UserName']}")
print(f"🆔 UserId       : {user['UserId']}")
print(f"🔗 ARN          : {user['Arn']}")
print(f"📅 Created On   : {user['CreateDate']}")

