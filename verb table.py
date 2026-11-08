import random
import tkinter as tk
from tkinter import messagebox
import sys
import os

# Complete database of all 172 verbs from Pages 1 to 6
FULL_VERB_DATABASE = [
    # --- Page 1 ---
    ["answer", "answered", "answered"],
    ["ask", "asked", "asked"],
    ["call", "called", "called"],
    ["climb", "climbed", "climbed"],
    ["enjoy", "enjoyed", "enjoyed"],
    ["help", "helped", "helped"],
    ["jump", "jumped", "jumped"],
    ["knock", "knocked", "knocked"],
    ["laugh", "laughed", "laughed"],
    ["listen", "listened", "listened"],
    ["look", "looked", "looked"],
    ["open", "opened", "opened"],
    ["pass", "passed", "passed"],
    ["pick", "picked", "picked"],
    ["play", "played", "played"],
    ["rain", "rained", "rained"],
    ["rest", "rested", "rested"],
    ["shout", "shouted", "shouted"],
    ["show", "showed", "showed / shown"],
    ["start", "started", "started"],
    ["stay", "stayed", "stayed"],
    ["talk", "talked", "talked"],
    ["turn", "turned", "turned"],
    ["wait", "waited", "waited"],
    ["wash", "washed", "washed"],
    ["watch", "watched", "watched"],
    ["work", "worked", "worked"],
    ["agree", "agreed", "agreed"],
    ["believe", "believed", "believed"],
    ["change", "changed", "changed"],
    ["close", "closed", "closed"],
    ["dance", "danced", "danced"],

    # --- Page 2 ---
    ["die", "died", "died"],
    ["live", "lived", "lived"],
    ["move", "moved", "moved"],
    ["promise", "promised", "promised"],
    ["smile", "smiled", "smiled"],
    ["use", "used", "used"],
    ["beg", "begged", "begged"],
    ["clap", "clapped", "clapped"],
    ["drop", "dropped", "dropped"],
    ["kidnap", "kidnapped", "kidnapped"],
    ["plan", "planned", "planned"],
    ["rob", "robbed", "robbed"],
    ["rub", "rubbed", "rubbed"],
    ["quarrel", "quarrelled", "quarrelled"],
    ["stir", "stirred", "stirred"],
    ["stop", "stopped", "stopped"],
    ["trap", "trapped", "trapped"],
    ["travel", "travelled", "travelled"],
    ["carry", "carried", "carried"],
    ["copy", "copied", "copied"],
    ["cry", "cried", "cried"],
    ["hurry", "hurried", "hurried"],
    ["pay", "paid", "paid"],
    ["reply", "replied", "replied"],
    ["say", "said", "said"],
    ["study", "studied", "studied"],
    ["tidy", "tidied", "tidied"],
    ["try", "tried", "tried"],
    ["dig", "dug", "dug"],
    ["find", "found", "found"],
    ["get", "got", "got"],
    ["hang", "hung", "hung"],
    ["hang (put to death)", "hanged, hung", "hanged, hung"],
    ["hear", "heard", "heard"],

    # --- Page 3 ---
    ["hold", "held", "held"],
    ["light", "lit", "lit"],
    ["lose", "lost", "lost"],
    ["make", "made", "made"],
    ["sell", "sold", "sold"],
    ["shine", "shone", "shone"],
    ["shoot", "shot", "shot"],
    ["sit", "sat", "sat"],
    ["stand", "stood", "stood"],
    ["stick", "stuck", "stuck"],
    ["strike", "struck", "struck"],
    ["swing", "swung", "swung"],
    ["tell", "told", "told"],
    ["understand", "understood", "understood"],
    ["win", "won", "won"],
    ["bring", "brought", "brought"],
    ["buy", "bought", "bought"],
    ["fight", "fought", "fought"],
    ["think", "thought", "thought"],
    ["creep", "crept", "crept"],
    ["catch", "caught", "caught"],
    ["teach", "taught", "taught"],
    ["feed", "fed", "fed"],
    ["feel", "felt", "felt"],
    ["keep", "kept", "kept"],
    ["kneel", "knelt", "knelt"],
    ["lead", "led", "led"],
    ["leave", "left", "left"],
    ["meet", "met", "met"],
    ["sleep", "slept", "slept"],
    ["smell", "smelt", "smelt"],
    ["spell", "spelt", "spelt"],
    ["sweep", "swept", "swept"],

    # --- Page 4 ---
    ["burn", "burnt / burned", "burnt / burned"],
    ["dream", "dreamt / dreamed", "dreamt / dreamed"],
    ["lean", "leant / leaned", "leant / leaned"],
    ["leap", "leapt / leaped", "leapt / leaped"],
    ["learn", "learnt / learned", "learnt / learned"],
    ["mean", "meant", "meant"],
    ["meet", "met", "met"],
    ["build", "built", "built"],
    ["lend", "lent", "lent"],
    ["send", "sent", "sent"],
    ["spend", "spent", "spent"],
    ["spin", "spun", "spun"],
    ["come", "came", "come"],
    ["become", "became", "become"],
    ["run", "ran", "run"],
    ["bite", "bit", "bitten"],
    ["hide", "hid", "hidden"],
    ["drive", "drove", "driven"],
    ["fall", "fell", "fallen"],
    ["give", "gave", "given"],
    ["ride", "rode", "ridden"],
    ["rise", "rose", "risen"],
    ["shake", "shook", "shaken"],
    ["take", "took", "taken"],
    ["write", "wrote", "written"],
    ["begin", "began", "begun"],
    ["break", "broke", "broken"],
    ["choose", "chose", "chosen"],
    ["drink", "drank", "drunk"],
    ["think", "thought", "thought"],  # (repeated/listed in table)
    ["forget", "forgot", "forgotten"],
    ["forgive", "forgave", "forgiven"],
    ["freeze", "froze", "frozen"],

    # --- Page 5 ---
    ["ring", "rang", "rung"],
    ["shrink", "shrank", "shrunk"],
    ["sing", "sang", "sung"],
    ["sink", "sank", "sunk"],
    ["speak", "spoke", "spoken"],
    ["steal", "stole", "stolen"],
    ["swim", "swam", "swum"],
    ["wake", "woke / waked", "woken / waked"],
    ["win", "won", "won"],
    ["blow", "blew", "blown"],
    ["draw", "drew", "drawn"],
    ["fly", "flew", "flown"],
    ["grow", "grew", "grown"],
    ["know", "knew", "known"],
    ["throw", "threw", "thrown"],
    ["bear", "bore", "borne"],
    ["tear", "tore", "torn"],
    ["wear", "wore", "worn"],
    ["beat", "beat", "beaten"],
    ["eat", "ate", "eaten"],
    ["go", "went", "gone"],
    ["lay (to put or to place)", "laid", "laid"],
    ["lie (to lie down)", "lay", "lain"],
    ["lie (to speak falsely)", "lied", "lied"],
    ["see", "saw", "seen"],
    ["burst", "burst", "burst"],
    ["cost", "cost", "cost"],
    ["cut", "cut", "cut"],
    ["hit", "hit", "hit"],
    ["hurt", "hurt", "hurt"],
    ["let", "let", "let"],

    # --- Page 6 ---
    ["put", "put", "put"],
    ["quit", "quit/quitted", "quit/quitted"],
    ["read", "read", "read"],
    ["set", "set", "set"],
    ["shut", "shut", "shut"],
    ["spread", "spread", "spread"],
    ["be(am/is/are)", "was / were", "been"],
    ["do", "did", "done"],
    ["has/have", "had", "had"]
]


class VerbGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌟 Super Verb Table Game! 🌟")
        self.root.geometry("600x500")
        self.root.config(bg="#f0f8ff")

        # Randomly select 20 verbs out of the 172 verbs every time
        self.questions = random.sample(FULL_VERB_DATABASE, min(20, len(FULL_VERB_DATABASE)))
        self.score = 0
        self.current_question = 0
        self.total_questions = len(self.questions)

        self.title_label = tk.Label(
            root, text="✏️ Fill in the Verb Table Game! ✏️",
            font=("Comic Sans MS", 20, "bold"), bg="#f0f8ff", fg="#2e8b57"
        )
        self.title_label.pack(pady=15)

        self.score_label = tk.Label(
            root, text=f"Score: {self.score} / {self.total_questions}",
            font=("Arial", 14, "bold"), bg="#f0f8ff", fg="#ff4500"
        )
        self.score_label.pack(pady=5)

        self.card_frame = tk.Frame(root, bg="#ffffff", bd=3, relief="ridge")
        self.card_frame.pack(pady=15, padx=20, fill="both", expand=True)

        self.instruction_label = tk.Label(
            self.card_frame, text="Complete the missing verb forms (Press Enter to submit):",
            font=("Arial", 13), bg="#ffffff", fg="#333333"
        )
        self.instruction_label.pack(pady=15)

        fields_frame = tk.Frame(self.card_frame, bg="#ffffff")
        fields_frame.pack(pady=10)

        tk.Label(fields_frame, text="Present:", font=("Arial", 12, "bold"), bg="#ffffff").grid(row=0, column=0,
                                                                                               sticky="w", padx=5,
                                                                                               pady=5)
        self.present_entry = tk.Entry(fields_frame, font=("Arial", 14), width=20)
        self.present_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(fields_frame, text="Past:", font=("Arial", 12, "bold"), bg="#ffffff").grid(row=1, column=0, sticky="w",
                                                                                            padx=5, pady=5)
        self.past_entry = tk.Entry(fields_frame, font=("Arial", 14), width=20)
        self.past_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(fields_frame, text="Past Participle:", font=("Arial", 12, "bold"), bg="#ffffff").grid(row=2, column=0,
                                                                                                       sticky="w",
                                                                                                       padx=5, pady=5)
        self.pp_entry = tk.Entry(fields_frame, font=("Arial", 14), width=20)
        self.pp_entry.grid(row=2, column=1, padx=5, pady=5)

        # Bind Enter key to submission
        self.past_entry.bind("<Return>", lambda event: self.check_answer())
        self.pp_entry.bind("<Return>", lambda event: self.check_answer())

        self.feedback_label = tk.Label(
            self.card_frame, text="", font=("Arial", 12, "italic"), bg="#ffffff"
        )
        self.feedback_label.pack(pady=10)

        self.submit_btn = tk.Button(
            root, text="Check Answer 🚀", font=("Arial", 14, "bold"),
            bg="#4682b4", fg="white", padx=10, pady=5, command=self.check_answer
        )
        self.submit_btn.pack(pady=15)

        self.load_question()

    def load_question(self):
        if self.current_question < self.total_questions:
            self.present_entry.config(state="normal")
            self.past_entry.config(state="normal")
            self.pp_entry.config(state="normal")

            self.present_entry.delete(0, tk.END)
            self.past_entry.delete(0, tk.END)
            self.pp_entry.delete(0, tk.END)
            self.feedback_label.config(text="")

            current_verb = self.questions[self.current_question]
            self.present_entry.insert(0, current_verb[0])
            self.present_entry.config(state="disabled")

            self.correct_answers = {
                "past": current_verb[1].lower().strip(),
                "pp": current_verb[2].lower().strip()
            }
            self.past_entry.focus()
        else:
            self.show_final_score()

    def check_answer(self):
        user_past = self.past_entry.get().strip().lower()
        user_pp = self.pp_entry.get().strip().lower()

        if not user_past or not user_pp:
            messagebox.showwarning("Oops!", "Please fill in all the blank boxes!")
            return

        if user_past == self.correct_answers["past"] and user_pp == self.correct_answers["pp"]:
            self.score += 1
            self.feedback_label.config(text="🎉 Correct! Great job!", fg="green")
            self.score_label.config(text=f"Score: {self.score} / {self.total_questions}")
            self.root.after(1200, self.next_question)
        else:
            correct_str = f"Past: {self.correct_answers['past']}, Past Participle: {self.correct_answers['pp']}"
            self.feedback_label.config(text=f"❌ Not quite! Correct was -> {correct_str}", fg="red")
            self.root.after(2500, self.next_question)

    def next_question(self):
        self.current_question += 1
        self.load_question()

    def show_final_score(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        end_frame = tk.Frame(self.root, bg="#f0f8ff")
        end_frame.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(
            end_frame, text="🏆 Quiz Completed! 🏆",
            font=("Comic Sans MS", 22, "bold"), bg="#f0f8ff", fg="#ff8c00"
        ).pack(pady=20)

        tk.Label(
            end_frame, text=f"Your Final Score: {self.score} / {self.total_questions}",
            font=("Arial", 18, "bold"), bg="#f0f8ff", fg="#2e8b57"
        ).pack(pady=10)

        praise = "Amazing work! You're a grammar star! ⭐" if self.score == self.total_questions else "Good effort! Keep practicing your verb tables! 👍"
        tk.Label(
            end_frame, text=praise, font=("Arial", 14), bg="#f0f8ff", fg="#333333"
        ).pack(pady=15)

        restart_btn = tk.Button(
            end_frame, text="Play Again (New Verbs!) 🔄", font=("Arial", 14, "bold"),
            bg="#3cb371", fg="white", padx=15, pady=8, command=self.restart_game
        )
        restart_btn.pack(pady=20)

    def restart_game(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)


if __name__ == "__main__":
    root = tk.Tk()
    app = VerbGroupApp if 'VerbGroupApp' in globals() else VerbGameApp(root)
    root.mainloop()
