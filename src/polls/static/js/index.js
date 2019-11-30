import { html, Component, render } from '../vendor/preact.min.js';

class App extends Component {
  state = { polls: [] };

  async componentDidMount() {
    const resp = await fetch('/api/polls');
    const polls = await resp.json();
    this.setState({ polls });
  }

  render() {
    return html`
      <div class="app">
        <ul>
          ${this.state.polls.map((poll) => html`
          <li><a href="/poll/${poll.id}">${poll.title}</a></li>
          `)}
        </ul>
      </div>
    `;
  }
}

render(html`<${App} />`, document.getElementById('app'));
