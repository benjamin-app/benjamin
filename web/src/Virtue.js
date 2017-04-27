import React, { Component } from 'react';
import { observer } from 'mobx-react';

import { _fetch } from './utils';

@observer
export default class Virtue extends Component {

  handleSuccess() {
    // TODO: pass the value in the click handler
    this.handleClick(1)
  }

  handleFail() {
    this.handleClick(0)
  }

  handleClick(value) {
    const date = this.props.appStore.selectedDay.unix();
    const virtue_id = this.props.virtue.id;

    this.props.appStore.recordVirtueEntry(date, value, virtue_id);
  }

  render() {
    const virtue = this.props.virtue;

    return (
      <div className="Virtue col-6">
        <h1 className="Virtue-title">{ virtue.title }</h1>
        <p className="Virtue-quote">{ virtue.quote }</p>
        <button className="btn btn-success" onClick={ this.handleSuccess.bind(this) }>Yes</button>
        <button className="btn btn-danger" onClick={ this.handleFail.bind(this) }>No</button>
      </div>
    );
  }
}

