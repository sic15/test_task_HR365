from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests


@api_view(['GET'])
def converter(request, fr, to, value):
    url = f'https://currate.ru/api/?get=rates&pairs={fr}{to}&key=25ec6aa2f0f7b53aa53ba28d9e7fdc54'
    answer = requests.get(url)
    res = answer.json().get('data').get(f'{fr}{to}')
    res_calc = float(res)*float(value)
    return Response({'result': res_calc})