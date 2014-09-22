## TDD Utils

## New assertion tools
def assertEquals(expected,returned,message=None):
    if not expected==returned:
        if message:
            print("assertEquals Failed: |%s| |%s| %s" % (expected,returned,message))
        assert expected==returned
