import boto3

# Create SQS client
# sqs = boto3.client('sqs')

# queue_url = 'https://sqs.ca-central-1.amazonaws.com/106129732153/my-orders'

# Send message to SQS queue
# response = sqs.receive_message(
#     QueueUrl=queue_url,
#     DelaySeconds=10,
#     MessageAttributes={
#         'Title': {
#             'DataType': 'String',
#             'StringValue': 'messagein'
#         },
#         'Author': {
#             'DataType': 'String',
#             'StringValue': 'Nikita'
#         },
#     },
#     MessageBody=(
#         'Message send successfully to the user '
#     )
# )
# 
# another method
# response=sqs.receive_message(QueueUrl = 'https://sqs.ca-central-1.amazonaws.com/106129732153/my-orders')
# for message in response['Messages']:
#   print(message['Body'])


# send and receive
queueUrl="https://sqs.ca-central-1.amazonaws.com/106129732153/my-orders"
sqs = boto3.client('sqs')

sqs.send_message(
        QueueUrl=queueUrl,
        MessageBody=('Hello Hinjawadi')
)

response = sqs.receive_message(QueueUrl=queueUrl)

for message in response['Messages']:
    print (message['Body'])
