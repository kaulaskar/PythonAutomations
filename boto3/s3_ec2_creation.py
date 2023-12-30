import boto3

client = boto3.client('s3')
client = boto3.client('ec2')

response = client.create_bucket(
     Bucket='sailesh-s3-buckeket-jan-20233',
     CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1',
    },
    )




aws_region = 'us-east-1'
instance_type = 't2.micro'
key_pair_name = 'desktop-key'

ami_id = 'ami-0c7217cdde317cfec'

# Create EC2 client
ec2 = boto3.client('ec2', region_name=aws_region)


response2 = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_pair_name,
    MinCount=1,
    MaxCount=1
   
)

print (response2)