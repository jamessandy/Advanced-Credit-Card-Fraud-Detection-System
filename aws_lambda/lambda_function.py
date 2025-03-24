
import json
import boto3

def lambda_handler(event, context):
    for record in event['Records']:
        payload = json.loads(record['body'])
        if payload['is_fraud'] == 1:
            alert_user(payload)
    return {
        'statusCode': 200,
        'body': json.dumps('Processed successfully')
    }

def alert_user(transaction):
    sns = boto3.client('sns')
    sns.publish(
        PhoneNumber='+1234567890',
        Message=f"Fraud Alert! Transaction ID: {transaction['transaction_id']}"
    )
