const functions = require('firebase-functions');
const nodemailer = require('nodemailer');

// Configure the email transport using the default SMTP transport and a GMail account.
// For Gmail, enable "Allow less secure apps" option in your account.
const mailTransport = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: 'bekatur32@gmail.com',
        pass: 'your-email-password',
    },
});

exports.sendWelcomeEmail = functions.https.onCall((data, context) => {
    const mailOptions = {
        from: 'bekatur32@gmail.com',
        to: data.email,
        subject: 'Welcome!',
        text: `Hello ${data.name}, welcome to our service!`,
    };

    return mailTransport.sendMail(mailOptions)
        .then(() => {
            return { success: true };
        })
        .catch((error) => {
            throw new functions.https.HttpsError('internal', error.message);
        });
});
