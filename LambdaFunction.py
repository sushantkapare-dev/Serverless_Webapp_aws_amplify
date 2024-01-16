
import json
import boto3
import time

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Product')

def lambda_handler(event, context):

    if(event['operation'] == 'addProduct'):
        return saveProduct(event) 
    else: 
        return getProducts()
    

def saveProduct(event):
    gmt_time = time.gmtime()
    
    now = time.strftime('%a, %d %b %Y %H:%M:%S', gmt_time)

    table.put_item(
        Item={
            'productCode': event['productCode'],
            'price': event['price'],
            'createdAt':now
            })

    return {
        'statusCode': 200,
        'body': json.dumps('Product with ProductCode : ' + event['productCode'] + ' created at '+ now)
    }

def getProducts():

    response = table.scan()
    
    items = response['Items']
    print(items)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(items),
        'headers': {
            'Content-Type': 'application/json',
        }
    } 
