python
import os
import requests

TOKEN = os.getenv('8409740518:AAG6mRJ5Q0pdt-QUtqLYU-lIUFuseHbwn3M)
CHAT_ID = os.getenv('967250869')

url = 'https://loteriascaixa-api.herokuapp.com/api/lotofacil/latest'
resp = requests.get(url).json()

if resp.get("acumulado"):
    mensagem = f"⚠️ Lotofácil acumulou no concurso {resp['concurso']}!\nPrêmio estimado: R$ {resp['valor_estimado_proximo_concurso']}"
else:
    mensagem = f"📢 Lotofácil *NÃO* acumulou no concurso {resp['concurso']}."

telegram_url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
params = {'chat_id': CHAT_ID, 'text': mensagem}
requests.get(telegram_url, params=params)
