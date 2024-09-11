# pylint: disable=[E0401, W0718, C0301, R0914]

"""
This module generates a vector database of restaurant information using ChromaDB.
It processes restaurant data, summarizes reviews, and stores the information in a vector database.
"""

from utils.helpers import documents_init, chromadb_init, format_restaurant_data, split_documents_and_add_to_collection

def main():
    """
    Main function to generate and store restaurant information in a vector database.
    
    Steps:
    1. Creates summarized documents for vector storage along with their metadata.
    2. Initializes the ChromaDB client and collection.
    3. Adds the summarized documents and metadata to the ChromaDB collection.
    """
    # Creating documents for vector store + metadata
    summarized_docs, restaurants_data = documents_init(
        'langchain_testing/test_data/medium-meh/restaurants_with_reviews.json'
    )
    formatted_metadata = format_restaurant_data(restaurants_data)

    # Initialize client and collection
    chroma = chromadb_init()

    # Add data to the database
    split_documents_and_add_to_collection(summarized_docs, formatted_metadata, chroma)

    print('Data is now in DB')

if __name__ == "__main__":
    main()
