import pygame
import random

# Pygameの初期化
pygame.init()

# 画面サイズの設定
screen = pygame.display.set_mode((800, 600))

# 選ばれたカードの記録を保存するセット
selected_cards = set()

# カードの設定
cards = [i for i in range(1, 17)]
random.shuffle(cards)
cards = [cards[n:n+4] for n in range(0, len(cards), 4)]

def containsDuplicate(n, selected_cards):
    if n in selected_cards:
        return True
    selected_cards.add(n)
    return False

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            card_x, card_y = x // 200, y // 150
            card = cards[card_y][card_x]
            print(f"Card selected at: ({card_x}, {card_y}) - Card is: {card}")

            if containsDuplicate(card, selected_cards):
                print("Duplicate card selected. Game Over.")
                running = False

    screen.fill((0, 0, 0))
    for y, row in enumerate(cards):
        for x, card in enumerate(row):
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x*200, y*150, 190, 140))
    pygame.display.flip()

pygame.quit()

"""
あなたが提供した `containsDuplicate` 関数は、リストに重複する要素があるかどうかを判断します。ここではこの関数を用いて、プレイヤーが順に数字を選び、既に選ばれた数字が再度選ばれた場合にゲームが終了する、というシンプルなゲームを作成します。

以下にそのコードを示します：

```python
import pygame
import random

# Pygameの初期化
pygame.init()

# 画面サイズの設定
screen = pygame.display.set_mode((800, 600))

# 選ばれたカードの記録を保存するセット
selected_cards = set()

# カードの設定
cards = [i for i in range(1, 17)]
random.shuffle(cards)
cards = [cards[n:n+4] for n in range(0, len(cards), 4)]

def containsDuplicate(n, selected_cards):
    if n in selected_cards:
        return True
    selected_cards.add(n)
    return False

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            card_x, card_y = x // 200, y // 150
            card = cards[card_y][card_x]
            print(f"Card selected at: ({card_x}, {card_y}) - Card is: {card}")

            if containsDuplicate(card, selected_cards):
                print("Duplicate card selected. Game Over.")
                running = False

    screen.fill((0, 0, 0))
    for y, row in enumerate(cards):
        for x, card in enumerate(row):
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x*200, y*150, 190, 140))
    pygame.display.flip()

pygame.quit()
```

このゲームでは、プレイヤーがカードを選ぶとそのカードの数字が `selected_cards` というセットに追加されます。もしプレイヤーが既に選ばれたカードを再度選ぶと `containsDuplicate` 関数が `True` を返し、ゲームが終了します。カードはただの白い四角形で、選ばれるとその数字がコンソールに表示されます。

ただし、このゲームは非常にシンプルで、プレイヤーがどのカードを選んだかを視覚的に示す機能や、スコアを表示する機能、ゲームが終了したときに何かを表示する機能などは含まれていません。これらの機能を追加して、ゲームをより楽しくすることが可能です。
"""