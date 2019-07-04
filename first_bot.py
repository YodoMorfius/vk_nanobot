import vk_api
import random
from config import *

vkBot = vk_api.VkApi(token = BOT_TOKEN)

def write_msg(user_id, text):
    vkBot.method('messages.send',
                 {'user_id': user_id,
                  'message': text,
                  'random_id': random.randint(0, 2147483648)})

lp_server=vkBot.method('messages.getLongPollServer',
                       {'lp_version': 3,
                        'need_pts' : 0})
print(lp_server)
ts, server, key=lp_server['ts'], lp_server['key'], lp_server['server']
write_msg(461394843, 'Привет!')