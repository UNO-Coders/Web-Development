import React from 'react';
import ReactDOM from 'react-dom';
import { Theme } from '@twilio-paste/core/theme';
import { Provider } from 'react-redux';

import Application from './components/Application';
import { store } from './store';

import './index.css';

ReactDOM.render(
  <Provider store={store}>
    <Theme.Provider theme="default">
      <React.StrictMode>
        <Application />
      </React.StrictMode>
    </Theme.Provider>
  </Provider>,
  document.getElementById('root')
);
