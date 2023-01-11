# Logistic Hackthon Vorbereitung 

## get started 
- create venv 
```shell 
pip install venv 
python -m venv .env
```

- activate venv  

powershell: 
```shell 
.env/Scripts/Activate.ps1
```

cmd: 
```shell 
env/Scripts/activate.bat
```

- install requirements 
```shell 
pip install -r requirements.txt
```

- solve hill_climbing.ipynb


## best practices 

1. start with the simplest solution possible 
2. make first "result" really fast
3. iterate to get to better solution over time 

-> this is important because:   
    - normally reading the input and getting the output in format is complicated   
    - you need to have a metric on which you can improve on - otherwise it's just guessing   
    - if the first pass through works the next iterations will also work it's different the other way around  

## walter group hackathon last year 

you get a skelleton of an api you have to fill [fastapi](https://fastapi.tiangolo.com/tutorial/first-steps/)  
the api is a POST call that sends you a list of offers  
offers have a lot of attributes like: revenue, cost, time, origin, destination etc.  
you also get a graph of the whole network with distances on each edge  
your driver needs to take breakes otherwise there is the risk of an accident  

you need to decide which is the best offer and return the id of the offer  
or return how long you want to take a break  
or return in which city you want to drive without taking an offer  

-> why did we win?  
1. make good profit function: we calculated profit over time  
2. choose wisely where to start or drive if there is no profit atm 

