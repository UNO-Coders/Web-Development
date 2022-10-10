export const TIP_PERCENTAGE_UPDATED = 'UPDATE_TIP_PERCENTAGE';

export const updateTip = (tipPercentage) => ({
  type: TIP_PERCENTAGE_UPDATED,
  payload: parseInt(tipPercentage, 10)
});
