# this is where I do the graphing for my assignment basics

# this is where I do the graphing for my assignment basics

# imports matplotlib and functions from
import matplotlib.pyplot as plt
from calculations import get_data, grade_distribution

def plot_grade_distribution():
    df = get_data()
    counts = grade_distribution(df)

    # order by grade name
    order = ['A', 'B', 'C', 'Fail']
    counts = counts.reindex(order)

    # Bar chart
    counts.plot(kind='bar', color=['green','orange','blue','red'])
    plt.title("Grade Distribution")
    plt.xlabel("Grade Band")
    plt.ylabel("Number of Students")
    plt.show()

def plot_grade_distribution_pie():
    df = get_data()
    counts = grade_distribution(df)
    counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Grade Distribution")
    plt.ylabel("")  # hide y-label
    plt.show()

if __name__ == "__main__":
    plot_grade_distribution()
    plot_grade_distribution_pie()