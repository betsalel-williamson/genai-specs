export function validateEmail(email: string): boolean {
  if (!email) {
    return false;
  }

  return email.includes('@');
}
