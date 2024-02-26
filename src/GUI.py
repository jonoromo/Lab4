"""!
@file GUI.py

This file is adapted to the Nerf blaster turret term project, from a template file
provided for the ME 405 class.

The file is based loosely on an example found at
https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html

@author Spluttflob
@author Brendan Stratford
@author Jonathan Romeo
@author Johnathan Waldmire
@date   2023-12-24 Original program, based on example from above listed source
@copyright (c) 2023 by Spluttflob and released under the GNU Public Licenes V3
"""

import math
import time
import tkinter
from random import random
from serial import Serial
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)


def plot_example(plot_axes, plot_canvas, xlabel, ylabel):
    """!
    This function is responsible for writing a Ctrl-D to the nucleo to run the
    main code containing the step response. Then the data is read through serial
    and plotted to a defined set of axes.
    @param plot_axes The plot axes supplied by Matplotlib
    @param plot_canvas The plot canvas, also supplied by Matplotlib
    @param xlabel The label for the plot's horizontal axis
    @param ylabel The label for the plot's vertical axis
    """
    # Here we create some fake data. It is put into an X-axis list (times) and
    # a Y-axis list (boing). Real test data will be read through the USB-serial
    # port and processed to make two lists like these
    
    # Create serial port
    ser = Serial("COM3", 115200) # COM5 for brendan's laptop, COM3 for johnathan
    ser.write(b'\x04')
    time.sleep(.5)
    
#     kp = "0.1\n"
#     ser.write(kp.encode())
    
    data = []
    x = []
    y = []
    time.sleep(2.5)
    for i in range(120):
        n = ser.readline().decode("utf-8")
        data.append(n)
    
    for line in data:
        try:
            txt = str(line)                          # converts each line to a string
            strings = txt.split(',')                 # separates the two data points
            x_val = float(strings[0])                # converts first data point to a float
            y_val = float(strings[1])                # converts second data point to a float
            x.append(x_val)                          # adds the first data value to the x list
            y.append(y_val)                          # adds the second data value to the y list
        except:
            continue
    


    # Draw the plot. Of course, the axes must be labeled. A grid is optional
    plot_axes.plot(x, y,'bo')
    plot_axes.set_xlabel(xlabel)
    plot_axes.set_ylabel(ylabel)
    plot_axes.grid(True)
    plot_canvas.draw()


def tk_matplot(plot_function, xlabel, ylabel, title):
    """!
    Create a TK window with one embedded Matplotlib plot.
    This function makes the window, displays it, and runs the user interface
    until the user closes the window. The plot function, which must have been
    supplied by the user, should draw the plot on the supplied plot axes and
    call the draw() function belonging to the plot canvas to show the plot. 
    @param plot_function The function which, when run, creates a plot
    @param xlabel The label for the plot's horizontal axis
    @param ylabel The label for the plot's vertical axis
    @param title A title for the plot; it shows up in window title bar
    """
    
    
    # Create the main program window and give it a title
    tk_root = tkinter.Tk()
    tk_root.wm_title(title)

    # Create a Matplotlib 
    fig = Figure()
    axes = fig.add_subplot()

    # Create the drawing canvas and a handy plot navigation toolbar
    canvas = FigureCanvasTkAgg(fig, master=tk_root)
    toolbar = NavigationToolbar2Tk(canvas, tk_root, pack_toolbar=False)
    toolbar.update()

    # Create the buttons that run tests, clear the screen, and exit the program
    button_quit = tkinter.Button(master=tk_root,
                                 text="Quit",
                                 command=tk_root.destroy)
    button_clear = tkinter.Button(master=tk_root,
                                  text="Clear",
                                  command=lambda: axes.clear() or canvas.draw())
    button_run = tkinter.Button(master=tk_root,
                                text="Run Test",
                                command=lambda: plot_function(axes, canvas,
                                                              xlabel, ylabel))

    # Arrange things in a grid because "pack" is weird
    canvas.get_tk_widget().grid(row=0, column=0, columnspan=3)
    toolbar.grid(row=1, column=0, columnspan=3)
    button_run.grid(row=2, column=0)
    button_clear.grid(row=2, column=1)
    button_quit.grid(row=2, column=2)

    # This function runs the program until the user decides to quit
    tkinter.mainloop()


# This main code is run if this file is the main program but won't run if this
# file is imported as a module by some other main program
if __name__ == "__main__":
    tk_matplot(plot_example,
               xlabel="Time [ms]",
               ylabel="Encoder Position [ticks]",
               title="PinB0 Time Response")

