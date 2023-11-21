from prac_09.musician import Musician


class Band(Musician):

    def __init__(self, band_name):
        super().__init__(self)
        self.band_name = band_name
        self.band_players = {}

    def __str__(self):
        return f"{self.band_name} {self.band_players}".strip("{}")

    def add(self, player):
        if len(player.instruments) > 0:
            self.band_players[player.name] = player.instruments
        else:
            self.band_players[player.name] = ""

    def play(self):
        for player in self.band_players.keys():
            if self.band_players[player] != "":
                print(player, self.band_players[player])
            else:
                print(f"{player} needs an instrument")

