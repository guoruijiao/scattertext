from unittest import TestCase

from scattertext.IndexStore import IndexStore


class TestIndexStore(TestCase):
	def test_main(self):
		index_store = IndexStore()
		self.assertEqual(index_store.getidx('a'), 0)
		self.assertEqual(index_store.getidx('b'), 1)
		self.assertEqual(index_store.getidx('a'), 0)
		self.assertEqual(index_store.getval(0), 'a')
		self.assertEqual(index_store.getval(1), 'b')
		self.assertTrue('a' in index_store)
		self.assertFalse('c' in index_store)
		self.assertFalse(0 in index_store)
		self.assertTrue(index_store.hasidx(0))
		self.assertFalse(index_store.hasidx(2))
		self.assertEqual(index_store.getnumvals(), 2)
		self.assertEqual(list(index_store.items()), [(0, 'a'), (1, 'b')])

	def test_batch_delete_copy(self):
		index_store = IndexStore()
		self.assertEqual(index_store.getidx('a'), 0)
		self.assertEqual(index_store.getidx('b'), 1)
		self.assertEqual(index_store.getidx('c'), 2)
		self.assertEqual(index_store.getidx('d'), 3)
		with self.assertRaises(KeyError):
			new_idx_store = index_store.batch_delete(['e', 'c'])
		new_idx_store = index_store.batch_delete(['b','c'])
		self.assertEqual(new_idx_store.getidx('a'), 0)
		self.assertEqual(new_idx_store.getidx('c'), 1)
		self.assertEqual(new_idx_store.getidx('e'), 2)
		self.assertEqual(index_store.getidx('d'), 3)
		self.assertEqual(index_store.getidx('c'), 2)
		self.assertEqual(index_store.getidx('b'), 1)
		self.assertEqual(index_store.getidx('a'), 0)