import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):

    def setUp(self):
        self.card_game = CardGame()

    def test_check_for_ace__false(self):
        card = Card("Club", 3)
        self.assertEqual(False, self.card_game.check_for_ace(card))

    def test_check_for_ace__true(self):
        card = Card("Heart", 1)
        self.assertEqual(True, self.card_game.check_for_ace(card))

    def test_highest_card__card1(self):
        card1 = Card("Heart", 12)
        card2 = Card("Diamond", 3)
        self.assertEqual(card1, self.card_game.highest_card(card1, card2))
        
    def test_highest_card__card2(self):
        card1 = Card("Diamond", 6)
        card2 = Card("Spade", 9)
        self.assertEqual(card2, self.card_game.highest_card(card1, card2))

    def test_cards_total(self):
        card1 = Card("Diamond", 12)
        card2 = Card("Diamond", 13)
        card3 = Card("Diamond", 11)
        cards = [card1, card2, card3]
        self.assertEqual("You have a total of 36", self.card_game.cards_total(cards))