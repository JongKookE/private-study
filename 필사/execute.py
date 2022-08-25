import my_data

data = my_data.titanic("train")

print('Highest Fare was:',data['Fare'].max())
print('Lowest Fare was:',data['Fare'].min())
print('Average Fare was:',data['Fare'].mean())

my_data.vis_Pclass_Fare(data)

my_data.corr_heatmap(data)