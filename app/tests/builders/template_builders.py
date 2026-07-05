from polyfactory.factories import DataclassFactory
from polyfactory.factories.pydantic_factory import ModelFactory

from template_service.contracts.template import CreateTemplateRequest
from template_service.features.templates.domain.template_models import TemplateModel
from template_service.features.templates.persistence.template_entities import Template


class TemplateFactory(DataclassFactory[Template]):
    __model__ = Template


class TemplateModelFactory(DataclassFactory[TemplateModel]):
    __model__ = TemplateModel


class CreateTemplateRequestFactory(ModelFactory[CreateTemplateRequest]):
    __model__ = CreateTemplateRequest
