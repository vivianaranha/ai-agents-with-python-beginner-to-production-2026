# MCP 2026 Notes

The July 28, 2026 MCP specification moved the protocol core to stateless request/response semantics. The old initialize/initialized handshake and `Mcp-Session-Id` protocol session were removed. Current architecture also emphasizes explicit routing metadata, authorization hardening, cacheable lists and an extensions model.

For this course, students focus on the architectural consequences: explicit tool contracts, stateless transport, identity/authorization boundaries, auditable calls and scalable server design.
