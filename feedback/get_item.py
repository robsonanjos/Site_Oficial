from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_feedback(id_fb, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="sa-east-1")

    table = dynamodb.Table('Feedback')

    try:
        response = table.get_item(Key={'id_fb': id_fb})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    feedback = get_feedback("1")
    if feedback:
        print("Get movie succeeded:")
        pprint(feedback, sort_dicts=False)