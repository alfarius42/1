from facefusion.process_manager import set_process_state, is_processing, is_stopping, is_pending, start, stop, pause


def test_start() -> None:
	set_process_state('pending')
	start()

	assert is_processing()


def test_stop() -> None:
	set_process_state('processing')
	stop()

	assert is_stopping()


def test_pause() -> None:
	set_process_state('processing')
	pause()

	assert is_pending()
