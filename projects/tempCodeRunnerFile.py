user_escape_chance = random.randint(1, 10) #TEN PERCENT CHANCE ESCAPE FAILS
            if user_escape_chance == 6:
                health_stat = health_stat - enemy_damage
                print(f"{enemy_name} snatched you before you could escape, and hit you! - You now have {health_stat} health.")
            else:
                street_respect_stat = street_respect_stat - 15
                print(f"Imagine running from a fight like a scaredy cat. 💔\nThis is your street respect now though: {street_respect_stat}.")
                break