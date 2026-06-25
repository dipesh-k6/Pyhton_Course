**Question:** 

Create a dictionary for a blog post with these keys:                                  - its same as objects in js



* title
* author
* likes (a number)
* published (True or False)



Then:



* Print just the title
* Increase likes by 10
* Add a new key tags as a list of 3 topic strings
* Print the final dictionary



**Answer:** 



blog_post = {

   "title": "AI Awakening",

  "author": "Robert Mark",   

   "likes": 35,

   "published": True,

}



print(blog_post["title"])     - we dont use blog_post.title()



blog_post["likes"] += 10

blog_post["tags"] = ["AI", "Robert", "Awakening"]        



print(blog_post)



-----------------------------------------------------------------------------------------------------------------------------------------------



print(blog_post.keys())    - all keys

print(blog_post.values())  - all values

print(blog_post.items())   - key-value pairs together

print(blog_post["rating"])          - ❌ crashes if key missing

print(blog_post.get("rating"))      - ✅ returns None safely

print(blog_post.get("rating", 0))   - ✅ returns 0 as default



-------------------------------------------------------------------------------------------------------------------------------------------------

**Question:**

Build a small blog system:



Create a function called create_post that:



* Takes title, author, likes as parameters
* likes should default to 0
* Returns a dictionary with those keys plus "published": False





Create 3 blog posts using your function and store them in a list

Write a function called find_most_liked that:



* Takes the list of posts
* Returns the post with the highest likes





**Answer:**

post_list = []



def create_post(title, author, likes = 0):

   post = {

       "title": title,

       "author": author,

       "likes": likes,

       "published": False,

  }

   post_list.append(post)

   return post



def most_liked_post(post_list):

   result = post_list[0]

   for post in post_list:

       if(post.get("likes") > result.get("likes")):

           result = post



   return result



create_post("abcd", "adam", 12)

create_post("efgh", "eve")

create_post("ijkl", "smith", 13)



print(most_liked_post(post_list))





\-

