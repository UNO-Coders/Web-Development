import {
  Box,
  Button,
  Card,
  Flex,
  Heading,
  Input,
  Label
} from '@twilio-paste/core';

import { toCurrency } from '../utilities';

export const MenuItem = ({
  uuid,
  name,
  price,
  quantity,
  total,
  updatePrice = () => {},
  updateQuantity = () => {},
  remove = () => {}
}) => {
  return (
    <Card marginTop="space40">
      <Heading variant="heading30" as="h3">
        {name}
      </Heading>
      <Flex>
        <Box padding="space20">
          <Label htmlFor={`$item-${uuid}-price`}>Price</Label>
          <Input
            id={`$item-${uuid}-price`}
            insertBefore={<div>$</div>}
            value={price}
            type="number"
            onChange={(event) => updatePrice(event.target.value)}
          />
        </Box>
        <Box padding="space20">
          <Label htmlFor={`$item-${uuid}-quantity`}>Quantity</Label>
          <Input
            id={`$item-${uuid}-quantity`}
            value={quantity}
            type="number"
            onChange={(event) => updateQuantity(event.target.value)}
          />
        </Box>
        <Box padding="space20" textAlign="right" width="100%">
          <Heading variant="heading50">Total</Heading>
          {toCurrency(total)}
        </Box>
      </Flex>
      <Box width="100%" textAlign="right">
        <Button variant="destructive_secondary" size="small" onClick={remove}>
          Remove
        </Button>
      </Box>
    </Card>
  );
};

export default MenuItem;
