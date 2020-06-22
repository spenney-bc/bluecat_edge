#!/usr/local/bin/python3

import bluecat_edge
import bluecat_edge.color as color

def main():
    ns_dict = dict()
    site_dict = dict()
    ns_list = bluecat_edge.list_ns()
    site_list = bluecat_edge.list_sites()
    sitegroup_list = bluecat_edge.list_site_groups()
    policy_list = bluecat_edge.list_policies()
    dl_list = bluecat_edge.list_dl()
    for site in site_list:
        site_dict[site.id] = site.name
    for sitegroup in sitegroup_list:
        site_dict[str(sitegroup.siteGroupId)] = "(GROUP) " + sitegroup.name
    for ns in ns_list:
        ns_dict[ns.id] = ns.name
    for ns in ns_list:
        print("NS: {:35.35s}{:5s}ID: {}".format(ns.name, " ", ns.id))
        if ns.description != "":
            print("{:3s}Desc: {}".format(" ", ns.description))
        for site in ns.associatedSiteSettings:
            print("{:6s}Site: {}".format(" ", site_dict[site.id]))
    for site in site_list:
        print("Site: {:35.35s}{:5s}ID: {}".format(site.name, " ", site.id))
        for ns in site.settings.associatedNamespaces:
            print("{:3s}NS: {:34.34s}{:5s}ID: {}".format(" ", ns.name,
                                                " ", ns.id))
    for policy in policy_list:
        print("Policy: {:35.35s}{:5s}ID: {}".format(policy.name, " ", policy.id))
        if policy.description != "":
            print("{:3s}Desc: {}".format(" ", policy.description))
        for site in policy.appliedTo:
            print("{:6s}Site: {}".format(" ", site_dict[site.name]))
    for dl in dl_list:
        print("DL: {:35.35s}{:5s}ID: {}".format(dl.name, " ", dl.id))
        print("{:4s}Count: {}{}{}".format(" ", color.fg.CYAN, dl.domainCount,
                                          color.fg.RESET))
        if dl.description != "":
            print("{:3s}Desc: {}".format(" ", dl.description))
    query_list = bluecat_edge.get_queries(batchSize=10, order="ASC", policyAction="Block")
    print(query_list)


if __name__ == "__main__":
    main()