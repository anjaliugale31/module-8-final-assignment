from django.test import TestCase
from restaurant.models import Menu


class MenuItemTest(TestCase):
    #setup method set the mock data 
    def setUp(self):
        Menu.objects.create(Title="ice-cream", Price=10, Inventory=100)

    def test_get_item(self):
        item = Menu.objects.get(Title="ice-cream", Price=10, Inventory=100)
        itemstr = item.get_item()
        self.assertEqual(itemstr, "ice-cream:1000.00")  # 10 * 100 = 1000