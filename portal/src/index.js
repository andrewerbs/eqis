import './styles/main.scss';

export function toggle_sidebar() {
    document.getElementsByClassName('transparent-box').item(0).classList.toggle('d-none');
    document.getElementsByClassName('on-mobile').item(0).classList.toggle('d-none');
    document.getElementsByClassName('sidebar').item(0).classList.toggle('d-none');
}
