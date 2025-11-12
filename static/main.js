<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Local Chat - Login</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">
</head>
<body class="bg-light d-flex flex-column align-items-center justify-content-center vh-100">
  <div class="card shadow-lg p-4 text-center" style="width: 350px;">
    <h3 class="mb-3 text-success"><i class="bi bi-chat-fill"></i> Local Chat</h3>
    <p class="text-muted">Join the chat by entering your name</p>
    <input id="username" class="form-control mb-3" placeholder="Enter your name">
    <button class="btn btn-success w-100" onclick="addUser()">Join</button>
  </div>

  <script>
    function addUser() {
      const username = document.getElementById('username').value.trim();
      if (!username) return alert("Enter a valid name!");
      fetch('/add_user', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username })
      })
      .then(() => window.location.href = `/chat/${username}`);
    }
  </script>
</body>
</html>
