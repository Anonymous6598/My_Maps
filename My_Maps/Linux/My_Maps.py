import customtkinter, tkintermapview, typing, geocoder, CTkMenuBar, My_Maps_AI_window, pickle, My_Maps_settings

with open(f"my_maps_theme_settings.pickle", f"rb+") as theme_data: theme: str = pickle.load(theme_data)

class Program(customtkinter.CTk):
    
    TITLE: typing.Final[str] = f"My Maps  "
    WIDGET_SCALING: typing.Final[int] = 1.251
    
    def __init__(self: typing.Self, *args: typing.Any, **kwargs: typing.Any) -> None:
        customtkinter.CTk.__init__(self, *args, **kwargs)
        
        customtkinter.deactivate_automatic_dpi_awareness()
        customtkinter.set_widget_scaling(self.WIDGET_SCALING)
        customtkinter.set_appearance_mode(theme)
        
        self.title(self.TITLE)

        self.main_screen_current_cordinates: tuple[float, float] = geocoder.ip(f"me")
        
        self.main_screen_map: tkintermapview.TkinterMapView = tkintermapview.TkinterMapView(master=self, corner_radius=0)
        self.main_screen_map.pack(fill=f"both", expand=True)
        
        self.main_screen_map.set_position(self.main_screen_current_cordinates.latlng[0], self.main_screen_current_cordinates.latlng[1])

        self.main_screen_menu: CTkMenuBar.CTkMenuBar = CTkMenuBar.CTkMenuBar(self)

        self.main_screen_menu_ai_button: customtkinter.CTkButton = self.main_screen_menu.add_cascade(text=f"AI", command=lambda: My_Maps_AI_window.AI_Window())

        self.main_screen_menu_settings_button: customtkinter.CTkButton = self.main_screen_menu.add_cascade(text=f"⚙️", command=lambda: My_Maps_settings.My_Maps_setting_window())
        
if __name__ == f"__main__":
    program: Program = Program().mainloop()
