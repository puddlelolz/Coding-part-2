extends RigidBody2D


func _input(event):
	if event.is_action_pressed("ui_accept"):
		apply_central_impulse(Vector2(0,-500))
