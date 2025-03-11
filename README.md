
# Attendance System

Pi-based RFID scanner that logs attendance and outputs data to a web ui


## Pinout Diagram

![App Screenshot](https://pimylifeup.com/wp-content/uploads/2017/10/RFID-Fritz-v2.png)

## Overview
```bash
scanCard(name,id,uid,date)
  IF card is NOT NULL
    name = name
    id = id
    uid = uid
    date = date
  ELSE catch exeption as ERROR
    PRINT ERROR

TRY datapase.push
  PRINT Upload Successful
Catch execption as ERROR
  PRINT ERROR
```

## Deployment

Clone the project

```bash
  git clone https://github.com/spraws/scanner
```

Go to the project directory

```bash
  cd scanner
```

Create the virtual enviroment

```bash
  python -m venv venv
```

Enter the virtual enviroment

```bash
  source .venv/bin/activate
```
Run the script
```bash
  python main.py
```
