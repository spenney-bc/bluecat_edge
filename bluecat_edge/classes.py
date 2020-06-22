from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List, Optional


@dataclass_json
@dataclass
class AssociatedSiteSettings:
    id: str
    overridingForwarders: Optional[List[str]]


@dataclass_json
@dataclass
class Namespace:
    name: str
    id: str
    isDefault: bool
    forwarders: List[str]
    description: Optional[str]
    umbrellaIntegrationId: Optional[str] = ""
    associatedSiteSettings: Optional[List[AssociatedSiteSettings]] \
        = field(default_factory=list)
    exceptionLists: Optional[List[str]] = field(default_factory=list)
    matchLists: Optional[List[str]] = field(default_factory=list)
    overridingForwarders: Optional[List[str]] = field(default_factory=list)
    ttl: int = 0


@dataclass_json
@dataclass
class Location(object):
    lat: str = ""
    lng: str = ""
    address: str = ""


@dataclass_json
@dataclass
class SiteSettings(object):
    timeZone: str
    associatedNamespaces: List[Namespace] = field(default_factory=list)


@dataclass_json
@dataclass
class Site:
    name: str = ""
    id: str = ""
    registeredServicePointCount: int = 0
    updateStatus: Optional[str] = None
    updateInitiatedTime: int = 0
    version: str = ""
    blockedServicePointIds: List[str] = field(default_factory=list)
    location: Location = field(default_factory=dict)
    settings: SiteSettings = field(default_factory=dict)


@dataclass_json
@dataclass
class SiteGroup:
    name: str
    siteGroupId: int
    description: str = ""
    siteIds: List[str] = field(default_factory=list)


@dataclass_json
@dataclass
class PolicySite:
    type: str = field(default_factory=str)
    name: str = field(default_factory=str)


@dataclass_json
@dataclass
class PolicyIps:
    type: str = ""
    ranges: List[str] = field(default_factory=list)


@dataclass_json
@dataclass
class PolicyDomain:
    type: str = ""
    listId: str = ""


@dataclass_json
@dataclass
class PolicyExceptionDL:
    type: str = ""
    listId: str = ""


@dataclass_json
@dataclass
class Policy:
    name: str
    id: str
    timestamp: int
    policyVersionId: str
    active: bool
    matchAnswer: bool
    matchAuthority: bool
    action: dict
    description: str = ""
    redirectTarget: str = field(default_factory=str)
    appliedTo: List[PolicySite] = field(default_factory=dict)
    domain: List[PolicyDomain] = field(default_factory=dict)
    exceptionDomainLists: List[PolicyExceptionDL] = field(default_factory=list)
    sourceIps: PolicyIps = field(default_factory=dict)
    threats: List[dict] = field(default_factory=dict)
    queryTypes: List[str] = field(default_factory=str)


@dataclass_json
@dataclass
class DomainList:
    name: str
    id: str
    sourceConfiguration: Optional[str]
    sourceType: str
    domainCount: int = 0
    description: str = ""


@dataclass_json
@dataclass
class Authority:
    domainName: str
    parsed: bool
    rData: str
    recordType: str


@dataclass_json
@dataclass
class QueriedNamespaces:
    id: str
    name: str


@dataclass_json
@dataclass
class Answer:
    domainName: str
    parsed: bool
    rData: str
    recordType: str


@dataclass_json
@dataclass
class Threats:
    indicators: List[str]
    type: str


@dataclass_json
@dataclass
class MatchedPolicy:
    id: str
    name: str


@dataclass_json
@dataclass
class Query:
    id: str
    time: int
    source: str
    siteId: str
    query: str
    queryType: str
    actionTaken: str
    response: str
    matchedPolicies: Optional[List[MatchedPolicy]]
    answers: Optional[List[Answer]]
    authority: Optional[List[Authority]]
    queryProtocol: str
    threats: Optional[List[Threats]]
    queriedNamespaces: Optional[List[QueriedNamespaces]]
    latency: int
