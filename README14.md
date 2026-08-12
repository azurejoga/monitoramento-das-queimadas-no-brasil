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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ec3bd98-0dc7-3530-b726-1ec3c8ff03de | -14.28286 | -45.28568 | 2026-08-12 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0180246d-9154-3c47-9a12-dd29cf2dadd8 | -14.30584 | -51.9895 | 2026-08-12 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 730726c3-d791-369e-ad9e-9d389d8eb545 | -11.48105 | -44.56982 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| f23cc90b-2981-3681-a8ad-635057dff73d | -11.95543 | -46.32319 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d86a4f9-b377-3ec7-a921-e87c4c96aed3 | -10.19047 | -48.7607 | 2026-08-12 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b248e11-15f0-37ba-b822-481fea170b8f | -12.8548 | -52.03928 | 2026-08-12 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23acd281-0bb7-3126-acce-80d483f4d5cc | -11.82594 | -51.84143 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a3a4a35d-019d-380c-910d-a528d3f90370 | -13.90186 | -53.81093 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf0d31b6-f5b5-346d-ac16-f3f9b82d209f | -14.50828 | -49.29009 | 2026-08-12 04:17:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7668e8c7-7c5d-330d-8f0f-375f32012dcf | -15.30258 | -48.87851 | 2026-08-12 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0f2dad44-1619-309e-a319-843e069af18e | -10.10138 | -46.20834 | 2026-08-12 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24cfc364-a328-3a14-8f6b-376ec95cfb9d | -11.95846 | -46.3904 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd96783f-c03b-3658-9b64-5958db8850bc | -13.90511 | -53.82161 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfc5a81f-ce51-3cc7-ba90-0621b12c9912 | -9.13436 | -46.38907 | 2026-08-12 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| edc4c9a2-6f25-382c-9d67-bb32a0162139 | -11.88955 | -45.83482 | 2026-08-12 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc595368-3632-3a9a-88d4-c2a44984f91b | -11.4805 | -44.57333 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d203fdd2-497f-38f4-a26e-12a72e69240c | -20.96494 | -47.41766 | 2026-08-12 04:17:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c951f370-0a5d-39b8-bcd2-40907a054361 | -15.16762 | -49.26069 | 2026-08-12 04:17:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c1d008f-3264-3656-a1e3-5ff2c553edc9 | -12.16345 | -50.12797 | 2026-08-12 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f51abfff-32f4-3a90-9671-74cb89b4e2a5 | -14.5217 | -49.30301 | 2026-08-12 04:17:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0ea4880-ee25-3949-93b7-396070cda152 | -13.83936 | -53.79352 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cad593bd-38d5-3f8f-b125-f6d09dd1168c | -11.95159 | -46.34657 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c8cdb568-d684-3e7d-85d4-61d6272f0603 | -11.82707 | -51.84983 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2f17efd-abcc-3f52-b68c-1a3e6d817d8d | -11.95566 | -46.34313 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| caa35897-f468-3be8-b97f-d7ebaf8caf34 | -9.3651 | -47.4482 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09eb90a7-c2c2-3d98-a0b7-6524a9821747 | -14.28617 | -45.28623 | 2026-08-12 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 637d8293-3ed3-353e-ba1d-87147fd142a6 | -11.4758 | -46.61244 | 2026-08-12 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 19fcebd7-5ab9-3025-beb2-d16bf8ebec61 | -15.27904 | -48.86106 | 2026-08-12 04:17:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96a4b894-6d28-3511-82e5-11300728d40d | -15.02727 | -46.59274 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c21c33bf-b4a7-3aef-8562-ebbe5ad5489d | -9.92605 | -49.26036 | 2026-08-12 04:17:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ba5ffb5-099a-3940-abf5-866f9d533916 | -11.89014 | -45.83118 | 2026-08-12 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e5c5e71-3688-309b-8729-9c49798643d2 | -14.34333 | -54.05021 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cc4d12f-ba88-3fa1-96bb-55546cc755db | -13.89032 | -53.78825 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8ba0495e-50c9-335f-96f8-b76ea7b58a02 | -11.49449 | -54.60012 | 2026-08-12 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 883edb93-0f41-3045-be33-61e541888e4c | -14.30089 | -51.99729 | 2026-08-12 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a59a1672-6ff7-3b60-987d-53c1c10d33bd | -11.97556 | -46.39322 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6df990f5-3b87-3cbc-b533-ed40bbf107f5 | -11.02938 | -45.65988 | 2026-08-12 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0063ed2-1282-3495-8996-e67729a7f1f6 | -11.95224 | -46.38548 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a536879c-bb65-39e4-8a04-b89185cc220a | -11.82308 | -51.85661 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81e7ded1-8229-31db-8e0d-7717f2af5877 | -11.95532 | -46.36663 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a8700fd-ef57-3960-9dc0-82aacd531a80 | -13.43229 | -48.27613 | 2026-08-12 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f379d5d6-0328-3ad2-acdb-fa21ef293866 | -11.98302 | -46.39054 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 83883b5f-c62e-311c-85c6-5bb788e5b910 | -21.15825 | -48.63797 | 2026-08-12 04:17:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8bb380bb-6738-357a-bd02-e26fd5f47455 | -12.85943 | -52.04024 | 2026-08-12 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69d8a683-b14c-3205-9c90-3c63b3bb66b1 | -14.28948 | -45.28678 | 2026-08-12 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a89ec33-a2d8-37a9-aff3-59e85878a346 | -10.22748 | -45.93065 | 2026-08-12 04:17:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dd2479bf-9d9d-3776-9d7a-416518d94899 | -13.60311 | -46.23884 | 2026-08-12 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a817abb-a8a1-35e6-80af-d347c465b802 | -9.37321 | -47.44501 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19ec1960-3060-32a0-adfe-e64418f2f919 | -9.13787 | -46.38963 | 2026-08-12 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 60a4b951-c502-3603-88d1-39014830a5d0 | -9.35031 | -47.49104 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16f01b0f-aaf6-3638-b11a-d19d9bfd2c8e | -10.63822 | -47.49145 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4dc1c59b-112c-3916-b930-0b68d103732b | -15.17138 | -49.26134 | 2026-08-12 04:17:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6473f9a-af5e-327b-b7ad-01ead74722bf | -9.67643 | -48.15935 | 2026-08-12 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4886835e-521d-3390-8e8b-fe3977e6eaba | -14.39984 | -52.07033 | 2026-08-12 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 5a5a35c8-b160-371a-8994-cbadbae28352 | -13.83879 | -53.79652 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6947ea3f-91cc-3c6c-83d5-0522ccdc66d5 | -14.28122 | -45.2745 | 2026-08-12 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2afee828-f933-3dde-aa4b-46075b9dc3ce | -15.0089 | -46.57798 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6920e99-2d30-32eb-8b86-0f0a4e99c4a5 | -20.03599 | -47.16407 | 2026-08-12 04:17:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad093d09-26f2-3dc3-9c60-93ea386a730e | -14.59117 | -46.75264 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c38b1947-fc8e-32f3-9114-84515b8bda6b | -14.55265 | -50.40612 | 2026-08-12 04:17:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79da0797-929a-3d5c-a32b-5816c1beb33c | -11.78399 | -51.84716 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d17a4e1e-4600-3174-b138-a6b40e1d2d0e | -21.15892 | -48.63403 | 2026-08-12 04:17:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ab4f0427-5564-3057-b10f-f115ad7063cb | -11.46561 | -44.56015 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7562ecd3-fb33-3f5b-a6c1-8261b3c47c87 | -10.21721 | -45.92917 | 2026-08-12 04:17:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 35.4 |
| cc8f5f13-7cef-3614-bc1b-e153f42f1dd6 | -10.8216 | -45.53274 | 2026-08-12 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa867e1d-7990-3229-b028-58cd5909ba41 | -13.59975 | -46.23826 | 2026-08-12 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5febd8cb-ace4-3110-b797-b241600467ac | -11.88735 | -45.82698 | 2026-08-12 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e48dcb8f-0179-3715-8a3c-181e04cebf3f | -12.10659 | -47.18959 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 137a29fa-c878-300a-a4ac-bd0b47b0dec8 | -11.48822 | -44.56738 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| bc761b39-1116-3b45-bbca-487bfd911a6c | -9.34138 | -47.52141 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3899dd2-2d08-31dc-b6c0-00d936a372c2 | -11.98463 | -46.35901 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa223007-95d2-3e2f-88b3-f8a0e9f5223c | -12.10608 | -47.19049 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27702f8b-fbfe-3807-88b6-04350a81b742 | -14.48193 | -51.86195 | 2026-08-12 04:17:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fda34c60-9fec-3aa4-b0b0-134aff6b3e23 | -11.46989 | -46.69152 | 2026-08-12 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a69167ec-1c1c-3196-b970-39c456009b67 | -14.98847 | -46.59731 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf3e2581-bde2-338c-8936-fa3ac35a80de | -14.03616 | -53.59858 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 19394a35-3e9c-3941-93bf-3f38231ce41a | -9.84294 | -45.70459 | 2026-08-12 04:17:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 572a13ba-47cc-3444-9ea3-81a1ac943fd1 | -9.45723 | -51.81571 | 2026-08-12 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb7ea25a-7a44-3ff2-9882-939b1f8da429 | -13.89153 | -53.78207 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 673c92c5-30c5-30f6-a68c-1d06ba8ae1c2 | -10.21965 | -45.91402 | 2026-08-12 04:17:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 59a4f486-4994-34b6-9989-763b77601b96 | -11.65487 | -50.14534 | 2026-08-12 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f2b43715-9b35-3cc5-9557-e44115b11078 | -11.46285 | -44.55611 | 2026-08-12 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b18df6a2-4dd6-3174-a9c6-5efb0df8d9c4 | -9.33543 | -47.53411 | 2026-08-12 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d4e08dc-e291-342d-b72a-cb595a5d9977 | -13.88638 | -53.78117 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1a9d2e92-41f9-3f4c-808e-6493ee542886 | -15.01933 | -46.5991 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c817dcd1-6c59-3107-8b19-d386050b415e | -13.57262 | -46.25624 | 2026-08-12 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 77177334-93c3-3de6-9e46-f09198c07eec | -13.88869 | -53.82378 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72b078b7-e5cc-3279-9ec1-d76c65eea2c9 | -9.13723 | -46.39355 | 2026-08-12 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6c3c77c4-f5d0-34ca-988c-82afe8166553 | -11.9796 | -46.38999 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 83cc48b7-2c9a-32a3-a9d9-7178f60349fe | -15.16679 | -49.26543 | 2026-08-12 04:17:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df9fb2c4-c801-3972-b7cc-3d6ec315de0c | -15.00864 | -46.601 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 359294a6-e718-3e60-801b-66c4c68df5e4 | -14.59271 | -46.76446 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 693d5298-bddd-3aa8-a31d-eff46257c558 | -11.95137 | -46.32655 | 2026-08-12 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| beff152a-0e47-3cd2-bcfd-8f97f325d963 | -11.6051 | -54.64778 | 2026-08-12 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b0d2df3-7f2e-3488-a6ec-68334e33f798 | -13.89547 | -53.78913 | 2026-08-12 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| dde5e435-91a1-3306-8807-25802cd846a6 | -12.10739 | -47.18248 | 2026-08-12 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 092cc482-cacb-3f03-a094-2824804efa36 | -14.58315 | -46.75898 | 2026-08-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7d28c08-13d1-3472-a729-79889552e275 | -8.88142 | -50.17984 | 2026-08-12 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64545235-5db4-3980-aa65-5fa372a8cf25 | -11.82688 | -51.8364 | 2026-08-12 04:17:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 61c9e779-6c67-30c4-9de1-e7ad0f038aa9 | -10.36902 | -46.38161 | 2026-08-12 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README15.md)
