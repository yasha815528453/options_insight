import schwab


api_key = "wKNrAIAtLD5REWZHW9lbnr9tPA0ySVFY"
app_secret = "cf5goO0bxducNndp"
callback_url = "https://127.0.0.1"
token_path = "C:\\Users\\spam8\\Documents\\optionsinsight\\Backend\\Infrastructure\\TD_API\\token.txt"



c = schwab.auth.client_from_token_file(token_path, api_key, app_secret, asyncio=False, enforce_enums=True)



resp = c.get_quote("MARA", fields=None)
print(resp)
print(resp.json())
