import os
import logging

from django.core.management.base import BaseCommand  # CommandError

from container_pipeline.models.tracking import ContainerImage
from jenkinsbuilder.cccp_index_reader import get_projects_from_index

from django.conf import settings

if not settings.configured:
    settings.configure()

logger = logging.getLogger('tracking')


class Command(BaseCommand):
    help = 'Fetch container image list from registry'
    args = "<indexd path>"
    can_import_settings = True
    output_transaction = True

    def handle(self, *args, **options):
        try:
            indexd_path = args[0]
            if not indexd_path.startswith('/'):
                indexd_path = os.path.abspath(
                    os.path.join(os.getcwd(), indexd_path))
        except IndexError:
            indexd_path = settings.INDEXD_PATH
        logger.debug('Fetching image list from index at %s' % indexd_path)
        projects = get_projects_from_index(indexd_path)
        deps_map = {}

        # Create container image entries
        for p in projects:
            project = p[0]['project']
            image_name = '{}/{}:{}'.format(
                project['appid'], project['jobid'], project['desired_tag'])
            c, created = ContainerImage.objects.get_or_create(name=image_name)
            if created:
                logger.debug('Created container image: %s' % c)
            deps = project.get('depends_on_img') or []
            if not isinstance(deps, list):
                deps = [deps]
            deps_map[c.name] = deps

        logger.info('Fetched image list from index')

        logger.debug('Populating image dependencies')
        # Populate container dependencies
        for image_name, parents in deps_map.items():
            c = ContainerImage.objects.get(name=image_name)
            parents = ContainerImage.objects.filter(name__in=parents)
            c.parents.clear()
            c.parents.add(*list(parents))
            logger.debug('Updated parents for container %s: %s' % (
                c, c.parents.all()))
        logger.info('Populated image dependencies')
