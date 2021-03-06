const CleanWebpackPlugin = require('clean-webpack-plugin');
const path = require('path');

module.exports = {
    'entry': path.resolve(__dirname, 'src', 'index.js'),
    'output': {
        'filename': 'main.js',
        'library': 'myeqip',
        'libraryTarget': 'window'
    },
    'module': {
        'rules': [
            {
                'test': /\.js$/,
                'exclude': [ /node_modules/ ],
                'use': {
                    'loader': 'babel-loader',
                    'options': {
                        'presets': [ 'env' ]
                    }
                }
            },
            {
                'test': /\.scss$/,
                'exclude': [ /node_modules/ ],
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
            {
                'test': /\.svg$/,
                'exclude': [ /node_modules/ ],
                'use': {
                    'loader': 'svg-url-loader'
                }
            },
            {
                'test': /\.(ttf|woff2)$/,
                'exclude': [ /node_modules/ ],
                'use': {
                    'loader': 'file-loader',
                    'options': {
                        'name': '[name].[ext]'
                    }
                }
            },
        ]
    },
    'plugins': [
        new CleanWebpackPlugin()
    ]
};