# Junction2017 - Fortum Challenge - Smart Electricity

#### A project by:

- Anders Eriksson *(Computer Science & Engineering)*
- Simon Johansson Nyberg *(Engineering Physics)*
- Johan Skrealid *(Energy Systems Engineering)*

## Introduction

With the introduction of technology such as Google Home and the Apple HomeKit line of products, the demand for home automation is growing ever larger.

This project aims to bring an entry level home automation feature to Fortum customers without any additional hardware requirements.

## Problem Statement

Home Automation is hotter than ever, but the step towards an automated home require both expensive hardware purchases as well as tiresome installation.   

## Fortum Home

Enter Fortum Home. Based on the already existing Fortum app, it gives the customer an entry level home automation feature without any expense from the customer, be it time or money.

The main feature of the Fortum Home app is...

### Real Time Home Status

The Fortum Home app gives the user real time updates of the power usage straight from their home.

When the Fortum Home app detects a rise or dip in power consumption of any of the users homes, the users is almost instantly informed of this through a push notification on their phone. This not only gives the Fortum customer peace of mind, but gives him or her valuable convenient information in daily life. The question of wether someone is already home is now not even a phone call away but is delivered to you automatically.

Wether it be a Finnish *mökki*, a Swedish *sommarstuga*, or Russian *dacha*, the service should give owners of vacational properties extra peace of mind. Considering the Nordic countries are Fortum's largest market, this would prove very interesting to both Fortum and their customers.

All already existing features of the Fortum app such as this month power usage, current price of electricity, etc. are of course maintained.

#### Asleep
When next to no power-related activity is taking place, apart from basic heating, your home status on the app will be showing the *Asleep* status.

#### Active
If the lights have been turned on and you are spending leisure time with the tv, radio or computer, resulting in a slight uptick in your power consumption, your home will be flagged *Active*.

## Benefits (Why)

1. Simplicity
...The data is readily available.
...The solution requires no additional installations beyond what is planned for Fortums customers.
...The app-extensions are simple and targets all of Fortums customers.

2. Usefullness
...Having an additional measure of control

## Technological Solution

With access to live data of the houses energy consumption, the actual implementation is actually simple and easy to deploy to anyone with the correct electricity meter.

The way we did it was to first of all smooth the data. The raw data can be very erratic due to certain electrical utilities in a household (heating etc.). Smoothing in this case means calculating the arithmetic mean based on the

#### Raw Data
![raw data](https://github.com/Anders-E/Junction2017_Fortum/blob/master/data/plots/10-01-11.png?raw=true "Raw Data")

#### Smoothed Data
![smoothed data](https://github.com/Anders-E/Junction2017_Fortum/blob/master/data/plots/10-01-11-smooth-60.png?raw=true "Smoothed Data")

After smoothing the data, it's just a matter of finding a suitable threshold for what's considered active vs asleep for a specific household. We used the median value which worked out very well for the household of the data we acquired. For actual deployment of this application, further research will have to be carried out to determine a good way to determine a threshold. We believe very simple machine learning could be used to determine this very effectively.

***Smart home notifications***
Status changes happening while you are absent results in a push notification (*"Your home is active"*), allowing the owner to know when their children come home from school or when the relatives arrives in the winter cabin.

Prolonged usage of a power-intensive appliance causes a push notification of reminding you of its use (*"Are you making slow cooked beef tenderloin or is it time to turn off the oven?"*)

Building upon the idea of certain appliances power usage being destinct a home-owner could personalise his/her house-profile by labeling the tycally intensive appliances (Oven, sauna, iron, dishwasher). This would enable reminders for things that need to be shut off or allow exclution of things that might be safe leaving on when leaving the house (dishwasher washing machine).

homes solutions. (Enable smarthome mode => push notification whenever a large power consumption is initatied, asking which kind of appliance was activated)

