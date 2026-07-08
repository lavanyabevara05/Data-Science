# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# iris = sns.load_dataset("iris")
# # print(iris.head())
# # print(iris.tail())
# # print(iris.groupby("species").size())

# print(sns.scatterplot(x= "sepal_length" , y = "sepal_width", data = iris))
# plt.figure(figsize= (12,8))
# print(sns.scatterplot(x= "sepal_length" , y = "sepal_width", data = iris))
# plt.show()

# install first if not installed
# pip install pywaffle

# from pywaffle import Waffle
# import matplotlib.pyplot as plt

# data = {'A': 40, 'B': 30, 'C': 20, 'D': 10}

# fig = plt.figure(
#     FigureClass=Waffle,
#     rows=10,
#     values=data,
#     title={'label': 'Waffle Chart Example'}
# )

# plt.show()

# pip install wordcloud

# from wordcloud import WordCloud
# import matplotlib.pyplot as plt

# text = "data science python python data visualization machine learning python"

# wc = WordCloud(background_color='white').generate(text)

# plt.imshow(wc)
# plt.axis('off')
# plt.show()


# import seaborn as sns
# import matplotlib.pyplot as plt

# data = [10, 20, 20, 30, 40, 40, 40, 50]

# sns.histplot(data)
# plt.show()


# import seaborn as sns
# import matplotlib.pyplot as plt

# x = ['A', 'B', 'C']
# y = [10, 20, 15]

# sns.barplot(x=x, y=y)
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [2,4,5,4,5]

# sns.regplot(x=x, y=y)
# plt.show()

# import folium

# m = folium.Map(location=[17.3850, 78.4867], zoom_start=10)

# m.save("map.html")

# import folium

# m = folium.Map(location=[17.3850, 78.4867], zoom_start=10)

# folium.Marker(
#     location=[17.3850, 78.4867],
#     popup="Hyderabad",
#     toggle="click me"
# ).add_to(m)

# m.save("map_marker.html")


# import folium

# # Step 1: Create base map
# m = folium.Map(location=[20, 0], zoom_start=2)

# # Step 2: Add Choropleth layer
# folium.Choropleth(
#     geo_data='world_countries.json',
#     data=[['India', 100], ['USA', 200]],
#     columns=['Country', 'Value'],
#     key_on='feature.properties.name',
#     fill_color='YlGn'
# ).add_to(m)

# # Step 3: Save map
# m.save("choropleth.html")
