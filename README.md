# Intelligent Office Surveillance System

A small Windows desktop app that watches a room through a USB webcam, saves the frames
around anything that moves, and turns each of those bursts into a short video you can flick
through afterwards. Built as an A-Level Computer Science coursework project with a
classmate.

The problem it was written for was mundane and real: a teacher's office chair kept
disappearing. The building has CCTV, but not pointed at that office, and getting footage
released takes days. The requirement was something that runs on the PC already sitting on
the desk, with no cloud account and no extra hardware.

The Analysis and Design writeup that used to occupy this file is still in the git history
if you want it.

## What it does

Arm the system and it starts sampling the webcam once a second. When two consecutive frames
differ by more than a set amount, it treats that as motion: the capture rate doubles, and
every frame from that point is staged for keeping. Sixty frames after the last movement it
stops, moves everything it staged into a timestamped event folder, and encodes that folder
into an AVI at 2 fps.

The GUI is four buttons. Arm and disarm, open the events folder, wipe all recorded media
behind a confirmation dialog, and cycle which camera index is in use.

## How it works

Detection is deliberately crude. Each frame is converted to greyscale, differenced against
the previous one with `PIL.ImageChops`, and the root mean square of that difference is
compared against a threshold of 15.0. No background subtraction, no object detection, no
model. For a static indoor scene with the lights on this is enough, and it costs almost
nothing per frame, which matters because the whole thing has to sit in the background on a
school PC without being noticed.

The dual-rate sampling is the part I would point at. Recording at a useful frame rate all
the time fills a disk quickly, and recording at 1 fps produces evidence too choppy to
identify anyone. So idle sampling is 1 fps and only writes to a rolling temp buffer capped
at 3000 files, while an active event samples at 2 fps and copies each frame into a staging
folder. The 60-frame countdown resets on every new detection, so continuous movement
extends the recording rather than chopping it into fragments.

Two problems came out of testing on real hardware. Reopening the camera for every capture
added enough latency that the effective frame rate could not be changed at all, so the
handle is now opened once in `init_camera` and held for the life of the run. And the app
would not see a virtual camera at all, because Windows Media Foundation does not enumerate
them. It now tries DirectShow first and falls back to MSMF.

Media flows through four directories:

```
temporary/   every frame, rolling buffer, capped at 3000
saved/       frames staged while an event is in progress
events/      event_YYYY-MM-DD_HH-MM-SS/ , the frames for one event
events2/     the rendered .avi for each event
```

## Running it

Windows 10 or 11, Python 3, a connected webcam.

```bash
pip install customtkinter opencv-python pillow numpy
python finalV/GUI1.py
```

`finalV/requirements.txt` exists but is saved as UTF-16, which some pip versions refuse to
read. The four packages above are what actually matters.

`finalV/` is the current version. `GUI_TKINTER.py`, `GUI-TKINTER-V2.py`, `GUI-TKINTER-V2b.py`
and `miniNEAstuf/` at the root are earlier iterations, kept because the coursework wanted
the development history visible. They are not maintained.

## Current state

The core loop works. Motion is caught reliably, events are bundled correctly, and the
videos come out watchable.

A fair amount of what the design document promised is not built:

- There is no live camera preview. The GUI has a label reserved for it and nothing ever
  draws into it, so you arm the system blind and have to trust that the camera index is
  right. This is the biggest gap.
- Sensitivity is a constant in `systemArmed.py`, not a Low/Medium/High selector.
- Ignored regions are not implemented. There is a hardcoded polygon mask in
  `capture_image` that is commented out, left from testing against a bright window.
- No audible alert, no event database, no unique event IDs beyond the folder timestamp.
- Nothing deletes old evidence automatically. Only the temp buffer has a cap, and clearing
  events is a manual button press.

Known rough edges: whole-frame differencing means a light switch or a sunlit cloud passing
counts as motion, and the threshold was tuned by hand for one room. Disarming blocks the UI
for up to five seconds while it joins the detection thread. The app is Windows-only, partly
for the camera backends and partly because opening the gallery uses `os.startfile`.

## Tech

Python, OpenCV for capture and video encoding, Pillow for the frame differencing,
CustomTkinter for the interface. MIT licensed.
