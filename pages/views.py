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
            {'src': 'images/muongthanh_1.jpg', 'alt': 'Khách Sạn Mường Thanh Xala'},
            {'src': 'images/muongthanh_2.jpg', 'alt': 'Khách Sạn Mường Thanh Xala'},
            {'src': 'images/muongthanh_3.jpg', 'alt': 'Khách Sạn Mường Thanh Xala'},
            {'src': 'images/muongthanh_4.jpg', 'alt': 'Khách Sạn Mường Thanh Xala'},
            {'src': 'images/muongthanh_5.jpg', 'alt': 'Khách Sạn Mường Thanh Xala'},
            {'src': 'images/muongthanh_6.jpg', 'alt': 'Khách Sạn Mường Thanh Xala'},
        ],
    },
    'khu-do-thi-yen-binh': {
        'slug': 'khu-do-thi-yen-binh',
        'name': 'Nhà ở cao tầng TT-01 thuộc dự án Khu đô thị Yên Bình',
        'category': 'Chung Cư',
        'category_icon': 'fa-hotel',
        'category_color': '#1a3a5c',
        'short_desc': 'Tư vấn, thiết kế, thi công & nghiệm thu hệ thống PCCC và TAHK cho tòa nhà 20 tầng.',
        'location': 'Ô đất ký hiệu TT-01 thuộc KĐT Yên Bình, phường Vạn Xuân, Tỉnh Thái Nguyên',
        'client': 'Công ty Cổ phần phát triển đô thị Yên Bình',
        'year': '2025-2026',
        'role': 'Nhà thầu độc lập',
        'scale': '20 tầng nổi và 02 tầng hầm',
        'scope': 'Tư vấn thiết kế hệ thống PCCC và TAHK, thẩm duyệt về PCCC. Cung cấp và lắp đặt hệ thống PCCC và TAHK; tổ chức nghiệm thu về PCCC',
        'description': 'Dự án Nhà ở cao tầng TT-01 thuộc dự án Khu đô thị Yên Bình, được thiết kế với quy mô 20 tầng và 02 tầng hầm. Dự án là tòa nhà chung cư tại KĐT Yên Bình, phường Vạn Xuân, Tỉnh Thái Nguyên',
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
            {'src': 'images/project_yenbinh_11.jpg', 'alt': 'Nhà ở cao tầng TT-01 thuộc dự án Khu đô thị Yên Bình'},
            {'src': 'images/project_yenbinh_12.jpg', 'alt': 'Nhà ở cao tầng TT-01 thuộc dự án Khu đô thị Yên Bình'},
            {'src': 'images/project_yenbinh_13.jpg', 'alt': 'Nhà ở cao tầng TT-01 thuộc dự án Khu đô thị Yên Bình'},
            {'src': 'images/project_yenbinh_14.jpg', 'alt': 'Nhà ở cao tầng TT-01 thuộc dự án Khu đô thị Yên Bình'},
        ],
    },
    'khu-do-thi-yen-binh_1': {
        'slug': 'khu-do-thi-yen-binh_1',
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
            {'src': 'images/project_yenbinh_31.jpg', 'alt': 'Nhà ở cao tầng TT-03 thuộc dự án Khu đô thị Yên Bình'},
            {'src': 'images/project_yenbinh_32.jpg', 'alt': 'Nhà ở cao tầng TT-03 thuộc dự án Khu đô thị Yên Bình' },
            {'src': 'images/project_yenbinh_33.jpg', 'alt': 'Nhà ở cao tầng TT-03 thuộc dự án Khu đô thị Yên Bình'},
            {'src': 'images/project_yenbinh_34.jpg', 'alt': 'Nhà ở cao tầng TT-03 thuộc dự án Khu đô thị Yên Bình'},
        ],
    },
    'nhom_viet_dung': {
        'slug': 'nhom_viet_dung',
        'name': 'Nhà máy Công ty cổ phần nhôm Việt Dũng',
        'category': 'Khu Công Nghiệp',
        'category_icon': 'fa-hotel',
        'category_color': '#1a3a5c',
        'short_desc': 'Tư vấn, thiết kế, thi công & nghiệm thu hệ thống PCCC và TAHK cho nhà xưởng.',
        'location': 'KCN Quang Minh, TP Hà Nội',
        'client': 'Công ty cổ phần nhôm Việt Dũng',
        'year': '2026',
        'role': 'Nhà thầu độc lập',
        'scale': 'Cụm nhà xưởng sản xuất nhôm',
        'scope': 'Tư vấn thiết kế, thẩm duyệt PCCC; Cung cấp và lắp đặt hệ thống PCCC',
        'description': 'Dự án nhà máy sản xuất nhôm của Công ty cổ phần nhôm Việt Dũng tại KCN Quang Minh, TP Hà Nội',
        'highlights': [
            {
                'title': 'Tiêu chuẩn KCN',
                'icon': 'fa-star',
                'content': 'Nằm trong KCN Quang Minh, dự án đòi hỏi sự khắt khe về tính an toàn tuyệt đối và sự phối hợp nhịp nhàng giữa hệ thống PCCC với không gian quần thể của khu công nghiệp.'
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
            {'src': 'images/nhom_vietdung_1.jpg', 'alt': 'Nhà máy Công ty cổ phần nhôm Việt Dũng'},
            {'src': 'images/nhom_vietdung_2.jpg', 'alt': 'Nhà máy Công ty cổ phần nhôm Việt Dũng' },
            {'src': 'images/nhom_vietdung_3.jpg', 'alt': 'Nhà máy Công ty cổ phần nhôm Việt Dũng' },
        ],
    },
    'chung_cu_hesco': {
        'slug': 'chung_cu_hesco',
        'name': 'Tòa nhà thương mại - Văn phòng thuộc dự án Trung tâm thương mại - văn phòng chung cư cao tầng Hesco',
        'category': 'Tòa nhà cao tầng',
        'category_icon': 'fa-hotel',
        'category_color': '#1a3a5c',
        'short_desc': 'Tư vấn, thiết kế, thi công & nghiệm thu hệ thống PCCC và TAHK cho tòa nhà thương mại - văn phòng.',
        'location': 'Số 135, Trần Phú, Quận Hà Đông, TP. Hà Nội',
        'client': 'Công ty thiết bị Thủy Lợi',
        'year': '2026',
        'role': 'Nhà thầu độc lập',
        'scale': 'Tòa nhà thương mại - Văn phòng',
        'scope': 'Tư vấn thiết kế, thẩm duyệt PCCC; Cung cấp và lắp đặt hệ thống PCCC',
        'description': 'Dự án Tòa nhà thương mại - Văn phòng thuộc dự án Trung tâm thương mại - văn phòng chung cư cao tầng Hesco tại Số 135, Trần Phú, Quận Hà Đông, TP. Hà Nội',
        'highlights': [
            {
                'title': 'Tiêu chuẩn Tòa nhà thương mại - Văn phòng',
                'icon': 'fa-star',
                'content': 'Dự án Tòa nhà thương mại - Văn phòng thuộc dự án Trung tâm thương mại - văn phòng chung cư cao tầng Hesco tại Số 135, Trần Phú, Quận Hà Đông, TP. Hà Nội'
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
            {'src': 'images/hesco_1.png', 'alt': 'Tòa nhà thương mại - Văn phòng thuộc dự án Trung tâm thương mại - văn phòng chung cư cao tầng Hesco'},
            {'src': 'images/hesco_2.png', 'alt': 'Tòa nhà thương mại - Văn phòng thuộc dự án Trung tâm thương mại - văn phòng chung cư cao tầng Hesco' },
            {'src': 'images/hesco_3.png', 'alt': 'Tòa nhà thương mại - Văn phòng thuộc dự án Trung tâm thương mại - văn phòng chung cư cao tầng Hesco'},
            {'src': 'images/hesco_4.png', 'alt': 'Tòa nhà thương mại - Văn phòng thuộc dự án Trung tâm thương mại - văn phòng chung cư cao tầng Hesco' },
            {'src': 'images/hesco_5.png', 'alt': 'Tòa nhà thương mại - Văn phòng thuộc dự án Trung tâm thương mại - văn phòng chung cư cao tầng Hesco'},
        ],
    }
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
