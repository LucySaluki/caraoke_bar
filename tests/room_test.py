import unittest

from classes.rooms import Room
from classes.guests import Guest
from classes.songs import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.song_1=Song("Sympathy for the Devil","Rolling Stones")
        self.song_2=Song("All Along the Watchtower","Jimi Hendrix")
        self.song_3=Song("Jumping Jack Flash","Rolling Stones")
        self.song_4=Song("Gangnam Sytle","Psy")
        self.song_5=Song("Fake Love","BTS")
        self.song_6=Song("Come Together","The Beatles")

        self.guest_1=Guest("Fred Smith",50,'Gangham Style')
        self.guest_2=Guest("Cynthia Applebaum",20,"All Along the Watchtower")

        songs=[self.song_1,self.song_2,self.song_3,self.song_6]
        songs_1=[self.song_4, self.song_5]
        guests=[self.guest_1,self.guest_2]
        guests_1=[]
        self.room_1=Room("Songs of the Sixties", guests,songs,2,len(guests)*20)
        self.room_2=Room("K-pop", guests_1,songs_1,3,0)

    def test_room_has_guest_alt(self):
        self.assertEqual(2,len(self.room_1.guests))

    def test_room_has_song(self):
        self.assertEqual(4,len(self.room_1.songs))

    def test_guest_added_to_room(self):
        new_guest=Guest("Joe Bloggs",100,"Sympathy for the Devil")
        self.room_2.add_guest(new_guest)
        self.assertEqual(1,len(self.room_2.guests))
    
    def test_guest_removed_from_room(self):
        guest_to_remove="Fred Smith"
        self.room_1.remove_guest(guest_to_remove)
        self.assertEqual(1,len(self.room_1.guests))
        
    def test_remove_all_guests_from_room(self):
        self.room_1.remove_all_guests()
        self.assertEqual(0,len(self.room_1.guests))

    def test_add_song_to_room(self):
        song_to_add=Song("Jumping Jack Flash","Rolling Stones")
        self.room_2.add_song(song_to_add)
        self.assertEqual(3,len(self.room_2.songs))

    def test_remove_song_from_room_by_name(self):
        song_to_remove="Sympathy for the Devil"
        self.room_1.remove_song(song_to_remove)
        self.assertEqual(3,len(self.room_1.songs))
  
    def test_find_if_guest_in_room_yes(self):
        guest_to_find="Cynthia Applebaum"
        self.assertEqual(True,self.room_1.find_guest(guest_to_find))
        
    def test_find_if_guest_in_room_no(self):
        guest_to_find="Elizabeth Windsor"
        self.assertEqual(False,self.room_1.find_guest(guest_to_find))

    def test_find_if_song_in_room_yes(self):
        song_to_find="All Along the Watchtower"
        self.assertEqual(True,self.room_1.find_song(song_to_find))

    def test_find_if_song_in_room_no(self):
        song_to_find="Gangham Style"
        self.assertEqual(False,self.room_1.find_song(song_to_find))

    def test_check_number_of_spaces(self):
        self.assertEqual("That room is full",self.room_1.check_room_capacity())

    def test_check_guest_has_enough_money_refuse_entry(self):
        new_guest=Guest("Joe Bloggs",10,"Sympathy for the Devil")
        self.assertEqual("Sorry, our rooms are £20",self.room_2.add_guest(new_guest))

    def test_check_guest_has_enough_money_accept_entry(self):
        new_guest=Guest("Adam Jones",20,"Come Together")
        self.room_2.add_guest(new_guest)
        self.assertEqual(1,len(self.room_2.guests))

    def test_guest_put_in_room_with_favourite_song_yes(self):
        new_guest=Guest("Archibald Constantinople",100,"Fake Love")
        self.assertEqual("Whoo-hoo!",self.room_2.add_guest(new_guest))

    def test_guest_put_in_room_with_favourite_song_no(self):
        new_guest=Guest("Rachel Dawson",40,"Halleluja")
        self.assertEqual("Boo!",self.room_2.add_guest(new_guest))

    def test_room_takings(self):
        self.assertEqual(40,self.room_1.takings)

    def test_add_guest_and_take_cash(self):
        new_guest=Guest("Rachel Dawson",40,"Halleluja")
        self.room_2.add_guest(new_guest)
        self.assertEqual(20,self.room_2.takings)
    
    def test_refuse_guest_and_dont_take_cash(self):
        new_guest=Guest("Joe Bloggs",10,"Sympathy for the Devil")
        self.room_2.add_guest(new_guest)
        self.assertEqual(0, self.room_2.takings)

    def test_guest_put_in_room_with_favourite_song_adds_tip(self):
        new_guest=Guest("Archibald Constantinople",100,"Fake Love")
        self.room_2.add_guest(new_guest)
        self.assertEqual(25, self.room_2.takings)