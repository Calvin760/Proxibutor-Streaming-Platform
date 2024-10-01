# Proxibutor-Streaming-Platform
#### Video Demo:  [<URL HERE>](https://youtu.be/X7KHHDxyCqY)
#### Music distribution and streaming service

The Music Release Platform is a web application designed to facilitate independent artists in managing their music releases, promoting their work and streaming other artist from the labe's music. This platform allows users to register, log in, and create artist profiles, as well as upload and manage music releases. By integrating functionalities like user authentication, file uploads, and a dynamic music library, this application serves as a comprehensive tool for artists to showcase their talent. Built with Django, the platform leverages a robust framework for rapid development and scalability, ensuring that it can grow alongside its users.

Key Features
User Authentication: Users can create accounts, log in, and manage their profiles. Secure password management features, such as password changes, enhance user safety.
Artist Profiles: Artists can create and update profiles with essential details, including stage name, biography, and images.
Music Releases: Users can upload music files along with metadata such as title, release date, and genre. The platform ensures that no duplicate releases are created for the same artist and title.
Dynamic Search: Users can search through a music collection, filtering by song title or artist to quickly find specific releases.
Responsive Design: The application is designed to be user-friendly and accessible, with a responsive layout suitable for various devices.
File Structure and Functionality
1. Django Project Setup
The project follows the standard Django structure, organized into apps that handle different functionalities. The main app, responsible for core features, contains the following files:

2. Models (models.py)
Artist Model: This model represents an artist and includes fields for their stage name, header image, profile picture, and biography. The __str__ method returns the artist's stage name, making it easy to identify instances in the admin interface.

Music Model: This model stores information about music releases. It includes fields for user references, UUIDs for unique identification, song titles, associated artists, featured artists, release dates, cover art, and song files. The Meta class specifies ordering by release date and enforces a unique constraint on the combination of title and artist. The model also includes a utility method to fetch a list of featured artists.

3. Views (views.py)
The views handle the business logic of the application and include:

Authentication Views: Functions for user registration, login, and logout manage user sessions and provide feedback through messages. Security features include validating user inputs to prevent unauthorized access.

Artist and Music Management: Views for creating and updating artist profiles, as well as releasing music. These views handle file uploads, validate data, and ensure the integrity of relationships between artists and their music.

Collection and Search: A view for displaying a searchable list of music releases, allowing users to filter results based on specific queries. This functionality enhances user experience by making navigation intuitive.

4. Templates (templates/)
The project utilizes Django’s templating engine to render HTML pages dynamically. Key templates include:

Base Template: Provides a consistent layout and styling across all pages, including a navigation bar and footer.

User Interfaces: Separate templates for login, registration, artist profiles, and music releases guide users through the functionalities of the platform, providing forms for input and displaying messages.

5. Static Files (static/)
Static files include CSS, JavaScript, and images, ensuring that the application has a visually appealing and interactive interface. Custom styles enhance usability, while responsive design principles ensure accessibility across devices.

Design Choices and Considerations
1. Framework Selection
Django was chosen as the web framework due to its comprehensive feature set, including built-in user authentication, an ORM for database management, and a robust admin interface for managing application data. This framework accelerates development while maintaining high standards of security and scalability.

2. User-Centric Features
Incorporating user authentication and artist profiles was crucial for creating a personalized experience. Allowing users to manage their releases and profiles helps establish a sense of ownership over their work. The decision to implement features like password recovery and session management reflects a commitment to user security and satisfaction.

3. Data Integrity
To maintain data integrity, unique constraints on music releases ensure that no two songs by the same artist can share the same title. This decision helps prevent confusion and ensures that users can easily manage and locate their work.

4. Responsive Design
Recognizing the diversity of devices used to access the platform, responsive design principles were employed. This approach ensures that the user experience remains consistent across smartphones, tablets, and desktops, maximizing accessibility for all users.
