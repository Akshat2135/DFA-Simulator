# DFA Simulator

A modern, interactive web application for building Deterministic Finite Automata (DFAs), running input strings through them, and stepping through state transitions in real time. Built with Python and Streamlit.

## Features

- **Interactive DFA Definition**: Specify states, alphabet, start state, and accepting states easily from the sidebar.
- **Dynamic Transition Matrix**: Configure next-state transitions for every state and symbol pair with full completeness checking.
- **Step-by-Step String Execution**: Test any input string (including the empty string $\epsilon$) and step through transitions using a playback slider.
- **State Diagram Visualization**: Real-time Graphviz state diagram highlighting the currently active state at each step.
- **Trace History Table**: Detailed step-by-step audit table showing `(From State, Symbol, To State)` with instant accept/reject verdict.
- **Save & Load**: Export DFA configurations to standard JSON format and restore them anytime.
- **Preloaded Example**: Comes with an example DFA accepting binary strings ending in `1`.

## Requirements

- Python 3.10 or newer
- `streamlit`
- `pytest` (for running unit tests)

## Installation & Setup

Clone the repository and install the dependencies:

```bash
pip install streamlit pytest
```

Or install the package in editable mode:

```bash
pip install -e .
```

## Running the Application

From the project root directory:

```bash
streamlit run src/dfa_simulator/app.py
```

Alternatively, run as a module:

```bash
python -m dfa_simulator
```

Streamlit will launch a local web server (usually at [http://localhost:8501](http://localhost:8501)) and open the application in your browser.

## How to Use

1. **Define the Automaton**:
   - In the sidebar, enter comma-separated states (e.g., `q0, q1, q2`) and single-character alphabet symbols (e.g., `0, 1`).
   - Select the designated start state and choose one or more accepting states.
2. **Set Transitions**:
   - Fill in the transition table for each `(state, symbol)` pair.
3. **Simulate Input**:
   - Enter an input string under **Run it on a string**.
   - Drag the **Step** slider to observe transitions one by one. The active state is highlighted in gold on the state diagram.
4. **Save / Load**:
   - Click **Save DFA as JSON** to download the machine configuration, or upload a previously saved file via **Load a saved DFA**.

## Project Structure

```
.
├── .gitignore
├── pyproject.toml
├── README.md
└── src/
    └── dfa_simulator/
        ├── __init__.py      # Package entry point and CLI runner
        ├── app.py           # Streamlit web user interface
        ├── dfa.py           # Core DFA class, validation, and Graphviz exporter
        └── test_dfa.py      # Automated test suite
```

## Running Tests

Run the test suite using pytest:

```bash
pytest
```

All 8 unit tests cover:
- Acceptance and rejection logic
- Out-of-alphabet character handling
- Transition table completeness and state validation
- JSON serialization round-tripping
- Input parsing edge cases

## Author

Developed by **Akshat**
