import { describe, expect, it } from 'vitest';
import { validateEmail } from '../src/validator.js';

describe('validateEmail', () => {
  it('shouldAcceptValidEmailAddress', () => {
    expect(validateEmail('user@example.com')).toBe(true);
  });

  it('shouldRejectEmailWithoutAtSymbol', () => {
    expect(validateEmail('userexample.com')).toBe(false);
  });

  it('shouldRejectEmptyEmail', () => {
    expect(validateEmail('')).toBe(false);
  });
});
