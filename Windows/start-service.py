import os

print("Make sure that the RPi code is running")
os.system("gst-launch-1.0 -v tcpclientsrc host=<your_Pi's_IP> port=5000 ! gdpdepay ! rtph264depay ! avdec_h264 ! videoconvert  ! autovideosink sync=false")