import unittest
import time
from store import Store

if __name__ == "__main__":

    class TestStore(unittest.TestCase):

        def test_set(self):
            Store.set('name', 'Mike')
            self.assertIn('name', Store._store.keys())
            self.assertEqual('Mike', Store._store.get('name')[0])

            Store.set('name', 'Joe')
            self.assertIn('name', Store._store.keys())
            self.assertEqual('Joe', Store._store.get('name')[0])

            Store.set(key='name', value='Mike', duration=30)
            self.assertIn('name', Store._store.keys())
            self.assertEqual('Mike', Store._store.get('name')[0])

            # Check that it won't accept a non-numeric duration
            with self.assertRaises(TypeError):
                Store.set(key='name', value='Mike', duration='x')

        def test_get(self):
            Store.set('name', 'Mike')
            self.assertEqual('Mike', Store.get('name'))

            Store.set(key='name', value='Mike', duration=30)
            self.assertEqual('Mike', Store.get('name'))

            Store.set(key='country', value='Germany', duration=-30)
            self.assertNotIn('country', Store._store.keys())
            self.assertIsNone(Store.get('country'))

        def test_delete(self):
            Store.set('name', 'Mike')
            self.assertEqual('Mike', Store.get('name'))
            Store.delete('name')
            self.assertNotIn('name', Store._store.keys())

        def test_clean(self):
            Store.set(key='name', value='Mike', duration=1)
            Store.set(key='country', value='Germany', duration=30)
            Store.set(key='hobby', value='soccer', duration=60)
            Store.set(key='age', value=35, duration=1)

            self.assertIn('name', Store._store.keys())
            self.assertIn('country', Store._store.keys())
            self.assertIn('age', Store._store.keys())
            self.assertIn('hobby', Store._store.keys())

            time.sleep(2)
            Store.clean()

            self.assertNotIn('name', Store._store.keys())
            self.assertIn('country', Store._store.keys())
            self.assertNotIn('age', Store._store.keys())
            self.assertIn('hobby', Store._store.keys())

        def test_purge(self):
            Store.set(key='name', value='Mike')
            Store.set(key='country', value='Germany')
            Store.set(key='age', value=35)
            Store.set(key='hobby', value='soccer')

            self.assertIn('name', Store._store.keys())
            self.assertIn('country', Store._store.keys())
            self.assertIn('age', Store._store.keys())
            self.assertIn('hobby', Store._store.keys())

            Store.purge()

            self.assertEqual({}, Store._store)

    unittest.main(verbosity=2)
