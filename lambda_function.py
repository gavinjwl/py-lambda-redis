from rediscluster import RedisCluster
import json

HOST='localhost'
PORT=6379

def lambda_handler(event, context):
    print('hello_world')

    startup_nodes = [
        {"host": HOST, "port": PORT},
    ]
    rc = RedisCluster(
        startup_nodes=startup_nodes,
        decode_responses=True,
        skip_full_coverage_check=True,
    )
    
    print('set-----------------')
    rc.set('foo', 'bar')
    
    print('get-----------------')
    foo = rc.get('foo')
    print(f'foo: {foo}')

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


if __name__ == '__main__':
    lambda_handler(None, None)
    pass