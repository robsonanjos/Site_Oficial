import boto3
from pprint import pprint
from datetime import datetime
import uuid
 
uuid_nl = str(uuid.uuid1())

data = datetime.today().strftime('%d-%m-%Y')


def put_newsletter(id_nl, nome_nl, email_nl, data_nl, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', region_name="sa-east-1")
 
    table = dynamodb.Table('Newsletter')
    response = table.put_item(
        Item={
            'id_nl': id_nl,
            'nome_nl': nome_nl,
            'email_nl': email_nl,
            'data_nl': data_nl
        }
    )
    return response

    
 
if __name__ == '__main__':
    newsletter_resp = put_newsletter(uuid_nl, "Julia", "giuliana@gmail.com", data)
    print("Put line succeeded:")
    pprint(newsletter_resp, sort_dicts=False)