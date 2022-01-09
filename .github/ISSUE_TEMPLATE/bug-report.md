---
name: Bug report
about: Create a report to submit encountered bug
title: "[BUG] Issue with XYZ"
labels: bug
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is. Please provide your initial assessment of the Bug. If you don't know what the issue is state `UNKNOWN` as the value here. **BUG REPORTS WITHOUT SUFFICIENT DETAILS OR CHECKLIST COMPLETE WILL BE CLOSED** please help us help you!

**Steps To Reproduce**
If possible please provide a sample single file style reproduction so our team can attempt to reproduce your results. This should look something like this:

```python
import dramatiq
import requests


@dramatiq.actor
def count_words(url):
     response = requests.get(url)
     count = len(response.text.split(" "))
     print(f"There are {count} words at {url!r}.")


# Synchronously count the words on example.com in the current process
count_words("http://example.com")

# or send the actor a message so that it may perform the count
# later, in a separate process.
count_words.send("http://example.com")
```

Steps to reproduce the behavior:
1. `pip install xyz`
2. `dramatiq count_words`
3. Look at stack trace 
4. See `xyz` error in stack trace

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Enviroment (please complete the following information):**
 - OS: [e.g. iOS]
 - Python Version:  [e.g. 3.9.6]
 - `dramatiq-mongodb` Version: [e.g. 1.0.0]

**Additional context**
Add any other context about the problem here.

**Priority**
Is this bug a High Priority to your mission, program, or application? (YES or NO). Please tag with issue priority [e.g. LOW, MEDIUM, HIGH, CRITICAL]

**Checklist**
- [ ] Added a descriptive title/subject to this bug or issue request.
- [ ] I search GitHub issues for this bug and could not find it.
- [ ] I added an example or steps to reproduce