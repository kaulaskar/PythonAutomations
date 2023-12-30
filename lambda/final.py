import json
import boto3

# def get_volme_id(vloume_arn):
#     arn_parts = vloume_arn.split(':')
#     id = arn_parts[-1].split('/')[-1]
#     return id

def lambda_handler(event, context):
    
    # vloume_arn = event["resources"][0]
    # id = get_volme_id(vloume_arn)
 
    vol_ID = (event["resources"][0]).split('/')[1]
    print(vol_ID)
    id = vol_ID
    ec2_client = boto3.client('ec2')
    
    response = ec2_client.modify_volume(
        VolumeId=id,
        VolumeType='gp3'
       
    )
   