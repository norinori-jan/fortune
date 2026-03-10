import PropTypes from 'prop-types';
import Hexagram from './Hexagram';

/**
 * 占い結果を表示するコンポーネント
 * 本卦・変爻・之卦を含む
 */
function DivinationResult({ result }) {
  if (!result) return null;

  const { honke, shike, changing_line, changing_line_name } = result;

  return (
    <div className="result-container">
      {/* 本卦 */}
      <section className="result-section">
        <h2 className="section-title">🔮 本卦（ほんけ）</h2>
        <Hexagram hexagram={honke} changingLine={changing_line} label="本卦" />
        <div className="description-card">
          <p className="description-text">{honke.description}</p>
        </div>
      </section>

      {/* 変爻 */}
      <section className="result-section changing-line-section">
        <h2 className="section-title">🎲 変爻（へんこう）</h2>
        <div className="changing-line-info">
          <div className="die-icon">🎲</div>
          <div>
            <p className="changing-line-text">
              <strong>{changing_line_name}</strong>（第{changing_line}爻）が動く
            </p>
            <p className="changing-line-sub">
              {honke.lines[changing_line - 1] === 1 ? '陽（⚊）→ 陰（⚋）' : '陰（⚋）→ 陽（⚊）'}
            </p>
          </div>
        </div>
      </section>

      {/* 之卦 */}
      <section className="result-section">
        <h2 className="section-title">✨ 之卦（しか）― 変化の先</h2>
        <Hexagram hexagram={shike} label="之卦" />
        <div className="description-card">
          <p className="description-text">{shike.description}</p>
        </div>
      </section>
    </div>
  );
}

DivinationResult.propTypes = {
  result: PropTypes.shape({
    honke: PropTypes.object,
    shike: PropTypes.object,
    changing_line: PropTypes.number,
    changing_line_name: PropTypes.string,
  }),
};

DivinationResult.defaultProps = {
  result: null,
};

export default DivinationResult;
