# ContentWarningVideoSaver

Cant't retrieve your last camera? Lost it on the last day? No Problem. 

**The recorded Videos still exists on your PC!!!**

Well.. as long as you didn't restart your PC/Game.

---
## How it works

Content Warning stores a _.webm_ file in your LocalAppData every time you hit "Record" ingame. You can find the files 
from your last session in _C:\Users\\<YourUsername\>\AppData\Local\Temp\rec_

After bringing back the camera to your home base and throwing it into the "VideoExtractor" (or whatever it is called) 
the game will concatenate the recorded videos into one file and you'll have the option to save it to your desktop.

But if you loose the camera and can't retrieve it anymore (for example loosing it on the last day of a phase), you won't 
have the option to save the video to your desktop. But the video is still there!

And this is where this script comes in. It will search for all _.webm_ files in your LocalAppData and concatenate them
into one file and save it to your desktop.

---

## Requirements

- Python 3.10 or higher
- ffmpeg installed and added to your PATH (https://ffmpeg.org/download.html)

## How to use

1. Download/copy the main.py from this repository
2. Open a terminal and navigate to the folder where you saved the main.py
3. Execute the script with the following command:
    ```shell
    python main.py
    ```
4. Follow the instructions in the terminal
5. Enjoy your video(s)!

## What you should see
After executing the script a folder named "output" will be created on your desktop. This folder should have the 
following structure:

```
output
|
|_ day 1 - d519f1e3-212d-4d93-80de-7f7b1f4d5ec3
|    |_ output.webm
|
|_ day 2 - 4c311efa-e269-4db9-88ae-912f400a6db0
|    |_ output.webm
|
|_ day 3 - e1821ce6-00de-4f27-b5f0-a4547001b047
|    |_ output.webm
|
|_ day 4 - c0980c0a-aef5-433c-9ce8-9df02401d432
|    |_ output.webm
|
|_ day 5 - f595c316-49df-4b87-b230-053a36a61711
|    |_ output.webm
|
|_ day 6 - d9d0f305-2e46-49d1-a32c-fb3f6fa572b3
|    |_ output.webm
...
```
