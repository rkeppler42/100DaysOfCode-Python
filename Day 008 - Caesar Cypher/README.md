# 🔐 Caesar Cipher

This is the project for **Day 08** of the course  
**"100 Days of Code: The Complete Python Pro Bootcamp"**.

A working implementation of the **Caesar Cipher** — one of the oldest encryption techniques — that can both encode and decode messages using a user-defined shift number.

---

## 🧠 What I Learned

- Defining and calling **functions** with multiple parameters
- Using keyword arguments for clearer function calls
- Encrypting and decrypting with **modular arithmetic** (`%`) to wrap around the alphabet
- Handling **non-alphabetic characters** (spaces, punctuation) by passing them through unchanged
- Reversing the shift to handle decoding
- Using a `while` loop to let the user **run the program multiple times**
- Using a **ternary expression** to set a boolean from user input

---

## 🛠️ Requirements

The final program must:

1. Display the **Caesar Cipher logo** on start.
2. Ask the user whether they want to **encode** or **decode**.
3. Ask for the **message** and the **shift number**.
4. Apply the Caesar Cipher logic:
   - Shift each letter forward (encode) or backward (decode) by the given amount.
   - **Wrap around** the alphabet using modulo so the shift never goes out of bounds.
   - Leave **non-letter characters** (spaces, numbers, punctuation) unchanged.
5. Print the result.
6. Ask if the user wants to **go again**, and loop if they say yes.

---

## 📝 Example Output

```
Type 'encode' to encrypt, type 'decode' to decrypt:
> encode
Type your message:
> hello world
Type the shift number:
> 5
Here is the encoded result: mjqqt btwqi

Type 'yes' if you want to go again. Otherwise type 'no'.
> decode
...
```

---

## 📦 Project Structure

```
Day 008 - Caesar Cipher/
│── main.py
│── art.py
└── README.md
```

| File | Purpose |
|------|---------|
| `main.py` | Cipher logic and user interaction loop |
| `art.py` | ASCII art logo |

---

## 🏁 Status

✅ Completed