import time
import winsound
import random
import customtkinter as ctk

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


class RoundsApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rounds-Intervals Timer")
        self.geometry("650x500")
        self.configure(fg_color="#f5f5f5")

        self.running = False
        self.work_seconds = 50
        self.minint_seconds = 3
        self.maxint_seconds = 10
        self.is_work_time = True # indica se è tempo di lavoro o pausa
        self.timer_job = None  # Riferimento per cancellare il countdown


       # Display del countdown
        self.timer_label = ctk.CTkLabel(
            self,
            text=f"{self.work_seconds} sec",
            font=("Arial", 30, "bold"),
            fg_color="#ff4500",
            text_color="white",
            width=400,
            height=80,
            corner_radius=10
        )
        self.timer_label.pack(pady=20)


        # Configura le colonne della griglia principale per avere la stessa larghezza
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(pady=10)


        for i in range(4):
            main_frame.grid_columnconfigure(i, weight=1)

        # Lavoro
        work_label = ctk.CTkLabel(master=main_frame, text="Lavoro (sec):", font=("Arial", 16, "bold"), text_color="#4682b4")
        work_label.grid(row=0, column=0, padx=5)

        self.work_minus_button = ctk.CTkButton(master=main_frame, corner_radius=10, text="−", fg_color="red",
            text_color="white", font=("Arial", 16, "bold"), width=60, height=60, command=self.decrease_work_seconds)
        self.work_minus_button.grid(row=0, column=1, padx=5, pady=5)

        self.work_label = ctk.CTkLabel(master=main_frame, text=f"{self.work_seconds}", font=("Arial", 16, "bold"),
            text_color="#4682b4", width=60)
        self.work_label.grid(row=0, column=2, padx=5)

        self.work_plus_button = ctk.CTkButton(master=main_frame, corner_radius=10, text="+", fg_color="green",
            text_color="white", font=("Arial", 16, "bold"), width=60, height=60, command=self.increase_work_seconds)
        self.work_plus_button.grid(row=0, column=3, padx=5, pady=5)

        # Intervallo minimo tra gli impulsi
        minint_label = ctk.CTkLabel(master=main_frame, text="Intervallo minimo tra i beep (sec):", font=("Arial", 16, "bold"), text_color="#4682b4")
        minint_label.grid(row=1, column=0, padx=5)

        self.minint_minus_button = ctk.CTkButton(master=main_frame, corner_radius=10, text="−", fg_color="red",
            text_color="white", font=("Arial", 16, "bold"), width=60, height=60, command=self.decrease_minint_seconds)
        self.minint_minus_button.grid(row=1, column=1, padx=5, pady=5)

        self.minint_label = ctk.CTkLabel(master=main_frame, text=f"{self.minint_seconds} sec", font=("Arial", 16, "bold"),
            text_color="#4682b4", width=100)
        self.minint_label.grid(row=1, column=2, padx=5)

        self.minint_plus_button = ctk.CTkButton(master=main_frame, corner_radius=10, text="+", fg_color="green",
            text_color="white", font=("Arial", 16, "bold"), width=60, height=60, command=self.increase_minint_seconds)
        self.minint_plus_button.grid(row=1, column=3, padx=5, pady=5)

        # Intervallo massimo tra gli impulsi
        maxint_label = ctk.CTkLabel(master=main_frame, text="Intervallo massimo tra i beep (sec):", font=("Arial", 16, "bold"), text_color="#4682b4")
        maxint_label.grid(row=2, column=0, padx=5)

        self.maxint_minus_button = ctk.CTkButton(master=main_frame, corner_radius=10, text="−", fg_color="red",
            text_color="white", font=("Arial", 16, "bold"), width=60, height=60, command=self.decrease_maxint_seconds)
        self.maxint_minus_button.grid(row=2, column=1, padx=5, pady=5)

        self.maxint_label = ctk.CTkLabel(master=main_frame, text=f"{self.maxint_seconds} sec", font=("Arial", 16, "bold"),
            text_color="#4682b4", width=100)
        self.maxint_label.grid(row=2, column=2, padx=5)

        self.maxint_plus_button = ctk.CTkButton(master=main_frame, corner_radius=10, text="+", fg_color="green",
            text_color="white", font=("Arial", 16, "bold"), width=60, height=60, command=self.increase_maxint_seconds)
        self.maxint_plus_button.grid(row=2, column=3, padx=5, pady=5)

        # Frame per START e RESET
        start_frame = ctk.CTkFrame(self, fg_color="transparent")
        start_frame.pack(pady=30)

        btn_start = ctk.CTkButton(
            start_frame, text="START", corner_radius=10, fg_color="#ff4500",
            text_color="white", font=("Arial", 16, "bold"), width=130, height=60,
            command=self.start_countdown
        )
        btn_start.pack(side="left", padx=10)

        btn_reset = ctk.CTkButton(
            start_frame, text="RESET", corner_radius=10, fg_color="darkblue",
            text_color="white", font=("Arial", 16, "bold"), width=130, height=60,
            command=self.reset_countdown
        )
        btn_reset.pack(side="left", padx=10)



            
    def increase_work_seconds(self):
        self.work_seconds += 1
        self.work_label.configure(text=f"{self.work_seconds} sec")
        self.timer_label.configure(text=f"{self.work_seconds} sec")

    def decrease_work_seconds(self):
        if self.work_seconds > 1:
            self.work_seconds -= 1
            self.work_label.configure(text=f"{self.work_seconds} sec")
            self.timer_label.configure(text=f"{self.work_seconds} sec")

    def increase_minint_seconds(self):
        self.minint_seconds += 1
        self.minint_label.configure(text=f"{self.minint_seconds} sec")

    def decrease_minint_seconds(self):
        if self.minint_seconds > 1:
            self.minint_seconds -= 1
            self.minint_label.configure(text=f"{self.minint_seconds} sec")


    def increase_maxint_seconds(self):
        self.maxint_seconds += 1
        self.maxint_label.configure(text=f"{self.maxint_seconds} sec")

    def decrease_maxint_seconds(self):
        if self.maxint_seconds > 1:
            self.maxint_seconds -= 1
            self.maxint_label.configure(text=f"{self.maxint_seconds} sec")

    def start_countdown(self):
        if not self.running:
            self.running = True
            self.current_round = 0
            for _ in range(3):
                winsound.Beep(1000, 500)
                time.sleep(0.6)
            winsound.Beep(2000, 800)
            self.countdown(self.work_seconds)

    def countdown(self, remaining_time):
        if remaining_time > 0:
            self.timer_label.configure(text=f"{remaining_time} sec")
            self.timer_job = self.after(1000, self.countdown, remaining_time - 1)
            # La pianificazione iniziale del suono avviene solo se non è già in corso
            if not hasattr(self, 'sound_scheduled') or not self.sound_scheduled:
                random_interval = random.randint(self.minint_seconds, self.maxint_seconds)
                self.sound_scheduled = True
                self.after(random_interval * 1000, self.emit_sound)
        else:
            self.timer_label.config(text="Tempo scaduto!")
            winsound.Beep(2500, 1500)
            self.running = False
            if hasattr(self, 'sound_scheduled'):
                self.sound_scheduled = False

    def emit_sound(self):
        if self.running:
            winsound.Beep(2880, 600)
            self.sound_scheduled = False # Permette la pianificazione di un nuovo suono
            # Pianifica il prossimo suono dopo un intervallo casuale
            random_interval = random.randint(self.minint_seconds, self.maxint_seconds)
            self.sound_scheduled = True
            self.after(random_interval * 1000, self.emit_sound)

    def reset_countdown(self):
        if self.timer_job:
            self.after_cancel(self.timer_job)
            self.timer_job = None
        self.running = False
        self.work_seconds = 50 # ripristina il settaggio iniziale
        self.minint_seconds = 3
        self.maxint_seconds = 10
        self.timer_label.configure(text=f"{self.work_seconds} sec")
        self.work_label.configure(text=f"{self.work_seconds} sec")
        self.minint_label.configure(text=f"{self.minint_seconds} sec")
        self.maxint_label.configure(text=f"{self.maxint_seconds} sec")

def main():
    app = RoundsApp()
    app.mainloop()