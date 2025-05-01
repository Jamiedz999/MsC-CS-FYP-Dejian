import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [article, setArticle] = useState('');
  const [searchTerm, setSearchTerm] = useState('');
  const [highlightedText, setHighlightedText] = useState('');
  const [selectedFile, setSelectedFile] = useState(null);

  // useEffect(() => {
  //   模拟获取文章的 API 调用
  //   fetch('/api/article')
  //     .then(response => response.text())
  //     .then(data => setArticle(data))
  //     .catch(error => console.error("Error fetching article: ", error));
  // }, []);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleFileUpload = () => {
    if (selectedFile) {
      const reader = new FileReader();
      reader.onload = (event) => {
        setArticle(event.target.result);
        setHighlightedText(''); // 清空高亮
      };
      reader.onerror = (error) => {
        console.error("Error reading file:", error);
        alert("读取文件时发生错误。");
      };
      reader.readAsText(selectedFile);
    } else {
      alert("请先选择一个 .txt 文件。");
    }
  };

  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleSearchClick = () => {
    if (searchTerm && article) {
      fetch('/api/search', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ searchText: searchTerm, article: article }),
      })
        .then(response => {
          if (!response.ok) {
            return response.json().then(errorData => {
              throw new Error(errorData.error || '搜索失败');
            });
          }
          return response.json();
        })
        .then(data => {
          console.log('后端返回的数据:', data);
          console.log('高亮文本:', data.highlightedText);
          setHighlightedText(data.highlightedText);
        })
        .catch(error => {
          console.error("Search error:", error);
          alert(error.message);
        });
    } else {
      alert("请输入搜索关键词并确保文章已加载。");
    }
  };

  const renderArticleWithHighlight = () => {
    if (highlightedText && article.includes(highlightedText)) {
      const parts = article.split(highlightedText);
      return (
        <>
          {parts.map((part, index) => (
            <React.Fragment key={index}>
              {part}
              {index < parts.length - 1 && <span className="highlighted">{highlightedText}</span>}
            </React.Fragment>
          ))}
        </>
      );
    }
    return article;
  };

  return (
    <div className="App">
      <header className="App-header">
        <div className="upload-container">
          <h4>Upload article</h4>
          <input type="file" accept=".txt" onChange={handleFileChange} />
          <button onClick={handleFileUpload} disabled={!selectedFile}>
            Display article
          </button>
        </div>
        <div className="article-container">
          <h4>Current article</h4>
          <div
            className="article-text"
            style={{whiteSpace: 'pre-wrap', border: '1px solid #ccc', minHeight: '200px', padding: '8px'}}
          >
            {renderArticleWithHighlight()}
          </div>
        </div>
        <div className="search-container">
          <h4>Search text</h4>
          <input
            type="text"
            className="search-input"
            placeholder="Input a sentence"
            value={searchTerm}
            onChange={handleSearchChange}
          />
          <button className="search-button" onClick={handleSearchClick}>
            Search
          </button>
          {/* 可以选择性地显示后端返回的原始高亮文本 */}
          {/* {highlightedText && <p>高亮结果: <span className="highlighted">{highlightedText}</span></p>} */}
        </div>
      </header>
    </div>
  );
}

export default App;