from tinyman.v1.pools import Pool
from tinyman.v1.client import TinymanTestnetClient,TinymanMainnetClient
import telegram_send
import time

client = TinymanMainnetClient()
AKITA = client.fetch_asset(384303832) #Add asset Id of the ASA you would like to fetch. 
ALGO = client.fetch_asset(0)
TINYUSDC = client.fetch_asset(312769)

pool = Pool(client, asset_a=AKITA, asset_b=ALGO, fetch=True)
pool_usdt = Pool(client, asset_a=TINYUSDC, asset_b=ALGO, fetch=True) # To convert algo to USD as tinyman doesnt show the asset price in USD yet
while(1):
    quote = pool.fetch_fixed_output_swap_quote(ALGO(100_000_0))
    quote_usdt = pool_usdt.fetch_fixed_output_swap_quote(ALGO(100_000_0))
    akita_algo_quote = (1/quote.amount_in.amount)*(quote_usdt.amount_in.amount/quote_usdt.amount_out.amount)
    if (akita_algo_quote > 0.05) or (akita_algo_quote < 0.02):
        msg = "Alert! Price is "+ str(akita_algo_quote)
        telegram_send.send(messages=[msg])
    time.sleep(180)
