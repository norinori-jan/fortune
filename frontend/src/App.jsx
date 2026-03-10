import { useState } from 'react';
import DivinationResult from './components/DivinationResult';
import './App.css';

function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [rolling, setRolling] = useState(false);

  const handleDivine = async () => {
    setRolling(true);
    setError(null);

    // サイコロを振るアニメーション（500ms）
    await new Promise((res) => setTimeout(res, 500));
    setRolling(false);
    setLoading(true);

    try {
      const response = await fetch('/api/divine', { method: 'POST' });
      if (!response.ok) {
        throw new Error(`サーバーエラー: ${response.status}`);
      }
      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message || '占いに失敗しました。バックエンドが起動しているか確認してください。');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1 className="app-title">☯ 易占い（周易）</h1>
        <p className="app-subtitle">六十四卦で運命を読む</p>
      </header>

      <main className="app-main">
        <div className="divine-section">
          <button
            className={`divine-button ${rolling ? 'rolling' : ''}`}
            onClick={handleDivine}
            disabled={loading || rolling}
          >
            {rolling ? '🎲 🎲 🎲' : loading ? '占い中...' : '🎲 占う'}
          </button>
          <p className="divine-hint">ボタンを押してサイコロを振り、卦を立ててください</p>
        </div>

        {error && (
          <div className="error-banner">
            <strong>エラー:</strong> {error}
          </div>
        )}

        {result && !loading && <DivinationResult result={result} />}
      </main>

      <footer className="app-footer">
        <p>易（周易）— 変化の書 | 八卦×八卦 = 六十四卦</p>
      </footer>
    </div>
  );
}

export default App;
