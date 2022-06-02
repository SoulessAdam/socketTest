import socket
import struct
import ctypes


m_IP = socket.gethostbyname(socket.gethostname())
m_PORT = 6969
ADDR = (m_IP, m_PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

packetType = {
    'motion': 0,
    'session':1,
    'lap_data':2,
    'event':3,
    'participants':4,
    'cat_setups':5,
    'car_telemetry':6,
    'car_status':7,
    'classification':8,
    'lobby_info':9,
    'car_damage':10,
    'session_history':11
}


def parseLapData(data):
    lastLapTimeInMS = ctypes.c_uint32(data[:32])
    currentLapTimeInMs = ctypes.c_uint32(data[33:65])

    return


def parseHeader(packet):
    print("<<< [PARSER] Beginning Parse")
    a = packet[6]#struct.unpack('<B', packet[6])
    print(">>> [PARSER]", a)
    packet = packet[64:]

def startRecv():
    print("[UDP] Listening on:", ADDR)
    while 1:
        bytesAddressPair = server.recvfrom(50000)
        print("<<< [UDP]",bytesAddressPair[1])
        message = bytesAddressPair[0]
        parseHeader(message)


startRecv()