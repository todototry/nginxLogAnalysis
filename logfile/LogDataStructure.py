#this script is create for ----
__author__ = 'fandongyun'


class LogDataStructure(object):
    def __init__(self, datalinesplited):
        self.__dict__ = {
            "remote_addr": datalinesplited.remote_addr,
            "remote_user": datalinesplited.remote_user,
            "time_local": datalinesplited.time_local,
            "time_zone": datalinesplited.time_zone,
            "request_method": datalinesplited.request_method,
            "request_url": datalinesplited.request_url,
            "request_protocol": datalinesplited.request_protocol,
            "response_status": datalinesplited.response_status,
            "body_bytes_sent": datalinesplited.body_bytes_sent,
            "http_referer": datalinesplited.http_referer,
            "user_agent":datalinesplited.user_agent,
            "user_agent_ver": datalinesplited.user_agent_ver,
            "user_agent_info": datalinesplited.user_agent_info,
            "http_x_forwarded_for": datalinesplited.http_x_forwarded_for,
            "server_name": datalinesplited.server_name,
            "proxy_host": datalinesplited.proxy_host,
            "upstream_addr": datalinesplited.upstream_addr,
            "http_uuid": datalinesplited.http_uuid,
            "http_session_token": datalinesplited.http_session_token
        }

    @property
    def log_data(self):
        return self.__dict__

