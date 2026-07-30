# Ocarina Tabs Translator

This project converts text files containing musical notes into the key mapping format used by the **12 Hole Ocarina Tabs Creator**.

The translation is based on the key mapping defined by Panzi's **12 Hole Ocarina Tabs Creator**: <br>
https://panzi.github.io/ocarina_tabs/

<img width="1882" height="847" alt="12holeocarinatabscreator" src="https://github.com/user-attachments/assets/f062bfcc-febf-4e09-9efb-bde0cdba685a" /> 
(Yellow Submarine - Beatles on 12 Hole Ocarina Tabs Creator)<br>
<br>

Each letter in the generated `.oc` file represents a specific note according to the creator's key mapping (see `dictionary.txt` for the full mapping).

The program reads a text file containing the notes of a song and generates a new file with the `.oc` extension inside the `tabs/` directory. This output file can then be opened directly in the **12 Hole Ocarina Tabs Creator** to generate the corresponding ocarina tablature.

## Example

The example below uses **Yellow Submarine – The Beatles**.

* **Left:** the original `.txt` file containing the song notes.
* **Right:** the generated `.oc` file containing the translated key mapping.

<img width="1912" height="1017" alt="comparing" src="https://github.com/user-attachments/assets/3b1a3bde-e85a-41b4-b236-77146ed656dc" />

## Usage

1. Create a `.txt` file containing only the notes of the song, following the format shown in the example.
2. Run the program and enter the path to your file when prompted.

Example:

```text
songs/yellow_submarine.txt
```

3. The translated `.oc` file will be created in the `tabs/` directory.
4. Open the generated `.oc` file in the **12 Hole Ocarina Tabs Creator** using the **Open Text File** option (highlighted in the screenshot).

<img width="1882" height="847" alt="textfileopener" src="https://github.com/user-attachments/assets/0ee74177-0699-4047-afc7-4bf1deae3a04" />

## Project Structure

* `translator.py` — Main translation script.
* `dictionary.txt` — Note-to-key mapping reference.
* `tabs/` — Output directory for generated `.oc` files.
* `songs/` — Example input files.

The text file opener is highlighted with the blue circle
