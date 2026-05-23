import matplotlib.pyplot as plt

# Data
languages = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
popularity = [30, 25, 20, 15, 10]

# Create pie chart
plt.figure()
plt.pie(popularity, labels=languages)
plt.title('Languages Popularity')

plt.show()


