In the previous tutorials we recreated the turtle demo by adding a tf2 broadcaster and a tf2 listener. This tutorial will teach you how to add an extra frame to the tf2 tree. This is very similar to creating the tf2 broadcaster, and will show some of the power of tf2.


Why adding frames

For many tasks it is easier to think inside a local frame, e.g. it is easiest to reason about a laser scan in a frame at the center of the laser scanner. tf2 allows you to define a local frame for each sensor, link, etc in your system. And, tf2 will take care of all the extra frame transforms that are introduced.


Where to add frames

tf2 builds up a tree structure of frames; it does not allow a closed loop in the frame structure. This means that a frame only has one single parent, but it can have multiple children. Currently our tf2 tree contains three frames: world, turtle1 and turtle2. The two turtles are children of world. If we want to add a new frame to tf2, one of the three existing frames needs to be the parent frame, and the new frame will become a child frame.



                    ------------[world]-----------
                    |                             |
                    |                             |
                    |                             |
                [/turtle1]                   [/turtle2]


  How to add a frame

In our turtle example, we'll add a new frame to the first turtle. This frame will be the "carrot" for the second turtle.

  Let's first create the source files. Go to the package we created for the previous tutorials:


  go to src file in learning_tf2 and make a node called frame_tf2_broadcaster. you will notice that this code is very similar to turtle_Tf2_broadcaster

in this example a new carrot frame will be added for the second turtle
