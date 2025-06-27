import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('website-db')

    # Add one to the counter and ask for the new value to be returned
    response = table.update_item(
        Key={'visitorId': 1},
        UpdateExpression="ADD #cnt :val",
        ExpressionAttributeNames={'#cnt': 'visitors'},
        ExpressionAttributeValues={':val': 1},
        ReturnValues="UPDATED_NEW"
    )

    # Retrieve the new value
    visitors = response['Attributes']['visitors']

    return {
        'statusCode': 200,
        'body': json.dumps(str(visitors))
    }
