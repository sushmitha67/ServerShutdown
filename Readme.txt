ServerShutdown:

	This program is used to send notification when the server goes down. It will ping server to check if server is up and running. If server doesn’t respond to ping request then application will send sms to mobile number mentioned in program. 
	
	IP address of server whose status have to be known, mobile number and password of way2sms user account have to be entered in user interface. If battery status is less than 20% and server is online sms will be sent. If battery status is less than 20% and server is offline sms will be sent.     

Installation:

Create an account in website www.way2sms.com.

Install psutil to check battery status.

	pip install psutil

Install Selenium. Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed. 

	pip install selenium

Install pyping to send ping request to computer.

	Pip install pyping

Install pyqt for user interface.











