from typing import Dict, Type, TypeVar

from polyfactory.factories import DataclassFactory
from polyfactory.factories.pydantic_factory import ModelFactory

from template_service.contracts.template import CreateTemplateRequest
from template_service.features.templates.domain.template_models import TemplateModel
from template_service.features.templates.persistence.template_entities import Template

__all__ = ["TemplateAutoFixture"]

T = TypeVar("T")


class _TemplateFactory(DataclassFactory[Template]):
    __model__ = Template


class _TemplateModelFactory(DataclassFactory[TemplateModel]):
    __model__ = TemplateModel


class _CreateTemplateRequestFactory(ModelFactory[CreateTemplateRequest]):
    __model__ = CreateTemplateRequest


class TemplateAutoFixture:
    _factories: Dict[type, type] = {
        Template: _TemplateFactory,
        TemplateModel: _TemplateModelFactory,
        CreateTemplateRequest: _CreateTemplateRequestFactory,
    }

    @staticmethod
    def generate(model_type: Type[T]) -> T:
        factory = TemplateAutoFixture._factories.get(model_type)
        if factory is None:
            raise ValueError(f"No factory registered for {model_type!r}")
        return factory.build()
