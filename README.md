# Self.py_Course
Self.py Course - Campus IL

## Hangman game
1. Print the opening screen.
2. Ask the player to enter: (a) a path to a word file and (b) a location (index) for a word in the file. Depending on the input from the player, the secret word for the game will be selected.
3. Introduce to the player the appropriate condition of the dependent man according to the number of his failed attempts. At the beginning of the game present the opening mode (the first of the seven modes, i.e. the horizontal line of the hanger).
4. Underneath the hanging man, the player was introduced to the secret word in the form of underlines (with spaces).
5. Ask the player to enter one character input in each round.
If the character is invalid (two or more characters and / or is not an English letter, or guessed it in the past), type "X" on the screen (as you did in the task at the end of the unit list), print the list of previously guessed letters (sorted in lower case Grow and separated by arrows) and ask the player to enter another character until the character to be typed is correct.
6. After each correct guess, present the player with the secret word in the form of underlines (even if he guessed partially or has not yet been able to guess at all).
In case of a failed guess - print the output for the player ":(" and below it print a picture of the man hanging in a more "advanced" mode.
7. End of the game:

    -If the player guessed the whole word correctly - print to the WIN screen.

    -If the player guesses six failed attempts - print to the LOSE screen.


### Example

```python
# Print the Welcome Screen
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
6

Enter file path: C:\files\words.txt
Enter index: 5

Let’s start!

    x-------x
_ _ _

Guess a letter: ^
X
Guess a letter: T
_ _ t
Guess a letter: b
:(
    x-------x
    |
    |
    |
    |
    |

_ _ t 
Guess a letter: c
c _ t 
Guess a letter: t
X
b -> c -> t
Guess a letter: p
:(

    x-------x
    |       |
    |       0
    |
    |
    |

c _ t
Guess a letter: a
c a t
WIN
```
