import random

def email_generator():
    random_value = random.randrange(1, 10)
    mail_server = 'mail.ru'
    random_mail = random.sample('abcdefghijklmnopqrstuvwxyz0123456789', random_value)
    random_mail = ''.join(random_mail)
    random_mail = random_mail + '@' + mail_server
    return random_mail
