# Box Inventory Management App  
A Streamlit-based web application for efficiently managing and tracking items across multiple boxes, with features like adding, finding, viewing, and deleting items. The app is built using Python, PostgreSQL, and Streamlit, with seamless navigation and an intuitive UI.

# Features  
Add Items: Adding items to specific boxes.  
Find Items: Quickly locate items using simple search queries.  
View Items: See a complete list of stored items of a specified box number.  
Delete Items: Remove items when they’re no longer needed.  

# Technologies Used  
- Streamlit for the web interface  
- PostgreSQL as the database  
- Python for backend logic and integration  
- Psycopg2 for database connectivity  
- Neon.tech for database hosting  

# Future Enhancements 
- Exporting data to csv format
- Adding  tags and more features for categorization
- Improving the response time of the application 

# Folder structure
### Folder Structure  
```plaintext
📦 box-inventory-app  
 ┣ 📂 pages  
 ┃ ┣ 📄 1_Add_Item.py  
 ┃ ┣ 📄 2_Find_Item.py  
 ┃ ┣ 📄 3_View_Items.py  
 ┃ ┗ 📄 4_Delete_Item.py  
 ┣ 📄 Home.py  
 ┣ 📄 requirements.txt  
 ┣ 📄 runtime.txt
 ┗ 📄 README.md  
