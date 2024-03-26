import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from time import sleep
from scrap import main_scrap

logging.basicConfig(level=logging.INFO)

bot = Bot(token='WRITE YOUR TOKEN')
dp = Dispatcher()


@dp.message(Command('start'))
async def start_commnad(message: types.Message):
  await message.answer(
      "Hello! Write '/ActivateSiteTracker' and I will start tracking site's mint graphic"
  )


WhileOption = True


@dp.message(Command('ActivateSiteTracker'))
async def SiteTrackerON(message: types.Message):
  mints = await main_scrap()
  for i, j in sorted(mints.items(), key=lambda kv: kv[1], reverse=True):
    card = f'Name of tick: {i.upper()}\n' \
        f'How many mints there: {j}\n' \
        f'THIS ONE IS RIGHT MEOW'
    await message.answer(card)
  await message.answer("Write '/TurnOFFSiteTracker' to disable tracker")
  global WhileOption
  WhileOption = True
  while WhileOption:
    await asyncio.sleep(600)
    new_mints = await main_scrap()
    if mints != new_mints:
      ResultHtable = {}
      for i, j in new_mints.items():
        if i in mints.keys():
          if mints[i] - j != 0:
            ResultHtable[i] = -(mints[i] - j)
        else:
          ResultHtable[i] = j

      await message.answer('WARNING! NEW LIST OF MINTS')
      for i, j in sorted(ResultHtable.items(),
                         key=lambda kv: kv[1],
                         reverse=True):
        if j > 0:
          card = f'Name of tick: {i.upper()}\n' \
              f'Has increased on: {j} mints\n' \
              f'Total mints: {new_mints[i]}\n'
          await message.answer(card)
        elif j < 0:
          card = f'Name of tick: {i.upper()}\n' \
              f'Has decreased on: {-j} mints\n' \
              f'Total mints: {new_mints[i]}\n'
          await message.answer(card)

      await message.answer(f"There's new list of mints: \n")
      for i, j in sorted(new_mints.items(), key=lambda kv: kv[1],
                         reverse=True):
        card = f'Name of tick: {i.upper()}\n' \
            f'amount of mints: {j}\n'
        await message.answer(card)
      mints = new_mints
    else:
      await message.answer("But no one came")


@dp.message(Command('CheckIfTrackerWorks'))
async def CheckIfWorks(message: types.Message):
  mints = await main_scrap()
  for i, j in sorted(mints.items(), key=lambda kv: kv[1], reverse=True):
    card = f'Name of tick: {i.upper()}\n' \
        f'How many mints there: {j}\n' \
        f'THIS ONE IS RIGHT MEOW'
    await message.answer(card)


@dp.message(Command('TurnOFFSiteTracker'))
async def SiteTrackerOFF(message: types.Message):
  global WhileOption
  if WhileOption is True:
    WhileOption = False
    await message.answer('Site Tracker has been successfully disabled')
  elif WhileOption is False:
    await message.answer('Site Tracker already disabled')


async def main():
  await dp.start_polling(bot)


if __name__ == "__main__":
  asyncio.run(main())
