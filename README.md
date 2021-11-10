# py-lambda-redis

- install package in local

`pip3 install -r requirements.txt --target ./package`

- package

```bash
cd package
zip -r ../my-deployment-package.zip .
cd ..
zip -g my-deployment-package.zip lambda_function.py
```

- deploy

```bash
aws lambda update-function-code \
    --function-name PyLambdaRedis \
    --zip-file fileb://my-deployment-package.zip
```
