import boto3
 
def create_newsletter_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', region_name="sa-east-1")
 
    table = dynamodb.create_table(
        TableName='Newsletter',
        KeySchema=[
            {
                'AttributeName': 'id_nl',
                'KeyType': 'HASH'  # Partition key
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id_nl',
                'AttributeType': 'S'
            }, 
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )
    return table
 
if __name__ == '__main__':
    feedback_table = create_newsletter_table()
    print("Table created")