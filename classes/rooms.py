class Room:
    def __init__(self, theme, guests, songs, spaces,takings):
        self.theme=theme
        self.guests=guests
        self.songs=songs
        self.spaces=spaces
        self.takings=takings
    

    def add_guest(self, new_guest):
        self.check_room_capacity()
        if (self.check_guest_cash(new_guest)):
            if (self.find_song(new_guest.favourite_song)):
                self.guests.append(new_guest)
                self.takings=self.takings+25
                return "Whoo-hoo!"
            else:
                self.guests.append(new_guest)
                self.takings=self.takings+20
                return "Boo!" 
        else:
            return"Sorry, our rooms are £20"

    def remove_guest(self,guest_to_remove):
        for guest in self.guests:
            if guest.name ==guest_to_remove:
                self.guests.remove(guest)

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
            if guest.name==guest_to_find:
                return True
            
        return False
    
    def check_room_capacity(self):
        if len(self.guests)>=self.spaces:
            return "That room is full"
        else:
            return

    def check_guest_cash(self, new_guest):
        if new_guest.wallet>=20:
            return True
    
    
