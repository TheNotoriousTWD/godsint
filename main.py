import godsint

twitterUsername = input("Enter twitter username: ")
socials = godsint.Osint(twitter=twitterUsername).osint()
for i in socials.keys():
    print(f"{i} - {socials[i]['user']}")
