# shira-mp3

I have no idea how most of this works.

This is basically normal `shiradl`, except I added a little escape hatch for old devices that want actual MP3 files instead of YouTube's usual AAC/M4A thing.

Important bit: just renaming `.m4a` to `.mp3` would be fake and bad. The file would still be AAC in disguise. This version adds `--encode-mp3`, which makes ffmpeg actually re-encode the downloaded audio with `libmp3lame`, so the final file is a real MP3.

## Install this local version

From this folder:

```powershell
uv tool install --force .
```

That replaces the regular installed `shiradl` command with this local modified one. You do not need to delete your config.

Do not run this unless you want the normal published version again:

```powershell
uv tool install shiradl
```

## Use it once

```powershell
shiradl --encode-mp3 "https://music.youtube.com/watch?v=whatever"
```

## Turn it on in the normal config

Your existing config should still live in the normal place, probably:

```text
C:\Users\maste\.shiradl\config.json
```

Add this:

```json
"encode_mp3": true
```

Then you can just use `shiradl` normally and it should spit out real `.mp3` files.

## What changed

- YouTube downloads still start from the normal AAC/M4A stream, because that is what YouTube gives us.
- If `encode_mp3` is on, ffmpeg does a final re-encode to MP3.
- SoundCloud was already using MP3-ish behavior, so that path mostly stays alone.
- Tags still go through the existing `mediafile` tagging setup, and I added a small test to make sure MP3 output is actually MP3 and still keeps tags.

This is mainly for my very old iPod, because apparently it has opinions.
