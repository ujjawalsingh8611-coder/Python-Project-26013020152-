STUDENT RECORD MANAGEMENT SYSTEM
=================================

PROJECT DESCRIPTION
A  Python terminal application to manage student records.
It can add, view, search, update and delete student information.
Records are saved in students.txt, so they remain available after closing
and reopening the program.

REQUIREMENTS
- Python 3
- Any text editor or Python IDE (such as VS Code or IDLE)
- No external libraries are required.

HOW TO RUN
1. Open the extracted folder in VS Code or a terminal.
2. Run:

   python student_management.py

   On some systems, use:
   python3 student_management.py

3. Choose an option from the menu and follow the prompts.

MENU OPTIONS
1. Add Student       - Save roll number, name, course/branch and marks.
2. View All Students - Display all saved records.
3. Search Student    - Find a student using the roll number.
4. Update Student    - Edit a student's name, course or marks.
5. Delete Student    - Remove a record after confirmation.
6. Exit              - Close the program.


DATA FILE
All records are stored in students.txt in the same folder as the Python file.
Do not delete this file if you want to keep your saved records. You can make
an extra copy of it as a backup.

NOTES
- Each roll number must be unique.
- Marks must be a number between 0 and 100.
- The data file uses the | character as a separator; do not enter this
  character in a student's name or course.
