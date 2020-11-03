from django.test import TestCase
from .models import Activity, User, NeighbourHood, Business
from django.contrib.auth.models import User

# Create your tests here.
class UserTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.virsail = User(id = 25)

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.virsail,User))
    
 #  def test_initialization(self):
    

    # Testing Save method
    def test_create_user(self):
#       self.virsail.save_user()
        users = User.objects.all()
        self.assertFalse(len(users)>0)

    # Testing Delete method
    def test_delete_user(self):
 #      self.virsail.delete_user()
        users = User.objects.all()
        self.assertTrue(len(users) == 0)



class NeighbourhoodTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Gigiri = NeighbourHood(id = 10, name = "westlandsspringvalley", location = "nairobi",occupants_count = 7080)

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Gigiri,NeighbourHood))
    
    def test_initialization(self):
        self.assertEqual(self.Gigiri.name,"westlandsspringvalley")
        self.assertEqual(self.Gigiri.location,"nairobi")
        self.assertEqual(self.Gigiri.occupants_count, 7080)
     

    # Testing Save method
    def test_create_neigborhood(self):
        self.Gigiri.save_neighborhood()
        neighborhoods = NeighbourHood.objects.all()
        self.assertTrue(len(neighborhoods)>0)

    # Testing Delete method
    def test_delete_neigborhood(self):
        self.Gigiri.delete_neighborhood()
        neighborhoods = NeighbourHood.objects.all()
        self.assertTrue(len(neighborhoods) == 0)


    
class ActivityTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.virsail = User(username = "showiz")
        
        self.Gigiri = NeighbourHood(name = "gigiri", location = "nairobi",occupants_count = 200)
       
        self.Activities = Activity(id = 95, title = "New activity", activity = "A good one ", submitter_id = 6)
    

        self.user = User(username="popshit")

    
   
 

class BusinessTestClass(TestCase):
        
    def setUp(self):
            self.cardealer = Business(name = "carexpo", id = 2, business_email = "cheki@gmail.com")

        # Testing instance
    def test_instance(self):
            self.assertTrue(isinstance(self.cardealer,Business))
        
    def test_initialization(self):
            self.assertEqual(self.cardealer.name,"carexpo")
            self.assertEqual(self.cardealer.business_email, "cheki@gmail.com")

        # Testing Save method
    def test_create_business(self):
            self.cardealer.save_business()
            businesses = Business.objects.all()
            self.assertTrue(len(businesses)>0)

        # Testing Delete method
    