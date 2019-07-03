import logging
import boto3
from botocore.exceptions import ClientError


def create_ec2_instance(image_id, instance_type, keypair_name):
    """Provision and launch an EC2 instance

    The method returns without waiting for the instance to reach
    a running state.

    :param image_id: ID of AMI to launch, such as 'ami-XXXX'
    :param instance_type: string, such as 't2.micro'
    :param keypair_name: string, name of the key pair
    :return Dictionary containing information about the instance. If error,
    returns None.
    """

    # Provision and launch the EC2 instance
    ec2_client = boto3.client('ec2')
    try:
        response = ec2_client.run_instances(ImageId=image_id,
                                            InstanceType=instance_type,
                                            KeyName=keypair_name,
                                            MinCount=1,
                                            MaxCount=1)
    except ClientError as e:
        logging.error(e)
        return None
    return response['Instances'][0]


def main():
    # Assign these values before running the program
    image_id = 'ami-0b99c7725b9484f9e'
    instance_type = 't2.micro'
    keypair_name = 'awsdemojmsth'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Provision and launch the EC2 instance
    instance_info = create_ec2_instance(image_id, instance_type, keypair_name)
    if instance_info is not None:
        logging.info(f'    Launched EC2 Instance {instance_info["InstanceId"]}')
        logging.info(f'    VPC ID: {instance_info["VpcId"]}')
        logging.info(f'    Private IP Address: {instance_info["PrivateIpAddress"]}')
        logging.info(f'    Current State: {instance_info["State"]["Name"]}')


if __name__ == '__main__':
    main()
