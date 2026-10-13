"""Axis-aligned bounding-box checks; overlap is not evidence of shared ink."""

def bbox_area(box: tuple[float, float, float, float]) -> float:
    x1, y1, x2, y2 = map(float, box)
    if not (x1 < x2 and y1 < y2):
        raise ValueError(f'Invalid bounding box: {box}')
    return (x2 - x1) * (y2 - y1)


def bbox_intersection(a: tuple, b: tuple) -> float:
    bbox_area(a); bbox_area(b)
    x1 = max(a[0], b[0]); y1 = max(a[1], b[1])
    x2 = min(a[2], b[2]); y2 = min(a[3], b[3])
    return max(0.0, x2 - x1) * max(0.0, y2 - y1)


def intersection_over_union(a: tuple, b: tuple) -> float:
    overlap = bbox_intersection(a, b)
    return overlap / (bbox_area(a) + bbox_area(b) - overlap)
