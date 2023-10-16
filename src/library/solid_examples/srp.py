# 1. Single Responsibility Principle (SRP):

# Description:
# The Single Responsibility Principle (SRP) states that a class should have only one reason to change.
# In other words, a class should have only one responsibility or job.
#
# Benefits:
#
# Maintainability: Classes with a single responsibility are easier to understand and maintain.
#                  Changes are localized to one area of the codebase.
#
# Flexibility: When a class has only one responsibility,
#              it's easier to adapt it to new requirements without affecting other parts of the system.
#
# Readability: Code is more readable because each class has a clear and focused purpose.

class FileManager:
    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def write_file(self, file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)