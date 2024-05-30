# 컴사 팀플 최종본

'''
일 에너지 - 일 = 힘x이동거리, 역학적 에너지 일정, 알짜힘이 한 일은 운동에너지의 변화량
파동 - 파동의 요소, 도플러효과, 파동의 굴절
운동 - 연직상방운동, 포물선 운동
뉴턴법칙 - 관성법칙, 가속도법칙, 작용반작용
'''


#함수 정의 시작

#일과 에너지를 이용하여 알짜힘이 한 일은 운동에너지의 변화량이다는 사실을 이용
def energy(): 
    print('일과 에너지에서 구하고 싶은 것을 골라주세요')
    print('힘, 이동거리, 운동에너지, 퍼텐셜에너지, 역학적에너지')
    exfactor=["힘", "이동거리", "운동에너지", "퍼텐셜에너지", "역학적에너지"]


#올바른 요소를 입력했는지 확인
    while True:
        factor=input('요소: ')
        if factor in exfactor:
            break
        else:
            print('다시 입력해주세요!')

#힘을 선택하였을 경우
    if factor=="힘":
        print('초기 운동에너지(J), 나중 운동에너지(J), 이동거리(m)를 입력해주세요')
        kineticEnergy1=float(input('초기 운동에너지[J]: '))
        kineticEnergy2=float(input('나중 운동에너지[J]: '))
        distance=float(input('이동 거리[m]: '))

        force=(kineticEnergy2-kineticEnergy1)/distance #힘x거리 = 운동에너지 변화량
        print('이 물체의 알짜힘은 %.2f N입니다.' %force)

#이동거리를 선택했을 경우
    elif factor=="이동거리":
        print('초기 운동에너지(J), 나중 운동에너지(J), 힘(N)을 입력해주세요')
        kineticEnergy1=float(input('초기 운동에너지[J]: '))
        kineticEnergy2=float(input('나중 운동에너지[J]: '))
        force=float(input('힘[N]: '))

        distance=(kineticEnergy2-kineticEnergy1)/force #힘x거리 = 운동에너지 변화량
        print('이 물체의 이동거리는 %.2f m입니다.' %distance)

#운동에너지를 선택했을 경우
    elif factor=="운동에너지":
        print('이 물체의 질량(kg), 속력(m/s)을 입력해주세요')
        mass=float(input('질량[kg]: '))
        velocity=float(input('속력[m/s]: '))

        kineticEnergy=0.5*mass*(velocity)**2 #운동에너지 = 질량*속도제곱*0.5
        print('이 물체의 운동에너지는 &.2f J입니다.' %kineticEnergy)
    
#퍼텐셜에너지를 선택했을 경우
    elif factor=="퍼텐셜 에너지":
        print('이 물체의 질량(kg), 현재 높이(m)를 입력해주세요 (중력가속도는 9.8m/s^2로 가정)')
        mass=float(input('질량[kg]: '))
        height=float(input('현재 높이[m]: '))
             
        potentialEnergy=mass*9.8*height #퍼텐셜 에너지 = 질량*중력가속도*높이
        print('이 물체의 퍼텐셜에너지는 %.2f J입니다.' %potentialEnergy)
    
#역학적 에너지를 선택했을 경우
    elif factor == "역학적에너지" :
        print('이 물체의 질량(kg), 현재 높이(m), 속력(m/s)을 입력해주세요 (중력가속도는 9.8m/s^2로 가정)')
        mass=float(input('질량[kg]: '))
        height=float(input('현재 높이[m]: '))
        velocity=float(input('속력[m/s]: '))

        kineticEnergy=0.5*mass*(velocity)**2 #운동에너지 = 질량*속도제곱*0.5
        potentialEnergy=mass*9.8*height #퍼텐셜 에너지 = 질량*중력가속도*높이
        mechanicalEnergy=kineticEnergy+potentialEnergy #역학적 에너지 = 운동에너지 + 퍼텐셜 에너지

        print('이 물체의 운동너지는 %.2f J, 퍼텐셜에너지는 %.2f J이므로 역학적에너지는 %.2f J입니다.' %(kineticEnergy, potentialEnergy, mechanicalEnergy))

#파동의 요소를 이용하여 각각의 요소를 구함
# 파동의 속도 = 파동의 파장 / 주기 = 파동의 파장 * 진동수
def wave():
    print("파동의 주기(진동수), 파장, 속도 중 구할 요소를 입력해주세요")
    exfactor = ["주기", "진동수", "파장", "속도"]

#올바른 요소를 입력했는지 확인
    while True:
        factor = input("요소: ")
        if factor in exfactor:
            break
        else:
            print("다시 입력해주세요!")

#주기를 선택했을 경우
    if factor == "주기":
        print("\n파동의 파장과 속도를 m와 m/s 단위로 입력해주세요")
        wavelength = float(input("파장[m]: "))
        velocity = float(input("속도[m/s]: "))

        cycle = wavelength / velocity
        print("파동의 주기는 %.2f s입니다." % cycle)
    
#진동수를 선택했을 경우
    elif factor == "진동수":
        print("\n파동의 파장과 속도를 m와 m/s 단위로 입력해주세요")
        wavelength = float(input("파장[m]: "))
        velocity = float(input("속도[m/s]: "))

        frequency = velocity / wavelength
        print("파동의 진동수는 %.2f Hz입니다." % frequency)
    
#파장을 선택했을 경우
    elif factor == "파장":
        print("\n파동의 주기와 속도를 s와 m/s 단위로 입력해주세요")
        cycle = float(input("주기[s]: "))
        velocity = float(input("속도[m/s]: "))

        wavelength = cycle * velocity
        print("파동의 파장은 %.2f m입니다." % wavelength)
    
#속도를 선택했을 경우
    elif factor == "속도":  
        print("\n파동의 파장과 주기를 m와 s 단위로 입력해주세요")
        wavelength = float(input("파장[m]: "))
        cycle = float(input("주기[s]: "))

        velocity = wavelength / cycle
        print("파동의 속도는 %.2f m/s입니다." % velocity)


#도플러 효과
#파원이 이동할 경우 관찰되는 진동수 = {파동의 속도/(파동의 속도-이동속도)}*파동의 진동수
#관찰자가 이동할 경우 관찰되는 진동수 = {(파동의 속도 + 관찰자의 이동속도)/파동의 속도}*파동의 진동수
def doppler():
    print("관찰자와 파원 중 어떤 것이 이동하나요?")
    exthing = ["파원", "관찰자"]

#올바른 요소를 입력했는지 확인
    while True:
        thing = input("대상 : ")
        if thing in exthing:
            break
        else:
            print("다시 입력해주세요!")
    
#이동하는 물체가 파원일 경우
    if thing == "파원":
        frequency_sound = float(input("파원의 진동수를 입력해주세요[Hz]: "))
        movingvelocity_sound = float(input("파원의 이동속도를 입력해주세요[m/s]: "))
        velocity_sound = float(input("파동의 속도를 입력해주세요[m/s]: "))

        frequency_observer = velocity_sound * frequency_sound / (velocity_sound - movingvelocity_sound)

        print("관찰자가 관측하는 파원의 진동수 : %.2f Hz입니다." % frequency_observer)
    
#이동하는 물체가 관찰자일 경우
    elif thing == "관찰자":
        frequency_sound = float(input("파원의 진동수를 입력해주세요[Hz]: "))
        movingvelocity_observer = float(input("관찰자의 이동속도를 입력해주세요[m/s]: "))
        velocity_sound = float(input("파동의 속도를 입력해주세요[m/s]: "))

        frequency_observer = (velocity_sound + movingvelocity_observer) * frequency_sound / velocity_sound

        print("관찰자가 관측하는 파원의 진동수 : %.2f Hz입니다." % frequency_observer)


#스넬의 법칙
#스넬의 법칙 n1sin(n1)=n2sin(n2)
def snell():
    import math

    print("빛이 굴절할 때 구할 요소를 입력해주세요(각도, 굴절률)")
    exfactor = ["각도", "굴절률"]

#올바른 요소를 입력했는지 확인
    while True:
        factor = input("요소 : ")
        if factor in exfactor:
            break
        else:
            print("다시 입력해주세요!")

#각도를 입력했을 경우
    if factor == "각도":
        factor_angle = input("입사각 또는 굴절각 중 무엇을 구하나요? : ")
        #입사각을 구할 경우
        if factor_angle == "입사각":
            angle_out_degree = float(input("굴절각을 입력해주세요(도): "))
            angle_out_radian = math.radians(angle_out_degree)

            refractive_index_in = float(input("입사하는 매질의 굴절률을 입력해주세요: "))
            refractive_index_out = float(input("굴절되는 매질의 굴절률을 입력해주세요: "))

            sin_value = refractive_index_out * math.sin(angle_out_radian) / refractive_index_in

            #올바른 값이 아닐 경우 오류를 내보냄
            if -1 <= sin_value <= 1:
                angle_in_radian = math.asin(sin_value)
                angle_in_degree = math.degrees(angle_in_radian)
                print("입사각은 %.2f도입니다." % angle_in_degree)
            else:
                print("계산된 값이 물리적으로 불가능해요. 입력값을 확인해주세요.")
        #굴절각을 구할 경우
        elif factor_angle == "굴절각":
            angle_in_degree = float(input("입사각을 입력해주세요 (도): "))
            angle_in_radian = math.radians(angle_in_degree)

            refractive_index_in = float(input("입사하는 매질의 굴절률을 입력해주세요: "))
            refractive_index_out = float(input("굴절되는 매질의 굴절률을 입력해주세요: "))

            sin_value = refractive_index_in * math.sin(angle_in_radian) / refractive_index_out
            
            #올바른 값이 아닐 경우 오류를 내보냄
            if -1 <= sin_value <= 1:
                angle_out_radian = math.asin(sin_value)
                angle_out_degree = math.degrees(angle_out_radian)
                print("굴절각은 %.2f도입니다." % angle_out_degree)
            else:
                print("계산된 값이 물리적으로 불가능해요. 입력값을 확인해주세요.")
#굴절률을 입력했을 경우
    elif factor == "굴절률":
        angle_in_degree = float(input("입사각을 입력해주세요(도): "))
        angle_in_radian = math.radians(angle_in_degree)

        angle_out_degree = float(input("굴절각을 입력해주세요(도): "))
        angle_out_radian = math.radians(angle_out_degree)

        refractive_index_in = float(input("입사 매질의 굴절률을 입력해주세요 : "))

        sin_out = math.sin(angle_out_radian)

        #불가능할 경우 오류를 내보냄
        if sin_out == 0:
            print("굴절각이 0도 또는 180도일 때 굴절률을 구할 수 없어요.")
        else:
            refractive_index_out = (math.sin(angle_in_radian) * refractive_index_in) / sin_out
            print("굴절되는 매질의 굴절률은 %.2f입니다." % refractive_index_out)

#물체의 운동 파악
#1차원 운동: 연직상방 운동

def freelyfalling():
    print("이상적인 연직상방 운동에서 구하고 싶은 것을 선택해주세요.(최대높이, 최대높이 도달시간, n초에서의 속도)")

    exfactor = ["최대높이", "최대높이 도달시간", "n초에서의 속도"]

    while True:
          factor = input("요소: ")
          if factor in exfactor:
               break
          else:
               print("다시 입력해주세요!")

    if factor == "최대높이" :
         print("초기 위치(m), 초기속도(m/s)를 입력해주세요.(중력가속도= 9.8m/s*s로 계산)")
         height = float(input("초기위치[m]: "))
         velocity = float(input("초기속도[m/s]: "))

         time= velocity/9.8
         MaxH= height + velocity*time + 0.5*(-9.8)*time*time
         print("최대높이는 %.2f m입니다." % MaxH)

    elif factor == "최대높이 도달시간" :
         print("초기속도(m/s)를 입력해주세요:(중력가속도= 9.8m/s*s로 계산)")
         velocity = float(input("초기속도[m/s]: "))

         time= velocity/9.8
         print("최대높이 도달시간은 %.2f s입니다." % time)

    elif factor == "n초에서의 속도" :
         print("n초(s), 초기속도(m/s)를 입력해주세요:(중력가속도= 9.8m/s*s로 계산)")
         print("(지면에서 무한대로 멀어져있는 상황으로 가정)\n")
         ntime= float(input("n[s]: "))
         velocity = float(input("초기속도[m/s]: "))

         nvelocity = velocity + (-9.8)*ntime
         print("n초에서의 속도는 %.2f m/s입니다." % nvelocity) 

#2차원 운동: 포물선 운동
def projectile():
    import math
    print("이상적인 포물선 운동에서 구하고 싶은 것을 선택해주세요.(최대높이, 최대높이 도달시간, 수평도달거리)")

    exfactor = ["최대높이", "최대높이 도달시간", "수평도달거리"]
    
    while True:
        factor = input("요소: ")
        if factor in exfactor:
            break
        else:
            print("다시 입력해주세요!")

    if factor == "최대높이" :
        print
        print("초기경사각, 초기속도(m/s)를 입력해주세요.(중력가속도= 9.8m/s*s로 계산)\n")
        angle = float(input("초기경사각(도): "))
        velocity = float(input("초기속도[m/s]: "))

        MaxH= velocity*velocity*math.sin(angle)*math.sin(angle)/2*(9.8)
        print("최대높이는 %.2f m입니다." % MaxH)

    elif factor == "최대높이 도달시간" :
        print("초기경사각, 초기속도(m/s)를 입력해주세요.(중력가속도= 9.8m/s*s로 계산)\n")
        angle = float(input("초기경사각(도): "))
        velocity = float(input("초기속도(m/s): "))

        time= velocity*math.sin(angle)/(-9.8)
        print("최대높이 도달시간은 %.2f s입니다." % time)

    elif factor == "수평도달거리" :
        print("초기경사각, 초기속도(m/s)를 입력해주세요.(중력가속도= 9.8m/s*s로 계산)\n")
        angle = float(input("초기경사각(도): "))
        velocity = float(input("초기속도(m/s): "))

        R= velocity*velocity*2*math.sin(angle)/(-9.8)
        print("수평도달거리는 %.2f m/s입니다." % R) 

#뉴턴법칙
#뉴턴 1법칙 - 관성의 법칙
def inertia_law():
    initial_velocity = float(input("처음 속력을 입력해주세요: "))
    final_velocity = initial_velocity
    print(f"처음 속력: {initial_velocity} m/s")
    print(f"나중 속력: {final_velocity} m/s")
    print("관성에 의해 계에 외력이 작용하지 않을 경우 물체의 속력이 동일해요.")
    #퀴즈 추가

#뉴턴 2법칙 - 가속도의 법칙
def calculate_acceleration():
    print("물체에 작용하는 가속도와 알짜힘 중 구할 요소를 입력해주세요")
    exfactor = ["가속도", "알짜힘"]

#올바른 요소를 입력했는지 확인
    while True:
        factor = input("요소: ")
        if factor in exfactor:
            break
        else:
            print("다시 입력해주세요!")
    
    if factor == "가속도":
        force = float(input("물체에 작용하는 힘을 입력해주세요 (단위: N): "))
        mass = float(input("물체의 질량을 입력해주세요 (단위: kg): "))

        acceleration = calculate_acceleration(force, mass)
        print("물체의 가속도는 %.2f m/s^2 입니다." %(acceleration))

    elif factor == "알짜힘":
        mass = float(input("질량을 입력해주세요 (kg): "))
        acceleration = float(input("가속도를 입력해주세요 (m/s^2): "))
        net_force = mass * acceleration
        print(f"알짜힘은 {net_force} N입니다.")

#뉴턴 3법칙
def newtonlaw_3():
    force_on_door = float(input("손에 작용하는 힘을 입력해주세요 (N): "))
    reaction_force = force_on_door
    print("손에 작용하는 힘:", force_on_door, "N")
    print("문의 반작용 힘: -", reaction_force, "N (반대 방향)")

#퀴즈
def quiz():
    print("깜짝 퀴즈를 시작하겠습니다!")
    print("물체가 포물선 운동을 할 경우 그래프 모양이 어떨지에 대한 문제입니다!")    

    factor = ["상수", "1차", "2차"]
    answer = input("어떤 그래프의 모양을 맞추시겠어요? (y-t그래프, a-t그래프, v(y)-t그래프): ").strip()
    if answer == "a-t그래프":
        user_choose = factor.index("상수")
    elif answer == "v(y)-t그래프":
        user_choose = factor.index("1차")
    elif answer == "y-t그래프":
        user_choose = factor.index("2차")
    else:
        print("잘못된 입력입니다. 다시 입력해주세요!")
    
    print("이제 퀴즈를 진행하겠습니다!")
    guess = int(input("그래프의 모양을 선택해주세요 (0: 상수, 1: 1차, 2: 2차): "))

    if guess == user_choose:
        print("정답입니다 :)")
    else:
        print(f"틀렸습니다. 정답은 {factor[user_choose]}입니다.")

'''
프로그램 시작 
함수를 불러와서 실행함
'''
def start():
    import time

    print("안녕하세요!")
    print("물리 문제 해결을 도와주는 에이조입니다!")
    time.sleep(1)
    print("저희는 물리 문제 중에서")
    time.sleep(1)
    print("1. 일-에너지\n2. 파동\n3. 물체의 운동\n4. 뉴턴법칙")
    print("문제 해결에 도움들 드리고 있습니다")
    time.sleep(1)
    print("깜짝 퀴즈가 숨어있으니 기대해주세요!!!\n\n")

    factor = ["일-에너지", "파동", "물체의 운동", "뉴턴법칙"]

    user_choose = int(input("어떤 문제에 대한 도움을 드릴까요?\n1. 일-에너지\n2. 파동\n3. 물체의 운동\n4. 뉴턴법칙\n입력 : "))-1

    if user_choose == 0:
        print("\n일 에너지 문제 해결을 시작할게요\n")
        time.sleep(1)
        energy()
    elif user_choose == 1:
        print("\n파동 문제 해결을 시작할게요\n")
        time.sleep(1)

        print("파동의 요소, 도플러효과, 스넬의 법칙 중 해결할 문제를 골라주세요")
        factor = ["파동의 요소", "도플러효과", "스넬의 법칙"]

        user_choose_2 = int(input("\n1. 파동의 요소\n2. 도플러효과\n3. 스넬의 법칙\n입력 : "))-1
        if user_choose_2 == 0:
            wave()
        elif user_choose_2 == 1:
            doppler()
        elif user_choose_2 == 2:
            snell()

    elif user_choose == 2:
        print("\n물체의 운동 문제 해결을 시작할게요\n")
        time.sleep(1)

        print("연직상방운동과 포물선운동 중 해결할 문제를 골라주세요")
        factor = ["연직상방운동", "포물선운동"]

        user_choose_2 = int(input("\n1. 연직상방운동\n2. 도플러효과\n입력 : "))-1
        if user_choose_2 == 0:
            freelyfalling()
        elif user_choose_2 == 1:
            projectile()

    elif user_choose == 3:
        print("\n뉴턴 문제 해결을 시작할게요\n")
        time.sleep(1)

        print("뉴턴법칙 중 해결할 문제를 골라주세요")
        factor = ["연직상방운동", "포물선운동"]

        user_choose_2 = int(input("\n1. 뉴턴 1법칙 (관성의 법칙)\n2. 뉴턴 2법칙(가속도의 법칙)\n3. 뉴턴 3법칙(작용 반작용의 법칙)\n입력 : "))-1
        if user_choose_2 == 0:
            inertia_law()
            time.sleep(1)
            quiz()
        elif user_choose_2 == 1:
            calculate_acceleration()
        elif user_choose_2 == 2:
            newtonlaw_3()
    else:
        print("잘못된 입력입니다. 다시 입력해주세요!")
    print("문제 해결이 끝났어요.")