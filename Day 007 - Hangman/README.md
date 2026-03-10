# 🪓 Hangman

This is the project for **Day 07** of the course  
**"100 Days of Code: The Complete Python Pro Bootcamp"**.

A classic **Hangman** game where the player tries to guess a hidden word one letter at a time before running out of lives.

---

## 🧠 What I Learned

- Splitting code across **multiple files** and importing from them
- Using `random.choice()` to pick a random item from a list
- Building and updating a **display string** with underscores and revealed letters
- Tracking state with lists (`correct_letters`, `guessed_letters`)
- Using a `while` loop to keep the game running until win or lose
- Detecting **repeated guesses** and warning the player
- Indexing into a list to display the correct **ASCII art stage**
- Structuring a project with separate files for art, words, and logic

---

## 🛠️ Requirements

The final program must:

1. Display the **Hangman logo** on start.
2. Pick a **random word** from the word list.
3. Show the word as a series of **underscores** (`_`) matching its length.
4. On each turn:
   - Show how many **lives remain** (out of 6).
   - Ask the player to **guess a letter**.
   - Reveal all matching letters in the word.
   - Warn the player if they **already guessed** that letter.
   - Deduct a life if the guess is **wrong**.
   - Print the appropriate **hangman ASCII art** stage.
5. End the game when:
   - The player **guesses all letters** → `YOU WIN`
   - The player **runs out of lives** → `YOU LOSE` + reveal the word

---

## 📝 Example Output

```
 _                                             
| |__   __ _ _ __   __ _ _ __ ___ ...

****************************6/6 LIVES LEFT****************************
Guess a letter: a
Word to guess: _ a _ _ _ a _

****************************5/6 LIVES LEFT****************************
Guess a letter: e
e is not in the word

  +---+
  |   |
  O   |
      |
      |
      |
=========
```

---

## 📦 Project Structure

```
Day 007 - Hangman/
│── main.py
│── hangman_art.py
│── hangman_words.py
└── README.md
```

| File | Purpose |
|------|---------|
| `main.py` | Game logic and loop |
| `hangman_art.py` | ASCII art stages and logo |
| `hangman_words.py` | Word list to draw from |

---

## 🏁 Status

✅ Completed