
# Object-Oriented Programming Examples

This repository contains examples of object-oriented programming in Python, demonstrating key OOP concepts through two different systems:

## 1. Library system
The library system models different types of media items in a library.
Classes:

Media: Base class for all library items with checkout functionality
Book: Print media with author and page count
DVD: Video media with director and runtime
AudioBook: Audio version of books with narrator and length

Key OOP Concepts Demonstrated:

Inheritance: Media types inherit from base classes
Encapsulation: Protected attributes with property decorators
Method Overriding: Each subclass implements its own version of get_info()
Composition: Complex relationships between objects.

## 3. to run
python class-design/library_system.py

## 2. Transportation System

The transportation system demonstrates inheritance and polymorphism using different types of vehicles.

### Classes:
- `Vehicle`: Base class with common attributes and methods
- `Car`: Land vehicle with wheels
- `Boat`: Water vehicle with specific propulsion type
- `Plane`: Air vehicle with altitude capabilities
- `Bicycle`: Human-powered vehicle

### Key OOP Concepts Demonstrated:
- **Inheritance**: All vehicle types inherit from the base Vehicle class
- **Polymorphism**: Each vehicle implements its own version of the `move()` method
- **Encapsulation**: Vehicle properties are properly encapsulated within classes

### To Run:
python polymorphism/transportation.py

