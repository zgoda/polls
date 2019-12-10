import { html, Component, render } from '../vendor/preact.min.js';

function Option(props) {
  return html`
    <div>
      <label>
        <input
          type="radio"
          name="option"
          value="${props.option.id}"
          onInput=${(e) => props.onInput(e)}
        />
        <span class="checkable">${props.option.title}</span>
      </label>
    </div>
  `;
}

class App extends Component {
  state = { voted: false, selected: null, ready: false };

  urls = { get: null, vote: null };

  csrfToken = null;

  poll = null;

  constructor() {
    super();
    const pollId = document.getElementsByName('poll-id')[0].content;
    this.csrfToken = document.getElementsByName('csrf-token')[0].content;
    this.urls = {
      get: `/api/poll/${pollId}`,
      vote: `/api/poll/${pollId}/vote`,
    };
  }

  async componentDidMount() {
    const resp = await fetch(this.urls.get);
    const poll = await resp.json();
    this.poll = poll;
    this.setState({ ready: true });
  }

  async doVote() {
    const resp = await fetch(this.urls.vote, {
      method: 'POST',
      body: JSON.stringify({ selected: this.state.selected }),
      headers: {
        'X-CSRFToken': this.csrfToken,
        'Content-Type': 'application/json',
      },
    });
    if (resp.ok) {
      this.setState({ voted: true });
    }
  }

  onOptionChange = (ev) => {
    this.setState({ selected: ev.target.value });
  }

  render() {
    let ret = html`<div></div>`;
    if (!this.state.ready) {
      return ret;
    }
    if (this.state.voted) {
      ret = html`<p>Thank you for your vote!</p>`;
    } else if (this.poll != null) {
      this.poll.options.sort((a, b) => ((a.title > b.title) ? 1 : -1));
      ret = html`
        <div class="app">
          ${this.poll.options.map((option) => html`
            <${Option} option=${option} onInput=${this.onOptionChange} />
          `)}
          <div>
            <button onClick=${() => this.doVote()}>Cast vote</button>
          </div>
        </div>
      `;
    }
    return ret;
  }
}

render(html`<${App} />`, document.getElementById('app'));
