import boto3


#This is a default session

aws_management_console = boto3.session.Session(profile_name="default")
iam_console_resource = aws_management_console.resource("iam")
iam_console_client = aws_management_console.client("iam")

#We can create multiple diffrent sessions too with in the same script

# aws_management_console_default = boto3.session.Session(profile_name="default")
# aws_management_console_ashree = boto3.session.Session(profile_name="ashree")
# iam_console = aws_management_console_ashree.resource("iam") 

#we just have to specify which profile we want to use
#since we have no such user we'll comment out these lines

#for resource object
for each_user in iam_console_resource.users.all():
    print(each_user.name)

#for client object
for each in iam_console_client.list_users()["Users"]:
    print(each["UserName"])


