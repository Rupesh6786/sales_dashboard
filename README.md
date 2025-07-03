
# 📊 Sales Analysis Dashboard using Tkinter & Pandas

A user-friendly, interactive **Sales Dashboard application** built with **Python (Tkinter)** for GUI and **Pandas** for data analysis. It enables users to visualize, filter, and interact with car sales data efficiently through dynamic charts, tables, and filters.

---

## 🚀 Features

- 📁 Upload custom sales datasets (CSV)
- 📈 Interactive charts: total revenue, monthly trends, and more
- 🔍 Smart filtering by brand, location, salesperson, etc.
- 📊 Tabular view with sorting and search functionality
- 🧠 Backend powered by Pandas for real-time data manipulation
- 📐 Modular and scalable project structure
- 👨‍💼 Perfect for business analysts, sales managers, and students

---

## 🖼️ Dashboard Preview

### 📊 Dashboard Overview  
![Dashboard](sale_dashboard_images/1_dashboard_overview.png)

### 📈 Sales Graph  
![Sales Graph](sale_dashboard_images/2_sales_chart.png)

### 📋 Product Table  
![Product Table](sale_dashboard_images/3_product_table.png)

### 🎛️ Filter and Sorting  
![Filters](sale_dashboard_images/4_filters_sorting.png)

### 🗂️ CSV Upload View  
![Upload](sale_dashboard_images/5_data_upload.png)

---

## 🛠️ Technologies Used

- **Language**: Python 3.x  
- **GUI**: Tkinter  
- **Data Analysis**: Pandas  
- **Visualization**: Matplotlib / Seaborn  
- **Others**: CSV, Custom styling with `ttk`

---

## 📂 Folder Structure

```
📦 SalesDashboard
├── gui/
│   ├── header.py
│   ├── sidebar.py
│   └── dashboard.py
├── logic/
│   ├── data_loader.py
│   └── filters.py
├── assets/
│   └── logo.png
├── car_sales_dataset.csv
├── main.py
└── README.md
```

---

## 📁 Dataset Format (CSV)

Ensure your CSV file has the following columns:

| Column          | Description                            |
|-----------------|----------------------------------------|
| Sale_ID         | Unique sale transaction ID             |
| Date            | Date of sale                           |
| Customer_Name   | Name of the customer                   |
| Car_Brand       | Brand of the car (e.g., Toyota)        |
| Car_Model       | Specific model (e.g., Camry)           |
| Year            | Year of manufacture                    |
| Fuel_Type       | Petrol, Diesel, Electric, etc.         |
| Transmission    | Manual / Automatic                     |
| Selling_Price   | Final sale amount                      |
| Cost_Price      | Cost to the dealer                     |
| Profit          | Calculated profit (Selling - Cost)     |
| Location        | Sale city                              |
| Sales_Person    | Who sold the car                       |

> ✔️ Sample file included: `car_sales_dataset.csv`

---

## 💻 How to Run

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/sales-dashboard.git
   cd sales-dashboard
   ```

2. **Install required libraries**:
   ```bash
   pip install pandas matplotlib
   ```

3. **Run the app**:
   ```bash
   python main.py
   ```

4. **Upload a CSV**, view analysis, and filter data dynamically.

---

## 💬 Future Enhancements

- Export filtered data to Excel or PDF  
- Add pie charts & advanced analytics  
- Integration with SQLite or Firebase  
- Web version using Flask/Django  

---

## 👨‍💻 Author

**Rupesh H. Thakur**  
🎓 BSc.IT Student, Thakur College of Science and Commerce  
🔗 [GitHub – @Rupesh6786](https://github.com/Rupesh6786)  
📧 Email: 55rupeshthakur@gmail.com  

---

## 📄 License

Licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more info.

---

> Turning raw car sales data into smart visual insights.
