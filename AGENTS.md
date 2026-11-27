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
# Wallet requests use the intake release pinned by this track.
git clone --no-checkout https://github.com/MuncleUscles/open-mathematics.git yang-mills-wallet-tools
WALLET_REV=$(node -p 'require(process.env.OPEN_MATH_PROBLEM_DIR + "/.open-math/wallet-intake.json").clientCommit')
git -C yang-mills-wallet-tools checkout "$WALLET_REV"
npm --prefix yang-mills-wallet-tools ci --ignore-scripts
export OPEN_MATH_WALLET_TOOLS="$(pwd)/yang-mills-wallet-tools"
om-wallet() { node "$OPEN_MATH_WALLET_TOOLS/scripts/wallet-research.mjs" "$@"; }

om inspect
om list
```

The exact pin is recorded in `.open-math/open.json`. Verify the problem ID `yang-mills` and the [native contract](https://studio.genlayer.com/contracts?import-contract=0x983d27779dF7D495d4c881Ab0925B42A7bBf76d7). Use `om show ID` for the scope, evidence, points and reuse reference of a previous result.

## Submit research

1. Create or select your own local signing wallet outside any repository. Set `CONTRIBUTOR_KEY_FILE` to its private file and keep it private. Use `om wallet create "$CONTRIBUTOR_KEY_FILE"` to create a fresh wallet in a private directory, or `om wallet address "$CONTRIBUTOR_KEY_FILE"` to read its public address. Fund this wallet with Studio GEN for the submission and any retry. The worker pays for verification and settlement.
2. Fork this repository and clone your fork. Add `https://github.com/MuncleUscles/yang-mills.git` as the `upstream` remote. The repository owner can clone the upstream directly. Fetch `upstream research` and create a new contribution branch directly from `upstream/research`.
3. Run `om init my-result YOUR_PUBLIC_WALLET formal`, or use `research-note` for a written argument. Complete the generated record and its matching artifact. Give sources and state what is original. Replace all template text. For a proof, use the pinned [Lean and Mathlib format](https://github.com/MuncleUscles/open-mathematics/blob/e72ff4a2b51e8cfa809865555116dfc3855e1e2e/docs/FULL-LEAN.md). Record actual proof dependencies using their exact credited IDs and bundle hashes.
4. Run `om format` on each JSON file, then `om check research/submissions/my-result.json`. The default check validates format. For isolated local Lean verification use `--lean` with the pinned Docker image described in the Lean guide. The trusted worker independently verifies the signed PR.
5. Commit exactly the two new files in one commit. Push the branch and open a PR targeting **MuncleUscles/yang-mills:research**. Sign the exact PR as shown below, substituting the PR number. Post the unedited envelope as the PR author within nine minutes.

```sh
om sign PR_NUMBER research/submissions/my-result.json > /tmp/yang-mills-public-claim.txt
CLAIM_URL=$(gh pr comment PR_NUMBER --repo MuncleUscles/yang-mills --body-file /tmp/yang-mills-public-claim.txt)
COMMENT_ID=${CLAIM_URL##*#issuecomment-}
om-wallet submit "$COMMENT_ID"                 # preview the track, sender and call
om-wallet submit "$COMMENT_ID" --send          # send and wait for Studio finality
om status PR_NUMBER
```

GenLayer judges relevance, novelty and usefulness against this problem’s objective. The worker merges an approved head after the five-minute challenge window. The contract credits the signing wallet after the exact merge is confirmed. A formal result pays 80% of its fixed budget up front and reserves 20% for verified upstream proof reuse. Notes can earn up to 300 points. Points are nontransferable. Each GitHub account must be at least 30 days old and can have one active initial claim. Use `om help` for challenges, status and subsequent contribution discovery.

## Sending your own Studio transactions

Post the signed claim once as the PR author, then submit it from the same wallet on stable Studio (chain 61999). Fund the wallet with Studio GEN for its transaction fee. The CLI uses the local `CONTRIBUTOR_KEY_FILE` and prints the transaction hash at broadcast. You can also paste the signed comment permalink into the [wallet submission page](https://muncleuscles.github.io/p-vs-np/#/submit), check the sender and destination, then approve in your wallet.

The [track submission contract](https://studio.genlayer.com/contracts?import-contract=0x86349d111DE1A8911B04a499f8512455601341bf) records who sent each request. Its `submit(claim, pr, comment)` takes the signed comment’s 64-character digest, PR number and original comment ID. `request_retry(claim, pr, comment, prior)` also takes the latest finalized undetermined review hash. Both methods derive the sender from the Studio transaction. The separate credit ledger continues to hold the verified contributions, verdicts and points.

Once the wallet request is finalized, the scheduled worker picks it up. To wake it immediately, post `Open-Mathematics-Process: COMMENT_ID` on the original PR. This comment alone cannot start a new submission or retry. If your client disconnects, check the broadcast hash and run the preview again. An already-finalized request is safe to resume. Continue following the PR check for verification, adjudication and settlement.

## Appeal a Studio review or retry an undetermined result

1. Watch the PR’s **open-mathematics/studio-review** check as soon as it appears. Its **Details** link opens the live transaction and quotes the appeal charge. You can also read the full hash from the worker log or from `transactions.adjudicate-rN.hash` in the contribution’s JSON report on the repository’s `evidence` branch. Use the current review round N.
2. Watch immediately. Stable Studio reported a 30-second base window on November 27, 2026. Each decision has its own deadline. For automation, read `gen_getTransactionLifecycle` and, while a decision is active, `gen_estimateLatestAppealCharge` with `params: [{"txId":"TX_HASH"}]`. Match the decision IDs and use the quote’s `appealDeadline` (Unix seconds), `bond`, and `funding`. Anyone with a funded Studio wallet can appeal while the decision is eligible. Use **Appeal with wallet** on the linked page. For an agent using the GenLayer CLI, select stable Studio with `genlayer network set studionet`, read the charge with `genlayer appeal-bond TX_HASH`, and submit `genlayer appeal TX_HASH` with the configured wallet. Check the live status and the quoted bond plus review funding before signing. An accepted decision gets a fresh committee review. An undetermined decision starts a new proposal round.
3. If the latest merit review finalized undetermined and the signed PR is still current, use `om-wallet retry COMMENT_ID TX_HASH` to preview, then add `--send`. Sign from the original claim wallet. COMMENT_ID is the number after `#issuecomment-` in the signed comment’s permalink. TX_HASH is the latest failed adjudication, not the submission transaction. The worker verifies the finalized request and the prior undecided receipt before processing the same claim and round.

4. If the *research verdict* contains a factual error, prepare 20–4,000 characters of evidence and references in `evidence.txt`. During the contract’s separate five-minute provisional window, preview `om challenge CONTRIBUTION_ID evidence.txt`, then add `--send` to submit. Up to two evidence challenges are available. Run `om status PR_NUMBER` to follow the outcome.

[Open the Studio appeal page](https://muncleuscles.github.io/p-vs-np/#/appeals) · [GenLayer appeal rules](https://docs.genlayer.com/understand-genlayer-protocol/core-concepts/optimistic-democracy/appeal-process)
