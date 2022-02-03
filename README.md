# virtual-mouse-using-Hand
This project proposes a  camera vision based cursor control system, using hand moment captured from a webcam through a landmarks of hand  by using Mideapipe module

# Work FLow or Algorithms

1. Find hand land marks
2. Get the tip of the index and middle fingure
3. check which fingers are up
4. only Index Finger : Moving Mode
5. convert Coordinates
6. smoothen Values
7. Move House
8. Both Index and Middle finger are up: Clicking Mode
9. find the distance Between finger
10. Click mouse if Distance
11. Frame Rate
12. display

# How to Run?

1. Copy this project to your local system 
2. Create New Virtual Environment by using `python -m venv env` in your `cmd` Note: Commend Line Will be same folder.
3. Activate that Environment by using `env\Scripts\activate`
4. Now Run our python code `python main.py`.

# Needed packages
1. absl-py==1.0.0
2. attrs==21.4.0
3. autopy==4.0.0
4. cycler==0.11.0
5. fonttools==4.29.1
6. kiwisolver==1.3.2
7. matplotlib==3.5.1
8. mediapipe==0.8.9.1
9. numpy==1.21.5
10. opencv-contrib-python==4.5.5.62
11. packaging==21.3
12. Pillow==9.0.0
13. protobuf==3.19.4
14. pyparsing==3.0.7
15. python-dateutil==2.8.2
16. six==1.16.0


# Thank You
