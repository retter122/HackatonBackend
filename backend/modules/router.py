from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from .scemas import ModuleCreate, ModuleRead, ModuleEdit
from .relscemas import ModuleRel
from .models import Module
from .filesystem import create_document, write_to_document, delete_document

from ..user.models import User
from ..user.auth import get_current_user
from ..db.depencies import get_session

router = APIRouter(prefix="/modules", tags=["modules"])


@router.delete("/{module_id}")
async def delete_module(module_id: int, user: User = Depends(get_current_user),
                        session: AsyncSession = Depends(get_session)) -> ModuleRead:
    module = await session.scalar(Module.get_by_id(module_id))

    if not module:
        raise HTTPException(404)

    delete_document(module.document)

    module_ret = ModuleRead.model_validate(module, from_attributes=True)

    try:
        await session.delete(module)

        await session.commit()
    except Exception as e:
        raise HTTPException(403)

    return module_ret


@router.post("/")
async def create_module(module_new: ModuleCreate, user: User = Depends(get_current_user),
                        session: AsyncSession = Depends(get_session)) -> ModuleRead:
    document = create_document(user.id)

    module = Module(name=module_new.name, description=module_new.description, document=document,
                    source_id=module_new.source_id)

    try:
        session.add(module)

        await session.commit()
    except Exception as e:
        raise HTTPException(403)

    return ModuleRead.model_validate(module, from_attributes=True)


@router.post('/document/')
async def upload_document(module_id: int, document: UploadFile = File(), user: User = Depends(get_current_user),
                          session: AsyncSession = Depends(get_session)) -> ModuleRead:
    module = await session.scalar(Module.get_by_id(module_id))

    if not module:
        raise HTTPException(404)

    write_to_document(module.document, await document.read())

    return ModuleRead.model_validate(module, from_attributes=True)


@router.put("/")
async def edit_document(module_edit: ModuleEdit, user: User = Depends(get_current_user),
                        session: AsyncSession = Depends(get_session)) -> ModuleRead:
    module = await session.scalar(Module.get_by_id(module_edit.id))

    if not module:
        raise HTTPException(404)

    try:
        module.name = module_edit.name
        module.description = module_edit.description

        await session.commit()
    except Exception as e:
        raise HTTPException(403)

    return ModuleRead.model_validate(module)


@router.get("/{module_id}")
async def get_module(module_id: int, user: User = Depends(get_current_user),
                     session: AsyncSession = Depends(get_session)) -> ModuleRel:
    module = await session.scalar(Module.get_by_id(module_id))

    if not module:
        raise HTTPException(404)

    return ModuleRel.model_validate(module, from_attributes=True)