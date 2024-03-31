from unittest import TestCase

from animal_shelter_queue import AnimalShelterQueue


class AnimalShelterQueueTests(TestCase):
    def setUp(self):
        self.asq = AnimalShelterQueue()
        
        self.asq.enqueue(is_cat=True)
        self.asq.enqueue(is_cat=True)
        self.asq.enqueue(is_cat=False)
        self.asq.enqueue(is_cat=False)
        
    def test_enqueue(self):
        # see setUp function
        self.assertEqual(self.asq.cat_root.data, 0)
        self.assertEqual(self.asq.cat_root.next.data, 1)
        self.assertEqual(self.asq.dog_root.data, 2)
        self.assertEqual(self.asq.dog_root.next.data, 3)
        
    def test_dequeue_cat(self):
        cat_ord = self.asq.dequeue_cat()
        self.assertEqual(cat_ord, 0)
        cat_ord = self.asq.dequeue_cat()
        self.assertEqual(cat_ord, 1)
        self.assertIsNone(self.asq.cat_root)
        
        with self.assertRaises(Exception):
            self.asq.dequeue_cat()
    
    def test_dequeue_dog(self):
        dog_ord = self.asq.dequeue_dog()
        self.assertEqual(dog_ord, 2)
        dog_ord = self.asq.dequeue_dog()
        self.assertEqual(dog_ord, 3)
        self.assertIsNone(self.asq.dog_root)
        
        with self.assertRaises(Exception):
            self.asq.dequeue_dog()
        
    def test_dequeue_any(self):
        # dequeue both cats because were added first
        animal_ord = self.asq.dequeue_any()
        self.assertEqual(animal_ord, 0)
        animal_ord = self.asq.dequeue_any()
        self.assertEqual(animal_ord, 1)
        
        # enqueue new cat
        self.asq.enqueue(is_cat=True)
        
        # dequeue both dogs before cat
        animal_ord = self.asq.dequeue_any()
        self.assertEqual(animal_ord, 2)
        animal_ord = self.asq.dequeue_any()
        self.assertEqual(animal_ord, 3)
        animal_ord = self.asq.dequeue_any()
        self.assertEqual(animal_ord, 4)
