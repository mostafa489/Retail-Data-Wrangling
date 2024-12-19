# Libraries
library(dplyr)
library(ggplot2)
library(readr)

# Load   
customer_shopping_data_expanded <- read_csv("C:/Users/youss/Downloads/customer_shopping_data_expanded.csv")

#first few rows of the dataset
head(customer_shopping_data_expanded)

# structure
str(customer_shopping_data_expanded)

# statistics
summary(customer_shopping_data_expanded)

#missing values
missing_values <- colSums(is.na(customer_shopping_data_expanded))
print("Missing values in each column:")
print(missing_values)

# Visualizations Before Cleaning

# Scatter plot of 'quantity' vs. 'price' to check for relationship
ggplot(customer_shopping_data_expanded, aes(x = quantity, y = price)) +
  geom_point(color = "purple", alpha = 0.6) +
  ggtitle("Scatter Plot of Quantity vs Price") +
  theme_minimal()

# Bar plot for categorical variable 'gender'
ggplot(customer_shopping_data_expanded, aes(x = gender)) +
  geom_bar(fill = "lightcoral", color = "darkred") +
  ggtitle("Gender Distribution") +
  theme_minimal()

# Cleaning the Data

# Handle missing values: Replace NAs with the column mean for numeric columns (e.g., age, quantity, price)
cleaned_data <- customer_shopping_data_expanded %>%
  mutate(across(where(is.numeric), ~ ifelse(is.na(.), mean(., na.rm = TRUE), .))) %>%
  # Alternatively, you can remove rows with missing values like so:
  # na.omit(customer_shopping_data_expanded)
  
  # Convert character columns to factors (for 'gender', 'category', 'payment method')
  mutate(across(c(gender, category, `payment_method`), as.factor))

# View the cleaned data
head("clean_data_1")

# Summary of the cleaned data
summary(clean_data_1)

# Save the cleaned data to a new CSV file
write.csv(clean_data_1, "C:/Users/youss/Downloads/cleaned_customer_shopping_data_expanded.csv", row.names = FALSE)

# Visualizations After Cleaning


# Scatter plot of 'quantity' vs. 'price' after cleaning
ggplot(clean_data_1, aes(x = quantity, y = price)) +
  geom_point(color = "purple", alpha = 0.6) +
  ggtitle("Scatter Plot of Quantity vs Price (Cleaned Data)") +
  theme_minimal()

# Bar plot for 'gender' distribution after cleaning
ggplot(clean_data_1, aes(x = gender)) +
  geom_bar(fill = "lightcoral", color = "darkred") +
  ggtitle("Gender Distribution (Cleaned Data)") +
  theme_minimal()
