A plugin is a C++ library that is loaded by Gazebo at runtime. A plugin has access to Gazebo's API, which allows a plugin to perform a wide variety of tasks including moving objects, adding/removing objects, and accessing sensor data.http://gazebosim.org/tutorials?cat=guided_i&tut=guided_i5

http://gazebosim.org/tutorials?cat=write_plugin

Overview of Gazebo Plugins

A plugin is a chunk of code that is compiled as a shared library and inserted into the simulation. The plugin has direct access to all the functionality of Gazebo through the standard C++ classes.

Plugins are useful because they:

    let developers control almost any aspect of Gazebo
    are self-contained routines that are easily shared
    can be inserted and removed from a running system

    You should use a plugin when:

        you want to programmatically alter a simulation

    Ex: move models, respond to events, insert new models given a set of preconditions

        you want a fast interface to gazebo, without the overhead of the transport layer

    Ex: No serialization and deserialization of messages.

        you have some code that could benefit others and want to share it


        Plugin Types

There are currently 6 types of plugins

    World
    Model
    Sensor
    System
    Visual
    GUI

Each plugin type is managed by a different component of Gazebo. For example, a Model plugin is attached to and controls a specific model in Gazebo. Similarly, a World plugin is attached to a world, and a Sensor plugin to a specific sensor. The System plugin is specified on the command line, and loads first during a Gazebo startup. This plugin gives the user control over the startup process.

A plugin type should be chosen based on the desired functionality. Use a World plugin to control world properties, such as the physics engine, ambient lighting, etc. Use a Model plugin to control joints, and state of a model. Use a Sensor plugin to acquire sensor information and control sensor properties.
