from app.pipeline.chunker import chunk_transcript


def test_chunker_creates_overlapping_chunks():
    transcript = "AB" * 20000

    chunks = chunk_transcript(
        transcript,
        max_chars=10000,
        overlap_chars=1000,
    )

    assert len(chunks) > 1

    # Every chunk should have content.
    assert all(chunk.text for chunk in chunks)

    # Adjacent chunks should overlap.
    assert chunks[0].text[-1000:] == chunks[1].text[:1000]


def test_short_transcript_is_one_chunk():
    transcript = "This is a short meeting."

    chunks = chunk_transcript(transcript)

    assert len(chunks) == 1
    assert chunks[0].text == transcript