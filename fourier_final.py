#Import required libraries
#to recall data from API
import requests	
#to modify the data obtained
import numpy as np 
#to plot the data obtained
import matplotlib.pyplot as plt 
#to calculate the fast fourier transform (fft)
from scipy.fftpack import fft, fftfreq      

def list_of_dates():
	#Create an array with the required dates
	s = list(('2018-08-31', '2018-09-01', '2018-09-02', '2018-09-03', '2018-09-04', '2018-09-05', '2018-09-06', '2018-09-07', '2018-09-08', '2018-09-09', '2018-09-10', '2018-09-11', '2018-09-12','2018-09-13','2018-09-14','2018-09-15','2018-09-16','2018-09-17','2018-09-18','2018-09-19','2018-09-20','2018-09-21','2018-09-22','2018-09-23','2018-09-24','2018-09-25','2018-09-26','2018-09-27','2018-09-28','2018-09-29','2018-09-30','2018-10-01', '2018-10-02', '2018-10-03', '2018-10-04', '2018-10-05'))
	f = list(('2018-09-01', '2018-09-02', '2018-09-03', '2018-09-04', '2018-09-05', '2018-09-06', '2018-09-07', '2018-09-08','2018-09-09','2018-09-10','2018-09-11','2018-09-12','2018-09-13','2018-09-14', '2018-09-15', '2018-09-16', '2018-09-17','2018-09-18','2018-09-19','2018-09-20','2018-09-21','2018-09-22', '2018-09-23','2018-09-24','2018-09-25','2018-09-26','2018-09-27','2018-09-28','2018-09-29','2018-09-30','2018-10-01','2018-10-02','2018-10-03', '2018-10-04', '2018-10-05', '2018-10-06'))
	return s,f

dem_values_whole_period = np.zeros([1])
for i in range(0,30):
#Calling the API for a particular archive (Real Demand)
	s,f = list_of_dates()
	end_date = f[i]
	url = 'https://api.esios.ree.es/archives/115/download_json?locale=es&start_date='+s[i]+'&end_date='+end_date
	payload={}
	headers = {
  	'Cookie': 'incap_ses_892_1885724=M0CXa3SbRHQsKTMNdQhhDPY4u2EAAAAA9HWKDtDKkOnjGich/aHeOA==; visid_incap_1885724=x43hqkeRThGoygt3R3Gp6OlLtmEAAAAAQUIPAAAAAADolXIQuvQ0EIkar+lrjtGp'
	}	

	response = requests.request("GET", url, headers=headers, data=payload)

#Recalling the data
	#Getting the data into a variable
	r = requests.get(url)
	#Declaring a variable to decide where to start reading the data
	startstep=0
	#Creating a list to fill with the data
	dem_index=list()
	#Creating a loop with a numpy array from 0 to 146(number of entries for the required variable)
	for i in np.arange(20,181):
		#Appending the "dem"(electricity demand) data entries found in API into the list
		dem_index.append(r.text.find("dem",startstep))	
		#Modify the start step every loop iteration to read all the data
		startstep=r.text.find("dem",startstep)+1
	#Convert the data obtained from a list into an array	
	dem_index=np.array(dem_index)
	#Declare a list where the demand results will be put into
	dem_value=list()										


	for i in np.arange(0,len(dem_index)):
		#Reading the data results for dem and appending the results into list dem_value
		dem_value.append(float(r.text[(dem_index+5)[i]:(dem_index+10)[i]]))		

	#Creating an arrange for the time variable of the data
	t = np.arange(0,800.09,1/6)	
	#Calculating the Fourier Transform of the Power Demand
	f = fft(dem_value)
	#Calculating the Fourier Frequency
	#T=sample spacing: 1/6
	#N=number of samplepoints:6154
	w = np.linspace(0,1/(1/3),2400) #np.linspace(0.0, 1.0/(2.0*T), N/2) 

	#Recalling all the data obtained for the Power Demand into a variable
	dem_values_whole_period = np.hstack((dem_values_whole_period,dem_value))
	dem_values_whole_period=dem_values_whole_period[1:]

#Calculate the Fourier Transform
f = fft(dem_values_whole_period)
#plt.plot(w,2.0/6154 * np.abs(f[0:int(6154/2)]))

#Adding the commands for the required plots. More info about the commands on matplotlib.org.
fig,axs = plt.subplots(2, sharex=False,sharey=False)
#axs[1].plot(w,2/30.2*np.abs(f[0:int(30.2//2)]))
axs[0].plot(t,dem_values_whole_period)	
axs[0].set(xlabel='Time (H)', ylabel='Power Demand (MW)',
       title='Power Demand')
axs[1].set(xlabel='Time^-1 (H^-1)', ylabel='Power Demand ^2 (MW^2)',
       title='Fourier Transform')
axs[1].plot(w,2/4801*np.abs(f[0:int(4801//2)]))	
axs[1].set_ylim((0,4000),auto=True)
axs[1].set_xlim((0,0.5),auto=True)
plt.show()


