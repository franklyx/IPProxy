#!/usr/bin/env sh

supervisord -c /etc/supervisor/supervisord.conf
supervisorctl -c /etc/supervisor/supervisord.conf