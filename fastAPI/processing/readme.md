findHolds

# detectColor.py:
If run as main, 


# findColours.ipynb

Image process:   
![normal image](./demo/1.png)   
- blur image to lose unimportant details   
![blurred image](./demo/2.png)   
- find contours on canny'd images   
![contours](./demo/3.png)   
- for every contour, store [avgColor, contourMask]    
    - avgColor : within contour
    - contourMask : Image of only the hold coloured in   
![contourMasks summed up](./demo/4.png)   

- use k-mean clustering to find no. different colours of holds   
    -  showColours() can produce an image with all the squares of colours   
![colours detected](./demo/5.png)   
![graph](./demo/graph.png)   

Currently, it picks out some colours. .. just not very good colours   

==================

labelsFiltered -> one label's colour, with rest 0's   
masksFiltered -> use above list to make list only containing active colours' masks   
