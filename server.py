import socket
from threading import Thread
import pickle
import multi_player_manager


class Server:

    def __init__(self):
        self.server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = 5555
        self.address = (self.host, self.port)
        self.game = None
        self.connections = 0
        self.max_connections = 2
        self.bind()


    def bind(self):
        ''' Bind socket to address '''
        try:
            self.server.bind(self.address)
        except socket.error as e:
            print(str(e))


    def open_server(self):
        self.server.listen(self.max_connections)
        print('[SERVER STARTED] Waiting for a connection')

        # Accepting connections
        while True:
            conn, addr = self.server.accept()
            print(f'Connected to: {addr}')

            self.connections += 1
            player_id = None

            # Create a new game when first player connects and assign them to player 0,
            # else set the next player to 1
            if self.connections == 1:
                self.game = multi_player_manager.MultiPlayerManager()
                player_id = 0
            else:
                player_id = 1
            self.game.increase_connection()

            thread = Thread(target=self.threaded_client, args=(conn, player_id))
            thread.start()


    def threaded_client(self, conn, player_id):
        # Send client what player they are on initial connection
        conn.send(str.encode(str(player_id)))

        reply = ''
        while True:
            try:
                # Get data from the client
                data = conn.recv(4096).decode()

                # If the game is still going
                if self.game:
                    if not data:
                        break
                    else:
                        # Set winner
                        if data == 'collide':
                            self.game.set_winner(player_id)
                        # Set opponent's position
                        elif data != 'game':
                            self.game.set_player_y(player_id, int(data))

                        # Always send game manager
                        reply = self.game
                        conn.sendall(pickle.dumps(reply))
                else:
                    break
            except:
                break

        print('[CONNECTION LOST] Connection closed')
        self.game = None
        self.connections -= 1
        conn.close()
