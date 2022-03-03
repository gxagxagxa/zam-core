from re import compile
from lazy import lazy
from resource_identifier.config import ZAM_CORE_CONFIG


def _determine_resource_catagory(result):
    part_1 = result.pop('product_part_01')
    part_2 = result.pop('product_part_02')
    part_3 = result.pop('product_part_03')
    part_4 = result.pop('product_part_04')

    result['project'] = part_1

    if 'ep' in part_2.lower():
        result['episode'] = part_2
        if part_3 in ZAM_CORE_CONFIG.config['ZAM_ASSET_TYPES']:
            result['category'] = 'asset'
            result['asset_type'] = part_3
            result['asset_name'] = part_4
        else:
            result['category'] = 'shot'
            result['sequence'] = part_3
            result['shot'] = part_4
    else:
        if part_2 in ZAM_CORE_CONFIG.config['ZAM_ASSET_TYPES']:
            result['category'] = 'asset'
            result['asset_type'] = part_2
            result['asset_name'] = part_3
        else:
            result['category'] = 'shot'
            result['sequence'] = part_2
            result['shot'] = part_3


def _determine_resource_type(result):
    if result['sub_path']:
        result['resource_type'] = result['sub_path'].split('/')[1]
    else:
        result['resource_type'] = None


class ZamResouceIdentifierBaseSolverMixin(object):
    pre_parse_functions = []
    post_parse_functions = [_determine_resource_catagory,
                            _determine_resource_type]

    @lazy
    def short_url(self) -> str:
        return ''

    @lazy
    def full_url(self) -> str:
        pattern = ZAM_CORE_CONFIG.config['ZAM_RESOURCE_IDENTIFIER_FULL_URL']
        return pattern.format(zam_core_api_version=ZAM_CORE_CONFIG.config['ZAM_CORE_API_VERSION'],
                              site='beijing',
                              resource=self)

    def post_parse_process(self, result):
        for func in __class__.post_parse_functions:
            func(result)

    def pre_parse_process(self, result):
        for func in __class__.pre_parse_functions:
            func(result)

    @lazy
    def parse(self):
        def traverse_parse(string, regex_component):
            if (not regex_component):
                return

            result[regex_component['name']] = string
            if string and regex_component['regex'] and regex_component['component_mappings']:
                regex = compile(regex_component['regex'])
                match = regex.match(string)
                if match:
                    for string_component, regex_component in zip(match.groups(), regex_component['component_mappings']):
                        traverse_parse(string_component, regex_component)
                else:
                    raise ValueError('Resource ID not match Regex: \n{}\n{}'.format(
                        string, regex_component['regex']))

        result = dict()
        regex_config = ZAM_CORE_CONFIG.config['ZAM_RESOURCE_IDENTIFIER_SYNTAX']
        self.pre_parse_process(result)
        traverse_parse(self, regex_config)
        print(result)
        self.post_parse_process(result)

        return result


class ZamResourceIdentifierDataBaseSolverMixin(object):
    def database_id(self) -> str:
        return ''


class ZamResourceIdentifierFilePathSolverMixin(object):
    def file_path(self) -> str:
        return ''


class ZamResouceIdentifierRestApiSolverMixin(object):
    def rest_api(self) -> str:
        return ''
