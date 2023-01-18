import openai as oa
import json
import credentials

oa.api_key = (credentials.openai_api_key)



def get_response(response):
    response_string = str(response)
    response_dic = json.loads(response_string)
    choice_dic = response_dic.get("choices")[0]
    antwort = choice_dic.get("text")
    return antwort

def chat(prompt):
    response = oa.Completion.create(
    model="text-davinci-003",
    prompt=f"{prompt} <|endoftext|>",
    max_tokens=2048,
    temperature=1)
    return response