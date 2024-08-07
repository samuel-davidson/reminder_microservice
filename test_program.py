import zmq
import time


def run_publisher():
    """ Send messages to the microservice. """
    context = zmq.Context()                                             # setup to send outgoing string
    send = context.socket(zmq.REQ)
    send.bind("tcp://*:3000")
    data = "Book1;07012024;Book2;07102024;Book3;06252024"               # Example data to send
    send.send_string(data)                                              # Send data
    time.sleep(2)                                                       # Give time to process data


def run_client():
    """ Send a request to the microservice and receive responses. """
    context = zmq.Context()                                             # setup to receive incoming message
    receive = context.socket(zmq.REP)
    receive.connect("tcp://localhost:3005")
    response = receive.recv_string()
    print("Reminder: ", response)                                       # print response


if __name__ == "__main__":
    run_publisher()                                                     # Run the publisher to send data
    time.sleep(2)                                                       # Give time for the microservice to process the data
    run_client()                                                        # Run the client receive the reminder service