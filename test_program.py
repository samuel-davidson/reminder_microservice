import zmq
import time


def run_publisher():
    """ Send messages to the microservice. """
    context = zmq.Context()                                             # setup to send outgoing string
    send = context.socket(zmq.REQ)
    send.bind("tcp://*:3000")

    # lines below are commented out to test different responses from the microservice
    # data = "Book1;07122024;Book2;07192024;Book3;06252024"
    # data = "Book1;07122024;Book2;07192024;Book3;06252024;Book4;08032024;Book5;08052024"

    data = "Book1;07122024;Book2;07192024;Book3;06252024;Book4;08032024;Book5;08052024;Book6;08062024"               # Example data to send
    send.send_string(data)                                              # Send data
    time.sleep(2)                                                       # Give time to process data


def run_client():
    """ Receive responses from microservice. """
    context = zmq.Context()                                             # setup to receive incoming message
    receive = context.socket(zmq.REP)
    receive.connect("tcp://localhost:3005")
    response = receive.recv_string()
    print(response)                                       # print response


if __name__ == "__main__":
    run_publisher()                                                     # Run the publisher to send data
    time.sleep(2)                                                       # Give time for the microservice to process the data
    run_client()                                                        # Run the client receive the reminder service