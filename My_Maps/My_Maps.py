import customtkinter, tkintermapview, typing, geocoder, My_Maps_AI, asyncio, tkinter, CTkMenuBar, locale, My_Maps_Interface

class Program(customtkinter.CTk, My_Maps_Interface.My_Maps_Interface):
    
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

        self.main_screen_menu_menu_button: customtkinter.CTkButton = self.main_screen_menu.add_cascade(text=f"☰")

        self.main_screen_menu_dropdownmenu: CTkMenuBar.CustomDropdownMenu = CTkMenuBar.CustomDropdownMenu(widget=self.main_screen_menu_menu_button)

        if locale.getdefaultlocale()[0] == f"sr_RS":
            self.main_screen_menu_dropdownmenu.add_option(option=f"🔎 (претрага)", command=self.__search__)
            self.main_screen_menu_dropdownmenu.add_option(option=f"ВИ", command=lambda: AI_Window())
        
        elif locale.getdefaultlocale()[0] == f"ru_RU":
            self.main_screen_menu_dropdownmenu.add_option(option=f"🔎 (поиск)", command=self.__search__)
            self.main_screen_menu_dropdownmenu.add_option(option=f"ИИ (Нейро сеть)", command=lambda: AI_Window())
        
        else:
            self.main_screen_menu_dropdownmenu.add_option(option=f"🔎 (search)", command=self.__search__)
            self.main_screen_menu_dropdownmenu.add_option(option=f"AI", command=lambda: AI_Window())


    @typing.override
    def __search__(self: typing.Self) -> None:
        if locale.getdefaultlocale()[0] == f"sr_RS":
            self.main_screen_search_dialog: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(text=f"претрага", title=f"претрага", button_fg_color=f"green")
            self.after(250, lambda: self.main_screen_search_dialog.iconbitmap(self.ICON))
            
            self.main_screen_map.set_address(self.main_screen_search_dialog.get_input())
        
        elif locale.getdefaultlocale()[0] == f"ru_RU":
            self.main_screen_search_dialog: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(text=f"поиск", title=f"поиск", button_fg_color=f"green")
            self.after(250, lambda: self.main_screen_search_dialog.iconbitmap(self.ICON))
            
            self.main_screen_map.set_address(self.main_screen_search_dialog.get_input())

        else:
            self.main_screen_search_dialog: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(text=f"search", title=f"search", button_fg_color=f"green")
            self.after(250, lambda: self.main_screen_search_dialog.iconbitmap(self.ICON))
            
            self.main_screen_map.set_address(self.main_screen_search_dialog.get_input())
        
class AI_Window(customtkinter.CTkToplevel):

	TITLE: typing.Final[str] = f"My Maps AI assistant"
	HEIGHT: typing.Final[int] = 375
	WIDTH: typing.Final[int] = 655
	ICON: typing.Final[str] = f"my maps icon.ico"

	def __init__(self: typing.Self, *args, **kwargs) -> None:
		customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

		self.title(self.TITLE)
		self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
		self.resizable(False, False)
		self.after(250, lambda: self.iconbitmap(self.ICON))

		self.ai_window_textbox: customtkinter.CTkTextbox = customtkinter.CTkTextbox(master=self, height=265, width=524, corner_radius=0, fg_color=f"transparent", text_color=(f"black", f"white"))
		self.ai_window_textbox.place(x=0, y=0)

		self.ai_window_textbox.configure(state=f"disabled")

		self.ai_window_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self, height=30, width=524, border_width=0, fg_color=f"transparent", placeholder_text=f"...")
		self.ai_window_entry.place(x=0, y=269)

		self.ai_window_entry.bind(f"<Return>", self.__response__)

	def __response__(self: typing.Self, configure: str | None = None) -> None:
		self.ai_window_entry_data: str = self.ai_window_entry.get()

		self.ai_window_textbox.configure(state=f"normal")
		self.query: str = asyncio.run(My_Maps_AI.My_Maps_LM().__response__(self.ai_window_entry_data))

		self.ai_window_textbox.insert(tkinter.END, f"{self.query}\n", f"-1.0")
		self.ai_window_textbox.configure(state=f"disabled")
		self.ai_window_entry.delete(f"-1", tkinter.END)

if __name__ == f"__main__":
    program: Program = Program().mainloop()