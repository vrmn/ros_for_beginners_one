what is tf?
1) tf package trnafomration library in ros
2) it perfroms computation for transforms between frames
3) it allows to find the pse of any object in any frame using transformation
4) a robot is a collection of frames attached to its different joints

Urdf is an XML document that describes the robot. also applicable in gazebo .world files

<joint name="base_joint" type="fixed">
    <parent link="base_footprint"/>
    <child link="base_link"/>
    <origin xyz="0.0 0.0 0.010" rpy="0 0 0"/>
</joint>

frames are attached to joints and called link

parent to chld relationship is defined between the different frames or links

the relative postioin between the joints are defined as transformation specified by a translation vector and or roatation matrix
the translation vector is specified by the xyz coordinates of the vector and the roation is defeined by the three angles ropy

any tranfomration between any two frames is defined in the urdf description and later it is used by the navigation stack and the locatlization modules to localize the objects

to learn more about urdf go to http://wiki.ros.org/urdf/Tutorials  http://wiki.ros.org/tf2/Tutorials http://wiki.ros.org/tf2#What_does_tf2_do.3F_Why_should_I_use_tf2.3F http://wiki.ros.org/tf2/Tutorials/Introduction%20to%20tf2

///////////////////// why is tf important ///////////////////////////////

transformation matrix and post transformation are perforemed under the hood by the tf package
In additon the tf package provides programmable api in python and c++ to listen to these tranformations and extract useful information that helps in accomplishing the mission
This is easiluy done because all of the frames and their tranformations are already described in the urdf file
without the tf package the user will have to define these transforamtion matrices manually which is very tedious and complex

///////////////////// why is tf important ///////////////////////////////

/////////////////////////overview of the tf package utilities
The tf package has several nodes that provide utilities to manipulate frams and transformation in ros
1) view_frames: visualizes the full tree of coorinate transforms
2) tf_monitor: monitors transforms between frames
3) tf_echo: prints specified transform to screen
4)roswtf: with the tfwtf plugin, helps you track down problems with tf
5) static_transform_publisher: is a comman line too for sendign static transform
