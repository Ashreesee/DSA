import boto3

session = boto3.Session()

print("✅ Services available as resource:")
for service in session.get_available_resources():
    print(f" - {service}")

# so far only these are available as resources: cloudformation, cloudwatch, dynamodb, ec2, glacier, iam, opsworks, s3, sns, sqs.

print("\n✅ Services available as client:")
for service in session.get_available_services():
    print(f" - {service}")

#created a session
aws_management_console = boto3.session.Session(profile_name='default')

#this will list all available objects inside the session
print(dir(aws_management_console))

#lets suppose from the list i picked get_available_regions (object)
service_name = "ec2" #choose a service

#get and print all the regions available for that service
regions = session.get_available_regions(service_name)


print(f"✅ Available regions for service '{service_name}':")
for region in regions:
    print(f" - {region}")


#to check multiple services regions
services = ['ec2', 's3', 'lambda', 'dynamodb']

for service in services:
    print(f"\n🔍 Regions for {service}:")
    for region in session.get_available_regions(service):
        print(f" - {region}")