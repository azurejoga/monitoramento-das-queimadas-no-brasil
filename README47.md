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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ef95db8-0ede-3c4f-b46b-29d96ea3ce19 | -13.03485 | -45.19141 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d7197913-9d0e-3161-bd6c-643019b4809d | -10.73774 | -48.25008 | 2025-08-22 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ac295785-b293-39ef-a8c9-90f08be0aa0f | -9.21606 | -59.46738 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdfc3e24-8df4-3aa1-9048-7bf7ec47403f | -13.03631 | -45.20186 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5a64594c-176f-3b12-a28c-7686b90c2dfb | -7.62485 | -69.94384 | 2025-08-22 05:12:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fda4b0b8-6a19-3d7e-83c5-732ea5ca2a06 | -9.2128 | -59.44476 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85cdfb2f-4fc4-34ab-b0e2-134f6051b67b | -8.85103 | -52.03782 | 2025-08-22 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b877fb21-af56-34d2-b6c8-760f06389880 | -9.52884 | -60.55691 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ceb00dd6-8ce2-3f4d-97f2-c9de2f101ccb | -6.68545 | -58.86317 | 2025-08-22 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7194300-88cb-3694-9755-4d32c0d7c674 | -7.09145 | -63.08522 | 2025-08-22 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2da8c59b-6b57-31e9-85c4-ae2db4fce086 | -11.3214 | -55.22354 | 2025-08-22 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 242501b7-cf6d-3f09-affd-e6cce35cfd7f | -9.20878 | -59.46988 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81d0c5cf-09bd-3829-ac6a-cacbddae1725 | -12.99299 | -56.88955 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 375080e0-cd94-3338-8168-a024e7b2b6d3 | -8.90725 | -47.33601 | 2025-08-22 05:12:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69b20124-b9b4-3116-8f27-d0443a814ff6 | -8.88502 | -62.43106 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c82808e-2368-3a09-a3ce-470c94425c3e | -6.87516 | -59.82529 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1561bb3e-991a-3df1-8b6b-8447e4d094b0 | -13.36429 | -46.26993 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dec03e51-b8a3-3936-8740-aa002b22f081 | -9.15706 | -59.59837 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 86dfb50e-3932-3634-a3ae-a052ea6cf25d | -7.62501 | -56.75264 | 2025-08-22 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b62674d-6af7-3845-acba-f318804a53a1 | -9.13982 | -46.3831 | 2025-08-22 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec30d827-e559-3f58-ba23-4c695cae60a9 | -6.89932 | -59.89545 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f1f3d37-ba88-3aeb-8233-622ae00cbead | -9.16379 | -59.59945 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c45715c8-8a76-3b8d-9e6a-c4b4c43500df | -12.99016 | -45.23165 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1562648a-306c-39b8-971a-ba40e5b31b50 | -8.71486 | -69.45905 | 2025-08-22 05:12:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e41b06da-7760-3363-9056-57cc4d5a9893 | -11.7307 | -49.10514 | 2025-08-22 05:12:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5406741d-66d9-3c4d-bd8b-1e8c21312f13 | -7.45698 | -59.9444 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ba5ec5a-a9af-363f-bf19-c10d719bb562 | -8.6215 | -62.61192 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 585ac6e4-952d-3d6c-95a6-c7a8058d75d0 | -9.9019 | -60.28947 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d14cdffd-f9a4-3454-af61-328703c3f415 | -9.13919 | -46.38819 | 2025-08-22 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce998b22-c69d-34de-9599-b49496430dd5 | -10.4607 | -59.13033 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b91289c2-3f86-35d5-80e9-f7171f3dfd79 | -12.97862 | -56.89133 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c1432bb-9b18-38b6-b10c-32e9d3ef2300 | -9.23161 | -59.76744 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74b62657-1aa6-3f70-a310-e74d3a9851c4 | -7.5884 | -63.43499 | 2025-08-22 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cf1f4e9e-2ca4-3669-b5e5-f593ae127377 | -6.89993 | -59.89164 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bb283a3-0db8-3292-a671-66969a05d337 | -9.1805 | -59.62442 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6f8970f-c824-3a78-a292-2d5d4260fb20 | -10.73159 | -48.25273 | 2025-08-22 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8bc26e09-c08c-37a0-bca8-cbc69ba8a760 | -13.14442 | -46.90174 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4393632c-9eec-3afa-a448-7c232983ca0f | -12.99456 | -45.23606 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8ea3b987-680f-369b-a290-fb9c2f468dbf | -9.52662 | -60.54865 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 960df09d-919b-3592-a05d-73ad7ac8147b | -9.31752 | -57.0177 | 2025-08-22 05:12:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 69bfa91b-50bf-368e-a70e-0cb966435d1f | -12.49751 | -53.8117 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 363349dc-79ad-3c15-a28f-cc50e8e8c46e | -12.95781 | -46.25938 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87c180c2-89d4-3cc6-9d3c-10db146f45ca | -7.84477 | -61.72174 | 2025-08-22 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84bd2ae0-d1f0-3294-85a6-0e9235f76c75 | -9.887 | -60.29475 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d20aaad7-399d-3e6c-b873-b15690fef02c | -10.2884 | -46.78086 | 2025-08-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c3b30f18-f8c2-3072-a091-7e9164663591 | -9.50799 | -60.51005 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81592b5e-63f2-3f3b-8d0d-4a96ec80d5d4 | -9.52156 | -60.53598 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d836e680-ee82-3149-81b2-a2a20fd58d1e | -6.63093 | -58.41338 | 2025-08-22 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3da422ca-bda1-3f45-b4bb-87b6d4318467 | -9.5165 | -60.52329 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 338a9f02-74e9-33c6-87af-166bf073118f | -9.65467 | -59.64215 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 417fa89f-4014-32dc-a599-ee2aa7429311 | -9.19536 | -65.66426 | 2025-08-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 777d397f-a915-3c0c-aaa6-e896ea768465 | -12.98495 | -56.89621 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62eb2164-404e-34bb-886a-f68f5b119259 | -7.29982 | -59.6317 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cc24a69-8bb2-3526-b915-97cd091e5108 | -9.20637 | -60.93617 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddf23195-dcaa-3f23-a49d-1235d18ec7aa | -10.45949 | -48.80828 | 2025-08-22 05:12:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a795c66-926e-3cbd-9b39-fbae5004af3c | -13.03341 | -45.20554 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0a476dfd-4a6e-37b5-8754-a266c141436d | -11.3314 | -48.33259 | 2025-08-22 05:12:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| da75e47f-acf7-3406-947a-60ddee1d7ff4 | -10.86312 | -50.82805 | 2025-08-22 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7a434211-83e2-3dcd-b677-ef028a7ca0f2 | -7.93499 | -63.04391 | 2025-08-22 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61750a8e-3a20-3c73-9cb2-1e50c6528e60 | -8.54642 | -66.94901 | 2025-08-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 328e4084-cce3-36ac-a43b-7cd5f4fff3c4 | -8.60509 | -62.61422 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a34cbb32-a073-3d00-8c50-8b1915aef206 | -9.15984 | -59.60253 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1bc925e-14b5-3273-9e74-d5b11ac4cc18 | -13.03708 | -45.1948 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e934bca8-4d5d-3d6c-a810-6c814c585180 | -9.21359 | -60.78209 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab001a0b-d19b-313b-9272-8b12a4f3605b | -13.03299 | -45.16617 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b9de8145-cf4d-3af3-941e-bf581671b2a7 | -10.86298 | -50.8246 | 2025-08-22 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 620e442a-c277-36fd-a6ce-c2327bb2e4a9 | -8.58244 | -48.55151 | 2025-08-22 05:12:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a16052b0-3531-3a16-a691-cbe75d3592c9 | -6.57255 | -59.8755 | 2025-08-22 05:12:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2590f8d-b428-3b95-a152-58a9ea210f6a | -9.16995 | -59.60415 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 116695f0-4c11-3b45-bb34-af04ec7e8cca | -13.3278 | -54.39899 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8e64f8d1-e74c-3aa2-94c7-319827dd3579 | -8.54586 | -66.9522 | 2025-08-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d2fe4b9-f8fc-3946-b06e-1ceae6b9e115 | -8.60342 | -62.62417 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4de6ffb-4622-3120-af4a-b9ee4a63a099 | -12.49399 | -53.80745 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac4952f8-06a9-3f18-afef-70e603fffc39 | -13.49291 | -47.04201 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29550320-d0e2-3af9-9402-7a0c506a6806 | -12.96448 | -46.26001 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 71f46e58-58b3-36d4-a04a-28961572ff9c | -6.90278 | -59.89599 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8eccb97a-6e27-331a-88f7-11891a62d16e | -12.99648 | -45.23949 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 074da475-5f5d-3f04-8641-90c412a1b01a | -9.2106 | -59.78232 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05ccc2f0-df0a-380b-9092-61936e033972 | -10.73721 | -48.25433 | 2025-08-22 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d7854cc5-5a54-386a-a98b-fe2e6ee0feba | -7.54918 | -63.84763 | 2025-08-22 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2ea5786-1691-397a-ab1c-3f77a863e430 | -9.21737 | -59.78341 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 314117b4-7f17-38dd-a46a-7df4e93608f1 | -12.49854 | -53.80437 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15a72946-ae71-3ea1-b46d-2bda43cc84a8 | -12.99011 | -56.88518 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 206664d4-5ee2-36ba-8935-e0ef06e112f8 | -12.99663 | -45.21521 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 78919044-da7e-3d7d-a635-b6fe562ac616 | -6.62058 | -60.00968 | 2025-08-22 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33d6d90a-4e3a-31b8-8801-8b332343d548 | -8.87509 | -62.41954 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ac70549-90db-38b1-8bcd-67eef0be81e3 | -12.92967 | -46.17065 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 26a4cd93-07d8-3e49-8738-8887785863d9 | -13.02704 | -45.19775 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1784be92-d6ed-374b-8d1c-26dc01dd1fbe | -9.16716 | -59.59999 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1902f0d-136a-3042-88f0-710ba316d433 | -7.36561 | -57.63419 | 2025-08-22 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 782b4b46-0c35-3eb0-be7d-419fc1f09599 | -7.30785 | -59.62534 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3f10c333-f05e-3fef-b065-723fba746f0b | -8.86519 | -62.408 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8ff8426-a4c5-30d8-8d49-9a8fc6b51b88 | -11.03513 | -59.17702 | 2025-08-22 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b503dcf8-30c3-3a67-813e-37e02cecbb35 | -9.52378 | -60.54423 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 717250c5-d6b7-33b0-a491-2f55322cd64f | -13.00301 | -45.22305 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 56812684-4359-318e-b2b8-0c9d97d76e59 | -13.00371 | -45.21608 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 51c2f03e-75c8-3c54-b66f-f503c882fc67 | -8.46619 | -64.04842 | 2025-08-22 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35082c7a-337f-34c9-8f7f-60cbf3427134 | -9.19562 | -59.63794 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29db481c-692d-3fff-b5d1-c4169892e873 | -7.55999 | -63.86214 | 2025-08-22 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 929a4bd9-2abf-3c85-b253-ee46b32f619a | -9.47487 | -57.82605 | 2025-08-22 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README48.md)
