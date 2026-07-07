# to import - import datetime form datetime
    datetime.now() gives current date and time 
        op: 2026-07-07 14:01:35.123456    - local_time
    datetime.now(timezone.utc)
        op: 2026-07-07 08:16:35.123456+00:00   - utc_time(needs to import timezone from datetime())

    - to convert string into datetime object use
        datetime.fromisoformat(date_time_in_string)

---------------------------------------------------------------------------------------

# use strf() to format time
    Common strftime() codes:
        Code   Meaning     Example
        %H     24-hour     14
        %I     12-hour     02
        %M     Minutes     35
        %S     Seconds     42
        %p     AM/PM       PM
        %Y     Year       2026
        %m     Month       07
        %d     Day         07

    examples:
        # 2026-07-07
        datetime.now().strftime("%Y-%m-%d")

        # 14:35:20
        datetime.now().strftime("%H:%M:%S")

        # 02:35 PM
        datetime.now().strftime("%I:%M %p")

        # Tuesday, 07 July 2026
        datetime.now().strftime("%A, %d %B %Y")