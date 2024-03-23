from fastapi import APIRouter,Query,Body,Path
from pydantic import BaseModel
from typing import Optional,List, Dict
from fastapi.params import Body

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)
class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    nb_comment: int
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1': 'value1'}
    image: Optional[Image] = None
    
@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version,
        }

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int,
        comment_title: int = Query(None, 
            title="Title of the comment",
            description="Some description for comment title",
            alias="CommentTitle",
            deprecated=True
        ),
        content: str = Body(...,
                            min_length=10,
                            max_length=18,
                           ),
        v: Optional[List[str]] = Query(['1.1', '1.2', '1.3']),
        comment_id: int = Path()
        ):
    return {
        'id': id,
        'data': blog,
        'comment_title': comment_title,
        'content': content,
        'version': v,
        'comment_id': comment_id
    }

def required_functinality():
    return {'message': 'FastAPI learning module'}