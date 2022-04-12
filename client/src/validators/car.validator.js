import Joi from "joi";

export const carValidator = Joi.object({
    id: Joi.number().min(0),
    brand: Joi.string().regex(new RegExp('^[a-zA-ZА-яіІїЇґҐ]{1,20}$')).required().messages({
        'string.empty': '"brand" cannot be empty',
        'string.pattern.base': 'Only letters min 1 max 20'
    }),
    year: Joi.number().min(1990).max(new Date().getFullYear()).required().messages({
        'number.base': 'Value has to be 1990 - 2022 inbetween',
        'number.min': 'Value has to be greater than or equal 1990',
        'number.max': 'Value has to be less than or equal 2022'
    }),
    price: Joi.number().min(0).max(1000000).required().messages({
        'number.base': 'Value has to be 1 - 1000000 inbetween',
        'number.min': 'Value has to be greater than 0',
        'number.max': 'Value has to be less than or equal 1000000'
    })
})