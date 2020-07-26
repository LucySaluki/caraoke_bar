import unittest

from classes.rooms import Room
from classes.guests import Guest
from classes.songs import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.song_1=Song("Sympathy for the Devil","Rolling Stones")
        self.song_2=Song("All Along the Watchtower","Jimi Hendrix")

        songs=[self.song_1,self.song_2]
        guests=["Fred Smith","Cynthia Applebaum"]
        self.room_1=Room(guests,songs)

    def test_room_has_guest(self):
        self.assertEqual("Fred Smith", self.room_1.guests[0])

    def test_room_has_song(self):
        self.assertEqual(2,len(self.room_1.songs))

    def test_guest_added_to_room(self):
        new_guest=Guest("Joe Bloggs")
        self.room_1.add_guest(new_guest)
        self.assertEqual(3,len(self.room_1.guests))
    
    def test_guest_removed_from_room(self):
        guest_to_remove="Fred Smith"
        self.room_1.remove_guest(guest_to_remove)
        self.assertEqual(1,len(self.room_1.guests))
        
    def test_remove_all_guests_from_room(self):
        self.room_1.remove_all_guests()
        self.assertEqual(0,len(self.room_1.guests))

    def test_add_song_to_room(self):
        song_to_add=Song("Jumping Jack Flash","Rolling Stones")
        self.room_1.add_song(song_to_add)
        self.assertEqual(3,len(self.room_1.songs))

    def test_remove_song_from_room_by_name(self):
        song_to_remove="Sympathy for the Devil"
        self.room_1.remove_song(song_to_remove)
        self.assertEqual(1,len(self.room_1.songs))
  
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


    