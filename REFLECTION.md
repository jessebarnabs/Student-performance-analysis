# Reflection and AI Use Declaration

## Reflection: challenges I encountered

My first challenge was setup. Python was not recognised in the VS Code terminal, and the terminal would not open at all because it was pointing to a folder that no longer existed because i had moved my file to a different location hence i had to restart my vs code for it to work.

The hardest part of the project was indentation. Several times my methods ended up outside the class or inside a loop, which caused an `IndentationError` and an `AttributeError`. I learned to read the line number in the error message and to check the column position of each line. I also got a `NameError` twice because I wrote a class below the code that used it, and I learned that Python reads a file from top to bottom, so a class must be defined before it is used.

Two bugs taught me the most. I accidentally wrote `get_summary` twice in the same class, so Python silently kept only the second one and my regular student was described as a scholarship student. I also placed a `return` inside the `for` loop of `average()`, which stopped it from checking every mark. Both bugs ran without crashing, so I had to compare the output against what I expected. If I did this project again, I would test each class straight after writing it instead of waiting until the end.

## AI use declaration

I used Claude, an AI assistant made by Anthropic, while completing this assignment. It explained the OOP concepts (encapsulation, abstraction, inheritance, polymorphism and variable-length arguments), provided code and templates for the classes, the analyzer, the CSV loader and the report, helped me understand error messages, and drafted the text of this reflection and declaration based on the problems I ran into since i used it to help me locate my problems.

I typed the code into my own files, ran and tested it myself, fixed errors, and checked the output against the assignment brief. I reviewed this document before submitting it.
