# Password Manager

Look, we both know you're using the same password everywhere. No judgment but let's change that.

# Screenshots


![screenshot]("password manager CLI screenshot.png")


## About

This is a simple commandline password manager I built for fun and learning. It generates secure passwords and stores them locally so you don't have to remember everything.

It does the basics: creates random passwords, generates passphrases, saves them, and lets you view them later. Nothing fancy, just something that works.

## Requirements

You'll need Python 3 and a couple of libraries:

```bash
pip install pyperclip pandas
```

You'll also need a `words.txt` file with a list of words (one per line) for the passphrase generator. Any word list works—just search for "common words list" online.

## Usage

Run it:

```bash
python password_manager.py
```

The menu is pretty straightforward. Generate a password, generate a passphrase, view what you've saved, or exit. Everything you generate gets copied to your clipboard automatically.

## Important Note

The passwords in the database are stored as plain text. No encryption, no hashing, nothing. This is purely for educational purposes and messing around. If someone gets access to your `passwords.db` file, they can read everything.

So yeah, use this for learning or just for fun, but don't trust it with anything important. For real password management, go with something like Bitwarden or 1Password.

## What's Included

•`password_manager.py` : The main script
•`words.txt` : Your word list (you need to add this)
•`passwords.db` :  Gets created when you save your first password

## Author

Sandman.
