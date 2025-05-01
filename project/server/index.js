const express = require('express');
const app = express();
const port = 8080; // 你可以选择其他端口
const dotenv = require("dotenv")

const bodyParser = require('body-parser'); // 需要处理 POST 请求的 body
const { spawn } = require('child_process'); // 用于执行 Python 脚本
const path = require('path');
const cors = require('cors'); // 处理跨域请求 (如果前端和后端不在同一个域)


const pythonExecutable = path.join(__dirname, '..', 'venv', 'bin', 'python');


app.use(cors()); // 允许跨域请求 (开发环境可能需要)
app.use(bodyParser.json()); // 解析 JSON 格式的请求体
app.use(express.json());

app.get('/api', (req, res) => {
  console.log("it's running here")
  res.json({ message: 'Hello from the backend!' });
});


app.post('/api/search', (req, res) => {
  const { article, searchText } = req.body;
  console.log("here")
  if (!searchText || !article) {
    return res.status(400).json({ error: 'searchText 和 article 不能为空' });
  }

  // 调用 Python 脚本

  const pythonProcess = spawn(pythonExecutable, [
    path.join(__dirname, 'service', 'search_algo.py'), 
    searchText,                                     // -> 对应 sys.argv[1]
    article                                         // -> 对应 sys.argv[2]
  ]);
  let scriptOutput = '';
  let scriptError = '';
  pythonProcess.stdout.on('data', (data) => {
    console.log(data.toString())
    scriptOutput += data.toString();
  });

  pythonProcess.stderr.on('data', (data) => {
    scriptError += data.toString();
  });


  pythonProcess.on('close', (code) => {
    if (code === 0) {
      res.json({ highlightedText: scriptOutput });
    } else {
      console.error('Python script execution failed with code:', code);
      console.error('Python script error:', scriptError);
      res.status(500).json({ error: 'Python 脚本执行失败', details: scriptError });
    }
  });
});





app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});