#lists methods:
course = ["Math", "Science", "English", "History", "Art"]

print("Original List:", course)

print("Length of List:", len(course))

print("First Course:", course[0])

print("Last Course:", course[-1])

print("Courses from index 1 to 3:", course[1:4])

print("course :"[:3])

print("courses from index 2:"[2:])

course.append("biology")

print("List after appending 'biology':", course)    

course.insert(3, "mechanics")

print("List after inserting 'mechanics' at index 3:", course) 

courses_2 = ["Geography", "Physics"]

course.extend(courses_2)

print("List after extending with another list:", course)

course.remove("Math")

print("List after removing 'Math':", course)

course.pop()

print("List after popping the last element:", course)


popped = course.pop(2)
print("Popped element:", popped)

course.reverse()
print("List after reversing:", course)  

course.sort(reverse=True)
print("List after sorting in descending order:", course)    

sorted_course = sorted(course)
print("Sorted List in ascending order:", sorted_course)

num = [5, 2, 9, 1, 7]

print(min(num))
print(max(num))
print(sum(num))


print(course.index("Geography"))

print("Science" in course)

for item in course:
    print(item)

for index, course in (enumerate(course)):
    print(index, course)


for index, course in (enumerate(course, start = 1)):

    print(index, course)

#tuples and sets methods:

a = ["apple", "banana", "cherry"]
a = ','.join(a)
print(a)

b = "apple,banana,cherry"

c = b.split('-')
print(c)

d = {'bmw', 'audi', 'toyota'}
e = {'ford', 'honda', 'toyota'}

print(d.intersection(e))
print(d.difference(e))
print(d.union(e))
