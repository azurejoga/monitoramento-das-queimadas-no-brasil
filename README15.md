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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4edf8424-ccca-3f3e-86ee-b3ee28126468 | -8.58578 | -44.3228 | 2025-07-21 12:12:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1647f491-6911-3782-9156-4a3507d2cba7 | -11.57585 | -44.83049 | 2025-07-21 12:12:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e988dc28-4047-3732-ac15-58abec2d5cdc | -10.138 | -49.66306 | 2025-07-21 12:12:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 3411f7dd-f154-3d51-b00c-a80392fdc9a1 | -8.83136 | -44.53919 | 2025-07-21 12:12:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4c3634a6-ab67-3a69-acff-5c3f695e725d | -14.61182 | -48.86264 | 2025-07-21 12:12:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| ae11c8e0-b732-379b-a45d-1009bfa7a932 | -11.12365 | -50.35993 | 2025-07-21 12:12:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| bcefdb68-02b4-3300-a569-bd8006b4ab80 | -8.82384 | -44.52908 | 2025-07-21 12:12:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| ed86c88f-17cb-3213-b7b1-f7080ce400cc | -10.66312 | -46.76976 | 2025-07-21 12:12:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 19066370-e5af-380c-9d3b-5eb9cca534f1 | -11.61733 | -44.22352 | 2025-07-21 12:12:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e400d2a2-54eb-3399-b18e-971ac68ed8ad | -20.56166 | -49.31075 | 2025-07-21 12:14:00 | TERRA_M-T | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 23e86c7f-7cbe-3fff-a0f4-e03861d52670 | -19.68177 | -46.44518 | 2025-07-21 12:14:00 | TERRA_M-T | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f8f6672f-e7ea-3898-8248-1ec00b1ed3d4 | -19.93464 | -48.17908 | 2025-07-21 12:14:00 | TERRA_M-T | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b95a143a-248d-3ff2-aa48-3babbbe42f2f | -17.6556 | -44.72784 | 2025-07-21 12:14:00 | TERRA_M-T | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 633a0568-7874-3bf4-bde5-f2f5df5d492d | -19.68044 | -46.45448 | 2025-07-21 12:14:00 | TERRA_M-T | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 26.7 |
| cb04fbbd-e3cb-3d0c-9a5c-1fa6672bea14 | -19.78349 | -45.25795 | 2025-07-21 12:14:00 | TERRA_M-T | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 20932daa-a8d1-35dd-ba10-ee29b5e3f5d5 | -18.59087 | -51.81297 | 2025-07-21 12:14:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 0e97f2ca-42b9-32b0-aafc-797c05a8361e | -23.4425 | -47.42972 | 2025-07-21 12:14:00 | TERRA_M-T | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| c65ffcea-30b1-3181-a38e-37ecdb6c3057 | -17.91083 | -47.76068 | 2025-07-21 12:14:00 | TERRA_M-T | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a460e431-27f1-3389-b093-c545e1a65312 | -21.47983 | -53.06195 | 2025-07-21 12:14:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 26.9 |
| cae52c2c-8dea-3598-b9c7-ea2f04a7a3ac | -17.0535 | -45.02303 | 2025-07-21 12:14:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1007c652-9f63-3e44-86dc-d0b5f8c05c46 | -16.64479 | -43.89192 | 2025-07-21 12:14:00 | TERRA_M-T | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 383c124a-1fb2-3749-8d8c-beaf5541b3c9 | -19.78481 | -45.24818 | 2025-07-21 12:14:00 | TERRA_M-T | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 406dcdff-b8fa-3d12-9ff1-8e22533eb0e3 | -18.4104 | -44.18349 | 2025-07-21 12:14:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| bf90569b-c55e-3a6d-a237-cd984184ec7d | -18.40902 | -44.19383 | 2025-07-21 12:14:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 4ca3293a-b607-3fc7-ae92-d6311908c969 | -18.04807 | -44.40737 | 2025-07-21 12:14:00 | TERRA_M-T | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| a85c8e86-10f9-39fd-924a-bec956cfccd3 | -18.39968 | -44.19256 | 2025-07-21 12:14:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 82d4b81c-28cc-35ee-97d0-ecce2965626a | -21.48688 | -53.05667 | 2025-07-21 12:14:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a88cd343-3f35-383e-9756-3f74f669dc27 | -23.86959 | -47.72812 | 2025-07-21 12:14:00 | TERRA_M-T | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 7fd53970-d5d6-3f98-acf4-d3ebfb2ff988 | -19.93613 | -48.16934 | 2025-07-21 12:14:00 | TERRA_M-T | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7d8d4f9b-8a01-31ac-ba39-a26fa9c9016f | -16.07885 | -46.85995 | 2025-07-21 12:14:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f0555b05-ef1c-34ef-845f-32a9d8cbe2f9 | -18.40105 | -44.18225 | 2025-07-21 12:14:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 40badc1a-a23a-3388-a299-22a293758d48 | -17.91989 | -47.76208 | 2025-07-21 12:14:00 | TERRA_M-T | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7f740f21-11e7-3cce-ab3b-a6bce3578299 | -17.65427 | -44.73759 | 2025-07-21 12:14:00 | TERRA_M-T | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 72b4e6ec-0a7d-3508-8524-d28dd6d005b3 | -6.7382 | -44.3215 | 2025-07-21 12:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 4ebfe9fa-d8ae-3110-ab41-5b4d72c8be26 | -6.9801 | -42.809 | 2025-07-21 12:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 99cd8101-b1de-3c7c-8758-ef984c67863a | -6.9801 | -42.809 | 2025-07-21 12:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 104.0 |
| f07530e1-56b7-33e9-9746-25e7a0877fd5 | -6.7382 | -44.3215 | 2025-07-21 12:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 78f7983b-89c4-36d1-9755-08bfe66b6361 | -6.7379 | -44.3445 | 2025-07-21 12:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 8e1af263-e5cf-396c-ba76-def3c21783df | -6.7379 | -44.3445 | 2025-07-21 12:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| b59a3099-e5c5-30b8-bfb4-f6ba9525249b | -6.9801 | -42.809 | 2025-07-21 12:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| 4449bf8a-bf95-3b09-965d-ef1d2efac146 | -6.7194 | -44.3231 | 2025-07-21 12:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| b01056cb-c5a7-3780-bf81-58582f2fe853 | -6.9801 | -42.809 | 2025-07-21 12:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 113.4 |
| c541246d-6894-3e66-bdcd-2fa0b8c5a385 | -6.7192 | -44.3461 | 2025-07-21 12:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 970f8dd9-4b52-3715-80cb-a4c03539b5ff | -6.896 | -45.38 | 2025-07-21 12:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| e51053da-d1d2-397a-a777-15d6b42bcc6c | -7.2646 | -44.2741 | 2025-07-21 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 376edd3f-6416-3e56-95d4-05c614cdf381 | -11.6079 | -44.2321 | 2025-07-21 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 9151905d-4358-3488-98f4-283698b030f8 | -11.6271 | -44.2292 | 2025-07-21 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| e0f02a28-f7b4-3c5f-a854-89ca05c9057f | -11.6275 | -44.2057 | 2025-07-21 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 15cd5a83-bc81-3f27-9701-24177aed71ab | -6.7194 | -44.3231 | 2025-07-21 12:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 89de09f9-87fe-3827-b3c7-abf68e5c4656 | -6.7379 | -44.3445 | 2025-07-21 12:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 06e5ba9d-819a-36fc-b72d-54ff87063026 | -6.7379 | -44.3445 | 2025-07-21 13:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 147.9 |
| b74c43be-c4a8-3049-b765-de1e6e4610a3 | -7.5622 | -44.5678 | 2025-07-21 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 35ffab1e-42a2-31f5-84de-1e71705ad6f4 | -6.9801 | -42.809 | 2025-07-21 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 104.0 |
| 3181a176-28ee-3154-babe-6cc58196f278 | -6.896 | -45.38 | 2025-07-21 13:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 326c7ad0-d1d3-3786-af38-3a8c32857fc7 | -6.7194 | -44.3231 | 2025-07-21 13:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 152.1 |
| f70e34de-4cc0-3b49-8287-e2251ab5ce00 | -6.7192 | -44.3461 | 2025-07-21 13:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 4d78ea83-79d0-38e6-8d3c-b67f49f801d3 | -11.6271 | -44.2292 | 2025-07-21 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| bbe90c6f-d702-381d-b98f-1b9b6da4142d | -11.6275 | -44.2057 | 2025-07-21 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 958c347b-37cb-38df-897e-5a551fdc2fb1 | -11.6079 | -44.2321 | 2025-07-21 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| f46075bf-5a49-3d2f-a1c0-a75bf6626b96 | -6.9613 | -42.8108 | 2025-07-21 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 2781ba17-0dd4-3b93-93a6-4dd8a909a33a | -6.9613 | -42.8108 | 2025-07-21 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 535bdc13-ead8-397d-9b9b-750a3191861f | -11.6271 | -44.2292 | 2025-07-21 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 11952caa-8723-313c-9a7f-d7b322ce0756 | -6.7194 | -44.3231 | 2025-07-21 13:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 183.7 |
| f0784ee0-1650-3fda-a4d2-dd228dd0a6db | -11.6079 | -44.2321 | 2025-07-21 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| e794490f-c564-332b-b6de-69350896becb | -6.896 | -45.38 | 2025-07-21 13:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 462a3894-0ab8-3fd6-bdfc-9e93abb22d0e | -6.7192 | -44.3461 | 2025-07-21 13:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| e4063d00-b014-3b74-93c9-32657e93163a | -7.5622 | -44.5678 | 2025-07-21 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| ddbf16ab-5e8f-32ab-8507-e1e17a5c3ab2 | -6.9801 | -42.809 | 2025-07-21 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 126.4 |
| 74cde060-d8c0-3c6d-962d-de3ab72cf96e | -7.9648 | -43.9738 | 2025-07-21 13:10:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 21b0d83c-01f1-3aae-b9f3-1345c1b91965 | -8.9405 | -44.4457 | 2025-07-21 13:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| db5c3cc8-3f41-3e45-8594-b7d93538cb64 | -7.5622 | -44.5678 | 2025-07-21 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| b97a2684-63b0-30cb-9a20-d9b1aafd65e0 | -11.6271 | -44.2292 | 2025-07-21 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 2cc5799b-feb5-3cc7-aa68-be7050d81b19 | -11.6079 | -44.2321 | 2025-07-21 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 3c3a44bb-3584-35ff-a475-e439d56d8af6 | -6.896 | -45.38 | 2025-07-21 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| afa64417-f984-3df7-b10d-f82c07b0ebc4 | -7.2772 | -60.1698 | 2025-07-21 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 415a32c0-eca3-30da-aad3-5ba8985472d1 | -6.9801 | -42.809 | 2025-07-21 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 143.9 |
| afbe3abe-168e-3a81-9dea-64e64abfd87e | -6.7192 | -44.3461 | 2025-07-21 13:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 6e9547e1-3288-3552-9c58-2ce3366c9a33 | -6.7194 | -44.3231 | 2025-07-21 13:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| fa1b89d0-86cf-373f-8600-05a24e66af31 | -6.9613 | -42.8108 | 2025-07-21 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 109.3 |
| d0001cea-9d21-3049-9635-24faaca33aec | -10.1357 | -49.6538 | 2025-07-21 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| de59bd3e-fd6e-33ab-83e0-92da61877f5a | -11.6079 | -44.2321 | 2025-07-21 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 0fc3b194-d654-33db-b05a-595b920396c7 | -7.2402 | -60.1904 | 2025-07-21 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 07c74fa3-e6e4-380c-8ace-eec57e3f8776 | -6.7192 | -44.3461 | 2025-07-21 13:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| f8963680-f6a2-38d9-80b2-e77578077a6e | -7.5624 | -44.5449 | 2025-07-21 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 7eb6ff5f-5c33-3bb9-ab07-e69fb7c75018 | -6.9801 | -42.809 | 2025-07-21 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 156.7 |
| 2f5938e5-c39c-3b76-ac44-737a7f5c52a4 | -6.896 | -45.38 | 2025-07-21 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| d46db015-6704-3810-a9e9-f0b776355f5f | -9.4031 | -47.9707 | 2025-07-21 13:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 89d26d8f-e04a-3b20-be6c-484835615097 | -13.8773 | -46.3681 | 2025-07-21 13:30:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 059c94f9-956d-314e-99b0-57b323215299 | -7.5622 | -44.5678 | 2025-07-21 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 7d5ece49-51b6-3345-bfdf-215b21884308 | -6.7194 | -44.3231 | 2025-07-21 13:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 158.5 |
| e0349ad8-18f2-30d7-9d0a-d780bf588c14 | -7.2772 | -60.1698 | 2025-07-21 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 99a68e07-6c87-3563-b0c5-31ec7d962305 | -7.2772 | -60.1698 | 2025-07-21 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 0d25dd07-ba98-36be-82e0-b70e37ccd113 | -7.2644 | -44.2972 | 2025-07-21 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 21da1e30-4693-3785-af44-5aba246a3090 | -6.9801 | -42.809 | 2025-07-21 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 147.5 |
| 185424fe-cb75-356d-94d8-533d6784d508 | -8.0061 | -43.6905 | 2025-07-21 13:40:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 3db02ad8-b661-34ce-a973-dc629463c758 | -7.5624 | -44.5449 | 2025-07-21 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.7 |
| a747a78f-c9f3-35f5-97d7-4419c84748c2 | -7.5622 | -44.5678 | 2025-07-21 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 205.3 |
| c7c70dc7-99d8-3d9b-85c9-39d6e6ce7745 | -6.7192 | -44.3461 | 2025-07-21 13:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| ca9d139e-b2b5-3870-933d-b2d7c09954e0 | -7.2402 | -60.1904 | 2025-07-21 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 498e4450-4262-3c81-8fb3-6129b107b667 | -7.2957 | -60.169 | 2025-07-21 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |


[Clique aqui para ver as próximas entradas](README16.md)
