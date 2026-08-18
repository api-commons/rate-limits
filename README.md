# Rate Limits

A machine-readable schema for the rate limits an API enforces — what is being counted,
how much of it is allowed, over what window, and against whom.

Rate limits are one of the most consequential things an API publishes and one of the
least machine-readable. They live in prose on a documentation page, in a table that
varies by plan, and in a footnote about which endpoints are counted separately. This
repo is the schema that turns that prose into something tooling and agents can consume,
behind the [RateLimits property](https://apicommons.org/common/rate-limits/) in
[API Commons](https://apicommons.org).

## Artifacts

- **[rate-limits-json-schema.yml](rate-limits-json-schema.yml)** — the JSON Schema
  (2020-12) for a rate limits document.
- **[rate-limits-example-1.yml](rate-limits-example-1.yml)** — a standalone document on a
  made-up `example.com` API, covering a flat platform limit, a per-application limit that
  scales with users, tiered limits, a per-endpoint limit, and a concurrency ceiling.
- **[rate-limits-example-2.yml](rate-limits-example-2.yml)** — the same limits wrapped in
  the `RateLimits` property envelope, ready to drop into an `apis.yml` index, plus a
  second property showing per-model input and output token limits.
- **[validate.py](validate.py)** — validates any document against the schema.
- **[drafts/](drafts/)** — unverified working data. Not an API Commons artifact; see the
  banner in the file.

## Using it

A document takes one of two shapes. Either a bare list of rate limit entries:

```yaml
- name: Search requests
  type: Endpoint
  limit: 30
  metric: request
  timeframe: minute
  description: Search carries its own limit, counted independently of the platform limit.
  domains:
    - api.example.com
```

…or those same entries wrapped in the `RateLimits` property envelope, for an `apis.yml`
index:

```yaml
- name: Rate Limits
  type: RateLimits
  description: The published rate limits for the Example API.
  url: https://developers.example.com/rate-limits
  source_date: '2026-08-17'
  data:
    - name: Search requests
      type: Endpoint
      limit: 30
      metric: request
      timeframe: minute
      description: Search carries its own limit.
```

Each entry requires `name`, `type`, `limit`, `metric`, `timeframe`, and `description`.
`tier`, `domains`, `userMultiplied`, `url`, and `source_date` are optional.

Three rules are worth stating outright, because they are what documents get wrong:

1. **`limit` is a number.** `250000`, never `"250,000"`. A comma-formatted limit is a
   string and will not validate.
2. **`metric` is singular and specific.** Use `input-token` and `output-token` when a
   provider quotes them separately; `token` alone loses the distinction that matters
   most for cost.
3. **A limit describing a real provider should carry `url` and `source_date`.** Rate
   limits change without notice. An entry with no date is an unverified claim, not a
   record.

## Validating

```
pip install jsonschema pyyaml
python3 validate.py rate-limits-example-1.yml
```

## Support

Questions, corrections, and requests go in
[the issues](https://github.com/api-commons/rate-limits/issues).

## License

Two licenses, by kind of thing:

- **Artifacts** — the schemas, rulesets, fixtures, examples and API descriptions — are
  **[CC BY-NC-SA 4.0](LICENSE)** (Attribution–NonCommercial–ShareAlike).
- **Code** — the validator, test harness and packaging — is **[Apache-2.0](LICENSE-CODE)**.

API Commons licenses **artifacts** under CC BY-NC-SA 4.0 and **code** under Apache-2.0.

## Part of API Commons

A machine-readable building block from **[API Commons](https://apicommons.org)** — open specifications and schemas for the APIs you produce and consume. See all building blocks at **[apicommons.org](https://apicommons.org)** and the tools at **[apicommons.org/tools](https://apicommons.org/tools/)**.

**Related building blocks**
- [plans](https://github.com/api-commons/plans) — access plans, tiers, and pricing
- [rate-limits](https://github.com/api-commons/rate-limits) — the quotas an API enforces
- [starters](https://github.com/api-commons/starters) — the smallest correct version of each artifact
