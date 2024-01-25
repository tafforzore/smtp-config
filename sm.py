import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Paramètres du serveur SMTP
smtp_server = 'mail.tandisgicaedef.cm'
smtp_port = 465  # Utilisez le port approprié pour votre configuration (peut être 465 pour SSL/TLS)
smtp_username = 'tandis@tandisgicaedef.cm'
smtp_password = '*Severin123'

# Paramètres de l'email
sender_email = 'tandis@tandisgicaedef.cm'
recipient_email = 'testpad24@gmail.com'
subject = 'Test SMTP'
body = 'Ceci est un test d\'envoi d\'email depuis Python.'

# Création de l'email
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Connexion au serveur SMTP avec SSL
try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_username, smtp_password)

        # Envoi de l'email
        server.sendmail(sender_email, recipient_email, message.as_string())
        print('Email envoyé avec succès!')

except Exception as e:
    print(f'Erreur lors de l\'envoi de l\'email : {e}')
