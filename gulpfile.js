// Agency Next Gulpfile
// Author: Patrick Beeson, pbeeson@thevariable.com

var gulp = require('gulp');

// Plugins
var jshint = require('gulp-jshint');
var stylus = require('gulp-stylus');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var minifyCSS = require('gulp-minify-css');
var nib = require('nib');

// Link Task
gulp.task('lint', function() {
    gulp.src('js/*.js')
        .pipe(jshint())
        .pipe(jshint.reporter('default'));
});

// Compile our Stylus
gulp.task('stylus', function() {
    gulp.src('agency/static/css/app.styl')
        .pipe(stylus({
            use: [nib()],
            compress: false
        }))
        .pipe(gulp.dest('agency/static/css'));
});

// Concatenate CSS
gulp.task('styles', function() {
    gulp.src(['agency/static/css/slick.css', 'agency/static/css/app.css'])
        .pipe(concat('all.min.css'))
        .pipe(gulp.dest('agency/static/css'));
});

// Minify CSS
gulp.task('minify-css', function() {
    gulp.src('agency/static/css/all.min.css')
        .pipe(minifyCSS({keepBreaks:true}))
        .pipe(gulp.dest('agency/static/css'));
});

// Concatenate and minify js
gulp.task('scripts', function() {
    gulp.src([
            'agency/static/js/jquery.js',
            'agency/static/js/jquery.stellar.js',
            'agency/static/js/fastclick.js',
            'agency/static/js/modernizr.custom.min.js',
            'agency/static/js/parallax.js',
            'agency/static/js/parsley.js',
            'agency/static/js/slick.js',
            'agency/static/js/app.js',
        ])
        .pipe(concat('all.js'))
        .pipe(gulp.dest('agency/static/js'))
        .pipe(rename('all.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest('agency/static/js'));
});

// Watch for changes
gulp.task('watch', function() {
    gulp.watch('agency/static/js/*.js', ['lint', 'scripts']);
    gulp.watch('agency/static/css/app.styl', ['stylus']);
});

gulp.task('default', ['minify-css', 'lint', 'stylus', 'styles', 'scripts', 'watch']);
gulp.task('css', ['stylus', 'styles', 'minify-css']);
