#  pip install gmplot
import gmplot
import pandas as pd
 
#gmap1 = gmplot.GoogleMapPlotter(30.3164945,78.03219179999999, 13 )
#gmap1.apikey = "AIzaSyDlakZYKdv6RNhMNG9oWKhWe1YFqijl7kw" 
#gmap1.draw( "/Users/rakesh/Desktop/map11.html" )
#


M1 = pd.read_csv('/Users/rakesh/Desktop/ded/Location_data_test1.csv')
M2 = M1["lat"].astype(float)
M3 = M1["lng"].astype(float)


Charminar_top_attraction_lats, Charminar_top_attraction_lons = zip(*[(M2[1],M3[1]),(M2[2],M3[2]),(M2[3],M3[3]),(M2[4],M3[4]),(M2[5],M3[5]),(M2[6],M3[6]),(M2[7],M3[7]),(M2[8],M3[8]),(M2[9],M3[9]),(M2[10],M3[10]),(M2[11],M3[11])])


gmap1 = gmplot.GoogleMapPlotter(M2[1],M3[1], 13 )

gmap1.scatter( Charminar_top_attraction_lats, Charminar_top_attraction_lons, '#FF0000',size = 50, marker = False )
              
gmap1.plot(Charminar_top_attraction_lats, Charminar_top_attraction_lons, 'cornflowerblue', edge_width = 3.0)

gmap1.apikey = "AIzaSyDlakZYKdv6RNhMNG9oWKhWe1YFqijl7kw" 
gmap1.draw( "/Users/rakesh/Desktop/map11.html" )




Charminar_top_attraction_lats, Charminar_top_attraction_lons = zip(*[
   (17.3833, 78.4011),(17.4239, 78.4738),(17.3713, 78.4804),(17.3616, 78.4747),
   (17.3578, 78.4717),(17.3604, 78.4736),(17.2543, 78.6808),(17.4062, 78.4691),
   (17.3950, 78.3968),(17.3587, 78.2988),(17.4156, 78.4750)])
#declare the center of the map, and how much we want the map zoomed in
gmap3 = gmplot.GoogleMapPlotter(17.3616, 78.4747, 13)
# Scatter map
gmap3.scatter( Charminar_top_attraction_lats, Charminar_top_attraction_lons, '#FF0000',size = 50, marker = False )
# Plot method Draw a line in between given coordinates
gmap3.plot(Charminar_top_attraction_lats, Charminar_top_attraction_lons, 'cornflowerblue', edge_width = 3.0)
gmap3.apikey = "AIzaSyDlakZYKdv6RNhMNG9oWKhWe1YFqijl7kw" 
gmap3.draw( "/Users/rakesh/Desktop/map12.html" )









gmap3 = gmplot.GoogleMapPlotter(M2[1],M3[1], 13) 
  
# scatter method of map object  
# scatter points on the google map 


gmap3.scatter( M2, M3 , 'green',size = 1, marker = False ) 
  
# Plot method Draw a line in 
# between given coordinates 
gmap3.plot(M2,M3 , 'cornflowerblue', edge_width = 2.5) 
gmap3.apikey = "AIzaSyDlakZYKdv6RNhMNG9oWKhWe1YFqijl7kw" 
gmap3.draw( "/Users/rakesh/Desktop/map13.html" ) 