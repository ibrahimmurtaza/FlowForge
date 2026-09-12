#!/bin/bash

# Array of ticket titles and their blockers
tickets=(
  [1]="User Registration & Login via Supabase Auth|None"
  [2]="Workspace Creation|1"
  [3]="Role-Based Access Control (RBAC) Foundation|2"
  [4]="User Invitation Flow|3"
  [5]="Data Provider Integration Management UI|3"
  [6]="OAuth Email Account Connection (Gmail)|3"
  [7]="OAuth Email Account Connection (Outlook)|6"
  [8]="Visual Flow Canvas with React Flow|3"
  [9]="Source Node: List Upload (CSV)|8"
  [10]="Source Node: Search (Data Provider Query)|8,5"
  [11]="Enrichment Node Configuration UI|8,5"
  [12]="Filter Node Configuration UI|8"
  [13]="Generate Message Node Configuration UI|8"
  [14]="Send Email Node Configuration UI|8,7"
  [15]="Flow Versioning on Edit|8"
  [16]="Celery Worker Setup & Basic Orchestration|2"
  [17]="List Upload Source Node Execution|9,16"
  [18]="Search Source Node Execution|10,16"
  [19]="Enrichment Node Execution (Apollo)|11,18"
  [20]="Enrichment Node Execution (Clearbit & Hunter.io)|19"
  [21]="Filter Node Execution|12,19"
  [22]="AI Message Generation Node Execution|13,21"
  [23]="Credit Pack Metering & Quota Enforcement|22"
  [24]="Bring Your Own Key (BYOK) for Anthropic API|23"
  [25]="Suppression List CRUD UI|3"
  [26]="Suppression List CSV Import/Export|25"
  [27]="Pre-Send Suppression Check|25"
  [28]="Unsubscribe Link Footer & Click Tracking|27"
  [29]="Email Bounce Detection & Auto-Suppression|27"
  [30]="Send Email Node Execution|14,22,27"
  [31]="Rate Limiting Enforcement (Hourly/Daily)|30"
  [32]="Test Mode|30"
  [33]="Per-Flow Cooldown Deduplication|30"
  [34]="Supabase Realtime Flow Run Log|30"
  [35]="Pause & Resume on Error|34"
  [36]="Inbound Email Polling & Storage|30"
  [37]="AI Reply Classification (Positive/Negative/OOO)|36"
  [38]="Auto-Suppress on Negative Reply Classification|37,27"
  [39]="Flow Run Results Table|34"
  [40]="Flow Run Summary Statistics|39"
  [41]="CSV Export of Flow Run Results|39"
  [42]="Flow Scheduling UI (Intervals + Time Picker)|30"
  [43]="Celery Beat Scheduled Flow Run Trigger|42"
  [44]="Golden Path Flow Templates|14"
  [45]="Email Notifications on Flow Run Completion/Failure|39"
  [46]="In-App Notifications|39"
  [47]="Slack Webhook Notification|39"
  [48]="Custom Webhook Notification|47"
  [49]="Docker Compose Deployment Package|43"
  [50]="Kubernetes Helm Charts|49"
)

# Label needs to be created first
gh label create ready-for-agent --description "Ready for agent implementation" --color 2ecc71 --force

for i in {1..50}; do
  IFS='|' read -r title blockers <<< "${tickets[$i]}"

  body="## Parent

  #2

  ## What to build

  $title

  ## Acceptance criteria

  - [ ] Criterion 1
  - [ ] Criterion 2

  ## Blocked by

  $blockers"

  echo "Creating issue $i: $title"
  issue_url=$(gh issue create --title "$i: $title" --body "$body" --label ready-for-agent)
  echo "Created: $issue_url"
done
