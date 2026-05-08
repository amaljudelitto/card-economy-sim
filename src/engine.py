import random

class Card:
    def __init__(self, card_id, name, cost, damage):
        self.id = card_id
        self.name = name
        self.cost = cost
        self.damage = damage

class Player:
    def __init__(self, player_id, deck):
        self.id = player_id
        self.hp = 20
        self.mana = 0
        self.max_mana = 0
        self.deck = deck.copy()
        random.shuffle(self.deck)
        self.hand = []
        self.cards_played_this_match = []
        self.draw_initial_hand()

    def draw_initial_hand(self):
        for _ in range(4):
            self.draw_card()

    def draw_card(self):
        if self.deck:
            self.hand.append(self.deck.pop(0))

class GameState:
    def __init__(self, p1_deck, p2_deck):
        self.p1 = Player(1, p1_deck)
        self.p2 = Player(2, p2_deck)
        self.turn_count = 0
        self.current_player = self.p1
        self.opponent = self.p2
        self.winner = None

    def switch_turns(self):
        self.current_player, self.opponent = self.opponent, self.current_player

    def play_turn(self, agent_logic):
        if self.current_player.id == 1:
            self.turn_count += 1
            
        if self.current_player.max_mana < 10:
            self.current_player.max_mana += 1
            
        self.current_player.mana = self.current_player.max_mana
        self.current_player.draw_card()

        # Execute agent logic
        cards_to_play = agent_logic(self.current_player)
        
        for card in cards_to_play:
            self.current_player.mana -= card.cost
            self.opponent.hp -= card.damage
            self.current_player.hand.remove(card)
            self.current_player.cards_played_this_match.append(card.name)
            
            if self.opponent.hp <= 0:
                self.winner = self.current_player.id
                return True 
                
        self.switch_turns()
        return False
