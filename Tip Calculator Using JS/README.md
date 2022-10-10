# Tip Calculator

A sample React and Redux application for teaching React and Redux.

Part of the [Redux Fundamentals](https://stevekinney.github.io/redux-fundamentals) course for [Frontend Masters](https://frontendmasters.com).

## Building a Tip Calculator in Redux

Let's start by creating some initial state for our application.

```js
const initialState = [
  { uuid: 1, name: 'Tofu Roast', price: 14, quantity: 1 },
  { uuid: 2, name: 'Vegan Ham', price: 12, quantity: 1 }
]
```

We'll also start with the world's simplest reducer again.

```ts
export const reducer = (state = initialState, action) => {
  return state;
};
```

Okay, we mostly have everything we need to create a store. Let's hook this up to our React application.

In `index.js`, let's pull in everything we need.

```js
import { Provider } from 'react-redux';
import { createStore } from 'redux';
import { reducer } from './reducer';
```

Next we'll create our store.

```js
const store = createStore(reducer);
```

So far, so good. Now, just like with the Context API, we need to wrap our application in a `Provider`.

```js
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
```

## Hooking It Up to the Redux Dev Tools

`createStore` takes a second argument for `enhancers` and/or middleware.

We can add in a line to hook up our Redux store to the developer tools.

```js
const store = createStore(
  reducer,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);
```

If we look at the tools, we'll see the following that Redux fired an `@@INIT` event. This went through the reducer and then populated the state with our `initialState`.

## Hooking the State Up a Component

This is very cool. But, we still have our hard-coded menu items.

Let's fix this. We're going to start by using `connect`, but we'll play around with some other approaches in a bit.

```js
import { connect } from 'react-redux';
```

`connect` takes a bunch of arguments, but we'll start by just focusing on two of them. `mapStateToProps` and `mapDispatchToProps`.

We'll copy over some of the logic from `Calculator.js` and move it into our new `MenuItems.js`.

```js
const MenuItems = ({ items }) => {
  return (
    <>
      {items.map((item) => (
        <MenuItem {...item} key={item.uuid} />
      ))}
    </>
  );
};
```

`MenuItems` takes a prop called `items`. It would be cool to figure out how to map the items in our Redux store to the props that `MenuItems` takes, right? Maybe, we should make a function called `mapStateToProps`.

```js
const mapStateToProps = (state) => {
  // …
};
```

This is just a function where Redux is going to pass in our entire state tree and we can pluck off what we want from it and map it to the props of the component that we're working with.

```js
const mapStateToProps = (state) => {
  return {
    items: state
  };
};

export const ConnectedMenuItems = connect(mapStateToProps)(MenuItems);
```

You'll notice two sets of parentheses. `connect` actually returns a function that takes a component as an argument. This allows you to reuse your logic to hook it up to multiple components.

Now, we can update our `Calculator` component.

```js
const Calculator = () => {
  return (
    <Card>
      <NewItemForm />
      <Stack orientation="vertical" spacing="space60">
        <ConnectedMenuItems /> // 👈
      </Stack>
      <TipSelect />
      <Stack orientation="vertical" spacing="space30">
        <SummaryLine title="Subtotal">$0.00</SummaryLine>
        <SummaryLine title="Tax">$0.00</SummaryLine>
        <SummaryLine title="Tip Amount">$0.00</SummaryLine>
        <SummaryLine title="Total">$0.00</SummaryLine>
      </Stack>
    </Card>
  );
};
```

## Dispatching from the UI

In order to update the state—and subsequently the UI, we're going to need to do a few things.

- We need an action to dispatch.
- We need the reducer to deal with that action.
- We need the `NewItemForm` to dispatch that action.

We'll use the aciton creator pattern to format our action for us in `reducer.js`.

```js
export const ADD_NEW_ITEM = 'ADD_NEW_ITEM';

export const addNewItem = (name, price) => {
  return {
    type: ADD_NEW_ITEM,
    payload: {
      uuid: Date.now(),
      name,
      price,
      quantity: 1
    }
  };
};
```

Next, we'll update the reducer.

```js
export const reducer = (state = initialState, action) => {
  if (action.type === ADD_NEW_ITEM) {
    return [...state, action.payload];
  }

  return state;
};
```

Let's try out firing an action from the developer tools.

```js
{
  type: 'ADD_NEW_ITEM',
  payload: { uuid: 3, name: 'Braised Seitan', price: 12, quantity: 1 }
}
```

Cool, we're most of the way there. Now we just need to wire that up with the `NewItemForm` and we're good to go.

We can't just require the action creator in the component because it's just a function that returns an object and it doesn't know anything about `dispatch`.

What we want to do is pass in an `onSubmit` prop, which the component is already expecting that is bound to Redux's `dispatch`.

Let's start with the simplest possible version:

```js
import { connect } from 'react-redux';
import { NewItemForm } from './NewItemForm';

export const ConnectedNewItemForm = connect()(NewItemForm);
```

Connect components received `dispatch` out of the box. So, now we can do something like this:

```js
export const NewItemForm = ({ onSubmit, dispatch }) => {
  // …

  const handleSubmit = (event) => {
    event.preventDefault();

    if (typeof onSubmit === 'function') {
      onSubmit(event, { name, price });
    }

    dispatch(addNewItem(name, price));

    setName('');
    setPrice(0);
  };

  // …
};
```

(We'll also want to swap out `NewItemForm` for `ConnectedNewItemForm` in `Calculator.js`.)

This approach is a bit flawed. It ties our presentational component to Redux, which is less than optimal. It doesn't create a clear API contract. `NewItemForm` can literally dispatch anything it wants. We can do better.

Just like we can format our state to the props of a presentation component. We can do that with `dispatch` as well.

```js
import { connect } from 'react-redux';
import { NewItemForm } from './NewItemForm';
import { addNewItem } from './reducer';

const mapDispatchToProps = (dispatch) => {
  return {
    onSubmit: (name, price) => dispatch(addNewItem(name, price))
  };
};

export const ConnectedNewItemForm = connect(
  null,
  mapDispatchToProps
)(NewItemForm);
```

We can rip out that fun stuff we did with `dispatch` and put the component back to the way we found it.

Let's say we had a whole bunch of actions. We probably don't need to call each one with `dispatch` by hand. We can use `bindActionCreators` in order to take an object of action creators and spit out an object with all of those aciton creators bound to `dispatch`.

```js
const mapDispatchToProps = (dispatch) => {
  return bindActionCreators(
    {
      onSubmit: addNewItem
    },
    dispatch
  );
};
```

For simple things, we can also use a simpler syntax.

```js
const mapDispatchToProps = {
  onSubmit: addNewItem
};
```

If `connect` receives an object, it will automatically pass it to `bindActionCreators` and pass it through to the component.

## Removing an Item

**Exercise**: Can you wire up the button to remove an item from state?

There are a few ways that we can tackle this. Let's start by creating an action creator.

```js
export const REMOVE_ITEM = 'REMOVE_ITEM';

export const removeItem = (uuid) => {
  return {
    type: REMOVE_ITEM,
    payload: {
      uuid
    }
  };
};
```

And then we need to add some logic to the reducer.

```js
if (action.type === REMOVE_ITEM) {
  return state.filter(item => item.uuid !== action.payload.uuid);
}
```

That doesn't make me feel great, but here we are.

Now, this is where it's going to get a bit tricky. Our application isn't well set up for this.

We could do something like this in `MenuItems.js`.

```js
const MenuItems = ({ items, dispatch }) => {
  return (
    <>
      {items.map((item) => {
        const remove = () => dispatch(removeItem(item.uuid));
        return <MenuItem {...item} key={item.uuid} removeItem={remove} />;
      })}
    </>
  );
};
```

This will work, but it has the same problems as before.

There is another approach. React Redux comes with a `useDispatch` hook that you can pull out from wherever you want.

Inside of `MenuItem`, we can do the following:

```js
const dispatch = useDispatch();

// …

<Button
  variant="destructive_secondary"
  size="small"
  onClick={() => dispatch(removeItem(uuid))}
>
  Remove
</Button>
```

Again, not bad, but it's really tying our state management to our view layer again. (Granted, this is a general complain about hooks.)

**Exercise**: Can you implement changing the quantity and the price of an item?

### Solution

Here are the action creators:

```js
export const updatePrice = (uuid, price) => {
  return {
    type: UPDATE_PRICE,
    payload: {
      uuid,
      price
    }
  };
};

export const updateQuantity = (uuid, quantity) => {
  return {
    type: UPDATE_QUANTITY,
    payload: {
      uuid,
      price: quantity
    }
  };
};
```

In the reducer:

```js
if (action.type === UPDATE_PRICE) {
  return state.map((item) => {
    if (item.uuid !== action.payload.uuid) return item;
    return { ...item, price: action.payload.price };
  });
}

if (action.type === UPDATE_QUANTITY) {
  return state.map((item) => {
    if (item.uuid !== action.payload.uuid) return item;
    return { ...item, price: action.payload.quantity };
  });
}
```

In the component:

```js
<Box padding="space20">
  <Label htmlFor={`${uuid}-price`}>Price</Label>
  <Input
    id={`${uuid}-price`}
    insertBefore={<div>$</div>}
    value={price}
    onChange={(event) => dispatch(updatePrice(+event.target.value))}
  />
</Box>
<Box padding="space20">
  <Label htmlFor={`${uuid}-quantity`}>Quantity</Label>
  <Input
    id={`${uuid}-quantity`}
    value={quantity}
    onChange={(event) => dispatch(updateQuantity(+event.target.value))}
  />
</Box>
```

### Bonus

We could use `bindActionCreators` with the `dispatch` we got from the `useDispatch` hook.

```js
const actions = bindActionCreators(
  {
    removeItem,
    updatePrice,
    updateQuantity
  },
  dispatch
);
```

## Refactoring Our Menu Items

Can we get that syntax where we get some of those nice perks of separating our data from our view layer? (Spoiler alert: Yes.)

```js
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import MenuItem from './MenuItem';
import { removeItem, updatePrice, updateQuantity } from './reducer';

const mapStateToProps = (state, ownProps) => {
  const item = state.find((item) => item.uuid === ownProps.uuid);

  return { ...item };
};

const mapDispatchToProps = (dispatch, ownProps) => {
  return bindActionCreators(
    {
      updatePrice(price) {
        updatePrice(ownProps.uuid, price);
      },
      updateQuantity(quantity) {
        updateQuantity(ownProps.uuid, quantity);
      },
      remove() {
        removeItem(ownProps.uuid);
      }
    },
    dispatch
  );
};

export const ConnectedMenuItem = connect(
  mapStateToProps,
  mapDispatchToProps
)(MenuItem);
```

An exercise to the reader could be to write another function that passed in that `uuid` as the first argument to all of those functions.

## Deriving Data

So, what do we do about the total price? Let's talk about what we're not going to do.

We're not going to store computable data in our store and then try to keep everything up to date. We're going to use `mapStateToProps` to derive whatever data we need whenever we need it.

```js
const mapStateToProps = (state, ownProps) => {
  const item = state.find((item) => item.uuid === ownProps.uuid);

  item.total = item.price * item.quantity;

  return { ...item };
};
```

This will work, but you'll notice that when state change, it's recomputing _everything_.

What if we could figure out if things have changed that matter for this component and then only rerender in those situations?

## Using Selectors

```js
const getMenuItem = (state, props) => {
  return state.find((item) => item.uuid === props.uuid)
};

const menuItem = createSelector([getMenuItem], (item) => {
  item.total = item.price * item.quantity;
  return item;
});

const mapStateToProps = (state, ownProps) => {
  return { ...menuItem(state, ownProps) };
};
```

This is still not great. The array changes every time.

## Restructing State

All this stuff we're doing with arrays isn't great. We're scanning through an array every time to find every menu item. That's fine in this silly example, but you can see how it might now scale.

Hash maps make a lot more sense. (Hash maps are just objects in JavaScript.)

The flatter you can keep your state and the more you can use objects, the happier you'll be.

```js
export const newInitialState = {
  items: {
    1: {
      name: 'Tofu Roast',
      price: 14,
      quantity: 1
    },
    2: {
      name: 'Vegan Ham',
      price: 12,
      quantity: 1
    }
  },
  itemIds: [1, 2]
};
```

This has a bunch of advantages. You can now edit an individual menu item without re-rendering the whole list. You can also access one of them without filtering through an array.

In `MenuItems`:

```js
const MenuItems = ({ items, dispatch }) => {
  return (
    <>
      {items.map((uuid) => {
        return <ConnectedMenuItem uuid={uuid} key={uuid} />;
      })}
    </>
  );
};

const mapStateToProps = (state) => {
  return {
    items: state.itemIds
  };
};
```

We're going to refactor this, but let's do this for now in `ConnectedMenuItem` just to stop the crashing.

```js
const getMenuItem = (state, props) => {
  return state.items[props.uuid];
};
```

Then, in `reducer.js`, we'll do the following to the structure of our state.

```js
export const newInitialState = {
  items: {
    1: {
      name: 'Tofu Roast',
      price: 14,
      quantity: 1
    },
    2: {
      name: 'Vegan Ham',
      price: 12,
      quantity: 1
    }
  },
  itemIds: [1, 2]
};
```

None of our actions should need to change, but our reducer will need to get a little more complex.

**Exercise**: I'll do `ADD_NEW_ITEM` and `UPDATE_QUANTITY`, you do `UPDATE_PRICE` and `UPDATE_QUANTITY`.

```js
export const reducer = (state = newInitialState, action) => {
  if (action.type === ADD_NEW_ITEM) {
    return {
      items: {
        ...state.items,
        [action.payload.uuid]: action.payload
      },
      itemIds: [...state.itemIds, action.payload.uuid]
    };
  }

  if (action.type === REMOVE_ITEM) {
    const items = omit(state.items, action.payload.uuid);
    const itemIds = remove(state.itemIds, (id) => id !== action.payload.uuid);

    return { items, itemIds };
  }

  if (action.type === UPDATE_PRICE) {
    const items = { ...state.items };
    const target = items[action.payload.uuid];

    items[action.payload.uuid] = {
      ...target,
      price: action.payload.price
    };

    return { ...state, items };
  }

  if (action.type === UPDATE_QUANTITY) {
    const items = { ...state.items };
    const target = items[action.payload.uuid];

    items[action.payload.uuid] = {
      ...target,
      quantity: action.payload.quantity
    };

    return { ...state, items };
  }

  return state;
};
```

## Simplifying Things with Immer

Immer gives us a copy of the object to mutate and then figures out the changes it needs to make. This allows us a much simplier syntax for updating our state.

```js
if (action.type === UPDATE_PRICE) {
  return produce(state, (draftState) => {
    draftState.items[action.payload.uuid].price = action.payload.price;
  });
}
```

**Exercise**: Can you implement `REMOVE_ITEM`?

### Refactoring the Entire Reducer

We can use this pattern for the entire reducer.

```js
export const reducer = produce((state = newInitialState, action) => {
  if (action.type === ADD_NEW_ITEM) {
    state.items[action.payload.uuid] = action.payload;
    state.itemIds.push(action.payload.uuid);
  }

  if (action.type === REMOVE_ITEM) {
    delete state.items[action.payload.uuid];
    state.itemIds = remove(state.itemIds, (id) => id !== action.payload.uuid);
  }

  if (action.type === UPDATE_PRICE) {
    state.items[action.payload.uuid].price = action.payload.price;
  }

  if (action.type === UPDATE_QUANTITY) {
    state.items[action.payload.uuid].quantity = action.payload.quantity;
  }

  return state;
}, newInitialState);
```

## Breaking Apart the Reducer

One of the cool things in Redux is that all actions flow through all of the reducers. It can be helpful to break apart your reducers so that you can deal with things indpendently.

```js
export const itemReducer = produce((state = newInitialState.items, action) => {
  if (action.type === ADD_NEW_ITEM) {
    state[action.payload.uuid] = action.payload;
  }

  if (action.type === REMOVE_ITEM) {
    delete state[action.payload.uuid];
  }

  if (action.type === UPDATE_PRICE) {
    state[action.payload.uuid].price = action.payload.price;
  }

  if (action.type === UPDATE_QUANTITY) {
    state[action.payload.uuid].quantity = action.payload.quantity;
  }

  return state;
}, newInitialState.items);

export const itemIdReducer = produce(
  (state = newInitialState.itemIds, action) => {
    if (action.type === ADD_NEW_ITEM) {
      state.push(action.payload.uuid);
    }

    if (action.type === REMOVE_ITEM) {
      state = remove(state, (id) => id !== action.payload.uuid);
    }

    return state;
  },
  newInitialState.itemIds
);

export const reducer = combineReducers({
  items: itemReducer,
  itemIds: itemIdReducer
});
```

## Adding a Tip Reducer

The reducer is pretty simple in this case.

```js
const tipReducer = (amount = 15, action) => {
  if (action.type === UPDATE_TIP) {
    return action.payload;
  }

  return amount;
};
```

And then we can add it to our state tree.

```js
export const reducer = combineReducers({
  items: itemReducer,
  itemIds: itemIdReducer,
  tip: tipReducer
});
```

Our action creator is pretty straight forward as well.

```js
const updateTip = (amount) => {
  return {
    type: UPDATE_TIP,
    payload: +amount
  };
};
```

Hooking it up to the component is pretty simple too.

```js
const mapStateToProps = (state) => {
  return { amount: state.tip };
};

const mapDispatchToProps = { updateTip };

export const TipSelect = connect(
  mapStateToProps,
  mapDispatchToProps
)(({ amount, updateTip }) => {
return (
  <Box marginY="space80">
    <Label htmlFor="tip-amount">How much would you like to tip?</Label>
    <Select
      id="tip-amount"
      value={amount}
      onChange={(event) => updateTip(event.target.value)}
    >
      <Option value="15">15%</Option>
      <Option value="20">20%</Option>
      <Option value="25">25%</Option>
    </Select>
  </Box>
);
});
```

We can even update with Reselect if we wanted to—even though it's a little ridiculous.

```js
const getTip = (state) => {
  return state.tip;
};

const tipPercentage = createSelector([getTip], (tip) => {
  return tip;
});

const mapStateToProps = (state) => {
  return { amount: tipPercentage(state) };
};
```

## Homework

Map the state to the final calculations at the bottom. You should be using selectors.
