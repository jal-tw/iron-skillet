# xpaths as python dictionary with name as a key
# %(text)s variables showing xpath variables - python substitution

xpaths_panorama = {
      "address": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/address",
      "decryption_rules_post": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/post-rulebase/decryption", 
      "decryption_rules_pre": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/pre-rulebase/decryption", 
      "default_security_rules": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/post-rulebase/default-security-rules",
      "device_group": "/config/devices/entry[@name='localhost.localdomain']/device-group",
      "device_setting": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/devices/entry[@name='localhost.localdomain']/deviceconfig/setting",
      "device_system": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/devices/entry[@name='localhost.localdomain']/deviceconfig/system",
      "dhcp_server": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/devices/entry[@name='localhost.localdomain']/network/dhcp/interface/entry[@name='%(port)s']/server",
      "email_scheduler": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/email-scheduler",
      "external_list": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/external-list",      
      "gpcs_service_connection": "/config/devices/entry[@name='localhost.localdomain']/plugins/cloud_services/service-connection",
      "gpcs_trusted-zone": "/config/devices/entry[@name='localhost.localdomain']/plugins/cloud_services/remote-networks/trusted-zones",
      "gpcs_onboarding": "/config/devices/entry[@name='localhost.localdomain']/plugins/cloud_services/remote-networks/onboarding",
      "ike_gateway": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/devices/entry[@name='localhost.localdomain']/network/ike",
      "interface": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/devices/entry[@name='localhost.localdomain']/network/interface",
      "ipsec_tunnel": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/devices/entry[@name='localhost.localdomain']/network/tunnel",
      "log_collector_group": "/config/devices/entry[@name='localhost.localdomain']/log-collector-group",
      "log_settings": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/shared/log-settings",
      "log_settings_profiles": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/log-settings/profiles",
      "nat": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/post-rulebase/nat",
      "network_profiles": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/devices/entry[@name='localhost.localdomain']/network/profiles",
      "ntp_servers": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/devices/entry[@name='localhost.localdomain']/deviceconfig/system/ntp-servers",
      "panorama_log_settings": "/config/panorama/log-settings",
      "panorama_setting": "/config/devices/entry[@name='localhost.localdomain']/deviceconfig/setting",
      "panorama_system": "/config/devices/entry[@name='localhost.localdomain']/deviceconfig/system",
      "profile_group": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/profile-group",
      "profiles_custom_url_category": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/profiles/custom-url-category",
      "profiles_decryption": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/profiles/decryption",
      "profiles_file_blocking": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/profiles/file-blocking",
      "profiles_spyware": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/profiles/spyware",
      "profiles_url_filtering": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/profiles/url-filtering",
      "profiles_virus": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/profiles/virus",
      "profiles_vulnerability": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/profiles/vulnerability",
      "profiles_wildfire_analysis": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/profiles/wildfire-analysis",
      "reports": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/reports",
      "report_group": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/report-group",
      "route_service": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/devices/entry[@name='localhost.localdomain']/deviceconfig/system/route/service/entry[@name='%(route_service)s']",
      "security_rules_post": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/post-rulebase/security",
      "security_rules_pre": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/pre-rulebase/security",
      "server_profile": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/shared/server-profile",
      "service": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/service",
      "shared_address": "/config/shared/address",
      "shared_external_list": "/config/shared/external-list",
      "shared_log_settings": "/config/shared/log-settings",
      "shared_log_settings_profiles": "/config/shared/log-settings/profiles",
      "shared_post_rulebase_decryption": "/config/shared/post-rulebase/decryption",
      "shared_post_rulebase_security": "/config/shared/post-rulebase/security",
      "shared_post_rulebase_default_security_rules": "/config/shared/post-rulebase/default-security-rules",
      "shared_pre_rulebase_decryption": "/config/shared/pre-rulebase/decryption",
      "shared_pre_rulebase_security": "/config/shared/pre-rulebase/security",
      "shared_profiles": "/config/shared/profiles",
      "shared_profiles_custom_url_category": "/config/shared/profiles/custom-url-category",
      "shared_profiles_decryption": "/config/shared/profiles/decryption",
      "shared_profiles_file_blocking": "/config/shared/profiles/file-blocking",
      "shared_profiles_spyware": "/config/shared/profiles/spyware",
      "shared_profiles_url_filtering": "/config/shared/profiles/url-filtering",
      "shared_profiles_virus": "/config/shared/profiles/virus",
      "shared_profiles_vulnerability": "/config/shared/profiles/vulnerability",
      "shared_profiles_wildfire_analysis": "/config/shared/profiles/wildfire-analysis",
      "shared_profile_group": "/config/shared/profile-group",
      "shared_report_group": "/config/shared/report-group",
      "shared_tag": "/config/shared/tag",
      "tag": "/config/devices/entry[@name='localhost.localdomain']/device-group/entry[@name='%(devicegroup)s']/tag",
      "template": "/config/devices/entry[@name='localhost.localdomain']/template",
      "template-stack": "/config/devices/entry[@name='localhost.localdomain']/template-stack",
      "update_schedule": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/devices/entry[@name='localhost.localdomain']/deviceconfig/system/update-schedule",
      "userid_agent": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/user-id-agent",
      "userid_group_mapping": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/group-mapping",
      "virtual_router": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/devices/entry[@name='localhost.localdomain']/network/virtual-router",
      "wildfire": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/devices/entry[@name='localhost.localdomain']/deviceconfig/setting/wildfire",
      "zone": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/zone",
      "zone_import_interface": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/import",
      "zone_protection_profile": "/config/devices/entry[@name='localhost.localdomain']/template/entry[@name='%(pan_template)s']/config/devices/entry[@name='localhost.localdomain']/network/profiles/zone-protection-profile",
            }
