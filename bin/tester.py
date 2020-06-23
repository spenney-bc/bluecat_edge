#!/usr/local/bin/python3
"""
    This script is intended to show usage of the various functions contained in the
    bluecat_edge module.  It can be used for testing purposes if desired.
"""

import bluecat_edge
import bluecat_edge.color as color


def main():
    # Create two dicts to contain mappings between names and IDs of sites
    # and namespaces - purely for convenience
    ns_dict = dict()
    site_dict = dict()

    # Get a list of namespaces, sites, sitegroups, policies, and domain lists -
    # essentially all of the meaningful objects within Edge
    ns_list = bluecat_edge.list_ns()
    site_list = bluecat_edge.list_sites()
    sitegroup_list = bluecat_edge.list_site_groups()
    policy_list = bluecat_edge.list_policies()
    dl_list = bluecat_edge.list_dl()

    # Build my mappings for site, sitegroup, and namespaces names to IDs
    for site in site_list:
        site_dict[site.id] = site.name
    for sitegroup in sitegroup_list:
        site_dict[str(sitegroup.siteGroupId)] = "(GROUP) " + sitegroup.name
    for ns in ns_list:
        ns_dict[ns.id] = ns.name

    # Print some summary information about namespaces, sites, policies
    # and domain lists to prove that this all works.
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

    # Pull and display some sample query data to demonstrate how to build
    # query strings for Edge
    query_list = bluecat_edge.get_queries(batchSize=10, order="ASC", policyAction="Block")
    print(query_list)


if __name__ == "__main__":
    main()
