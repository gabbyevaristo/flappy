import socket
import pickle


class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host= socket.gethostbyname(socket.gethostname())
        self.port = 5555
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
        ''' Send data to the server '''
        try:
            self.client.send(str.encode(data))

            # If game, then deserialize the Manager object, else
            # decode the opponent's position
            if data == 'game':
                return pickle.loads(self.client.recv(2048 * 2))
            else:
                return self.client.recv(2048 * 2).decode()
        except socket.error as e:
            print(e)


    def get_player_id(self):
        return self.player_id
