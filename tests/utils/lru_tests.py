from __future__ import absolute_import

from opbeat.utils.lru import LRUCache
from tests.utils.compat import TestCase


class LRUTest(TestCase):
    def test_insert_overflow(self):

        lru = LRUCache(4)

        for x in range(6):
            lru.set(x)

        self.assertFalse(1 in lru)
        for x in range(2, 6):
            self.assertTrue(x in lru)
