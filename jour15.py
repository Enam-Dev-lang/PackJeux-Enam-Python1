import tkinter as tk
import random


# --- JEU 1 : DEVINETTE ---
def ouvrir_devinette():
    win = tk.Toplevel()
    win.title("Devinette")
    win.geometry("300x200")
    secret = random.randint(1, 100)
    vies = 10
    def tester():
        nonlocal vies
        try:
            n = int(entry.get())
            if n == secret:
                lbl.config(text="GAGNE!🎉🎇")
            else:
                vies-= 1
                txt= "Plus grand' if n < secret else'Plus petit"
                lbl.config(text=f"{txt} - {vies[0]} vies")
        except:pass
    tk.Label(win, text="Devine 1 à 100 - 10 vies").pack(pady=10)
    entry = tk.Entry(win, font=("Arial, 14"))
    entry.pack()
    tk.Button(win, text="Deviner", bg="blue", fg="white", command=tester).pack(pady=10)
    lbl = tk.Label(win, text="", font=("Arial", 12, "bold"))
    lbl.pack()


# --- JEU 2 : CALCULATRICE ---
def ouvrir_calc():
    win = tk.Toplevel()
    win.title("Calculatrice")
    expr = tk.StringVar()
    tk.Entry(win, textvariable=expr, font=("Arial", 18)).pack(fill="x", pady=10)
    def clic(t):
        if t == "=":
            try: expr.set(str(eval(expr.get())))
            except: expr.set("Erreur")
        elif t == "C": expr.set("")
        else: expr.set(expr.get()+t)
    frame = tk.Frame(win)
    frame.pack()
    for i, t in enumerate(["7", "8", "9", "/", "4", "5", "6","*", "1", "2", "3","-", "0", "C", "=", "+"]):
        tk.Button(frame, text=t, width=5, height=2, command=lambda x=t: clic(x)).grid( row=i//4, column=i%4, padx=2, pady=2)


    # --- JEU 3 : MORPION ---
def ouvrir_morpion():
        win = tk.Toplevel()
        win.title("Morpion")
        tour = ["X"]
        btns = []
        def jouer(i):
            if btns[i]["text"] == "":
                btns[i].config(text=tour[0])
                tour[0] = "0" if tour[0]=="X" else "X"
        grille = tk.Frame(win)
        grille.pack(pady=20)
        for i in range(9):
            b = tk.Button(grille, text="", width=4, height=2, font= ("Arial", 20, "bold"), command=lambda k=i: jouer(k))
            b.grid(row=i//3, column=i%3, padx=2, pady=2)
            btns.append(b)


# --- JEU 4 : SNAKE (NOUVEAU JOUR 15) ---
def ouvrir_snake():
    win = tk.Toplevel()
    win.title("Snake-Jour15")
    win.geometry("420x440")
    canvas = tk.Canvas(win, width=400, height=400, bg="black")
    canvas.pack()
    canvas.focus_set() # <- C'est ça qui manquait!



    snake = [(100, 100), (80, 100), (60, 100)]
    food = (200, 200)
    score = [0]
    direction = ["Right"]


    def change_dir(new_dir):
        opposites = {"Up":"Down", "Down":"Up", "Left":"Right", "Right":"Left"}
        if opposites[new_dir]!= direction[0]:
            direction[0] = new_dir


    def move():
        nonlocal food
        x, y = snake[0]
        if direction[0] == "Up": y -= 20
        if direction[0] == "Down": y +=20
        if direction[0] == "Left": x -=20
        if direction[0] == "Right": x +=20
        new_head = (x, y)
        if x < 0 or x >= 400 or y < 0 or y >= 400 or new_head in snake:
            canvas.create_text(200, 200, text=f"GAME OVER\nScore: {score[0]}", fill="white", font=("Arial", 20, "bold")); return
        snake.insert(0, new_head)
        if new_head == food:
            score[0] += 1; food = (random.randint(0, 19)*20, random.randint(0, 19)*20)
        else: snake.pop()
        canvas.delete("all")
        canvas.create_rectangle(food[0], food[1], food[0]+20, food[1]+20, fill="red")
        for sx, sy in snake: canvas.create_rectangle(sx, sy, sx+20, sy+20, fill="green")
        canvas.create_text(50, 15, text=f"Score: {score[0]}", fill="white", font=("Arial", 12))
        win.after(100, move)


    win.bind("<Up>", lambda e: change_dir("Up"))
    win.bind("<Down>", lambda e: change_dir("Down"))
    win.bind("<Left>", lambda e: change_dir("Left"))
    win.bind("<Right>", lambda e: change_dir("Right"))
    win.bind("<a>", lambda e: change_dir("Up"))
    win.bind("<z>", lambda e: change_dir("Down"))
    win.bind("<e>", lambda e: change_dir("Left"))
    win.bind("<r>", lambda e: change_dir("Right"))
    move()


# --- MENU PRINCIPAL ---
fen = tk.Tk()
fen.title("Mon Pack Jeux - jour15")
fen.geometry("420x550")
fen.config(bg="black")
tk.Label(fen, text="MES JEUX PYTHON", font=("Arial", 22, "bold"), bg="black", fg="white").pack(pady=20)
tk.Button(fen, text="1. Devinette (Jour 9)", font=("Arial", 14), bg="#3498db", fg="white", width=25, height=2, command=ouvrir_devinette).pack(pady=7)
tk.Button(fen, text="2. Calculatrice (Jour 11)", font=("Arial", 14), bg="#e67e22", fg="white", width=25, height=2, command=ouvrir_calc).pack(pady=7)
tk.Button(fen, text="3. Morpion (Jour 12)", font=("Arial", 14), bg="#2ecc71", fg="white", width=25, height=2, command=ouvrir_morpion).pack(pady=7)
tk.Button(fen, text="4. SNAKE - NEW! (Jour15) ", font=("Arial", 14, "bold"), bg="#f1c40f", fg="black", width=25, height=2, command=ouvrir_snake).pack(pady=7) 
tk.Label(fen, text="Pack Final V2- Créé par Enam - Jour 15", bg="black", fg="gray").pack(side="bottom", pady=20)
fen.mainloop()