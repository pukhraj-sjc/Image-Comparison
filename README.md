# Image-Comparison

This program compares two images, and gives the user an output
stating whether the images compared are both same or not.

Input is provided in the form of a CSV file.
The format of a CSV file is shown below.

```
image1 image2
aa.png ba.png 
ab.png bb.png 
ac.png ac.gif 
ad.png bd.png
```

The output file should also be in a CSV format. 

Example:-
```
image1 image2 similar elapsed
aa.png ba.png 0       0.006
ab.png bb.png 0.23    0.843
ac.png ac.gif 0       1.43
```

The third column states how much the images are different from
each other. To calculate the difference we will be calculating
ROOT MEAN SQUARE diff.

The fourth column elapsed states the time the program has taken to
compare all the images present in each row of the CSV file.

### Usage
This program used python Pillow library for image comparisons.
Run the below command to install the library.
```
pip install Pillow
```
One need to provide input file as an argument, and also the name of the output file
should be passed as an argument.

To see the options:-
Run the below command on your terminal.
```
[localhost]$ python assignment.py -h
usage: assignment.py [-h] [-i    INPUTFILE] [-o    OUTPUTFILE]

optional arguments:
  -h, --help        show this help message and exit
  -i    INPUTFILE   Input CSV file
  -o    OUTPUTFILE  Output CSV file
```
Complete command to run the script:-
```
[localhost]$ python assignment.py -i inputfile.csv -o outputfile.csv
```




