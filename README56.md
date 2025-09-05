# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0ed89d7-d5e0-3bba-9a34-b445807f30b6 | -18.62047 | -44.26601 | 2025-09-05 04:59:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8aef8e7-1f45-3dc9-a870-61b4e6da8a6f | -16.3134 | -52.94957 | 2025-09-05 04:59:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0eccd9cf-08d8-3a28-a690-0798c8b19dad | -16.32438 | -52.9515 | 2025-09-05 04:59:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1ff8b1f-b8ac-3307-889f-f06f0422e961 | -18.6847 | -51.80502 | 2025-09-05 04:59:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6436c8fa-3830-3d37-a27e-ffd94605b107 | -15.99351 | -55.94712 | 2025-09-05 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d8e8558d-715f-3e0c-91f8-a1ff6c34f98d | -19.68357 | -54.81213 | 2025-09-05 04:59:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d49da0d0-c7aa-3df7-bb50-59bbc042b432 | -20.24148 | -51.30075 | 2025-09-05 04:59:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 5d7a9d1f-55e7-3047-ab43-2eb3deb32e7c | -18.95553 | -44.68599 | 2025-09-05 04:59:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74b553c4-2f26-3718-923e-7c02c7947475 | -16.30667 | -52.94398 | 2025-09-05 04:59:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ded54a3-0154-3e4b-a9b0-07b3fc3172db | -15.84664 | -56.23538 | 2025-09-05 04:59:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fed94b44-f320-3036-9540-959349860ddd | -15.98851 | -55.95736 | 2025-09-05 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5a91fabe-427d-30e1-ac53-5abc74cea997 | -17.66373 | -52.28194 | 2025-09-05 04:59:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34892f17-77b2-39f4-9a84-f9e20f15ea51 | -18.87023 | -46.37381 | 2025-09-05 04:59:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b472b82d-7d81-3180-a96a-7a79a69ef776 | -15.99236 | -55.97644 | 2025-09-05 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 71c37caf-c24d-3bab-9a02-2c9bb2d2d4a3 | -18.95659 | -44.68712 | 2025-09-05 04:59:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c792db82-6c5c-3129-b8c7-7e3469ac26aa | -17.53427 | -46.60736 | 2025-09-05 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab484cd8-7677-3b21-a52f-367da73b79c2 | -20.24524 | -51.30545 | 2025-09-05 04:59:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| f5a02574-7ac3-320f-b504-39c4074b215b | -18.9295 | -48.35493 | 2025-09-05 04:59:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c0f859e-252e-3317-9eca-d57ad2dad97a | -19.68371 | -54.80509 | 2025-09-05 04:59:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d043c48f-68f7-3874-9a3a-28addfa05039 | -15.98904 | -55.97589 | 2025-09-05 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| adf9ecd6-7dd8-3654-b984-f8c4f9ccb4bf | -18.73703 | -46.88863 | 2025-09-05 04:59:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4ec0f1e2-f5de-3169-93c1-e89d58e1f2a2 | -20.24096 | -51.30493 | 2025-09-05 04:59:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 681e7e39-e3cf-3e40-92ff-1a27bf14c9a4 | -18.73337 | -46.88567 | 2025-09-05 04:59:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77db11d2-5da7-3dd7-ac46-7f69c563ae82 | -16.32504 | -52.94687 | 2025-09-05 04:59:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| afdfbbee-3bbb-3e72-84d0-8951cfbb644a | -18.95706 | -44.68184 | 2025-09-05 04:59:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3c79930-3ff8-3251-936e-c263056b9a91 | -16.59777 | -50.82791 | 2025-09-05 04:59:00 | NOAA-20 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4213ccc-b9da-39bf-893a-70cb9209f682 | -18.73296 | -46.88947 | 2025-09-05 04:59:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b991cf1-95ab-321e-859d-06b7744519d8 | -17.66307 | -52.28697 | 2025-09-05 04:59:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09326cb7-88e1-36a9-8973-5b437c57404c | -18.73142 | -46.88823 | 2025-09-05 04:59:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3730802-8ba0-3ace-8e85-f021d9e4af72 | -15.96012 | -54.92739 | 2025-09-05 04:59:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d9bfc2c5-a280-3292-954a-4475b45d894b | -18.46039 | -53.03839 | 2025-09-05 04:59:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0d0eec86-6b01-3723-b617-dd03367d0cdf | -18.7318 | -46.88447 | 2025-09-05 04:59:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83e1635c-4e05-37bd-82ea-1200afe2e45f | -16.55587 | -55.13125 | 2025-09-05 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b742350c-424f-38d2-bcd9-a2e6c7997fde | -17.53385 | -46.61126 | 2025-09-05 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d634ff97-b26c-3466-98c8-2c1504193cac | -18.87001 | -46.37033 | 2025-09-05 04:59:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4b40225-eedc-3565-9218-a22ecb7000fc | -16.55982 | -55.12799 | 2025-09-05 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 92e35a6c-b66e-3ff3-af54-818c6a2fdc0a | -16.53671 | -55.09765 | 2025-09-05 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fd1bb01b-ae2d-3be3-89ed-45222794980d | -15.99239 | -55.95432 | 2025-09-05 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 22836fe1-59a4-3df9-b5c7-acd08ff215a9 | -15.9918 | -55.98004 | 2025-09-05 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9d0b8700-2562-37c8-ad51-9320b7d62ef1 | -17.53303 | -46.61903 | 2025-09-05 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0856346f-5eb8-3f10-a3df-bea62e8e589f | -16.32375 | -52.95598 | 2025-09-05 04:59:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5dcabb6e-857a-318a-bf03-d465ffb2c000 | -16.4471 | -51.06544 | 2025-09-05 04:59:00 | NOAA-20 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcf3b455-6519-3e00-8b93-803db9f9107c | -18.86957 | -46.37459 | 2025-09-05 04:59:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c76b5a1c-efdf-3377-9eed-49cf5da75561 | -16.31036 | -52.94444 | 2025-09-05 04:59:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2353215e-78be-31bc-b382-bb880a460f76 | -16.30541 | -52.95304 | 2025-09-05 04:59:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96ba54bd-198b-36f3-a07c-793b7f5b4aa2 | -20.23721 | -51.3002 | 2025-09-05 04:59:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 647b3185-2f0e-3ce8-bc38-ea8d75708fc5 | -18.46103 | -53.03368 | 2025-09-05 04:59:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6d138319-1617-31bd-bd15-be7fe20e4648 | -19.68765 | -54.80856 | 2025-09-05 04:59:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11c53b76-6578-3636-9d4a-0b3e9f9661af | -16.31705 | -52.95026 | 2025-09-05 04:59:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07f79744-771c-3448-ab96-a3e9e1bc231e | -17.53344 | -46.61515 | 2025-09-05 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18028f0e-5f56-35ba-ae89-c6e0ac7e25f7 | -19.67962 | -54.80865 | 2025-09-05 04:59:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b3e2e0bf-36d9-3328-a55d-7ec04579836e | -16.30972 | -52.94902 | 2025-09-05 04:59:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb0c4dc8-b8fb-37f0-b0fd-c18755895d10 | -18.53924 | -46.6919 | 2025-09-05 04:59:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af269f55-3db9-3a35-a1d3-0e891d0cffa4 | -20.5244 | -46.11341 | 2025-09-05 04:59:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e088a37a-d14f-34ae-b074-e02726bd0abc | -15.99295 | -55.95071 | 2025-09-05 04:59:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 112ca956-f3ae-35a7-acb5-ec7a208abba3 | -16.31404 | -52.94499 | 2025-09-05 04:59:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c895a904-c3b8-3070-ae30-8f3496c7e3bf | -20.24472 | -51.30959 | 2025-09-05 04:59:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 33487732-64e3-304d-b6ad-54ca9a4f4ea3 | -14.56711 | -48.08373 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4efab10b-562f-3924-98ba-b1c772684213 | -14.99732 | -50.04071 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c5cc9b8-8f18-3945-944e-2a16696d4f42 | -14.55445 | -48.08655 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b88a9b92-845d-3ed0-ac90-727e3fa53691 | -14.55221 | -48.04191 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8063329-678e-3917-908b-7f4228642ead | -15.85143 | -52.30408 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bab4b23-b4b9-3366-85f9-f6275f41c98c | -15.02483 | -48.12223 | 2025-09-05 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43887302-e3e9-3198-afad-0cc0c00a7c2a | -13.11456 | -57.11343 | 2025-09-05 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2f57824-452a-3aa1-8679-4421334abd27 | -15.14207 | -52.38268 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fff6b03e-ddd4-3030-9ef2-58a30945ce2c | -15.71509 | -46.23309 | 2025-09-05 04:59:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ccb735c-75df-37a9-ac88-b6bf54031310 | -12.35036 | -63.64487 | 2025-09-05 04:59:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b7db8558-9d13-3075-ba24-9040371f6a72 | -15.71741 | -46.22968 | 2025-09-05 04:59:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5591d6bc-af48-3442-969d-25376473fa6b | -15.84766 | -52.30338 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ca8a4f0-fb4a-31e4-9604-9bbd3a6be1ff | -15.61651 | -52.89846 | 2025-09-05 04:59:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cc80eae9-222c-3d77-88f4-1bf1a5c6106d | -15.71697 | -46.23357 | 2025-09-05 04:59:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2cef9f9-6d91-3f81-8799-f96447df36f9 | -15.54596 | -48.39517 | 2025-09-05 04:59:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94bc03a9-8445-3170-ad01-aac192948e1e | -15.16679 | -52.39644 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cffb6d39-4255-3a98-adbe-3e00dd46335a | -15.75765 | -53.63985 | 2025-09-05 04:59:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4befaec1-4780-3271-9c15-a26e348898e3 | -15.57165 | -54.29827 | 2025-09-05 04:59:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1400fc3f-f757-3b6b-bd55-254e32b50b08 | -15.13979 | -52.34484 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5023ee25-5450-3e62-8a77-60e9a21ffd55 | -15.19762 | -52.37656 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 517f3702-fb62-3b9f-97a1-043f746bbc90 | -15.62872 | -52.89147 | 2025-09-05 04:59:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9d531ba-9d8a-3303-937a-ed69963e4b09 | -13.10724 | -57.11596 | 2025-09-05 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a07a985-2274-3f66-8429-91b259a40c74 | -14.54196 | -53.13966 | 2025-09-05 04:59:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41d4d849-87de-3816-9116-f81f9c4d3d84 | -15.14643 | -52.37881 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| db96b154-c4a8-3d80-ac2f-b9ccc8afe7cc | -15.45502 | -53.03675 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d96d574-f081-3528-9667-a0909b8b0c6e | -15.02909 | -48.12822 | 2025-09-05 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73db5e44-4d33-3f7c-bd33-8299bf3aeb0f | -15.54332 | -48.4166 | 2025-09-05 04:59:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c80ce03c-2b4b-33ec-b69a-3edc8e63825d | -15.1684 | -52.39483 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29b5aa1b-9732-3453-9852-eb95e4032835 | -14.98007 | -50.07217 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd9a8072-4db5-34ae-8fd6-4b20fd0ddcf6 | -15.54529 | -48.40062 | 2025-09-05 04:59:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de963e79-5f52-3b86-a0e9-34cf949923db | -15.05734 | -50.06902 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da331f81-71f6-3cd4-ad7b-599321ed1b43 | -15.06113 | -50.0737 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bab53c9b-4656-36ee-8c6c-2b5bf3df62aa | -15.19893 | -52.36713 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 576bab2b-2823-3dff-b009-3a36228000d9 | -13.80564 | -56.57689 | 2025-09-05 04:59:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 643657d5-b1ef-3edf-bda8-7967daffba7e | -14.58336 | -48.03182 | 2025-09-05 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 000a4795-d00b-3817-ba19-e215ff5284ed | -15.71551 | -46.2292 | 2025-09-05 04:59:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 260465a8-cb95-3d8a-8cd2-f723b06dcc80 | -15.85262 | -52.29536 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2add8df1-5dfc-3377-987a-2ed6a5b30911 | -15.85709 | -52.29097 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 028274cc-3ac6-318b-a0c7-1e4bd04dcca1 | -15.07121 | -50.0635 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf543622-69f2-3f85-a713-a2edbc426948 | -16.29518 | -45.69088 | 2025-09-05 04:59:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 020071b1-df68-3477-a759-ec215260c08e | -15.54174 | -48.38929 | 2025-09-05 04:59:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0dde3b60-ab8d-3485-a2db-abe0d595eefb | -14.99525 | -50.09015 | 2025-09-05 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0ad3c9f-0d5b-3c61-9fba-0010ed090a4b | -15.22203 | -52.36583 | 2025-09-05 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README57.md)
