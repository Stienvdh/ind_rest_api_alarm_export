# IND REST API demo for exporting alarms
This prototype allows its user to export alarms from Cisco Industrial Network Director using REST API.

## Contacts
* Stien Vanderhallen (stienvan@cisco.com)

## Solution Components
*  Cisco Industrial Network Director (IND)
*  Python: https://www.python.org/downloads/

## Installation/Configuration

0. In your terminal, clone this repository

```
$ git clone https://github.com/Stienvdh/ind_rest_api_alarm_export.git
$ cd ind_rest_api_alarm_export
```

1. In `.env`, enter your IND credentials.

2. Install the required Python libraries

```
$ pip install -r requirements.txt
```

3. Run this script

```
$ python3 main.py
```

4. In a browser, navigate to `localhost:5555`

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.