import json
import requests

# from sentiment_analysis import sentiment_analyzer
# sentiment_analyzer("I love this new technology")
def sentiment_analyzer(text_to_analyze):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyze}}
    response = requests.post(url, json = myobj, headers = header)

    formatted_response = json.loads(response.text)
    status = response.status_code

    if status == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif status == 500:
        label = None
        score = None

    return {'label': label, 'score': score}