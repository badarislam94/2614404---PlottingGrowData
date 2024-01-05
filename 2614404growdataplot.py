#importing necessary libraries 
import pandas as pd                                   #The pandas library is used for data manipulation and analysis
from shapely.geometry import Point                    #shapely.geometry library will be used to create the points and adjust them according to our task
import matplotlib.pyplot as plt                       #This library is used for plotting the data
import matplotlib.image as mpimg                      #This library is used to deal with images

# Here we are loading the Grow dataset into a DataFrame
df = pd.read_csv('GrowLocations.csv') #As i placed dataset file in the same directory so that's why did not paste the complete path otherwise write full path here

#In this step we are swapping latitude and longitude columns as we observed the column headings were swapped corresponding to the values
df['Latitude'], df['Longitude'] = df['Longitude'], df['Latitude']

#Now we are defining the bounding box for the map as per given dimensions in the assignment
minlongitude = -10.592
maxlongitude = 1.6848
minimumlatitude = 50.681
maximumlatitude = 57.985

# Now we'll be filtering out locations outside the allowed bounding box created in previous step
df = df[(df['Longitude'] >= minlongitude) & (df['Longitude'] <= maxlongitude) &  #This line of code will limit the map w.r.t longitude on x-axis (defined below)
        (df['Latitude'] >= minimumlatitude) & (df['Latitude'] <= maximumlatitude)]  #This line of code will limit the map w.r.t latitude on y-axis (defined below)

# Here we are loading the given uk map image
ukmap = mpimg.imread('map7.png')  #As i placed 'map7.png' in the same directory so that's why did not paste the complete path otherwise write full path here

#Now creating a subplot to display UKMAP stored in last step and setting the plots using extent which sets the limits of x and y axes according to bounding box
figure, subplot_ax = plt.subplots(figsize=(11, 11))
subplot_ax.imshow(ukmap, extent=[minlongitude, maxlongitude, minimumlatitude, maximumlatitude])

#Now we are plotting GROW sensor locations on the top of figure created in previous step
subplot_ax.scatter(df['Longitude'], df['Latitude'], color='Teal', marker='o', s=27, label='GROW Sensors')

# Setting x and y axes limits in the below step
subplot_ax.set_xlim(minlongitude, maxlongitude)
subplot_ax.set_ylim(minimumlatitude, maximumlatitude)

# Now we are adding necessary legends and labels to make the plot readable, presentable and understandle for everyone
subplot_ax.legend()
plt.title('Plotting Grow Data on UK Map')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Below command will simply create the plot
plt.show()
