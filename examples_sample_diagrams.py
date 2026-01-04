"""Sample UML descriptions and Mermaid diagrams."""

SAMPLE_DESCRIPTIONS = {
    "basic_user": "Create a User class with name, email attributes and login(), logout() methods",
    "inheritance": "Create Animal class with name attribute. Dog and Cat classes inherit from Animal.",
    "library_system": "Create Library with books list. Book class has title, author, isbn. User can borrow books.",
    "ecommerce": "Create Product with name, price. Customer has cart and can place orders.",
    "school": "Create Student with name, id. Teacher with subject. Course connects students and teachers."
}

SAMPLE_MERMAID_CODES = {
    "user_profile": """classDiagram
    class User {
        +userId : String
        +name : String
        +email : String
        +login() : Boolean
        +logout() : void
    }
    
    class Profile {
        +avatar : String
        +bio : String
        +preferences : Object
        +updateProfile() : void
    }
    
    User ||--|| Profile : has""",
    
    "animal_hierarchy": """classDiagram
    class Animal {
        +name : String
        +age : Integer
        +makeSound() : void
        +move() : void
    }
    
    class Dog {
        +breed : String
        +bark() : void
        +fetch() : void
    }
    
    class Cat {
        +color : String
        +meow() : void
        +hunt() : void
    }
    
    Animal <|-- Dog
    Animal <|-- Cat"""
}