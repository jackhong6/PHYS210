function in_set = in_mandelbrot(c)

z = 0;
k = 1;
while k < 1e10
    z = z^2 + c;
    k = k+1;
    if abs(z) > 2
        in_set = false;
        return
    end
end

in_set = true;

end