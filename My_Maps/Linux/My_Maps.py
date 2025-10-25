import customtkinter, tkintermapview, typing, geocoder, CTkMenuBar, My_Maps_AI_window, pickle, My_Maps_settings, ctypes, My_Maps_interface

with open(f"my_maps_theme_settings.pickle", f"rb+") as theme_data: theme: str = pickle.load(theme_data)

class Program(customtkinter.CTk, My_Maps_interface.My_Maps_interface):
    
    TITLE: typing.Final[str] = f"My Maps  "
    WIDGET_SCALING: typing.Final[int] = 1.251
    
    def __init__(self: typing.Self, *args: typing.Any, **kwargs: typing.Any) -> None:
        customtkinter.CTk.__init__(self, *args, **kwargs)
        
        customtkinter.deactivate_automatic_dpi_awareness()
        customtkinter.set_widget_scaling(self.WIDGET_SCALING)
        customtkinter.set_appearance_mode(theme)
        
        self.title(self.TITLE)
        self.bind(f"<F11>", lambda event: self.__fullscreen__())

        self.main_screen_current_cordinates: tuple[float, float] = geocoder.ip(f"me")

        self.main_screen_menu: CTkMenuBar.CTkMenuBar = CTkMenuBar.CTkMenuBar(self)

        self.main_screen_menu_ai_button: customtkinter.CTkButton = self.main_screen_menu.add_cascade(text=f"AI", command=lambda: My_Maps_AI_window.AI_Window())

        self.main_screen_menu_settings_button: customtkinter.CTkButton = self.main_screen_menu.add_cascade(text=f"⚙️", command=lambda: My_Maps_settings.My_Maps_setting_window())
        
        self.main_screen_map: tkintermapview.TkinterMapView = tkintermapview.TkinterMapView(master=self, corner_radius=0)
        self.main_screen_map.pack(fill=f"both", expand=True)
        
        self.main_screen_map.set_position(self.main_screen_current_cordinates.latlng[0], self.main_screen_current_cordinates.latlng[1])

    @typing.override
    def __fullscreen__(self: typing.Self) -> None:
        if self.attributes(f"-fullscreen"): self.attributes(f"-fullscreen", False)
        
        else: self.attributes(f"-fullscreen", True)

        if customtkinter.get_appearance_mode()=="Dark": value=1
        
        else: value=0
    
        try:
            hwnd = ctypes.windll.user32.GetParent(self.winfo_id())
            DWMWA_USE_IMMERSIVE_DARK_MODE = 20
            DWMWA_USE_IMMERSIVE_DARK_MODE_BEFORE_20H1 = 19

            if ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, ctypes.byref(ctypes.c_int(value)), ctypes.sizeof(ctypes.c_int(value))) != 0: ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE_BEFORE_20H1, ctypes.byref(ctypes.c_int(value)), ctypes.sizeof(ctypes.c_int(value)))
        
        except Exception as err: pass
        
if __name__ == f"__main__":
    program: Program = Program().mainloop()
