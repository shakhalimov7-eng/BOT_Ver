import fetch from "node-fetch";

const TELEGRAM_BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN;

export default async function handler(req, res) {
  if (req.method === "POST") {
    const body = req.body;

    if (body.message && body.message.text) {
      const chatId = body.message.chat.id;
      const text = body.message.text;

      // Oddiy javob: qabul qilingan matnni qaytaradi
      const replyText = `Siz yozdingiz: ${text}`;

      await fetch(`https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          chat_id: chatId,
          text: replyText
        })
      });
    }

    return res.status(200).send("ok");
  }

  res.status(405).send("Method Not Allowed");
}
