
event ={
   "version":"0",
   "id":"d22372af-2211-8e85-5552-8275d9f2e7b2",
   "detail-type":"EBS Volume Notification",
   "source":"aws.ec2",
   "account":"844609451572",
   "time":"2023-12-20T11:14:37Z",
   "region":"us-east-1",
   "resources":[
      "arn:aws:ec2:us-east-1:844609451572:volume/vol-0b0c2fb743a4a2045"
   ],
   "detail":{
      "result":"available",
      "cause":"",
      "event":"createVolume",
      "request-id":"24c14286-17d5-4add-a79d-6b3fe288de45"
   }
} 

Vol_ID = str(event["resources"][0]).split('/')[1]

print (type(Vol_ID))

# arn = (event["resources"][0])
# print(arn)

# def id(arn):
#     id = arn.split(':')[-1] 

#     v_id = id.split('/')[-1]
#     return v_id   

# def lambda_handler(event, context):
#     # arn = (event["resources"][0])
#     vol_ID = (event["resources"][0]).split('/')[1]
#     print(vol_ID)


###########    
# import json
# import boto3

# def id(arn):
    
#     id = arm.split(':')[-1] 
#     v_id = id.split('/')[-1]
#     print(v_id)

# def lambda_handler(event, context):
#     # arn = (event["resources"][0])
#     vol_ID = (event["resources"][0]).split('/')[1]
#     print(vol_ID)
    
#     ec2_client = boto3.client('ec2')
    
#     response = ec2_client.modify_volume(
#         VolumeId='vol_ID',
#         VolumeType='gp3',
       
#     )
   