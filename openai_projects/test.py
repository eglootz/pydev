import requests

link = "https://api.openai.com/v1/images/generations"

data = "{ \
    \"token\": \"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\" \
    \"prompt\": \"A cute baby sea otter\", \
    \"n\": 2, \
    \"size\": \"1024x1024\" \
}"

images = requests.post(link, data)

print(images)