import sqlite3


conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()



c.execute('''INSERT INTO auth_user VALUES (
            1,
            "Default Password",
            "2000-01-01 01:01:01",
            0,
            "Default Username",
            "First Name",
            "Default email",
            0,
            0,
            "2000-01-01 01:01:01",
            "Last Name")''')
c.execute('''INSERT INTO website_customer VALUES (
            1,
            "Default User Address",
            "000-000-0000",
            0)''')
c.execute('''INSERT INTO website_product VALUES (
            1,
            "Jabra Elite Active 65t",
            "The Jabra Elite Active 65t completely wireless earbuds are our favorite pick for working out, and clearly everyone else's. They offer a combination of great sound and battery life, a flawless fit, and, most importantly, a reliable wireless connection.",
            151.99,
            765,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544049078-gifts-for-brothers-jabra-ear-buds-1541438364.jpg?crop=1xw:1xh;center,top&resize=768:*",
            0,
            1,
            1)''')
c.execute('''INSERT INTO website_product VALUES (
            2,
            "Mattel Lil' Gleemerz Glowzer Figure",
            "These Lil’ Gleemerz Glowzer figures are the hot new toy this season. They have light-up tails and glowing eyes, and they make noises and say phrases in response to touch and sound.",
            19.99,
            200,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544112867-lil-gleemerz-1544112844.jpg?crop=1xw:1xh;center,top&resize=768:*",
            0,
            1,
            6)''')
c.execute('''INSERT INTO website_product VALUES (
            3,
            "Becoming by Michelle Obama",
            "It's no surprise that the top-selling book in 2018 is a top seller on Amazon. The book sold more than 2 million copies in just the first 15 days. Becoming chronicles both Obama's public and private experiences that have shaped the person she is today.",
            19.50,
            275,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544050047-becoming-1544050036.jpg?crop=1xw:1xh;center,top&resize=768:*",
            0,
            1,
            7)''')
c.execute('''INSERT INTO website_product VALUES (
            4,
            "Instant Pot 7-in-1 Multi-Cooker",
            "The Instant Pot is a 7-in-1 multicooker that functions as a programmable pressure cooker, rice cooker, slow cooker, steamer, yogurt maker, and more. Many customers report cooking with it almost every day of the week!",
            79.95,
            450,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1532378051-51U59UGZTQL.jpg?crop=1xw:1.00xh;center,top&resize=768:*",
            0,
            1,
            5)''')
c.execute('''INSERT INTO website_product VALUES (
            5,
            "All-New Echo Dot",
            "It's no surprise that one of the best-selling electronics is Amazon's own, considering how much visibility they get on the site. The Echo Dot 3rd Generation is a voice-controlled device that uses Alexa (your new BFF) to do everything — from adding new products to your Amazon shopping cart to playing music and notifying you about the weather. ",
            49.99,
            900,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544047756-amazon-echo-dot-1543505742.jpg?crop=1xw:1xh;center,top&resize=768:*",
            0,
            1,
            1)''')
c.execute('''INSERT INTO website_product VALUES (
            6,
            "Fire TV Stick 4K",
            "The Amazon Fire Stick allows you to watch from platforms like Netflix, Hulu, and Amazon Video directly on your TV in 4K. This version has an Alexa (aka voice-activated) remote, making it easier than ever to select what you want to watch. ",
            39.99,
            99,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544048575-fire-stick-4k-1544048564.jpg?crop=1xw:1xh;center,top&resize=768:*",
            0,
            1,
            1)''')
c.execute('''INSERT INTO website_product VALUES (
            7,
            "Fire HD 8 Tablet with Alexa",
            "The Fire Tablet is like a portable entertainment center that's perfect for travel, and it also doubles as an e-reader. You can watch from various show platforms and apps like Netflix, Hulu, HBO, and more, plus play games and video chat with friends. With 3.9 stars out of 40,000 reviews, it's safe to say this is the perfect affordable alternative to an iPad. ",
            49.99,
            1200,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544125088-1508971596-amazon-fire-7-tablet.jpg?crop=1xw:1xh;center,top&resize=768:*",
            0,
            1,
            1)''')
c.execute('''INSERT INTO website_product VALUES (
            8,
            "ZonLi Weighted Blanket",
            "Gravity blankets are the latest craze that is helping people relax, destress, and get better sleep. Gravity makes the original blanket, but these lower-priced ZonLi versions on Amazon are becoming just as popular. And don't think it's just a cheap knockoff. Out of over 1,000 reviews, they have a 4.4-star rating and come in different sizes, weights, and colors. ",
            65.50,
            133,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544113351-zonli-weighted-blanket-1544113343.jpg?crop=1xw:1xh;center,top&resize=768:*",
            0,
            1,
            2)''')
c.execute('''INSERT INTO website_product VALUES (
            9,
            "Educated: A Memoir",
            "The New York Times just named Educated one of their 10 best books of the year. Once you start, it’ll completely envelop you and stay with you long after you finish.",
            16.80,
            275,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544050353-educated-1544050340.jpg?crop=1xw:1xh;center,top&resize=768:*",
            0,
            1,
            7)''')
c.execute('''INSERT INTO website_product VALUES (
            10,
            "Lagunamoon Essential Oils",
            "Whether you need a mood-lifter or a sleep-inducer, this set of eight therapeutic essential oils is an Amazon favorite for its affordability and variety.",
            11.99,
            275,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544119187-essential-oils-1544119170.jpg?crop=1xw:1xh;center,top&resize=768:*",
            0,
            1,
            4)''')
c.execute('''INSERT INTO website_product VALUES (
            11,
            "If You Can Read This Bring Me Wine Socks",
            "Whether it's the season of gag gifts, or people just need more wine during the stressful holiday season, these socks are a hit, with a 5-star rating.",
            11.89,
            275,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544119592-wine-socks-1544119580.jpg?crop=1xw:1xh;center,top&resize=768:*",
            0,
            1,
            8)''')
c.execute('''INSERT INTO website_product VALUES (
            12,
            "Fujifilm Instax Mini 9 Instant Camera",
            "People — especially millennials — love these Fujifilm instant cameras. They're a fun and popular way to capture moments instead of having all your photos in the cloud on your smartphone. Plus, the cameras come in five fun colors.",
            55.00,
            275,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544111794-instax-1543344276.jpg?crop=1xw:1xh;center,top&resize=768:*",
            0,
            1,
            1)''')
c.execute('''INSERT INTO website_product VALUES (
            13,
            "URPOWER Essential Oil Diffuser",
            "Nearly 28,000 reviewers agree that this diffuser, which has a 4.5-star rating, is worth the investment. There are tons to choose from on Amazon, but why not go with the best-selling one? It has an LED light that cycles through colors when in use.",
            15.99,
            48,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1524594351-51cwyov2s4l_sl1001_.jpg?crop=1xw:1xh;center,top&resize=768:*",
            0,
            1,
            2)''')
c.execute('''INSERT INTO website_product VALUES (
            14,
            "Nintendo Switch",
            "The Nintendo Switch is the latest craze in the gaming world. The continually growing selection of games attracts new users all the time — that and the fact that you can virtually play anywhere, and with another person using the Joy-Con controllers.",
            345.96,
            275,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544114944-nintendo-switch-1544114935.jpg?crop=1xw:1xh;center,top&resize=768:*",
            0,
            1,
            3)''')
c.execute('''INSERT INTO website_product VALUES (
            15,
            "Wemo Mini Smart Plug",
            "This smart plug only needs Wi-Fi, and it comes with features like 'Away Mode', which will randomize the times your lights go on to make it look like you’re home even when you’re not.",
            22.99,
            572,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544111610-1507836531-wemo-mini-smart-plug.jpg?crop=1xw:1xh;center,top&resize=768:*",
            0,
            1,
            1)''')
c.execute('''INSERT INTO website_product VALUES (
            16,
            "GoPro HERO7 Black",
            "This is an obvious top seller. It’s the best action camera you can buy. It has excellent video quality and amazing image stabilization for those more adventurous trips.",
            349.00,
            52,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544115628-gopro-1544115617.jpg?crop=1xw:1xh;center,top&resize=768:*",
            0,
            1,
            1)''')
c.execute('''INSERT INTO website_product VALUES (
            17,
            "Hasbro Connect 4 Game",
            "This game is a classic for a reason! The updated version is played the same way we all played it as kids, but it features newer-looking pieces.",
            9.99,
            887,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1524593152-connect-4.jpg?crop=1xw:1.0xh;center,top&resize=768:*",
            0,
            1,
            3)''')
c.execute('''INSERT INTO website_product VALUES (
            18,
            "Z-Man Games Pandemic",
            "A favorite among tweens and teens who are too young for this and too old for that, Pandemic will keep them entertained and off electronics for hours. Nearly 2,300 Amazon reviewers and players say that it's worthy of an average 4.7-star rating.",
            35.99,
            275,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1524583821-71xajOgHMAL._SL1000_.jpg?crop=1xw:1.00xh;center,top&resize=768:*",
            0,
            1,
            3)''')
c.execute('''INSERT INTO website_product VALUES (
            19,
            "Body Merry Retinol Moisturizer",
            "You might not have heard of this brand, but people love it. The Body Merry Retinol Moisturizer is huge seller that always pops up on the best-seller list. After reading some of the glowing reviews, you might be convinced to try it yourself.",
            22.99,
            30,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544133800-body-merry-1544133789.jpg?crop=1xw:1xh;center,top&resize=768:*",
            0,
            1,
            4)''')
c.execute('''INSERT INTO website_product VALUES (
            20,
            "Marvel’s Spider-Man for PlayStation 4",
            "This PlayStation exclusive is currently one of the top games on Amazon. It even has a 4.8-star rating, and according to some of the buyers, you'll spend hours swinging from webs through the big-city buildings. ",
            38.98,
            421,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544115261-spider-man-1544115241.jpg?crop=1xw:1xh;center,top&resize=768:*",
            0,
            1,
            3)''')
c.execute('''INSERT INTO website_product VALUES (
            21,
            "KRUPS F203 Electric Spice and Coffee Grinder",
            "Make the morning grind a little easier with a coffee grinder that can process up to 3 ounces of coffee beans in just seconds. Buyers love its speedy 200-watt motor and smooth operation.",
            14.49,
            111,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1524585554-71v4Mm5X49L._SL1500_.jpg?crop=1xw:0.909xh;center,top&resize=768:*",
            0,
            1,
            5)''')
c.execute('''INSERT INTO website_product VALUES (
            22,
            "Kindle Paperwhite E-reader",
            "The new Kindle Paperwhite is one of the best, and buyers love that it's waterproof. Heavy readers will enjoy not having to lug those massive hardcovers around with them. ",
            99.99,
            643,
            "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544456960-kindle-paperwhite-waterproof-1543852057.jpg?crop=1xw:1xh;center,top&resize=768:*",
            0,
            1,
            1)''')
c.execute('''INSERT INTO website_productType Values (
            1,
            "Technology",
            0)''')
c.execute('''INSERT INTO website_productType Values (
            2,
            "Household Goods",
            0)''')
c.execute('''INSERT INTO website_productType Values (
            3,
            "Games/Entertainment",
            0)''')
c.execute('''INSERT INTO website_productType Values (
            4,
            "Personal Products",
            0)''')
c.execute('''INSERT INTO website_productType Values (
            5,
            "Kitchen",
            0)''')
c.execute('''INSERT INTO website_productType Values (
            6,
            "Toys",
            0)''')
c.execute('''INSERT INTO website_productType Values (
            7,
            "Books",
            0)''')
c.execute('''INSERT INTO website_productType Values (
            8,
            "Apparel",
            0)''')
c.execute('''INSERT INTO website_order Values (
            1,
            0,
            2,
            1)''')
c.execute('''INSERT INTO website_productOrder Values (
            1,
            0,
            1,
            3)''')
c.execute('''INSERT INTO website_productOrder Values (
            2,
            0,
            1,
            6)''')
c.execute('''INSERT INTO website_paymenttype VALUES (
             1,
            "None",
             0)''')
c.execute('''INSERT INTO website_paymenttype VALUES (
             2,
            "Credit Card",
             0)''')
c.execute('''INSERT INTO website_paymenttype VALUES (
             3,
            "Debit Card",
             0)''')
c.execute('''INSERT INTO website_paymenttype VALUES (
             4,
            "Gift Card",
             0)''')
c.execute('''INSERT INTO website_paymenttype VALUES (
             5,
            "Gold Bullion",
             0)''')
c.execute('''INSERT INTO website_paymentmethod VALUES (
             1,
             0,
             0,
             1,
             1)''')
c.execute('''INSERT INTO website_paymentmethod VALUES (
             Null,
             999999999,
             0,
             2,
             4)''')
c.execute('''INSERT INTO website_productlike VALUES (
             Null,
             5,
             "Great product!!! It has all my favorite shows and an easy link to surf the web!",
             6,
             2)''')
c.execute('''INSERT INTO website_productlike VALUES (
             Null,
             4,
             "Pretty great gaming. Deducted a star due to the price.",
             14,
             2)''')
c.execute('''INSERT INTO website_productlike VALUES (
             Null,
             1,
             "The text might be alright, but I prefer pop-up books.",
             3,
             2)''')

conn.commit()
