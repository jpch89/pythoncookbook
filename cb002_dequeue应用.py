from collections import deque


def search(lines, pattern, history=3):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, previous_lines in search(f, 'python', 2):
            for pline in previous_lines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

"""
I'm not going to tell you this word yet.
Because I have to make up all these sentences.
Ok, the word is python.
--------------------
Now you have the word.
The mission of this file is finished.
Yeah, the word is python.
--------------------
"""
