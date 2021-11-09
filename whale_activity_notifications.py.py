import requests
import telegram_send

address1=<Add the address of the pool/wallet you would like to track.># String value and hence the address should be within double quote ("")
url = 'https://algoexplorerapi.io/v2/accounts/<Add wallet/pool address here>/transactions/pending' #mainnet address
amt = 0
while(1):
    res = requests.get(url)
    for trans in res.json()['top-transactions']:
        if 'aamt' in trans['txn']:
            if trans['txn']['snd'] == address1:
                if trans['txn']['aamt']>500000: # I consider any transactions more than 500000 a whale activity. Modify this number as required. 
                    if trans['txn']['arcv'] != amt:
                        amt = trans['txn']['aamt']
                        msg = "Bought " + str(trans['txn']['aamt']) + " Akitas"
                        telegram_send.send(messages=[msg])
            if trans['txn']['arcv'] == address1:
                if trans['txn']['aamt']>500000:
                    if trans['txn']['arcv'] != amt:
                        amt = trans['txn']['aamt']
                        msg = "Sold " + str(trans['txn']['aamt']) + " Akitas"
                        telegram_send.send(messages=[msg])
