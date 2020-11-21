import pandas as pd 

csv_path = "Resources/cities.csv"

cities_df = pd.read_csv(csv_path)

html = cities_df.to_html()

text_file = open("data_extract.html", "w")
text_file.write(html)
text_file.close