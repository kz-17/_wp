async function handleDelete(postId) {
  const res = await fetch(`/api/posts/${postId}`, {
    method: 'DELETE',
    headers: {
      Authorization: `Bearer ${userToken}`,
    },
  });

  const result = await res.json();
  if (res.ok) {
    alert('刪除成功');
    // 更新畫面，例如重新拉貼文列表
  } else {
    alert(`刪除失敗：${result.message}`);
  }
}



{post.authorId === currentUser.id && (
  <button onClick={() => handleDelete(post._id)}>刪除</button>
)}
