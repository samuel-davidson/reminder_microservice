# Library Reminder Microservice
## Overview
This microservice is a reminder service for a library application.  It receives as a string
the titles in a user's library and last edit/ add date for those titles, and returns a 
string containing the titles which were added or edited in the last week.  If the user added
or edited more than 3 titles in the past week, an additional encouraging message is also sent
in return.  If there are no such titles, then the service returns the amount of days since the
most recent update or addition of a title to that user's library.   
## Requirements
- Python 3.x
- ZeroMQ Library
- DateTime Module
- Time Module
## Installation
##### 1. Clone git repository to your local machine

    git clone https://github.com/samuel-davidson/reminder_microservice.git
    
##### 2. Navigate to the project directory

    cd reminder-microservice

##### 3. Set up a virtual environment and activate it

    python3 -m venv venv

    source venv/bin/activate

##### 4. Install required dependencies

    pip install -r requirements.txt

## Usage
### Running the Microservice
##### 1. Start the reminder service
    python3 reminder_ms.py
   
This starts the client which will wait for an incoming string.
##### 2. Start the test program

    python3 test_program.py
This starts the server which receives the string and returns a reminder message.
### Example Request
#### Request Data:
1. Collect all the titles in the library with their last edit/ add date in the following string format: 
            "title;mmddyyyy;title;mmddyyyy;title;mmddyyyy" etc...
2. Use ZeroMQ send_string() method to send to the string to microservice
#### Receive Data
1. Use ZeroMQ receive_string() method to get the reminder message.
2. Print the reminder message
#### Example:
    def main():
        data = "Book1;07122024;Book2;07192024;Book3;06252024;Book4;08032024;Book5;08052024;Book6;08062024"               # Example data to send
        send.send_string(data)
        response = receive.recv_string()
        print(response)
    



### UML sequence diagram

![UML Diagram - Frame 1.jpg](..%2F..%2FDesktop%2FFILES%2FOSU%2FQ4%20-%20Summer%20%2724%2FCS%20361%2FHW%2F8%2FUML%20Diagram%20-%20Frame%201.jpg)