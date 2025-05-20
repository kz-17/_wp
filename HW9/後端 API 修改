// routes/posts.js
const express = require('express');
const router = express.Router();
const Post = require('../models/Post');
const authenticate = require('../middleware/authenticate'); // 驗證 JWT 的 middleware

// 刪除貼文
router.delete('/:postId', authenticate, async (req, res) => {
  const postId = req.params.postId;
  const userId = req.user.id; // 來自 JWT middleware

  try {
    const post = await Post.findById(postId);

    if (!post) {
      return res.status(404).json({ message: '找不到貼文' });
    }

    if (post.authorId.toString() !== userId) {
      return res.status(403).json({ message: '你只能刪除自己的貼文' });
    }

    await Post.findByIdAndDelete(postId);
    res.status(200).json({ message: '貼文已刪除' });
  } catch (err) {
    res.status(500).json({ message: '伺服器錯誤', error: err.message });
  }
});

module.exports = router;
