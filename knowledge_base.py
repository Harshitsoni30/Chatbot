# from phi.knowledge.text import TextKnowledgeBase
# from phi.vectordb.pgvector import PgVector

# knowledge_base = TextKnowledgeBase(
#     path="data/txt_files",
#     # Table name: ai.text_documents
#     vector_db=PgVector(
#         table_name="knowledge_base",
#         db_url = "postgresql+psycopg://ai:ai@localhost:5432/ai"
# ,
#     ),
# )

from phi.knowledge.text import TextKnowledgeBase
from phi.vectordb.pgvector import PgVector

class AgentKnowledge:
    def __init__(self, data=None):
        self.kb = TextKnowledgeBase(
            path="data/txt_files",
            vector_db=PgVector(
                table_name="knowledge_base",
                db_url="postgresql+psycopg://ai:ai@localhost:5432/ai"
            )
        )
        self.data = data or {}

    def query(self, question):
        # Optionally use self.data as fallback
        return self.kb.query(question)
