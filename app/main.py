import socket

def generate_response():
    response = [0 for _ in range(12)] #it's always 12 bytes long
    response[0] = (1234 >> 8) & 255 #packet ID in big-endian format; shifts the bits of 1234 right by 8 and masks with 255
    response[1] = 1234 & 255 #mask with 255 to get the low byte
    response[2] = 128 #corresponds to 10000000; qr bit = 1 now as expected
    return bytes(response)

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("127.0.0.1", 2053))
    
    while True:
        try:
            buf, source = udp_socket.recvfrom(512)
    
            response = generate_response()
            print(response)
    
            udp_socket.sendto(response, source)
        except Exception as e:
            print(f"Error receiving data: {e}")
            break


if __name__ == "__main__":
    main()
