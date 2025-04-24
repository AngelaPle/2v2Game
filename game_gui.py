import random
import tkinter as tk
from tkinter import simpledialog, messagebox
import game_logic
from tkinter import ttk
from PIL import Image, ImageTk  # Importa le librerie per gestire le immagini

class GameGUI:
    def __init__(self, master):
        self.master = master
        master.title("Epic 2 vs 2 Battle!")
        master.geometry("800x600")
        master.configure(bg='#f0f8ff')  # LightSteelBlue per uno sfondo più gradevole

        # *** STILI UNIFICATI E ANCORA PIÙ CARINI ***
        self.font_labels = ('Segoe UI', 14)
        self.font_labels_large = ('Segoe UI', 16, 'bold') # Font più grande per i nomi dei team
        self.font_title = ('Segoe UI', 20, 'bold') # Font per il titolo
        self.font_buttons = ('Segoe UI', 14, 'bold')
        self.bg_color_entry = '#e0ffff'  # LightCyan per i campi di input
        self.text_color = '#2f4f4f'  # DarkSlateGray per il testo
        self.button_color = '#4682b4'  # SteelBlue per i bottoni
        self.button_text_color = 'white'
        self.health_bar_color = '#3cb371'  # MediumSeaGreen per la barra di salute
        self.health_bar_bg = '#f0fff0'  # Honeydew per lo sfondo della barra di salute
        self.output_bg = '#f5f5dc'  # Beige per l'output
        self.output_fg = '#006400'  # DarkGreen per il testo dell'output
        self.dropdown_bg = '#afeeee'  # PaleTurquoise per i dropdown
        self.dropdown_fg = '#191970'  # MidnightBlue per il testo dei dropdown

        # Carica l'immagine di sfondo e la ridimensiona
        try:
            self.background_image = Image.open("/Users/angela.plescia/Desktop/Biomedical Project/2v2Game.jpg")  # Sostituisci con il percorso effettivo
            self.resized_image = self.background_image.resize((master.winfo_width(), master.winfo_height()))
            self.background_photo = ImageTk.PhotoImage(self.resized_image)
            self.background_label = tk.Label(master, image=self.background_photo)
            self.background_label.place(relwidth=1, relheight=1)

            # Aggiorna lo sfondo quando la finestra viene ridimensionata
            master.bind("<Configure>", self._resize_background)

        except FileNotFoundError:
            messagebox.showerror("Errore", "Immagine di sfondo non trovata!")
            master.config(bg='#f0f8ff') # Se l'immagine non c'è, usa un colore di sfondo gradevole

         # Titolo
        ttk.Label(master, text="2 vs 2 EPIC BATTLE", font=self.font_title, background='#f0f8ff', foreground='#4682b4').grid(row=0, column=0, columnspan=2, pady=(10, 20))

        # Configurazione del peso per righe e colonne per un layout più flessibile
        for i in range(13):  # Aumento righe per il titolo
            master.grid_rowconfigure(i, weight=1)
        for i in range(2):
            master.grid_columnconfigure(i, weight=1)

        # Opzioni per il tipo di personaggio
        self.character_types = ["Warrior", "Mage", "Archer"]

        # Team 1 Input
        ttk.Label(master, text="Team 1", font=self.font_labels_large, background=self.bg_color_entry, foreground=self.text_color).grid(row=1, column=0, padx=10, pady=5, sticky='ew') # Sposta in basso per il titolo
        self.team1_name_entry = ttk.Entry(master, font=self.font_labels)
        self.team1_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

        ttk.Label(master, text="Character 1 Type:", font=self.font_labels, background=self.bg_color_entry, foreground=self.text_color).grid(row=2, column=0, padx=10, pady=5, sticky='ew') # Sposta in basso
        self.char1_type = tk.StringVar(master)
        self.char1_type.set("") # Imposta come vuoto inizialmente
        self.char1_type_dropdown = ttk.Combobox(master, textvariable=self.char1_type, values=self.character_types, font=self.font_labels, style="Dropdown.TCombobox")
        self.char1_type_dropdown.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

        ttk.Label(master, text="Character 2 Type:", font=self.font_labels, background=self.bg_color_entry, foreground=self.text_color).grid(row=3, column=0, padx=10, pady=5, sticky='ew') # Sposta in basso
        self.char2_type = tk.StringVar(master)
        self.char2_type.set("") # Imposta come vuoto inizialmente
        self.char2_type_dropdown = ttk.Combobox(master, textvariable=self.char2_type, values=self.character_types, font=self.font_labels, style="Dropdown.TCombobox")
        self.char2_type_dropdown.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

        # Team 2 Input
        ttk.Label(master, text="Team 2", font=self.font_labels_large, background=self.bg_color_entry, foreground=self.text_color).grid(row=4, column=0, padx=10, pady=5, sticky='ew') # Sposta in basso
        self.team2_name_entry = ttk.Entry(master, font=self.font_labels)
        self.team2_name_entry.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

        ttk.Label(master, text="Character 3 Type:", font=self.font_labels, background=self.bg_color_entry, foreground=self.text_color).grid(row=5, column=0, padx=10, pady=5, sticky='ew') # Sposta in basso
        self.char3_type = tk.StringVar(master)
        self.char3_type.set("") # Imposta come vuoto inizialmente
        self.char3_type_dropdown = ttk.Combobox(master, textvariable=self.char3_type, values=self.character_types, font=self.font_labels, style="Dropdown.TCombobox")
        self.char3_type_dropdown.grid(row=5, column=1, padx=10, pady=5, sticky='ew')

        ttk.Label(master, text="Character 4 Type:", font=self.font_labels, background=self.bg_color_entry, foreground=self.text_color).grid(row=6, column=0, padx=10, pady=5, sticky='ew') # Sposta in basso
        self.char4_type = tk.StringVar(master)
        self.char4_type.set("") # Imposta come vuoto inizialmente
        self.char4_type_dropdown = ttk.Combobox(master, textvariable=self.char4_type, values=self.character_types, font=self.font_labels, style="Dropdown.TCombobox")
        self.char4_type_dropdown.grid(row=6, column=1, padx=10, pady=5, sticky='ew')

        # Start Battle Button
        self.start_button = ttk.Button(master, text="Start Battle!", command=self.start_battle,
                                       style="StartButton.TButton")
        self.start_button.grid(row=7, column=0, columnspan=2, pady=20, padx=10, sticky='ew') # Sposta in basso

        # Health Bars Frame
        self.health_frame = ttk.Frame(master)
        self.health_frame.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky='ew') # Sposta in basso
        self.health_frame.grid_columnconfigure(0, weight=1)
        self.health_frame.grid_columnconfigure(1, weight=1)

        self.health_bars = {}
        self.health_labels = {}

        # Output Text Area
        self.output_text = tk.Text(master, height=10, width=60, font=self.font_labels, bg=self.output_bg, fg=self.output_fg, relief=tk.SUNKEN, borderwidth=2)
        self.output_text.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky='nsew') # Sposta in basso
        self.output_text.config(state=tk.DISABLED)

        self.battle_running = False
        self.battle_turn = 0 # Inizializza battle_turn qui

        # *** STILI TTK ***
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Un tema che permette una buona personalizzazione

        self.style.configure('TLabel', font=self.font_labels, background=self.bg_color_entry, foreground=self.text_color, padding=5) # Aggiunto padding
        self.style.configure('TEntry', font=self.font_labels, background=self.bg_color_entry, foreground=self.text_color, padding=5) # Aggiunto padding
        self.style.configure('TCombobox', font=self.font_labels, background=self.dropdown_bg, foreground=self.dropdown_fg, padding=5) # Aggiunto padding
        self.style.map('TCombobox',
                       background=[('active', '#b0e0e6')], # Cambia colore al passaggio del mouse
                       foreground=[('active', self.dropdown_fg)])

        self.style.configure('StartButton.TButton', font=self.font_buttons, background=self.button_color, foreground=self.button_text_color, padding=10)
        self.style.map('StartButton.TButton',
                       background=[('active', '#5e94c1')]) # Cambia colore al passaggio del mouse

        self.style.configure("Health.Horizontal.TProgressbar",
                             foreground=self.health_bar_color,
                             background=self.health_bar_bg)
        self.style.layout("Health.Horizontal.TProgressbar",
                          [('Horizontal.Progressbar.trough',
                            {'children': [('Horizontal.Progressbar.pbar',
                                          {'side': 'left', 'sticky': 'ns'})],
                             'sticky': 'ewns'}),
                           ('Horizontal.Progressbar.label', {'sticky': 'ew'})])
        self.style.configure("Health.Horizontal.TProgressbar", text='0 %', anchor='center')

    def _resize_background(self, event):
        new_width = event.width
        new_height = event.height
        self.resized_image = self.background_image.resize((new_width, new_height))
        self.background_photo = ImageTk.PhotoImage(self.resized_image)
        self.background_label.config(image=self.background_photo)

    def create_character(self, name, char_type):
        char_type = char_type.lower()
        if char_type == "warrior":
            return game_logic.Warrior(name)
        elif char_type == "mage":
            return game_logic.Mage(name)
        elif char_type == "archer":
            return game_logic.Archer(name)
        else:
            return game_logic.Character(name, 100, 10) # Default character

    def output_to_gui(self, text):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, text + "\n")
        self.output_text.config(state=tk.DISABLED)
        self.output_text.see(tk.END)

    def update_health_bars(self, team):
        for char in team.members:
            if char.name in self.health_bars:
                self.health_bars[char.name]['value'] = char.get_health_percentage() * 100
                self.health_bars[char.name]['text'] = f"{int(self.health_bars[char.name]['value'])} %" # Aggiorna il testo
                self.health_bars[char.name]['compound'] = 'center'
                self.health_labels[char.name]['text'] = f"{char.name}: {char.health}/{char.max_health}"

    def start_battle(self):
        if self.battle_running:
            messagebox.showinfo("Attention", "The battle is already running!")
            return

        team1_name = self.team1_name_entry.get()
        char1_type = self.char1_type.get()
        char2_type = self.char2_type.get()
        team2_name = self.team2_name_entry.get()
        char3_type = self.char3_type.get()
        char4_type = self.char4_type.get()

        if not all([team1_name, char1_type, char2_type, team2_name, char3_type, char4_type]):
            messagebox.showerror("Error", "Please enter names for all teams and character types.")
            return

        team1 = game_logic.Team(team1_name)
        team1.add_member(self.create_character(f"{team1_name} 1", char1_type))
        team1.add_member(self.create_character(f"{team1_name} 2", char2_type))

        team2 = game_logic.Team(team2_name)
        team2.add_member(self.create_character(f"{team2_name} 1", char3_type))
        team2.add_member(self.create_character(f"{team2_name} 2", char4_type))

        # Clear previous output and health bars
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state=tk.DISABLED)

        for name in list(self.health_bars.keys()):
            self.health_bars[name].destroy()
            self.health_labels[name].destroy()
        self.health_bars = {}
        self.health_labels = {}

        # Create initial health bars
        for i, char in enumerate(team1.members):
            row = 10 + i # Sposta in basso
            label = ttk.Label(self.master, text=f"{char.name}: {char.health}/{char.max_health}")
            label.grid(row=row, column=0, padx=10, pady=5, sticky='ew')
            progress = ttk.Progressbar(self.master, orient=tk.HORIZONTAL, length=200, mode='determinate', maximum=100, style="Health.Horizontal.TProgressbar")
            progress['value'] = char.get_health_percentage() * 100
            progress['text'] = f"{int(progress['value'])} %"
            progress['compound'] = 'center'
            progress.grid(row=row, column=1, padx=10, pady=5, sticky='ew')
            self.health_bars[char.name] = progress
            self.health_labels[char.name] = label

        for i, char in enumerate(team2.members):
            row = 10 + i + 2 # Offset for team 2, sposta in basso
            label = ttk.Label(self.master, text=f"{char.name}: {char.health}/{char.max_health}")
            label.grid(row=row, column=0, padx=10, pady=5, sticky='ew')
            progress = ttk.Progressbar(self.master, orient=tk.HORIZONTAL, length=200, mode='determinate', maximum=100, style="Health.Horizontal.TProgressbar")
            progress['value'] = char.get_health_percentage() * 100
            progress['text'] = f"{int(progress['value'])} %"
            progress['compound'] = 'center'
            progress.grid(row=row, column=1, padx=10, pady=5, sticky='ew')
            self.health_bars[char.name] = progress
            self.health_labels[char.name] = label

        self.battle_running = True
        self.battle_turn = 0 # Reinizializza il turno all'inizio di ogni battaglia
        self.run_battle_step(team1, team2)

    def run_battle_step(self, team1, team2):
        if not team1.alive_members() or not team2.alive_members():
            winner_team = team1.name if team1.alive_members() else team2.name
            self.output_to_gui(f"\n--- {winner_team} Wins! ---")
            messagebox.showinfo("Winner!", f"{winner_team} has won the battle!")
            self.battle_running = False
            return

        attacker_team = team1 if self.battle_turn % 2 == 0 else team2
        defender_team = team2 if attacker_team == team1 else team1

        attacker = attacker_team.random_alive_member()
        defender = defender_team.random_alive_member()

        if attacker and defender:
            # Action selection (basic attack or special ability)
            action = "attack"
            if random.random() < 0.4: # 40% chance to use special ability
                action = "special"

            if action == "attack":
                damage, crit = attacker.deal_damage(defender)
                attack_text = f"{attacker.name} attacks {defender.name} for {damage} damage."
                if crit:
                    attack_text += " Critical hit!"
                self.output_to_gui(attack_text)
            elif action == "special":
                special_damage, special_text = attacker.special_ability(defender, self.output_to_gui)
                if special_text:
                    self.output_to_gui(f"{attacker.name} uses {special_text}.")

            if defender.is_alive():
                self.output_to_gui(f"{defender.name}'s health: {defender.health}/{defender.max_health}")
            else:
                self.output_to_gui(f"{defender.name} has been defeated!")

            self.update_health_bars(team1)
            self.update_health_bars(team2)

            self.battle_turn += 1
            self.master.after(500, self.run_battle_step, team1, team2)
        else:
            winner_team = team1.name if team1.alive_members() else team2.name
            self.output_to_gui(f"\n--- {winner_team} Wins! ---")
            messagebox.showinfo("Winner!", f"{winner_team} has won the battle!")
            self.battle_running = False
            return

    battle_turn = 0

if __name__ == "__main__":
    root = tk.Tk()
    gui = GameGUI(root)
    root.mainloop()