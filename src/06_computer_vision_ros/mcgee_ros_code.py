#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys
import time
import imutils
from decimal import *
import numpy as np
import argparse
from imutils import perspective
from scipy.spatial import distance as dist
from imutils import contours
from collections import deque

bridge = CvBridge()

def midpoint(ptA, ptB):
    return ((ptA[0]+ptB[0]) * 0.5, (ptA[1]+ptB[1]) * 0.5)

getcontext().prec = 6

ap = argparse.ArgumentParser()
ap.add_argument("-w", "--width", type=float, required=False, help="width of the left-most object")
ap.add_argument("-b", "--buffer", type=int, default=32, help="max buffer size")
args = vars(ap.parse_args())


def image_callback(ros_image):
    print 'got an image'
    global bridge, midpoint


    #convert ros_image into an opencv image

    frame0 = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    frame1 = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    frame2 = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    frame3 = bridge.imgmsg_to_cv2(ros_image, "bgr8")

    (h, w, d) = frame1.shape
    # print(frame1.shape)
    pts = deque(maxlen=args["buffer"])
    counter = 0
    (dX, dY) = (0, 0)
    direction = ""

    time.sleep(1/42)
    cv2.rectangle(frame0,(0,0),(25,25),(0,0,255),2)

    diff_size = cv2.absdiff(frame0,frame3)

    diff_coordinates = cv2.absdiff(frame1,frame2)

    #image processing for coordinates
    gray = cv2.cvtColor(diff_coordinates, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=1)

    # cv2.imshow("imaged dilated", dilated.copy())
    # cv2.imshow("frame1 copy", frame1.copy())

    # image processing for SIZE
    gray_size = cv2.cvtColor(diff_size, cv2.COLOR_BGR2GRAY)
    blur_size = cv2.GaussianBlur(gray_size, (5,5), 0)
    _, thresh_size = cv2.threshold(blur_size, 20, 255, cv2.THRESH_BINARY)
    dilated_size = cv2.dilate(thresh_size, None, iterations=1)

    # cv2.imshow("dilated size", dilated_size)

    edged = cv2.Canny(diff_size, 50, 100)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)

    # cv2.imshow("edged copy", edged.copy())

    # HERE THERE ARE TWO CONTOUR CAPTURING METHODS. CON FOR THE COORDINATES AND CNTS FOR THE SIZE

    _, con, _= cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # this handles the contours for the size. note the contours need to be sorted so that we can use our square as ref

    # compared edged to dilated_size and dilated_size performs better
    cnts = cv2.findContours(dilated_size, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    (cnts, _) = contours.sort_contours(cnts)

    # cv2.imshow("image edged,", edged)

    pixelsPerMetric = None

    for (i,c) in enumerate(cnts):

        if cv2.contourArea(c) < 250:
            continue

        box = cv2.minAreaRect(c)
        box = cv2.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)

        for (x,y) in box:
            cv2.circle(frame1, (int(x), int(y)), 2, (0,0,255), -1)

        (tl,tr,br,bl) = box
        (tltrX, tltrY) = midpoint(tl, tr)
        (blbrX, blbrY) = midpoint(bl, br)

        (tlblX, tlblY) = midpoint(tl, bl)
        (trbrX, trbrY) = midpoint(tr, br)

        cv2.circle(frame1, (int(tltrX), int(tltrY)), 1, (255, 0, 0), -1)
        cv2.circle(frame1, (int(blbrX), int(blbrY)), 1, (255, 0, 0), -1)
        cv2.circle(frame1, (int(tlblX), int(tlblY)), 1, (255, 0, 255), -1)
        cv2.circle(frame1, (int(trbrX), int(trbrY)), 1, (255, 0, 255), -1)

        dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))  # height in pixels
        dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))     # width in pixels


        if pixelsPerMetric is None:
        #     # pixelsPerMetric = dB / args["width"]
            pixelsPerMetric = 0.22   # top right contour is about a quarter inch by a quarter inch # his was found by meaasuing that 106 px were in an inch
        #250
        dimA = dA / pixelsPerMetric  # pixels divided by the appx pixel size in inches of the first countour
        dimB = dB / pixelsPerMetric

        appx_area = dA * dB

        cv2.putText(frame1, '{:.1f}" px in x'.format(dimB), (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
        cv2.putText(frame1, '{:.1f}" px in y'.format(dimA), (int(trbrX - 120), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
        cv2.putText(frame1, "{:.1f} pxsq".format(appx_area), (int(trbrX - 140), int(trbrY + 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

        # below is for coordinates
    if len(con) > 0:

        c = max(con, key=cv2.contourArea)
        ((x,y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 0:

            cv2.circle(frame1, center, 1, (0, 0, 255), -1)
            pts.appendleft(center)

    for c in con:
        M = cv2.moments(c)

        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])


        ex = (Decimal(cX) - Decimal(frame_x)) / Decimal(frame_x)
        why = -1 * (Decimal(cY) - Decimal(frame_y)) / Decimal(frame_y)

        (x, y, w, h) = cv2.boundingRect(c)

        if cv2.contourArea(c) < 250:
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h),(0, 255, 0), 2 )
        cv2.putText(frame1, 'UTEP: {}'.format('DETECTED'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,    1, (0, 69, 255), 3)
        cv2.putText(frame1, "dx: {},        dy: {}".format(ex, why),(10, frame1.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX,	1, (0, 255, 0), 3)
        cv2.putText(frame1, "dx: {},        dy: {}".format(cX, cY),(10, frame1.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,	1, (0, 255, 0), 3)

        for i in np.arange(1, len(pts)):
            if pts[i - 1] is None or pts[i] is None:
                continue

            if counter >= 10 and i == 1 and pts[-10] is not None:
                dX = pts[-10][0] - pts[i][0]
                dY = pts[-10][1] - pts[i][1]
                (dirX, dirY) = ("", "")

                if np.abs(dX) > 20:
                    dirX = "east" if np.sign(dX) == 1 else "west"

                if np.abs(dY) > 20:
                    dirY = "Nort" if np.sign(dY) == 1 else "south"

                if dirX != "" and dirY != "":
                    direction = "{}-{}.format"(dirY, dirX)

                else:
                    direction = dirX if dirX != "" else dirY
            thickness = int(np.sqrt(args["buffer"] / float(i +1)) * 1.5)
            cv2.line(frame1, pts[i-1], pts[i], (255, 0, 0), thickness)
    # out.write(frame1)
    cv2.imshow('feed', frame1)

    frame1 = frame2
    frame0 = frame3
    frame2 = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    frame3 = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    #
    # cv2.imshow("image window", frame1)
    cv2.waitKey(3)



def main(args):

    #initialize ros subscriber node
    rospy.init_node('image_converter', anonymous=True)

    image_sub = rospy.Subscriber("/webcam/image_raw", Image, image_callback)


    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting Down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
