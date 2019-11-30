import { html, Component, render } from '../vendor/preact.min.js';

class App extends Component {
  addTodo() {
    const { todos = [] } = this.state;
    this.setState({ todos: todos.concat(`Item ${todos.length}`) });
  }

  render({ todos = [] }) {
    return html`
      <div class="app">
        <ul>
          ${todos.map((todo) => html`
            <li>${todo}</li>
          `)}
        </ul>
        <button onClick=${() => this.addTodo()}>Add Todo</button>
      </div>
    `;
  }
}

render(html`<${App} />`, document.getElementById('app'));
