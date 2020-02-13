import unittest
import distributeur


class DistribTest(unittest.TestCase):
    def floatMoney( self ):
        money = type(distributeur.money)
        testmoney = type(45.3)
        self.assertEqual(money, testmoney)

    def stockNotNull( self ):
        quantity = distributeur.Product.quantity
        self.assertNotEqual(quantity, 0)

    def selectCharExist( self ):
        selection = distributeur.Product.id
        self.assertEqual(type(selection), type('a'))

    def giveBack( self ):
        spend = distributeur.spend
        giveBack = distributeur.give_back
        self.assertLess(giveBack, spend)

    def giveBackNotMinus( self ):
        giveBack = distributeur.give_back
        self.assertLess(0, giveBack)

    def transactionTrue( self ):
        spend = distributeur.spend
        cost = distributeur.Product.cost
        total = spend > cost
        self.assertEqual(total, True)

    def transactionFalse( self ):
        spend = distributeur.spend
        cost = distributeur.Product.cost
        total = spend > cost
        self.assertEqual( total, False )
