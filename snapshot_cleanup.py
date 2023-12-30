import boto3
from datetime import datetime, timedelta

def cleanup_snapshots(max_age_days=7):
    ec2 = boto3.client('ec2')
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']

    current_time = datetime.utcnow()

    for snapshot in snapshots:
        snapshot_time = snapshot['StartTime']
        age = current_time - snapshot_time
        if age > timedelta(days=max_age_days):
            ec2.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
            print(f"Deleting snapshot {snapshot['SnapshotId']} created at {snapshot_time}.")

if __name__ == "__main__":
    cleanup_snapshots()
