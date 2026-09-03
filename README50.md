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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a119211e-0331-35d6-b244-d466cfda8fe9 | -5.2078 | -60.04852 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 70862d42-27ec-308b-befb-0115bd48f714 | -3.61316 | -60.56884 | 2026-09-03 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77d4d7ab-e74d-31cf-9165-ae19a621286c | -3.20258 | -61.22539 | 2026-09-03 06:18:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c4f8984-e25b-36cc-98c6-a1eb938475ff | -3.61869 | -60.56136 | 2026-09-03 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9280263f-5579-37a9-b4d3-ecde58271e48 | -5.25822 | -60.18275 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de9d0bc6-9882-3ac1-bac8-5af4509c5dc1 | -5.25696 | -60.17919 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de49bc8a-46d2-37f3-a11f-bee85505de95 | -5.46864 | -60.05957 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b4c310a-64b0-3ecc-a891-5f5c5b6605a0 | -5.59018 | -60.20232 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0771097-3510-33d9-be6e-a6c0e4ad4f01 | -5.46309 | -60.05385 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3c91437-e9f3-35eb-a442-aef1e7a9d12f | -3.14618 | -60.64441 | 2026-09-03 06:18:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54a1e195-d08a-3797-a24a-477104f0b825 | -3.20422 | -61.2142 | 2026-09-03 06:18:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab71f285-7af1-3840-a51b-b65d16b40482 | -5.33168 | -60.14147 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb633b92-5aa5-32a6-aed9-4d0e50e8ed79 | -5.20983 | -60.03404 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75ed7095-7708-3a63-9774-862f3460593e | -5.33236 | -60.13669 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c00f38c-6333-3064-a2d2-f747126ebafa | -3.12383 | -61.23369 | 2026-09-03 06:18:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6305494a-cc47-3c2a-8398-358910834270 | -5.4624 | -60.05871 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd6c1932-0a2b-32bf-9ea5-834527d34b72 | -3.39341 | -59.36533 | 2026-09-03 06:18:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9200675f-239e-3e62-98b0-44b81168a802 | -5.55506 | -60.23587 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffd8cd23-6d49-3ec6-b909-f3a226814373 | -4.23983 | -62.23455 | 2026-09-03 06:18:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40ca04a0-2549-307f-b7f4-19520d39adf4 | -3.20444 | -61.23071 | 2026-09-03 06:18:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 55d69ea9-3e85-3914-b953-59db8ace17b9 | -3.20204 | -61.22911 | 2026-09-03 06:18:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4e4a08f-35ef-32d6-af12-2ecc1d186b2e | -3.61808 | -60.56557 | 2026-09-03 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6ad74029-c979-396a-b035-dd045a945984 | -5.54889 | -60.23497 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5675003b-a61c-3491-afa4-5e6c479b2233 | -3.20501 | -61.22698 | 2026-09-03 06:18:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f338416-b1f5-37f5-ab9a-a6b75803ddd0 | -5.20915 | -60.03889 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cc96951-50b7-34b9-b445-c0609c7001e7 | -3.3853 | -59.42081 | 2026-09-03 06:18:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc650c48-acbc-3e24-9c42-2edeb3602397 | -3.12495 | -61.22621 | 2026-09-03 06:18:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cebe1d94-44c4-38e7-8fd0-986e6f2d5ca3 | -3.14037 | -60.64349 | 2026-09-03 06:18:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a90d672e-539b-33ef-bd83-e83d347e100f | -5.56868 | -60.1747 | 2026-09-03 06:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37d6a0f8-8951-321e-b862-e3bfd22622db | -8.5917 | -67.1603 | 2026-09-03 06:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 30.3 |
| fcef949a-fd7c-38d9-a48d-cd9a2245ee76 | -6.6698 | -59.9443 | 2026-09-03 06:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| ff5b8c03-e541-3eca-a91a-5eb792cc1576 | -6.6883 | -59.9436 | 2026-09-03 06:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 6abe6706-534c-3f0a-acb0-83f521d33c82 | -8.0737 | -50.9656 | 2026-09-03 06:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 93371d80-b62b-31f3-8257-e482bc11ec91 | -8.5916 | -67.1788 | 2026-09-03 06:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 57b05137-db12-3263-bc9d-235fd2be5acc | -8.0924 | -50.9642 | 2026-09-03 06:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 06efc520-3fe6-3236-bb40-c12a5be95d80 | -8.38925 | -71.05185 | 2026-09-03 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44a9f04a-1f84-3800-8f68-8cc84a6035ae | -8.59271 | -67.17339 | 2026-09-03 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6dd0ebfd-ea8f-3602-ad41-09d480151296 | -8.58814 | -67.17636 | 2026-09-03 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 381d9e97-2df8-36bd-988a-7f72570796e9 | -7.02607 | -62.97227 | 2026-09-03 06:20:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c894d5f1-b23a-338a-ab9d-1d6b687802c2 | -6.75808 | -59.43865 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f36dc476-34a5-3e1b-bce7-cff007fa69bf | -7.03134 | -62.97303 | 2026-09-03 06:20:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63a02b42-4a25-3e8c-820e-950db930bfa5 | -6.65108 | -59.4353 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 088c6670-1752-3c76-8f93-aed1a1d82d76 | -9.02534 | -65.44772 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddddcb36-10bc-3399-b80c-a58d47c6ad59 | -7.35961 | -60.60361 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4112439-5809-3581-8a32-b02f2e28ce2a | -6.84218 | -69.90567 | 2026-09-03 06:20:00 | NPP-375D | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01a61b09-9434-3799-b17c-31fc0169c2c3 | -9.07221 | -65.7204 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faf0d583-f8d7-3d8c-9c7a-47c19bd49e73 | -6.63964 | -59.43731 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d57ed014-2af9-3973-9032-a81f9809cbf5 | -7.5307 | -60.71888 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bea7b42-5b88-3aac-9d68-970796b113d2 | -9.13876 | -61.60167 | 2026-09-03 06:20:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f51b3ba7-25fa-3b90-9eaf-49d97d4fead5 | -6.68972 | -59.94078 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0d15f8c8-3e75-3a45-8bab-20fa97ef75d9 | -9.02838 | -65.72438 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5289038c-8b2b-3650-9e93-479c091682c8 | -6.77045 | -59.43509 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 213ce72d-fc8a-3dc6-bc6e-3dfee1c84dae | -7.84745 | -71.74967 | 2026-09-03 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| acfc3a45-e9d6-3098-b061-71749e0a79e8 | -8.58866 | -67.17278 | 2026-09-03 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b1530d62-974a-3745-9e04-d9b8cd3df752 | -5.59124 | -61.47325 | 2026-09-03 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6225fd0a-5fee-3a6e-b1c8-042e1f98a5ad | -8.59624 | -67.17755 | 2026-09-03 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e1da2d7f-920f-330d-82e6-d42719459f14 | -6.65179 | -59.42995 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c103e55d-7f79-3f6b-87fb-e30bcf89f222 | -6.67555 | -59.94938 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 39350a69-3dc4-3d74-908f-81df022cb82e | -9.08708 | -65.37459 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63ed7a43-f7ec-35b6-9ba2-6b266933659c | -8.79252 | -71.28626 | 2026-09-03 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af15b876-b44f-33d9-9fd7-6dd3a3b2810b | -7.02562 | -62.9755 | 2026-09-03 06:20:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 750be75a-57d0-34e1-b69b-610920cc9da9 | -10.28225 | -60.53665 | 2026-09-03 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f3ca455-4202-3256-9fd8-3d1a554b302a | -8.99264 | -65.44775 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10ca7b58-2a74-3c71-9382-cb7ad3263c6d | -5.58898 | -61.47508 | 2026-09-03 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ea58276-616c-3ea7-8dc6-2a1d8fe358f5 | -7.02383 | -62.98843 | 2026-09-03 06:20:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 795474ae-c512-3a29-9bde-12ac98770629 | -8.71775 | -70.68404 | 2026-09-03 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aad550ac-413d-373d-885e-ecd62740254c | -8.87597 | -66.67126 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be4b2d89-54e2-3acf-ac85-0f6f8a3b3d8b | -7.53685 | -60.71973 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1a7ea81-2d18-361a-a9aa-3f2b62e19082 | -9.01937 | -65.72321 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73a591f1-c0dc-35cc-a957-96d45b799561 | -7.36641 | -60.59996 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0f3813f-5748-3165-8578-9f4ab456d1ae | -7.19642 | -60.66196 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5950f321-2d4f-3204-83cf-93683cc6704d | -8.85247 | -70.62616 | 2026-09-03 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 947fcfc4-cf4e-337c-ac19-3c55c6eaa98f | -7.71867 | -61.13066 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cedc1df-77a2-3910-b376-d3775aa79ab9 | -6.7507 | -59.44333 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e5c8981-1997-34cf-a6de-6a3e60d7364d | -7.79525 | -70.05938 | 2026-09-03 06:20:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84520b52-f12a-31e7-91ad-e02b81c07eb4 | -10.28232 | -60.53646 | 2026-09-03 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c86c09c-6802-38ba-be89-13ed22e6e6d7 | -7.79582 | -70.05562 | 2026-09-03 06:20:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8926041e-7ab6-3ce8-aad2-a762eca33a8a | -6.74408 | -59.44265 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bfabcdc-8f21-31c4-be84-8a1ea7b2cf2d | -9.04442 | -65.74055 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d03d2959-9354-3a5f-8ef3-6f1fe0849e00 | -8.59323 | -67.16982 | 2026-09-03 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b4a7465e-48f9-3735-a977-fdfdb33d4edd | -7.84412 | -71.74915 | 2026-09-03 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e3b47d84-22c0-3a16-9e60-5159311f18ae | -9.02011 | -65.45172 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf918e0d-9f36-3cfe-96eb-62fc82ad9e89 | -8.49449 | -70.61642 | 2026-09-03 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efb05ec3-0221-3204-a1e2-4631b98d92f8 | -7.03044 | -62.9795 | 2026-09-03 06:20:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58d1d510-02eb-3763-a893-8f31e6a8b554 | -9.09169 | -65.37524 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95e23212-d9f6-3e17-9ca6-5ae852b26d1f | -6.64375 | -59.43997 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0f9fdbe2-0d25-3472-bbe8-5ac23d7ebf30 | -9.01947 | -65.45639 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20a88674-6319-3022-9bd5-a9c1a448b738 | -6.68904 | -59.94587 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a8caefcd-09f5-3726-99d2-6f9498ec86b9 | -9.10224 | -65.50008 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 321945a8-19dc-3546-8337-5043af5ec101 | -7.67886 | -67.0836 | 2026-09-03 06:20:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5a0bb25e-9935-3af7-b12f-88f0dab9a682 | -8.8519 | -70.62984 | 2026-09-03 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ca91970-5b35-3662-8a9d-df84cbfe5652 | -7.03089 | -62.97626 | 2026-09-03 06:20:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f3e7e8c-f075-38b6-8834-427e6af6b046 | -6.68076 | -59.94413 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bd512778-1144-3636-9e49-8bd19a0aca2a | -7.84748 | -71.77111 | 2026-09-03 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08da018e-4c35-35f0-8c2c-e0c3c8f57ca6 | -6.68836 | -59.95094 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 36268fab-9f94-3b6c-8c20-881ace085edb | -6.68129 | -59.95513 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 24154abb-7ee8-33d0-976d-1f3a06ef9833 | -7.29582 | -60.71427 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50ce597a-6c1f-39ce-8b09-1f417c5c56d9 | -9.10109 | -65.50628 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2c89c5b-e166-376c-89ad-1c84f88b96c7 | -8.92102 | -70.58699 | 2026-09-03 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72d798c2-9d0a-34ea-a3c8-4a265f4bc9d6 | -6.64699 | -59.43272 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README51.md)
