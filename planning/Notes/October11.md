# Dice System
for dice system, dice should only correspond to the type of moves in your team and shouldn't contains all type of pokemon

# Database
Player's pokemon team table:
    player_id: FK
    team_id: PK

Player's active pokemon team table:
    player_id: FK
    team_id: FK


Pokemon's moves table:
    player_id: FK
    pokemon_id: FK
    move_id: FK
    slot: SMALLINT

Pokemon's table:
    pokemon_id: PK INT
    name: VARCHAR(100)
    description: TEXT
    primary_type: VARCHAR(20)
    secondary_type: VARCHAR(20)

    stat: JSON
        {
            "base_hp": int,
            "base_attack": int,
            "base_defense": int,
            "base_sp_attack": int,
            "base_sp_defense": int,
            "base_speed": int
        }