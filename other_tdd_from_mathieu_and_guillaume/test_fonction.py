import unittest
from main import theBossFunction


class TestBossFunction( unittest.TestCase ):

    def setUp( self ):
        self.bossDict = theBossFunction()

    def test_formatInput( self ):
        self.assertIsInstance( self.bossDict, dict )
        length = len( self.bossDict )
        self.assertEqual( length, 2 )

    def test_valueInputKey( self ):
        bossKeys = self.bossDict.keys()
        self.assertIn( "chameau", bossKeys )
        self.assertIn( "dromadaire", bossKeys )

    def test_valueInputValue( self ):
        self.assertIsInstance( self.bossDict["chameau"], int )
        self.assertIsInstance( self.bossDict["dromadaire"], int )
        self.assertGreaterEqual( self.bossDict["chameau"], 0 )
        self.assertGreaterEqual( self.bossDict["dromadaire"], 0 )

    def test_calculDeBosses( self ):
        testChameau = self.bossDict["chameau"] * 2
        testDromadaire = self.bossDict["dromadaire"] * 1
        res = testChameau + testDromadaire
        self.assertEqual( res, theBossFunction( self.bossDict ) )

unittest.main()
