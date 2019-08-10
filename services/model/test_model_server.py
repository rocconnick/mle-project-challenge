import hashlib
import unittest

import model_server


class TestModelServer(unittest.TestCase):

    def test_check_hash(self):
        """
        Test the check_hash() function.
        """

        test_object = bytes([1, 2, 3])
        expected_hash = hashlib.sha1(test_object).hexdigest()

        # Test desired behavior, happily return None
        self.assertIsNone(model_server.check_hash(test_object, expected_hash))

        # Test raise on invalid hash
        self.assertRaises(ValueError,
                          model_server.check_hash,
                          test_object,
                          "deadbeef")
