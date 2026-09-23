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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0a9b609-1d8b-3b00-875f-a74e9a561b5d | -6.6115 | -59.95024 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 927e0169-96a6-3d0d-be79-dde7052af3ec | -5.97938 | -55.37419 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad5cd29e-ed6e-3810-a79d-a0ebbf1abcd6 | -6.46491 | -59.97412 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e18a9904-0de8-3fed-ad5e-72d5a8e27923 | -7.42995 | -49.85528 | 2026-09-23 05:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17135bb2-324b-3a7f-a482-e02f67ba4152 | -6.64643 | -59.92356 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5598c320-3d0c-38aa-93d1-f095bda1ce7f | -6.67934 | -58.5569 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58928efc-a0ba-34fc-873c-68b6c08f7e6e | -5.92693 | -59.91675 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d89ea0e9-d72d-3183-9de6-e04a3a750b21 | -6.09278 | -57.70571 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cec35821-d2ac-368c-bf83-ba5eef0a660f | -6.61431 | -59.91126 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| afec46c3-ac72-38c2-915f-958dddd0cfc5 | -6.73445 | -55.08294 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 848f91d4-c55b-3fd7-b2c6-0f3fb64e344d | -6.30325 | -57.74909 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 821cc9e0-001d-3f26-8eaa-eb1a36683d1b | -13.92184 | -47.83687 | 2026-09-23 05:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 02dd1a7b-3592-3c75-86f4-dcf41ee8ae49 | -6.08941 | -57.70518 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07778e45-b9bc-3bf4-a294-56c5373658ba | -6.44162 | -59.97039 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6dbfabe1-5b0b-365d-9d09-552f058576ff | -6.67413 | -55.06903 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| db1b4048-f69a-3de9-a669-5a2a19275b46 | -5.80651 | -57.73913 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04104089-3ca2-3b68-8287-c7b1dfe74980 | -7.33273 | -55.59916 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae597f37-49d0-30ea-ab68-2ef63007728c | -5.81574 | -57.73607 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b31a30b9-c53b-334f-bebc-07070f858d00 | -6.63867 | -59.92949 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 498e97fe-4395-3842-85ec-332fd8546354 | -6.1241 | -59.93704 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d830558d-815c-3536-8406-5096699e7310 | -6.16411 | -57.72421 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3facc9d2-e6a1-36cd-8944-777ab0db60cf | -6.15795 | -59.93888 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a151dcf-0bf8-3a76-b0a5-acb7a001c02e | -7.1506 | -48.4457 | 2026-09-23 05:25:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5ae59c59-f93d-3ed3-a4d2-776b12b71237 | -6.08376 | -57.63049 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 57a6a72e-2ada-3f27-b5a1-5ce9e4780687 | -5.28093 | -60.19818 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fe53eb3-3f39-3fd7-98df-41f6d508dc43 | -6.64311 | -59.92304 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9faee59-34c9-3288-a495-d51b5801fcf9 | -6.31001 | -60.01025 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c30a5570-a1a9-3f38-9c6f-0ebf9e3cb92f | -6.358 | -58.29103 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10c48547-2b3c-38f5-b259-16da42b9b48c | -6.19614 | -57.78421 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60bf1400-5423-3eb7-ab50-041bd28320cd | -5.86113 | -60.16302 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2def8bf-c59d-3477-8f82-cb68187b5416 | -8.17386 | -54.78308 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60e39c1b-105a-304f-9db6-6d2dade294a3 | -6.10007 | -57.6811 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0688c364-4851-326c-9a56-6a0da0c1dc98 | -6.30065 | -59.94043 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5045f5f3-3c3a-3e60-8a0b-38d91754177b | -6.35467 | -58.29051 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91d52200-2c1a-39e7-8714-b1b3bc2095ae | -8.19964 | -54.71856 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| eb2fc53a-df75-38e0-a970-0f59a780cbff | -8.45692 | -51.48375 | 2026-09-23 05:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21f77612-9c45-3079-8793-a24537ba3680 | -6.62054 | -57.981 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 268a9dc3-9dca-345c-932a-84e9d2f2aa09 | -8.24157 | -55.24189 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4ee2896-6ce7-30bc-b90e-a0d2f37ee719 | -7.43129 | -49.84539 | 2026-09-23 05:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76e0d7f5-0775-373a-abbd-04ea564480ea | -5.66876 | -60.23404 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 956046aa-3ab9-3d78-b16b-e1af4653d93e | -5.86387 | -60.15965 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ec5513a-2b59-3ed5-88e5-792fd3be6c17 | -6.14243 | -59.92919 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6178245-f98a-3609-8202-0e810f3475e1 | -6.30099 | -57.74138 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22c23ea4-ca46-3134-aa83-2cfb0d248692 | -6.61596 | -59.92227 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| cc457f94-959e-3847-8aee-3b998a747836 | -6.34887 | -57.77773 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f347fb8f-4881-3a03-aba9-2a15bb1e0ce6 | -6.00641 | -57.82797 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42842e80-27f6-3195-a99d-5685ffe5a9f4 | -6.08435 | -57.69339 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d92b523-ca83-3d53-b5b4-dc40ccc1d15d | -7.77909 | -50.2305 | 2026-09-23 05:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 551e44f1-8d9e-3c99-88ec-566edc9f94f2 | -6.62334 | -57.98509 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12bf799e-bc01-376b-8d55-924640e4947f | -6.30548 | -57.73473 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f8e2f4b-fe9b-3847-9ec1-dd468cf174a9 | -6.67794 | -55.06961 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fc33890-9fe3-3fc3-9965-336406ab46e8 | -6.61652 | -59.91878 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| fac59d9a-b5a8-39f5-bf4e-b6ab5b786afa | -6.6716 | -58.56284 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65f59ada-460d-381e-92db-ae07b0f4dd24 | -6.00082 | -57.70997 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cf46f32-7023-326e-a936-e42fc06071d6 | -6.63479 | -59.93245 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 20.6 |
| de28fda6-fd9a-3a9b-97b8-f2509f0c7dc2 | -6.67547 | -58.55987 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f883777-0e81-3d73-a4c8-9c56eb7758cf | -6.35632 | -58.27999 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86b2374f-57c0-3fab-886e-b6d4caec2e7a | -8.08526 | -54.94827 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c06fd65-8f36-32fa-9fe0-14be9b3eb678 | -6.61929 | -59.9228 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1a585b3b-b9e3-3d57-8b76-93031dfb4af4 | -6.66387 | -58.56876 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d86aec6e-2608-3d99-9f58-bbd711f2e007 | -6.66773 | -58.5658 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfbba74a-fe62-3ede-abe6-e4510419bf30 | -6.61038 | -59.95724 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd037f9d-61f8-3ebf-9758-9773064eb972 | -5.45582 | -60.14165 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a8e73b4-ec8b-3845-8b8e-1cbb35112fb0 | -6.61426 | -59.95426 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ff47a4e-60ff-3371-a926-5caadeb1c56e | -7.60715 | -57.6078 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb38dbf3-fdde-3fda-8798-bb1c9ffefad4 | -6.42432 | -59.97449 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d19ad09d-d5aa-3182-89b3-0a291bebf754 | -7.32638 | -55.60134 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d3fb00e6-42bd-3b9d-97e5-7d60d08ad355 | -7.02967 | -59.50082 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 536d27c2-5d49-33f2-b0ca-3b680fbeadfa | -6.14027 | -59.9001 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 760d89a0-1420-335c-8f40-193af5255f6b | -8.82593 | -45.93003 | 2026-09-23 05:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5b95ed21-f3df-35fa-ae62-3d503f4dcc61 | -7.32704 | -55.59679 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 643d0fc0-f031-3a64-92d4-b5dd8e03cdfb | -5.45803 | -60.14929 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed4bd4d7-8013-39f0-b662-4388e78deebf | -8.27585 | -54.76857 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1b59fccc-8dcb-393a-b66a-b7916248cc07 | -6.67492 | -58.56336 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb45e0d8-71b1-3e74-8248-7cc3c5bfeec2 | -6.44654 | -60.00353 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b48cdcf2-8626-311c-9761-330deb72ae19 | -7.58446 | -57.66476 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc20c297-5dbe-3559-8de6-28470657dc8a | -7.13797 | -48.4305 | 2026-09-23 05:25:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b70cd2a1-ff3f-3749-8c87-29167a9e7f49 | -8.30686 | -54.77851 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbbe036b-ceab-388a-b174-21f0cb9050b7 | -6.67106 | -58.56633 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac101074-59ce-34c4-944d-0dd6b9b89b3e | -6.68318 | -55.06058 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6e80747-c6d6-38a6-9ee3-9fbe419c6467 | -7.29364 | -59.52841 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 869fc48e-8c55-3b7e-851f-c08cddaa78bb | -7.23128 | -56.41882 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfda5da3-ff27-3ded-a742-df2dcc55c0e3 | -6.09163 | -57.62433 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6503a1d7-2b11-369d-8cc8-bc036417e096 | -6.60705 | -59.95671 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e05d1070-326b-3f9b-b65a-913daf2702ac | -8.83499 | -50.48661 | 2026-09-23 05:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28f74ca5-c92f-3914-9afd-344ee0cfee68 | -7.55904 | -57.66879 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35289b79-2138-399c-a2e0-c50694ae58a7 | -7.5714 | -57.65897 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b687bca3-d983-350a-b3f3-760057771dda | -5.14483 | -60.30519 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbaac23e-330e-3859-ba52-42fc713fa93a | -8.27906 | -54.77434 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 65ba3600-0b9b-3140-9b01-97cde174c82e | -6.30773 | -57.74243 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fed625b4-5db6-3281-9bdc-8f76765109f6 | -6.09726 | -57.67699 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 24246337-f434-30a8-903b-cac0e7eb362f | -6.45212 | -55.00142 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3611dd50-be2f-3c37-804b-7d8acca4388b | -5.98231 | -57.69609 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60c70b1e-ec03-3511-a862-6016215ef2ee | -6.67554 | -55.05948 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5392b7ee-fef0-3f42-b737-b8c1aa66478f | -6.62758 | -59.93489 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| c54f0d4c-ec26-3470-8bee-5d18ac1c0f51 | -6.34776 | -59.96225 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4cdcac8-17a9-3c7a-b748-b68b3b441803 | -6.4494 | -59.96443 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28916d6c-75dc-307a-a7f9-12ae77982077 | -6.12644 | -57.75497 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c12c5295-95ab-3471-950c-202a5814d592 | -6.70205 | -59.95787 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 915eba6a-55f7-381c-ab3f-c901c6bd48f5 | -6.60982 | -59.96074 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README118.md)
