extends Camera2D

@export var scroll_speed: float = 200.0

func _process(delta: float) -> void:
	# Moves the camera downwards continuously
	position.y += scroll_speed * delta
