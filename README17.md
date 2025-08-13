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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1d3bba6-0681-387c-96c6-d76095eca214 | -7.06354 | -44.35839 | 2025-08-13 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a88fe23f-c17f-3c98-aacf-72dc796c66c7 | -12.5511 | -46.97837 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dc5b732-482e-3f18-adf8-a94a1a084fbb | -11.91087 | -52.53702 | 2025-08-13 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6823c2e8-b992-3fef-a654-7fd8f04ba726 | -10.01947 | -58.43788 | 2025-08-13 04:40:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d9d34213-76a5-326e-85d1-56fc46b87d23 | -7.07458 | -44.94107 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 347bd520-b305-3665-8d68-1ef2f9ca01ea | -10.37294 | -46.63569 | 2025-08-13 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb289b61-5267-3d35-ba53-2b9b9a21e371 | -7.25932 | -60.00517 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8fab459-e94f-378c-b838-7a433bb23846 | -12.63872 | -45.33373 | 2025-08-13 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f75476cf-221b-30bd-a7c0-10a5ced8b5b2 | -5.66797 | -51.3638 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2cc02fa-0e60-3ffa-a9be-95a363dbaf47 | -12.46451 | -46.96236 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16d7497c-9466-3c0d-a2c3-f73b47cdc2f4 | -10.97075 | -49.56942 | 2025-08-13 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc9c004f-51d1-3d68-b372-d25b85cbaf9b | -6.88285 | -59.1368 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 11a1af9a-fa21-3bda-b570-8b90ee8ea97a | -7.25364 | -60.00422 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c0052e8-d5ac-3e93-9fcd-7d85a27dcc29 | -8.56539 | -54.71616 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1096e5d8-5d4a-325b-8d48-893fc145f521 | -6.86669 | -59.15302 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b5dc88b6-1596-3d50-8946-eed3e6b1be8b | -5.84255 | -59.92468 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ed4f5f2-96fa-31ca-810e-2268aa365c46 | -9.18608 | -59.67027 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee7c146e-6d2e-300d-9ca4-ad5b42ee505e | -12.53093 | -46.98482 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f1382ed2-64d8-3d34-bfdd-728889352c5e | -12.5067 | -46.96405 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a2c35444-a930-3047-a4a9-93f25423508d | -10.2495 | -48.25915 | 2025-08-13 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 603bc98e-f19e-380b-8717-dcffcf8443a0 | -11.45747 | -47.32395 | 2025-08-13 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9b99bfe-d83f-3c1d-87e9-620a0cfd1a27 | -12.67274 | -46.96527 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ff470b7-0c1b-3f54-86d3-6c314704a469 | -7.48726 | -48.37876 | 2025-08-13 04:40:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db5769b6-d2d8-371a-b5ad-77353f28bc5e | -12.52843 | -46.97493 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0e2a8649-8de7-3272-9b4c-d7db6fac763e | -6.87209 | -59.1348 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| db7297dd-5a83-39f4-98b1-313f7246fe4e | -11.7615 | -48.18951 | 2025-08-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f9c35cd5-798d-3b33-ae8b-812949658c2f | -5.66839 | -51.36333 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 870efca9-f102-3009-8ce4-47b4e7264149 | -7.24742 | -59.99175 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 495d164a-9b96-3dde-adc4-4850f9f93484 | -9.65488 | -48.15652 | 2025-08-13 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10807703-0c21-3d9e-94de-29b107833f04 | -8.56115 | -54.66968 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acf8e6cd-b03e-3443-b2ea-bb0113fc2a6c | -12.55084 | -47.03563 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29d40917-6e7a-3ab6-8911-ac5cb8e5c0e3 | -6.87376 | -59.15639 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.1 |
| e24fd610-d595-3781-8743-e2397a5bcceb | -12.50293 | -46.96346 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 381585c4-0ba6-3303-9bfb-fb133c3a7518 | -6.88347 | -59.13337 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 6c52236c-1056-3c42-afbf-d4786a00bf20 | -7.09705 | -60.03407 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 641adf50-bae9-3ef2-9098-a3a96833b402 | -12.30387 | -50.00526 | 2025-08-13 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 711d5b03-ac19-35c8-a5d7-21c933df1cc1 | -12.58585 | -47.05991 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d61f1d1-a503-3655-bd6a-82ea7c8a500b | -9.8482 | -47.82313 | 2025-08-13 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f0740c4-2182-34e9-92bb-50ad4df12937 | -6.61668 | -43.88119 | 2025-08-13 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e72f931f-2344-39db-989f-6b1d903ab9b3 | -9.31003 | -48.92737 | 2025-08-13 04:40:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cfcc285-2085-3911-a741-6d51d2416e4e | -9.06112 | -60.66018 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7cf980ab-8c9c-3c03-ac4b-f4c8375ec4f4 | -8.57095 | -54.70689 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff176925-b42a-33c7-bebd-9955560d41d1 | -6.09187 | -59.93497 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1fe6cf40-6f55-3f89-a9d2-0926546559e7 | -10.75669 | -48.77883 | 2025-08-13 04:40:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c36b2cb2-2452-34fe-8b72-76ae98a0ccf6 | -7.25512 | -59.99617 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcfe65f3-5c80-3520-a9be-0c451b96b726 | -12.57877 | -46.97361 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8211677c-63b5-373e-ba28-617504f94292 | -6.88949 | -59.13082 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| ce65a450-f3d5-343a-a030-e185d59b2b33 | -7.26319 | -60.63494 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b437605b-c661-3b55-8281-31d6bc1f1ef2 | -12.47206 | -46.9635 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bd31842-b092-3d54-b5f7-af6317cdc405 | -12.69158 | -46.96874 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16545a78-fcd7-3124-87a0-7132ed983e7c | -10.01757 | -58.43508 | 2025-08-13 04:40:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 577ca238-26dd-3b6d-a75a-0761ee2fa9d2 | -5.85274 | -59.90128 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8f9027b-42f3-321b-a413-7a4f91bd505e | -7.8024 | -48.38213 | 2025-08-13 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df7514c9-c489-341a-afd8-ce319b133443 | -12.52114 | -46.97101 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 702a2955-5ad5-3f91-a325-b8ed73ccdf2b | -12.58272 | -47.05489 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a24aca8-e20b-3fa1-b5c8-0745d06ea0f3 | -9.94922 | -48.34364 | 2025-08-13 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84751685-18bd-3901-abb4-f0f059e637cf | -9.6589 | -48.15327 | 2025-08-13 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac0a9735-99d8-3da4-9e50-4b16a3e44d8c | -6.89241 | -59.14557 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 2b543945-418e-3eb9-9b17-3f3f7c781173 | -6.89302 | -59.14215 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 9cf85aac-89a7-3402-9fdb-d6b4a72b6a3f | -6.90503 | -59.13716 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 0ad42408-2f99-3185-aa22-bacaf51d6e99 | -7.25016 | -59.99136 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e537748-78ea-3255-960f-9298d0cc6273 | -9.2952 | -50.27322 | 2025-08-13 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5628ec53-e92f-314d-a1bf-26346a21e222 | -12.54355 | -46.97719 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b935a750-748e-3fe9-aacd-df6c7c5450b4 | -8.79499 | -49.88387 | 2025-08-13 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77d7516f-5bff-3cd0-8749-5ba5930e7b5e | -11.45632 | -47.30597 | 2025-08-13 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f903ce9-db3c-38de-b5fe-f1ee7f091c9c | -6.87685 | -59.13921 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 42c82568-6360-32fc-87bb-5b30a5c5acbd | -11.76443 | -48.19408 | 2025-08-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 27f8859b-386c-3cda-a008-90804f6e32c0 | -10.34535 | -50.82113 | 2025-08-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e21e9bb9-689f-3b1b-aeba-595e4abd046d | -5.66738 | -51.36753 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21547261-0e7d-35c1-8433-46e9c2107ecb | -7.14066 | -60.12774 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d21f0d43-1743-3478-804f-9b2a063fabe0 | -12.58307 | -46.9979 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22d584b7-fc80-3be9-96a3-8caa17c59269 | -5.73165 | -51.68817 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c2afe87-c502-3e7e-9496-488ddc9a5164 | -6.87439 | -59.1529 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 3a984fd5-a5d4-3e1f-9151-fad15224a41d | -6.87916 | -59.15735 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4a618db2-3b95-32be-a4dd-02c87b5b3b9f | -5.84847 | -59.92264 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80dcdf61-2fde-3ba2-abde-6301cfbc4452 | -6.97072 | -59.28029 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57572c97-5413-3ea2-9d8e-d11013cefdf0 | -9.65947 | -48.14942 | 2025-08-13 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67b8a9a7-00ba-36f6-9f1d-46f2992265ae | -10.96795 | -49.56532 | 2025-08-13 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ebfaa64-97c0-3c80-9db9-651be26b6ec6 | -12.52424 | -46.97626 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ecca8675-e658-331a-828d-983761ef2a3e | -6.86729 | -59.14953 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2fda7737-a44e-3afe-9362-f0262c0b1be3 | -10.7465 | -48.18472 | 2025-08-13 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3362396c-c148-391d-9191-85cf52af89ba | -8.56954 | -54.69136 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c8fe86b-f31d-37c0-8c41-8e45ecd6939b | -7.13492 | -60.12679 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 033d3fa1-8658-32f1-962b-0df9d398fdee | -6.89363 | -59.13874 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| c468c5bc-f2af-3ac9-99c2-ebd4e7bfa35e | -11.9041 | -52.53588 | 2025-08-13 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b58fdca-ae21-3c1c-be22-3f620d8fcb9d | -7.46408 | -59.88765 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0dffe24d-5d0b-3c8f-80fa-80a2b26a4c87 | -10.3448 | -50.82463 | 2025-08-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27cd7f7a-d03f-3a8e-be2d-21c414a454a1 | -8.12195 | -55.56616 | 2025-08-13 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6ff80ce7-130a-3a39-8ba6-8ed663c756d9 | -9.77519 | -46.68206 | 2025-08-13 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc469597-6089-38e8-9235-5bbd81d9a92e | -12.30279 | -50.01242 | 2025-08-13 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 377dbef8-70e8-3311-be90-9f2f3140a80a | -8.56871 | -54.6963 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a827ff97-bd84-368e-98c5-c9a7e905098b | -12.46073 | -46.96179 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ef1020d-dbee-32e8-adb7-086625d5eab0 | -6.41645 | -53.37688 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af77b8e5-4d77-3c1e-a8a3-d8abcf5202b9 | -11.71186 | -51.87713 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53fcbfce-f248-374b-be4a-9dfe658a2482 | -11.76794 | -48.19462 | 2025-08-13 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d84b489-7093-38d2-8fd0-dced4aab03ad | -12.46828 | -46.96293 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ede6019-5a11-3077-b963-9d1fb91647bd | -9.71475 | -49.4756 | 2025-08-13 04:40:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b415bc5-31b7-3599-ac33-168a1e07f920 | -9.82932 | -60.75977 | 2025-08-13 04:40:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f166ce1-4cf3-3e55-ad4c-6345eb32f751 | -10.1832 | -49.50193 | 2025-08-13 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e82b5bc-0d4c-36a1-908b-443c913a9647 | -7.06339 | -59.21019 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README18.md)
