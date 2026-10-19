import { readFile } from "node:fs/promises";

type Email = { id: string; category: string; subject: string; body: string };
type KBResponse = { answer: string; status: string; sources: {title: string; url: string}[]; needs_human: boolean };

const kbUrl = process.env.KB_API_URL ?? "http://127.0.0.1:8000";

async function main() {
  const path = process.argv[2] ?? "../data/emails.json";
  const index = Number(process.argv[3] ?? "0");
  const emails = JSON.parse(await readFile(path, "utf8")) as Email[];
  const email = emails[index];
  if (!email) throw new Error(`No email at index ${index}. Dataset has ${emails.length} emails.`);

  const response = await fetch(`${kbUrl}/query`, {
    method: "POST",
    headers: {"content-type":"application/json"},
    body: JSON.stringify({question: `${email.subject}\n${email.body}`}),
    signal: AbortSignal.timeout(10000)
  });
  if (!response.ok) throw new Error(`Knowledge Brain returned HTTP ${response.status}`);
  const knowledge = await response.json() as KBResponse;

  const needsHuman = knowledge.needs_human ||
    ["refund", "complaint", "quote", "project request"].includes(email.category.toLowerCase());
  const draft = knowledge.needs_human
    ? `Hello,\n\nThank you for contacting us. I want to make sure we give you an accurate answer. Our support team will review your request and follow up.\n\nBest regards,\nSupport Team`
    : `Hello,\n\nThank you for reaching out about "${email.subject}". ${knowledge.answer}\n\nIf the issue continues, please share the relevant page URL and steps to reproduce it so our team can investigate.\n\nBest regards,\nSupport Team`;

  console.log(JSON.stringify({
    emailId: email.id, category: email.category, subject: email.subject,
    draft, sources: knowledge.sources, needsHumanApproval: needsHuman,
    note: "Starter only: no email is sent automatically."
  }, null, 2));
}
main().catch((err: unknown) => { console.error(err); process.exitCode = 1; });
