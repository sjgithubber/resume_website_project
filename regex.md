# Complete Regular Expressions Reference Guide

## Table of Contents
1. [Basic Regex Identifiers](#basic-regex-identifiers)
2. [Quantifiers](#quantifiers)
3. [Most Common Regex Patterns](#most-common-regex-patterns)
4. [Using Regex in Python](#using-regex-in-python)
5. [Using Regex in Bash](#using-regex-in-bash)
6. [Exercises](#exercises)
7. [Exercise Answers](#exercise-answers)

---

## Basic Regex Identifiers

### Character Classes
| Pattern | Description | Example |
|---------|-------------|---------|
| `.` | Any character except newline | `a.c` matches `abc`, `axc` |
| `\d` | Any digit (0-9) | `\d+` matches `123` |
| `\D` | Any non-digit | `\D+` matches `abc` |
| `\w` | Word character (a-z, A-Z, 0-9, _) | `\w+` matches `hello_123` |
| `\W` | Non-word character | `\W+` matches `@#$` |
| `\s` | Whitespace (space, tab, newline) | `\s+` matches spaces |
| `\S` | Non-whitespace | `\S+` matches `hello` |
| `[abc]` | Any character in brackets | `[aeiou]` matches vowels |
| `[^abc]` | Any character NOT in brackets | `[^0-9]` matches non-digits |
| `[a-z]` | Character range | `[a-zA-Z]` matches letters |

### Anchors
| Pattern | Description | Example |
|---------|-------------|---------|
| `^` | Start of string/line | `^hello` matches line starting with "hello" |
| `$` | End of string/line | `world$` matches line ending with "world" |
| `\b` | Word boundary | `\bcat\b` matches "cat" but not "catch" |
| `\B` | Non-word boundary | `\Bcat\B` matches "cat" in "concatenate" |

### Special Characters
| Pattern | Description | Example |
|---------|-------------|---------|
| `\` | Escape character | `\.` matches literal dot |
| `\|` | OR operator | `cat\|dog` matches "cat" or "dog" |
| `()` | Grouping | `(ab)+` matches "ab", "abab", etc. |
| `(?:)` | Non-capturing group | `(?:ab)+` groups without capturing |

---

## Quantifiers

| Quantifier | Description | Example |
|------------|-------------|---------|
| `*` | Zero or more | `a*` matches "", "a", "aa", "aaa" |
| `+` | One or more | `a+` matches "a", "aa", "aaa" |
| `?` | Zero or one (optional) | `colou?r` matches "color" or "colour" |
| `{n}` | Exactly n times | `\d{3}` matches exactly 3 digits |
| `{n,}` | n or more times | `\d{3,}` matches 3 or more digits |
| `{n,m}` | Between n and m times | `\d{3,5}` matches 3-5 digits |

### Greedy vs Non-Greedy
| Type | Pattern | Description |
|------|---------|-------------|
| Greedy | `.*` | Matches as much as possible |
| Non-greedy | `.*?` | Matches as little as possible |
| Example | `<.*>` vs `<.*?>` | In `<b>bold</b>`: greedy matches whole string, non-greedy matches `<b>` |

---

## Most Common Regex Patterns

### Email Validation
```regex
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```

### Phone Numbers
```regex
^\+?[\d\s\-\(\)]{10,}$
# US Format: ^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$
```

### URLs
```regex
^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$
```

### IP Address
```regex
^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$
```

### Date Formats
```regex
# MM/DD/YYYY
^(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])\/\d{4}$

# YYYY-MM-DD
^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$
```

### Password Strength
```regex
# At least 8 chars, 1 uppercase, 1 lowercase, 1 digit, 1 special char
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$
```

### Credit Card Numbers
```regex
# Visa: ^4[0-9]{12}(?:[0-9]{3})?$
# MasterCard: ^5[1-5][0-9]{14}$
# American Express: ^3[47][0-9]{13}$
```

### HTML Tags
```regex
<\/?[a-zA-Z][^>]*>
```

### Extract Numbers
```regex
-?\d+\.?\d*
```

---

## Using Regex in Python

### Import and Basic Usage
```python
import re

# Search for pattern
text = "Hello World 123"
match = re.search(r'\d+', text)
if match:
    print(match.group())  # Output: 123

# Find all matches
matches = re.findall(r'\d+', text)
print(matches)  # Output: ['123']
```

### Common Python Regex Functions
```python
import re

text = "Contact: john@example.com or call 555-1234"

# re.search() - Find first match
match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
if match:
    print(f"Email found: {match.group()}")

# re.findall() - Find all matches
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(f"All emails: {emails}")

# re.sub() - Replace matches
cleaned = re.sub(r'\d{3}-\d{4}', '[PHONE]', text)
print(cleaned)

# re.split() - Split by pattern
parts = re.split(r'[,\s]+', "apple, banana orange grape")
print(parts)

# re.match() - Match from beginning
match = re.match(r'Contact', text)
print(match.group() if match else "No match")

# Compiled patterns (for repeated use)
pattern = re.compile(r'\b\w+@\w+\.\w+\b')
matches = pattern.findall(text)
```

### Advanced Python Examples
```python
import re

# Using groups
text = "Born on 1990-05-15"
match = re.search(r'(\d{4})-(\d{2})-(\d{2})', text)
if match:
    year, month, day = match.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")

# Named groups
match = re.search(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', text)
if match:
    print(f"Year: {match.group('year')}")

# Flags
text = "Hello WORLD"
matches = re.findall(r'hello', text, re.IGNORECASE)
print(matches)  # ['Hello']

# Multi-line and verbose
pattern = re.compile(r'''
    (\d{3})     # Area code
    [-.]        # Separator
    (\d{3})     # First 3 digits
    [-.]        # Separator
    (\d{4})     # Last 4 digits
''', re.VERBOSE)
```

---

## Using Regex in Bash

### Using grep
```bash
# Basic search
grep "pattern" file.txt

# Case insensitive
grep -i "hello" file.txt

# Extended regex
grep -E "pattern1|pattern2" file.txt

# Show line numbers
grep -n "pattern" file.txt

# Invert match (lines NOT containing pattern)
grep -v "pattern" file.txt

# Count matches
grep -c "pattern" file.txt

# Recursive search
grep -r "pattern" /path/to/directory/
```

### Common grep Examples
```bash
# Find email addresses
grep -E "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b" file.txt

# Find IP addresses
grep -E "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" file.txt

# Find phone numbers
grep -E "\b[0-9]{3}-[0-9]{3}-[0-9]{4}\b" file.txt

# Find lines starting with specific word
grep "^Error" logfile.txt

# Find lines ending with specific word
grep "success$" logfile.txt

# Find empty lines
grep "^$" file.txt

# Find lines with only whitespace
grep "^\s*$" file.txt
```

### Using sed for Find and Replace
```bash
# Basic substitution
sed 's/old/new/' file.txt

# Global substitution (all occurrences in line)
sed 's/old/new/g' file.txt

# Case insensitive substitution
sed 's/old/new/gi' file.txt

# In-place editing
sed -i 's/old/new/g' file.txt

# Delete lines matching pattern
sed '/pattern/d' file.txt

# Print only matching lines
sed -n '/pattern/p' file.txt
```

### Using awk with Regex
```bash
# Print lines matching pattern
awk '/pattern/ {print}' file.txt

# Print specific field if line matches
awk '/pattern/ {print $1}' file.txt

# Case insensitive match
awk 'tolower($0) ~ /pattern/ {print}' file.txt

# Count matches
awk '/pattern/ {count++} END {print count}' file.txt
```

### Bash Parameter Expansion with Patterns
```bash
#!/bin/bash
text="hello-world-123"

# Remove shortest match from beginning
echo ${text#*-}        # world-123

# Remove longest match from beginning  
echo ${text##*-}       # 123

# Remove shortest match from end
echo ${text%-*}        # hello-world

# Remove longest match from end
echo ${text%%-*}       # hello

# Replace first occurrence
echo ${text/-/_}       # hello_world-123

# Replace all occurrences
echo ${text//-/_}      # hello_world_123
```

---

## Exercises

### Exercise 1: Basic Pattern Matching
Write regex patterns to match:
1. Any 3-digit number
2. Words that start with 'a' and end with 'e'
3. Lines that contain either 'cat' or 'dog'
4. Email addresses (simple version)

### Exercise 2: Quantifiers
Create patterns for:
1. Phone numbers in format XXX-XXX-XXXX
2. Words with 5 to 10 characters
3. HTML tags (opening and closing)
4. Repeated characters (like 'aaaa' or 'bbbb')

### Exercise 3: Advanced Patterns
Design regex for:
1. Validate strong passwords (8+ chars, uppercase, lowercase, digit, special char)
2. Extract all URLs from text
3. Match dates in MM/DD/YYYY format
4. Find all hexadecimal color codes (#RRGGBB)

### Exercise 4: Python Implementation
Write Python code to:
1. Extract all email addresses from a text file
2. Replace all phone numbers with '[REDACTED]'
3. Split a string by multiple delimiters (comma, semicolon, space)
4. Validate user input against a pattern

### Exercise 5: Bash Usage
Write bash commands to:
1. Find all .log files containing 'ERROR'
2. Count lines in a file that start with a number
3. Replace all tabs with 4 spaces in a file
4. Extract IP addresses from a log file

---

## Exercise Answers

### Exercise 1 Answers
1. `\d{3}` or `[0-9]{3}`
2. `\ba\w*e\b` or `^a.*e$`
3. `cat|dog`
4. `\w+@\w+\.\w+`

### Exercise 2 Answers
1. `\d{3}-\d{3}-\d{4}`
2. `\b\w{5,10}\b`
3. `</?[a-zA-Z][^>]*>`
4. `(.)\1{3,}` (same character repeated 4+ times)

### Exercise 3 Answers
1. `^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$`
2. `https?://[^\s]+`
3. `^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$`
4. `#[0-9A-Fa-f]{6}`

### Exercise 4 Answers
```python
# 1. Extract emails from file
import re
with open('file.txt', 'r') as f:
    content = f.read()
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', content)
    print(emails)

# 2. Replace phone numbers
text = "Call me at 555-123-4567"
redacted = re.sub(r'\d{3}-\d{3}-\d{4}', '[REDACTED]', text)

# 3. Split by multiple delimiters
text = "apple,banana;orange grape"
parts = re.split(r'[,;\s]+', text)

# 4. Validate input
def validate_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return bool(re.match(pattern, email))
```

### Exercise 5 Answers
```bash
# 1. Find .log files with ERROR
find . -name "*.log" -exec grep -l "ERROR" {} \;

# 2. Count lines starting with number
grep -c "^[0-9]" file.txt

# 3. Replace tabs with 4 spaces
sed -i 's/\t/    /g' file.txt

# 4. Extract IP addresses
grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" logfile.txt
```

---

## Tips and Best Practices

1. **Use raw strings in Python**: `r"pattern"` to avoid escaping issues
2. **Test your regex**: Use online tools like regex101.com
3. **Be specific**: Avoid overly broad patterns like `.*`
4. **Use non-capturing groups**: `(?:...)` when you don't need to capture
5. **Consider performance**: Complex patterns can be slow on large texts
6. **Escape special characters**: Remember to escape `.` `*` `+` `?` etc. when matching literally
7. **Use anchors**: `^` and `$` to match entire strings
8. **Comment complex patterns**: Use `re.VERBOSE` flag in Python

---

*This guide covers the most essential regex concepts. Practice with real examples to master regular expressions!*
