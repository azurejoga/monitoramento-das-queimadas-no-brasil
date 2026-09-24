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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bea49dab-c5cd-396a-89c9-3fd5761f98da | -2.62637 | -51.70245 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7236d711-f532-3400-855c-9ec08bc7b6ea | -9.2369 | -47.35717 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ca5d0109-1480-30f7-819e-39733c433fc2 | -6.685 | -55.0577 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ae480b8-c880-3303-9ef6-19d23eecdf1e | -6.26776 | -55.45831 | 2026-09-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f22dc93a-b375-3bcd-8a0d-7c3f4bdf5f84 | -2.28469 | -56.67374 | 2026-09-24 05:04:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 04f7bb10-9363-322c-9eac-bab7b4731566 | -8.26465 | -54.78065 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53f631c4-fad3-3afb-aa0b-11144137bac6 | -6.10161 | -57.67132 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38c636ba-71f4-38a0-8bb6-c69beeab97ba | -8.08688 | -54.76619 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a08a3916-48ce-31ad-b293-8c43f523b4cd | -3.79178 | -49.02952 | 2026-09-24 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a86d1d31-b401-3964-b073-ec8946f3f227 | -6.40676 | -46.20242 | 2026-09-24 05:04:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20495075-55a3-390c-a99f-b04a97c06fa4 | -6.19211 | -57.78118 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| beeebe1b-4967-311b-ba68-06815f36f395 | -7.58445 | -57.66256 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 186eda6c-5b86-3d69-a5de-698e8298dc3b | -8.2474 | -54.78112 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bf1c8d5-3e7b-3ef7-b248-c23c7fe810f8 | -4.99468 | -45.55195 | 2026-09-24 05:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0229c4d0-0280-36ea-96ba-971abd083fb8 | -7.04241 | -62.93889 | 2026-09-24 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fff13ddb-0ec3-3d35-b89e-7612e3f8a5e5 | -6.88646 | -55.56139 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f34199d0-5f53-30d7-848c-c34f4e6336ad | -4.49892 | -54.96004 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cecceac7-008e-3576-990d-b5037f48df74 | -10.08963 | -46.06001 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 23ac9459-8070-3d55-85c6-0e73d85bc5f8 | -3.4456 | -50.0874 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea552cd2-fcb9-3ae2-a310-38c59c4344b3 | -3.56724 | -59.45592 | 2026-09-24 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4976785a-5d96-3fc3-bbd2-7dc6133a318b | -3.00336 | -54.17373 | 2026-09-24 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d6028b0-9a5c-3c56-87b0-4e09fc3fc924 | -4.44416 | -55.06699 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b332daf7-d44f-3256-ac0f-9fce984b5192 | -6.85739 | -57.65623 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14cf3720-0bbe-339e-b488-7e68926f81f6 | -6.64488 | -50.93833 | 2026-09-24 05:04:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96d46485-59be-3b46-80d9-c771b20e6ea7 | -6.31505 | -52.67393 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cab67d93-a049-3767-a9d3-84886935043b | -7.38345 | -55.19464 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e7a58c0-b376-3120-ae26-21a263c029b2 | -7.26955 | -45.53388 | 2026-09-24 05:04:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51db7529-d613-33ba-9f4c-ae5ce9ac5cf1 | -2.9746 | -50.39716 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfb82502-815d-3c05-b1be-281ce70d7737 | -7.89197 | -54.73124 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de87afaf-61a6-3180-a618-51d7fab2a6b6 | -3.85481 | -58.88913 | 2026-09-24 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9c523f3b-7a02-3802-9587-4b0e7bac1357 | -1.79432 | -53.74212 | 2026-09-24 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77042e48-7be5-3c89-892d-eb41887a2e8c | -6.34335 | -57.77376 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aacd6fb2-fdc2-32c3-8273-5f74e0badbb1 | -6.43617 | -59.96481 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 794eb9fd-831b-3cad-a0c0-e01057c59eec | -6.65679 | -55.06393 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79f0b73a-7258-333c-a985-fd68e8d01bc1 | -6.61275 | -59.91691 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fe87db9f-596c-31a3-8ecd-215613c9a425 | -3.71953 | -55.9726 | 2026-09-24 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2ee3551-aee0-3e10-b90c-fe58cd1316b0 | -6.01432 | -59.94337 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| afd4cb62-2bd1-3806-a722-0a42c481efa1 | -4.88813 | -55.97083 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92b12b18-0df7-343e-9f0c-3b7324922c3a | -5.11055 | -60.25911 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f2e77189-f3a9-3f70-8527-13b903d3c219 | -10.13931 | -45.54038 | 2026-09-24 05:04:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95935d1f-605b-3eb6-82c8-5f47b61452fa | -8.28283 | -54.75151 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22527e38-23d9-3a2d-90a9-9141abfe76cd | -3.55314 | -43.46819 | 2026-09-24 05:04:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5e252a1e-1efc-3fe0-be45-14c29f6ed5ff | -6.13179 | -59.96705 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7a43c5d-5402-32fa-ad25-15b12bd88d4c | -2.14528 | -50.89978 | 2026-09-24 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75ac4c0d-4719-3b7d-a1cb-92c60674a4bd | -5.17708 | -56.18008 | 2026-09-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f155432-b502-35f0-af5d-1865e8473f8d | -3.06702 | -54.39297 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea5de748-4956-3916-8d9a-652a3902cc77 | -8.27291 | -54.77129 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77fd2d1b-9bf7-36c4-a9f5-7916d927691c | -7.56017 | -55.02311 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11cf8e5a-2c23-34ab-b35a-f68714ceb7dd | -5.83906 | -53.85849 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0696aa3e-538e-3f57-91e9-9d481688c239 | -3.7076 | -54.21027 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce1eddb1-99af-33e1-9e4f-02fbb10305e9 | -9.74878 | -48.34931 | 2026-09-24 05:04:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 93ef7347-952f-321e-bac6-a06c12ff9cc6 | -3.57712 | -51.55907 | 2026-09-24 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a3c2627-e910-3232-a727-385b5fb726c6 | -1.27589 | -57.03136 | 2026-09-24 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63014453-98f9-34d6-8dca-4eaaa4c1e859 | -5.84723 | -57.62343 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17610d01-0282-3360-9bf0-f2bcb29c07da | -5.82043 | -47.75978 | 2026-09-24 05:04:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f5ff204-2689-3e60-8344-4095990487ae | -3.07477 | -54.38704 | 2026-09-24 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0513cd5-96b4-39f4-9a75-45d5dbd1f2d5 | -3.76605 | -60.72194 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 122d59c4-5ec1-3e6f-9137-7429b65f405a | -6.67413 | -58.57077 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff8d2e66-1791-3e47-ba8c-199daf45ffca | -9.23327 | -47.35518 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 617d9467-6dc4-3251-a6d4-76c7fbc0d320 | -7.01172 | -55.41502 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| beb099a3-3c2c-320b-8e19-5243c63ef0c9 | -6.6357 | -59.93255 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 840e55a1-328f-375a-822e-229843bb8dbb | -2.8817 | -54.08337 | 2026-09-24 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0931be0f-65d1-34f6-ad9c-c2b891052122 | -4.33611 | -55.21374 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 828bd32e-a74b-35d4-845b-3cfae66dfd51 | -5.91987 | -59.91205 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f616309d-eb80-3bed-87e2-2c72b8754df1 | -3.55076 | -59.95036 | 2026-09-24 05:04:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc76c2ea-2e12-38e5-86e6-7b2d8e708815 | -6.63444 | -59.9401 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 89f33c49-8ae5-3e32-8931-1fb7c9bf5aee | -1.83679 | -54.71939 | 2026-09-24 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e593580-f8ae-39bb-aff5-fbf3e8f02cd0 | -6.6446 | -59.93025 | 2026-09-24 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02de41cb-e401-3806-908e-b1697a26067b | -3.72416 | -54.21287 | 2026-09-24 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0b2efe5-5da2-35a2-91ea-5bb92ca7acd3 | -6.21523 | -47.49731 | 2026-09-24 05:04:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1ce0de72-fbad-333d-bbae-6ee13a96e309 | -5.81655 | -57.74267 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f0626fc-9b7d-3b22-886b-e02d544c58cf | -8.08861 | -54.99059 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f376a60-a7ce-3370-8ad9-f304d25d504c | -6.52921 | -51.50408 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bd75ba4-4041-3da0-8d5a-85b740d3b97b | -2.14759 | -59.23544 | 2026-09-24 05:04:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0ad62ea-3836-380c-908d-342a009e2e6e | -8.4588 | -51.49422 | 2026-09-24 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b94f191e-1a8c-38e0-9177-0061635ef304 | -3.44397 | -50.07359 | 2026-09-24 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8768b9a7-b899-3dc8-9ac2-a03b70254d67 | -4.52945 | -54.97892 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce3c9230-9a35-3921-948b-24a80fc036b2 | -8.93006 | -45.9446 | 2026-09-24 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6637e78c-f465-346e-bfcc-e791ac5121b4 | -5.84359 | -57.62282 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4da18b5a-a1f1-330a-a4e0-3cf57cddb05f | -6.66196 | -50.94968 | 2026-09-24 05:04:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fe012396-607c-3cae-be93-c6947d2ba896 | -7.26909 | -45.53723 | 2026-09-24 05:04:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4f91bfa-c402-3e85-bcb8-2c089010d1e3 | -2.29741 | -47.8913 | 2026-09-24 05:04:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 491dd9a6-2d17-39d4-b6dd-228c90b33ae6 | -9.2381 | -47.35579 | 2026-09-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 547b45d2-266b-3799-a45d-cac5371036ae | -3.68051 | -60.55754 | 2026-09-24 05:04:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18282b16-9397-3476-980c-a33a5301dbd1 | -4.42239 | -55.07441 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6cf3ab87-b0eb-3c07-a6c4-882bcadf1809 | -3.21112 | -53.39799 | 2026-09-24 05:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57337033-ffa6-34f7-bcdc-d4fda97fa456 | -6.61498 | -59.92897 | 2026-09-24 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 828aadf9-4ff9-3177-9a6d-7482a791dc5f | -10.08469 | -46.05618 | 2026-09-24 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 062aaf38-d0a7-3ab5-928c-627a102d7f43 | -8.2718 | -54.75687 | 2026-09-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55c2e7e5-e4ba-3232-999f-9584f4fe6823 | -6.48709 | -57.8785 | 2026-09-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79b788a5-159f-35e4-96b9-07dffed8cf9a | -5.2604 | -49.22631 | 2026-09-24 05:04:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0c03939-c904-320f-86d9-40791dde06a6 | -7.04797 | -62.93687 | 2026-09-24 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7d91bb7-a7b7-35f5-abca-6c09ab6c5776 | -3.00685 | -51.53579 | 2026-09-24 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0d8b8df-906c-3629-9b24-a6220bd227c4 | -1.92009 | -58.26853 | 2026-09-24 05:04:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 104e3a59-dc67-3154-8bc9-ae66bd6fdbb8 | -7.32676 | -55.59189 | 2026-09-24 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d40a1fca-c565-37e4-86b6-c34aa24fed11 | -2.39167 | -48.52199 | 2026-09-24 05:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d3d35db-ef6a-3ce8-9e9a-5651b2f5af34 | -2.4509 | -49.21805 | 2026-09-24 05:04:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33b5df08-ddaa-3781-bf52-2350aa4ed23d | -6.35993 | -58.29071 | 2026-09-24 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6e90c16-f1f8-3261-80de-595038cddea8 | -4.48975 | -55.56897 | 2026-09-24 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ba02818-2a84-3a8f-995a-4c3ed492f0eb | -6.05428 | -53.28782 | 2026-09-24 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README67.md)
