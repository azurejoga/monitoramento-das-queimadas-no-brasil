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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d54812fe-aa0a-3961-897b-d4978c6d03a8 | -8.7936 | -36.87563 | 2026-10-07 15:16:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| faf03b52-0b1f-32ef-8cbf-e6956ae34f84 | -6.62996 | -37.88129 | 2026-10-07 15:16:00 | NOAA-20 | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 05868c31-46a1-3fec-8762-70ad1f4a8238 | -8.07411 | -38.23037 | 2026-10-07 15:16:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 261a842f-c76f-3920-969e-3dc2f4d6ff8c | -5.08359 | -37.60016 | 2026-10-07 15:18:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c6c097dd-74c9-3e2c-a3e4-59c6de08389d | -5.14679 | -37.35554 | 2026-10-07 15:18:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 98b6894d-57ff-307a-9a20-c46e3b22b8fb | -4.93559 | -38.84131 | 2026-10-07 15:18:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 26c893b9-eea5-3621-a853-81f55581e74b | -4.28016 | -39.54737 | 2026-10-07 15:18:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 397b3691-e2a3-3b82-b9c8-be6a7ffa7e80 | -3.94321 | -38.49429 | 2026-10-07 15:18:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| cacc7378-81b5-3776-9d1a-77a00dc0cb45 | -4.93646 | -38.84771 | 2026-10-07 15:18:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 34014d17-d0ff-30d4-9499-934b737f044b | -5.08432 | -37.60545 | 2026-10-07 15:18:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 71ee70fb-562c-3992-854e-53ed74346708 | -5.25148 | -37.57526 | 2026-10-07 15:18:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a1d7069b-efbe-3079-bae5-56ffed61511c | -4.27919 | -39.5403 | 2026-10-07 15:18:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 5277cc28-2244-3bfa-ae1c-75bd7cd2998a | -5.71403 | -37.70784 | 2026-10-07 15:18:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0821d4ac-18d6-3e46-87d8-8c214a2e287e | -4.74993 | -37.30444 | 2026-10-07 15:18:00 | NOAA-20 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d321bc84-f225-38f0-85aa-78597061c99e | -3.68443 | -38.81242 | 2026-10-07 15:18:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b089c00c-469c-3645-bba4-e6f8f89e70ac | -4.45344 | -38.65854 | 2026-10-07 15:18:00 | NOAA-20 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 56729995-0a4c-33c6-a69f-58a60883caef | -4.93589 | -38.84251 | 2026-10-07 15:18:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 15.9 |
| a6a4d546-86d0-3e68-a888-8dec4a20194f | -5.24059 | -37.5811 | 2026-10-07 15:18:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 71ff5279-bd56-3c77-abcb-bb701c89c558 | -5.76893 | -38.55368 | 2026-10-07 15:18:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 3fcfdf17-e06e-3d36-b5da-2d35afb724cf | -4.27621 | -39.54653 | 2026-10-07 15:18:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 18.2 |
| b26cf22f-7e75-3a33-b326-9c39ea40700a | -5.23965 | -38.54242 | 2026-10-07 15:18:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fdd12114-0be5-38bc-8634-0a343d0a6b3c | -4.45874 | -38.65931 | 2026-10-07 15:18:00 | NOAA-20 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 7c856435-ff4f-3783-aa34-1eccbd9d9279 | -5.7138 | -37.70707 | 2026-10-07 15:18:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e487d30f-81a1-347e-bb22-91a0dfc6c06a | -3.49423 | -39.49593 | 2026-10-07 15:18:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| fd031776-3a20-356d-9fe9-1763f7224bcf | -3.49516 | -39.50235 | 2026-10-07 15:18:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 7514114d-1d98-311e-b212-aac3ba2fb5c6 | -3.58353 | -39.14204 | 2026-10-07 15:18:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 20c5641b-b637-3b13-b56a-16b9f9490b78 | -3.65363 | -39.43561 | 2026-10-07 15:18:00 | NOAA-20 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1c31961d-7140-38ae-b78b-2518ac87dabc | -3.49269 | -39.50219 | 2026-10-07 15:18:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 26becf30-23a1-30de-838e-47309fd7d3cf | -3.56098 | -39.13237 | 2026-10-07 15:18:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1e194f5f-5ab2-36b7-90c9-cc5891b42a14 | -3.53107 | -39.50215 | 2026-10-07 15:18:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 79985d2d-bc7e-3398-b3f2-e01aa90f7cef | -3.58332 | -39.13894 | 2026-10-07 15:18:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| b57395ec-ed14-3f0d-acd9-11b87441d4cb | -3.49179 | -39.4957 | 2026-10-07 15:18:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| be0c4f06-7f2b-33c6-bcf1-092f15dea391 | -3.64875 | -39.43909 | 2026-10-07 15:18:00 | NOAA-20 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a7339e9f-3b80-32b0-9cf9-0922103c00a5 | -3.53569 | -39.50146 | 2026-10-07 15:18:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 563c4c81-9362-361a-8536-4619e88418e0 | -3.56087 | -39.12941 | 2026-10-07 15:18:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b1668f28-5530-34ac-b472-77b06f462d7c | -3.0264 | -57.4855 | 2026-10-07 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 8e9aa40a-119c-3a6e-84f6-0f76760704ae | -8.7866 | -47.5713 | 2026-10-07 15:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 68b075f9-5572-32b9-988e-745b50e4f86d | -12.2132 | -44.6991 | 2026-10-07 15:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 363.4 |
| f0ff5c6b-4ef6-33d7-86ee-569bd907c2ca | -3.0192 | -53.887 | 2026-10-07 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 9f61130e-5a07-3df0-84e7-62ec1c5bca01 | -8.6106 | -67.0486 | 2026-10-07 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 26ad425c-7a04-33fe-8627-694ecb8496c3 | -7.1813 | -55.1237 | 2026-10-07 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| cd3d5762-6356-327f-aafd-87d00f4b5248 | -9.1363 | -65.2835 | 2026-10-07 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 02b7e834-ee80-3048-8b13-14f01a35f5c1 | -3.063 | -57.5236 | 2026-10-07 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 160.7 |
| 1dfa2241-138b-3b6b-adae-5a4f08a2c5e5 | -3.4944 | -54.6167 | 2026-10-07 15:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 5125de1d-fcda-35b5-b93b-61328f343251 | -3.0992 | -57.6589 | 2026-10-07 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 1c9afa6f-e390-301f-a5eb-f62a3aa0c5d8 | -9.0612 | -65.4916 | 2026-10-07 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 0dd5e99c-cc01-3d8b-a18e-e037e2facec3 | -2.4428 | -56.5399 | 2026-10-07 15:20:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| f0bc4e70-9aac-37ab-a807-bc6d2d2ec012 | -11.1051 | -45.689 | 2026-10-07 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 53373f39-7228-3a00-80e6-b7eedb8897d5 | -3.3134 | -53.8592 | 2026-10-07 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 169.0 |
| cabcd4c0-4a31-38bb-bbfc-8ee4af557184 | -3.0373 | -53.9469 | 2026-10-07 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| fd3b4d19-6846-31c1-aa86-0540e0650a51 | -3.0915 | -54.2469 | 2026-10-07 15:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| fed001b2-553c-3974-9204-1a2373dcfcab | -5.6932 | -53.487 | 2026-10-07 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 134.2 |
| a47b2d17-bec3-3e6f-9a4a-b5c24e65c7cb | -6.4568 | -55.4609 | 2026-10-07 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 6c53b473-b46e-353e-970f-38874d4d58de | -12.2048 | -48.4319 | 2026-10-07 15:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| e2576c48-c696-38f6-b433-1bcb47793e21 | -8.2623 | -54.6969 | 2026-10-07 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 8929be76-3f04-36ae-ad68-fa884900a57b | -2.3889 | -56.1285 | 2026-10-07 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 45d810a4-a3b3-3145-a024-5062546e34ac | -3.9843 | -56.2099 | 2026-10-07 15:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| f20cce46-bb3d-3d4c-992c-fb882f625eb0 | -6.4756 | -52.8142 | 2026-10-07 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| f1798b92-5b38-3656-9d13-500cfae6e068 | -9.1542 | -65.4138 | 2026-10-07 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 0376ff0e-07a5-39fd-b5ae-38230de00104 | -3.476 | -54.6172 | 2026-10-07 15:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 5bd6b46a-56a3-33d5-b566-72ba907c8ec1 | -4.1367 | -54.917 | 2026-10-07 15:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| b1282871-b615-317a-b220-b83510b992c2 | -5.9587 | -55.3448 | 2026-10-07 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 2f68a7c7-758f-3ead-9245-65bed936e7f7 | -2.9327 | -58.3204 | 2026-10-07 15:20:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 2214f11a-652f-3f05-9ea3-403555450af5 | -1.2639 | -49.0618 | 2026-10-07 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 67619b7a-9779-38d2-b9c1-958db03d5851 | -3.2945 | -54.0006 | 2026-10-07 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 048301a9-7df5-38ee-9a10-72ad398155b1 | 1.8221 | -55.5456 | 2026-10-07 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ad4aaf1d-01e6-3688-8003-33cb0a8fff36 | -3.0375 | -53.8865 | 2026-10-07 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 1d7fb5fa-2c2e-3149-af9f-ee38833b4bdf | -6.1974 | -52.8295 | 2026-10-07 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 1292d716-247c-32e1-8811-daa622b2e56a | -2.9979 | -54.7692 | 2026-10-07 15:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 2027b4a2-a36e-32ec-88d1-25e811a6e4f0 | -2.8164 | -54.0929 | 2026-10-07 15:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 6f4a4a9d-f791-3663-a91d-afa8f35a413c | -3.0375 | -53.9066 | 2026-10-07 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 8ae4ae8f-f08f-38a9-a727-4c895b0ef8e4 | -6.0075 | -53.5122 | 2026-10-07 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| c543fe88-1abb-35db-ae43-1c801031aa1d | -3.4496 | -56.9303 | 2026-10-07 15:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 141.2 |
| d4758a68-49bb-3055-943c-d6859d1b50bd | -9.3394 | -65.4638 | 2026-10-07 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| cf1cf4e9-194b-34af-b1ce-46169f534fc4 | -2.7879 | -57.6843 | 2026-10-07 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| df716231-e7a9-3400-8e38-ef52ac968561 | -2.4988 | -56.1266 | 2026-10-07 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| a6d50155-646b-359d-ac3e-b0cf868916dd | -1.4752 | -54.7759 | 2026-10-07 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 284.7 |
| a37bef20-8e60-3bd8-a9f7-4d0533d8f1a8 | -7.3304 | -55.0151 | 2026-10-07 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| c1a93eda-2b38-3200-927f-6b34dd5b7a6e | -6.5852 | -53.0331 | 2026-10-07 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b0caafaa-1842-3ce7-8275-8c0e43112392 | -7.349 | -55.014 | 2026-10-07 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 075075e0-c905-38f9-a83b-23e5da49ebb1 | 1.7121 | -55.6063 | 2026-10-07 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 1d2ffe90-3c2a-3316-bea4-5510423d06d9 | -3.6381 | -55.5084 | 2026-10-07 15:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 168.4 |
| 9c8ee83e-c27e-317f-8bb0-0e52928e497c | -9.0987 | -65.3783 | 2026-10-07 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c08c3b5c-b893-3458-a6d3-dadb436f1948 | -9.9175 | -65.0313 | 2026-10-07 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 5fc34bf7-7c5c-37ca-9d0b-bdcb38ecfd17 | -9.1356 | -65.4145 | 2026-10-07 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 1fff8545-acda-34e7-aa3c-e26c32bcf270 | -3.5312 | -54.6157 | 2026-10-07 15:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 559d6da5-a523-3751-9789-88b6f0f25a22 | 1.7121 | -55.6261 | 2026-10-07 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 61f718ef-146b-35ba-9603-6054c7dccb6c | -6.217 | -52.6851 | 2026-10-07 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 8f593faf-b609-39ce-82d1-b5fa1b59cc9f | -4.0025 | -56.2487 | 2026-10-07 15:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 72ac0cc7-6032-3833-9657-f90896151389 | -3.9675 | -55.8157 | 2026-10-07 15:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 6b9acbde-fd83-3eee-b913-100a12a6a5fc | -6.0448 | -53.4697 | 2026-10-07 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 596f36fc-5832-31f4-9bdf-73dc987eda06 | -3.0559 | -53.9062 | 2026-10-07 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 191.1 |
| 6d83a786-a39c-3028-98cb-77f31a8c2afb | -7.2179 | -55.1817 | 2026-10-07 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| de518b59-b9eb-3144-a535-7ca347417c4e | -3.0798 | -58.0276 | 2026-10-07 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 9fbad90c-81a4-3cb9-a9c4-d69089bda1bb | -6.2162 | -52.7876 | 2026-10-07 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 2b225995-d6e5-393f-927a-09dd6d479f88 | -3.0446 | -57.524 | 2026-10-07 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 2e46366d-2878-3670-a0ad-760a4d9c9014 | -7.1814 | -55.1036 | 2026-10-07 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| ec6ecf2f-df06-3620-8235-90d36abf701e | -3.2951 | -53.8395 | 2026-10-07 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 9626cb07-3b13-3591-906b-95e5dafb0463 | -6.0447 | -53.49 | 2026-10-07 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| e1466eb6-7c67-3c63-b3e8-1fca31510916 | -2.1361 | -54.4471 | 2026-10-07 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |


[Clique aqui para ver as próximas entradas](README140.md)
