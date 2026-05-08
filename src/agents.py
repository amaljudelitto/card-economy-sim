import random

def random_agent(player):
    """Plays valid cards completely at random."""
    playable = [c for c in player.hand if c.cost <= player.mana]
    played = []
    current_mana = player.mana
    
    random.shuffle(playable)
    for card in playable:
        if card.cost <= current_mana:
            played.append(card)
            current_mana -= card.cost
            
    return played

def heuristic_agent(player):
    """Greedy algorithm: prioritizes playing the highest damage cards first."""
    playable = sorted([c for c in player.hand if c.cost <= player.mana], 
                      key=lambda x: x.damage, reverse=True)
    played = []
    current_mana = player.mana
    
    for card in playable:
        if card.cost <= current_mana:
            played.append(card)
            current_mana -= card.cost
            
    return played
