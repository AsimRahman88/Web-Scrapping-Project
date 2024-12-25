import requests
from bs4 import BeautifulSoup

#different list initialized for later use
storeList = []
itemList = []
votesList = []
usernameList = []
timestampList = []
categoryList = []
repliesList = []
viewsList = []
urlList =[]
dealsDetail = {}

#from the sample
def get_store(listing):
        """
        Extracts the store name from the given listing.

        Parameters:
        - listing (BeautifulSoup): The BeautifulSoup object representing a deal listing.

        Returns:
        - str: The extracted store name.
        """
        store_element_retailer = listing.select_one('.topictitle_retailer')
        store_element = listing.select_one('.topictitle')

        if store_element_retailer:
            return store_element_retailer.text.strip()
        elif store_element:
            # Extract store from the square brackets, if available
            store_text = store_element.text.strip()
            return store_text.split(']')[0][1:].strip() if ']' in store_text else store_text
        else:
            return "N/A"

response = requests.get("https://forums.redflagdeals.com/hot-deals-f9/")

soup = BeautifulSoup(response.text, 'html.parser')

# the majority is from the sample, but with the modification to append each elements of a list
def LatestDeals():
        #clear the list so that every time the method is called, the list is not appended from the last time the method was called.
        storeList.clear()
        itemList.clear()
        votesList.clear()
        usernameList.clear()
        timestampList.clear()
        categoryList.clear()
        repliesList.clear()
        viewsList.clear()
        urlList.clear()
        
        

        for listing in soup.find_all("li", class_="row topic"):

            store = get_store(listing)
            storeList.append(store) #add the store in the list
            
    
            item_element = listing.select_one('.topic_title_link')
            item = item_element.text.strip() if item_element else "N/A"
            itemList.append(item) #add the item in the list
            

            votes_element = listing.select_one('.total_count_selector')
            votes = votes_element.text.strip() if votes_element else "N/A"
            votesList.append(votes) #add the votes in the list
            

            username_element = listing.select_one('.thread_meta_author')
            username = username_element.text.strip() if username_element else "N/A"
            usernameList.append(username) #add the username in the list
            

            timestamp_element = listing.select_one('.first-post-time')
            timestamp = timestamp_element.text.strip() if timestamp_element else "N/A"
            timestampList.append(timestamp) #add the time in the list
            

            category_element = listing.select_one('.thread_category a')
            category = category_element.text.strip() if category_element else "N/A"
            categoryList.append(category) #add the category in the list
            

            replies_element = listing.select_one('.posts')
            replies = replies_element.text.strip() if replies_element else "N/A"
            repliesList.append(replies) #add the replies in the list
            

            views_element = listing.select_one('.views')
            views = views_element.text.strip() if views_element else "N/A"
            viewsList.append(views) # add the views on the list
            

            # Example: Extracting information from HTML elements
            # Base URL
            base_url = "https://forums.redflagdeals.com/"
    
            # Extract the URL and prepend the base URL
            url_element = item_element['href'] if item_element else "N/A"
            url = base_url + url_element
            urlList.append(url) #add the url in the list
            
        
#class choice that has a methods for option 1 to 4
class choice:
    #default constructor
    def __init__(self):
        print()  

    #method for option 1
    def DisplayLatestDeals(self):
        LatestDeals()  #add every element into the corresponding list
        #dealsDetail dictionary that has all the lists appended from latestDeals() method as values
        dealsDetail = {"store" : storeList, "item" : itemList, "votes" : votesList, "username" : usernameList, "timestamp" : timestampList, "category" : categoryList, "replies" : repliesList, "views" : viewsList}
        totalDeals = len(storeList) #totalDeals is the lenght of any list(we chose storelist, but it could have been the other lists as well)
        print(f"total deals found: {totalDeals}") #print the number of deals
        print()
        for i in range(totalDeals): #nested for loop where the outer loop is for each deal 
            for key, value in dealsDetail.items(): #and the inner loop is for every element of the deal such as the item, the store and so on
                print(f"{key}: {value[i]}")
            print("-----------------------------------------")

    #method for option2
    def AnalyzeDealsByCategory(self):
        LatestDeals() #add every element into the corresponding list
        #dealsDetail dictionary that has all the lists appended from latestDeals() method as values 
        dealsDetail = {"store" : storeList, "item" : itemList, "votes" : votesList, "username" : usernameList, "timestamp" : timestampList, "category" : categoryList, "replies" : repliesList, "views" : viewsList}
        totalDeals = len(storeList) #totalDeals is the lenght of any list(we chose storelist, but it could have been the other lists as well)
        nbDeals=0
        categoryDict ={}
        for i in range(totalDeals): #nested for loop where the outer loop takes a category from the list 
            # Initialize nbDeals for each category
            nbDeals = 0
            for j in range(totalDeals): #the inner loop checks how many times the category(taken from the outer loop) occurs(or matches) in the list so we know how many deals there are for a specific category
                if categoryList[i] == categoryList[j]:
                    nbDeals += 1
            # The outer loop also assigns the total number of deals for the category to the dictionary 
            # because there is no duplicates for dictionay keys, so each category occur onces, 
            # but its values on the other hand, increments each time for the number of deals
            categoryDict[categoryList[i]] = nbDeals
        
        # Sorting the dictionary items based on values in decreasing order
        sorted_items = sorted(categoryDict.items(), key=lambda x: x[1], reverse=True)

        print("Deals by Category:")
        print()
        # Printing the sorted items
        for key, value in sorted_items:
            print(f"{key}: {value} deals")
    
    #method for option3 where nb is the number entered by the user for the number of top stores
    def topStores(self, nb):
        LatestDeals() #add every element into the corresponding list
        #dealsDetail dictionary that has all the lists appended from latestDeals() method as values 
        dealsDetail = {"store" : storeList, "item" : itemList, "votes" : votesList, "username" : usernameList, "timestamp" : timestampList, "category" : categoryList, "replies" : repliesList, "views" : viewsList}
        totalDeals = len(storeList) #totalDeals is the lenght of any list(we chose storelist, but it could have been the other lists as well)
        nbDeals=0
        storeDict ={}
        for i in range(totalDeals):#nested for loop where the outer loop takes a store from the list 
             # Initialize nbDeals for each store
            nbDeals = 0
            for j in range(totalDeals): #the inner loop checks how many times the store(taken from the outer loop) occurs(or matches) in the list so we know how many deals there are for a specific store
                if storeList[i] == storeList[j]:
                    nbDeals += 1
            
            # The outer loop also assigns the total number of deals for the store to the dictionary 
            # because there is no duplicates for dictionay keys, so each store occur onces, 
            # but its values on the other hand, increments each time for the number of deals
            storeDict[storeList[i]] = nbDeals
        
        # Sorting the dictionary items based on values in decreasing order
        sorted_items = sorted(storeDict.items(), key=lambda x: x[1], reverse=True)
        
        print("Top Stores:")
        print()
        # Printing the sorted items
        for key, value in sorted_items[:nb]:
            print(f"{key}: {value} deals")

    #method for option4
    def logDealInfo(self):
        LatestDeals() #add every element into the corresponding list
        #dealsDetail dictionary that has all the lists appended from latestDeals() method as values 
        dealsDetail = {"store" : storeList, "item" : itemList, "votes" : votesList, "username" : usernameList, "timestamp" : timestampList, "category" : categoryList, "replies" : repliesList, "views" : viewsList}
        totalDeals = len(storeList) #totalDeals is the lenght of any list(we chose storelist, but it could have been the other lists as well)
        nbDeals=0
        #f = open("log.txt", "w") # variable to write to log.txt

        categoryDict ={}
        for i in range(totalDeals): #for loop to put every category in the dictionary 
            categoryDict[categoryList[i]] = 1 #since there are no duplicates in the keys of dictionary (random element as value)

        keys_list = list(categoryDict.keys()) #make the category keys as a list

        list_index = 0
        count = 1
        for j in range(len(keys_list)): #use for loop to print every category present
            print(f"{count}. {keys_list[list_index]}")
            list_index += 1
            count += 1
        
        
        valid_category=0 #variable to know if we repeat the while loop
        found_category = False
        while(valid_category==0):
            user_category_nb = input("Enter the number corresponding to the category: ")
            if user_category_nb.isdigit() and 1 <= int(user_category_nb) <= len(keys_list):
                category_nb = int(user_category_nb)
                index=0
                try:
                    with open("log.txt", "w") as f:
                        for i in categoryList: #for loop to see if the number entered(-1 since the index of a list starts at 0) by the user matches with an element of an index of the category list
                            if(categoryList[index]==keys_list[category_nb-1]):
                                f.write(f"{urlList[index]}\n")
                            index += 1
                except IOError as e:
                    print(f"Error: {e}")

                print("All the links have been logged successfully.")
                valid_category=1 #right user input
            else:
                max_category=len(keys_list)
                print(f"Invalid choice. Please enter a number between 1 and {max_category}.")
                valid_category=0 #wrong user input
        
        f.close()
        

          
        
        





    
