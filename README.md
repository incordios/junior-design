# ECE-3872
This is the class repository for ECE3872, Fundamentals of Design. Below are the instructions and details to get you up and running with Wonderland project :smiley:

# Getting Started

## Windows
### For Students

Clone this repo into desired working directory on the Raspberry Pi 
```bash 
git clone https://github.gatech.edu/tbrothers3/ECE-3872.git
cd Projects/Wonderland
```

You will be editing the `robot.py` file to code in your robot's corresponding logic. Please follow the comments for guidance. 

For deployment into actual environment, obtain the director IP and edit the script. Then on bootup, you must run the `robot.py` script. 

### For Director

Clone this repo into desired working directory on the Linux machine. 
```bash 
git clone https://github.gatech.edu/tbrothers3/ECE-3872.git
cd Projects/Wonderland
```

Install the necessary dependencies
```bash
sudo python3 install -r requirements.txt
sudo python3 install keyboard
```

Create or edit an appropriate CSV file to define the robot order, latency, and command. Then use the following to run the director. 
```bash
sudo python3 director.py <path to csv file>
```

### For Demo Run

Clone this repo into desired working directory on the Linux machine. 
```bash 
git clone https://github.gatech.edu/tbrothers3/ECE-3872.git
cd Projects/Wonderland
```

Install the necessary dependencies
```bash
python3 install -r requirements.txt
```

You can either get two ssh or shell sessions on the Pi and run the commands for director and robot above. If you can't do the following below. 
Create a separate screen sessions for the robot
```bash
sudo apt update
sudo apt install screen
```

Run the director in one session. 
```bash
screen -d -m sudo python3 director.py <path to csv file>
```

Run the robot in a separate terminal.
```bash
screen -d -m sudo python3 demo_robot.py
```

View all the screen sessions
```bash
screen -ls
```

Attach to the director screen session to enter q to continue the demo
```bash 
screen -r <director screen session name> 
```

## Mac
Run server.py
```bash 
python3 server.py
```

Run client.py
```bash 
python3 client.py
```

# Workflows

### Director Workflow
![image](https://github.gatech.edu/storage/user/36924/files/3a65e800-8db5-4410-b7be-3a2d468da0d8)


### Robot Workflow
![image](https://github.gatech.edu/storage/user/36924/files/5009c66e-b7c6-4e2b-939d-f8608703b652)

