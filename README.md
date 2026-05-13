# Cyber Security Base Project 1

A deliberately vulnerable Django web application demonstrating 5+ security flaws from the OWASP Top 10 (2021) list, with commented-out fixes for educational purposes.

## OWASP Version Used

This project uses the **OWASP Top 10 2021** list.

## Vulnerabilities Demonstrated

### 1. A03:2021 – Injection (SQL Injection)
**Location:** `accounts/views.py` - `login_view()` function
- **Flaw:** User credentials are concatenated directly into SQL query without parameterization
- **Impact:** Attacker can bypass authentication or extract database data
- **Fix:** Use Django ORM's `authenticate()` function (commented in code)

### 2. A07:2021 – Identification and Authentication Failures (Weak Password Policy)
**Location:** `accounts/views.py` - `register_view()` function
- **Flaw:** Password validation function is commented out; no minimum requirements enforced
- **Impact:** Users can create weak passwords like "123"
- **Fix:** Uncomment the `is_at_least_decent_password()` validation

### 3. A07:2021 – Identification and Authentication Failures (Plaintext Password Storage)
**Location:** `accounts/views.py` - `register_view()` function
- **Flaw:** Uses `User.objects.create()` instead of `User.objects.create_user()`, storing passwords unhashed
- **Impact:** Compromised database leaks all user passwords in plaintext
- **Fix:** Use `User.objects.create_user()` (commented in code)

### 4. A01:2021 – Broken Access Control (CSRF)
**Location:** `accounts/views.py` - `home_view()` function
- **Flaw:** `@csrf_exempt` decorator disables CSRF protection
- **Impact:** Attacker can force authenticated users to perform unwanted actions
- **Fix:** Remove the `@csrf_exempt` decorator and include CSRF token in forms

### 5. A03:2021 – Injection (Stored XSS - Cross-Site Scripting)
**Location:** `accounts/views.py` - `home_view()` function and `accounts/templates/home.html`
- **Flaw:** User content is stored without sanitization and rendered with `|safe` template filter
- **Impact:** Attacker can inject malicious JavaScript that executes in other users' browsers
- **Fix:** Remove `|safe` filter or use `django.utils.html.escape()`

### 6. A01:2021 – Broken Access Control (IDOR - Insecure Direct Object Reference)
**Location:** `accounts/views.py` - `delete_post_view()` function
- **Flaw:** Any logged-in user can delete any post by modifying the post ID in the URL
- **Impact:** Data loss and unauthorized modification of other users' content
- **Fix:** Add check `post = Post.objects.get(id=post_id, user=request.user)` (commented in code)

---

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Linux & macOS

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kimtakala/CyberSecurityBaseProject1.git
   cd CyberSecurityBaseProject1
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open `http://127.0.0.1:8000/` in your browser

### Windows

1. **Clone the repository:**
   ```cmd
   git clone https://github.com/kimtakala/CyberSecurityBaseProject1.git
   cd CyberSecurityBaseProject1
   ```

2. **Create a virtual environment:**
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```cmd
   python manage.py migrate
   ```

5. **Start the development server:**
   ```cmd
   python manage.py runserver
   ```

6. **Access the application:**
   Open `http://127.0.0.1:8000/` in your browser

---

## How to Test Each Vulnerability

### Testing Flaw 1: SQL Injection
1. Navigate to `/login/`
2. In the username field, enter: `admin' OR '1'='1`
3. Leave password blank
4. You may be able to bypass authentication
5. **Expected result:** Access granted despite invalid credentials

### Testing Flaw 2: Weak Password Policy
1. Navigate to `/register/`
2. Create an account with username: `testuser` and password: `123`
3. The system accepts the weak password
4. **Expected result:** Account created without password strength validation

### Testing Flaw 3: Plaintext Password Storage
1. Access the Django admin panel at `/admin/`
2. Use credentials to view stored users
3. Check the database directly with SQLite browser or Django shell
4. **Expected result:** Passwords are stored as plain text, not hashed

### Testing Flaw 4: CSRF
1. Log in to the application
2. Create an HTML file on another domain with:
   ```html
   <form action="http://127.0.0.1:8000/home/" method="POST">
     <input type="hidden" name="content" value="Hacked post">
     <input type="submit">
   </form>
   ```
3. Open this file while logged into the vulnerable app
4. Submit the form
5. **Expected result:** Post is created without CSRF token validation

### Testing Flaw 5: Stored XSS
1. Create a post with content: `<script>alert('XSS')</script>`
2. Refresh the page or have another user view your post
3. **Expected result:** JavaScript executes, showing an alert

### Testing Flaw 6: IDOR
1. Log in and create a post
2. Note the post ID from the delete button URL
3. Try to delete another user's post by changing the post ID in the URL
4. **Expected result:** You can delete posts that don't belong to you

---

## Project Structure

```
CyberSecurityBaseProject1/
├── accounts/
│   ├── migrations/          # Database migrations
│   ├── templates/
│   │   ├── home.html        # Main page with posts
│   │   ├── login.html       # Login form
│   │   └── register.html    # Registration form
│   ├── models.py            # Post and User models
│   ├── views.py             # Views with vulnerabilities
│   ├── urls.py              # URL routing
│   └── admin.py             # Admin configuration
├── projekti/                # Django project settings
├── screenshots/             # Before/after vulnerability screenshots
├── manage.py                # Django management script
└── README.md                # This file
```

---

## Notes

- All vulnerabilities are **intentional and educational**
- Fixes are provided as **commented code** to prevent accidental enabling
- **DO NOT use this code in production**
- Screenshots documenting each flaw are included in the `screenshots/` folder
- The application uses Django's built-in SQLite database for simplicity

---

## Disclaimer

This project is for educational purposes only as part of the Cyber Security Base course. It intentionally contains security vulnerabilities. Never deploy this code in production environments.
