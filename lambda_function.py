import json

def lambda_handler(event, context):
    try:
        # Extract username and password from the event object
        username = event.get("username")
        password = event.get("password")
        
        # Input validation: Check if both username and password are provided
        if username is None or password is None:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Failure: Missing username or password"})
            }

        # Sample check for valid credentials
        if username == "validUser" and password == "validPassword":
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Success: User authenticated"})
            }
        else:
            return {
                "statusCode": 401,
                "body": json.dumps({"message": "Failure: Invalid username or password"})
            }

    except KeyError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": f"Failure: Missing key {str(e)}"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Failure: An unexpected error occurred", "error": str(e)})
        }
