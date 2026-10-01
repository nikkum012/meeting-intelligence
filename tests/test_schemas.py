from app.models.schemas import (
    ActionItem,
    Decision,
    Entities,
    Evidence,
    MeetingOutput,
)


def test_meeting_output_schema():
    evidence = Evidence(
        quote="The motion carries.",
        source_chunk_id="chunk_001",
    )

    decision = Decision(
        decision="The motion was approved.",
        status="approved",
        evidence=[evidence],
        confidence=0.95,
    )

    action_item = ActionItem(
        task="Prepare the approved document.",
        assigned_to=None,
        due_date=None,
        status="open",
        evidence=[evidence],
        confidence=0.80,
    )

    output = MeetingOutput(
        summary="The council approved the motion.",
        decisions_made=[decision],
        action_items=[action_item],
        entities=Entities(),
    )

    assert output.decisions_made[0].status == "approved"
    assert output.decisions_made[0].confidence == 0.95