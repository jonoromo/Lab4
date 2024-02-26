# Lab4

The purpose of this experiment was to practice operating
multiple devices simultaneously with our microcontroller.
We implemented functions using cotask from the ME405 library.
This allowed us to define multiple tasks and operate them at
different frequencies and priorities. The first step was to
implement one motor/encoder pair as a task and run it using
the scheduler. This first plot shows the step response of 
a motor being run with a default period of 10 ms.

![first plot](https://github.com/jonoromo/Lab4/blob/main/base_case%20per%20%3D%2010.png)

With the motor/encoder and the GUI functioning properly, we
then tested for slower rates at which the motor performance 
would run similarly to our default period. After multiple runs,
we concluded that 20 ms was an acceptable period that produced
near identical results to the 10 ms rate. The plot for the 20 ms
step response is shown below:

![second plot](https://github.com/jonoromo/Lab4/blob/main/slowest_good_performance%20per%20%3D%2020.png)

In order to determine the limits for the rate at which the task
is called, we continued to test the motor task at slower rates.
The following plot shows the step response of the motor with
a rate of 50 ms. This response is not acceptable. It has
significant overshoot and has a slower transient response than
the 20 ms step response.

![third plot](https://github.com/jonoromo/Lab4/blob/main/too_slow%20per%20%3D%2050.png)

After completing these tests, we confirmed that a period of 20 ms
is the optimal speed for motor performance. With this rate determined,
we then created a second task to control another motor simultaneously.
Operation of these two tasks was successful.