# playerpiano

Play images like a piano roll!

Uses ikarth's implementation of [mxgmn/WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse) in Python (https://github.com/ikarth/wfc_python)

Shoutout to this chord playing directory for helpming me figure out how to add sine waves together https://github.com/akkana/scripts/blob/master/play_chord.py

# Getting started 

The best way to get started is to clone this directory to your machine and dive in! 
The required packages for this project can be found in requirements.txt and installed to your environment using: 
```pip install -r requirements.txt```

# Generate a images

To generate an image from WaveFunctionCollapse, you will need an sample image to generate from. 
You can choose an existing image from wfc/Samples/ or add your own .png there. 

Note of caution - images of > 100 pixels will take a looooong time to generate from, so choose something simple.

Here's an example.
To generate images based on the Water sample run the following: 
``` python wfc/wfc_main.py -f Water ```

From one image you will get 5 unique images: 

<img src="https://raw.githubusercontent.com/bbaltaxe/player_piano/master/wfc/samples/Water.png" alt="example image" height="50"/>
---------->
<img src="https://raw.githubusercontent.com/bbaltaxe/player_piano/master/example.png" alt="example image" height="50"/>

# Play your image

Note - The default background is Black. If your image's background is not black, you will need to change the background global variable in soundify.py
