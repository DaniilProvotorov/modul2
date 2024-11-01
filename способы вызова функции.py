def send_email(message, recipient, *, sender = "university.help@gmail.com"):
   x = '@'
   y = '.com'
   n = '.ru'
   m = '.net'
   if sender == recipient:
       print("Нельзя отправить письмо самому себе!")
   elif sender != "university.help@gmail.com":
       print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
   elif x in recipient and  y in recipient:
       print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
   elif x in recipient and n in recipient:
       print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
   elif x in recipient and m in recipient:
       print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
   else: print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)


send_email('wolf', 'mom@gmail.com')
