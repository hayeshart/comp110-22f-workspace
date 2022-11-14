"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730449088"  # TODO


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, other: Point) -> float: 
        """Finds the variable of the distance between two distinct points."""
        new_y: float = self.y - other.y
        new_x: float = self.x - other.x
        return sqrt((new_x**2) + (new_y**2))


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.

    def tick(self) -> None: 
        """Makes an infected cell have immunity if the cell outlasts recovery."""
        self.location = self.location.add(self.direction)
        if self.is_infected(): 
            self.sickness += 1 
            if (self.sickness) == (constants.RECOVERY_PERIOD): 
                self.immunize()
    
    def contract_disease(self) -> None: 
        """Makes a cell infected with the disease."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool: 
        """Sees if the cell = 0 which means that it is vulnerable to the disease."""
        if self.sickness == 0: 
            return True 
        else: 
            return False

    def is_infected(self) -> bool: 
        """Sees whether the cell is infected with the disease."""
        if self.sickness >= 1: 
            return True 
        else: 
            return False

    def color(self) -> str:
        """Return the color representation of a cell."""
        if (self.is_vulnerable()) is True:
            return "gray"
        elif (self.is_infected()) is True:
            return "pink"
        elif (self.is_immune()) is True:
            return "blue"
    
    def contact_with(self, other: Cell) -> None: 
        """Shows if a cell has had contact with an infected cell. If yes, the cell becomes infected."""
        if other.is_vulnerable() is True and self.is_infected() is True: 
            other.contract_disease()
        elif self.is_vulnerable() is True and other.is_infected() is True: 
            self.contract_disease()

    def immunize(self) -> None: 
        """Assigns a cell the value of -1 to signify that it has developed immunity to the disease."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool: 
        """Determines if a cell's value is -1."""
        if self.sickness == -1: 
            return True 
        else: 
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        if immune_cells < 0: 
            raise ValueError("The number of immune cells can't be less than zero.")
        elif infected_cells >= cells: 
            raise ValueError("Infected cells can't account for all cells.")
        elif immune_cells >= cells: 
            raise ValueError("The number of immune cells exceeds all cells.")
        elif immune_cells + infected_cells >= cells: 
            raise ValueError("Number of immune and infected cells exceeds the toral number of cells.")
        elif infected_cells <= 0: 
            raise ValueError("There are not any infected cells.")

        self.population = []
        
        for _ in range(cells): 
            start_location: Point = self.random_location() 
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for i in range(infected_cells): 
            self.population[i].contract_disease()
        for i in range(immune_cells): 
            self.population[i].immunize()
        
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population: 
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed 
        direction_y: float = sin(random_angle) * speed 
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X: 
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        elif cell.location.y > constants.MAX_Y: 
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        elif cell.location.x < constants.MIN_X: 
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0 
        elif cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population: 
            if cell.is_infected(): 
                return False
        return True

    def check_contacts(self) -> None: 
        """Sees if a cell has had contact with another cell within the distance of CELL_RADIUS. If yes and one cell is infected, the other vulnerable cell becomes infected too."""
        for m in range(0, len(self.population)): 
            for h in range(m + 1, len(self.population)): 
                if self.population[m].location.distance(self.population[h].location) < constants.CELL_RADIUS:
                    self.population[m].contact_with(self.population[h])