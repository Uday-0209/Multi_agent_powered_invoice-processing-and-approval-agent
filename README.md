<h1 align="center">Multi-Agent Invoice Processing & Approval System</h1>

<p align="center">
AI-powered document automation pipeline built with <b>LangGraph</b>, <b>DSPy</b>, and <b>FastAPI</b>.
</p>

<hr>

<h2>Overview</h2>

<p>
This project implements a <b>multi-agent architecture</b> for processing financial documents such as:
</p>

<ul>
<li>Purchase Orders</li>
<li>Invoices</li>
<li>Receipts</li>
</ul>

<p>
Each document passes through an intelligent workflow where specialized agents perform tasks such as
OCR, data extraction, validation, fraud detection, policy evaluation, and final approval decisions.
</p>

<hr>

<h2>System Architecture</h2>

<pre>
DOCUMENT UPLOAD
      │
      ▼
Document Intake Agent
      │
      ▼
OCR Agent
      │
      ▼
Extraction Agent
      │
      ▼
Classification Agent
      │
      ▼
Document Router
      │
      ├──────────── PURCHASE ORDER FLOW ─────────────┐
      │ Vendor Verification → Company Verification
      │ → Fraud Detection → Validation
      │ → Policy Check → Save → Decision → Notify
      │
      ├──────────── INVOICE FLOW ────────────────────┤
      │ Vendor Verification → Company Verification
      │ → Validation → Policy Check
      │ → Save → Decision → Notify
      │
      └──────────── RECEIPT FLOW ────────────────────┘
        Vendor Verification → Company Verification
        → Validation → Policy Check
        → Payment Verification → Save → Decision → Notify
</pre>

<hr>

<h2>Agents in the System</h2>

<table>
<tr>
<th>Agent</th>
<th>Responsibility</th>
</tr>

<tr>
<td>Document Intake Agent</td>
<td>Initializes workflow and prepares document metadata.</td>
</tr>

<tr>
<td>OCR Agent</td>
<td>Extracts text from uploaded PDF documents.</td>
</tr>

<tr>
<td>Extraction Agent</td>
<td>Identifies structured fields like vendor, invoice number, and totals.</td>
</tr>

<tr>
<td>Classification Agent</td>
<td>Determines whether the document is a PO, Invoice, or Receipt.</td>
</tr>

<tr>
<td>Vendor Verification Agent</td>
<td>Checks if the vendor exists in the internal database.</td>
</tr>

<tr>
<td>Company Verification Agent</td>
<td>Validates the company referenced in the document.</td>
</tr>

<tr>
<td>Validation Agent</td>
<td>Ensures document information matches stored records.</td>
</tr>

<tr>
<td>Fraud Detection Agent</td>
<td>Analyzes potential risk using AI reasoning.</td>
</tr>

<tr>
<td>Policy Agent</td>
<td>Applies business rules such as approval thresholds.</td>
</tr>

<tr>
<td>Payment Verification Agent</td>
<td>Verifies receipt payments against invoice records.</td>
</tr>

<tr>
<td>Decision Agent</td>
<td>Determines final outcome (Approved / Rejected / Manual Review).</td>
</tr>

<tr>
<td>Notification Agent</td>
<td>Sends workflow completion notifications.</td>
</tr>

</table>

<hr>

<h2>Technology Stack</h2>

<ul>

<li><b>LangGraph</b> — Agent workflow orchestration</li>
<li><b>DSPy</b> — Structured LLM reasoning</li>
<li><b>FastAPI</b> — API service</li>
<li><b>Python</b> — Core application language</li>
<li><b>SQLAlchemy</b> — Database ORM</li>
<li><b>PostgreSQL</b> — Persistence layer</li>
<li><b>LangSmith</b> — Observability and tracing</li>
<li><b>Unstructured OCR</b> — Document text extraction</li>

</ul>

<hr>

<h2>Database Persistence</h2>

<p>
The system stores processed documents and validation results in a relational database.
</p>

<ul>

<li>Purchase Orders</li>
<li>Invoices</li>
<li>Receipts</li>
<li>Vendor records</li>
<li>Payment records</li>

</ul>

<p>
Each workflow run stores validation status, fraud score, and decision outcomes.
</p>

<hr>

<h2>Observability</h2>

<p>
The system integrates <b>LangSmith</b> to trace agent execution across the workflow.
</p>

<p>
Each document run records:
</p>

<ul>

<li>Workflow execution path</li>
<li>Agent execution sequence</li>
<li>AI reasoning steps</li>
<li>Execution time and performance metrics</li>

</ul>

<hr>

<h2>Testing the Workflow</h2>

<p>The project contains automated tests that simulate document processing.</p>

<pre>
python -m tests.test_workflow
</pre>

<p>This executes the full workflow pipeline for:</p>

<ul>
<li>Purchase Orders</li>
<li>Invoices</li>
<li>Receipts</li>
</ul>

<hr>

<h2>Key Features</h2>

<ul>

<li>Multi-agent AI architecture</li>
<li>Fraud detection and policy enforcement</li>
<li>Automated approval decisions</li>
<li>Database persistence</li>
<li>LangSmith observability</li>
<li>Extensible agent framework</li>

</ul>

<hr>

<h2>Future Improvements</h2>

<ul>

<li>Human-in-the-loop review dashboard</li>
<li>Advanced fraud detection models</li>
<li>Agent performance analytics</li>
<li>Workflow replay for debugging</li>

</ul>

<hr>

<p align="center">
Built using LangGraph Multi-Agent Architecture
</p>
