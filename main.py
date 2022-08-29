import godsint

socials = godsint.Osint(twitter="twitter_username").osint()
for i in socials.keys():
    print(f"{i} - {socials[i]['user']}")
