import json

# Read the JSON array from zone_events.json
with open('pipeline/zone_events.json', 'r') as f:
    events = json.load(f)

# Write each event as a single line in JSONL format
with open('data/output/events.jsonl', 'w') as f:
    for event in events:
        f.write(json.dumps(event) + '\n')

print(f"Converted {len(events)} events to JSONL format")
print(f"Output saved to data/output/events.jsonl")
