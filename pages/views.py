from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Project data store - can be moved to a database model later
PROJECTS = {
    'khach-san-muong-thanh-xala': {
        'slug': 'khach-san-muong-thanh-xala',
        'name': 'Khách Sạn Mường Thanh Xala',
        'category': 'Khách Sạn',
        'category_icon': 'fa-hotel',
        'category_color': '#1a3a5c',
        'short_desc': 'Tư vấn, thiết kế, thi công & nghiệm thu hệ thống PCCC và TAHK cho khách sạn cao cấp 15 tầng.',
        'location': 'Số 66 Phúc La, Phường Hà Đông, TP Hà Nội',
        'client': 'Khách sạn Mường Thanh Xala – chi nhánh Công ty Cổ phần Tập đoàn Mường Thanh',
        'year': '2024',
        'role': 'Nhà thầu độc lập',
        'scale': '15 tầng nổi và 01 tầng hầm',
        'scope': 'Tư vấn thiết kế hệ thống PCCC và TAHK, thẩm duyệt về PCCC. Cung cấp và lắp đặt hệ thống PCCC và TAHK; tổ chức nghiệm thu về PCCC',
        'description': 'Dự án KHÁCH SẠN MƯỜNG THANH XALA nằm trong khu đô thị Xala, được thiết kế với quy mô 15 tầng và 01 tầng hầm. Dự án là 1 khách sạn cao cấp trong khu vực với Chủ Đầu tư là tập đoàn có tiếng trong ngành khách sạn Việt Nam.',
        'highlights': [
            {
                'title': 'Tiêu chuẩn cao cấp',
                'icon': 'fa-star',
                'content': 'Nằm trong chuỗi khách sạn của Tập đoàn Mường Thanh – một trong những thương hiệu khách sạn hàng đầu Việt Nam, dự án đòi hỏi sự khắt khe về tính an toàn tuyệt đối và sự phối hợp nhịp nhàng giữa hệ thống PCCC với kiến trúc sang trọng của tòa nhà.'
            },
            {
                'title': 'Tiến độ thần tốc',
                'icon': 'fa-clock',
                'content': 'Với tư cách nhà thầu độc lập, chúng tôi đã tối ưu hóa quy trình từ khâu thiết kế đến nghiệm thu để đáp ứng tiến độ khẩn trương của dự án trong năm 2024.'
            },
        ],
        'work_items': [
            {
                'title': 'Tư vấn và Pháp lý PCCC',
                'icon': 'fa-file-contract',
                'tasks': [
                    'Tư vấn thiết kế hệ thống Phòng cháy chữa cháy (PCCC) và hệ thống Tạo áp cầu thang - Hút khói (TAHK).',
                    'Thực hiện thủ tục, hồ sơ và đại diện Chủ đầu tư làm việc với cơ quan chức năng để Thẩm duyệt thiết kế về PCCC.',
                ]
            },
            {
                'title': 'Cung cấp và Thi công',
                'icon': 'fa-wrench',
                'tasks': [
                    'Cung cấp vật tư, thiết bị đạt chuẩn cho hệ thống PCCC & TAHK.',
                    'Trực tiếp lắp đặt, đấu nối và vận hành thử nghiệm hệ thống tại hiện trường, đảm bảo đúng tiêu chuẩn kỹ thuật và tính thẩm mỹ của khách sạn cao cấp.',
                ]
            },
            {
                'title': 'Nghiệm thu và Bàn giao',
                'icon': 'fa-clipboard-check',
                'tasks': [
                    'Tổ chức thực hiện công tác Nghiệm thu về PCCC với Cục/Phòng Cảnh sát PCCC & CNCH.',
                    'Hoàn thiện hồ sơ hoàn công và bàn giao hệ thống đi vào hoạt động chính thức.',
                ]
            },
        ],
        'images': [
            {'src': 'images/muongthanh_exterior.png', 'alt': 'Toàn cảnh Khách Sạn Mường Thanh Xala'},
            {'src': 'images/muongthanh_pccc_1.png', 'alt': 'Hệ thống PCCC bên trong khách sạn'},
            {'src': 'images/muongthanh_pccc_2.png', 'alt': 'Phòng máy bơm chữa cháy'},
        ],
    },
    'khu-do-thi-yen-binh': {
        'slug': 'khu-do-thi-yen-binh',
        'name': 'Nhà ở cao tầng TT-03 thuộc dự án Khu đô thị Yên Bình',
        'category': 'Chung Cư',
        'category_icon': 'fa-hotel',
        'category_color': '#1a3a5c',
        'short_desc': 'Tư vấn, thiết kế, thi công & nghiệm thu hệ thống PCCC và TAHK cho tòa nhà 20 tầng.',
        'location': 'Ô đất ký hiệu TT-03 thuộc KĐT Yên Bình, phường Vạn Xuân, Tỉnh Thái Nguyên',
        'client': 'Công ty Cổ phần phát triển đô thị Yên Bình',
        'year': '2026',
        'role': 'Nhà thầu độc lập',
        'scale': '20 tầng nổi và 02 tầng hầm',
        'scope': 'Tư vấn thiết kế hệ thống PCCC và TAHK, thẩm duyệt về PCCC. Cung cấp và lắp đặt hệ thống PCCC và TAHK; tổ chức nghiệm thu về PCCC',
        'description': 'Dự án Nhà ở cao tầng TT-03 thuộc dự án Khu đô thị Yên Bình, được thiết kế với quy mô 20 tầng và 02 tầng hầm. Dự án là tòa nhà chung cư tại KĐT Yên Bình, phường Vạn Xuân, Tỉnh Thái Nguyên',
        'highlights': [
            {
                'title': 'Tiêu chuẩn cao cấp',
                'icon': 'fa-star',
                'content': 'Nằm trong chuỗi tòa nhà chung cư cao tầng thuộc dự án khu đô thị Yên Bình, dự án đòi hỏi sự khắt khe về tính an toàn tuyệt đối và sự phối hợp nhịp nhàng giữa hệ thống PCCC với không gian quần thể của khu đô thị.'
            },
            {
                'title': 'Tiến độ thần tốc',
                'icon': 'fa-clock',
                'content': 'Với tư cách nhà thầu độc lập, chúng tôi đã tối ưu hóa quy trình từ khâu thiết kế đến nghiệm thu để đáp ứng tiến độ khẩn trương của dự án trong năm 2026.'
            },
        ],
        'work_items': [
            {
                'title': 'Tư vấn và Pháp lý PCCC',
                'icon': 'fa-file-contract',
                'tasks': [
                    'Tư vấn thiết kế hệ thống Phòng cháy chữa cháy (PCCC) và hệ thống Tạo áp cầu thang - Hút khói (TAHK).',
                    'Thực hiện thủ tục, hồ sơ và đại diện Chủ đầu tư làm việc với cơ quan chức năng để Thẩm duyệt thiết kế về PCCC.',
                ]
            },
            {
                'title': 'Cung cấp và Thi công',
                'icon': 'fa-wrench',
                'tasks': [
                    'Cung cấp vật tư, thiết bị đạt chuẩn cho hệ thống PCCC & TAHK.',
                    'Trực tiếp lắp đặt, đấu nối và vận hành thử nghiệm hệ thống tại hiện trường, đảm bảo đúng tiêu chuẩn kỹ thuật và tính thẩm mỹ của khách sạn cao cấp.',
                ]
            },
            {
                'title': 'Nghiệm thu và Bàn giao',
                'icon': 'fa-clipboard-check',
                'tasks': [
                    'Tổ chức thực hiện công tác Nghiệm thu về PCCC với Cục/Phòng Cảnh sát PCCC & CNCH.',
                    'Hoàn thiện hồ sơ hoàn công và bàn giao hệ thống đi vào hoạt động chính thức.',
                ]
            },
        ],
        'images': [
            {'src': 'images/project_yenbinh.jpg', 'alt': 'Nhà ở cao tầng TT-03 thuộc dự án Khu đô thị Yên Bình'},
            {'src': 'images/muongthanh_pccc_1.png', 'alt': 'Hệ thống PCCC bên trong khách sạn'},
            {'src': 'images/muongthanh_pccc_2.png', 'alt': 'Phòng máy bơm chữa cháy'},
        ],
    },
}

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def projects(request):
    return render(request, 'pages/projects.html')

def project_detail(request, project_slug):
    project = PROJECTS.get(project_slug)
    if not project:
        raise Http404("Dự án không tồn tại")
    return render(request, 'pages/project_detail.html', {'project': project})

def news(request):
    return render(request, 'pages/news.html')

def contact(request):
    return render(request, 'pages/contact.html')
