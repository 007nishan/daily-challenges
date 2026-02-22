### Key Concepts
1. **Conditional Logic (if/else)**: How multiple conditions (date ranges) determine the output.
2. **Date Parsing**: Converting day/month integers into a comparable date object or range.
3. **String Formatting**: Creating the output string correctly.

### Approach
- Identify the date ranges for each zodiac sign.
- Use `if-elif-else` blocks to check which range the input `(day, month)` falls into.
- Handle edge cases like invalid dates (e.g., month > 12 or day > 31).
