from datetime import datetime


def ig_fake():
    current_dateTime = datetime.now()
    month_txt = {
        1:"January",
        2:"February",
        3:"March",
        4:"April",
        5:"May",
        6:"June",
        7:"July",
        8:"August",
        9:"September",
        10:"October",
        11:"November",
        12:"December",
    }
    now = current_dateTime.now()
    time = now.strftime("%I:%M %p")
    ig_fake_datatime = f"{month_txt[current_dateTime.month]} {current_dateTime.day} at {time} (PDT)"
    
    return ig_fake_datatime