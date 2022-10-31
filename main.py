# Desktop-Notification
# Destop-Notification
from plyer import notification

notification_title = 'My application'
notification_message = 'Thank you. Have a Good Day.'

notification.notify(
    title=notification_title,
    message=notification_message,
    app_icon=None,
    timeout=10,
    toast=False
)
