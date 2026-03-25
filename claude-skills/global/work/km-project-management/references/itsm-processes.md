# IT Service Management Processes (KM-PROC-0149)

KM's ITSM framework based on ITIL practices, applicable to all IT services within the KONGSBERG Group.

## Table of Contents
- [Information Security Management](#information-security-management)
- [IT Project Management](#it-project-management)
- [Access Management](#access-management)
- [Incident Management](#incident-management)
- [IT Change Management](#it-change-management)
- [IT Configuration Management](#it-configuration-management)
- [IT Service Continuity Management](#it-service-continuity-management)
- [Knowledge Management](#knowledge-management)
- [Monitoring and Event Management](#monitoring-and-event-management)
- [Problem Management](#problem-management)
- [Release and Deployment Management](#release-and-deployment-management)
- [Service Level Management](#service-level-management)
- [Service Catalogue Management](#service-catalogue-management)
- [Service Request Management](#service-request-management)
- [Service Validation and Testing](#service-validation-and-testing)

## Information Security Management

Protect information confidentiality, integrity, and availability. Policies cover: IT asset use/misuse, access control, passwords, communications/social media, malware protection, information classification, remote access, supplier access, IP, records retention, personal data protection.

## IT Project Management

Applies to all IT projects executed by KONGSBERG IT across all subsidiaries. IT Project Manager ensures process compliance.

Phases:
1. **Analyse and Plan** — Detailed preparation for execution
2. **Execute** — Project mandate put into action
3. **Archive** — Per LODL requirements

## Access Management

Three user categories:
- **Standard user**: Employees, temporary, consultants, interns, apprentices
- **Personal Non-Standard**: Admin, DMZ (incl. external), Guest, Test accounts
- **Non-standard**: System accounts

## Incident Management

Flow: Raise ticket → Analyse → Handle escalation → Implement resolution → Close (auto-close after defined period) → Periodic review

## IT Change Management

Flow: Create Change → Validate (IT Change Manager) → Assess (technical feasibility, risks) → Authorize (CAB review) → Schedule → Implement → Review (post-implementation) → Close

Multiple change types exist with fewer steps, documented in procedures.

## IT Configuration Management

Two sub-processes:
1. Plan IT Configuration Management
2. IT Configuration Identification

## IT Service Continuity Management

Goal: Ensure IT service recovery after major incidents/disasters. Covers proactive risk reduction and reactive recovery.

**Backup process:**
- Server preparation (backup software install, client group assignment, schedule/retention configuration)
- Daily backup operations (error logging, alert checks, monthly tape backup)
- Restore process (find file/date, check disk/tape availability, prepare and restore)
- Backup stop procedure (disable machine, inform organization, remove after retention period)

Data stored on disk for 10 weeks, then on tape until retention limit.

## Knowledge Management

Flow: Create/Update article (Contributor) → Review (periodic validity checks) → Publish (Knowledge Manager) → Retire

## Monitoring and Event Management

Flow: Detect event (manual/automatic monitoring, logs, scheduled jobs) → Evaluate (check security, correlate, check impact) → Assign (if unresolvable in group) → Close (corrective actions, verify service, inform stakeholders)

## Problem Management

Flow: Raise ticket → Assess → Root Cause Analysis → Fix in Progress → Resolve (verify fix/workaround) → Close

## Release and Deployment Management

Flow:
1. **Plan deployment** — Content/change log, time schedule, inform customers per SLA, inform 1st Line Support
2. **Plan and prepare release** — Scope, stakeholders, responsibilities, schedule, acceptance test plan, configuration changes, server environment
3. **Install release** — Deploy per SLA, staging area procedure
4. **Prepare for test** — Assemble components, install on stage/test, run configurations
5. **Verify test/release** — 10-minute verification of key features and data
6. **Test and approve** — FAT with customer on staging, error correction
7. **Close change/task** — Complete documentation, review open changes/incidents, publish user docs, remove notifications

## Service Level Management

Flow: Negotiate agreements (triggered by reviews, service changes, or breaches) → Create/update SLA → Implement service levels (ITSM tool or manual) → Monitor and report

## Service Catalogue Management

Flow: Request new/modify/retire service → Review completeness → Create/modify catalogue item → Retire or Review (with Business Service Owner for business services) → Refine based on feedback → Raise Change → Apply to production → Close

## Service Request Management

Flow: Submit request (from catalogue) → Approve → Complete tasks → Close

## Service Validation and Testing

Links to both Projects and Changes. Ensures new/changed products and services meet defined requirements using a common methodology.
