import customtkinter, tkintermapview, typing, geocoder, CTkMenuBar, locale, My_Maps_Interface, My_Maps_AI_window, pickle, My_Maps_settings

with open(f"my_maps_language_settings.pickle", f"rb+") as data: language_data: str = pickle.load(data)

with open(f"my_maps_theme_settings.pickle", f"rb+") as theme_data: theme: str = pickle.load(theme_data)

class Program(customtkinter.CTk, My_Maps_Interface.My_Maps_Interface):
    
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

        self.main_screen_menu: CTkMenuBar.CTkTitleMenu = CTkMenuBar.CTkTitleMenu(self)

        self.main_screen_menu_menu_button: customtkinter.CTkButton = self.main_screen_menu.add_cascade(text=f"☰")

        self.main_screen_menu_dropdownmenu: CTkMenuBar.CustomDropdownMenu = CTkMenuBar.CustomDropdownMenu(widget=self.main_screen_menu_menu_button)

        if language_data == f"Српски":
            self.main_screen_menu_dropdownmenu.add_option(option=f"🔎 (претрага)", command=self.__search__)
            self.main_screen_menu_dropdownmenu.add_option(option=f"AI", command=lambda: My_Maps_AI_window.AI_Window())
        
        elif language_data == f"Русский":
            self.main_screen_menu_dropdownmenu.add_option(option=f"🔎 (поиск)", command=self.__search__)
            self.main_screen_menu_dropdownmenu.add_option(option=f"ИИ (Нейро сеть)", command=lambda: My_Maps_AI_window.AI_Window())
        
        else:
            self.main_screen_menu_dropdownmenu.add_option(option=f"🔎 (search)", command=self.__search__)
            self.main_screen_menu_dropdownmenu.add_option(option=f"AI", command=lambda: My_Maps_AI_window.AI_Window())

        self.main_screen_menu_settings_button: customtkinter.CTkButton = self.main_screen_menu.add_cascade(text=f"⚙️", command=lambda: My_Maps_settings.My_Maps_setting_window())

    @typing.override
    def __search__(self: typing.Self) -> None:
        if language_data == f"Српски":
            self.main_screen_search_dialog: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(text=f"претрага", title=f"претрага", button_fg_color=f"green")
            
            self.main_screen_map.set_address(self.main_screen_search_dialog.get_input())
        
        elif language_data == f"Русский":
            self.main_screen_search_dialog: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(text=f"поиск", title=f"поиск", button_fg_color=f"green")
            
            self.main_screen_map.set_address(self.main_screen_search_dialog.get_input())

        else:
            self.main_screen_search_dialog: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(text=f"search", title=f"search", button_fg_color=f"green")
            
            self.main_screen_map.set_address(self.main_screen_search_dialog.get_input())
        
if __name__ == f"__main__":
    program: Program = Program().mainloop()