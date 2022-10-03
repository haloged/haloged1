const types = {
    isInvisibleWidget: true,
    type: "COCO_TOOLS_WIDGET",
    icon: "https://ocean.codemao.cn/appcraft/resource/icon/%E5%9F%BA%E7%A1%80/%E8%B0%83%E8%8A%82.svg",
    title: "CoCo工具箱",
    version: "1.0.0",
    isGlobalWidget: true,
    properties: [],
    methods: [],
    events: [],
};

class Widget extends InvisibleWidget {
    constructor(props) {
        super(props);

    }

}

types['methods'].push({
    key: 'OS',
    label: '获取操作系统',
    params: [],
    valueType: ['string','number','boolean','array','color','object',],
})
Widget.prototype.OS = function () {
      return (this.navigator.platform);
}
types['methods'].push({
    key: 'TIME',
    label: '获取时间戳',
    params: [],
    valueType: ['string','number','boolean','array','color','object',],
})
Widget.prototype.TIME = function () {
      return (new Date().getTime());
}
types['methods'].push({
    key: 'VW',
    label: '获取屏幕宽度',
    params: [],
    valueType: ['string','number','boolean','array','color','object',],
})
Widget.prototype.VW = function () {
      return (this.screen.width);
}
types['methods'].push({
    key: 'VH',
    label: '获取屏幕长度',
    params: [],
    valueType: ['string','number','boolean','array','color','object',],
})
Widget.prototype.VH = function () {
      return (this.screen.height);
}
types['methods'].push({
    key: 'XS1',
    label: '获取屏幕像素深度',
    params: [],
    valueType: ['string','number','boolean','array','color','object',],
})
Widget.prototype.XS1 = function () {
      return (this.screen.pixelDepth);
}
types['methods'].push({
    key: 'XS1',
    label: '获取屏幕色深',
    params: [],
    valueType: ['string','number','boolean','array','color','object',],
})
Widget.prototype.XS1 = function () {
      return (this.screen.colorDepth);
}
types['methods'].push({
    key: 'XS2',
    label: '获取屏幕色深',
    params: [],
    valueType: ['string','number','boolean','array','color','object',],
})
Widget.prototype.XS2 = function () {
      return (this.screen.colorDepth);
}
types['methods'].push({
    key: 'L',
    label: '获取语言',
    params: [],
    valueType: ['string','number','boolean','array','color','object',],
})
Widget.prototype.L = function () {
      return (this.navigator.language);
}
types['methods'].push({
    key: 'QK',
    label: '清空F12控制台',
    params: [],

})
Widget.prototype.QK = function () {
      console.clean();

}
types['methods'].push({
    key: 'JC',
    label: '检查是否有网络',
    params: [],
    valueType: 'boolean',
})
Widget.prototype.JC = function () {
      if ((this.navigator.onLine) == true) {
    return true;} else {
    return false;}

}
types['methods'].push({
    key: 'TIME1',
    label: '获取当前时间（YY/MM/DD）',
    params: [],
    valueType: ['string','number','boolean','array','color','object',],
})
Widget.prototype.TIME1 = function () {
      return ([new Date().getFullYear(),'/',new Date().getMonth(),'/',new Date().getDate()].join(''));
}
types['methods'].push({
    key: 'TIME2',
    label: '获取当前时间（TT/MM/SS）',
    params: [],
    valueType: ['string','number','boolean','array','color','object',],
})
Widget.prototype.TIME2 = function () {
      return ([new Date().getHours(),':',new Date().getMinutes(),':',new Date().getSeconds()].join(''));
}
types['methods'].push({
    key: 'WEK',
    label: '获取当前星期',
    params: [],
    valueType: ['string','number','boolean','array','color','object',],
})
Widget.prototype.WEK = function () {
      return (new Date().getDay());
}
exports.types = types;
exports.widget = Widget;
