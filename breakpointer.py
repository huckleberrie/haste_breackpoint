import numpy as np


class BreakPointer:

    def __init__(self, name, haste, rotation, pi, bl):
        self.name = name
        self.gcd = 1.5
        self.pi = pi
        self.bl = bl
        self.base_haste = haste
        self.haste = self.base_haste
        if self.pi:
            self.haste = self.haste * 1.25
        if self.bl:
            self.haste = self.haste * 1.30
        self.rotation = rotation
        self.tv_count = 0
        self.data = ''
        self.calc_gcds()

    def haste_conversion(self, base_cd):
        """Converts a given base CD into a new one depending on the haste."""

        return base_cd / self.haste

    def add_gcd(self, time):
        """Converts the base GCD into a new one depending on the haste and adds it to the time given."""

        new_gcd = self.haste_conversion(self.gcd)
        if new_gcd >= 0.75:
            return time + new_gcd
        else:
            return time + 0.75

    def calc_gcds(self):
        """Calculates the amount of TVs that fit into an ES window based on the GCD and a set rotation."""

        time = 0
        es_uptime = 8
        es_activation = 0
        es_active = False
        sera_uptime = 15
        sera_activation = 0
        sera_active = False
        self.data += f'{self.name}\n'
        self.data += f'Amount of Base-Haste before buffs: {(self.base_haste - 1) * 100}%, Pi={self.pi}, BL={self.bl} \n'
        last_judge = 0
        last_boj = 0
        for cd in self.rotation:
            error_judge = ''
            error_boj = ''

            if (es_uptime + (es_activation - time)) < 0:
                es_active = False

            if (sera_uptime + (sera_activation - time)) < 0:
                sera_active = False
                self.haste = self.haste / 1.08

            if cd['Name'] == 'Judge' and (time - last_judge) < self.haste_conversion(cd['CD']) and last_judge != 0:
                error_judge = ' | You made an error with the Judge CD / GCD'

            if cd['Name'] == 'BoJ' and (time - last_boj) < self.haste_conversion(cd['CD']) and last_boj != 0:
                error_boj = ' | You made an error with the BoJ CD / GCD'

            self.data += f'ES active: {es_active} | Sera active: {sera_active} | Casting: {cd["Name"]} at {time} secs {error_judge} {error_boj}\n'

            if cd['Name'] == 'Sera':
                self.haste = self.haste * 1.08
                sera_active = True
                sera_activation = time

            if cd['Name'] == 'ES':
                es_active = True
                es_activation = time

            if cd['Name'] == 'TV' and es_active:
                self.tv_count += 1

            if cd['Name'] == 'Judge':
                last_judge = time

            if cd['Name'] == 'BoJ':
                last_boj = time

            time = round(self.add_gcd(time), 2)

        self.data += f'Number of TVs in ES Window: {self.tv_count}\n'


def execute_rotation(name, rotation, pi, bl):
    """

    :param name: Takes a string to use as the file name.
    :param rotation: Takes in an array consisting of abilities.
    :param pi: Takes a boolean indicating if pi should be considered.
    :param bl: Takes a boolean indicating if bl should be considered.
    :return: Return the results of the iteration as a string.
    """
    last_tv_count = 0
    text = ''
    for i in np.arange(1.0, 2.01, 0.01):
        BP = BreakPointer(name, i, rotation, pi=pi, bl=bl)
        if BP.tv_count is not last_tv_count:
            text += f'{BP.data}\n'
            last_tv_count = BP.tv_count
    return text


def setup_rotation(name, rotation, extra):
    """Setup the different combinations of pi and bl.

    Puts some basic formatting into the results.

    :param name: Takes a string to use as the file name.
    :param rotation: Takes in an array consisting of abilities.
    :param extra: Takes in a string with custom information.
    """
    full_text = 'Rotation: '
    for cast in rotation:
        full_text += f'{cast["Name"]} - '
    full_text += f'\n{extra}'
    full_text += '\n---------------------------------------------------\n'
    full_text += execute_rotation(name, rotation, pi=False, bl=False)
    full_text += '---------------------------------------------------\n'
    full_text += execute_rotation(name, rotation, pi=False, bl=True)
    full_text += '---------------------------------------------------\n'
    full_text += execute_rotation(name, rotation, pi=True, bl=False)
    full_text += '---------------------------------------------------\n'
    full_text += execute_rotation(name, rotation, pi=True, bl=True)
    with open(f'reports\{name}.txt', 'a') as file:
        file.write(full_text)


if __name__ == '__main__':
    cs = {
        'Name': 'CS',
        'CD': 6.0,
    }
    boj = {
        'Name': 'BoJ',
        'CD': 12.0,
    }
    judge = {
        'Name': 'Judge',
        'CD': 12.0,
    }
    how = {
        'Name': 'HoW',
        'CD': 7.5,
    }
    sera = {
        'Name': 'Sera',
    }
    es = {
        'Name': 'ES',
    }
    dt = {
        'Name': 'DT',
    }
    wake = {
        'Name': 'Wake',
    }
    fr = {
        'Name': 'FR',
    }
    tv = {
        'Name': 'TV',
    }
    extra_text = "Base Rotation without MJ or AoW | RC 3 proc"
    base_rotation = [judge, boj, cs, cs, sera, how, cs, fr, es, dt, tv, wake, tv, boj, tv, how, judge, tv]
    setup_rotation('Judge-Sera-DT4', base_rotation, extra_text)

    extra_text = "Base Rotation without MJ or AoW | RC 2 proc"
    base_rotation = [judge, boj, cs, cs, sera, how, cs, fr, es, dt, tv, wake, tv, boj, tv, how, judge, tv]
    setup_rotation('Judge-Sera-DT3', base_rotation, extra_text)

    extra_text = "Base Rotation without MJ or AoW | RC 1 proc"
    base_rotation = [judge, boj, cs, cs, sera, how, cs, fr, es, dt, tv, wake, tv, boj, tv, how, judge, cs, tv]
    setup_rotation('Judge-Sera-DT2', base_rotation, extra_text)

    extra_text = "Base Rotation without MJ or AoW | RC 0 proc"
    base_rotation = [judge, boj, cs, cs, sera, how, cs, fr, es, dt, tv, wake, tv, boj, how, tv, judge, cs, cs, tv]
    setup_rotation('Judge-Sera-DT1', base_rotation, extra_text)

    """MJ LEGENDARY - With Judgement Proc at the End."""

    extra_text = "Assumes that DT procs one MJ. The Judgement cast at the end is proccing MJ. | RC 3 proc"
    pre_judge_mj_rotation = [judge, boj, cs, cs, sera, how, cs, fr, es, dt, tv, tv, wake, tv, boj, judge, tv, how, cs,
                             tv]
    setup_rotation('Judge-Sera-1MJ-DT4-MJEND', pre_judge_mj_rotation, extra_text)

    extra_text = "Assumes that DT procs one MJ. The Judgement cast at the end is proccing MJ. | RC 2 proc"
    pre_judge_mj_rotation = [judge, boj, cs, cs, sera, how, cs, fr, es, dt, tv, tv, wake, tv, boj, judge, tv, how, cs,
                             tv]
    setup_rotation('Judge-Sera-1MJ-DT3-MJEND', pre_judge_mj_rotation, extra_text)

    extra_text = "Assumes that DT procs one MJ. The Judgement cast at the end is proccing MJ. | RC 1 proc"
    pre_judge_mj_rotation = [judge, boj, cs, cs, sera, how, cs, fr, es, dt, tv, wake, tv, judge, tv, boj, tv, how, cs,
                             tv]
    setup_rotation('Judge-Sera-1MJ-DT2-MJEND', pre_judge_mj_rotation, extra_text)

    extra_text = "Assumes that DT procs one MJ. The Judgement cast at the end is proccing MJ. | RC 0 proc"
    pre_judge_mj_rotation = [judge, boj, cs, cs, sera, how, cs, fr, es, dt, tv, wake, tv, boj, tv, judge, how, tv, cs,
                             cs]
    setup_rotation('Judge-Sera-1MJ-DT1-MJEND', pre_judge_mj_rotation, extra_text)

    """MJ LEGENDARY - Without Judgement Proc at the End."""

    extra_text = "Assumes that DT procs one MJ. The Judgement cast at the end is not proccing MJ. | RC 3 proc"
    pre_judge_mj_rotation = [judge, boj, cs, cs, sera, how, cs, fr, es, dt, tv, tv, wake, tv, boj, judge, tv, how, cs,
                             cs, tv]
    setup_rotation('Judge-Sera-1MJ-DT4', pre_judge_mj_rotation, extra_text)

    extra_text = "Assumes that DT procs one MJ. The Judgement cast at the end is not proccing MJ. | RC 2 proc"
    pre_judge_mj_rotation = [judge, boj, cs, cs, sera, how, cs, fr, es, dt, tv, tv, wake, tv, boj, judge, tv, how, cs,
                             cs, tv]
    setup_rotation('Judge-Sera-1MJ-DT3', pre_judge_mj_rotation, extra_text)

    extra_text = "Assumes that DT procs one MJ. The Judgement cast at the end is not proccing MJ. | RC 1 proc"
    pre_judge_mj_rotation = [judge, boj, cs, cs, sera, how, cs, fr, es, dt, tv, wake, tv, judge, tv, boj, how, tv, cs,
                             cs]
    setup_rotation('Judge-Sera-1MJ-DT2', pre_judge_mj_rotation, extra_text)

    extra_text = "Assumes that DT procs one MJ. The Judgement cast at the end is not proccing MJ. | RC 0 proc"
    pre_judge_mj_rotation = [judge, boj, cs, cs, sera, how, cs, fr, es, dt, tv, wake, tv, boj, tv, judge, how, cs, tv,
                             cs]
    setup_rotation('Judge-Sera-1MJ-DT1', pre_judge_mj_rotation, extra_text)

    extra_text = "Assumes that DT procs two Mjs. The Judgement cast at the end is proccing MJ. | RC 3 proc"
    pre_judge_lucky_dt_mj_rotation = [judge, boj, cs, cs, sera, how, cs, fr, es, dt, tv, tv, wake, tv, boj, tv, judge,
                                      how, cs, tv]
    setup_rotation('Judge-Sera-2MJ-DT4', pre_judge_lucky_dt_mj_rotation, extra_text)

    extra_text = "Assumes that DT procs two Mjs. The Judgement cast at the end is proccing MJ. | RC 3 proc"
    pre_judge_lucky_dt_mj_rotation = [judge, boj, cs, cs, sera, how, cs, fr, es, dt, tv, tv, wake, tv, boj, tv, judge,
                                      how, tv]
    setup_rotation('Judge-Sera-2MJ-DT4-MJEND', pre_judge_lucky_dt_mj_rotation, extra_text)

    """MJ LEGENDARY - Sera is casted before Judgement and we assume an AoW proc at the start for better buildup."""

    extra_text = "Assumes that DT procs one MJ. The Judgement cast after Sera is proccing one MJ. One AoW proc guarantees quick build up to 5 HP pre ES. | RC 3 proc."
    after_judge_mj_rotation = [boj, cs, cs, sera, how, boj, judge, fr, es, tv, dt, tv, wake, tv, how, tv, boj, judge,
                               tv]
    setup_rotation('Sera-JudgeMJ-1AoW-1MJ-DT4', after_judge_mj_rotation, extra_text)

    extra_text = "Assumes that DT procs one MJ. The Judgement cast after Sera is proccing one MJ. One AoW proc guarantees quick build up to 5 HP pre ES. | RC 2 proc."
    after_judge_mj_rotation = [boj, cs, cs, sera, how, boj, judge, fr, es, tv, dt, tv, wake, tv, how, judge, tv, boj,
                               cs, tv]
    setup_rotation('Sera-JudgeMJ-1AoW-1MJ-DT3', after_judge_mj_rotation, extra_text)

    extra_text = "Assumes that DT procs one MJ. The Judgement cast after Sera is proccing one MJ. One AoW proc guarantees quick build up to 5 HP pre ES. | RC 1 proc."
    after_judge_mj_rotation = [boj, cs, cs, sera, how, boj, judge, fr, es, tv, dt, tv, wake, tv, how, judge, cs, tv,
                               boj, how, tv]
    setup_rotation('Sera-JudgeMJ-1AoW-1MJ-DT2', after_judge_mj_rotation, extra_text)

    extra_text = "Assumes that DT procs one MJ. The Judgement cast after Sera is proccing one MJ. One AoW proc guarantees quick build up to 5 HP pre ES. | RC 0 proc."
    after_judge_mj_rotation = [boj, cs, cs, sera, how, boj, judge, fr, es, tv, dt, wake, tv, how, tv, boj, judge, tv]
    setup_rotation('Sera-JudgeMJ-1AoW-1MJ-DT1', after_judge_mj_rotation, extra_text)

    extra_text = "Assumes that DT procs two MJ. The Judgement cast after Sera is proccing one MJ. One AoW proc guarantees quick build up to 5 HP pre ES.  | RC 3 proc."
    after_judge_lucky_dt_mj_rotation = [boj, cs, cs, sera, how, boj, judge, fr, es, tv, dt, tv, tv, wake, tv, boj, tv,
                                        how, judge, tv]
    setup_rotation('Sera-JudgeMJ-1AoW-2MJ-DT4', after_judge_lucky_dt_mj_rotation, extra_text)
