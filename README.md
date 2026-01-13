# Late Show API

A Flask REST API for managing episodes, guests, and appearances on a late-night talk show.

## Features

- **Episodes**: Manage show episodes with dates and episode numbers
- **Guests**: Track guest information including names and occupations
- **Appearances**: Link guests to episodes with ratings (1-5 scale)
- **Relationships**: Many-to-many relationship between episodes and guests through appearances
- **Validations**: Rating validation ensures values are between 1 and 5

## Setup

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Late-show
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. Seed the database:
```bash
python seed.py
```

6. Run the application:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Episodes

#### GET /episodes
Retrieve all episodes.

**Response:**
```json
[
  {
    "id": 1,
    "date": "1/11/99",
    "number": 1
  },
  {
    "id": 2,
    "date": "1/12/99",
    "number": 2
  }
]
```

#### GET /episodes/:id
Retrieve a specific episode with its appearances.

**Response (Success):**
```json
{
  "id": 1,
  "date": "1/11/99",
  "number": 1,
  "appearances": [
    {
      "episode_id": 1,
      "guest": {
        "id": 1,
        "name": "Michael J. Fox",
        "occupation": "actor"
      },
      "guest_id": 1,
      "id": 1,
      "rating": 4
    }
  ]
}
```

**Response (Not Found):**
```json
{
  "error": "Episode not found"
}
```

### Guests

#### GET /guests
Retrieve all guests.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Michael J. Fox",
    "occupation": "actor"
  },
  {
    "id": 2,
    "name": "Sandra Bernhard",
    "occupation": "Comedian"
  }
]
```

### Appearances

#### POST /appearances
Create a new appearance linking a guest to an episode.

**Request Body:**
```json
{
  "rating": 5,
  "episode_id": 1,
  "guest_id": 2
}
```

**Response (Success):**
```json
{
  "id": 162,
  "rating": 5,
  "guest_id": 2,
  "episode_id": 1,
  "episode": {
    "date": "1/11/99",
    "id": 1,
    "number": 1
  },
  "guest": {
    "id": 2,
    "name": "Sandra Bernhard",
    "occupation": "Comedian"
  }
}
```

**Response (Validation Error):**
```json
{
  "errors": ["Rating must be between 1 and 5"]
}
```

## Database Schema

### Models

- **Episode**: `id`, `date`, `number`
- **Guest**: `id`, `name`, `occupation`
- **Appearance**: `id`, `rating`, `episode_id`, `guest_id`

### Relationships

- An Episode has many Guests through Appearances
- A Guest has many Episodes through Appearances
- An Appearance belongs to an Episode and a Guest
- Cascade deletes are configured for data integrity

## Testing

Use the provided Postman collection (`challenge-4-lateshow.postman_collection.json`) to test all endpoints:

1. Import the collection into Postman
2. Ensure the Flask app is running on `http://localhost:5000`
3. Run the requests to test functionality

## Validations

- **Appearance rating**: Must be between 1 and 5 (inclusive)
- **Foreign keys**: Episode and Guest must exist when creating an Appearance

## Technologies Used

- **Flask**: Web framework
- **SQLAlchemy**: ORM for database operations
- **Flask-Migrate**: Database migration management
- **SQLAlchemy-serializer**: JSON serialization for models
- **SQLite**: Database (development)

## Project Structure

```
Late-show/
├── app.py                 # Main Flask application
├── models.py              # Database models
├── seed.py                # Database seeding script
├── requirements.txt       # Python dependencies
├── challenge-4-lateshow.postman_collection.json  # API testing collection
└── README.md             # Project documentation
```