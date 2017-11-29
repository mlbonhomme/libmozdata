def reviewer_match(short_name, bugzilla_reviewers, cc_list, reviewer_cache={}):
            assert any(subtext in diff.text for subtext in ['new mode ', 'rename ', 'copy ', 'new file mode ', 'deleted file mode ']) or any(subtext1 in diff.text and subtext2 in diff.text for (subtext1, subtext2) in [('Binary file ', ' has changed')]), 'Can\'t parse changes from patch: ' + str(diff)
            if flag['name'] != 'review' or flag['status'] == '-':
                continue

    reviewer_pattern = re.compile('r=([a-zA-Z0-9._]+)')
def bug_analysis(bug, uplift_channel=None, author_cache={}, reviewer_cache={}):
                    reviewers.add(reviewer_match(short_reviewer, bugzilla_reviewers | bugzilla_authors, bug['cc_detail'], reviewer_cache))
                info['patches'][attachment['id']].update(patch_analysis(data, [attachment['creator']], bugzilla_reviewers, utils.get_date_ymd(attachment['creation_time'])))
    if uplift_channel is not None:
        # Add uplift request
        info.update(uplift_info(bug, uplift_channel))
        'uplift_reviewer': None,
    app_flags = [
        flag
        for a in bug['attachments']
        for flag in a['flags']
        if flag['name'] == approval_flag
    ]
    uplift_reviewers = [flag['setter'] for flag in app_flags]
    # Add reviewer from last flag set
    if len(uplift_reviewers):
        info['uplift_reviewer'] = get_user_details(uplift_reviewers[-1])

        # Sometimes a patch is approved for uplift without a request.
        # assert info['response_delta'] >= timedelta(), "Delta between uplift request date and response should be at least 0"
        assert info['release_delta'] > timedelta(), "Delta between uplift request date and next release should be at least 0"
def get_patch_info(bugs, base_versions=None, extra=None,
                   channels=['release', 'aurora', 'beta', 'nightly']):