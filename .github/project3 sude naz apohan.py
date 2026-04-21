import csv
import os

def solve_everything():
    # 1. ADIM: CSV dosyasını kodun içinden otomatik oluşturuyoruz (Dış dosyaya gerek kalmasın diye)
    filename = 'bookings.csv'
    csv_content = """date,room,event_type,attendees
2025-03-01,Room A,Lecture,80
2025-03-01,Room B,Workshop,20
2025-03-02,Room A,Meeting,12
2025-03-02,Room C,Social,65
2025-03-03,Room A,Lecture,90
2025-03-03,Room B,Social,55
2025-03-04,Room C,Workshop,30
2025-03-04,Room A,Meeting,8
2025-03-05,Room B,Lecture,72
2025-03-05,Room C,Social,48
2025-03-06,Room A,Workshop,35
2025-03-06,Room B,Meeting,15
2025-03-07,Room C,Lecture,61
2025-03-07,Room A,Social,44
2025-03-08,Room B,Workshop,22"""

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(csv_content)

   
    room_counts = {}
    type_counts = {}
    day_attendees = {}
    all_events = []

   
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            room = row["room"]
            etype = row["event_type"]
            date = row["date"]
            att = int(row["attendees"])
            
            room_counts[room] = room_counts.get(room, 0) + 1
            type_counts[etype] = type_counts.get(etype, 0) + 1
            day_attendees[date] = day_attendees.get(date, 0) + att
            all_events.append(row)

    
    busiest_day = max(day_attendees, key=day_attendees.get)
    busiest_count = day_attendees[busiest_day]
    
    large_events = [e for e in all_events if int(e["attendees"]) > 50]
    large_events_sorted = sorted(large_events, key=lambda x: int(x["attendees"]), reverse=True)

    
    print("=== Community Centre Booking Report ===")
    
    print("\nBookings by Room:")
    for room in sorted(room_counts):
        print(f"  {room} : {room_counts[room]} events")

    print("\nBookings by Event Type:")
    for etype in sorted(type_counts):
        print(f"  {etype} : {type_counts[etype]} events")

    print(f"\nBusiest Day: {busiest_day} ({busiest_count} total attendees)")

    print("\nLarge Events (> 50 attendees):")
    for e in large_events_sorted:
        print(f"  {e['date']} | {e['room']} | {e['event_type']} | {e['attendees']} attendees")

if __name__ == "__main__":
    solve_everything()