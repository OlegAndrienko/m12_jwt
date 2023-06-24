from jose import jwt, JWTError

secret = "09b7a6e0b994ede14247d1cddacd1d838e8985dc95c718cbfcf8d314bae0b98f"

payload = {'sub': 'example@test.com', 'username': 'John Doe', 'role': 'moderator'}

token = jwt.encode(payload, secret, algorithm='HS256')

print(token)


try:
    decoded = jwt.decode(token, secret , algorithms=['HS256'])
    print(decoded)
except JWTError as e:
    print(e)
    