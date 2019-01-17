import model 
import random
import xml.etree.ElementTree as ET
import uuid
import argparse

#iterations = 5
#name = "Water"
#length = 48
#width = 13
#n = 5 #size of tiles to generate from

def generate(model):
    for i in range(iterations):
        print("Iteration {0} of {1}".format(i,iterations))
        finished = model.Run(random.random(),0)
        if finished: 
            print("Done")
            model.Graphics().save("{0}_{1}_{2}.png".format(name, i, uuid.uuid4()), format="PNG")
        else: 
            print("Contradiction")

if __name__ == "__main__":
    #commandline handling
    parser = argparse.ArgumentParser(description='Performs wfc on an image to generate a specified number of images')
    parser.add_argument('-f', dest='name', type=str,required=True,
                   help='source file name (located in samples/) to generate from. Do not include file type.')
    parser.add_argument('-i', dest='n', type=int, nargs='?',default='5',
                    help='number of images to create. defaults to 5')
    parser.add_argument('-l', dest='length', type=int, nargs='?',default='48',
                    help='length in pixels of images to create. defaults to 48')
    parser.add_argument('-t', dest='height', type=int, nargs='?',default='48',
                    help='height in pixels of images to create. defaults to 13')

    
    args = parser.parse_args()
    
    
    print("Creating Model...")
    a_model = model.OverlappingModel(args.length, args.height, args.name, args.n, True, True, 2,0)
    print("Generating Outputs...")
    generate(a_model)
