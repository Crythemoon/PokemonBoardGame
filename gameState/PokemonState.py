class PokemonState:
    def __init__(self):
        self.currentHealth = 0
        self.maxHealth = 0
        self.position = (0, 0)

        # Major Pokemon Status Conditions: "paralyzed", "asleep", "frozen", "poisoned", "burned"
        self.status_condition = set()

        # Stat modifiers for each stat type
        self.stat_modifiers = []

        # Temporary special effects that can be applied to the Pokemon, such as "double damage" or "immunity"
        self.effects = []

        # Things pokemon is restricted from doing, such as "cannot attack" or "cannot retreat"
        self.restrictions = set()

    def getPokemonStatus(self, playerID, pokemonID):
        pass