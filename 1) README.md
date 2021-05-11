# Basic-Traffic-Signal-Violation
Building a basic model for detection of traffic signal violation using raspberry pi.
here our main motive is to print out a graph representing all the times when the violations occured during a day.
so the idea is to take use of ir sensors as the main input signal and when ever a vehicle passes through the red signal, raspberry pi records the time at which the violation occoured and by the end of the day we get a list of the times when the violations occur.
with help of pandas and matplotlib we have plotted a graph for the list representing all the points when ever violation occured.
in the raspberry pi module, we'll use LCD to print 'Vechile detected' whenever violaton occurs!
