#step 1:Read the provided CSV file into R using read.csv().
library(ggplot2)
library(dplyr)

df <- read.csv(file.choose(), stringsAsFactors = FALSE)

#step 2:Inspect the first few rows of the dataset as well as the structure of the dataset.
str(df)
head(df)

#step 3:Select the rows where exports exceed 200,000.
high_export_data <- df %>% filter(Exports > 200000)

#step 4:Add a new column that calculates the trade balance (exports - imports).
df <- df %>% mutate(Trade_Balance = Exports - Imports)

#step 5:Create a line plot to visualize the trade balance over time using ggplot2
plot <- ggplot(df, aes(x = Year, y = Trade_Balance)) +
  geom_line(color = "blue", size = 1) +
  labs(
    title = "Trade Balance Over Time",
    x = "Year",
    y = "Trade Balance (Exports - Imports)"
  ) +
  theme_minimal()
print(plot)


