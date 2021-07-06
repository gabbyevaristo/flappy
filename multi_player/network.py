import socket
import pickle
import constants


class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host= socket.gethostbyname(socket.gethostname())
        self.port = constants.PORT_NUMBER
        self.address = (self.host, self.port)
        self.player_id = self.connect()


    def connect(self):
        ''' Connect to the server '''
        try:
            self.client.connect(self.address)
            # Receive player_id upon initial server connection
            return self.client.recv(2048).decode()
        except:
            pass


    def send(self, data):
        ''' Send data to the server and receive game manager object'''
        try:
            self.client.send(str.encode(data))
            response = self.client.recv(2048 * 2)
            if response:
                return pickle.loads(response)
            return response
        except socket.error as e:
            print(e)


    def get_player_id(self):
        return int(self.player_id)
