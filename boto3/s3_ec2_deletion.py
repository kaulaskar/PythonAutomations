import boto3

# Replace these values with your AWS credentials and configuration

region_name = 'us-east-1'
region_name2 = 'ap-south-1'

# Replace these values with your EC2 instance ID and S3 bucket name
ec2_instance_id = 'i-09448403023db1706'
s3_bucket_name = 'sailesh-s3-buckeket-jan-20233'

# Create EC2 and S3 clients
ec2_client = boto3.client('ec2', region_name=region_name)
s3_client = boto3.client('s3', region_name=region_name2)

# Delete EC2 instance
def delete_ec2_instance(instance_id):
    try:
        response = ec2_client.terminate_instances(InstanceIds=[instance_id])
        print(f"EC2 instance {instance_id} termination response: {response}")
    except Exception as e:
        print(f"Error terminating EC2 instance {instance_id}: {e}")

# Delete S3 bucket
def delete_s3_bucket(bucket_name):
    try:
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"S3 bucket {bucket_name} deleted successfully")
    except Exception as e:
        print(f"Error deleting S3 bucket {bucket_name}: {e}")

# Uncomment the following lines to execute the deletion functions
delete_ec2_instance(ec2_instance_id)
delete_s3_bucket(s3_bucket_name)
