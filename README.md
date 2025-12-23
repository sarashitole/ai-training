📌 What does your script do?

My Python script calls a public API to get a random joke.
It reads the JSON response and prints three fields:

Type of the joke

Setup of the joke

Punchline

It also handles errors like no internet, API failure, or timeout, so the program does not crash.

📌 Which API did you use?

I used the Official Joke API, a free public API.

API Endpoint:https://official-joke-api.appspot.com/random_joke
📌 What broke while building it?

While building the project, I faced a few problems:

requests library was not installed → fixed by running pip install requests.

Python could not find the file → fixed by checking the folder and file name.

GitHub push failed initially because remote URL was incorrect → fixed by adding the correct URL.

📌 Show it running

When the program runs successfully, the output looks like:Type: general
Setup: Why did the programmer quit his job?
Punchline: Because he didn't get arrays.
📌 Explain one mistake you made

One mistake I made was initially running Git in the wrong folder.
Git could not find my file, so the commit failed.
I fixed it by navigating to the correct folder where week1.py is located before running Git commands.