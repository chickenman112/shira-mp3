from pathlib import Path

from mediafile import MediaFile

from shiradl.dl import Dl
from shiradl.tagging import metadata_applier


def test_encode_mp3_reencodes_stub_and_keeps_tags(tmp_path):
	dl = Dl(
		Path("out"),
		tmp_path,
		None,
		Path("ffmpeg"),
		"140",
		1200,
		"jpg",
		94,
		"{albumartist}/{album}",
		"{track:02d} {title}",
		None,
		60,
		encode_mp3=True,
	)
	temp_location = dl.get_temp_location("stub")
	fixed_location = dl.get_fixed_location("stub")

	dl.stub_download(temp_location)
	dl.fixup(temp_location, fixed_location)
	metadata_applier(
		{
			"title": "Test Title",
			"album": "Test Album",
			"artist": "Test Artist",
			"albumartist": "Test Artist",
			"track": 1,
			"tracktotal": 1,
			"year": "2026",
			"date": "2026-05-19T00:00:00Z",
			"cover_url": "",
		},
		fixed_location,
		["cover"],
	)

	tagged_file = MediaFile(fixed_location)
	assert fixed_location.suffix == ".mp3"
	assert dl.get_audio_codec(fixed_location) == "mp3"
	assert tagged_file.title == "Test Title"
	assert tagged_file.artist == "Test Artist"
