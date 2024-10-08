# Interactive Whiteboard with Hand Gestures

This project implements an interactive whiteboard using Python and OpenCV. The whiteboard operates using a webcam feed, where hand poses are tracked and interpreted to allow for drawing (printing) and erasing actions. Different hand gestures made by the presenter trigger various actions on the whiteboard.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Hand Gestures](#hand-gestures)
- [Project Structure](#project-structure)
- [License](#license)

## Features

- **Interactive Whiteboard:** Use hand gestures to draw on a virtual whiteboard.
- **Gesture-Based Controls:**
  - Detects different hand poses to enable drawing or erasing.
  - Dynamic interaction through live webcam feed.
- **Python and OpenCV-Based:** Built using OpenCV for computer vision and hand tracking.
  
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/interactive-whiteboard.git
   cd interactive-whiteboard
   ```
2. Create venv:
    ```bash
   python -m venv venv
   venv/Scripts/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install wheel piptools setuptools
   ```

4. To generate the `requirements.txt` file, you can list all necessary libraries in `requirements.in` and run:

   ```bash
   pip-compile
   pip-sync
   ```

   Ensure you have Python 3.12+ installed.

## Usage

1. Start the whiteboard application:

   ```bash
   python whiteboard.py
   ```

   This will launch the webcam feed and display the interactive whiteboard.

2. Use different hand poses to interact with the whiteboard:
   - One pose will enable drawing, while another will erase.
   - Move your hand to draw on the screen or remove previously drawn shapes.

## Hand Gestures

- **Drawing Mode:** When the system detects a specific hand pose (e.g., a single raised finger), it switches to drawing mode, allowing you to draw on the whiteboard.
- **Erasing Mode:** Another hand pose (e.g., a closed fist) switches to erasing mode, enabling you to remove drawn content.

Feel free to customize the hand poses in the code for your specific use case.

## Project Structure

```bash
├── data/
│   └── gestures/                # Predefined hand gesture data (if applicable)
├── whiteboard.py                # Main script to run the whiteboard
├── requirements.in              # Dependencies for pip-tools
├── requirements.txt             # Compiled dependency file
└── README.md                    # Project documentation
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
