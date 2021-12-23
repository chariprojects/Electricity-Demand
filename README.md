# Electricity-Demand
Determination of patterns in the Spanish Real Electricity Demand
**Determination of patterns in the Spanish Real Electricity Demand**

This project aims to use Fourier Transforms to find the frequency in the Spanish Real Electricity Demand from 02/09/2018 to 06/10/2018.
The project uses Python 3.7.4 and the libraries: requests, numpy, matplotlib and scipy.fftpack. The project can be broken down into two sections. 
The first one requests information from the [e.sios API website](https://api.esios.ree.es/). The required variable _Real Power Demand_ can be found through the API with the name "IND_DemandaRealGen". To access it, a personal token must be requested at [consultasios@ree.es](consultasios@ree.es). Select _Getting a list of archives of type JSON_ option in the e.sios API website to obtain a list of archives of type JSON and filter by _start_date_ and _end_date_.
Now that the data has been accessed, the second section aims to manipulate the data and perform a Fourier Transform.
This is done by selecting the variable "dem" in the data obtained. Once the data from the variable is recalled and put into a numpy array, it must be transformed using the Fast Fourier Transform (FFT) library pack. Remember to calculate the corresponding frequencies to plot the Fourier Transform. Once the data has been obtained, use the library matplotlib to plot it.

The resulting Fourier Transform shows the frequency structure of the signal (Power Demand). This information can then be used to find other variables and to study the power demand evolution. 
In the results obtained there is clearly a pattern in the power demand evolution, where demand periods resemble each other. Through the Fourier Transform, the peaks obtained can be studied to find these periods of time. 
In this project it was found that there is a trend for the power demand every 24h.

Finally, it is important to note that there is still room for improvement in this project. The API call was made filtering the start_date and end_date, but it did only return 2 days' data. Due to this issue, string arrays were created for all the dates that were required to analyse. This method does not help towards the program optimisation and other methods should be studied to improve it. 
