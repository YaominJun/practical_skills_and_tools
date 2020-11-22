# Rviz visualization

## step0: Dependencies

    #include <visualization_msgs/MarkerArray.h>

## step1: ROS publisher

    ros::Publisher visual_pub;
then in **initialization function**:</br>
    if you just want to draw one point: </br>

    visual_pub = nh_.advertise<visualization_msgs::Marker>("/marker", 1, false);

or if you just want to draw one path (many points): </br>

    visual_pub = nh_.advertise<visualization_msgs::MarkerArray>("/markers", 1, false);

## step2：Set markers or marker array to publish
### main visualization tools: 
(0) **Marker**: Compact Message Definition: </br>
[]()[Marker wiki](http://docs.ros.org/en/api/visualization_msgs/html/msg/Marker.html)

    uint8 ARROW=0
    uint8 CUBE=1
    uint8 SPHERE=2
    uint8 CYLINDER=3
    uint8 LINE_STRIP=4
    uint8 LINE_LIST=5
    uint8 CUBE_LIST=6
    uint8 SPHERE_LIST=7
    uint8 POINTS=8
    uint8 TEXT_VIEW_FACING=9
    uint8 MESH_RESOURCE=10
    uint8 TRIANGLE_LIST=11

    uint8 ADD=0
    uint8 MODIFY=0
    uint8 DELETE=2
    uint8 DELETEALL=3

    std_msgs/Header header
    string ns
    int32 id
    int32 type
    int32 action    # 0 add/modify an object, 1 (deprecated), 2 deletes an object, 3 deletes all objects
    geometry_msgs/Pose pose     # Pose of the object
    geometry_msgs/Vector3 scale     # Scale of the object 1,1,1 means default (usually 1 meter square)
    std_msgs/ColorRGBA color
    duration lifetime
    bool frame_locked

    #Only used if the type specified has some use for them (eg. POINTS, LINE_STRIP, ...)
    geometry_msgs/Point[] points

    #Only used if the type specified has some use for them (eg. POINTS, LINE_STRIP, ...)
    #number of colors must either be 0 or equal to the number of points
    #NOTE: alpha is not yet used
    std_msgs/ColorRGBA[] colors

    # NOTE: only used for text markers
    string text

    # NOTE: only used for MESH_RESOURCE markers
    string mesh_resource
    bool mesh_use_embedded_materials
</br>

(1) **MarkerArray**: Compact Message Definition: </br>
It's a array contains Marker. </br>
[]()[MarkerArray wiki](http://docs.ros.org/en/api/visualization_msgs/html/msg/MarkerArray.html)

    visualization_msgs/Marker[] markers

### some important setting:
(0) marker.type: </br>
*definition*: int32 type </br>

*types*: 

    uint8 ARROW=0
    uint8 CUBE=1
    uint8 SPHERE=2
    uint8 CYLINDER=3
    uint8 LINE_STRIP=4
    uint8 LINE_LIST=5
    uint8 CUBE_LIST=6
    uint8 SPHERE_LIST=7
    uint8 POINTS=8
    uint8 TEXT_VIEW_FACING=9
    uint8 MESH_RESOURCE=10
    uint8 TRIANGLE_LIST=11

*examples*: </br>

    marker.type = visualization_msgs::Marker::ARROW;
or </br>
    
    marker.type = 0;

(1) marker.color </br>
*definition*: std_msgs/ColorRGBA color </br>
and **std_msgs/ColorRGBA**: Compact Message Definition </br>

    float32 r
    float32 g
    float32 b
    float32 a

while r, g, b is to set color, and a is to set object transparency. </br>
*examples*: </br>

    marker.color.a = 0.5;
    path_marker.color.r = 1;
    path_marker.color.g = 0;
    path_marker.color.b = 0;

(2) marker.pose </br>
*definition*: geometry_msgs/Pose pose </br>
this is the definition of the pose of the object. </br>
and **geometry_msgs/Pose**: Compact Message Definition </br>

    geometry_msgs/Point position
    geometry_msgs/Quaternion orientation

*examples*: </br>

    marker.pose.position.x = mp.position.x;
    marker.pose.position.y = mp.position.y;
    marker.pose.position.z = mp.position.z;
    marker.pose.orientation = mp.orientation;
**Notice!** </br>
if you just want to draw points rather than arrows, you can just set the 
    
    pose.position.x, pose.position.y, pose.position.z
and don't need to set `pose.orientation`. </br>
(3) MarkerArray </br>
*definition*: **visualization_msgs/Marker[] markers** </br>
when you want to draw a series of points (like a path) rather than one point, you can use this msg. </br>

*examples*: </br>

    marker_array.markers.push_back(marker);


## Publish the markers and marker array

draw one point:

    visual_pub.publish(marker);
or draw one path (many points): 

    visual_pub.publish(marker_array);
