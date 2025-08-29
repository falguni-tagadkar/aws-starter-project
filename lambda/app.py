def lambda_handler(event, context):
    raise Exception("Test error to trigger CloudWatch alarm")
    # return {
    #     'statusCode': 200,
    #     'body': 'Hello from Lambda!'
    # }
