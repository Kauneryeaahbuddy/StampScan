import requests
from fake_useragent import UserAgent
import json
from time import sleep


async def main_scrap():
  ua = UserAgent()
  url = 'https://pkizh327c7.execute-api.us-west-2.amazonaws.com/prod/src20/latest?count=200'
  headers = {'user-agent': f'{ua.random}'}
  response = requests.get(url=url, headers=headers)

  data = response.json()
  list_of_mints = {}

  for items in data:
    name_of_tick = items.get('tick')
    if name_of_tick not in list_of_mints:
      list_of_mints[name_of_tick] = 1
    else:
      list_of_mints[name_of_tick] += 1

  return list_of_mints


async def main_scrap():
  ua = UserAgent()
  url = 'https://pkizh327c7.execute-api.us-west-2.amazonaws.com/prod/src20/latest?count=200'
  headers = {'user-agent': f'{ua.random}'}
  response = requests.get(url=url, headers=headers)

  data = response.json()
  list_of_mints = {}

  try:
    for items in data:
      name_of_tick = items.get('tick')
      if name_of_tick not in list_of_mints:
        list_of_mints[name_of_tick] = 1
      else:
        list_of_mints[name_of_tick] += 1
    return list_of_mints
  except Exception as _ex:
    sleep(120)
    return await main_scrap()
