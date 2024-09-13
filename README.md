# Project Name
## Description
The notification_app is a Python application that allows users to send and receive notifications.

## Installation
To install the notification_app, follow these steps:
1. Clone the repository: `git clone https://github.com/ezequielsalas/notification_app.git`
2. Navigate to the project directory: `cd notification_app`
3. Install the dependencies: `pip install -r requirements.txt`
4. Run migration `alembic upgrade head`

## Usage
To use the notification_app, follow these steps:
1. You can access to directly to the api at `http://127.0.0.1:8000/docs`
2. Also, you can clone the ui, and interact with the api with it at http://localhost:3000/

## Features
- Send notifications to users
- View a list of logs

## Configuration
The notification_app can be configured by modifying the `config.py` file. This file contains options for setting up the database connection, email server, and other settings.

## Contributing
Contributions to the notification_app are welcome. To contribute, please follow these guidelines:
- Fork the repository
- Create a new branch
- Make your changes
- Submit a pull request

## Authors
- Ezequiel Salas

## Roadmap
- Implement real-time notifications using websockets
- Add support for mobile push notifications, and other notifications

## Acknowledgements
- The FastAPI framework for web development
- The SQLAlchemy library for database management

## Changelog
### Version 1.0.0
- Initial release of the notification_app
- Added basic notification functionality
- Improved error handling
- Updated documentation
- Fixed minor bugs
