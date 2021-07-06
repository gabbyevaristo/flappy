class MultiPlayerManager:

    def __init__(self):
        self.players_connected = 0
        self.y_positions = {0: 0, 1: 0}     # Starting y position for players


    def increase_connection(self):
        self.players_connected += 1


    def are_both_connected(self):
        return self.players_connected == 2


    def set_player_y(self, player, y):
        self.y_positions[player] = y


    def get_player_y(self, player):
        return self.y_positions[player]
