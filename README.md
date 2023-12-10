# New Russian Wine
This project is created to display a web page with information about a winery and its products.
## Installation and Setup Instructions
### Step 1: Clone the Repository

```bash
git clone https://github.com/barseeek/wine.git
cd repository
```
### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 3: Fill in the excel template with your data
1. Open the `wine_template.xlsx` file in a spreadsheet program such as Microsoft Excel or Google Sheets.

2. Enter the product data into their respective columns:
   
   - **Категория**: Specify the product category (e.g., White Wines, Beverages, Red Wines).
   - **Название**: Enter the product name.
   - **Сорт**: Provide the variety of the product, if applicable.
   - **Цена**: Enter the product price.
   - **Картинка**: If available, indicate the image file name for the product, images are stored in the `images/` folder.
   - **Акция**: If there's a special offer, provide information about it; otherwise, leave the field blank.

3. Save the excel file after entering all the necessary product details.

### Step 4: Run script
Specify the Excel file name as a parameter, by default `wine_template.xlsx` will be used
```bash
python main.py excel_filename
```
### Step 5: Open Site

Open browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Project Goals
The code is written for educational purposes - it's a lesson in a course on Python and web development at [Devman](https://dvmn.org).