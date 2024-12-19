#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

file_path = 'customer_shopping_data_expanded.csv'
data = pd.read_csv(file_path)


# In[2]:


# Displaying the first few rows of the dataset
print(data.head())


# In[3]:


# Checking the number of rows in the dataset
print("Number of rows:", data.shape[0])


# In[4]:


# Checking for null values
print("Null values in each column:")
print(data.isnull().sum())


# In[5]:


# Dropping rows with null values
data_cleaned = data.dropna()


# In[6]:


# Displaying the cleaned dataset
print("Cleaned dataset:")
print(data_cleaned.head())


# In[7]:


# Checking the number of rows after cleaning
print("Number of rows after cleaning:", data_cleaned.shape[0])


# In[8]:


# Feature Engineering, Pivoting, Grouping, and Insights

# Adding a new feature: Total cost (quantity * price)
data_cleaned['total_cost'] = data_cleaned['quantity'] * data_cleaned['price']


# In[9]:


# Adding a new feature: Age group
bins = [0, 18, 35, 50, 65, 100]
labels = ['Under 18', '18-35', '36-50', '51-65', '65+']
data_cleaned['age_group'] = pd.cut(data_cleaned['age'], bins=bins, labels=labels, right=False)


# In[10]:


# Pivot table: Average total cost by gender and age group
pivot_table = data_cleaned.pivot_table(values='total_cost', index='gender', columns='age_group', aggfunc='mean')


# In[11]:


# Grouping: Total revenue by shopping mall
total_revenue_by_mall = data_cleaned.groupby('shopping_mall')['total_cost'].sum().sort_values(ascending=False)


# In[12]:


# Insights
# 1. Top 5 shopping malls by total revenue
top_5_malls = total_revenue_by_mall.head(5)


# In[13]:


# 2. Average total cost by payment method
avg_cost_by_payment = data_cleaned.groupby('payment_method')['total_cost'].mean().sort_values(ascending=False)


# In[14]:


# Read the data
df = pd.read_csv('clean_data.csv')


# In[15]:


# Get a summary of transactions by country
country_summary = df.groupby('country')['total_cost'].agg(['count', 'sum', 'mean']).round(2)
country_summary = country_summary.sort_values('sum', ascending=False)


# In[16]:


# Displaying results
print("Pivot Table: Average Total Cost by Gender and Age Group")
print(pivot_table)


# In[17]:


print("\
Top 5 Shopping Malls by Total Revenue:")
print(top_5_malls)


# In[18]:


print("\
Average Total Cost by Payment Method:")
print(avg_cost_by_payment)


# In[19]:


# Fill missing values in each column with the median of that column
data_cleaned = data_cleaned.fillna(data_cleaned.median(numeric_only=True))


# In[19]:


# Calculating mean, mode, and IQR for the 'total_cost' column
mean_total_cost = data_cleaned['total_cost'].mean()
mode_total_cost = data_cleaned['total_cost'].mode()[0]
iqr_total_cost = data_cleaned['total_cost'].quantile(0.75) - data_cleaned['total_cost'].quantile(0.25)

# Displaying the calculated values
print("Mean of Total Cost:", mean_total_cost)
print("Mode of Total Cost:", mode_total_cost)
print("IQR of Total Cost:", iqr_total_cost)

# Creating a pie chart for the 'category' distribution
plt.figure(figsize=(8, 8))
data_cleaned['category'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140, cmap='viridis')
plt.title('Category Distribution')
plt.ylabel('')
plt.show()

# Generating a normal distribution using the mean and standard deviation
std_total_cost = data_cleaned['total_cost'].std()
normal_dist = np.random.normal(mean_total_cost, std_total_cost, 1000)

# Plotting the normal distribution
plt.figure(figsize=(10, 6))
sns.histplot(normal_dist, kde=True, color='blue', bins=30)
plt.title('Normal Distribution of Total Cost')
plt.xlabel('Total Cost')
plt.ylabel('Frequency')
plt.show()


# In[20]:


# Create sample data
np.random.seed(42)
data = {
    'total_cost': np.random.lognormal(mean=4, sigma=0.5, size=1000),
    'category': np.random.choice(['Electronics', 'Clothing', 'Food', 'Books'], size=1000)
}
data_cleaned = pd.DataFrame(data)

# Calculate statistics
stats = {
    'mean': data_cleaned['total_cost'].mean(),
    'mode': data_cleaned['total_cost'].mode()[0],
    'iqr': data_cleaned['total_cost'].quantile(0.75) - data_cleaned['total_cost'].quantile(0.25)
}

print("Statistical Summary:")
for key, value in stats.items():
    print(f"{key.title()}: {value:.2f}")

# Create subplots for better organization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Category distribution pie chart
data_cleaned['category'].value_counts().plot(
    kind='pie', 
    autopct='%1.1f%%', 
    ax=ax1, 
    cmap='viridis'
)
ax1.set_title('Category Distribution')
ax1.set_ylabel('')

# Distribution plot
sns.histplot(data_cleaned['total_cost'], kde=True, ax=ax2, color='skyblue')
ax2.set_title('Distribution of Total Cost')
ax2.set_xlabel('Total Cost')

plt.tight_layout()
plt.show()


# In[21]:


# Set style
plt.style.use('seaborn')

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot 1: Revenue by Shopping Mall
sns.barplot(x=total_revenue_by_mall.head().values, y=total_revenue_by_mall.head().index, ax=ax1)
ax1.set_title('Top 5 Shopping Malls by Revenue')
ax1.set_xlabel('Total Revenue')

# Plot 2: Payment Method Distribution
sns.barplot(x=avg_cost_by_payment.index, y=avg_cost_by_payment.values, ax=ax2)
ax2.set_title('Average Cost by Payment Method')
ax2.set_xlabel('Payment Method')
ax2.set_ylabel('Average Cost')

plt.tight_layout()
plt.show()

# Category distribution
plt.figure(figsize=(10, 6))
data_cleaned['category'].value_counts().plot(kind='bar')
plt.title('Distribution of Product Categories')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[22]:


# Create a bar plot of total sales by country
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='country', y='total_cost', estimator=sum)
plt.xticks(rotation=45)
plt.title('Total Sales by Country')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

print("\
Summary of transactions by country:")
print(country_summary)


# In[23]:


# Check missing values
print("Missing Values Count:")
print(data_cleaned.isnull().sum())

# Calculate percentage of missing values
print("\
Percentage of Missing Values:")
print((data_cleaned.isnull().sum() / len(data_cleaned) * 100).round(2))

# Visual representation of missing values
plt.figure(figsize=(10, 6))
sns.heatmap(data_cleaned.isnull(), yticklabels=False, cbar=True, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.show()


# In[24]:


data_cleaned.to_csv('clean_data_1.csv', index=False)

