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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b98b739-9e91-35ba-800e-3d2a8074e01e | -6.89876 | -43.64045 | 2026-08-28 04:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 579a221c-acb4-3ccb-a537-011ee9241f00 | -6.93705 | -42.67659 | 2026-08-28 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 91091ea4-14d0-3ae4-991b-dda0934d45d3 | -6.26339 | -53.33805 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7217dbe-cfd1-3eae-9b65-f6c141b83c0a | -7.269 | -49.85695 | 2026-08-28 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 156de5f6-a0e2-31d9-8aed-846c69a171d8 | -7.88063 | -46.09594 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b72d1cb8-aa23-385e-a3fe-55731b0dc9ee | -3.35331 | -49.23539 | 2026-08-28 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5abae109-84c4-38b1-81e9-7ab5b26ad5de | -7.09854 | -42.18624 | 2026-08-28 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 574cc1c1-07a1-324a-8c47-1300ed56a18f | -6.59492 | -55.4399 | 2026-08-28 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebbf2b29-ecce-3465-b795-ad70e25eef81 | -6.15818 | -57.79919 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| eea2738e-a05c-3d08-83c5-b6bdc6ac36dc | -7.26346 | -49.84895 | 2026-08-28 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4e2f256-89bf-3d9a-9a5b-d1aa582cdb82 | -6.4156 | -51.67758 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e051bd7c-4e62-39c9-8d24-97e153e9a3d0 | -4.84625 | -45.39041 | 2026-08-28 04:49:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2fb690ea-b1c9-386e-9256-f8c6c0bb52e6 | -7.10673 | -42.82734 | 2026-08-28 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 42febc26-ea80-3592-ba89-f274178e92ce | -7.19913 | -42.73923 | 2026-08-28 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1398362c-7718-3195-b60e-cc1b0bc56b64 | -6.43826 | -55.77769 | 2026-08-28 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a505aeb-1c5b-3c71-91d2-deef993e686c | -6.44298 | -54.98485 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0daac9c3-4450-39ac-9fbf-0c929504c10a | -8.0741 | -45.80839 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ac21cb9-83a1-3668-88a5-c9e18e20c2c7 | -2.73195 | -47.04051 | 2026-08-28 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bbb89f0-aa5e-3f20-963e-0c85905ac6aa | -5.26303 | -50.96596 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dce3ddd9-bcf9-3e26-8a63-da5d95d69c90 | -2.04475 | -48.03206 | 2026-08-28 04:49:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25e278ba-8120-3d9f-af25-9e6e37f3f8df | -7.26733 | -49.84602 | 2026-08-28 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b26ce92d-2e40-3b4c-aaa2-d7f91938461c | -5.59058 | -46.24523 | 2026-08-28 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f58b4bd1-dc4a-328e-ba3e-b272ee9758d3 | -1.59283 | -47.35702 | 2026-08-28 04:49:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 61382032-3a81-3ee3-b753-4a6c6241e637 | -6.37393 | -54.95434 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b0083ad-a400-3731-82ca-39f93045e9a4 | -2.73252 | -47.03687 | 2026-08-28 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 133965e4-426c-3960-a79e-5bdc85c110f8 | -6.3076 | -53.57921 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43f49399-c51d-38ca-be2c-95a243458225 | -5.54182 | -46.60933 | 2026-08-28 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fa6c2cd-d98e-3f29-b2c8-9585b07a9c77 | -4.85239 | -45.40051 | 2026-08-28 04:49:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1b2a9554-3d1d-3d1a-9412-1000b2f48b4e | -7.24993 | -45.85682 | 2026-08-28 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2c654e7-7c72-3c8b-9ef7-03dea03f5bac | -6.23101 | -55.49072 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75603e96-6b3a-3c66-9283-457078ccabf0 | -5.81707 | -46.22575 | 2026-08-28 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d3b2c2f-5965-3bf5-badd-67bd75c98c12 | -6.16021 | -57.78768 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca9d6e45-fec9-340f-93dc-96437e765217 | -8.09614 | -45.80899 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 718acb19-579b-308d-9320-4740af835a59 | -2.4986 | -48.13865 | 2026-08-28 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78fac782-d790-3fd9-b1f7-baf28c359e9c | -2.81302 | -48.63057 | 2026-08-28 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 216c7380-fa8e-3240-9e38-b8ee4f9887e5 | -7.88882 | -46.09242 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 009db27c-ef53-3ddb-ac83-bc1dc6836ff7 | -5.93857 | -52.36446 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 656d1971-e916-325c-be20-f68f726a3491 | -3.05554 | -48.74621 | 2026-08-28 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 554724b7-4588-3fc3-b00f-9dece4ed68a9 | -6.26064 | -55.42072 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 971a5552-70ba-3dc2-870a-17dfe5bf6f6b | -6.48737 | -53.5025 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f1ceec8-27d4-32b2-a0c7-c3b609bedae5 | -6.17606 | -55.46648 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb479446-03d7-331a-90bd-e6db51bc91fd | -7.02105 | -42.11298 | 2026-08-28 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ce1a5b77-09e3-32a4-bca7-bde32985b4af | -7.26387 | -45.35619 | 2026-08-28 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7acae22e-717d-3250-a7b7-4840add9b83a | -2.71674 | -49.47316 | 2026-08-28 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9096f78-299f-32a6-8b09-bcaf2eb52aec | -5.25681 | -50.9612 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 899e58c5-5191-3a8d-ae8f-34b4e4539fa1 | -1.35668 | -54.62943 | 2026-08-28 04:49:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 762bd7f8-2074-3932-856e-a3104701c1ce | -5.87432 | -52.1844 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 588db75e-9347-36c1-839e-8b9cbe7e2752 | -6.06573 | -53.76947 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6f7ca95-11e4-39da-97e6-2bed536cecb5 | -7.03942 | -50.72062 | 2026-08-28 04:49:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bc5e80f-d9cd-3ff4-b157-5c96b6a14e81 | -7.15487 | -46.53961 | 2026-08-28 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48d34d2d-6211-3b19-ad30-bd3c34079be7 | -6.3065 | -46.41268 | 2026-08-28 04:49:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 620d33d4-0a3d-37e7-b390-64e15293e35d | -7.31137 | -42.96413 | 2026-08-28 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 80d4f8b6-fae0-3d25-b25f-3b2581a0b7bd | -6.25132 | -53.36398 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d92ab02a-58ea-3577-91ba-3540bd1acb46 | -7.28563 | -49.94505 | 2026-08-28 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| beca6c08-0d02-3364-ba20-1bad84169cb3 | -6.49352 | -53.25737 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06befac1-d24e-39f9-b635-65f969b99352 | -6.16776 | -57.80385 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5f27472-895b-32f5-9857-db6a85d4b28d | -7.46409 | -50.92403 | 2026-08-28 04:49:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7396cc12-bd07-336e-83fd-a42637a1bd53 | -6.64406 | -53.18547 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd6ac599-7b48-3285-a4a3-6a0242cc03a9 | -6.32327 | -54.73767 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 178e701b-6381-33ba-a965-1fcc4ce655a9 | -7.25234 | -45.8665 | 2026-08-28 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| f93f70f6-f189-3183-83c9-b17c46e50f33 | -6.27766 | -53.13871 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| aa1278a2-e791-3e0a-8eca-1d939d43925b | -8.08021 | -45.81107 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b7344d3a-dfbf-3b30-ac11-74116d3dbc80 | -2.73479 | -47.04466 | 2026-08-28 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ceeea49f-0cb1-399f-9f99-faa96f811fdd | -2.72235 | -48.79951 | 2026-08-28 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 149aaa7a-9847-3f57-a432-cdb64c48377d | -6.16576 | -57.7857 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21a7ecf7-d646-346b-b9b7-7e8bd1fc1307 | -4.16774 | -42.43897 | 2026-08-28 04:49:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6ac41e32-1ea6-337b-afc3-ec8f0b56c7a0 | -3.46316 | -39.585 | 2026-08-28 04:49:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c36deff3-c83a-3983-af8d-759733100672 | -7.01624 | -42.11224 | 2026-08-28 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a8fbff06-dca5-3c00-bbda-37aff19785bd | -6.25136 | -55.42347 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45989bb1-d683-36b8-ad71-9ffb2b2e19fe | -2.88608 | -48.08208 | 2026-08-28 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be6bcc88-f1ff-3cad-86cf-c9a79e48b366 | -6.90323 | -44.6696 | 2026-08-28 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93736e6a-b558-3396-ac6c-92a31b763647 | -7.24925 | -45.86138 | 2026-08-28 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| be4b7c13-d3b5-3f11-bf6d-3f5310495b1d | -7.26502 | -45.85903 | 2026-08-28 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 25e5f6ec-27a2-3f38-9a80-6efc826d0d4e | -6.63964 | -53.18923 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 143411d5-8b04-3ffe-b15e-29b769b70d2e | -6.16324 | -57.80003 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccaed4df-8821-39cb-86dd-81e2266810da | -5.87723 | -52.18897 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd5070e3-7003-313a-8c8f-32571349cf22 | -7.27287 | -49.854 | 2026-08-28 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e182db8c-9907-38e1-adb4-650b41ed9f5b | -5.25962 | -50.96541 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 660829a7-4c72-3916-94c5-89806e27ae8a | -5.75894 | -50.22361 | 2026-08-28 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0312498f-bdb8-39d1-866f-57247b5cf5ba | -6.30225 | -46.41628 | 2026-08-28 04:49:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b53f971-1906-3597-96e8-555659ad767c | -6.24307 | -55.47196 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f0970d4-2890-31cd-a217-5f314d89a5d6 | -2.09675 | -48.21729 | 2026-08-28 04:49:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4288784f-3b81-32a3-b1f3-fa5e587c1394 | -8.08037 | -45.8185 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8dbb3df7-bc41-3f97-9c9f-313709df6a2f | -4.93082 | -47.46405 | 2026-08-28 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 879685eb-f847-3a0d-b2a4-7369f3482285 | -2.81248 | -48.63402 | 2026-08-28 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 195e320b-8f3f-3cc7-9218-6e3625616bee | -7.2884 | -49.94905 | 2026-08-28 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e319ec3-b863-38d4-b296-63c97f3d1913 | -4.3019 | -55.24497 | 2026-08-28 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d540c420-d31a-38b2-85d1-6c1b8f5e3e0c | -8.07725 | -45.81337 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42f642b3-5733-3eda-a662-e265d3e24254 | -7.1645 | -43.16702 | 2026-08-28 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| edc047f4-0e02-302b-a3c8-4d79879f6b84 | -6.16928 | -57.79519 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87c27a54-0954-3b2d-8cbd-15099335ea21 | -7.74658 | -44.73476 | 2026-08-28 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce4f10fd-0ba6-3a02-8961-bb5303eea42c | -7.78006 | -46.14717 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9df22cc3-5af9-3f0e-b809-930a69d0e029 | -2.80639 | -48.62953 | 2026-08-28 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7099487e-0913-31b8-86d7-d7d157d2f8f8 | -3.7994 | -50.61646 | 2026-08-28 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1417540c-ff01-32e1-8296-3feefa42a422 | -6.62557 | -53.18227 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfb26f35-7959-3ef7-b086-6d929d758843 | -7.07334 | -46.2633 | 2026-08-28 04:49:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78cdb34b-ed22-3942-809c-468006ef52a5 | -4.84795 | -45.40443 | 2026-08-28 04:49:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d3bc86cf-e7a5-3803-a91e-3cc0314592e9 | -6.16425 | -57.79426 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f3251d4-db6d-309d-8159-285923b08d74 | -0.70366 | -50.58489 | 2026-08-28 04:49:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59c15478-da0c-3b83-b0c1-db79f525c837 | -6.64036 | -53.18484 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README31.md)
