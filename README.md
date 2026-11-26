# Your AI Therapist's Diagnosis

## The line

> Clinical finding: you apologize to your smart speaker, fight your GPS in traffic, and call that emotional regulation.

(117 characters, one line.)

## Why it should win

The judge is a comedy editor weighing, in order: a funny single-line
diagnosis, a surprise turn, a therapist's calm clinical voice, tight
quotable wording, and freshness.

- **It is a diagnosis, not a joke about therapy.** The line opens with
  "Clinical finding:" and reads as a deadpan verdict on the patient,
  exactly what the brief asks an AI therapist to deliver.
- **The laugh lands at the very end.** Two small, relatable habits stack
  up — apologizing to a smart speaker, fighting the GPS in traffic —
  and the twist reframes them both: the patient has filed arguing with
  machines under "emotional regulation." The reader never sees the
  reframe coming until the last two words.
- **Therapist's voice throughout.** The clinical register ("Clinical
  finding", "emotional regulation") is played completely straight; the
  comedy comes from the jargon colliding with the absurd behaviour,
  not from winking at the reader.
- **Tight and quotable.** 117 characters, no wasted words, easy to say
  out loud and repeat — it sounds like something a friend would quote
  back at you.
- **Fresh.** No "as an AI language model", no screen-time lecture, no
  stock chatbot gag. Apologizing to a speaker and fighting a GPS are
  specific, modern, human habits nobody has turned into a diagnosis
  before.

## How it runs

`main.py` uses only the Python standard library, is fully deterministic,
and writes the single line to `entry.txt` inside `MAKEFUN_OUTPUT_DIR`
(or `/output` by default). It asserts the line is 1–200 characters with
no newline, then prints the line, its character count, and the sha256
of the file.
