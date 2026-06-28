# rtp-dvr
Video Recorder app for RTP Play/ RTP Palco

## What is it?
This is a "video recorder" to record live transmisions in RTP.
If you want to use it, just clone this repo, open the .py files inside the src directory and modify the URL variable, just like in the example bellow, to use the url of RTP Play you need:
URL
```python
import subprocess
import time
from playwright.sync_api import sync_playwright

URL = "https://www.rtp.pt/play/palco/direto/rtppalco1" # --> change here to the url you need to record!

```
In this example, we have 3 scripts, used to record in parallel until 3 different live streams, for 3 different live stages, just adapt the script to point to your url adress, then it will start recording the stream and saving it under the same directory, in the format rtp_palco1_{timestamp}.ts .
Thenif you prefer to convert it to mp4, to archive it, it would be better to convert it into mp4, you can use the following command to do it:

```bash
ffmpeg -i rtp_palco3_1781456969.ts -c copy rtp_Xinobi_PrimaveraSound_2026.mp4

```
### Remarks
Feel free to use it, copy it, improve it.
