import unittest
import compteur


class TestCompteurFunction( unittest.TestCase ):

    def test_entry_is_string( self ):
        self.assertIsInstance( compteur.my_string, str )

    def test_result_is_dict( self ):
        self.assertIsInstance( compteur.result, dict )

    def test_clef_dict( self ):
        self.assertIsInstance( compteur.result.key(), str )

    def test_length_clef_dict( self ):
        self.assertEqual( len( compteur.result.key() ), 1 )

    def test_value_dict( self ):
        self.assertIsInstance( compteur.result.value(), int )

    def test_total_value( self ):
        string1 = len( compteur.my_string )
        values_count = sum( compteur.result.value() )
        self.assertEqual( string1, values_count )


unittest.main()