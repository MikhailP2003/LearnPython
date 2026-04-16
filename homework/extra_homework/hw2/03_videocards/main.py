count = int(input("Количество видеокарт: "))

video_cards = []
for i in range(1, count + 1):
    card = int(input(f"{i} Видеокарта: "))
    video_cards.append(card)

max_card = max(video_cards)
new_video_cards = []

for card in video_cards:
    if card != max_card:
        new_video_cards.append(card)

print("\nСтарый список видеокарт:", video_cards)
print("Новый список видеокарт:", new_video_cards)