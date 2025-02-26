# FastAPI File Server

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/fizycurry/RW_env_fastapi.git
   ```
2. **Open the cloned directory in an editor like Vscode**: this can also be done using a bash terminal but for ease of use, Vscode can be used.
3. **Setup (and activate) a Virtual Environment**: This is necessary to prevent dependency conflicts
    
    For windows:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    For Linux:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

4. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

5. **Set some environment variables**: Create a ```.env``` file in the root of the project. An example of content could be:
    ```.env
    PORT=8000
    FILEPATH=uploads/
    ```
    ***Note*** the port variable is the one the server will run on

6. **Run the Server:**
    ```bash
    python main.py
    ```

7. **Access the Application:** Visit http://127.0.0.1:8000/docs to view the API documentation.


## Commands to create executables
### For all distributions
```bash
python3 -m nuitka --standalone --include-data-dir=./inject_files=inject_files main.py
```
### Running on single machine 
```bash
python -m nuitka --onefile main.py --output-filename=test --include-data-dir=./inject_files=inject_files
```

## Note
While trying out the commands above, it would be better to keep the name of the folder or data directory the same for the output folder to understand how the commands work and/or differ. Specifically this option:

```bash
--include-data-dir={folder containing data to include in the executable}={folder name used by the executable}
```
