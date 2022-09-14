# Selenium Grid Brown Bag Session
Base Selenium Behave with simple Page verifications

# Requirements
* `python 3.9`
* virtualenv
* `java 11`
* `docker`
* Download the `selenium-server-4.4.0.jar` file from [Selenium Downloads](https://www.selenium.dev/downloads/)

# Setup
- Setup Virtual Environment
```
# virtualenv
virtualenv .venv
```
- Activate Virtual Environment
```
# activate via virtualenv
.\venv\Scripts\activate
```
- Install Dependencies
```
# install dependencies via pip
pip install -r requirements.txt
```

# Tasks
1. Setup Remote WebDrivers
2. Set WebDriver Capabilities
3. Setup Grid Hub
4. Setup Grid Nodes and Register them to the Hub 
5. Run Grid and Nodes on Containers with Docker Compose



# Grid Node and Hub
![nodenhub](./assets/nodenhub.png)

# Dockerized Grid Node and Hub
![dockerizednodenhub](./assets/dockerizednodenhub.png)