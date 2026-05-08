import pandas as pd
from engine import GameState, Card
from agents import heuristic_agent

def create_deck(include_op_card=False):
    deck = [
        Card(1, "Strike", 1, 2), Card(2, "Strike", 1, 2),
        Card(3, "Blast", 2, 4), Card(4, "Blast", 2, 4),
        Card(5, "Fireball", 3, 6), Card(6, "Fireball", 3, 6),
        Card(7, "Meteor", 5, 10), Card(8, "Meteor", 5, 10),
        Card(9, "Zap", 0, 1), Card(10, "Zap", 0, 1)
    ] * 2
    
    if include_op_card:
        # Intentionally inject a highly efficient card to test data extraction
        deck[0] = Card(11, "Broken_Sword", 1, 7)
        
    return deck

def run_monte_carlo(iterations=10000):
    match_logs = []
    
    for i in range(iterations):
        # P1 has standard deck, P2 has a deck with an overpowered card
        game = GameState(create_deck(), create_deck(include_op_card=True))
        
        while not game.winner and game.turn_count < 50:
            # Both players use the same logic to isolate deck balance as the variable
            game_over = game.play_turn(heuristic_agent)
            if game_over: break
            
        match_logs.append({
            'match_id': i,
            'winner': game.winner,
            'total_turns': game.turn_count,
            'p1_cards_played': ",".join(game.p1.cards_played_this_match),
            'p2_cards_played': ",".join(game.p2.cards_played_this_match)
        })

    df = pd.DataFrame(match_logs)
    output_path = "analysis/simulation_results.csv"
    df.to_csv(output_path, index=False)
    print(f"Simulation of {iterations} matches complete. Data saved to {output_path}")

if __name__ == "__main__":
    run_monte_carlo(50000)
