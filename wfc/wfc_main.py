import model 
import random
import xml.etree.ElementTree as ET
import uuid

iterations = 5
name = "Bone"
length = 48
width = 13
n = 5 #size of tiles to generate from

def generate(model):
    for i in range(iterations):
        print("Iteration {0} of {1}".format(i,iterations))
        finished = model.Run(random.random(),0)
        if finished: 
            print("Done")
            model.Graphics().save("{0}_{1}_{2}.png".format(name, i, uuid.uuid4()), format="PNG")
#            break
        else: 
            print("Contradiction")

if __name__ == "__main__":
    
    print("Creating Model...")
    a_model = model.OverlappingModel(length, width, name, n, True, True, 2,0)
    print("Generating Outputs...")
    generate(a_model)
