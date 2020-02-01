# video_maker
This program converts consecutive pictures to one .mp4 video file.
Maybe it can be used for making videos from pictures taken by drone like Tello.

# How to use
## Standard usage
1. Make a directory containing pictures which you want to convert.
1. Set the directory where make_video.py is.
1. Run make_video.py with name of the directory as a command line argument such as,  
`python make_video.py dir_pictures`
1. make_video.py outputs .mp4 video file named same as command line argument.

## Optional usage
On by default, this converter gives a good result for high fps pictures, for example, pictures taken by drone.
If you want to apply low fps pictures such as ones taken by rapid shots by cellphone, you can use an option -p  
`python make_video.py dir_low_fps_pictures -p`  
Then, it produces a video adapting  low fps pictures.
