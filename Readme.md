# plot_map

plot_map is a module to plot map backgroud using matplotlib. Just use the following code:  

    plot_map(plt,bounds,zoom = 9,style = 1)

You can change your map style by changing the "style" and "styleid" in the function plot_map  

	bounds -- Set your plotting boundary [lon1,lat1,lon2,lat2] (wgs1984)  
	zoom -- The zoom level of the map  
	style -- From 1 to 7 represent different map styles,1-6 is from openstreetmap and 7 is the mapbox    
	styleid -- if style is set as 7(from mapbox), you can change the styleid here, "dark" or "light" or your own style  

<<<<<<< HEAD
see more on the ipynb: Tutorial(https://github.com/ni1o1/plot_map/blob/master/tutorial/Tutorial_of_plot_map.ipynb)
=======
see more on the ipynb: Tutorial(https://github.com/ni1o1/plot_map/blob/master/Tutorial_of_plot_map.py)
>>>>>>> e9d8d83577458028a6a49b8479584274492eef15

<img height="600" src="img/example.png">
