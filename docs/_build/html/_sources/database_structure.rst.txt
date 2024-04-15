*******************************************************
Description of the database structure and data models.
*******************************************************

This project uses the SQLite3 database to maintain a flexible and adaptive structure without excessive constraints. The database is structured with four distinct tables: letting, address, profile, and user.

**letting :**
- id
- title
- address_id (linked to the address table)

**address :**
- id
- number
- street
- city
- state
- zip_code
- country_iso_code

**profile :**
- id
- favorite_city
- user_id (linked to the user table)

**user :**
- id
- last_name
- date_joined
- is_active
- is_staff
- email
- first_name
- username
- is_superuser
- last_login
- password

These four tables are grouped into two models (with the user model managed by Django's authentication) as follows:

**Lettings :**
- letting
- address

**Profiles :**
- profile

Using these models, the application effectively handles and organizes rental and user data, streamlining information retrieval and manipulation.