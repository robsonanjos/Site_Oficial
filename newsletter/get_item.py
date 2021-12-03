from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_newsletter(id_nl, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="sa-east-1")

    table = dynamodb.Table('Newsletter')

    try:
        response = table.get_item(Key={'id_nl': id_nl})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    newsletter = get_newsletter("1")
    if newsletter:
        print("Get movie succeeded:")
        pprint(newsletter, sort_dicts=False)