# Secondary Node Addition Procedure
This project simulates the Secondary Node Addition procedure betweeen MN , SN and MME Nodes.

![Image](https://github.com/ardaisker/SecondaryNodeAdditionProcedure/blob/main/MNSNProcedure.jpg?raw=true)

## Project Prequisites
Python 3.6
## Installation
Clone the repository to your local file ([Clone](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)) , 

# Demo
A demo video for the project :  [https://youtu.be/bdMS8DcUUMQ](https://youtu.be/bdMS8DcUUMQ) 




## Usage


```bash
python execute.py
```


**config.json** file is configuration file for the connections.\
 on "Nodes" array : **node names , node ids , node ip addresses** *(real addresses)* are adjustable.\
\
on "Connections"  array : **name of connections , activity status** (0 : unactive , 1: active)  **, port number , sender & receiver ids** are adjustable.\
\
on "Messages" array : **Message to send(string),activity status (0 : unactive , 1: active)** , are adjustable.\
If a message is active, it appends to total message to send (from up to down).




```json
{
  "Nodes": [
    {
      "name": "MN",
      "id": "1",
      "ip": "127.0.0.1"
    },
    {
      "name": "SN",
      "id": "2",
      "ip": "127.0.0.1"
    },
    {
      "name": "MME",
      "id": "3",
      "ip": "127.0.0.1"
    }
  ],
  "Connections": [
    {
      "name": "con1",
      "isActive":"1",
      "port": 10000,
      "from": "1",
      "to": "2"
    },
    {
      "name": "con2",
      "isActive":"1",
      "port": 10001,
      "from": "1",
      "to": "3"
    },
    {
      "name": "con3",
      "isActive":"1",
      "port": 20000,
      "from": "2",
      "to": "1"
    },
    {
      "name": "con4",
      "isActive":"1",
      "port": 20001,
      "from": "2",
      "to": "3"
    },
    {
      "name": "con5",
      "isActive":"1",
      "port": 30000,
      "from": "3",
      "to": "1"
    },
    {
      "name": "con6",
      "isActive":"1",
      "port": 30001,
      "from": "3",
      "to": "2"
    }
  ],
  "Messages": [
    {
      "message": "Hello",
      "isActive":"1"
    },
    {
      "message": "Taco",
      "isActive":"1"
    },
    {
      "message": "Apple",
      "isActive":"1"
    }
  ]
}
```

## Contact
Arda Isker - ardaegeisker@gmail.com\
Project Link: [https://github.com/ardaisker/SecondaryNodeAdditionProcedure](https://github.com/ardaisker/SecondaryNodeAdditionProcedure) 


## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## License
[MIT](https://choosealicense.com/licenses/mit/)
