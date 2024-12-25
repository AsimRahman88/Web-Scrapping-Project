# **Web Scraping Adventure**

## **Description**
This project implements a Python-based web scraping application designed to extract and analyze deal data from `https://forums.redflagdeals.com/hot-deals-f9/`. The application provides users with a menu-driven interface to interact with the data and offers functionalities such as displaying the latest deals, analyzing deals by category, identifying top stores, and logging specific deal information.

The project showcases expertise in Python programming, including concepts such as:
- Object-Oriented Programming (OOP)
- File handling
- Web scraping using `requests` and `BeautifulSoup`
- Data organization using dictionaries and lists
- Error handling for user input and file operations

---

## **Features**
### **1. Display Latest Deals**
- Scrapes the latest deals and displays them in a formatted structure.
- Each deal includes:
  - Store name
  - Item description
  - Votes
  - Username
  - Timestamp
  - Category
  - Replies
  - Views
  - URL
- Outputs:
  - Total number of deals found
  - Details for each deal

### **2. Analyze Deals by Category**
- Categorizes deals and calculates the total number of deals in each category.
- Displays a sorted list of categories with their respective deal counts in descending order.

### **3. Find Top Stores**
- Allows users to specify the number of top stores to display.
- Identifies stores with the highest number of deals and displays them with their deal counts.

### **4. Log Deal Information**
- Displays a list of available categories.
- Prompts the user to select a category and logs all the deal links under the chosen category into a `log.txt` file.

### **5. Exit**
- Terminates the application gracefully, ensuring all resources are released.

---

## **Technical Details**
### **Programming Language**
- **Python**: Showcasing proficiency in object-oriented programming, file operations, and error handling.

### **Libraries Used**
- `requests`: For sending HTTP requests to fetch website content.
- `BeautifulSoup` (from `bs4`): For parsing HTML and extracting structured data.

### **Implementation Highlights**
- **Object-Oriented Design**: Encapsulated functionalities within a class (`choice`) for modular and reusable code.
- **Web Scraping**: Implemented using `requests` and `BeautifulSoup` to extract data from the target website.
- **File Operations**: Includes reading, writing, and error handling for `log.txt`.
- **Dynamic Data Storage**: Leveraged dictionaries and lists to organize and process scraped data.
- **User Input Validation**: Ensured robust handling of user input with clear prompts and error messages.

---

## **How to Run the Program**
1. **Prerequisites**:
   - Install required Python libraries:
     ```bash
     pip install requests beautifulsoup4
     ```

2. **Run the Program**:
   - Execute the `driver.py` script to launch the application:
     ```bash
     python driver.py
     ```

3. **Interact with the Menu**:
   - Choose from the following options:
     - **1**: Display the latest deals.
     - **2**: Analyze deals by category.
     - **3**: Find top stores.
     - **4**: Log deal information into a file.
     - **5**: Exit the application.

---

## **Key Learnings**
### **Python Programming Skills**
- **Object-Oriented Programming (OOP)**:
  - Designed modular classes to handle menu options and data processing.
  - Encapsulated functionalities like displaying deals and analyzing data.
- **Web Scraping**:
  - Implemented efficient scraping techniques using `requests` and `BeautifulSoup`.
  - Extracted and organized complex data from HTML elements.
- **File Handling**:
  - Implemented robust file read/write operations with error handling.
  - Ensured data persistence by logging links into `log.txt`.
- **Data Manipulation**:
  - Organized scraped data using dictionaries and lists for efficient processing.
  - Performed sorting and filtering operations on data.

### **Additional Knowledge**
- **Error Handling**:
  - Validated user inputs to ensure program stability.
  - Included fallback mechanisms for invalid inputs and file operation errors.
- **Python Best Practices**:
  - Adopted clean coding standards, including docstrings and inline comments.
  - Followed the Zen of Python's principle: "Readability counts."

---

## **Project Structure**
### **Files**
- `driver.py`: Contains the main program logic and menu system.
- `options.py`: Includes methods for scraping data and performing operations on it.
- `log.txt`: Output file for storing logged deal information (created dynamically).

### **Functions Overview**
#### **driver.py**
- **`main()`**: Manages the main menu and handles user input to invoke functionalities from `options.py`.

#### **options.py**
- **`LatestDeals()`**: Scrapes the latest deals and organizes them into lists.
- **`DisplayLatestDeals()`**: Displays the total deals and their details in a formatted manner.
- **`AnalyzeDealsByCategory()`**: Categorizes deals and calculates their counts.
- **`topStores(nb)`**: Displays the top `nb` stores with the highest number of deals.
- **`logDealInfo()`**: Logs deal URLs of a selected category into `log.txt`.

---

## **Sample Output**
```plaintext
***** Web Scraping Adventure *****
1. Display Latest Deals
2. Analyze Deals by Category
3. Find Top Stores
4. Log Deal Information
5. Exit
Enter your choice (1-5): 1

Total deals found: 55

store: No Frills
item: Swanson Oven Easy Meals or Family Skillets $1.88 (reg. $11.49) with printed coupon
votes: +56
username: hill15
timestamp: Feb 13th, 2024 3:25 pm
category: Groceries
replies: 65
views: 10,817
url: https://forums.redflagdeals.com/no-frills-swanson-oven-easy-meals-family-skillets
-----------------------------------------
