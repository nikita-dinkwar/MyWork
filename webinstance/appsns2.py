import boto3

client = boto3.client('sns')

topic = client.create_topic(Name="discountoffers")
topic_arn = topic['TopicArn']


client.subscribe(TopicArn=topic_arn, Protocol='email', Endpoint='nikitadinkwar@gmail.com')
print("Successful Subscription")
client.publish( TopicArn = topic_arn, Message="Hi,what a lovely day it is",Subject="yes it is")
print("Message Published")



