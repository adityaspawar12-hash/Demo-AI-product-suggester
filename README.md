## Demo-AI-product-suggester

Structure for future  AI model project


## Features

- Suggests phones based on budget
- Takes user input (budget, purpose)
- Provides multiple recommendations

 ##  How It Works
 
The system takes user input:

- Category (currently: phone)
- Budget
- Purpose (gaming / camera / general)

Then it applies rule-based logic to recommend the best matching smartphones.


## Tech Used

- Python
- Conditional Statements (if-elif-else)
- Functions
- Basic CLI input/output

##Challenges & Solutions

Developing a rule-based recommendation engine involves more than just writing code; it requires structuring data so it is scalable and user-friendly.

1. Handling Invalid Inputs

The Problem: During initial testing, if a user entered a string (e.g., "five thousand") instead of an integer for the budget, or typed "Gaming" with a capital letter, the program would crash or fail to find a match.

The Solution: I implemented input normalization and error handling.

Used .strip().lower() on all string inputs to ensure case-insensitivity.

Wrapped budget inputs in try-except blocks or used isdigit() checks to prevent crashes from non-numeric data.

2. Logic Overlap (The "Budget Gap")

The Problem: Early versions used strict equality for budgets, meaning if a user had ₹15,500, but my rules only looked for ₹15,000 or ₹20,000, they received no recommendation.

The Solution: I transitioned from specific values to Range-Based Logic. By using comparison operators (e.g., if budget >= 15000 and budget < 25000), the system became much more flexible and "intelligent" in its suggestions.

3. Avoiding "Spaghetti Code"

The Problem: As the number of phone models grew, the if-elif-else chain became long, repetitive, and difficult to read.

The Solution: I refactored the code using Functions. Instead of one giant block of code, I created specific functions for different categories.

Future Iteration: I am planning to move this data into a Dictionary or JSON file to decouple the data from the logic entirely


