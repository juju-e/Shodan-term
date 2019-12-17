# Shodan-term
To get started with ShodanTerm, first be sure to have already installed the following python
packages:

- Shodan
$ **_pip install shodan_**

This package is used to make the api requests from https://shodan.io

- Termcolor
$ **_pip install termcolor_**

This package is used to make the python terminal colorful.

The text editor I used is **_Vim_**.

These are the steps I followed to make the ShodanTerm program,

**_1._**
The first step I took was to read the official documentation at https://shodan.readthedocs.io and
think of a way to implement the program myself, my first thought was creating a gui but if I made a
gui I could not record an asciinema,and so I implemented a terminal version of the program,

The first few lines of code are the following:
![here](/img/step1.png)

I just import the needed modules then declare some needed variables like the api key and the option
the user wants to choose.
As you can see, for each input or output I use the colored() method from the termcolor module.

Then I first started by implementing the ”what’s my ip” section of the program;
here is the code of this section
![here](/img/step2.png)
On the first line of this section I made a loop that kills the program if the user gives ‘0’ as the
option.
On line 4 I used the subprocess method ‘check_output’ to execute terminal commands from a
python file and checks the output.
The user then reenters an option or kills the program with ‘0’.

**_2._**


Then I implemented the ‘IP scan’ section which was certainly the most difficult part I had yet to
implement, I needed to do more than simply reading the docs, I started to test the api myself by
doing ip scans and carefully reading the output to see which section of the outputted dictionary I
needed, I then started writing the code and doing some tests myself, here it is:
![here](/img/step3.png)
I put the code in a try→except statement because sometimes for one or another case the program
might raise a shodan.APIError exception so I had to catch it before it kills the process.
As you can see I printed the results in a formatted format for readability purposes.

**_3._**
Lastly I implemented the “custom search” section. This one was pretty tricky because it didn’t work
like the “ip scan” one so I had to go back to the official documentation to see what I could find, then
I found out that the query returns a dictionnary in this state:
![here](/img/step4.png)
So it returned a dictionary containing the total number of results and a list containing dictionaries
for each match, the tricky thing was how to find the organization name when it was not in the given
dictionary so I had to figure out a way to overcome it.
Here is the code:
![here](/img/step5.png)
For each result I recuperated the IP address and then ran “ **_host.get('org','n/a_** '” to get the
organization name,

These are the steps that I followed to make this program,

Thanks for your time.


