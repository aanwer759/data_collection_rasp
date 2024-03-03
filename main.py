import socket 
from kafka import KafkaProducer

host = "0.0.0.0"
port = 3333

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(5)
print("making kafka producer : ")
print("TCP Server listening on port : ",port)

while True:
    client_socket, client_address = sock.accept()
    print ("Socket accepted from address :" , client_address)

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            received_data = data.decode("utf-8")
            print ("recieved data",received_data)
            producer.send("test-events",received_data.encode('utf-8'))
            producer.flush()

    except Exception as e:
        print ("error recieving data" , e)
    finally:
        client_socket.close()
        print ("client socket closed")


