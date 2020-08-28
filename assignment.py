#!/usr/bin/python
# Standard Modules
import csv
import math, operator
import time
import argparse
import sys
from PIL import Image
from PIL import ImageChops
from functools import reduce
from io import BytesIO

class imageComparison():
    def __init__(self):
        self.currenttime = time.process_time()

    def readCsvfile(self,inputfile):
        """
         Function to read the CSV file provided by the user
        """
        with open(inputfile, 'r') as csvfile:
            image_list = []
            csvreader = csv.reader(csvfile, delimiter=',')
            for row in csvreader:
                image_list.append(row[0])
                image_list.append(row[1])
            self.compareImages(image_list)


    def compareImages(self,image_list):
        """
        Function comparing the images
        :param image_list:
        :return:
        """
        for i in range(0,len(image_list),2):
            image_one = Image.open(image_list[i])
            image_two = Image.open(image_list[i+1])
            if (image_one.format != image_two.format):
                image_one,image_two = self.convertImageformat(image_one, image_two)
            image_one = image_one.resize((600, 600))
            image_two = image_two.resize((600, 600))
            diff = ImageChops.difference(image_one, image_two)
            if (diff.getbbox()) and ( float(self.calculateDiff(diff,image_one,image_two)) > 1.0 ):
                self.writer.writerow([image_list[i], image_list[i+1],self.calculateDiff(diff,image_one,image_two),self.timeElapsed()])
            else:
                self.writer.writerow([image_list[i], image_list[i + 1],"0",self.timeElapsed()])
        self.csvwritefile.close()

    def calculateDiff(self,diff,image_one,image_two):
        """
        Function comparing how much the image differ. The difference
        is measured in terms of Root Mean Square
        :param diff:
        :param image_one:
        :param image_two:
        :return:
        """
        h = diff.histogram()
        return str((math.sqrt(reduce(operator.add, map(lambda h, i: h * (i ** 2), h, range(256))) / (
            float(image_one.size[0]) * image_two.size[1]))))

    def timeElapsed(self):
        """
        Function calculating the time elasped
        :return:
        """
        stop = time.process_time()
        time_diff = stop - self.currenttime
        return str(time_diff)

    def createCSVfile(self,outputfile):
        """
        CSV file is created, the name of the output file
        is provided by the user as an argument.
        :param outputfile:
        :return:
        """
        self.csvwritefile = open(outputfile, 'w')
        self.writer = csv.writer(self.csvwritefile)
        self.writer.writerow(["image1", "image2", "similar", "elapsed"])

    def convertImageformat(self,image_one,image_two):
        """
        This function convert both the files to jpg format in case both
        the image files are in a different format.
        :param image_one:
        :param image_two:
        :return:
        """
        image_name_one = (image_one.filename).split('.')[0] + ".jpg"
        image_name_two = (image_two.filename).split('.')[0] + ".jpg"
        image_one = image_one.convert('RGB').save(image_name_one)
        image_two = image_two.convert('RGB').save(image_name_two)
        image_one = Image.open(image_name_one)
        image_two = Image.open(image_name_two)
        return image_one, image_two

    def build_parser(self):
        """
        Command line arguments:87
        :return:
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('-i   ', action='store' ,dest='inputfile', help='Input CSV file'
                            , type=str, default="")
        parser.add_argument('-o   ', action='store', dest='outputfile', help='Output CSV file'
                            , type=str, default="")
        return parser

    def main(self):
        parser = self.build_parser()
        res = parser.parse_args()
        try:
            assert (len(sys.argv) >= 4), "use -h for usage information"
            if ((res.inputfile) and (res.outputfile)):
                self.createCSVfile(res.outputfile)
                self.readCsvfile(res.inputfile)
        except AssertionError as msg:
            print (msg)

if __name__ == '__main__':
    compare_object=imageComparison()
    compare_object.main()