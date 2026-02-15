from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def open(self):
        pass


class Report(Document):
    def open(self):
        print("Opening Report document...")


class Resume(Document):
    def open(self):
        print("Opening Resume document...")


class Letter(Document):
    def open(self):
        print("Opening Letter document...")


class Invoice(Document):
    def open(self):
        print("Opening Invoice document...")


class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self):
        pass


class ReportCreator(DocumentCreator):
    def create_document(self):
        return Report()


class ResumeCreator(DocumentCreator):
    def create_document(self):
        return Resume()


class LetterCreator(DocumentCreator):
    def create_document(self):
        return Letter()


class InvoiceCreator(DocumentCreator):
    def create_document(self):
        return Invoice()


def main():
    print("1 - Report")
    print("2 - Resume")
    print("3 - Letter")
    print("4 - Invoice")

    choice = input("Choose document type: ")

    creator = None

    if choice == "1":
        creator = ReportCreator()
    elif choice == "2":
        creator = ResumeCreator()
    elif choice == "3":
        creator = LetterCreator()
    elif choice == "4":
        creator = InvoiceCreator()
    else:
        print("Invalid choice")
        return

    document = creator.create_document()
    document.open()


if __name__ == "__main__":
    main()
