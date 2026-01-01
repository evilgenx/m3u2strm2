# m3u2strm Usage Guide

## Overview

The `m3u2strm` tool converts M3U playlist files to STRM files with the proper folder structure for use with media servers like Emby.

## Syntax

```bash
python main.py <input_path_or_url>
```

## Input Options

### 1. Local M3U File (Recommended)

Process a local M3U file directly:

```bash
python main.py ./ptgold.m3u
python main.py /path/to/your/playlist.m3u
python main.py playlist.m3u
```

### 2. URL (Original Functionality)

Download and process M3U files from a URL:

```bash
python main.py http://example.com/
```

This will attempt to download:
- `http://example.com/tvshows/1` through `http://example.com/tvshows/9`
- `http://example.com/movies/`

## Output Structure

The tool creates STRM files in the following directory structure:

```
tvshows/
├── Show Name/
│   ├── Season 01/
│   │   ├── Show Name - S01E01.strm
│   │   ├── Show Name - S01E02.strm
│   │   └── ...
│   ├── Season 02/
│   │   ├── Show Name - S02E01.strm
│   │   └── ...
│   └── ...

movies/
├── Movie Name (Year).strm
├── Another Movie (Year).strm
└── ...
```

## Examples

### Processing a Local File

```bash
# Process a local M3U file
python main.py ./my_playlist.m3u

# Process with absolute path
python main.py /home/user/playlists/tv.m3u
```

### Processing from URL

```bash
# Download and process from URL
python main.py http://streaming.example.com/
```

## Error Handling

The tool includes comprehensive error handling for:

- Missing input files
- Invalid URLs
- Network download failures
- Malformed M3U entries
- Invalid episode/movie information

## Dependencies

Required Python packages:
- `wget` - For downloading files from URLs
- Standard library modules: `os`, `re`, `sys`

## Troubleshooting

### Common Issues

1. **File not found error**: Ensure the M3U file path is correct
2. **Network errors**: Check internet connection when using URLs
3. **Permission errors**: Ensure write permissions in the current directory

### Debug Information

The tool provides detailed logging showing:
- File processing progress
- Stream type detection (TV shows vs Movies vs Live TV)
- Directory creation
- STRM file generation

## Notes

- The tool automatically creates necessary directories (`tvshows/`, `movies/`)
- For URL processing, it creates an `m3u/` directory for temporary downloads
- STRM files contain direct links to the media streams
- The tool preserves episode information including season/episode numbers, resolution, and language tags when available
