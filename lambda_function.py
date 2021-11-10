import redis
import json

def lambda_handler(event, context):
    print('hello_world')

    r = redis.Redis(host='localhost', port=6379, db=0)
    print('set-----------------')
    r.set('foo', 'bar')
    print('get-----------------')
    foo = r.get('foo')
    print(f'foo: {foo}')

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


if __name__ == '__main__':
    lambda_handler(None, None)
    pass