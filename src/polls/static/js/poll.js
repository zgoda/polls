import { html, Component, render } from '../vendor/preact.min.js';

class App extends Component {
  state = { poll: null, voted: false, selected: null };

  async componentDidMount() {
    const pollId = document.getElementsByName('poll-id')[0].content;
    const url = `/api/poll/${pollId}`;
    const resp = await fetch(url);
    const poll = await resp.json();
    this.setState({ poll });
  }

  async doVote() {
    const resp = await fetch(`/api/poll/${this.state.poll.id}/vote`, {
      method: 'POST',
      body: JSON.stringify({ option: this.state.selected }),
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
      ret = html`<p>Oh noes, you already voted!</p>`;
    } else if (this.state.poll != null) {
      ret = html`
        <div class="app">
          ${this.state.poll.options.map((option) => html`
            <label>
              <input
                type="radio"
                name="option"
                value="${option.value}"
                onChange=${(e) => this.onOptionChange(e)}
              />
              ${option.title}
            </label>
          `)}
          <button onClick=${() => this.doVote()}>Cast vote</button>
        </div>
      `;
    }
    return ret;
  }
}

render(html`<${App} />`, document.getElementById('app'));
