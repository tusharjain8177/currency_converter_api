from flask import Flask,request, jsonify
import requests
# Url https://api.exchangerate.host/convert?from=USD&to=EUR

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']
    # print(str(source_currency) + " " + str(amount) + " " + str(target_currency))
    cf = converter(source_currency,target_currency)
    final_amount = amount * cf
    # print(final_amount)
    final_amount = round(final_amount)
    response = {
        'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currency)
    }
    return jsonify(response)

def converter(source, target):
    url = "https://api.exchangerate.host/convert?from={}&to={}".format(source,target)
    response = requests.get(url)
    response = response.json()
    # print(response['info']['rate'])

    return response['info']['rate']

if __name__ == '__main__':
    app.run(debug=True)