const CleanWebpackPlugin = require('clean-webpack-plugin');
const path = require('path');

module.exports = {
    'entry': path.resolve(__dirname, 'src', 'index.js'),
    'output': {
        'filename': 'main.js',
        'publicPath': '/static/'
    },
    'module': {
        'rules': [
            {
                'test': /\.js$/,
                'exclude': [ /node_modules/, /static_serve/ ],
                'use': {
                    'loader': 'babel-loader',
                    'options': {
                        'presets': [ 'env' ]
                    }
                }
            },
            {
                'test': /\.scss$/,
                'exclude': [ /node_modules/, /static_serve/ ],
                'use': [
                    {
                        'loader': 'file-loader',
                        'options': {
                            'name': '[name].css'
                        }
                    },
                    { 'loader': 'extract-loader' },
                    { 'loader': 'css-loader' },
                    { 'loader': 'sass-loader' }
                ]
            },
        ]
    },
    'resolve': {
        'alias': {
            'static': path.resolve('static'),
        }
    },
    'plugins': [
        new CleanWebpackPlugin()
    ]
};