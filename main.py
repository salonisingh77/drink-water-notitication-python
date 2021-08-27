import time
from plyer import notification
if __name__=="__main__":
    notification.notify(
        title="Please drink water now!",
        message="Water is your body's principal chemical component and makes up about 50% to 70% of your body weight. Your body depends on water to survive.",
        app_icon ="icon.ico",
        timeout=5
        
        
    )
    time.sleep(60*60)
