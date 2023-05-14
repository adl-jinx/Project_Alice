book_content = ""

# Read the content of the book from the file
with open("alice_pg.txt", encoding="utf-8") as file:
    lines = file.readlines()

# Remove newlines and create a single string
book_content = "".join(lines)

# Save the book content to a new file
with open("book_output.txt", "w", encoding="utf-8") as output_file:
    output_file.write(book_content)

print("Book content saved to book_output.txt.")


with open("book_output.txt") as book_made:
    book_made.readlines()


print(book_made.readlines())