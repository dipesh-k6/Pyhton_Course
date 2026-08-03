\# Common lookups



|Lookup|	Meaning|	SQL equivalent|
|-|-|-|
|\_\_gt|greater than|>|
|\_\_gte|greater than or equal|>=|
|\_\_lt|less than|<|
|\_\_lte|less than or equal|<=|
|\_\_exact|exactly equal|=|
|\_\_contains|contains string|LIKE %value%|
|\_\_startswith|starts with|LIKE value%|
|\_\_in|in a list|IN (1, 2, 3)|



\# example

&#x09;- create a post

&#x09;post1 = Post.objects.create(

&#x20;   	title="First Post",

&#x20;   	author="Ali",

&#x20;   	content="This is my first post!",

&#x20;   	likes=15

&#x09;)



&#x09;- create another

&#x09;post2 = Post.objects.create(

&#x20;   	title="Django Basics",

&#x20;   	author="Sara", 

&#x20;   	content="Django is awesome!",

&#x20;   	likes=42

&#x09;)



&#x09;- get all posts

&#x09;posts = Post.objects.all()

&#x09;print(posts)



\# using lookups

&#x09;- get ALL posts

&#x09;Post.objects.all()



&#x09;- get ONE specific post by id

&#x09;Post.objects.get(id=2)



&#x09;- filter posts

&#x09;Post.objects.filter(author="Ali")



&#x09;- filter with condition

&#x09;Post.objects.filter(likes\_\_gt=10)  # likes greater than 10



&#x09;- order by

&#x09;Post.objects.all().order\_by('-likes')  # descending by likes



&#x09;- count

&#x09;Post.objects.count()



&#x09;- delete the post

&#x09;Post.objects.get(id=1).delete()

