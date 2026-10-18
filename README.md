#  Music Database Application (Django)

A Django web application for viewing artists, music releases, and tracks, 
and for managing a favorites list (favorite artists and releases) in the user's personal account.

---

##  Key Features

* **Authentication and Profiles:**
  * Registration, login, and editing a user's profile.
  * A separate user dashboard (`UserProfileView`) displaying lists of favorite artists and releases.
* **Music Catalog:**
  * Browsing the list of artists (`Artists`) and releases (`Release`).
  * Filtering and browsing by genre (`Genre`) and tracks (`Tracks`).
* **Favorites:**
  * Toggling favorite status (checking and toggling via `toggle_favorite_releases` / `toggle_favorite_artists`).
  * Adding/removing artists and albums with a single click, with automatic redirection.
* **Query Optimization (ORMs Optimization):**
  * Using `select_related` for `ForeignKey` relationships and `prefetch_related` for `ManyToManyField` relationships (reducing the N+1 problem).
  * Custom QuerySet managers (e.g., `ReleaseQuerySet.published_with_relations()`).

---

##  Technology Stack

* **Backend:** Python 3.14+, Django 6.1+
* **Database:** PostgreSQL / SQLite
* **Frontend:** HTML5, CSS3, Bootstrap / Tailwind (HTML-templates Django)
* **IDE / Tools:** PyCharm, pgAdmin 4

---

##  Model Structure (Key Relationships)

### `User` (`users.User`)
* `favorite_artists` — `ManyToManyField("artists.Artists", blank=True)`
* `favorite_releases` — `ManyToManyField("artists.Release", blank=True)`

### `Artists` (`artists.Artists`)
* `name` — `CharField`
* `slug` — `SlugField` (unique identifier)
* `genre` — `ManyToManyField(Genre)`

### `Release` (`artists.Release`)
* `release_name` — `CharField`
* `slug` — `SlugField`
* `artists` — `ForeignKey(Artists)`
* `genres` — `ManyToManyField(Genre)`
* `tracks` — `ManyToManyField(Track)`

---

##  Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MyDevilCry/music_data_base.git
   cd music_data_base
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (administrator):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

---

## 🔒 Security and Access Rights

* **Class-Based Views (CBV):** Protected using `LoginRequiredMixin`.
* **Function-Based Views (FBV):** Protected using the `@login_required` decorator.
