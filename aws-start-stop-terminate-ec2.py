import boto3
client = boto3.client('ec2')

resp = client.terminate_instances(InstanceIds=['i-0158ab7a03bb6a954'])

for instance in resp['TerminatingInstances']:
    print("The instance with id {} Terminated".format(instance['InstanceId']))


# If you want to stop replace terminate with stop same for start as well
# import boto3
# ec2 = boto3.client('ec2')

# resp = ec2.stop_instances(
#     InstanceIds=['i-054818b730192804d']
# )
# print(resp)
