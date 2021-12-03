import boto3
from pprint import pprint
from datetime import datetime
import uuid
 
uuid_fb = str(uuid.uuid1())

data = datetime.today().strftime('%d-%m-%Y')


def put_feedback(id_fb, nome_fb, email_fb, tema_contato, mensagem, data_fb, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', region_name="sa-east-1")
 
    table = dynamodb.Table('Feedback')
    response = table.put_item(
        Item={
            'id_fb': id_fb,
            'nome_fb': nome_fb,
            'email_fb': email_fb,
            'tema_contato': tema_contato,
            'mensagem': mensagem,
            'data_fb': data_fb
        }
    )
    return response

    
 
if __name__ == '__main__':
    feedback_resp = put_feedback(uuid_fb, "Giuliana", "giuliana@gmail.com", "Sugestão", "Teste", data)
    print("Put line succeeded:")
    pprint(feedback_resp, sort_dicts=False)