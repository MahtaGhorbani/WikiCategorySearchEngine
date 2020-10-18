class Util:
    @classmethod
    def get_prefix(cls, string1, string2):
        """
        Get prefix string for two strings
        :param string1: string 1
        :param string2: string 2
        :return: The common prefix in string1 and string2
        """
        prefix = ""

        for i in range(min(len(string1), len(string2))):
            if string1[i] == string2[i]:
                prefix += string1[i]
            else:
                return prefix

        return prefix

    @classmethod
    def has_prefix(cls, string1, string2):
        """
        Check if the two strings have any prefix in common
        :param string1: string 1
        :param string2: string 2
        :return: True if both string share a prefix else False
        """
        return len(cls.get_prefix(string1, string2)) > 0
