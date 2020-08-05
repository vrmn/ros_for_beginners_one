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

boundaries = [
    ([17, 15, 100], [50, 56, 200])   # red boundary ([17, 15, 100], [50, 56, 200]) upper and lower limit
                                       # R >= 100, B >=15, G >=17
    #                                    # R <=20 B, <=56, G <= 50
    # ([86, 31, 4], [220, 88, 50]),
    # ([25, 146, 190], [62, 174, 250]),
    # ([13, 86, 65], [145, 133, 128])
]

ap = argparse.ArgumentParser()
ap.add_argument("-w", "--width", type=float, required=False, help="width of the left-most object")
ap.add_argument("-b", "--buffer", type=int, default=32, help="max buffer size")
args = vars(ap.parse_args())


def image_callback(ros_image):
    print 'got an image'
    global bridge, midpoint, boundaries


    #convert ros_image into an opencv image

    frame0 = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    frame1 = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    frame2 = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    frame3 = bridge.imgmsg_to_cv2(ros_image, "bgr8")

    # (h, w, d) = frame1.shape
    # # print(frame1.shape)
    # pts = deque(maxlen=args["buffer"])
    # counter = 0
    # (dX, dY) = (0, 0)
    # direction = ""
    #
    # time.sleep(1/42)
    # cv2.rectangle(frame0,(0,0),(25,25),(0,0,255),2)
    #
    # diff_size = cv2.absdiff(frame0,frame3)
    #
    # diff_coordinates = cv2.absdiff(frame1,frame2)
    #
    # ######## color filtering for red
    # for (lower, upper) in boundaries:
    #
    #     lower = np.array(lower, dtype = "uint8")
    #     upper = np.array(upper, dtype = "uint8")
    #
    #     mask = cv2.inRange(frame1, lower, upper)
    #
    # cv2.imshow("mask", mask)
    #
    # ####### color filtering for red
    #
    # #image processing for coordinates
    # gray = cv2.cvtColor(diff_coordinates, cv2.COLOR_BGR2GRAY)
    # blur = cv2.GaussianBlur(gray, (5,5), 0)
    # _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    # dilated = cv2.dilate(thresh, None, iterations=1)
    #
    # # cv2.imshow("imaged dilated", dilated.copy())
    # # cv2.imshow("frame1 copy", frame1.copy())
    #
    # # image processing for SIZE
    # gray_size = cv2.cvtColor(diff_size, cv2.COLOR_BGR2GRAY)
    # blur_size = cv2.GaussianBlur(gray_size, (5,5), 0)
    # _, thresh_size = cv2.threshold(blur_size, 20, 255, cv2.THRESH_BINARY)
    # dilated_size = cv2.dilate(thresh_size, None, iterations=1)
    #
    # # cv2.imshow("dilated size", dilated_size)
    #
    # edged = cv2.Canny(diff_size, 50, 100)
    # edged = cv2.dilate(edged, None, iterations=1)
    # edged = cv2.erode(edged, None, iterations=1)
    #
    # # cv2.imshow("edged copy", edged.copy())
    #
    # ## shapes
    # gray_shapes = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    # blurred_shapes = cv2.GaussianBlur(gray_shapes, (5,5), 0)
    # thresh_shapes = cv2.threshold(blurred_shapes, 60, 255, cv2.THRESH_BINARY)[1]
    #
    # ## by this point we're ready to find and draw shape contours
    #
    # # first extract controus from the image
    # cnts_shapes = cv2.findContours(thresh_shapes.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cnts_shapes = imutils.grab_contours(cnts_shapes)
    # for c in cnts_shapes:
    #     cv2.drawContours(frame1, [c], -1, (0, 255, 0), 2)
    #
    # # display the total number of shapes on the image
    # text = "I found {} total shapes".format(len(cnts_shapes))
    # cv2.putText(frame1, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
    #
    # # shapes
    #
    #
    # # HERE THERE ARE TWO CONTOUR CAPTURING METHODS. CON FOR THE COORDINATES AND CNTS FOR THE SIZE
    #
    # _, con, _= cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #
    # # this handles the contours for the size. note the contours need to be sorted so that we can use our square as ref
    #
    # # compared edged to dilated_size and dilated_size performs better
    # cnts = cv2.findContours(dilated_size, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cnts = imutils.grab_contours(cnts)
    #
    # (cnts, _) = contours.sort_contours(cnts)
    #
    # # cv2.imshow("image edged,", edged)
    #
    # pixelsPerMetric = None
    #
    # for (i,c) in enumerate(cnts):
    #
    #     if cv2.contourArea(c) < 250:
    #         continue
    #
    #     box = cv2.minAreaRect(c)
    #     box = cv2.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    #
    #     for (x,y) in box:
    #         cv2.circle(frame1, (int(x), int(y)), 2, (0,0,255), -1)
    #
    #     (tl,tr,br,bl) = box
    #     (tltrX, tltrY) = midpoint(tl, tr)
    #     (blbrX, blbrY) = midpoint(bl, br)
    #
    #     (tlblX, tlblY) = midpoint(tl, bl)
    #     (trbrX, trbrY) = midpoint(tr, br)
    #
    #     cv2.circle(frame1, (int(tltrX), int(tltrY)), 1, (255, 0, 0), -1)
    #     cv2.circle(frame1, (int(blbrX), int(blbrY)), 1, (255, 0, 0), -1)
    #     cv2.circle(frame1, (int(tlblX), int(tlblY)), 1, (255, 0, 255), -1)
    #     cv2.circle(frame1, (int(trbrX), int(trbrY)), 1, (255, 0, 255), -1)
    #
    #     dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))  # height in pixels
    #     dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))     # width in pixels
    #
    #
    #     if pixelsPerMetric is None:
    #     #     # pixelsPerMetric = dB / args["width"]
    #         pixelsPerMetric = 0.22   # top right contour is about a quarter inch by a quarter inch # his was found by meaasuing that 106 px were in an inch
    #     #250
    #     dimA = dA / pixelsPerMetric  # pixels divided by the appx pixel size in inches of the first countour
    #     dimB = dB / pixelsPerMetric
    #
    #     appx_area = dA * dB
    #
    #     cv2.putText(frame1, '{:.1f}" px in x'.format(dimB), (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
    #     cv2.putText(frame1, '{:.1f}" px in y'.format(dimA), (int(trbrX - 120), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
    #     cv2.putText(frame1, "{:.1f} pxsq".format(appx_area), (int(trbrX - 140), int(trbrY + 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
    #
    #     # below is for coordinates
    # if len(con) > 0:
    #
    #     c = max(con, key=cv2.contourArea)
    #     ((x,y), radius) = cv2.minEnclosingCircle(c)
    #     M = cv2.moments(c)
    #     center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    #
    #     if radius > 0:
    #
    #         cv2.circle(frame1, center, 1, (0, 0, 255), -1)
    #         pts.appendleft(center)
    #
    # for c in con:
    #     M = cv2.moments(c)
    #
    #     cX = int(M["m10"] / M["m00"])
    #     cY = int(M["m01"] / M["m00"])
    #
    #
    #     ex = (Decimal(cX) - Decimal(frame_x)) / Decimal(frame_x)
    #     why = -1 * (Decimal(cY) - Decimal(frame_y)) / Decimal(frame_y)
    #
    #     (x, y, w, h) = cv2.boundingRect(c)
    #
    #     if cv2.contourArea(c) < 250:
    #         continue
    #     cv2.rectangle(frame1, (x,y), (x+w, y+h),(0, 255, 0), 2 )
    #     cv2.putText(frame1, 'UTEP: {}'.format('DETECTED'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,    1, (0, 69, 255), 3)
    #     cv2.putText(frame1, "dx: {},        dy: {}".format(ex, why),(10, frame1.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX,	1, (0, 255, 0), 3)
    #     cv2.putText(frame1, "dx: {},        dy: {}".format(cX, cY),(10, frame1.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,	1, (0, 255, 0), 3)
    #
    #     for i in np.arange(1, len(pts)):
    #         if pts[i - 1] is None or pts[i] is None:
    #             continue
    #
    #         if counter >= 10 and i == 1 and pts[-10] is not None:
    #             dX = pts[-10][0] - pts[i][0]
    #             dY = pts[-10][1] - pts[i][1]
    #             (dirX, dirY) = ("", "")
    #
    #             if np.abs(dX) > 20:
    #                 dirX = "east" if np.sign(dX) == 1 else "west"
    #
    #             if np.abs(dY) > 20:
    #                 dirY = "Nort" if np.sign(dY) == 1 else "south"
    #
    #             if dirX != "" and dirY != "":
    #                 direction = "{}-{}.format"(dirY, dirX)
    #
    #             else:
    #                 direction = dirX if dirX != "" else dirY
    #         thickness = int(np.sqrt(args["buffer"] / float(i +1)) * 1.5)
    #         cv2.line(frame1, pts[i-1], pts[i], (255, 0, 0), thickness)
    # # out.write(frame1)
    # cv2.imshow('feed', frame1)
    #
    # frame1 = frame2
    # frame0 = frame3
    # frame2 = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    # frame3 = bridge.imgmsg_to_cv2(ros_image, "bgr8")
    #
    # cv2.imshow("image window", frame1)
    # cv2.waitKey(3)
# color filtering

# def read_rgb_image(image_name, show):
#     rgb_image = cv2.imread(image_name)
#     if show:
#         cv2.imshow("RGB Image",rgb_image)
#     return rgb_image
def image_callback(ros_image):

  print 'got an image'
  global bridge
  #convert ros_image into an opencv-compatible image
  try:
    cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
  except CvBridgeError as e:
      print(e)
  #from now on, you can work exactly like with opencv
  (rows,cols,channels) = cv_image.shape
  if cols > 200 and rows > 200 :
      cv2.circle(cv_image, (100,100),90, 255)
  font = cv2.FONT_HERSHEY_SIMPLEX
  # cv2.putText(cv_image,'Webcam Activated with ROS & OpenCV!',(10,350), font, 1,(255,255,255),2,cv2.LINE_AA)
  # cv2.imshow("Image window", cv_image)
  # cv2.waitKey(3)
  # return cv_image

# def filter_color(cv_image, lower_bound_color, upper_bound_color):
    #convert the image into the HSV color space
  hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
  cv2.imshow("hsv image",hsv_image)

    #define a mask using the lower and upper bounds of the yellow color
  redLower =(17, 15, 100)
  redUpper = (50, 56, 200)
  mask = cv2.inRange(hsv_image, redLower, redUpper)

#     return mask
#
#
#
#
# def getContours(binary_image):
  _, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  _, contours, hierarchy = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # return contours
# def get_contour_center(contour):
  for c in contours:

      M = cv2.moments(c)
      cx=-1
      cy=-1
      if (M['m00']!=0):

          cx= int(M['m10']/M['m00'])
          cy= int(M['m01']/M['m00'])
 # return cx, cy


# def draw_ball_contour(binary_image, cv_image, contours):
  black_image = np.zeros([mask.shape[0], mask.shape[1],3],'uint8')

  for c in contours:
     area = cv2.contourArea(c)
     perimeter= cv2.arcLength(c, True)
     ((x, y), radius) = cv2.minEnclosingCircle(c)
     if (area>3000):
         cv2.drawContours(cv_image, [c], -1, (150,250,150), 1)
         cv2.drawContours(black_image, [c], -1, (150,250,150), 1)
         # cx, cy = get_contour_center(c)
         cv2.circle(cv_image, (cx,cy),(int)(radius),(0,0,255),1)
         cv2.circle(black_image, (cx,cy),(int)(radius),(0,0,255),1)
         cv2.circle(black_image, (cx,cy),5,(150,150,255),-1)
            #print ("Area: {}, Perimeter: {}".format(area, perimeter))
    #print ("number of contours: {}".format(len(contours)))
  cv2.imshow("RGB Image Contours",cv_image)
  cv2.imshow("Black Image Contours",black_image)

# def get_contour_center(contour):
    # M = cv2.moments(contour)
    # cx=-1
    # cy=-1
    # if (M['m00']!=0):
    #     cx= int(M['m10']/M['m00'])
    #     cy= int(M['m01']/M['m00'])
    # return cx, cy

# def detect_box_in_a_frame(image_frame):

  redLower =(17, 15, 100)
  redUpper = (50, 56, 200)
  # cv_image = image_frame
  # binary_image_mask = filter_color(cv_image, redLower, redUpper)
  # contours = getContours(binary_image_mask)
  # draw_ball_contour(binary_image_mask, rgb_image,contours)

  cv2.imshow('cv color image',cv_image)
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
