import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# List of topics
topics = [
    # Technology & Programming
    "Artificial Intelligence", "Machine Learning", "Deep Learning", "Neural Networks",
    "Natural Language Processing", "Computer Vision", "Cloud Computing", "DevOps",
    "Kubernetes", "Docker", "Python programming", "C# .NET", "Java programming",
    "Cybersecurity", "Data Science", "Big Data", "Blockchain", "Internet of Things",
    "Quantum Computing", "5G Technology", "Virtual Reality", "Augmented Reality",
    "Edge Computing", "ChatGPT", "GitHub", "Git vs SVN", "Jenkins CI/CD",
    "Linux Administration", "Red Hat Enterprise Linux", "Windows Server",
    "Networking basics", "Ansible Automation", "Terraform IaC",
    "Agile vs DevOps", "CI/CD best practices", "Cloud Security",
    
    # Science & Space
    "Black Holes", "Space Exploration", "NASA Artemis mission", "Mars colonization",
    "Exoplanets", "String Theory", "Dark Matter", "Relativity theory",
    "Climate Change", "Renewable Energy", "Nuclear Fusion", "Genetic Engineering",
    "Human Brain", "Evolution of species", "CRISPR technology", "Nanotechnology",

    # History & Culture
    "Ancient Egypt", "Roman Empire", "World War I", "World War II",
    "Cold War", "Industrial Revolution", "French Revolution", "American Civil War",
    "History of Mathematics", "History of Computers", "Philosophy of Aristotle",
    "Islamic Golden Age", "Renaissance Art", "Shakespeare works",
    
    # General Knowledge
    "Best programming languages in 2025", "Future of jobs with AI",
    "Digital Marketing strategies", "E-commerce trends", "Stock Market basics",
    "Personal Finance tips", "Best productivity tools", "Mindfulness techniques",
    "Psychology of learning", "Habits of successful people"
]


# Number of searches
num_searches = 30  

# Delay between typing/searching
delay_seconds = 10

# Pick random topics
chosen_topics = random.sample(topics, num_searches)

# Start Microsoft Edge with Selenium
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)

for i, topic in enumerate(chosen_topics):
    if i > 0:
        # Open a new tab
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
    
    # Go to Bing homepage
    driver.get("https://www.bing.com")

    # Wait for page
    time.sleep(2)

    # Find the search box and type the query
    search_box = driver.find_element("name", "q")
    search_box.send_keys(topic)
    search_box.send_keys(Keys.RETURN)

    print(f"Searched: {topic}")
    
    # Wait before next search
    time.sleep(delay_seconds)
