from dataclasses import dataclass
from typing import List


@dataclass
class TranscriptChunk:
    chunk_id: str
    text: str
    start_char: int
    end_char: int


def chunk_transcript(
    transcript: str,
    max_chars: int = 18000,
    overlap_chars: int = 1500,
) -> List[TranscriptChunk]:
    """
    Baseline chunker.

    Splits a transcript into overlapping character windows.
    This is intentionally simple and will be improved later
    with sentence/utterance boundaries.
    """

    if not transcript:
        return []

    if max_chars <= overlap_chars:
        raise ValueError("max_chars must be greater than overlap_chars")

    chunks = []
    start = 0
    chunk_number = 1

    while start < len(transcript):
        end = min(start + max_chars, len(transcript))

        chunks.append(
            TranscriptChunk(
                chunk_id=f"chunk_{chunk_number:04d}",
                text=transcript[start:end],
                start_char=start,
                end_char=end,
            )
        )

        if end == len(transcript):
            break

        start = end - overlap_chars
        chunk_number += 1

    return chunks