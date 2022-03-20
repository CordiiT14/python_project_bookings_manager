import string
import unittest

from models.event import Event

class TestEvent(unittest.TestCase):

    def setUp(self):
        self.event_1 = Event("Loud Poets", "11 April 2022", "18:30", "Spoken Word", "Showcasing the top spoken word talent from Scotland and the UK! From laugh-out-loud funny, through the wonderfully surreal, to the thoughtful and emotional. Loud Poets continue to prove that Spoken Word has something for everyone.")

    def test_event_name(self):
        self.assertEqual("Loud Poets", self.event_1.event_title)
    
    def test_event_date(self):
        self.assertEqual("11 April 2022", self.event_1.date)

    def test_event_time(self):
        self.assertEqual("18:30", self.event_1.time)

    def test_event_type(self):
        self.assertEqual("Spoken Word", self.event_1.event_type)

    def test_event_description_exists(self):
        self.assertNotEqual( None , self.event_1.description)
    
    def test_event_description(self):
        self.assertEqual( "Showcasing the top spoken word talent from Scotland and the UK! From laugh-out-loud funny, through the wonderfully surreal, to the thoughtful and emotional. Loud Poets continue to prove that Spoken Word has something for everyone." , self.event_1.description)

    def test_event_id(self):
        self.assertEqual( None, self.event_1.id)