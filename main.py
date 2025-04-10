import customtkinter as ctk
import sys
import importlib

# Imposta il tema e l'aspetto
ctk.set_appearance_mode("light")  # oppure "dark"
ctk.set_default_color_theme("blue")  # puoi usare anche "green", "dark-blue", ecc.

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Start UI")
        self.geometry("800x400")
        self.configure(fg_color="#f5f5f5")  # colore di sfondo

        # Titolo / Label principale
        self.timer_label = ctk.CTkLabel(
            self, text="SELEZIONA IL TIMER", font=("Arial", 30, "bold"),
            text_color="#708090", width=600, height=60
        )
        self.timer_label.pack(pady=20)

        # Frame per i pulsanti
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(pady=20)

        # Pulsante Countdown
        self.create_button("Countdown", "#32cd32", lambda: self.start_app("countdown"))
        self.create_button("Round / Intervalli", "#4682b4", lambda: self.start_app("rounds"))
        self.create_button("Random Beep", "#ff4500", lambda: self.start_app("rand-beep"))

    def create_button(self, text, color, command):
        button = ctk.CTkButton(
            master=self.buttons_frame, text=text, corner_radius=10,
            fg_color=color, text_color="white", font=("Arial", 16, "bold"),
            width=200, height=50, command=command
        )
        button.pack(pady=10)

    def start_app(self, module_name):
        try:
            if module_name in sys.modules:
                importlib.reload(sys.modules[module_name])
                module = sys.modules[module_name]
            else:
                module = importlib.import_module(module_name)
            module.main()
        except Exception as e:
            print(f"Errore durante l'importazione di {module_name}: {e}")


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
