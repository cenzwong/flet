import ai21

def ai21_rewrite(text, intent):
    print(text, intent)
    ai21.api_key = 'jc5dvUcu1UVpWxqMcBCEUUUpFyVUrkvv'
    r = ai21.Experimental.rewrite(
        text=text, 
        intent=intent
    )
    print(r)
    return r["values"]["suggestions"]

# import requests

# def ai21_rewrite(text, intent):
#     api_key = 'jc5dvUcu1UVpWxqMcBCEUUUpFyVUrkvv'
#     r = requests.post(
#         "https://api.ai21.com/studio/v1/experimental/rewrite",
#         headers={"Authorization": f"Bearer {api_key}"},
#         json={
#             "text": text,
#             "intent": "general"
#         }
#     )
#     print(r.json())
#     return r.json()["suggestions"]

# ai21_rewrite("Tomorrow is a good day.", "general")
