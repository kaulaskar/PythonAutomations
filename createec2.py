import boto3

def provision_ec2_instance(instance_type, key_pair, security_group):
    # Use boto3 to interact with AWS EC2
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId='ami-12345678',
        InstanceType=instance_type,
        KeyName=key_pair,
        SecurityGroups=[security_group],
        MinCount=1,
        MaxCount=1
    )[0]
    print(f"Provisioned instance ID: {instance.id}")

# Example usage
provision_ec2_instance("t2.micro", "my-key-pair", "my-security-group")
