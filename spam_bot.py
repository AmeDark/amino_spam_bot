try: import AminoLab, time
except:
	import os
	os.system("pip install AminoLab && clear")
	import AminoLab, time

client = AminoLab.Client()

while True:
	try:
		email = input("Email >> ")
		password = input("Password >> ")
		client.auth(email=email, 		password=password)
		print()
		break
		
	except:
		print("\nError.\n")

while True:
	try:
		clients = client.my_communities()
		for x, name in enumerate(clients.name, 1):
 		   print(f"{x}.{name}")

		ndc_Id = clients.ndc_Id[int(input("Select the community >> ")) - 1]
		print()
		break
		
	except:
		print("\nError.\n")

while True:
	try:
		chats = client.my_chat_threads(ndc_Id=ndc_Id, size=100)

		for z, title in enumerate(chats.title, 1):
 		   print(f"{z}.{title}")

		thread_Id = chats.thread_Id[int(input("Select The Chat >> ")) - 1]
		print()
		break
		
	except:
		print("\nError.\n")
   
msg = input("Сообщение >> ")
print()

while True:
	try:
		msg_type = int(input("Тип сообщения >> "))
		print()
		break
	
	except:
		print("\nError.\n")

count = int(input("Количество ботов >> "))

from threading import Thread

def spamer():
	global times
	global msg
	
	global ready
	
	while True:
		if ready == False: time.sleep(1)
		else: break
		
	while True:
		try:
			client.send_message(ndc_Id=ndc_Id, thread_Id=thread_Id, message = msg, message_type = msg_type)
				
			times += 1

		except BaseException:
			spamer()

print("\n")
ready = False
bots = 0
for i in range(count):
	try:
		Thread(target = spamer).start()
		bots += 1

	except: pass
	
	print(f"\033[AВсего сгенерировано ботов: {bots} / {count}.         ")
	
ready = True
        
print("\nCreated by Ame.\n\n")

times = 0

while True:
	print(f"\033[AВсего отправлено сообщений: {times}.         ")
	
	time.sleep(0.1)
