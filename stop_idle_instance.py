import boto3
from datetime import datetime, timedelta

def stop_idle_instances(max_idle_hours=24):
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    current_time = datetime.utcnow()

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            launch_time = instance['LaunchTime']
            idle_time = current_time - launch_time
            if idle_time > timedelta(hours=max_idle_hours):
                ec2.stop_instances(InstanceIds=[instance['InstanceId']])
                print(f"Stopping instance {instance['InstanceId']} due to inactivity.")

if __name__ == "__main__":
    stop_idle_instances()
