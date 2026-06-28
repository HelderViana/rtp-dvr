import subprocess
import time
from playwright.sync_api import sync_playwright


#URL = "https://www.rtp.pt/play/direto/rtp1"
URL = "https://www.rtp.pt/play/palco/direto/rtppalco2"


def get_stream_and_headers():
    stream_url = None

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )

        page = browser.new_page()

        # headers base (fixos e seguros)
        headers = {
            "referer": URL,
            "origin": "https://www.rtp.pt",
            "user-agent": page.evaluate("navigator.userAgent")
        }

        def on_request(request):
            nonlocal stream_url

            if ".m3u8" in request.url and "chunklist" in request.url:
                stream_url = request.url

        page.on("request", on_request)

        print("A abrir RTP Play...")
        page.goto(URL)

        # dar tempo ao player para arrancar
        page.wait_for_timeout(15000)

        browser.close()

    return stream_url, headers


def record(stream_url, headers):
    filename = f"rtp_palco2_{int(time.time())}.ts"

    cmd = [
        "ffmpeg",
        "-user_agent", headers.get("user-agent", "Mozilla/5.0"),
        "-headers",
        f"Referer: {headers.get('referer')}\r\nOrigin: {headers.get('origin')}\r\n",
        "-i", stream_url,
        "-c", "copy",
        "-f", "mpegts",
        filename
    ]

    print("A gravar:")
    print(stream_url)
    print(f"Ficheiro: {filename}")

    subprocess.run(cmd)


if __name__ == "__main__":
    url, headers = get_stream_and_headers()

    if not url:
        print("Não foi possível encontrar stream (.m3u8)")
        exit(1)

    record(url, headers)
