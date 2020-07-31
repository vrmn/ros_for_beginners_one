Ros services

instead of publishers and subscribers here what we have are
server and client

this is for one time communication

instead of topic what we have is a service

a client sends a request for a service
server sends back a response which is the service

you want to use ros service
when you request a robot to perform a specific action
For example find the path from point A to point B, spawn one robot in the simulator

to see list of all services available type in a terminal (rosservice list)

use (rosservice info <name of service>) to see what node provides the service
you'll also get the port number (URT)
The type of message
args that need to be provided.

you can find the structure of the message by typing in a terminal
rossrv info node_name/service_name

fthe structre of the ros service message is divided into two parts
( this is the service definition in your .srv file that you create)

the top - contains the arguments found in the service message
        - these are the arguments that the client should send in a request
---
the bottom - this represents the response of the server ie what the server is going to return


example
float32 x
float 32 y
float theta
string name
---
string name

to use this service type into the terminal
rosservice call </name of service> <its arguments  x  y  theta name>

///////////////////////////////////////////////////////////////////////////////

////////////////////////STEPS TO WRITE A ROS SERVICE/////////////////////

the service starts when a server first wakes up and begins listening for incoming request
the client will send a service request to the server which will parse the incoming message, process the requested service and then return  response back to the client

we have two types of messages, onde for sending the request and another message for the receiving the response
this is different from the publisher and subscriber communication paradigm

one step) [PUBLISHER]   -------- topic message -------> [SUBSCRIBER]     topic
_______________________________________________________________________

step 1) [SERVER] <----------- request message --------  [CLIENT]        service
step 2) [SERVER] ------------ response message -------> [CLIENT]


PRACTICAL STEPS TO CREATE A CLIENT/SERVER ROS SERVICE APP
step 1) define the service message (service file)
        - start by going to the package src folder and then creating folder srv. inside this folder you will define the service .srv file
        - this defines the request, the response and the type of data they will carry out
        - FOLLOW Up STEPS: next you have to compile the service and generate the source code
           *  go to package.xml and make sure that <build_depend>message_generation</build_depend> and <exec_depend>message_runtime</exec_depend> are included
           * then go to CMakeList.txt in find_package(catkin REQUIRED COMPOENETS make sure that message_generation is included)
           * also in CMakeList.txt make sure that add_service_files(FILES(this specifies all the files) name_of_service.srv is included )
           * finally go back to workspace and catkin build.
        - to check and see if the service was compiled go to the workspace devel folder,
          - then inside the include folder you will find another folder with the package name and inside that folder is the .h header files for the .srv file
          -  3 .h files would have been created

          - you can also use (rossrv list) and (rossrv show package_name/service_name) to see details about it

          - you can als just use the name of the service (rossrv show service_name such as AddTwoints) this returns the name of all the packages that define the same service

step 2) create ROS server node
step 3) create ROS client node
step 4) execute the service
step 5) consume the service by the client
