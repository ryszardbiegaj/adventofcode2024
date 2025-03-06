
# Advent of Code - Data Processing Script

## Description

This script processes numerical data from an input file (`input.txt`) as part of an Advent of Code challenge. It reads, extracts, and manipulates the data to compute specific results.

## How It Works

1. Reads `input.txt`, where each line contains two numbers separated by three spaces.
2. Stores the numbers in two separate lists.
3. Sorts both lists.
4. Computes:
   - The **total absolute difference** between corresponding elements.
   - A **weighted sum of occurrences**, counting how often numbers from one list appear in the other.

## Usage

1. Ensure `input.txt` is in the same directory as the script.
2. Run the script:
   ```sh
   python3 1.py
   ```
3. Outputs:
   - **Total Difference**
   - **Weighted Sum of Occurrences**

## Dependencies

- Python 3.x
- `collections` module (built-in)

## Example `input.txt`

```
1   2
3   4
2   3
4   4
```

## Output Example

```
Total Difference: 2
12
```

## Notes

- Designed for Advent of Code-style challenges, focusing on data extraction and transformation.
- The script efficiently handles large datasets by leveraging Python’s built-in tools like `zip()`, `sorted()`, and `Counter`.



