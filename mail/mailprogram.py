import send_mail as sm

subject = input("Bitte mach Betreff: ")
content = input("Bitte mach Content: ")

sm.send_mail(subject=subject, content=content, person="Bewegungslogger")
