# CodeClause_Internship
# Alarm Clock with GUI

This project is an alarm clock application built using Python and the tkinter library for creating a graphical user interface (GUI). It allows users to set an alarm by entering the desired time in the format HH:MM. Once the alarm is set, the program calculates the time difference between the current time and the alarm time.

If the alarm time is in the past, it adds one day to the alarm datetime to ensure it triggers the next day. The program then sleeps for the calculated time difference in seconds, effectively pausing the execution until the alarm time is reached.

When the alarm time is reached, it plays an alarm sound using the playsound library and displays a message box with the text "Wake up!".

The application provides error handling for invalid input, displaying an error message if the entered time is not in the correct format.

This project can be uploaded to GitHub as an open-source repository to share with others who are interested in building a simple alarm clock application using Python and tkinter.
