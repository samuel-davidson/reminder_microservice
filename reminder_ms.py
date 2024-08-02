# REMINDER MICROSERVICE
    # Implement a library reminder microservice that lets users know how long it has been since
        # they have been active.
    # receives string format and returns string format
    # if not string format, then maybe json? with the list of the entries for that
        # user and the date of entry/ last update?
    # incoming string should be:
        # list of titles updated in last 7 days
        # if none:
            # return : "You have no new entries in the past 7 days! Would you like to make a new entry?"
        # else:
            # return : "Here are your most recent additions to the library: [List of titles]
    # communication with zeroMQ


    # USER STORIES

    # Duration Since Last Use
        # As an existing user, I want to be reminded when I haven’t updated my library in a certain
            # amount of days so that I can get back to using the software
                        # Given the user logs into the software, when they get to their library, then they are
                            # reminded that they have yet to update the library in X amount of days

    # Set Reminders
        # As a new user, I want to set reminders to read after 7 days of no activity so that I can stay
            # on top of my reading
                        # Given the new user sets up their new profile, when they reach the profile
                            # registration page, then they are given the option to set a reminder time limit

    # Titles Recently Updated
        # As a user, I want to be reminded of the titles that I updated or added to in the last week so
            # that I can know which books are new in my library.
                        # Given the user logs into the software, when they get to their library, then they are
                            # notified of the titles added to the library within the last week.





# Write a small test program to demonstrate that the microservice can be called and respond with data.
# Add a README to your GitHub (or update it if you already have one) that
    # contains your communication contract. (Once you define it, don't change it!
    # Your teammate is relying on you.) README must contain...
# Clear instructions for how to programmatically REQUEST data from the microservice
    # you implemented. Include an example call.
# Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.
# UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that
    # your teammate (and your grader) will understand.
# Write a mitigation plan by answering these questions:
# For which teammate did you implement “Microservice A”?
# What is the current status of the microservice? Hopefully, it’s done!
# If the microservice isn’t done, which parts aren’t done and when will they be done?
# How is your teammate going to access your microservice? Should they get your code from
    # GitHub? Should they run your code locally? Is your microservice hosted somewhere? Etc.
# If your teammate cannot access/call YOUR microservice, what should they do?
    # Can you be available to help them? What’s your availability?
# If your teammate cannot access/call your microservice,
    # by when do they need to tell you?
# Is there anything else your teammate needs to know? Anything
    # you’re worried about? Any assumptions you’re making? Any other mitigations
    # / backup plans you want to mention or want to discuss with your teammate?