from django.core.management.base import BaseCommand
# from django_seed import Seed
# seeder = Seed.seeder()
# import random
# from ...models import *
from django.utils import timezone
import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()


########

cur.execute('''INSERT into website_product values ( null, "Jabra Elite Active 65t", "The Jabra Elite Active 65t completely wireless earbuds are our favorite pick for working out, and clearly everyone else's. They offer a combination of great sound and battery life, a flawless fit, and, most importantly, a reliable wireless connection." , 151.99, 765, "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544049078-gifts-for-brothers-jabra-ear-buds-1541438364.jpg?crop=1xw:1xh;center,top&resize=768:*", 0, 1, 1)''')
cur.execute('''INSERT into website_product values ( null, "Mattel Lil' Gleemerz Glowzer Figure", "These Lil’ Gleemerz Glowzer figures are the hot new toy this season. They have light-up tails and glowing eyes, and they make noises and say phrases in response to touch and sound." , 19.99, 200, "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544112867-lil-gleemerz-1544112844.jpg?crop=1xw:1xh;center,top&resize=768:*", 0, 1, 2)''')
cur.execute('''INSERT into website_producttype values ( null, "Techology", 0 )''')
cur.execute('''INSERT into website_producttype values ( null, "Toys/Games", 0 )''')
conn.commit()

# cur.execute('SELECT firstname, lastname, phonenumber FROM People')
# for row in cur:
#     print row

# conn.close()

# class Command(BaseCommand):
#   """This class runs the operation of seeding the database with fake data. This will create a DB that is for testing purposes only.

#   Author(s): Zac Jones
#   """

#   # this is where the magic happens
#   def handle(self, *args, **options):

#     # add departments
#     # TODO - currently department names can duplicate, fix this so they only occur once?
#     INSERT into website_product values ( null, "Jabra Elite Active 65t", "The Jabra Elite Active 65t completely wireless earbuds are our favorite pick for working out, and clearly everyone else's. They offer a combination of great sound and battery life, a flawless fit, and, most importantly, a reliable wireless connection." , 151.99, 765, "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544049078-gifts-for-brothers-jabra-ear-buds-1541438364.jpg?crop=1xw:1xh;center,top&resize=768:*", 0, 1, 1 )
#     INSERT into website_product values ( null, "Mattel Lil' Gleemerz Glowzer Figure", "These Lil’ Gleemerz Glowzer figures are the hot new toy this season. They have light-up tails and glowing eyes, and they make noises and say phrases in response to touch and sound." , 19.99, 200, "https://hips.hearstapps.com/vader-prod.s3.amazonaws.com/1544112867-lil-gleemerz-1544112844.jpg?crop=1xw:1xh;center,top&resize=768:*", 0, 1, 2 )


#     INSERT into website_producttype values ( null, "Techology", 0 )
#     INSERT into website_producttype values ( null, "Toys/Games", 0 )

#     seeder.add_entity(EmployeeTrainingProgram, 10)

#     seeder.execute()