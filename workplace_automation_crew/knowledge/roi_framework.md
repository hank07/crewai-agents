# Automation ROI Calculation Framework

## Core Formula

    Annual Saving = (Hours saved per week × Hourly cost × 52 weeks) - Annual tool cost
    Payback period (months) = Implementation cost / Monthly net saving

## Step 1: Calculate Current Manual Cost

    Hours spent on task per week: H
    Number of people doing it: N
    Fully-loaded hourly cost per person: C (use €50-80/hour for knowledge workers in EU)

    Weekly manual cost = H × N × C
    Annual manual cost = Weekly cost × 52

**Example**:
- 6 hours/week × 1 person × €60/hour = €360/week = €18,720/year

## Step 2: Estimate Automation Coverage

Not all steps will be fully automated. Estimate coverage per phase:

| Phase | Automation Coverage | Hours Saved/Week |
|-------|--------------------|--------------------|
| Phase 1 (Quick Win) | 20-30% | e.g., 1.5h |
| Phase 2 (Core) | 70-80% | e.g., 4.5h |
| Phase 3 (Full) | 85-95% | e.g., 5.5h |

Some manual oversight is always needed (edge case review, quality check).
Use 85-90% as realistic maximum automation for knowledge work.

## Step 3: Add Non-Time Benefits

- **Error reduction**: Estimate cost of manual errors (rework, decisions on bad data)
  - Conservative: €500-2,000/year for typical reporting errors
- **Faster availability**: Report available Friday 3pm instead of 6pm
  - Soft benefit: earlier decision-making
- **Scalability**: Automation handles 10x volume with no extra staff cost
  - Include if growth is expected

## Step 4: Calculate Implementation Cost

    Implementation cost = Engineering days × Day rate + Tool setup cost

| Item | Estimate |
|------|----------|
| Engineering time (internal) | 5-20 person-days depending on complexity |
| Internal day rate | €400-600/day (fully loaded) |
| Tool licences (one-time setup) | €0-500 |
| Training | 0.5-1 day per person × number of users |

**Example**: 10 engineer-days × €500 = €5,000 implementation cost

## Step 5: Calculate Ongoing Running Cost

| Cost | Typical Range |
|------|--------------|
| Tool subscriptions | €0-300/month |
| LLM API calls | €0.01-10/month (cheap at typical volumes) |
| Maintenance overhead | 0.5-1 hour/week of someone's time |

**Example**: Power Automate premium €15/user + LLM API €5 = €20/month

## Step 6: Build the Business Case

    Monthly saving = Hours saved/week × 4.33 × Hourly cost
    Monthly net saving = Monthly saving - Monthly running cost
    Payback period = Implementation cost / Monthly net saving

**Full Example**:
- Hours saved: 5h/week × €60/hour × 4.33 = €1,299/month saved
- Running cost: €20/month
- Net monthly saving: €1,279
- Implementation cost: €5,000
- Payback period: 5,000 / 1,279 = **3.9 months**
- Year 1 net saving: (1,279 × 12) - 5,000 = **€10,348**
- Year 2+ net saving (running cost only): **€15,108/year**

## Presenting the ROI

Always present three numbers prominently:
1. **Hours saved per week** (tangible, relatable)
2. **Payback period** (months to break even)
3. **Annual saving after Year 1** (the real business case)

Then add a qualitative line:
> "Beyond the €10,000 annual saving, this eliminates the Friday afternoon scramble,
> reduces errors that affect executive decisions, and frees the PM rotation
> from the most disliked task in the team."

## Common Mistakes to Avoid
- Do NOT assume 100% automation — always budget for exception handling
- Do NOT forget maintenance cost — automations break when source systems change
- Do NOT underestimate change management — users need to trust the automation output
- DO include error reduction in the business case — it's often as valuable as time saved
