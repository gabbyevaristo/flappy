class MultiPlayerManager:

    def __init__(self):
        self.players_connected = 0
        # These initial values are overwritten by the player's actual y values
        self.y_positions = {0: 0, 1: 0}
        self.rematch = {0: True, 1: True}
        self.winner = None


    def increase_connection(self):
        self.players_connected += 1


    def are_both_connected(self):
        return self.players_connected == 2


    def game_over(self):
        self.winner = None
        self.rematch[0] = False
        self.rematch[1] = False


    def set_rematch(self, player):
        self.rematch[player] = True


    def get_rematch(self):
        if self.rematch[0] and self.rematch[1]:
            return True
        return False


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
