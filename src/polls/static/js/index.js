import { html, Component, render } from '../vendor/preact.min.js';

function Poll(props) {
  return html`
    <li><a href="/poll/${props.poll.id}">${props.poll.title}</a></li>
  `;
}

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
            <${Poll} poll=${poll} />
          `)}
        </ul>
      </div>
    `;
  }
}

render(html`<${App} />`, document.getElementById('app'));
