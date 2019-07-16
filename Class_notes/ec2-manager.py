import boto3
import json 
import argparse

#dir(ec2)

ec2 = boto3.client('ec2')

images = {
    'aws-linux'  : 'ami-0d8f6eb4f641ef691',
    'centos'     : 'ami-0f2b4fc905b0bd1f1',
}


parser = argparse.ArgumentParser(description='Script to manager EC2 instances.')

required = parser.add_argument_group('required group')
required.add_argument('-n', '--name', help='Please provide image name for ec2 instances.', required=False)

notrequired = parser.add_argument_group('not required group')
notrequired.add_argument('-g', '--get', help='Please provide image id', required=False)
args = parser.parse_args()



def get_instances():
    data = ec2.describe_instances()
    for item in data['Reservations']:
        if item['Instances'][0]['State']['Name'].lower() == 'running':
            print('InstanceId', item['Instances'][0]['InstanceId'])
            print('SubnetId', item['Instances'][0]['SubnetId'])

# Resource is needed when you need to create, start/stop or terminating
def create_instance(name):
    image_id = None 
    
    if name in images.keys():
        image_id =  images[name]
    else:
        print('Image not found ')

    if image_id:
        ec2 = boto3.resource('ec2')
        ec2.create_instances(ImageId=image_id, MinCount=1, MaxCount=1, InstanceType='t2.micro')

    
def main():
    if args.get:
        get_instances()
        exit()
        
    if args.name in images.keys():
        create_instance(args.name)
    else:
        print('Image name is not supported.')
    

# every functions you have, they have to work in main function.
if __name__ == "__main__" :
    main()