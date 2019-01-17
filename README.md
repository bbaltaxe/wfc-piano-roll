# playerpiano

Play images like a piano roll!

Uses ikarth's implementation of [mxgmn/WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse) in Python (https://github.com/ikarth/wfc_python)

Shoutout to this chord playing directory for helpming me figure out how to add sine waves together https://github.com/akkana/scripts/blob/master/play_chord.py

## Getting started 

The best way to get started is to clone this directory to your machine and dive in! 
The required packages for this project can be found in requirements.txt and installed to your environment using: 
```pip install -r requirements.txt```

## Generate images

To generate an image from WaveFunctionCollapse, you will need an sample image to generate from. 
You can choose an existing image from wfc/Samples/ or add your own .png there. 

Note of caution - images of > 100 pixels will take a looooong time to generate from, so choose something simple.

Here's an example.
To generate images based on the Water sample run the following: 
``` python wfc/wfc_main.py -f Water ```

From one image you will get 5 unique images: 

<img src="https://raw.githubusercontent.com/bbaltaxe/player_piano/master/wfc/samples/Water.png" alt="example image" height="75"/> ---------->
<img src="https://raw.githubusercontent.com/bbaltaxe/player_piano/master/example.png" alt="example image" height="75"/>

If you would like more output images, to change the output dimensions, etc:
```optional arguments:
  -h, --help   show this help message and exit
  -f NAME      source file name (located in samples/) to generate from. Do not
               include file type.
  -i [N]       number of images to create. defaults to 5
  -l [LENGTH]  length in pixels of images to create. defaults to 48
  -t [HEIGHT]  height in pixels of images to create. defaults to 13
  
  ```

## Play your image

Note - For now, if you would like to use the chromatic or major scale options, the max height of your image is 24 pix.
Note - The default background is Black. If your image's background is not black, you will need to change the background global variable in soundify.py
