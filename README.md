# API Rate Limits

An API Rate Limit is a machine-readable description of the limits an API places on consumption—how many requests, tokens, or other units a consumer may use, over what timeframe, and against which domains. Rate limits are one of the most important operational details of an API, shaping how consumers design their applications and integrations, yet they are usually buried in prose across documentation. This building block turns them into structured, interoperable data so producers can publish them consistently and consumers (and tooling) can read and plan against them reliably.

## API Commons

API Rate Limits are an [API Commons](https://apicommons.org) building block—an open, machine-readable schema for describing the consumption limits an API enforces, made interoperable as part of the API contract so it can be discovered, referenced, and reused across the APIs.json ecosystem and surfaced through [apis.io](https://apis.io). This schema is just getting started and will mature as it is applied to profiling existing APIs and describing new ones.

## What's in this repo

- [rate-limits-json-schema.yml](rate-limits-json-schema.yml) — The JSON Schema that defines a single rate limit.
- [rate-limits-example-1.yml](rate-limits-example-1.yml) — A worked example capturing per-model rate limits for the Claude API.
- [claude-openai-gemini-rate-limits.yaml](claude-openai-gemini-rate-limits.yaml) — A real-world example capturing rate limits across the Claude, OpenAI, and Gemini APIs.

## The Schema

The [rate-limits-json-schema.yml](rate-limits-json-schema.yml) defines each rate limit as an object with the following properties:

- **name** — The name of the rate limit.
- **type** — The type of the rate limit (for example, `Model`).
- **limit** — The numeric value of the limit.
- **metric** — The unit the limit is measured in (for example, `token` or `request`).
- **domains** — An array of the API domains the limit applies to.
- **timeframe** — The window the limit is measured over (for example, `minute`).
- **description** — A description of the rate limit.
- **userMultiplied** — Whether the limit is multiplied per user (boolean).

## Example

The [rate-limits-example-1.yml](rate-limits-example-1.yml) file describes a set of per-model rate limits:

```yaml
- name: Claude Opus 4 Input Tokens
  type: Model
  limit: 30000
  metric: token
  domains:
    - api.anthropic.com
  timeframe: minute
  description: The input token limits for the Claude Opus 4 model.
  userMultiplied: false
```

## How It Fits

Rate limits are one of a growing set of API Commons building blocks that describe the business and technical realities of API operations in a machine-readable way. They sit alongside [plans](https://github.com/api-commons/plans)—which describe access, packaging, and pricing—and [tiers](https://github.com/api-commons/tiers)—which describe the service level applied to requests—together giving a complete picture of how an API is consumed. Each is a small, reusable schema that can stand alone or be composed together within an APIs.json index.

## Support

This schema is managed using the issues on this GitHub repository. If there is a feature you'd like to see, or you have questions, please submit an issue or email kin@apievangelist.com.

## Part of API Commons

A machine-readable building block from **[API Commons](https://apicommons.org)** — open specifications and schemas for the APIs you produce and consume. See all building blocks and tools at **[apicommons.org](https://apicommons.org)** and the tools at **[apicommons.org/tools](https://apicommons.org/tools/)**.

**Related building blocks**
- [plans](https://github.com/api-commons/plans) — machine-readable access plans, tiers, and pricing
- [tiers](https://github.com/api-commons/tiers) — the access/service tiers available for an API
- [use-cases](https://github.com/api-commons/use-cases) — how an API is actually put to work, tied to its operations
- [policies](https://github.com/api-commons/policies) — the business rules behind API governance
