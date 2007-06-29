class Data:
    '''Data object that returns menu descriptions to be used in wxgui.py.
    Probably could be changed to XML or *.dtd file.'''
    def GetMenu(self):
	return [(
	("Files", (
	    ("Import", "Import files", "self.runMenuCmd", "r.in.gdal"),
	    ("Export", "Export files", "self.runMenuCmd", "r.out.gdal"),
	    ("","","", ""),
	    ("E&xit", "Exit from wxgui.py", "self.onCloseWindow", "")
	    )),
	("Config", (
	    ("Region", "Set region", "self.runMenuCmd", "g.region"),
	    ("","","", "")
	    )),
	("Raster", (
	    ("Develop map", (
		("Digitize raster", "Digitize raster", "self.runMenuCmd", "r.digit"),
		("","","", ""),
		("Compress/decompress raster file", "Compress/decompress raster file", "self.runMenuCmd", "r.compress"),
		("Manage boundary definition (WHICH COMMAND?)", "Manage boundary definition", "self.runMenuCmd", "r.region"),
		("Manage null values", "Manage null values", "self.runMenuCmd", "r.null"),
		("Manage timestamp for files", "Manage timestamp for files", "self.runMenuCmd", "r.timestamp"),
		("Quantization for floating-point maps", "Quantization for floating-point maps", "self.runMenuCmd", "r.quant"),
		("Resample (change resolution) using nearest neighbor method", "Resample (change resolution) using nearest neighbor method", "self.runMenuCmd", "r.resample"),
		("Resample (change resolution) using regularized spline tension", "Resample (change resolution) using regularized spline tension", "self.runMenuCmd", "r.resamp.rst"),
		("Support file creation and maintenance", "Support file creation and maintenance", "self.runMenuCmd", "r.support.sh"),
		("","","", ""),
		("Reproject raster from other location", "Reproject raster from other location", "self.runMenuCmd", "r.proj"),
		("Generate tiling for other projection", "Generate tiling for other projection", "self.runMenuCmd", "r.tileset"),
	    )),
	    ("Manage map colors", (
		("Set colors to predefined color tables", "Set colors to predefined color tables", "self.runMenuCmd", "r.colors"),
		("Set colors using color rules", "Set colors using color rules", "self.runMenuCmd", "r.colors.rules"),
		("","","", ""),
		("Blend 2 color maps to produce 3 RGB files", "Blend 2 color maps to produce 3 RGB files", "self.runMenuCmd", "r.blend"),
		("Create color image from RGB files", "Create color image from RGB files", "self.runMenuCmd", "r.composite"),
		("Create 3 RGB (red, green, blue) maps from 3 HIS (hue, intensity, saturation) maps", "Create 3 RGB (red, green, blue) maps from 3 HIS (hue, intensity, saturation) maps", "self.runMenuCmd", "r.his"),
	    )),
	    ("Query by coordinates", "Query by coordinates", "self.runMenuCmd", "r.what"),
	    ("","","", ""),
	    ("Create raster buffers", "Develop raster buffer", "self.runMenuCmd", "r.buffer"),
	    ("Create raster MASK", "Develop raster mask", "self.runMenuCmd", "r.mask"),
	    ("Locate closest points between areas in 2 raster maps", "r.distance", "self.runMenuCmd", "r.distance"),
	    ("Map calculator", "Map calculator", "self.runMenuCmd", "scripts/mapcalc_gparser.sh"),
	    ("Neighborhood analysis", (
		("Moving window analysis of raster cells", "Moving window analysis of raster cells", "self.runMenuCmd", "r.neighbors"),
		("Analyze vector points in neighborhood of raster cells", "Analyze vector points in neighborhood of raster cells", "self.runMenuCmd", "v.neighbors"),
	    )),
	    ("Overlay maps", (
		("Cross product", "Cross product", "self.runMenuCmd", "r.cross"),
		("Function of map series (time series)", "Function of map series (time series)", "self.runMenuCmd", "r.series"),
		("Patch maps", "Patch maps", "self.runMenuCmd", "r.patch"),
		("","","", ""),
		("Statistical calculations for cover map over base map", "Statistical calculations for cover map over base map", "self.runMenuCmd", "r.statistics"),
	    )),
	    ("Solar radiance and shadows", (
		("Solar irradiance and daily irradiation", "Solar irradiance and daily irradiation", "self.runMenuCmd", "r.sun"),
		("Shadow map for sun position or date/time", "Shadow map for sun position or date/time", "self.runMenuCmd", "r.sunmask"),
	    )),
	    ("Terrain analysis", (
		("Calculate cumulative movement costs between locales", "Calculate cumulative movement costs between locales", "self.runMenuCmd", "r.walk"),
		("cost surface", "cost surface", "self.runMenuCmd", "r.cost"),
		("Least cost route or flow", "Least cost route or flow", "self.runMenuCmd", "r.drain"),
		("Profile analysis", "Profile analysis", "self.runMenuCmd", "d.profile"),
		("Shaded relief map", "Shaded relief map", "self.runMenuCmd", "r.shaded.relief"),
		("Slope and aspect", "Slope and aspect", "self.runMenuCmd", "r.slope.aspect"),
		("Terrain parameters", "Terrain parameters", "self.runMenuCmd", "r.param.scale"),
		("Textural features", "Textural features", "self.runMenuCmd", "r.texture"),
		("Visibility/Line of sight", "Visibility/Line of sight", "self.runMenuCmd", "r.los"),
	    )),
	    ("Transform features", (
		("Clump small areas (statistics calculated by r.volume)", "Clump small areas (statistics calculated by r.volume)", "self.runMenuCmd", "r.clump"),
		("Grow areas", "Grow areas", "self.runMenuCmd", "r.grow"),
		("Thin linear features", "Thin linear features", "self.runMenuCmd", "r.thin"),
	    )),
	    ("","","", ""),
	    ("Hydrologic modeling", (
		("Carve stream channels into elevation map using vector streams map", "Carve stream channels into elevation map using vector streams map", "self.runMenuCmd", "r.carve"),
		("Depressionless elevation map and flowline map", "Depressionless elevation map and flowline map", "self.runMenuCmd", "r.fill.dir"),
		("Fill lake from seed point to specified level", "Fill lake from seed point to specified level", "self.runMenuCmd", "r.lake"),
		("Flow accumulation for massive grids (WHICH COMMAND?)", "Flow accumulation for massive grids", "self.runMenuCmd", "r.flow"),
		("Generate flow lines for raster map (WHICH COMMAND?)", "Generate flow lines for raster map", "self.runMenuCmd", "r.flow"),
		("SIMWE overland flow modeling (WHICH COMMAND?)", "SIMWE overland flow modeling", "self.runMenuCmd", "r.simwe"),
		("SIMWE sediment erosion, transport, deposition modeling (WHICH COMMAND?)", "SIMWE sediment erosion, transport, deposition modeling", "self.runMenuCmd", "r.simwe"),
		("Topographic index map", "Topographic index map", "self.runMenuCmd", "r.topidx"),
		("TOPMODEL simulation", "TOPMODEL simulation", "self.runMenuCmd", "r.topmodel"),
		("Watershed subbasins", "Watershed subbasins", "self.runMenuCmd", "r.basins.fill"),
		("Watershed analysis", "Watershed analysis", "self.runMenuCmd", "r.watershed"),
		("Watershed basin creation", "Watershed basin creation", "self.runMenuCmd", "r.water.outlet"),
	    )),
	    ("Landscape structure modeling", (
		("Set up sampling and analysis framework", "Set up sampling and analysis framework", "self.runMenuCmd", "r.le.setup"),
		("","","", ""),
		("Analyze landscape characteristics", "Analyze landscape characteristics", "self.runMenuCmd", "r.le.pixel"),
		("Analyze landscape patch characteristics", "Analyze landscape patch characteristics", "self.runMenuCmd", "r.le.patch"),
		("Output landscape patch information", "Output landscape patch information", "self.runMenuCmd", "r.le.trace"),
	    )),
	    ("Wildfire modeling", (
		("Generate rate of spread (ROS) maps", "Generate rate of spread (ROS) maps", "self.runMenuCmd", "r.ros"),
		("Generate least-cost spread paths", "Generate least-cost spread paths", "self.runMenuCmd", "r.spreadpath"),
		("Simulate anisotropic spread phenomena", "Simulate anisotropic spread phenomena", "self.runMenuCmd", "r.spread"),
	    )),
	    ("","","", ""),
	    ("Change category values and labels", (
		("Edit category values of individual cells for displayed raster map", "Edit category values of individual cells for displayed raster map", "self.runMenuCmd", "d.rast.edit"),
		("","","", ""),
		("Reclassify categories for areas of specified sizes", "Reclassify categories for areas of specified sizes", "self.runMenuCmd", "r.reclass.area"),
		("Reclassify categories using rules", "Reclassify categories using rules", "self.runMenuCmd", "r.reclass.rules"),
		("Reclassify categories using rules file", "Reclassify categories using rules file", "self.runMenuCmd", "r.reclass.file"),
		("","","", ""),
		("Recode categories using rules (create new map)", "Recode categories using rules (create new map)", "self.runMenuCmd", "r.recode.rules"),
		("Recode categories using rules file (create new map)", "Recode categories using rules file (create new map)", "self.runMenuCmd", "r.recode.file"),
		("","","", ""),
		("Rescale categories (create new map)", "Rescale categories (create new map)", "self.runMenuCmd", "r.rescale"),
		("Rescale categories with equalized histogram (create new map)", "Rescale categories with equalized histogram (create new map)", "self.runMenuCmd", "r.rescale.eq"),
	    )),
	    ("","","", ""),
	    ("Generate concentric circles around points", "Generate concentric circles around points", "self.runMenuCmd", "r.circle"),
	    ("Generate random raster cells", (
		("Generate random cells", "Generate random cells", "self.runMenuCmd", "r.random.cells"),
		("Generate random cells and vector points from raster map", "Generate random cells and vector points from raster map", "self.runMenuCmd", "r.random"),
	    )),
	    ("Generate surfaces", (
		("Generate density surface using moving Gaussian kernel", "Generate density surface using moving Gaussian kernel", "self.runMenuCmd", "v.kernel"),
		("Generate fractal surface", "Generate fractal surface", "self.runMenuCmd", "r.surf.fractal"),
		("Generate gaussian deviates surface", "Generate gaussian deviates surface", "self.runMenuCmd", "r.surf.gauss"),
		("Generate plane", "Generate plane", "self.runMenuCmd", "r.plane"),
		("Generate random deviates surface", "Generate random deviates surface", "self.runMenuCmd", "r.surf.random"),
		("Generate random surface with spatial dependence", "Generate random surface with spatial dependence", "self.runMenuCmd", "r.random.surface"),
	    )),
	    ("Generate vector contour lines", "Generate vector contour lines", "self.runMenuCmd", "r.contour"),
	    ("Interpolate surfaces", (
		("Bilinear interpolation from raster points", "Bilinear interpolation from raster points", "self.runMenuCmd", "r.bilinear"),
		("Inverse distance weighted interpolation from raster points", "Inverse distance weighted interpolation from raster points", "self.runMenuCmd", "r.surf.idw"),
		("Interpolation from raster contour", "Interpolation from raster contour", "self.runMenuCmd", "r.surf.contour"),
		("","","", ""),
		("Inverse distance weighted interpolation from vector points", "Inverse distance weighted interpolation from vector points", "self.runMenuCmd", "v.surf.idw"),
		("Regularized spline tension interpolation from vector points or contours (WHICH COMMAND ?)", "Regularized spline tension interpolation from vector points or contours", "self.runMenuCmd", "v.surf.rst"),
		("","","", ""),
		("Fill NULL cells by interpolation using regularized spline tension", "Fill NULL cells by interpolation using regularized spline tension", "self.runMenuCmd", "r.fillnulls"),
	    )),
	    ("","","", ""),
	    ("Report and statistics", (
		("Report basic file information", "Report basic file information", "self.runMenuCmd", "r.info"),
		("Report category labels and values", "Report category labels and values", "self.runMenuCmd", "r.cats"),
		("","","", ""),
		("General statistics", "General statistics", "self.runMenuCmd", "r.stats"),
		("Range of all category values", "Range of all category values", "self.runMenuCmd", "r.describe"),
		("Sum all cell category values", "Sum all cell category values", "self.runMenuCmd", "r.sum"),
		("Sum area by map and category", "Sum area by map and category", "self.runMenuCmd", "r.report"),
		("Summary statistics for clumped cells (work with r.clump)", "Summary statistics for clumped cells (work with r.clump)", "self.runMenuCmd", "r.volume"),
		("Total surface area corrected for topography", "Total surface area corrected for topography", "self.runMenuCmd", "r.surf.area"),
		("Univariate statistics", "Univariate statistics", "self.runMenuCmd", "r.univar"),
		("Univariate statistics (script version)", "Univariate statistics (script version)", "self.runMenuCmd", "r.univar.sh"),
		("","","", ""),
		("Sample values along transects", "Sample values along transects", "self.runMenuCmd", "r.profile"),
		("Sample values along transects (use azimuth, distance)", "Sample values along transects (use azimuth, distance)", "self.runMenuCmd", "r.transect"),
		("","","", ""),
		("Covariance/correlation", "Covariance/correlation", "self.runMenuCmd", "r.covar"),
		("Linear regression between 2 maps", "Linear regression between 2 maps", "self.runMenuCmd", "r.regression.line"),
		("Mutual category occurrences (coincidence)", "Mutual category occurrences (coincidence)", "self.runMenuCmd", "r.coin"),
	    )),
	    ("","","", "")
	    )),
	("Vector", (
	    ("Develop map", (
		("Digitize", "Digitize vector", "self.runMenuCmd", "v.digit"),
		("","","", ""),
		("Create/Rebuild topology", "Create/Rebuild topology", "self.runMenuCmd", "v.build"),
		("Clean vector files", "clean vector files", "self.runMenuCmd", "v.clean"),
		("","","", ""),
		("Break lines at intersections", "Break lines at intersections", "self.runMenuCmd", "v.topo.check"),
		("Build polylines from adjacent segments", "Build polylines from adjacent segments", "self.runMenuCmd", "v.build.polylines"),
		("Split polylines into segments", "Split polylines into segments", "self.runMenuCmd", "v.segment"),
		("Create lines parallel to existing lines", "Create lines parallel to existing lines", "self.runMenuCmd", "v.parallel"),
		("","","", ""),
		("Convert vector feature types", "Convert vector feature types", "self.runMenuCmd", "v.type"),
		("Convert 2D vector to 3D by sampling raster", "Convert 2D vector to 3D by sampling raster", "self.runMenuCmd", "v.drape"),
		("Extrude 2D vector into 3D vector", "Extrude 2D vector into 3D vector", "self.runMenuCmd", "v.extrude"),
		("","","", ""),
		("Create text label file for vector features", "Create text label file for vector features", "self.runMenuCmd", "v.label"),
		("","","", ""),
		("Reproject vector from other location", "Reproject vector from other location", "self.runMenuCmd", "v.proj"),
		("","","", "")
	    )),
	    ("","","", ""),
	    ("vector<->database connections", (
		("Create new vector as link to external OGR layer", "Create new vector as link to external OGR layer", "self.runMenuCmd", "v.external"),
		("Set database connection for vector attributes", "Set database connection for vector attributes", "self.runMenuCmd", "v.db.connect"),
	    )),
	    ("Query by attributes", "Query by attributes", "self.runMenuCmd", "v.extract"),
	    ("Query by coordinate(s)", "Query by coordinate(s)", "self.runMenuCmd", "v.what"),
	    ("Query by map features", "Query by map features", "self.runMenuCmd", "v.select"),
	    ("","","", ""),
	    ("Create vector buffers", "Create vector buffers", "self.runMenuCmd", "v.buffer"),
	    ("Linear referencing for vectors", (
		("Create linear reference system", "Create linear reference system", "self.runMenuCmd", "v.lrs.create"),
		("Create stationing from input lines, and linear reference system", "Create stationing from input lines, and linear reference system", "self.runMenuCmd", "v.lrs.label"),
		("Create points/segments from input lines, linear reference system and positions read from stdin", "Create points/segments from input lines, linear reference system and positions read from stdin", "self.runMenuCmd", "v.lrs.segment"),
		("Find line id and real km+offset for given points in vector map using linear reference system", "Find line id and real km+offset for given points in vector map using linear reference system", "self.runMenuCmd", "v.lrs.where"),
	    )),
	    ("Neighborhood analysis", (
		("Locate nearest feature to points or centroids", "Locate nearest feature to points or centroids", "self.runMenuCmd", "v.distance"),
		("Generate Thiessen polygons around points (Voronoi diagram)", "Generate Thiessen polygons around points (Voronoi diagram)", "self.runMenuCmd", "v.voronoi"),
		("Connect points to create Delaunay triangles", "Connect points to create Delaunay triangles", "self.runMenuCmd", "v.delaunay"),
	    )),
	    ("Network analysis", (
		("Allocate subnets", "Allocate subnets", "self.runMenuCmd", "v.net.alloc"),
		("Network maintenance", "Network maintenance", "self.runMenuCmd", "v.net"),
		("Shortest route", "Shortest route", "self.runMenuCmd", "v.net.path"),
		("Shortest route (visualization only)", "Shortest route (visualization only)", "self.runMenuCmd", "d.path"),
		("Split net to bands between cost isolines", "Split net to bands between cost isolines", "self.runMenuCmd", "v.net.iso"),
		("Steiner tree", "Steiner tree", "self.runMenuCmd", "v.net.steiner"),
		("Traveling salesman analysis", "Traveling salesman analysis", "self.runMenuCmd", "v.net.salesman"),
	    )),
	    ("Overlay maps", (
		("Overlay/combine 2 vector maps", "Overlay/combine 2 vector maps", "self.runMenuCmd", "v.overlay"),
		("Patch multiple maps (combine)", "Patch multiple maps (combine)", "self.runMenuCmd", "v.patch"),
	    )),
	    ("Generate area feature for extent of current region", "Generate area feature for extent of current region", "self.runMenuCmd", "v.in.region"),
	    ("Generate rectangular vector grid", "Generate rectangular vector grid", "self.runMenuCmd", "v.mkgrid"),
	    ("","","", ""),
	    ("Change attributes", (
		("Attach/delete, or report categories", "Attach/delete, or report categories", "self.runMenuCmd", "v.category"),
		("Reclassify features using rules file", "Reclassify features using rules file", "self.runMenuCmd", "v.reclass"),
	    )),
	    ("","","", ""),
	    ("Work with vector points", (
		("Generate points", (
		    ("Generate points from database", "Generate points from database", "self.runMenuCmd", "v.in.db"),
		    ("Generate random points", "Generate random points", "self.runMenuCmd", "v.random"),
		    ("Random location perturbations of points", "Random location perturbations of points", "self.runMenuCmd", "v.perturb"),
		)),
		("Generate areas from points", (
		    ("Generate convex hull for point set", "Generate convex hull for point set", "self.runMenuCmd", "v.hull"),
		    ("Generate Delaunay triangles for point set", "Generate Delaunay triangles for point set", "self.runMenuCmd", "v.delaunay"),
		    ("Generate Voronoi diagram/Thiessen polygons for point set", "Generate Voronoi diagram/Thiessen polygons for point set", "self.runMenuCmd", "v.voronoi"),
		)),
		("Sample raster maps", (
		    ("Calculate statistics for raster map overlain by vector map", "Calculate statistics for raster map overlain by vector map", "self.runMenuCmd", "v.rast.stats"),
		    ("Sample raster maps at point locations", "Sample raster maps at point locations", "self.runMenuCmd", "v.what.rast"),
		    ("Sample raster neighborhood around points", "Sample raster neighborhood around points", "self.runMenuCmd", "v.sample"),
		)),
		("Partition points into test/training sets for k-fold cross validation", "Partition points into test/training sets for k-fold cross validation", "self.runMenuCmd", "v.kcv"),
		("Transfer attribute data from queried vector map to points", "Transfer attribute data from queried vector map to points", "self.runMenuCmd", "v.what.vect"),
	    )),
	    ("","","", ""),
	    ("Reports and statistics", (
		("Basic information", "Basic information", "self.runMenuCmd", "v.info"),
		("Load vector attributes to database or create reports", "Load vector attributes to database or create reports", "self.runMenuCmd", "v.to.db"),
		("Report areas for vector attribute categories", "Report areas for vector attribute categories", "self.runMenuCmd", "v.report"),
		("Univariate statistics", "Univariate statistics", "self.runMenuCmd", "v.univar"),
		("","","", ""),
		("Test normality of point distribution", "Test normality of point distribution", "self.runMenuCmd", "v.normal"),
		("Calculate stats for raster map underlying vector objects", "Calculate stats for raster map underlying vector objects", "self.runMenuCmd", "v.rast.stats"),
		("Indices of point counts in quadrats", "Indices of point counts in quadrats", "self.runMenuCmd", "v.qcount"),
	    )),
	    ("","","", "")
	    )),
	("Image", (
	    ("Develop images and groups", (
		("Create/edit imagery group", "Create/edit imagery group", "self.runMenuCmd", "i.group"),
		("Target imagery group", "Target imagery group", "self.runMenuCmd", "i.target"),
		("","","", ""),
		("Mosaic up to 4 adjacent images", "Mosaic up to 4 adjacent images", "self.runMenuCmd", "i.image.mosaic"),
		)),
	    ("Manage image colors", (
		("Color balance and enhance color tables of multiband imagery for rgb display", "Color balance and enhance color tables of multiband imagery for rgb display", "self.runMenuCmd", "i.landsat.rgb"),
		("Transform HIS (Hue/Intensity/Saturation) color image to RGB (Red/Green/Blue)", "Transform HIS (Hue/Intensity/Saturation) color image to RGB (Red/Green/Blue)", "self.runMenuCmd", "i.his.rgb"),
		("Transform RGB (Red/Green/Blue) color image to HIS (Hue/Intensity/Saturation)", "Transform RGB (Red/Green/Blue) color image to HIS (Hue/Intensity/Saturation)", "self.runMenuCmd", "i.rgb.his"),
		)),
	    ("Rectify and georeference image group", (
		("Set ground control points (GCP's) from raster map or keyboard entry", "Set ground control points (GCP's) from raster map or keyboard entry", "self.runMenuCmd", "i.points"),
		("Set ground control points (GCP's) from vector map or keyboard entry", "Set ground control points (GCP's) from vector map or keyboard entry", "self.runMenuCmd", "i.vpoints"),
		("Affine and Polynomial rectification (rubber sheet)", "Affine and Polynomial rectification (rubber sheet)", "self.runMenuCmd", "i.rectify"),
		("Ortho Photo rectification", "Ortho Photo rectification", "self.runMenuCmd", "i.ortho.photo"),
		)),
	    ("","","", ""),
	    ("Classify image", (
		("Clustering input for unsupervised classification", "Clustering input for unsupervised classification", "self.runMenuCmd", "i.cluster"),
		("","","", ""),
		("Maximum likelihood Classification (MLC)", "Maximum likelihood Classification (MLC)", "self.runMenuCmd", "i.maxlik"),
		("Sequential maximum a posteriori classification (SMAP)", "Sequential maximum a posteriori classification (SMAP)", "self.runMenuCmd", "i.smap"),
		("","","", ""),
		("Interactive input for supervised classification", "Interactive input for supervised classification", "self.runMenuCmd", "i.class"),
		("Non-interactive input for supervised classification (MLC)", "Non-interactive input for supervised classification (MLC)", "self.runMenuCmd", "i.gensig"),
		("Non-interactive input for supervised classification (SMAP)", "Non-interactive input for supervised classification (SMAP)", "self.runMenuCmd", "i.gensigset"),
		)),
                ("Classify image (pr library)", (
                  ("subsets", "pr_subsets", "self.RunMenuCmd", "i.pr_subsets"),
                  ("training", "pr_training", "self.RunMenuCmd", "i.pr_training"),
                  ("classify", "pr_classify", "self.RunMenuCmd", "i.pr_classify"),
                  ("","","", ""),
                  ("features", "pr_features", "self.RunMenuCmd", "i.pr_features"),
                  ("features_additional", "pr_features_additional", "self.RunMenuCmd", "i.pr_features_additional"),
                  ("features_extract", "pr_features_extract", "self.RunMenuCmd", "i.pr_features_extract"),
                  ("features_selection", "pr_features_selection", "self.RunMenuCmd", "i.pr_features_selection"),
                  ("","","", ""),
                  ("model", "pr_model", "self.RunMenuCmd", "i.pr_model"),
                  ("sites_aggregate", "pr_sites_aggregate", "self.RunMenuCmd", "i.pr_sites_aggregate"),
                  ("blob", "pr_blob", "self.RunMenuCmd", "i.pr_blob"),
                  ("uxb", "pr_uxb", "self.RunMenuCmd", "i.pr_uxb"),
                  ("","","", ""),
                  ("statistics", "pr_statistics", "self.RunMenuCmd", "i.pr_statistics"),
                  )),
              ("","","", ""),
              ("RS Pre-Processing (DN->Rad->Ref)", (
                ("Landsat 7 ETM+", "Landsat 7 ETM+", "self.RunMenuCmd", "i.dn2ref.l7"),
                ("Landsat 7 ETM+ (from .met)", "Landsat 7 ETM+ (from .met)", "self.RunMenuCmd", "i.dn2full.l7"),
                ("Terra-Aster", "Terra-Aster", "self.RunMenuCmd", "i.dn2ref.ast"),
                ("","","", ""),
                ("Atmospheric correction", "Atmospheric correction", "self.RunMenuCmd", "i.atcorr"),
                ("Dehaze Landsat", "Dehaze Landsat", "self.RunMenuCmd", "i.landsat.dehaze"),
                )),
              ("RS Processing (Basic)", (
                ("Vegetation Index (Tasseled cap)", "Vegetation index (Tasseled cap)", "self.OnMenuCmd", "i.tasscap"),
                ("Vegetation Indices (13 types)", "Vegetation Indices (13 types)", "self.RunMenuCmd", "i.vi"),
                ("Vegetation Indices (13 types) cluster", "Vegetation Indices (13 types) cluster", "self.RunMenuCmd", "i.vi.mpi"),
                ("","","", ""),
                ("Albedo", "Albedo", "self.RunMenuCmd", "i.albedo"),
                ("Emissivity (generic from NDVI)", "Emissivity (generic from NDVI)", "self.RunMenuCmd", "i.emissivity"),
                ("","","", ""),
                ("Latitude map", "Latitude map", "self.RunMenuCmd", "i.latitude"),
                ("Sunshine hours (potential)", "Sunshine hours (potential)", "self.RunMenuCmd", "i.sunhours"), 
                ("Satellite overpass time", "Satellite overpass time", "self.RunMenuCmd", "i.sattime"),
                )),
              ("RS Processing (Advanced)", (
                ("ETo, ETP, ETa", (
                  ("Reference ET (Hargreaves)", "Reference ET (Hargreaves)", "self.RunMenuCmd", "r.evapo.MH"),
                  ("","","", ""),
                  ("Potential ET (Penman-Monteith)", "Potential ET (Penman-Monteith)", "self.OnMenuCmd", "r.evapo.PM"),
                  ("Potential ET (Prestley and Taylor)", "Potential ET (Prestley and Taylor)", "self.RunMenuCmd", "i.evapo.PT"),
                  ("Potential ET (Radiative)", "Potential ET (Radiative)", "self.RunMenuCmd", "i.evapo.potrad"),
                  ("Potential ET (Radiative) from L7DN (.met)", "Potential ET (Radiative) from L7DN (.met)", "self.RunMenuCmd", "i.dn2potrad.l7"),
                  ("","","", ""),
                  ("Actual ET (SEBAL)", "Actual ET (SEBAL)", "self.RunMenuCmd", "i.eb.eta"),
                  ("Actual ET (TSA)", "Actual ET (TSA) NOT WORKING YET", "self.RunMenuCmd", "i.evapo.TSA"),
                  )),
                ("Energy Balance", (
                  ("Surface roughness", "surface roughness", "self.RunMenuCmd", "i.eb.z0m"),
                  ("Delta T", "delta T", "self.RunMenuCmd", "i.eb.deltat"), 
                  ("Net radiation", "net radiation", "self.RunMenuCmd", "i.eb.netrad"),
                  ("","","", ""),
                  ("Displacement height", "Displacement height", "self.RunMenuCmd", "i.eb.disp"),
                  ("Monin-Obukov Length", "Monin-Obukov Length", "self.RunMenuCmd", "i.eb.molength"),
                  ("Psichrometric param. for heat", "psichrometric param. for heat", "self.RunMenuCmd", "i.eb.psi"),
                  ("Blending height wind speed", "blending height wind speed", "self.RunMenuCmd",  "i.eb.ublend"),
                  ("Nominal wind speed", "nominal wind speed", "self.RunMenuCmd", "i.eb.ustar"),
                  ("Aerod. resis. to heat transp.", "aerod. resis. to heat transp.", "self.RunMenuCmd", "i.eb.rah"),
                  ("","","", ""),
                  ("Soil heat flux", "soil heat flux", "self.RunMenuCmd", "i.eb.g0"),
                  ("Sensible heat flux", "sensible heat flux", "self.RunMenuCmd", "i.eb.h0"),
                  ("Sensible heat flux iteration (fixed delta T)", "sensible heat flux iteration (fixed delta T)", "self.RunMenuCmd", "i.eb.h_iter"),
                  ("","","", ""),
                  ("Evaporative fraction", "evaporative fraction", "self.RunMenuCmd", "i.eb.evapfr"),
                  )),
                ("","","", ""),
                ("Biomass growth", "Biomass growth", "self.RunMenuCmd", "i.biomass"),
                )),
              ("","","", ""),
	    ("Filter image", (
		("Zero edge crossing detection", "Zero edge crossing detection", "self.runMenuCmd", "i.zc"),
		("User defined matrix/convolving filter", "User defined matrix/convolving filter", "self.runMenuCmd", "r.mfilter"),
		)),
	    ("Spectral response", "Spectral response", "self.runMenuCmd", "i.spectral"),
	    ("Tasseled cap vegetation index", "Tasseled cap vegetation index", "self.runMenuCmd", "i.tasscap"),
	    ("Transform image", (
	        ("Brovey transformation and pan sharpening", "Brovey transformation and pan sharpening", "self.runMenuCmd", "i.fusion.brovey"),
                ("","","", ""),
		("Canonical component", "Canonical component", "self.runMenuCmd", "i.cca"),
		("Principal component", "Principal component", "self.runMenuCmd", "i.pca"),
		("Fast Fourier Transform", "Fast Fourier Transform", "self.runMenuCmd", "i.fft"),
		("Inverse Fast Fourier Transform", "Inverse Fast Fourier Transform", "self.runMenuCmd", "i.ifft"),
		)),
	    ("","","", ""),
	    ("Report and statistics", (
		("Report basic file information", "Report basic file information", "self.runMenuCmd", "r.info"),
		("Range of image values", "Range of image values", "self.runMenuCmd", "r.describe"),
		("","","", ""),
		("Bit pattern comparison for ID of low quality pixels", "Bit pattern comparison for ID of low quality pixels", "self.runMenuCmd", "r.bitpattern"),
		("Kappa classification accuracy assessment", "Kappa classification accuracy assessment", "self.runMenuCmd", "r.kappa"),
		("Optimum index factor for LandSat TM", "Optimum index factor for LandSat TM", "self.runMenuCmd", "i.oif"),
		)),
	    ("","","", "")
	    )),
	("Database", (
	    ("Query", "Query database", "self.Nomethod", ""),
	    ("","","", "")
	    )))]










