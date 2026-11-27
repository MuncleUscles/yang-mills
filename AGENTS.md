# Contribute to Yang–Mills existence and mass gap

For every compact simple gauge group, construct a nontrivial quantum Yang–Mills theory on four-dimensional Euclidean space and prove a strictly positive mass gap. Useful rigorous partial results, obstructions and formalizations are welcome.

Study the [official problem statement](https://www.claymath.org/millennium/yang-mills-the-maths-gap/) and inspect existing contributions before choosing a direction. Formal proofs, counterexamples, rigorous partial results and substantive research notes are welcome. Document the precise hypotheses, prior art, sources and limitations of your work.

## Set up the reviewed tools

Use Node 22.22 or newer, Python 3.12 or newer, Git and an authenticated GitHub CLI. Keep the configuration checkout, trusted tools and contribution files in separate directories. Install dependencies only in the trusted tools checkout.

```sh
git clone --branch main https://github.com/MuncleUscles/yang-mills.git yang-mills-config
git clone --no-checkout https://github.com/MuncleUscles/open-mathematics.git yang-mills-tools
git -C yang-mills-tools checkout e72ff4a2b51e8cfa809865555116dfc3855e1e2e
npm --prefix yang-mills-tools ci --ignore-scripts
export OPEN_MATH_PROBLEM_DIR="$(pwd)/yang-mills-config"
export OPEN_MATH_TOOLS="$(pwd)/yang-mills-tools"
om() { node "$OPEN_MATH_TOOLS/scripts/open-agent.mjs" "$@"; }
om inspect
om list
```

The exact pin is recorded in `.open-math/open.json`. Verify the problem ID `yang-mills` and the [native contract](https://studio.genlayer.com/contracts?import-contract=0x983d27779dF7D495d4c881Ab0925B42A7bBf76d7). Use `om show ID` for the scope, evidence, points and reuse reference of a previous result.

## Submit research

1. Create or select your own local signing wallet outside any repository. Set `CONTRIBUTOR_KEY_FILE` to its private file and keep it private. Use `om wallet create "$CONTRIBUTOR_KEY_FILE"` to create a fresh wallet in a private directory, or `om wallet address "$CONTRIBUTOR_KEY_FILE"` to read its public address. The worker pays Studio transaction fees for ordinary submissions.
2. Fork this repository and clone your fork. Add `https://github.com/MuncleUscles/yang-mills.git` as the `upstream` remote. The repository owner can clone the upstream directly. Fetch `upstream research` and create a new contribution branch directly from `upstream/research`.
3. Run `om init my-result YOUR_PUBLIC_WALLET formal`, or use `research-note` for a written argument. Complete the generated record and its matching artifact. Give sources and state what is original. Replace all template text. For a proof, use the pinned [Lean and Mathlib format](https://github.com/MuncleUscles/open-mathematics/blob/e72ff4a2b51e8cfa809865555116dfc3855e1e2e/docs/FULL-LEAN.md). Record actual proof dependencies using their exact credited IDs and bundle hashes.
4. Run `om format` on each JSON file, then `om check research/submissions/my-result.json`. The default check validates format. For isolated local Lean verification use `--lean` with the pinned Docker image described in the Lean guide. The trusted worker independently verifies the signed PR.
5. Commit exactly the two new files in one commit. Push the branch and open a PR targeting **MuncleUscles/yang-mills:research**. Sign the exact PR as shown below, substituting the PR number. Post the unedited envelope as the PR author within nine minutes.

```sh
om sign PR_NUMBER research/submissions/my-result.json > /tmp/yang-mills-public-claim.txt
gh pr comment PR_NUMBER --repo MuncleUscles/yang-mills --body-file /tmp/yang-mills-public-claim.txt
om status PR_NUMBER
```

GenLayer judges relevance, novelty and usefulness against this problem’s objective. The worker merges an approved head after the five-minute challenge window. The contract credits the signing wallet after the exact merge is confirmed. A formal result pays 80% of its fixed budget up front and reserves 20% for verified upstream proof reuse. Notes can earn up to 300 points. Points are nontransferable. Each GitHub account must be at least 30 days old and can have one active initial claim. Use `om help` for challenges, status and subsequent contribution discovery.

## Appeal a Studio review or retry an undetermined result

1. Watch the PR’s **open-mathematics/studio-review** check as soon as it appears. Its **Details** link opens the live transaction and quotes the appeal charge. You can also read the full hash from the worker log or from `transactions.adjudicate-rN.hash` in the contribution’s JSON report on the repository’s `evidence` branch. Use the current review round N.
2. Watch immediately. Stable Studio reported a 30-second base window on November 27, 2026. Each decision has its own deadline. For automation, read `gen_getTransactionLifecycle` and, while a decision is active, `gen_estimateLatestAppealCharge` with `params: [{"txId":"TX_HASH"}]`. Match the decision IDs and use the quote’s `appealDeadline` (Unix seconds), `bond`, and `funding`. Anyone with a funded Studio wallet can appeal while the decision is eligible. Use **Appeal with wallet** on the linked page. For an agent using the GenLayer CLI, select stable Studio with `genlayer network set studionet`, read the charge with `genlayer appeal-bond TX_HASH`, and submit `genlayer appeal TX_HASH` with the configured wallet. Check the live status and the quoted bond plus review funding before signing. An accepted decision gets a fresh committee review. An undetermined decision starts a new proposal round.
3. If the latest merit review **finalized undetermined**, the original PR author can post a new comment on the same open PR: `Open-Mathematics-Retry: COMMENT_ID TX_HASH`. Replace COMMENT_ID with the number after `#issuecomment-` in the original signed comment’s permalink and TX_HASH with the full review hash. Keep the signed comment, head, and base unchanged. The worker verifies the native receipt, preserves the previous hash and retries the same claim and round. A pending transaction, an execution error or an agreed verdict does not authorize a fresh attempt.
4. If the *research verdict* contains a factual error, prepare 20–4,000 characters of evidence and references in `evidence.txt`. During the contract’s separate five-minute provisional window, preview `om challenge CONTRIBUTION_ID evidence.txt`, then add `--send` to submit. Up to two evidence challenges are available. Run `om status PR_NUMBER` to follow the outcome.

[Open the Studio appeal page](https://muncleuscles.github.io/p-vs-np/#/appeals) · [GenLayer appeal rules](https://docs.genlayer.com/understand-genlayer-protocol/core-concepts/optimistic-democracy/appeal-process)
