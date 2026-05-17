# 🚀 Deploy to Vercel in 3 Steps

## Quick Start

### 1. Click Deploy Button

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/YOUR_USERNAME/CodeReuse&env=HUGGINGFACE_API_TOKEN&envDescription=Hugging%20Face%20API%20token%20for%20IBM%20Granite&envLink=https://huggingface.co/settings/tokens)

### 2. Add Environment Variable

When prompted, add your Hugging Face API token:
- Get token from: https://huggingface.co/settings/tokens
- Paste in `HUGGINGFACE_API_TOKEN` field

### 3. Deploy!

Click "Deploy" and wait 2-3 minutes. Your app will be live!

---

## What Gets Deployed

- ✅ **Frontend**: Beautiful UI at `https://your-app.vercel.app`
- ✅ **API**: Serverless functions at `https://your-app.vercel.app/api/*`
- ✅ **Auto-scaling**: Handles traffic spikes automatically
- ✅ **Global CDN**: Fast loading worldwide

---

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variable
export HUGGINGFACE_API_TOKEN="your_token"

# Run backend
python -m uvicorn src.api.main:app --reload --port 8000

# Open frontend
cd frontend && open index.html
```

---

## Full Documentation

See [VERCEL_DEPLOYMENT.md](./VERCEL_DEPLOYMENT.md) for:
- Detailed deployment guide
- Troubleshooting
- Custom domains
- Monitoring & logs
- Production checklist

---

## Architecture

```
User Request
    ↓
Vercel Edge Network (CDN)
    ↓
┌─────────────┬──────────────────┐
│  Frontend   │   API Functions  │
│  (Static)   │   (Serverless)   │
└─────────────┴──────────────────┘
    ↓                ↓
Browser         IBM Granite
                (via HuggingFace)
```

---

## Features

- 🧠 **AI-Powered**: Uses IBM Granite for code generation
- 🔍 **AST Analysis**: Deep code understanding
- 📊 **Dependency Graphs**: Visual code relationships
- ✅ **Code Reuse Enforcement**: 40% minimum reuse threshold
- 🚫 **Plagiarism Detection**: Structural similarity checking
- ⚡ **Real-time Metrics**: Live quality scores

---

## Support

- 📖 [Full Documentation](./VERCEL_DEPLOYMENT.md)
- 🐛 [Report Issues](https://github.com/YOUR_USERNAME/CodeReuse/issues)
- 💬 [Discussions](https://github.com/YOUR_USERNAME/CodeReuse/discussions)

---

*Made with IBM Bob - Deployed on Vercel* 🚀