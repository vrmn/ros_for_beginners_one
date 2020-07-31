/*  Practial steps to write a publisher and subscriber for ros topics refer to the c++ and python versions of listener and talker

PUBLISHER

STEP 1)   Determine a name for the topic to publish
STEP 2)   Dettermine the type of the messages that the topic will publish
STEP 3)   Determine the frequency of topic publication (how many messages per second)
STEP 4)   Create a publisher object with parameters chosen
STEP 5)   Keep publishing the topic message at the selected frequency

*/

/* Practical steps to write a publisher and subscribe for ros topics

SUBSCRIBER

STEP 1)  Identify the name for the topic to listen to
STEP 2)  Identify the type of the messages to be received
STEP 3)  Define a callback function that will be automatically executed when a new message is received on the topic
STEP 4)  Start listening for the topic messages
STEP 5)  Spin to listen forever

For python publisher and subscribers nodes are ready as soon as made executable using
chmod +x node_name.py

For c++ publisher and subscriber nodes additional changes to the CMakeList.txt must take place or else project wont build
