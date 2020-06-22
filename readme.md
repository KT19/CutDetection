# CutDetectionSystem
## This system is based on "Projection Detecting Filter for Video Cut Detection", (1993).

## Requirement
opencv-python

### usage
Please specify path in main.py (video file)

### How to work
When you start this system, the window is automatically generated, and two images will be in it.
The left image of the window means the previous frame and the right image means the current frame.

When the difference of both frames satisfies the threshold (this is also defined in main.py, if you want to change, need modify),
the cut will be detected.
