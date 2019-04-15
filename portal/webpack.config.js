const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    output: {
        path: path.resolve(__dirname, './dist/webpack_bundles/'),
        filename: 'main.js'
    },
    module: {
        rules: [{
            test: /\.scss$/,
            use: [ 'style-loader', 'css-loader', 'sass-loader' ]
        }]
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
    ],
    devtool: 'inline-source-map'
};