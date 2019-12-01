import { html, Component, render } from '../vendor/preact.min.js';

class App extends Component {
  state = { poll: null, voted: false, selected: null };

  async componentDidMount() {
    const pollId = document.getElementsByName('poll-id')[0].content;
    const csrfToken = document.getElementsByName('csrf-token')[0].content;
    const url = `/api/poll/${pollId}`;
    const resp = await fetch(url);
    const poll = await resp.json();
    this.setState({ poll, pollId, csrfToken });
  }

  async doVote() {
    const resp = await fetch(`/api/poll/${this.state.pollId}/vote`, {
      method: 'POST',
      body: JSON.stringify({ selected: this.state.selected }),
      headers: {
        'X-CSRFToken': this.state.csrfToken,
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
    let ret = 'empty';
    if (this.state.voted) {
      ret = html`<p>Thank you for your vote!</p>`;
    } else if (this.state.poll != null) {
      this.state.poll.options.sort((a, b) => ((a.title > b.title) ? 1 : -1));
      ret = html`
        <div class="app">
          ${this.state.poll.options.map((option) => html`
          <div>
            <label>
              <input
                type="radio"
                name="option"
                value="${option.value}"
                onInput=${(e) => this.onOptionChange(e)}
              />
              ${option.title}
            </label>
          </div>
          `)}
          <div>
            <button class="button is-primary" onClick=${() => this.doVote()}>Cast vote</button>
          </div>
        </div>
      `;
    }
    return ret;
  }
}

render(html`<${App} />`, document.getElementById('app'));
