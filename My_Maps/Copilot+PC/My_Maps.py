import customtkinter, tkintermapview, typing, geocoder, CTkMenuBar, warnings, tkinter, speech_recognition, My_Maps_AI, My_Maps_AI_window_interface, threading

warnings.filterwarnings(f"ignore")

SLM: My_Maps_AI. My_Maps_LM = My_Maps_AI. My_Maps_LM().__initialize_model__()

class Program(customtkinter.CTk):
	
	TITLE: typing.Final[str] = f"My Maps (Copliot+PC edition)"
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

		self.main_screen_menu_ai_button: customtkinter.CTkButton = self.main_screen_menu.add_cascade(text=f"AI", command=lambda: AI_Window())

class AI_Window(customtkinter.CTkToplevel, My_Maps_AI_window_interface.My_Maps_AI_window_interface):

	TITLE: typing.Final[str] = f"My Maps AI assistant (Copliot+PC edition)"
	HEIGHT: typing.Final[int] = 375
	WIDTH: typing.Final[int] = 655
	ICON: typing.Final[str] = f"my maps icon.ico"
	COLOR_THEME: typing.Final[str] = f"dark-blue"
	WIDGET_SCALING: typing.Final[float] = 1.251
	THEME: typing.Final[str] = f"system"

	def __init__(self: typing.Self, *args, **kwargs) -> None:
		customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

		customtkinter.set_widget_scaling(self.WIDGET_SCALING)
		customtkinter.set_default_color_theme(self.COLOR_THEME)
		customtkinter.set_appearance_mode(self.THEME)
		customtkinter.deactivate_automatic_dpi_awareness()

		self.title(self.TITLE)
		self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
		self.resizable(False, False)
		self.after(250, lambda: self.iconbitmap(self.ICON))

		self.ai_window_textbox: customtkinter.CTkTextbox = customtkinter.CTkTextbox(master=self, height=265, width=524, corner_radius=0, fg_color=f"transparent", text_color=(f"black", f"white"))
		self.ai_window_textbox.place(x=0, y=0)

		self.ai_window_textbox.configure(state=f"disabled")

		self.ai_window_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self, height=30, width=465, border_width=0, fg_color=f"transparent", placeholder_text=f"...")
		self.ai_window_entry.place(x=0, y=269)

		self.ai_window_microphone_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=30, width=30, border_width=0, fg_color=f"transparent", text=f"🎤", command=self.__audio_input__)
		self.ai_window_microphone_button.place(x=465, y=269)

		self.ai_window_send_request_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=30, width=30, border_width=0, fg_color=f"transparent", text=f"->", command=self.__response__)
		self.ai_window_send_request_button.place(x=495, y=269)

		self.ai_window_entry.bind(f"<Return>", self.__response__)

	@typing.override
	def __response__(self: typing.Self, event: str | None = None) -> None:
		self.ai_window_entry_data: str = self.ai_window_entry.get()

		def run_model():
			response_text: str = My_Maps_AI.My_Maps_LM().__response__(pipe=SLM, query=f"<|system|>You are a helpful AI assistant.<|end|><|user|>{self.ai_window_entry_data}<|end|><|assistant|>")

			def update_gui():
				self.ai_window_textbox.configure(state="normal")
				self.ai_window_textbox.insert(tkinter.END, f"USER:\n{self.ai_window_entry_data}\nLlama:\n{response_text}\n")
				self.ai_window_textbox.configure(state="disabled")
				self.ai_window_entry.delete(0, tkinter.END)

			self.after(0, update_gui)

		threading.Thread(target=run_model).start()

	@typing.override
	def __audio_input__(self: typing.Self) -> None:
		self.recognizer: speech_recognition.Recognizer = speech_recognition.Recognizer()
		with speech_recognition.Microphone() as self.source:
			self.audio_data: speech_recognition.AudioData = self.recognizer.record(self.source, duration=5)
			self.text: str = self.recognizer.recognize_google(self.audio_data)

		self.ai_window_entry.insert(f"0", self.text)

if __name__ == f"__main__":
	program: Program = Program().mainloop()
