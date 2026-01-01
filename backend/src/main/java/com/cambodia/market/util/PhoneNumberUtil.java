package com.cambodia.market.util;

import com.google.i18n.phonenumbers.NumberParseException;
import com.google.i18n.phonenumbers.PhoneNumberUtil as LibPhoneNumberUtil;
import com.google.i18n.phonenumbers.Phonenumber;

public class PhoneNumberUtil {
    private static final LibPhoneNumberUtil phoneUtil = LibPhoneNumberUtil.getInstance();
    private static final String DEFAULT_REGION = "KH"; // Cambodia

    /**
     * Checks if the phone number is a valid number for the default region (Cambodia).
     */
    public static boolean isValidPhone(String raw) {
        if (raw == null) return false;
        try {
            Phonenumber.PhoneNumber number = phoneUtil.parse(raw, DEFAULT_REGION);
            return phoneUtil.isValidNumber(number);
        } catch (NumberParseException e) {
            return false;
        }
    }

    /**
     * Returns the phone number formatted in E.164 (e.g., +85512345678). If invalid, returns null.
     */
    public static String formatE164(String raw) {
        if (raw == null) return null;
        try {
            Phonenumber.PhoneNumber number = phoneUtil.parse(raw, DEFAULT_REGION);
            if (phoneUtil.isValidNumber(number)) {
                return phoneUtil.format(number, Phonenumber.PhoneNumberFormat.E164);
            }
        } catch (NumberParseException ignored) {}
        return null;
    }
}
