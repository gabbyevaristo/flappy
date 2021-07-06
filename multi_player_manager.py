class MultiPlayerManager:

    def __init__(self):
        self.players_connected = 0
        # These initial values are overwritten by the player's actual y values
        self.y_positions = {0: 355, 1: 355}
        self.winner = None


    def increase_connection(self):
        self.players_connected += 1


    def are_both_connected(self):
        return self.players_connected == 2


    def set_player_y(self, player, y):
        self.y_positions[player] = y


    def set_winner(self, player):
        self.winner = 0 if player == 1 else 1


    def get_player_y(self, player):
        return self.y_positions[player]


    def get_opponent_y(self, player):
        if player == 0:
            return self.y_positions[1]
        else:
            return self.y_positions[0]


    def get_winner(self):
        return self.winner
