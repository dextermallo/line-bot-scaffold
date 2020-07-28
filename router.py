from linebot.exceptions import InvalidSignatureError
import json

from function.example import *


def webhook_handler(event, context):
    signature = event['headers']['X-Line-Signature']

    resp = {
        'statusCode': 200,
        'body': json.dumps({'message': 'hello world'})
    }

    try:
        handler.handle(event['body'], signature)
    except InvalidSignatureError:
        print('signature error')
    except Exception as e:
        print(e)
    finally:
        return resp
