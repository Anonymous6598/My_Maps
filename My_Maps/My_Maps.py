import customtkinter, tkintermapview, typing, geocoder

class Program(customtkinter.CTk):
    
    TITLE: typing.Final[str] = f"My Maps"
    THEME: typing.Final[str] = f"system"
    ICON: typing.Final[str] = f"my maps icon.ico"
    
    def __init__(self: typing.Self, *args: typing.Any, **kwargs: typing.Any) -> None:
        customtkinter.CTk.__init__(self, *args, **kwargs)
        
        customtkinter.set_appearance_mode(self.THEME)
        
        self.title(self.TITLE)
        self.iconbitmap(self.ICON)
        
        self.main_screen_current_cordinates: tuple[float, float] = geocoder.ip(f"me")
        
        self.main_screen_map: tkintermapview.TkinterMapView = tkintermapview.TkinterMapView(master=self, corner_radius=0)
        self.main_screen_map.pack(fill=f"both", expand=True)
        
        self.main_screen_map.set_position(self.main_screen_current_cordinates.latlng[0], self.main_screen_current_cordinates.latlng[1])

if __name__ == f"__main__":
    program: Program = Program().mainloop()