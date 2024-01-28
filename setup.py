from distutils.core import Extension, setup


def main():
    setup(
        name="myadd",
        version="1.0.0",
        description="Python interface for the myadd C library function",
        author="Nadiah",
        author_email="nadiah@nadiah.org",
        ext_modules=[
            Extension(
                "myadd",
                sources=["myadd.cpp"],
                language="c++",
                extra_compile_args=["-std=c++20", "-g0"],
            )
        ],
    )


if __name__ == "__main__":
    main()
