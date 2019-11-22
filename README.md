#FINDING THE BEST LOCATION FOR A COMPANY GIVING CERTAIN CONDITIONS#

In this project I followed this steps:

    - Decided I wanted my company to be in New York
    - Decided I wanted my company to be close to a Starbucks
    - Decided I wanted my company to be close to a School
    - Decided I wanted my company to be close to a Club

That been said, I started working from a dataset and a collection on mongodb with thousands of companies. I got the coordiantes form its offices.location tag and create a new tag called loc (with {'type':'point', 'coordinates':[]} form in order to create a geoindex)with the coordinates, with which I update the collection.

Then I used Google Places Api to get the Starbucks, Schools, and Clubs in New York. Each of this requests were made in separated jupyter notebooks.

After that, I transformed it into a dataframe, and I kept only columns name, location (also with {'type':'point', 'coordinates':[]}).

Those dataframes were turned into json and then uploaded to the database in spread collections.

Finally, I checked in my companies collections for companies with a deadpoled year bigger than 2010 to find empty offices, created a dataframe and a new collection importing its json.

Ultimately, I created geoindex in ecach collection. Then I check the number of each nearby places for each empty office using a geoquery function and found two different locations that matches the conditions.