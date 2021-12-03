import boto3
 
def create_feedback_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', region_name="sa-east-1")
 
    table = dynamodb.create_table(
        TableName='Feedback',
        KeySchema=[
            {
                'AttributeName': 'id_fb',
                'KeyType': 'HASH'  # Partition key
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id_fb',
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
    feedback_table = create_feedback_table()
    print("Table created")