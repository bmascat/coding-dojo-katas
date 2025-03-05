# String Calculator Kata

This is a Test-Driven Development (TDD) kata designed to help you improve your incremental development and refactoring skills.

## Instructions

- Try not to read ahead.
- Solve one task at a time.
- Only test for correct inputs; invalid inputs do not require tests.
- Always follow a test-first approach.

## String Calculator Requirements

1. **Basic Addition**  
   - Implement a `StringCalculator` class with a method:
     ```csharp
     public int Add(string numbers)
     ```
   - The method can take 0, 1, or 2 numbers and return their sum.
   - If the input is an empty string (`""`), return `0`.
   - Examples:
     ```
     "" => 0
     "1" => 1
     "1,2" => 3
     ```
   - Start with the simplest test case and incrementally add complexity.
   - Always refactor after a test passes.

2. **Handle an Unknown Number of Numbers**  
   - Modify `Add` to handle any amount of numbers.

3. **Support New Line as a Delimiter**  
   - Allow new lines (`\n`) in addition to commas as delimiters.
   - Example:
     ```
     "1\n2,3" => 6
     ```
   - Do not allow invalid cases like `"1,\n"`.

4. **Support Custom Delimiters**  
   - A different delimiter can be specified at the beginning of the input string:
     ```
     "//[delimiter]\n[numbers...]"
     ```
   - Example:
     ```
     "//;\n1;2" => 3
     ```
   - All previous test cases should still work.

5. **Handle Negative Numbers**  
   - If a negative number is passed, throw an exception with the message `"negatives not allowed"` followed by the number.
   - If multiple negatives are provided, list all of them in the exception message.

6. **Track Number of Calls**  
   - Implement a method:
     ```csharp
     public int GetCalledCount()
     ```
   - This method returns the number of times `Add` has been called.

7. **(.NET Only) Event on Addition**  
   - Implement an event in `StringCalculator`:
     ```csharp
     public event Action<string, int> AddOccured;
     ```
   - This event should trigger after every call to `Add`.
   - Write a failing test first that listens to the event and validates its behavior.

8. **Ignore Numbers Greater than 1000**  
   - Any number greater than 1000 should be ignored.
   - Example:
     ```
     "2,1001" => 2
     ```

9. **Support Delimiters of Any Length**  
   - Delimiters can be of any length:
     ```
     "//[***]\n1***2***3" => 6
     ```

10. **Support Multiple Delimiters**  
    - Allow multiple custom delimiters:
      ```
      "//[*][%]\n1*2%3" => 6
      ```

11. **Support Multiple Delimiters of Any Length**  
    - Example:
      ```
      "//[**][%%]\n1**2%%3" => 6
      ```

## Additional Information

For more details, visit [osherove.com](https://osherove.com) or contact [roy@osherove.com](mailto:roy@osherove.com).