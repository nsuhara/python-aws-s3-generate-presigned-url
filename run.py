import os

import boto3

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID', '')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY', '')
region_name = os.getenv('REGION_NAME', '')

bucket = os.getenv('BUCKET', '')
key = os.getenv('KEY', '')
expires_in = os.getenv('EXPIRES_IN', '')  # sec / 1hour = 3600sec.


def main():
    s3 = boto3.client(
        service_name='s3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )

    presigned_url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': bucket,
            'Key': key
        },
        ExpiresIn=expires_in,
        HttpMethod='GET'
    )

    print('-----\n{}\n-----'.format(presigned_url))


if __name__ == '__main__':
    main()
