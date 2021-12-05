
# License Plate Recognition + Interpretation

This project is designed to be a license plate recognition and interpretation program. The program takes an input image and detects a license plate from the image (using the OpenCV library). The plate is then cropped and sent to a function that is responsible for recognizing the text written on the plate (using the Tesseract OCR library). Then the text is passed to an automation script, which navigates to a car recognition database [FAXVIN](https://www.faxvin.com/license-plate-lookup), whereupon the script will search the license plate and retrieve the car's information. Program will then output the license plate, VIN, Year, Make, and Model of the queried car into a CSV file.
  
_(Note: This application was designed using Java 8, Apache Maven, Java Sockets, JavaFX 12, SceneBuilder, and JUnit 4)_

## Prerequisites


## Testing (_with Maven_)

  

Extensive unit test cases have been written using JUnit 4 to ensure the game elements are working in order.

  

First, `cd` into the project directory, then:

  

```

mvn test

```

  

## Build/Compile (_with Maven_)

  

First, `cd` into the project directory, then:

  

```

mvn package

```

  

_This makes a folder named `target` in the project root, containing the `.jar` and `.class` files._

  

## Run (_with Maven_)

  

Ensure that you are running [baccarat-server](https://github.com/N19htw1n9/Baccarat-Server). Once you have built/compiled, execute this command within the same directory:

  

```

mvn exec:java

```
