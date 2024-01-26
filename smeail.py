import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Paramètres du serveur SMTP
smtp_server = "mail.tandisgicaedef.cm"
smtp_port = 587  # Le port SMTP peut varier selon la configuration du serveur

# Informations d'authentification
smtp_username = "tandis@tandisgicaedef.cm"
smtp_password = "*Severin123"

# Destinataire et expéditeur
from_email = "tandis@tandisgicaedef.cm"
to_email = "nzomutchawilfrid@gmail.com"

# Objet du message
subject = "Objet de votre e-mail"

# Corps du message
body = "Corps de votre e-mail."

# Création de l'objet MIMEMultipart
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject

# Ajout du corps du message
msg.attach(MIMEText(body, 'plain'))

# Connexion au serveur SMTP
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Utilisation de TLS, peut varier selon la configuration du serveur

# Authentification
server.login(smtp_username, smtp_password)

# Envoi de l'e-mail
server.sendmail(from_email, to_email, msg.as_string())

# Fermeture de la connexion
server.quit()
