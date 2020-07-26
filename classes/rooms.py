class Room:
    def __init__(self,guests, songs):
        self.guests=guests
        self.songs=songs

    def add_guest(self, new_guest):
        self.guests.append(new_guest)

    def remove_guest(self,guest_to_remove):
        self.guests.remove(guest_to_remove)

    def remove_all_guests(self):
        while self.guests:
            self.guests.pop(0)
    
    def add_song(self, song_to_add):
        self.songs.append(song_to_add)
    
    def remove_song(self, song_to_remove):
        for song in self.songs:
            if song.title==song_to_remove:
                self.songs.remove(song)

    def find_song(self,song_to_find):
        for song in self.songs:
            if song.title==song_to_find:
                return True
   
        return False
    
    def find_guest(self,guest_to_find):
        for guest in self.guests:
            if guest==guest_to_find:
                return True
            
        return False
    