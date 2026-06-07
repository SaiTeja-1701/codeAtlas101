
# Architecture Overview
The project follows the MVC architecture, which separates the application logic into three interconnected components:
* **Model**: Represents the data and business logic of the application
* **View**: Represents the user interface of the application
* **Controller**: Represents the interaction between the model and view

## Architecture Diagram
```mermaid
graph LR
    A[Model] -->|Database Query|> B[Controller]
    B -->|Business Logic|> A
    B -->|Render|> C[View]
    C -->|User Interaction|> B
```
The model represents the data and business logic of the application, while the controller interacts with the model and view to handle user input and render the user interface.

### Important Routes
The project has the following important routes:
* **/login**: Handles user login
* **/register**: Handles user registration
* **/complete-level**: Handles user activity completion
* **/leaderboard**: Handles leaderboard retrieval

