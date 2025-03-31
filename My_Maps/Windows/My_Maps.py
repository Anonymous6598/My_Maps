import customtkinter, tkintermapview, typing, geocoder, CTkMenuBar, My_Maps_AI_window, warnings

warnings.filterwarnings(f"ignore")

class Program(customtkinter.CTk):
    
    TITLE: typing.Final[str] = f"My Maps  "
    ICON: typing.Final[str] = f"my maps icon.ico"
    WIDGET_SCALING: typing.Final[int] = 1.251
    
    def __init__(self: typing.Self, *args: typing.Any, **kwargs: typing.Any) -> None:
        customtkinter.CTk.__init__(self, *args, **kwargs)
        
        customtkinter.deactivate_automatic_dpi_awareness()
        customtkinter.set_widget_scaling(self.WIDGET_SCALING)
        
        self.title(self.TITLE)
        self.iconbitmap(self.ICON)

        self.main_screen_current_cordinates: tuple[float, float] = geocoder.ip(f"me")
        
        self.main_screen_map: tkintermapview.TkinterMapView = tkintermapview.TkinterMapView(master=self, corner_radius=0)
        self.main_screen_map.pack(fill=f"both", expand=True)
        
        self.main_screen_map.set_position(self.main_screen_current_cordinates.latlng[0], self.main_screen_current_cordinates.latlng[1])

        self.main_screen_menu: CTkMenuBar.CTkTitleMenu = CTkMenuBar.CTkTitleMenu(self)

        self.main_screen_menu_ai_button: customtkinter.CTkButton = self.main_screen_menu.add_cascade(text=f"AI", command=lambda: My_Maps_AI_window.AI_Window())

if __name__ == f"__main__":
    program: Program = Program().mainloop()