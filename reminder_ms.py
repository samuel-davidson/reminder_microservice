# REMINDER MICROSERVICE
    # Implement a library reminder microservice that lets users know how long it has been since
        # they have been active.

import zmq
from datetime import datetime, timedelta

def process_dates(dates_string):
    """ Process the dates and titles from the incoming string. """
    entries = dates_string.split(';')                               # split string
    titles = []
    dates = []
    for i in range(1, len(entries), 2):                             # traverse the string and split dates and times into two lists
        title = entries[i - 1]
        date_str = entries[i]
        date = datetime.strptime(date_str, "%m%d%Y")
        dates.append(date)
        titles.append(title)
    return dates, titles                                            # return lists

def get_recent_entries(dates, titles):
    """ Check for entries and updates within the last week. """
    now = datetime.now()                                                                    # get current time
    one_week_ago = now - timedelta(days=7)                                                  # get 7 days ago for limit
    recent_titles = [titles[i] for i, date in enumerate(dates) if date >= one_week_ago]
    if recent_titles:
        if len(recent_titles) >= 3:
            return (
                f"You've had a busy week! Entries added or updated in the last week: "
                f"{', '.join(recent_titles)}"
            )
        else:
            return (
                f"Entries added or updated in the last week: "
                f"{', '.join(recent_titles)}"
            )
    else:
        if dates:
            last_entry_date = max(dates)
            days_since_last_entry = (now - last_entry_date).days
            return f"No recent updates to your library. Days since last entry: {days_since_last_entry}"
        else:
            return "No titles in library."

def main():
    context = zmq.Context()
    # Create a SUB socket for receiving messages
    subscriber = context.socket(zmq.SUB)
    subscriber.bind("tcp://*:5555")
    subscriber.setsockopt_string(zmq.SUBSCRIBE, "")

    # Create a REP socket for sending responses
    responder = context.socket(zmq.REP)
    responder.bind("tcp://*:5556")

    while True:
        # Receive a message from the publisher
        dates_string = subscriber.recv_string()
        # Process the received message
        dates, titles = process_dates(dates_string)
        # Determine the reminder string
        reminder_message = get_recent_entries(dates, titles)
        # Send the reminder back
        responder.send_string(reminder_message)

if __name__ == "__main__":
    main()



