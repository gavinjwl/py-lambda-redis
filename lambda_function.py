import redis
import json

HOST='localhost'
PORT=6379

def lambda_handler(event, context):
    print('hello_world')

    r = redis.Redis(host=HOST, port=PORT, db=0)
    
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