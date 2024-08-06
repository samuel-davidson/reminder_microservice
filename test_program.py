import zmq
import time


def run_publisher():
    """ Send messages to the microservice. """
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://127.0.0.1:5555")

    # Example data to send (format: title;mmddyyyy;title;mmddyyyy;...)
    data = "Book1;07012024;Book2;07102024;Book3;06252024"
    print("Publishing data:", data)

    # Send data
    publisher.send_string(data)
    print("Data sent.")

    # Give some time for the data to be processed by the microservice
    time.sleep(2)


def run_client():
    """ Send a request to the microservice and receive responses. """
    context = zmq.Context()
    requester = context.socket(zmq.REQ)
    requester.connect("tcp://127.0.0.1:5556")

    print("Requesting reminder...")
    requester.send_string("REQUEST")

    # Wait for the microservice to process the request and send a response
    response = requester.recv_string()
    print("Received response:", response)


if __name__ == "__main__":
    # Run the publisher to send data
    run_publisher()

    # Give some time for the microservice to process the data
    time.sleep(2)

    # Run the client to request and receive the response
    run_client()