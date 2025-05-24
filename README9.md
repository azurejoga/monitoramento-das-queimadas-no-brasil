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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5582b85c-9a70-3d64-9a81-4b4207a2c8ac | -9.49654 | -47.47699 | 2025-05-24 04:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ddcb41c2-db77-38bf-af1a-15813f528f22 | -7.21527 | -43.12097 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 99e12574-3696-3549-a7ae-8effb9f5df45 | -6.22464 | -43.35055 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 537c658b-f50a-363b-ba65-a9d8e8beda62 | -10.02753 | -48.70082 | 2025-05-24 04:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8734869c-f6ee-3215-9597-43facb94b714 | -7.5884 | -43.31081 | 2025-05-24 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03c31e17-e1a6-3cae-8e70-bbbd83a9be40 | -5.68428 | -44.12321 | 2025-05-24 04:06:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 653303fe-b5c0-337e-99a5-1a86ddb04daa | -10.48843 | -42.42485 | 2025-05-24 04:06:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d9c47ffb-9f7a-3f1f-9339-89f374400a0f | -7.20003 | -43.12963 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c2abefd8-f5e5-3033-9ea0-440ca83fc5fc | -7.06859 | -44.92933 | 2025-05-24 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ed043b4-8e81-3ee6-91a9-b7a4561f3e48 | -7.06789 | -44.93364 | 2025-05-24 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 98318fc0-d0a4-3d76-a9ec-376e5f2abb44 | -6.21556 | -43.34154 | 2025-05-24 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 136784a9-3a3f-3258-be44-9b6a3093cbb0 | -5.21407 | -43.3115 | 2025-05-24 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5425a2b-d3fc-3733-a558-e09031f1229c | -8.07894 | -43.11522 | 2025-05-24 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 49cf0cae-8a38-304d-ae2d-2d6d5a0fefb4 | -10.49284 | -42.4184 | 2025-05-24 04:06:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 35c6870f-61e1-36ce-97c0-b5ee52dee4dd | -9.49104 | -40.34386 | 2025-05-24 04:06:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 832ee845-9958-320b-b2e9-dfe9c182fd8c | -8.75231 | -48.03333 | 2025-05-24 04:06:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3a17a21-ed64-3d59-be6d-5a0b02b9dd69 | -9.37901 | -48.40298 | 2025-05-24 04:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5759030e-f825-30d2-8c9d-af956d280f50 | -8.75517 | -48.04221 | 2025-05-24 04:06:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 958f82b1-50f9-3f55-839c-ca6849eacff5 | -10.49174 | -42.42539 | 2025-05-24 04:06:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 715fd49f-aed6-337a-bbe4-1e8777081045 | -5.34682 | -43.7479 | 2025-05-24 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 487d1bd8-77f2-371a-b602-b753ae600938 | -9.73077 | -45.42575 | 2025-05-24 04:06:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44f7328d-2d48-332c-94b8-0cf779d0bcd5 | -7.21073 | -43.12765 | 2025-05-24 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3f1bc287-c636-3219-bf4f-d863e08dd480 | -8.37254 | -47.09039 | 2025-05-24 04:06:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6f0d75c-4d1a-3584-b443-421e5a397326 | -10.3673 | -47.98997 | 2025-05-24 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| add9962a-5b04-3aba-b370-4f04b05ffafa | -11.56224 | -47.45145 | 2025-05-24 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f3ff1858-db1f-35ec-ad81-aef9cfac8c97 | -18.34528 | -45.59011 | 2025-05-24 04:08:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67fbca66-6ba6-3513-af86-fdbb1f18aa39 | -13.19057 | -53.58607 | 2025-05-24 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e66128d3-18f0-3551-89f3-360209212269 | -17.59327 | -43.20021 | 2025-05-24 04:08:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e8add59-1fb3-38d5-8286-9d6df6063d84 | -17.59716 | -43.19709 | 2025-05-24 04:08:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b588eaab-5197-35bc-8a65-a43298f507b5 | -12.40034 | -49.97981 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e59b78c8-fbf5-388d-8689-aad139b57dc7 | -10.72988 | -45.1554 | 2025-05-24 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d022d22c-7c43-3a7b-98b7-db84f56eaa0d | -12.13633 | -54.66422 | 2025-05-24 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16e0d432-e6f0-32b3-b0ef-38eea6e531ec | -12.13787 | -54.66813 | 2025-05-24 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1a9b3f1-505f-3260-9723-748929a3fa57 | -12.38555 | -49.98625 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 686dd73a-5936-3b32-8d7a-da76117afcd7 | -10.52688 | -47.58246 | 2025-05-24 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83635a62-b28c-3e8a-be8a-aabf42130efb | -14.2282 | -44.63411 | 2025-05-24 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 332f7f01-df17-3eca-9261-cd66064de067 | -13.47172 | -52.28397 | 2025-05-24 04:08:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd31d168-d26d-3443-ab4c-0c411469154a | -12.27627 | -44.59668 | 2025-05-24 04:08:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d836c925-5f73-34e6-8f15-d4d2d830fe35 | -13.15753 | -56.82133 | 2025-05-24 04:08:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cf0a8811-e562-36f2-be45-2f19bb8e2ba8 | -12.83647 | -47.39574 | 2025-05-24 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 359f0a6f-1f78-34a8-b9cc-33dc0d93fc0a | -14.03757 | -55.14252 | 2025-05-24 04:08:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06ae3a7f-d0a1-3531-bd87-a52963e3e2f0 | -14.22939 | -44.6268 | 2025-05-24 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0b29c21-3358-309d-acbc-c35ba9dcc605 | -11.57368 | -47.62006 | 2025-05-24 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ea25526-7b6f-3c88-9661-b804fc08a6ef | -16.61165 | -43.31881 | 2025-05-24 04:08:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55610101-0def-396d-a1fa-2f8e09a324df | -12.39945 | -49.98458 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f84cf0f2-2f47-3459-9e1e-5deecd76890a | -15.98227 | -47.01224 | 2025-05-24 04:08:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 147ee666-150a-3216-8096-9dc7a6de3fe5 | -12.83849 | -47.39222 | 2025-05-24 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 975876f0-bc94-3f02-b775-47a2bc6af5c2 | -14.01497 | -55.12726 | 2025-05-24 04:08:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7994ed21-29ac-3c90-b6dd-238f601c740e | -15.69919 | -42.25698 | 2025-05-24 04:08:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd549255-04be-3508-921b-b1b4b1c4a5cc | -10.36314 | -47.98921 | 2025-05-24 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3869123b-45da-30cf-b763-27268f9c422b | -11.5574 | -47.45585 | 2025-05-24 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 222ca82f-d554-3401-81fe-8b704960b851 | -12.38569 | -49.98204 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7dfd8053-20bd-36a2-be58-88dd8adce038 | -11.56134 | -47.45657 | 2025-05-24 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c879a837-6395-39b3-9ed7-b0b860d99fb2 | -12.40742 | -42.52873 | 2025-05-24 04:08:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 29512cb2-2362-3129-a812-ab041920f9e9 | -10.94095 | -48.75215 | 2025-05-24 04:08:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bacca52-ae73-390a-9eec-c4768e9feee0 | -14.01188 | -55.14192 | 2025-05-24 04:08:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1046ef0-8843-389f-b411-0cbdf1c68d70 | -13.47212 | -52.284 | 2025-05-24 04:08:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ef3d40f-ba28-34b6-83e2-067bf0f83c61 | -10.46777 | -47.94064 | 2025-05-24 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b462b207-cba1-34dd-a6ea-b89d53dc4d59 | -12.37469 | -49.99006 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c9c9078-c5c8-3210-b485-b43d105cf3b8 | -17.12392 | -49.12206 | 2025-05-24 04:08:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b0e4c79a-c6ad-3504-bdc3-0a35ecf56f59 | -12.35395 | -49.92554 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b46554ba-82dd-36a1-ba7f-4668f46c0889 | -14.06977 | -57.10866 | 2025-05-24 04:08:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75f2940f-718b-36d8-ae53-18172618773a | -12.38008 | -49.9903 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfc3bfa4-e224-34b3-bc71-97affc70921c | -12.39119 | -49.97805 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9d618a6-e3d1-33d5-b401-c01966834b64 | -13.47239 | -52.28063 | 2025-05-24 04:08:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3fff974-fc95-394c-840f-e5445f46a7ff | -12.38387 | -49.99176 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b41fce29-ab16-317a-94dc-7320e4f5fc87 | -11.7568 | -54.22409 | 2025-05-24 04:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| af1056a0-a536-330a-8703-67f622c74879 | -14.67374 | -48.1107 | 2025-05-24 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca45a534-eeb2-30b0-b166-36ceab65e7d0 | -11.7945 | -44.28189 | 2025-05-24 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66af5375-34bc-3ff5-a5aa-de246e02626a | -15.83069 | -41.82469 | 2025-05-24 04:08:00 | NOAA-20 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2422727-85b4-3f4b-a27d-def750d197a9 | -15.62754 | -57.30583 | 2025-05-24 04:08:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93419df2-8b23-344c-ab08-7df975f6da36 | -11.75586 | -54.22886 | 2025-05-24 04:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 366f60f0-c57a-3c93-be0b-f35cb7bb354d | -15.62825 | -57.30602 | 2025-05-24 04:08:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82737429-1de4-381e-8226-b21f30986c60 | -12.40411 | -42.52819 | 2025-05-24 04:08:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 87b9ded6-282b-364d-89af-a39f064b7051 | -13.18564 | -53.58097 | 2025-05-24 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5cbee82d-4621-3e85-9dff-b3475460f6bc | -10.72921 | -45.15935 | 2025-05-24 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fb2ad6a-f2f5-3a3e-881c-b19ecc7cad1a | -13.47276 | -52.28064 | 2025-05-24 04:08:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb72e660-837d-353c-8a5d-aa1186608e6c | -14.67783 | -52.4399 | 2025-05-24 04:08:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a655a06-8009-3e8e-ad81-c9166ae2e86c | -13.15222 | -56.81707 | 2025-05-24 04:08:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| af21a991-aba8-3fc6-99da-6b4a59556a4c | -16.30281 | -42.77084 | 2025-05-24 04:08:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b41a0d4-3353-39ef-8273-08ea501640ba | -12.38019 | -49.98605 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4040084-bbe7-3722-8e6f-1d217d9e99e1 | -11.38875 | -47.96215 | 2025-05-24 04:08:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63a10a86-86af-3470-a914-0498ebde12fc | -13.1385 | -56.81372 | 2025-05-24 04:08:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66cc1d59-ecd3-39c8-a7a6-71942dbd05c1 | -13.67256 | -53.93913 | 2025-05-24 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2876b2ac-b0b2-3572-bc92-223422285117 | -13.58186 | -47.35019 | 2025-05-24 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0929f362-2a12-3cb8-8ae1-03369bf8ffc3 | -13.98624 | -56.02226 | 2025-05-24 04:08:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41390d5d-4c51-3f91-8bc5-b309227ca21d | -11.57429 | -47.61655 | 2025-05-24 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 345c8f90-88c0-3df3-b656-9abe45eb3d4a | -10.72072 | -52.47516 | 2025-05-24 04:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8314c3d6-e6cc-38a1-8581-8fdd448b5903 | -13.15062 | -56.81989 | 2025-05-24 04:08:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1adc6d04-7082-3473-b70d-5f93028f56dd | -11.74885 | -54.23222 | 2025-05-24 04:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 506dc496-c629-300e-a17a-0c7d122408fa | -10.46509 | -47.94426 | 2025-05-24 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eaedf89d-24ff-36d1-a896-b75a73454500 | -10.46574 | -47.94048 | 2025-05-24 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| afdc757c-acae-3e64-bd82-e114daf26ce4 | -13.78274 | -54.3134 | 2025-05-24 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b0600004-44b9-3bf1-9d12-faed729afee2 | -12.38479 | -49.98686 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 275c7032-d7d4-3d24-b326-c1c50e639fa2 | -13.68912 | -45.26383 | 2025-05-24 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62ac5b0d-33a3-3c15-baba-ff4455dd813c | -11.76188 | -54.23042 | 2025-05-24 04:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 04fb2dc0-4347-304f-9709-d7a6931618e8 | -12.06683 | -47.3527 | 2025-05-24 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c1b9011-8ac2-3b5b-9ff9-4125022111fd | -12.40798 | -42.5252 | 2025-05-24 04:08:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 131800ae-1533-3f95-8ca6-2332fb498945 | -11.42358 | -54.30666 | 2025-05-24 04:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58309496-6a7b-3ab0-a429-1078d6d7b24d | -16.67963 | -43.88373 | 2025-05-24 04:08:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README10.md)
