#!/usr/bin/env python3
# Copyright 2022 Darsox <https://t.me/DarsoX>
# All rights reserved

import vk_api, random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


'''
Получите "GROUPS_TOKEN" через сайт: https://vkhost.github.io/ нажмите "Настройки" - "Сообщество". Укажите: "ID Приложения" (6121396 - VkAdmin) и "ID сообщества" на ID вашего сообщества.
Get "GROUPS_TOKEN" through the site: https://vkhost.github.io/ click "Settings" - "Community". Specify: "Application ID" (6121396 - VkAdmin) and "Community ID" for your community ID.
'''
vkExample = vk_api.VkApi(token = :"GROUPS_TOKEN") 


'''
Замените CLUB_ID на в ID сообщества что идет после: "vk.com/club". ID должен быть положительным без знака - и числом
Replace CLUB_ID with the community ID that comes after: "vk.com/club". The ID must be positive, unsigned - and a number.
'''

lp = VkBotLongPoll(vkExample, CLUB_ID) 

bugChatId = 0 #PeerId чата, куда будет приходить сообщение с ошибками/PeerId of the chat where the error message will be sent.




def msgSend(peer,ms,att = None, keyb = None):
	msId = self.vk.method('messages.send', {'peer_id': peer,'random_id': random.randint(0, 2**64), 'message': ms, 'attachment': att,'keyboard': keyb})
    
	return msId

def bot():
    while True:
        try:
            for event in lp.listen():
				if event.type == VkBotEventType.MESSAGE_NEW:
					event_obj = event.obj.get('message')
					userId = event_obj.get('from_id')
					peerId = event_obj.get('peer_id')
					text = event_obj.gey('text')
					ms = text.lower()
					
					if ms == "peer":
						msgSend(peerId, f"PeerId чата: {peerId}")
					
					if ms == "привет":
						msgSend(peerId, "Ну привет")
					if ms == "арт":
						msgSend(peerId,"",att = "photo-62399927_457270315")
        except requests.exceptions.ReadTimeout:
            msgSend(bugChatId, '&#9888; Ошибка: Перезагрузка вк.')
		except Exception as e:
			err_tx = f'&#9888; Ошибка: {e}\n&#128169; Пользователь: @id{user_id} (Профиль)\n&#129511; Беседа: {peer_id}\n&#128140; Текст сообщения: {text_id}\n\n&#9881; Детальная ошибка:\n\n {traceback.format_exc()}'
            msgSend(bugChatId, err_tx)
            print(e)
			

if __name__ == '__main__':
    bot()
