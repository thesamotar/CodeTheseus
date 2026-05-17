# Vercel Deployment Guide

## 🚀 Quick Deploy to Vercel

This guide will help you deploy the Context-Aware Code Generation Agent to Vercel.

---

## Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **GitHub Repository**: Push this code to GitHub
3. **Hugging Face API Token**: Get from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

---

## Deployment Steps

### Option 1: Deploy via Vercel Dashboard (Recommended)

1. **Import Project**
   - Go to [vercel.com/new](https://vercel.com/new)
   - Click "Import Git Repository"
   - Select your GitHub repository

2. **Configure Project**
   - **Framework Preset**: Other
   - **Root Directory**: `./` (leave as default)
   - **Build Command**: Leave empty (static files + serverless)
   - **Output Directory**: Leave empty

3. **Add Environment Variables**
   - Click "Environment Variables"
   - Add: `HUGGINGFACE_API_TOKEN` = `your_token_here`
   - Click "Add"

4. **Deploy**
   - Click "Deploy"
   - Wait 2-3 minutes for deployment
   - Your app will be live at `https://your-project.vercel.app`

### Option 2: Deploy via Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy
cd CodeReuse
vercel

# Follow prompts:
# - Set up and deploy? Yes
# - Which scope? Your account
# - Link to existing project? No
# - Project name? codereuse-ai
# - Directory? ./
# - Override settings? No

# Add environment variable
vercel env add HUGGINGFACE_API_TOKEN

# Deploy to production
vercel --prod
```

---

## Configuration Files

### `vercel.json`
Main configuration file that defines:
- **Builds**: Python serverless function + static frontend
- **Routes**: API routes to `/api/*`, frontend to `/*`
- **Functions**: Memory (3GB) and timeout (5 min) settings

### `api/index.py`
Serverless function entry point that wraps the FastAPI app

### `api/requirements.txt`
Lightweight dependencies optimized for serverless deployment

---

## Architecture on Vercel

```
┌─────────────────────────────────────────┐
│         Vercel Edge Network             │
│  (Global CDN for static files)          │
└─────────────────────────────────────────┘
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
┌──────────────┐    ┌──────────────────┐
│   Frontend   │    │  API Functions   │
│   (Static)   │    │  (Serverless)    │
│              │    │                  │
│ - index.html │    │ - FastAPI app    │
│ - app.js     │    │ - Python runtime │
│ - styles.css │    │ - 3GB memory     │
└──────────────┘    │ - 5min timeout   │
                    └──────────────────┘
```

---

## Environment Variables

Set these in Vercel Dashboard → Settings → Environment Variables:

| Variable | Required | Description |
|----------|----------|-------------|
| `HUGGINGFACE_API_TOKEN` | ✅ Yes | Your Hugging Face API token for IBM Granite |

---

## Limitations & Considerations

### Serverless Constraints

1. **Cold Starts**: First request may take 5-10 seconds
2. **Execution Time**: Max 5 minutes per request (configurable up to 15 min on Pro)
3. **Memory**: 3GB allocated (sufficient for embeddings)
4. **Storage**: Ephemeral - ChromaDB resets between invocations

### Recommended Optimizations

1. **Use External Vector DB**
   - Consider Pinecone, Weaviate, or Qdrant for persistent storage
   - Update `src/indexing/vector_db.py` to use cloud provider

2. **Cache Embeddings**
   - Store embeddings in external storage (S3, Vercel Blob)
   - Load on cold start instead of regenerating

3. **Optimize Dependencies**
   - `api/requirements.txt` already optimized
   - Removed heavy dependencies (torch, transformers for local inference)

4. **Use Edge Functions** (Future)
   - Move lightweight operations to Edge Runtime
   - Keep heavy ML operations in serverless functions

---

## Testing Deployment

### 1. Test Frontend
```bash
# Visit your Vercel URL
https://your-project.vercel.app

# Should see landing page with "Backend online" status
```

### 2. Test API Health
```bash
curl https://your-project.vercel.app/api/health
# Expected: {"status": "healthy"}
```

### 3. Test Repository Indexing
```bash
curl -X POST https://your-project.vercel.app/api/index/repository \
  -H "Content-Type: application/json" \
  -d '{"repository_path": "./sample_repo"}'
```

### 4. Test Code Generation
```bash
curl -X POST https://your-project.vercel.app/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "user_request": "Add email validation",
    "target_file": "user_service.py",
    "mode": "legacy"
  }'
```

---

## Troubleshooting

### Issue: "Function execution timed out"
**Solution**: 
- Reduce repository size
- Use external vector DB
- Increase timeout in `vercel.json` (Pro plan)

### Issue: "Module not found"
**Solution**:
- Check `api/requirements.txt` includes all dependencies
- Verify `api/index.py` path imports are correct
- Redeploy: `vercel --prod --force`

### Issue: "Out of memory"
**Solution**:
- Increase memory in `vercel.json` (currently 3GB)
- Optimize embedding batch size
- Use smaller embedding model

### Issue: "CORS errors"
**Solution**:
- Already configured in `src/api/main.py` with `allow_origins=["*"]`
- If issues persist, check Vercel logs: `vercel logs`

### Issue: "WebSocket connection failed"
**Solution**:
- WebSockets not supported in Vercel serverless functions
- Use polling or Server-Sent Events (SSE) instead
- Or deploy WebSocket server separately (Railway, Render)

---

## Monitoring & Logs

### View Logs
```bash
# Real-time logs
vercel logs --follow

# Recent logs
vercel logs

# Specific deployment
vercel logs [deployment-url]
```

### Vercel Dashboard
- Go to your project → Deployments
- Click on a deployment → View Function Logs
- Monitor: Invocations, Duration, Memory usage

---

## Custom Domain

### Add Custom Domain

1. Go to Project Settings → Domains
2. Add your domain: `codereuse.yourdomain.com`
3. Configure DNS:
   ```
   Type: CNAME
   Name: codereuse
   Value: cname.vercel-dns.com
   ```
4. Wait for DNS propagation (5-30 minutes)

---

## Scaling & Performance

### Free Tier Limits
- 100GB bandwidth/month
- 100 hours serverless execution/month
- 6,000 minutes build time/month

### Pro Tier Benefits ($20/month)
- Unlimited bandwidth
- Unlimited serverless execution
- 400 hours build time/month
- 15-minute function timeout
- Advanced analytics

---

## Alternative Deployment Options

If Vercel doesn't meet your needs:

### 1. **Railway** (Recommended for WebSockets)
- Full Docker support
- Persistent storage
- WebSocket support
- $5/month starter

### 2. **Render**
- Free tier available
- Persistent disks
- Background workers
- Good for long-running tasks

### 3. **Fly.io**
- Edge deployment
- Persistent volumes
- Global distribution
- Free tier available

### 4. **AWS Lambda + S3**
- Maximum control
- Persistent storage (S3)
- Pay per use
- More complex setup

---

## Production Checklist

- [ ] Environment variables set in Vercel
- [ ] Custom domain configured (optional)
- [ ] API health check passes
- [ ] Frontend loads correctly
- [ ] Repository indexing works
- [ ] Code generation works
- [ ] Metrics display correctly
- [ ] Error handling tested
- [ ] Monitoring/logging configured
- [ ] Performance optimized

---

## Support & Resources

- **Vercel Docs**: [vercel.com/docs](https://vercel.com/docs)
- **FastAPI on Vercel**: [vercel.com/guides/python](https://vercel.com/guides/python)
- **Project Issues**: [GitHub Issues](https://github.com/your-repo/issues)

---

## Next Steps

1. ✅ Deploy to Vercel
2. 🔧 Test all features
3. 📊 Monitor performance
4. 🚀 Share with users
5. 🎯 Iterate based on feedback

**Your Context-Aware Code Generation Agent is now live! 🎉**

---

*Made with IBM Bob - Deployed on Vercel*