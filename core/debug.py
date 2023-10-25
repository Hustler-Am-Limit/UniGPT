from langchain.vectorstores import VectorStore
from typing import Iterable, List, Any, Optional
from langchain.docstore.document import Document
from langchain.embeddings.base import Embeddings
from langchain.embeddings.fake import FakeEmbeddings as FakeEmbeddingsBase
from langchain.chat_models.fake import FakeListChatModel


class FakeChatModel(FakeListChatModel):
    def __init__(self, **kwargs):
        responses = ["""Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.

Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.

Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo.

Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, ."""]
        super().__init__(responses=responses, **kwargs)


class FakeEmbeddings(FakeEmbeddingsBase):
    def __init__(self, **kwargs):
        super().__init__(size=4, **kwargs)


class FakeVectorStore(VectorStore):
    """Fake vector store for testing purposes."""

    def __init__(self, texts: List[str]):
        self.texts: List[str] = texts

    def add_texts(
        self, texts: Iterable[str], metadatas: List[dict] | None = None, **kwargs: Any
    ) -> List[str]:
        self.texts.extend(texts)
        return self.texts

    @classmethod
    def from_texts(
        cls,
        texts: List[str],
        embedding: Embeddings,
        metadatas: Optional[List[dict]] = None,
        **kwargs: Any,
    ) -> "FakeVectorStore":
        return cls(texts=list(texts))

    def similarity_search(
        self, query: str, k: int = 4, **kwargs: Any
    ) -> List[Document]:
        return [
            Document(page_content=text, metadata={"source": f"{i+1}-{1}"})
            for i, text in enumerate(self.texts)
        ]
