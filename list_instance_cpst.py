import boto3

def list_running_instances():
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}, Cost: {calculate_instance_cost(instance)}")

def calculate_instance_cost(instance):
    # Implement your own logic to calculate instance cost based on instance type, region, etc.
    # You may use the AWS Pricing API or a cost calculator library.
    # Example: https://aws.amazon.com/pricing/
    return 0.0

if __name__ == "__main__":
    list_running_instances()
