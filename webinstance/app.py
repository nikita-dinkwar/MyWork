import boto3
s3 = boto3.resource('s3')
client=boto3.client('s3')
# for bucket in s3.buckets.all():
#         print(bucket.name)

# s3.create_bucket(Bucket='typo121212', CreateBucketConfiguration={
#     'LocationConstraint': 'ca-central-1'})
# print("Bucket created")

client.put_object(Bucket='typo121212',Key='file199.txt',Body=b'Hello snehal!!')

client.put_object(Bucket='typo121212',Key='file200.txt',Body=b'Hello file200!!')

