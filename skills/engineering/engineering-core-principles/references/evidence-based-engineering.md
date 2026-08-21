# Evidence-Based Engineering

All engineering work must be grounded in evidence, experimentation, and verifiable claims. This applies to architecture decisions, implementation choices, performance assertions, and documentation.

- **No Unqualified Assumptions**
  Never make assertions about performance, behavior, scalability, or capabilities without:
  - Measured data from experiments or prototypes
  - Citations to authoritative sources (documentation, research papers, benchmarks)
  - Explicit labeling as targets, estimates, or hypotheses to be validated
- **Distinguish Facts from Targets**
  Clearly differentiate between:
  - **Verified facts**: Measured results from implementation or cited from authoritative sources
  - **Targets**: Performance goals or requirements to be validated through implementation
  - **Hypotheses**: Educated assumptions that require experimental validation before being treated as fact
  - **Constraints**: Known limitations from platform documentation or requirements
- **Experiment Before Committing**
  For critical architectural decisions or performance-sensitive implementations:
  - Build prototypes or spikes to validate assumptions
  - Measure actual performance on target hardware
  - Document experimental results that informed decisions
  - Use profiling tools and benchmarks rather than intuition
- **Cite Sources**
  When referencing framework capabilities, algorithms, standards, or best practices, include links to:
  - Official documentation
  - Research papers or technical articles
  - Benchmark results or case studies
  - Community consensus (with appropriate caveats)
- **Avoid Precision Without Proof**
  Do not use specific numbers (for example, "95% accuracy", "<5 seconds", "~50 MB", "10x faster") unless they are:
  - Measured from actual implementation or prototype
  - Cited from authoritative sources with context
  - Explicitly labeled as targets or estimates to be validated
- **Qualify Performance Claims**
  When discussing performance:
  - Specify test conditions (hardware, data size, environmental factors)
  - Use qualitative language ("responsive", "efficient", "scalable") when specific metrics are unavailable
  - Frame unvalidated claims as targets: "target 60 FPS" not "achieves 60 FPS"
  - Document performance degradation conditions
- **Challenge Assumptions**
  Regularly question and validate assumptions through:
  - Code reviews that ask "how do we know this?"
  - Performance testing on minimum supported hardware
  - User testing to validate usability assumptions
  - Load testing to validate scalability claims
