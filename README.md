# Sound Puzzle

An educational audio-visual puzzle game for Greek-speaking children, built with Pygame.

> This project was implemented as part of the course **"Introduction to Computers" (ECE_Y106)** during the academic year 2022–2023.

---

## Overview

Players listen to audio narration clips from Greek fairytales, matches those audio clips to image puzzle picies and then drags those pieces into the correct order. The game is meant to test audio comprehension and memory for children. It used a simple score system based on correctly placed pieces.

---

## Features

- **3 Greek fairytales** with increasing difficulty:
  - ΤΑ 3 ΓΟΥΡΟΥΝΑΚΙΑ (The Three Little Pigs) — Easy, 3 pieces
  - ΛΑΓΟΣ ΚΑΙ ΧΕΛΩΝΑ (The Tortoise and the Hare) — Medium, 5 pieces
  - ΚΟΚΚΙΝΟΣΚΟΥΦΙΤΣΑ (Little Red Riding Hood) — Hard, 6 pieces
- **Drag-and-drop** puzzle interface with auto-snap to lock positions
- **Audio playback** button per puzzle piece to hear the narration clip
- **Score system**: `(correct pieces / total pieces) × 100`
- **Mute/unmute** toggle the background music on and off
- **ESC key** to return to the previous screen at any time

---

## Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/)

Install dependencies:

```
pip install pygame
```

---

## Running the Game

```
python game.py
```

