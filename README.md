# Vendor Management System API

## Overview
The Vendor Management System API provides endpoints to manage vendors, track purchase orders, and evaluate vendor performance metrics.

## Setup Instructions
1. **Clone the Repository:**
git clone https://github.com/your-username/vendor-management-system.git
cd vendor-management-system

2. **Install Dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Database Setup:**
- Ensure you have PostgreSQL installed and running.
- Update the database settings in `settings.py` with your PostgreSQL credentials.
- Run migrations:
  ```
  python manage.py migrate
  ```

4. **Run the Development Server:**
    ```
    python manage.py runserver
    ```


## API Endpoints
- **Vendor Management:**
- `POST /api/vendors/`: Create a new vendor.
- `GET /api/vendors/`: List all vendors.
- `GET /api/vendors/{vendor_id}/`: Retrieve details of a specific vendor.
- `PUT /api/vendors/{vendor_id}/`: Update a vendor's details.
- `DELETE /api/vendors/{vendor_id}/`: Delete a vendor.

- **Purchase Order Tracking:**
- `POST /api/purchase_orders/`: Create a purchase order.
- `GET /api/purchase_orders/`: List all purchase orders.
- `GET /api/purchase_orders/{po_id}/`: Retrieve details of a specific purchase order.
- `PUT /api/purchase_orders/{po_id}/`: Update a purchase order.
- `DELETE /api/purchase_orders/{po_id}/`: Delete a purchase order.

- **Vendor Performance Evaluation:**
- `GET /api/vendors/{vendor_id}/performance/`: Retrieve performance metrics for a vendor.


## Contributing
Contributions are welcome! Please fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
