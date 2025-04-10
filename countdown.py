import customtkinter as ctk
import time
import random
import winsound

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


class CountdownApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Countdown Timer")
        self.geometry("650x500")
        self.configure(fg_color="#f5f5f5")

        self.seconds = 60
        self.running = False
        self.timer_job = None

        # Display del countdown
        self.timer_label = ctk.CTkLabel(
            self,
            text=f"{self.seconds} sec",
            font=("Arial", 30, "bold"),
            fg_color="#32cd32",
            text_color="white",
            width=400,
            height=80,
            corner_radius=10
        )
        self.timer_label.pack(pady=20)

        # Frame per i pulsanti + e −
        sec_frame = ctk.CTkFrame(self, fg_color="transparent")
        sec_frame.pack()

        btn_decrease = ctk.CTkButton(
            sec_frame, text="−", corner_radius=10, fg_color="red",
            text_color="white", font=("Arial", 16, "bold"), width=60, height=60,
            command=self.decrease_time
        )
        btn_decrease.pack(side="left", padx=10)

        btn_increase = ctk.CTkButton(
            sec_frame, text="+", corner_radius=10, fg_color="green",
            text_color="white", font=("Arial", 16, "bold"), width=60, height=60,
            command=self.increase_time
        )
        btn_increase.pack(side="left", padx=10)

        # Frame per START e RESET
        start_frame = ctk.CTkFrame(self, fg_color="transparent")
        start_frame.pack(pady=30)

        btn_start = ctk.CTkButton(
            start_frame, text="START", corner_radius=10, fg_color="#32cd32",
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

    def increase_time(self):
        self.seconds += 1
        self.timer_label.configure(text=f"{self.seconds} sec")

    def decrease_time(self):
        if self.seconds > 1:
            self.seconds -= 1
            self.timer_label.configure(text=f"{self.seconds} sec")

    def start_countdown(self):
        if not self.running:
            self.running = True
            for _ in range(3):
                winsound.Beep(1000, 500)
                time.sleep(0.6)
            winsound.Beep(2000, 800)
            self.countdown(self.seconds)

    def countdown(self, remaining_time):
        if remaining_time > 0:
            self.timer_label.configure(text=f"{remaining_time} sec")
            self.timer_job = self.after(1000, self.countdown, remaining_time - 1)
        else:
            self.timer_label.configure(text="Tempo scaduto!")
            winsound.Beep(2500, 1500)
            self.running = False

    def reset_countdown(self):
        if self.timer_job:
            self.after_cancel(self.timer_job)
            self.timer_job = None
        self.running = False
        self.seconds = 60
        self.timer_label.configure(text=f"{self.seconds} sec")


def main():
    app = CountdownApp()
    app.mainloop()
