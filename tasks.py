from invoke import task


@task
def lint(ctx):
    ctx.run("pylint forty_two")
