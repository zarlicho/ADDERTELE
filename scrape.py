from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import ChannelParticipantsSearch
import sys
import csv
import traceback
import time
import random
import re


api_id = 19167912       # YOUR API_ID
api_hash = '6c9626ac600dab939cf2c03308f23c3a'        # YOUR API_HASH
phone = '+6285157905521'        # YOUR PHONE NUMBER, INCLUDING COUNTRY CODE
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

offset = 0
limit = 100
all_participants = []
channel = 'https://t.me/belajarngodingbareng'
targetGroup = 'https://t.me/johnStillinTheSchool'
client(JoinChannelRequest(targetGroup))
while True:
    participants = client(GetParticipantsRequest(
        channel, ChannelParticipantsSearch(''), offset, limit,
        hash=0
    ))
    if not participants.users:
        break
    all_participants.extend(participants.users)
    offset += len(participants.users)
    for user in all_participants:
        print(user.first_name, user.last_name, user.username)
        # add user to group
        try:
            client(InviteToChannelRequest(
                targetGroup,
                [user.id]
            ))
        except Exception as e:
            print(e) 
        time.sleep(20)