import smtplib

g_email = ""
g_password = ""

y_email = ""
y_password = ""

"""
connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=g_email, password=g_password)
connection.sendmail(
    from_addr=g_email, 
    to_addrs=y_email, 
    msg="Subject:Hello\n\nThis is the body of my email.")
connection.close()
"""
"""
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=g_email, password=g_password)
    connection.sendmail(
        from_addr=g_email, 
        to_addrs=y_email, 
        msg="Subject:Hello\n\nThis is the body of my email.")
"""

with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as  connection:
    connection.starttls()
    connection.login(user=y_email, password=y_password)
    connection.sendmail(
        from_addr=y_email, 
        to_addrs=g_email, 
        msg="Subject:Hello\n\nThis is the body of my email.")
