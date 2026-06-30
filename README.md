# GourmetHub

GourmetHub is a Django food ordering and analytics platform. Customers can create accounts, browse menu items, place orders, review totals, and view ordering insights. Administrators can manage menu data and inspect aggregate demand through Chart.js dashboards.

## Features

- User registration and authentication
- Dynamic menu backed by Django models
- Quantity selection and order summaries
- Automatic order-total calculation
- Customer-specific ordering dashboard
- Platform-wide analytics dashboard
- Django admin integration for menu and order management

## Technology stack

- Python and Django
- SQLite and Django ORM
- HTML and CSS
- Chart.js

## Data model

- `MenuItem` stores each dish, description, price, and image.
- `OrderList` connects a customer to a menu item, quantity, and calculated total.

## Run locally

```bash
git clone https://github.com/Virajpoolabhavi/GourmetHub-Integrated-Food-Order-and-Analytics-platform.git
cd GourmetHub-Integrated-Food-Order-and-Analytics-platform
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and provide a strong Django secret. Export the variables for your shell, then initialize the application:

```bash
cd order
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Security

- Secrets and email credentials are loaded from environment variables.
- `DEBUG` is disabled by default.
- Never commit a populated `.env` file.

## Future improvements

- Add automated tests for authentication, ordering, totals, and permissions
- Replace hard-coded dashboard categories with database aggregation
- Add order lifecycle states and payment integration
- Deploy a live demonstration with production settings

## Author

Built by [Viraj Poolabhavi](https://github.com/Virajpoolabhavi).
