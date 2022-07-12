# from pynotifier import Notification


# Notification(
#     title= 'Hello',
#     description= 'Learn more and don\'t stop',
#     icon_path= '/home/rasmesxiii/Downloads/me.jpg',
#     duration=5,
#     urgency='normal'
# ).send()

from plyer import notification

title = 'check it out'
message = 'it work!'

notification.notify(title=title, message=message, timeout=8)