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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1e490b7-8935-333a-be20-cd983fa93fdb | -6.86842 | -46.01493 | 2026-07-30 00:16:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 2164fda5-6712-379f-9fc8-0b7e5de1adad | -9.22473 | -50.10435 | 2026-07-30 00:16:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3d343944-dddb-35bd-a32d-ead2fe606a1e | -7.34121 | -45.85533 | 2026-07-30 00:16:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 87000a13-bfef-385b-98bb-8a3b23e633cf | -6.86482 | -46.02272 | 2026-07-30 00:16:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 3e2d80f1-6153-3b8f-86ac-1c18724c1f40 | -4.3751 | -47.7752 | 2026-07-30 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 62b618f0-e63f-30ad-81ed-48df59562d28 | -5.75281 | -51.71257 | 2026-07-30 00:18:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| a66482a1-05d6-31e8-8f9e-d5cb08a3c616 | -6.65408 | -59.09634 | 2026-07-30 00:18:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 060ac98d-b6c9-373f-a5c2-ba50c96edd42 | -6.65705 | -59.11919 | 2026-07-30 00:18:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 68d92252-2537-358f-b764-d78561507ff6 | -4.37298 | -47.76103 | 2026-07-30 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 7ffecd2f-085c-3aa6-a801-c3a8b351d481 | -3.17879 | -48.02076 | 2026-07-30 00:18:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| adaf1e13-2b71-369f-89b6-9e1db9ca2e32 | -5.23506 | -56.00933 | 2026-07-30 00:18:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| ed5d0062-f1f2-3efb-a1ad-b15486dce5a6 | -6.64989 | -59.11347 | 2026-07-30 00:18:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 0090a19a-7945-3791-87cc-32dde2b15259 | -3.18081 | -48.03492 | 2026-07-30 00:18:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 72e5d89a-2300-31e5-8bfd-4d01e807450e | -6.66363 | -59.11183 | 2026-07-30 00:18:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 8d805b74-3e65-3201-bceb-618f9c038534 | -5.75159 | -51.70374 | 2026-07-30 00:18:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 33832864-33c1-3784-9c2e-77ef2f1356b9 | -2.58618 | -55.16431 | 2026-07-30 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 19d8b03e-a48b-34d1-a89b-dffa2ee013cd | -4.37197 | -47.76769 | 2026-07-30 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 1c9db0c1-afe0-3b5e-a966-1ba932eec92e | -2.58758 | -55.17458 | 2026-07-30 00:18:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| fb122ef3-bff6-3336-a7f0-0466128b039b | -9.6136 | -47.7508 | 2026-07-30 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| f06931fe-8bda-3340-b31d-f4908f62ef56 | -9.6133 | -47.7728 | 2026-07-30 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 9415d913-9be6-3556-85ef-43477b5e8fd9 | -14.1797 | -43.9875 | 2026-07-30 00:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| b2fb3dfd-55e0-3378-90e5-0a484c8318f0 | -9.6133 | -47.7728 | 2026-07-30 00:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| d7d1da0a-0395-334c-8091-1c95cbb62c30 | -9.6136 | -47.7508 | 2026-07-30 00:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 28b0ac84-ddcc-3150-b755-b1c7f1244ea3 | -18.2374 | -42.21 | 2026-07-30 00:30:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.9 |
| 9decaf49-e433-3c39-a37c-26f3740c08a5 | -9.6133 | -47.7728 | 2026-07-30 00:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 33d1323c-1e2b-3243-9f13-7b3c73d7ef19 | -9.6136 | -47.7508 | 2026-07-30 00:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 4335e77b-ed96-335a-a1c5-714e6406a009 | -18.2381 | -42.1849 | 2026-07-30 00:50:00 | GOES-19 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.7 |
| acb70419-6794-3d2a-a546-f8bda1dd1c34 | -18.2374 | -42.21 | 2026-07-30 00:50:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.6 |
| bae40fd4-877b-364d-b4cd-510394a0a525 | -9.6133 | -47.7728 | 2026-07-30 00:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| adeca93f-5971-3938-9e8a-04d879fdce9e | -9.6136 | -47.7508 | 2026-07-30 00:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 6194445d-2159-34a9-9fdc-c0571ba4d78b | -9.6136 | -47.7508 | 2026-07-30 01:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 3daf053c-7d3d-3950-8e9d-1ccf0bc0cb2b | -9.6133 | -47.7728 | 2026-07-30 01:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 08191e4f-8d31-3c61-88f0-42dc5e1377af | -11.9296 | -43.4288 | 2026-07-30 01:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 36163db2-207c-304b-9617-e92561e5fec1 | -9.6133 | -47.7728 | 2026-07-30 01:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 16d3c1dd-4cec-39fe-b315-da1f0c9589d2 | -18.2374 | -42.21 | 2026-07-30 01:10:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.4 |
| f143c0d6-c1bb-3190-b4cb-c5dd0209e168 | -9.6136 | -47.7508 | 2026-07-30 01:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 529bfb81-04a3-3361-8395-ed088ee31e29 | -11.9292 | -43.4526 | 2026-07-30 01:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 22082ecc-7f57-32fb-9a7e-6e708eef0d48 | -20.787901 | -57.869202 | 2026-07-30 01:12:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b943842a-3f8d-32b7-aeb7-05d543e15251 | -12.3746 | -63.444698 | 2026-07-30 01:12:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9f545b2c-fbf6-3d27-9c27-393ee5c1cfcf | -6.6577 | -59.107498 | 2026-07-30 01:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 482eb4df-3141-35f2-badd-3a2f91a504f5 | -21.807301 | -53.374901 | 2026-07-30 01:12:00 | METOP-B | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b3723bd5-561f-3167-9b71-e54ddf1ad140 | -6.6547 | -59.0951 | 2026-07-30 01:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f6512b31-c30b-3173-94c0-bbd14d4c7c40 | -12.3762 | -63.451698 | 2026-07-30 01:12:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 06603194-ca74-36ee-a83e-88d34cca908c | -8.827 | -66.7463 | 2026-07-30 01:12:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1464c399-9d76-3abd-868c-3ba1f19531c6 | -20.785601 | -57.859699 | 2026-07-30 01:12:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f0df92f6-715b-3b87-b46b-01a2cb1211b1 | -6.6479 | -59.109901 | 2026-07-30 01:12:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14af6654-0e35-3a31-901e-bdfa4d05ac39 | -9.9536 | -63.041599 | 2026-07-30 01:12:00 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bd4124b5-87e7-3e5f-b579-d4dc6f8e83e6 | -18.2374 | -42.21 | 2026-07-30 01:20:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.1 |
| 610c535f-2bd1-3084-b218-e6387313c77c | -13.3147 | -43.5986 | 2026-07-30 01:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| cf45c1a1-337f-3c2f-9a69-4d1f901d6aeb | -9.6133 | -47.7728 | 2026-07-30 01:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| c720589e-c0f3-3a5a-abde-0ceac9c4f721 | -11.9296 | -43.4288 | 2026-07-30 01:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| c2c63260-f156-3529-9870-1799b5af99d3 | -9.6136 | -47.7508 | 2026-07-30 01:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| bd2ff52d-f866-3a86-bccb-ab1a8ab4de95 | -9.6133 | -47.7728 | 2026-07-30 01:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 2d4e395a-648b-3697-8dcc-487f78bfb3ed | -9.6136 | -47.7508 | 2026-07-30 01:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 3631d406-2b01-3c22-a0a0-2103ffc21fbb | -18.2374 | -42.21 | 2026-07-30 01:30:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.0 |
| f183675b-e6b2-335a-98ac-3e7412ceff40 | -18.2171 | -42.2153 | 2026-07-30 01:30:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.5 |
| 82cf6d80-0d2d-31e0-9075-ae51dfa7dee1 | -9.9494 | -63.048401 | 2026-07-30 01:34:00 | METOP-C | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 80bca019-91b8-365d-aa02-05f976096a93 | -20.790199 | -57.870499 | 2026-07-30 01:34:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1af4f140-46ea-3b49-bd26-78018ecce2f0 | -21.812099 | -53.371899 | 2026-07-30 01:34:00 | METOP-C | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b6c6b71c-1d30-367a-861e-5beac31809a6 | -12.3767 | -63.4576 | 2026-07-30 01:34:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 32dd882b-07bd-356d-91b8-eedc1745bd3c | -21.8153 | -53.384602 | 2026-07-30 01:34:00 | METOP-C | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f0b2355d-955f-3efb-9d1e-ed9c0f9fb06c | -6.666 | -59.117599 | 2026-07-30 01:37:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee88f9a8-6240-386d-8fe1-1427403e398d | -8.8237 | -66.752701 | 2026-07-30 01:37:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9869d938-71e8-3b4f-afdf-252c5e682f8e | -6.6638 | -59.108299 | 2026-07-30 01:37:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1e2e94bf-6185-3c17-8122-a80d06ffe2e0 | -6.6616 | -59.098999 | 2026-07-30 01:37:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5abd326-3666-3c43-be39-58032fb1eeed | -6.6541 | -59.1106 | 2026-07-30 01:37:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| acea3913-ee30-3aae-b8dd-7050cdb20454 | -9.6136 | -47.7508 | 2026-07-30 01:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| e2e00236-146e-3e02-98d5-eb067236dcb1 | -18.2171 | -42.2153 | 2026-07-30 01:40:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.7 |
| a5f88520-85a1-3be0-a310-0c4073ee7246 | -9.6133 | -47.7728 | 2026-07-30 01:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 7df0a50f-ccac-3590-926c-08d49b013e77 | -18.2374 | -42.21 | 2026-07-30 01:40:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.0 |
| ea4e7554-f6ef-3328-88b9-919425c42245 | -18.2381 | -42.1849 | 2026-07-30 01:50:00 | GOES-19 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.7 |
| 97a1e9dc-1f4f-389c-b949-853ae5b23858 | -18.2374 | -42.21 | 2026-07-30 01:50:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.6 |
| e80de49b-7dc9-3d99-8240-6f1fc4f4d6bf | -8.85691 | -71.28851 | 2026-07-30 01:54:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 032c3b4c-328e-3c5d-9163-5ab1e023a13a | -13.3147 | -43.5986 | 2026-07-30 02:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 9785e307-24b7-3e3e-a170-8d1a0f97037f | -18.2171 | -42.2153 | 2026-07-30 02:00:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.4 |
| d255a6fe-418a-3a2c-b8e3-cd31a29ffc63 | -18.2374 | -42.21 | 2026-07-30 02:00:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 123.2 |
| a7362aaa-a30b-3eb6-a7da-d6e20ee315b0 | -18.2381 | -42.1849 | 2026-07-30 02:00:00 | GOES-19 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.4 |
| 5e476e3f-65ae-3c1f-8fae-102de970f439 | -18.2381 | -42.1849 | 2026-07-30 02:10:00 | GOES-19 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.5 |
| 79320123-4b2b-382d-b7b2-44b1b4096efe | -18.2374 | -42.21 | 2026-07-30 02:10:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 177.4 |
| cdf112a1-0a0f-3683-bb0b-da6e8ee037e2 | -6.6559 | -59.1174 | 2026-07-30 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 6dbc1b6d-d527-35a9-a261-b4dfde5208de | -18.2171 | -42.2153 | 2026-07-30 02:10:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.9 |
| e04d01b5-b67f-3350-9429-51481f100951 | -18.2381 | -42.1849 | 2026-07-30 02:20:00 | GOES-19 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.9 |
| 3183eb30-a551-3a67-b667-861c01539660 | -18.2374 | -42.21 | 2026-07-30 02:20:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 164.2 |
| f908b520-5356-3677-b8a0-eadd5fba29e6 | -18.2374 | -42.21 | 2026-07-30 02:30:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.1 |
| ac73f1b5-4fab-3b3b-a2db-7c79b1ce2387 | -18.2381 | -42.1849 | 2026-07-30 02:30:00 | GOES-19 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.5 |
| 35afa1d0-1930-3379-ba05-8c00bb5428c6 | -18.2374 | -42.21 | 2026-07-30 02:40:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.3 |
| 30340099-075f-3b97-ac57-f3d05159df71 | -18.2374 | -42.21 | 2026-07-30 02:50:00 | GOES-19 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.1 |
| 71c38a2e-a47c-321f-ad7c-c1b659332c99 | -21.3518 | -44.8075 | 2026-07-30 03:00:00 | GOES-19 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.3 |
| cf0cef42-2675-36bb-82bc-33f0c63f9175 | -2.90237 | -40.3949 | 2026-07-30 03:15:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 31e1f4dd-97f3-3049-a81e-9146971e599a | -2.90882 | -40.39976 | 2026-07-30 03:15:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bc5aeb2d-20ad-3531-8b4d-805e7839d6aa | -2.90228 | -40.39869 | 2026-07-30 03:15:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2016fcf8-0111-3700-93ab-c209275fdf6d | -4.44644 | -37.92804 | 2026-07-30 03:15:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d4447b04-b6d7-3474-9867-d2f16e7c8034 | -5.90395 | -35.72655 | 2026-07-30 03:15:00 | NOAA-21 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 15.2 |
| ba4c3ca9-a1dc-37d8-9c9a-f5501a713fda | -5.1733 | -35.67444 | 2026-07-30 03:15:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| aebc4091-5801-3223-9736-c5d381f56eb2 | -5.50344 | -35.58599 | 2026-07-30 03:15:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bd502fe4-c692-3f5e-9de9-a9b6338f7faf | -5.90855 | -35.72723 | 2026-07-30 03:15:00 | NOAA-21 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 9520e9f4-d635-3531-a6a8-ae924c033e04 | -2.9089 | -40.39598 | 2026-07-30 03:15:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| db9cba6a-d2c5-3978-a614-e8fa186fcd59 | -10.93378 | -43.06205 | 2026-07-30 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 8e6f6530-ddab-39a0-9558-e5ab30f49270 | -6.23527 | -35.33633 | 2026-07-30 03:17:00 | NOAA-21 | JUNDIÁ | RIO GRANDE DO NORTE | Brasil | 2406155 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 70e368c3-1efc-315b-87f1-1420aed13f3c | -8.90264 | -37.97224 | 2026-07-30 03:17:00 | NOAA-21 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README3.md)
