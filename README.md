# SIH_project
Designed a device which can detect whether an elder person is within  the specified boundary and will alarm if he/she crosses the boundary. 
The device also detects fire and face .

    • LIBRARIES:- 
    1. Rpi.gpio 
    2. Time
    3. gps
    4. OpenCV
    5. keras 
    6. Matplotlib 
    7. numpy
    8. Opencv 
    
    • TOOLS:-
    1. Raspberry pi 3B+
    2. Ultrasonic Sensor SR-04 
    3. Gps module NEO-6M
    4. Buzzer 
    
The “You Only Look Once,” or YOLO, family of models are a series of end-to-end deep learning models designed for fast object detection, developed by Joseph Redmon, et al. 
and first described in the 2015 paper titled “You Only Look Once: Unified, Real-Time Object Detection.
model uses trained weights from MSCOCO dataset.

The entire implementation is done for explanatory purpose.
The face reconginition and fire detection code are separate both of these are not currently integrated with actual module.
Only Object detection is working. 
The actual code uses YOLOv3 from OpenCV and detects the object as threat or not for that person.
Any Object are detected using SR04 ultrasonic sensor.
The location of the coordinates were obtained by GPS NEO-6M using Haversine formula. If the person crosses the boundary, a buzzer will buzz .
