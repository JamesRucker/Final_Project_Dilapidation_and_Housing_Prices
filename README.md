# Housing Prices Machine Learning
A project to use machine learning to better predict housing prices.

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Conclusion](#conclusion)
* [Deployment](#deployment)
* [Sources](#sources)

## General Info
Housing prices are one of the few expenses that can not ever be avoided. Purchasing a home is seen as a necessary step toward achieving "The American Dream". This, combined with the high prices of housing, mean that better methods of predicting prices are incredibly valuable. In this particular case, machine learning's ability to be trained using various variables and then to apply that to prediction makes it promising. A Convoluted Neural Network was used to create the machine, and the data was limited to the greater Phoenix metropolitan area.

This project was done for a data visualization bootcamp with particular interest towards learning to use machine learning.

## Technologies
* Python version: 3.6.10.final.0
* Pandas version: 1.0.4
* Numpy version: 1.18.1
* Matplotlib version: 3.2.1
* Scipy version: 1.4.1
* Tensorflow version: 2.1.0
* Tableau
* SQL
* Keras
* Plotly.py
* Sklearn
* CSS
* Javascript
* HTML
* Flask
* splinter
* BeautifulSoup
* Census python module

## Setup
In order to rerun the program for extracting census data, a config.py containing an API key for the census API (named "census_api_key" as a string) and located in 
the Resources folder will be necessary. Similarly, to ensure that the Zillow webscraping will work properly, ensure that Chrome and Chromedriver are fully updated and that chromedriver.exe is  located in the same folder as the zillow scraping program.

## Conclusion
The machine learning program did give promising results. Even though the machine was trained on data ranging from condos to mansions, the mean absolute error was about $58000, and the mean percent difference was about 18%. The varied nature of the data undoubtedly contributed to this, so a model with a narrower scope, such as one focusing only on family houses, may increase the accuracy of the results. A correlation matrix give credence to the inclusion of census data by zip code in the model. In particular, categories related to income and education attainment were somewhat predictive.  However, as income and educational attainment are shown in the same matrix to be heavily correlated, one of the categories may be unnecessary in the model. Educational attainment being the more complicated would be the first candidate to cut. Unsurprisingly however, the size of the house and the number of bedrooms and bathrooms were the most predictive. Information concerning the model and the housing data was then deployed to heroku in the url contained in the deployment section below.

## Deployment
https://homeprice-prediction.herokuapp.com/

## Sources
https://www.census.gov/data/developers/data-sets/acs-5year/2018.html  
https://zillow.com  
https://simplemaps.com/data/us-zips
