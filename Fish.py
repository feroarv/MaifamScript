import time
import asyncio
import sys
import random

from telethon import TelegramClient, events, utils, Button

api_id = 2578350
api_hash = '4ba467bcddfae36a61a4ed78b653372f'
sesi_file = 'Neptune'

bot_id = 'KampungMaifamBot'
Area = input('Area = ')
Alat = input('Alat = ')

with TelegramClient(sesi_file, api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_message(bot_id, Area))
        @client.on(events.NewMessage(from_users=bot_id))
        async def handler(event):
            pesan = event.raw_text


            if "You've" in pesan:
                time.sleep(2)
                await event.respond(Area)
                print(pesan)
                return
                
            elif 'Your energy is too low' in pesan:
                time.sleep(1)
                await event.respond('/restore')
                print(time.asctime(), 'Isi Ulang Energi')
                return
                
            elif "not fishing" in pesan:
                time.sleep(2)
                await event.respond(Area)
                print('Lanjot')
                return
                
            elif 'restored' in pesan:
                time.sleep(1)
                await event.respond(Area)
                print('Lanjot')
                return
            
            else :
                time.sleep(2)
                await event.click(text=Alat)
                print(time.asctime(), 'Lempar pancingan')
                return
            
            
client.start()
client.run_until_disconnected()
print(time.asctime(), '-', 'Berhenti')
