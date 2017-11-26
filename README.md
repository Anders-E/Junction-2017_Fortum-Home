# Fortum Challenge - Smart Electricity
# Husa 

#### A project by:

- Anders Eriksson *(Computer Science & Engineering)*
- Simon Johansson Nyberg *(Engineering Physics)*
- Johan Skrealid *(Energy Systems Engineering)*

## Introduction

With the introduction of technology such as Google Home and the Apple HomeKit line of products, the demand for smart home services is on the rise and Fortum has the opportunity to take a leading role in the field.

This project aims to bring an entry level smart home feature to the customers of Fortum without any additional hardware requirements.

## Problem Statement

What new useful services can be created utilizing already existing data that are interseting to and applicable for Fortums large customer base?   

## Husa

Enter Husa, an addition to the already existing Fortum app, Husa gives the customer an entry level smart home feature in the shape of notifications.

### Home Status - In Real Time 

The Fortum app already allows the customer to view his/her homes power consumption in real time. This information, however interesting isn't used by the majority of customers. Husa simplifies this information into two categories and informs the customer if his/her home is asleep or active.

#### Asleep
When next to no power-related activity is taking place, apart from indoor climate being maintained, your home status on the app will be showing the *Asleep* status.

#### Active
If the lights have been turned on and you are spending leisure time with the tv, radio or computer, resulting in a slight uptick in your power consumption, your home will be flagged *Active*.

When a rise or dip in power consumption occurs a the users homes, the user is informed of this through a push notification on their phone. No more wondering if the children are already home from school or if the relatives have reached the winter cottage, this is answered automatically. A simple way of giving the customer valuable and convenient information in daily life.

Wether it be a Finnish *mökki*, a Swedish *sommarstuga*, or Russian *dacha*, the service should give owners of vacational properties extra peace of mind. Considering the Nordic countries are Fortum's largest market, this would prove very interesting to both Fortum and their customers.

All already existing features of the Fortum app such as this month power usage, current price of electricity, etc. are of course maintained.

## Benefits (Why)

#### Simplicity

- The data is readily available.

- The solution requires no additional installations beyond what is planned for Fortums customers.

- Husa is simple and targets all of Fortums customers.

#### Usefullness

- Having an additional measure of control.

## Technological Solution

With access to live data of the houses energy consumption, the actual implementation is actually simple and easy to deploy to anyone with the correct electricity meter.

The way we did it was to first of all smooth the data. The raw data can be very erratic due to certain electrical utilities in a household (heating etc.). Smoothing in this case means calculating the arithmetic mean based on the

#### Raw Data
![raw data](https://github.com/Anders-E/Junction-2017_Fortum-Home/blob/master/data/plots/10-01-11.png?raw=true "Raw Data")

#### Smoothed Data
![smoothed data](https://github.com/Anders-E/Junction-2017_Fortum-Home/blob/master/data/plots/10-01-11-smooth-60.png?raw=true "Smoothed Data")

After smoothing the data, it's just a matter of finding a suitable threshold for what's considered active vs asleep for a specific household. We used the median value which worked out very well for the household of the data we acquired. For actual deployment of this application, further research will have to be carried out to determine a good way to determine a threshold. We believe very simple machine learning could be used to determine this very effectively.

#### Smoothed Data With Threshold
![smoothed data thresh](https://github.com/Anders-E/Junction-2017_Fortum-Home/blob/master/data/plots/10-01-11-smooth-60-thresh.png?raw=true "Smoothed Data With Threshold")

## Screenshots

#### Notification

![notification active](https://github.com/Anders-E/Junction-2017_Fortum-Home/blob/master/prototype-screens/notification_active.png?raw=true "Notification Awake")

#### Active
![active](https://github.com/Anders-E/Junction-2017_Fortum-Home/blob/master/prototype-screens/home.png?raw=true "Active")

#### Asleep
![asleep](https://github.com/Anders-E/Junction-2017_Fortum-Home/blob/master/prototype-screens/cabin.png?raw=true "Asleep")

## Ideas For Further Development

Building upon the idea of certain appliances having a destinct power profile, a customer could tailor his/her home profile by labeling the typically intensive appliances (Oven, sauna, shirt iron, dishwasher). This would enable reminders for things that need to be shut off or allow exclution of things that can safely be left unattended when leaving the house (dishwasher, washing machine).

Prolonged usage of a power-intensive appliance causes a push notification of reminding you of its use (*"Are you making slow cooked beef tenderloin or is it time to turn off the oven?"*)
