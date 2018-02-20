from unittest import TestCase

from .utils import dynamicdefaultdict


class TestDynamicDefaultDict(TestCase):
    def test_default_factory_can_return_key_for_missing_item(self):
        test_dict = dynamicdefaultdict(lambda key: key)

        self.assertEqual(test_dict['missing_key'], 'missing_key')