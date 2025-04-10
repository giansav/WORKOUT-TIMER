import customtkinter as ctk
import time
import random
import winsound

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


class RoundsApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rounds-Intervals Timer")
        self.geometry("650x500")
        self.configure(fg_color="#f5f5f5")

        self.running = False
        self.rounds = 3
        self.work_seconds = 60
        self.break_seconds = 30
        self.current_round = 0  # Round corrente
        self.is_work_time = True # indica se è tempo di lavoro o pausa
        self.timer_job = None  # Riferimento per cancellare il countdown


        # Display del countdown
        self.timer_label = ctk.CTkLabel(
            self,
            text=f"{self.work_seconds} sec",
            font=("Arial", 30, "bold"),
            fg_color="#4682b4",
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

        # Round
        round_label = ctk.CTkLabel(master=main_frame, text="Round:", font=("Arial", 16, "bold"), text_color="#4682b4")
        round_label.grid(row=0, column=0, padx=5)

        self.rounds_minus_button = ctk.CTkButton(master=main_frame, corner_radius=10, text="−", fg_color="red",
            text_color="white", font=("Arial", 16, "bold"), width=60, height=60, command=self.decrease_rounds)
        self.rounds_minus_button.grid(row=0, column=1, padx=5, pady=5)

        self.rounds_label = ctk.CTkLabel(master=main_frame, text=f"{self.rounds}", font=("Arial", 16, "bold"),
            text_color="#4682b4", width=60)
        self.rounds_label.grid(row=0, column=2, padx=5)

        self.rounds_plus_button = ctk.CTkButton(master=main_frame, corner_radius=10, text="+", fg_color="green",
            text_color="white", font=("Arial", 16, "bold"), width=60, height=60, command=self.increase_rounds)
        self.rounds_plus_button.grid(row=0, column=3, padx=5, pady=5)

        # Lavoro
        work_label = ctk.CTkLabel(master=main_frame, text="Lavoro (sec):", font=("Arial", 16, "bold"), text_color="#4682b4")
        work_label.grid(row=1, column=0, padx=5)

        self.work_minus_button = ctk.CTkButton(master=main_frame, corner_radius=10, text="−", fg_color="red",
            text_color="white", font=("Arial", 16, "bold"), width=60, height=60, command=self.decrease_work_time)
        self.work_minus_button.grid(row=1, column=1, padx=5, pady=5)

        self.work_label = ctk.CTkLabel(master=main_frame, text=f"{self.work_seconds} sec", font=("Arial", 16, "bold"),
            text_color="#4682b4", width=100)
        self.work_label.grid(row=1, column=2, padx=5)

        self.work_plus_button = ctk.CTkButton(master=main_frame, corner_radius=10, text="+", fg_color="green",
            text_color="white", font=("Arial", 16, "bold"), width=60, height=60, command=self.increase_work_time)
        self.work_plus_button.grid(row=1, column=3, padx=5, pady=5)

        # Pausa
        break_label = ctk.CTkLabel(master=main_frame, text="Pausa (sec):", font=("Arial", 16, "bold"), text_color="#4682b4")
        break_label.grid(row=2, column=0, padx=5)

        self.break_minus_button = ctk.CTkButton(master=main_frame, corner_radius=10, text="−", fg_color="red",
            text_color="white", font=("Arial", 16, "bold"), width=60, height=60, command=self.decrease_break_time)
        self.break_minus_button.grid(row=2, column=1, padx=5, pady=5)

        self.break_label = ctk.CTkLabel(master=main_frame, text=f"{self.break_seconds} sec", font=("Arial", 16, "bold"),
            text_color="#4682b4", width=100)
        self.break_label.grid(row=2, column=2, padx=5)

        self.break_plus_button = ctk.CTkButton(master=main_frame, corner_radius=10, text="+", fg_color="green",
            text_color="white", font=("Arial", 16, "bold"), width=60, height=60, command=self.increase_break_time)
        self.break_plus_button.grid(row=2, column=3, padx=5, pady=5)

        # Frame per START e RESET
        start_frame = ctk.CTkFrame(self, fg_color="transparent")
        start_frame.pack(pady=30)

        btn_start = ctk.CTkButton(
            start_frame, text="START", corner_radius=10, fg_color="#4682b4",
            text_color="white", font=("Arial", 16, "bold"), width=130, height=60,
            command=self.start_intervals
        )
        btn_start.pack(side="left", padx=10)

        btn_reset = ctk.CTkButton(
            start_frame, text="RESET", corner_radius=10, fg_color="darkblue",
            text_color="white", font=("Arial", 16, "bold"), width=130, height=60,
            command=self.reset_countdown
        )
        btn_reset.pack(side="left", padx=10)



    def increase_rounds(self):
        self.rounds += 1
        self.rounds_label.configure(text=f"{self.rounds}")

    def decrease_rounds(self):
        if self.rounds > 1:
            self.rounds -= 1
            self.rounds_label.configure(text=f"{self.rounds}")
            

    def increase_work_time(self):
        self.work_seconds += 1
        self.work_label.configure(text=f"{self.work_seconds} sec")
        self.timer_label.configure(text=f"{self.work_seconds} sec")

    def decrease_work_time(self):
        if self.work_seconds > 1:
            self.work_seconds -= 1
            self.work_label.configure(text=f"{self.work_seconds} sec")
            self.timer_label.configure(text=f"{self.work_seconds} sec")

    def increase_break_time(self):
        self.break_seconds += 1
        self.break_label.configure(text=f"{self.break_seconds} sec")

    def decrease_break_time(self):
        if self.break_seconds > 1:
            self.break_seconds -= 1
            self.break_label.configure(text=f"{self.break_seconds} sec")

    def start_intervals(self):
        if not self.running:
            self.running = True
            self.current_round = 0
            for _ in range(3):
                winsound.Beep(1000, 500)
                time.sleep(0.6)
            winsound.Beep(2000, 800)
            self.run_interval()

    def run_interval(self):
        if self.current_round < self.rounds:
            if self.is_work_time:
                self.timer_label.configure(text=f"{self.work_seconds} sec")
                self.countdown(self.work_seconds, self.end_work_time)
            else:
                self.timer_label.configure(text=f"{self.break_seconds} sec")
                self.countdown(self.break_seconds, self.end_break_time)
        else:
            self.timer_label.configure(text="Completato!")
            winsound.Beep(2500, 1500)
            self.running = False

    def countdown(self, remaining_time, end_function):
        if remaining_time >= 0:
            self.timer_label.configure(text=f"{remaining_time} sec")
            self.timer_job = self.after(1000, self.countdown, remaining_time - 1, end_function)
        else:
            end_function()

    def end_work_time(self):
        winsound.Beep(2500, 800)
        if self.current_round < self.rounds - 1:  # Controlla se siamo all'ultimo round di lavoro
            self.is_work_time = False
            self.run_interval()
        else:
            self.timer_label.configure(text="Lavoro completato!")
            winsound.Beep(2500, 1500)
            self.running = False

    def end_break_time(self):
        winsound.Beep(2000, 800)
        self.is_work_time = True
        self.current_round += 1
        self.run_interval()

    def reset_countdown(self):
        if self.timer_job:
            self.after_cancel(self.timer_job)
            self.timer_job = None
        self.running = False
        self.rounds = 3 # ripristina il settaggio iniziale
        self.work_seconds = 60
        self.break_seconds = 30
        self.timer_label.configure(text=f"{self.work_seconds} sec")
        self.rounds_label.configure(text=f"{self.rounds}")
        self.work_label.configure(text=f"{self.work_seconds} sec")
        self.break_label.configure(text=f"{self.break_seconds} sec")

def main():
    app = RoundsApp()
    app.mainloop()