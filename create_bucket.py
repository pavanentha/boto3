import logging
import boto3
from botocore.exceptions import ClientError


def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    s3_client = boto3.client('s3')
    try:
        if region is None:
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def main():
    """Exercise create_bucket() method"""

    # Assign these values before running the program
    bucket_name_in_default_region = 'jmsthbucket1'
    bucket_name_in_specified_region = 'jmsthbucket'
    region = 'ap-south-1'

    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Create a bucket in the S3 default region (us-east-1)
    if create_bucket(bucket_name_in_default_region):
        logging.info(f'Created bucket {bucket_name_in_default_region} '
                     f'in the S3 default region (us-east-1)')

    # Create a bucket in a specified region
    if create_bucket(bucket_name_in_specified_region, region):
        logging.info(f'Created bucket {bucket_name_in_specified_region} '
                     f'in region {region}')


if __name__ == '__main__':
    main()
