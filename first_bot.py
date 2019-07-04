import vk_api
import random
from config import *

vkBot = vk_api.VkApi(token = BOT_TOKEN)

USER_ID = 461394843
text = 'Это сообщение отправлено с помощью vk_api'
result = vkBot.method('messages.send',
{'user_id' : USER_ID,
 'random_id' : random.randint(1, 2147483648),
 'message' : text})
print(result)