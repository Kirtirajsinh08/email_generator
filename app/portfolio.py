import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path="app/resource/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name='portfolio')

    def load_portfolio(self):
        """Load portfolio CSV into ChromaDB (only if empty)."""
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=[row['Techstack']],
                    metadatas=[{'links': row["Links"]}],
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills):
        """Query Chroma collection with extracted skills and return portfolio links."""
        if not skills:  # handle empty input
            return []

        result = self.collection.query(query_texts=skills, n_results=2)
        # Flatten metadata results into a list of links
        links = [meta['links'] for sublist in result.get('metadatas', []) for meta in sublist if 'links' in meta]
        return links
