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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c5b3427-b892-3447-8ca4-3e53104d2a4b | -6.45739 | -59.9745 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27d9d724-111e-3962-afcf-5adcf1b4a0e5 | -9.54081 | -45.38893 | 2026-09-22 04:46:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a079398-3d78-357e-895b-37dd4315ce97 | -8.8382 | -50.48697 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac3d8c3d-d0b7-3194-8b0c-650b940d773a | -3.01008 | -54.19252 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08c193e8-8d08-3cc3-ba99-4a7ffccd885e | -4.41412 | -55.24013 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f1770721-72f5-38bb-be87-940b6ae99c46 | -5.84641 | -49.78743 | 2026-09-22 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c047fb68-39b3-3c26-8b9b-6701583a401a | -6.43524 | -55.61008 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07382e86-caaa-33b7-9fa0-5726428d2e29 | -3.21361 | -53.95449 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad838ab0-bcc9-3312-8bac-d48c083dca4f | -4.27582 | -56.25633 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28ef8e54-b7bc-3d07-8949-a683d74914cd | -4.30288 | -49.12619 | 2026-09-22 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88d2a0a0-f605-329f-a3d0-cd419ff1396b | -6.28833 | -57.74478 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b3f173d-98f5-33dd-80e8-62e44a775a6c | -4.27937 | -56.26074 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0c2476a-3c63-3821-ae0a-19f8209d9c61 | -6.7123 | -43.98304 | 2026-09-22 04:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c1dc1009-ca5b-3f3f-b867-d4ef14b6bbcf | -6.31035 | -57.74228 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8aac6596-3109-30fb-b280-e07fa9bb8fc4 | -4.64551 | -50.99199 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c6ba0ad-47d4-383d-8443-c5a37c5eaf1e | -10.85196 | -50.15056 | 2026-09-22 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd3a9b8b-cbda-3180-9dac-87e36343fb00 | -9.61351 | -43.92169 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b17890af-6018-3207-b1eb-827ccba419c9 | -9.61123 | -43.93851 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2f96a81d-45aa-3013-becd-4386b0d8e3a3 | -4.96739 | -55.82511 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ec7b5b4-34a8-343b-8106-3d75458c4e91 | -8.24646 | -55.28992 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c044dcf-fbb6-32b1-9034-e21ef9dae97e | -6.3115 | -60.00886 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc8055e0-573b-3e13-83b2-fdea5ea8715e | -6.01572 | -47.90558 | 2026-09-22 04:46:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a170f1ea-f3e3-3382-ba64-be592d2e7739 | -5.88516 | -52.04715 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c0d87f2-6816-3dff-9e60-9112b713f898 | -9.53264 | -45.39 | 2026-09-22 04:46:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2390d69d-1d91-3b7a-9cfb-60d36c282ca2 | -4.65795 | -42.08487 | 2026-09-22 04:46:00 | NOAA-21 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bf032202-26b6-3eb1-8b82-cb6c16ef0f9d | -6.42301 | -55.01374 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| edcb6cdc-764e-3e1b-b39b-1938ae7a094d | -6.6706 | -50.94391 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4d55732-b60a-3b32-a81b-4db6a754a8c2 | -6.64421 | -59.92873 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 8f16f753-fbc8-352f-ac71-215c1c75bfba | -6.5777 | -44.15266 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 58c21b41-3e9a-3d88-8b2b-d185fe71e8c3 | -3.26993 | -54.26146 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f47ff672-92eb-37d2-aa4f-ac580deae3de | -3.20995 | -53.95389 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d1b8dbc-d404-3756-854c-f9fe59ae3ba8 | -5.83906 | -52.1228 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c84c808e-38c3-3577-8b7d-2f57f4535706 | -5.61407 | -44.8425 | 2026-09-22 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f0b9382b-c6b4-3d80-8577-77919cc38de5 | -3.4491 | -50.61697 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 960d1ac6-1496-3e66-848a-b2f2434f7720 | -6.12644 | -59.95237 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f190405-a92e-3ff6-b147-f9eaed2733f1 | -6.34167 | -55.30034 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83645217-9cc4-3c70-8c1b-ce6c0fee2e96 | -6.30522 | -60.01425 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb0f55f7-61d4-321b-bffb-4a4bde00d736 | -5.81548 | -53.51724 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ce0dd1a-32bb-3dce-8a9c-5f869df65f58 | -6.46469 | -59.97344 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f23a74c-12a8-3cc4-b2ae-b7b88a7fa312 | -6.00638 | -45.2463 | 2026-09-22 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41cb5a20-313b-3851-ac00-28eaaa6f85ff | -5.9809 | -44.72657 | 2026-09-22 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2dbc0ada-e467-3919-81d0-44b2bd9fdc74 | -10.86563 | -50.89774 | 2026-09-22 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b44f61f7-cebc-36cf-a4a6-86e2da09fc71 | -6.35743 | -58.28716 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b3774ba-230f-3cc9-8803-cfa9d4658264 | -4.68725 | -40.14885 | 2026-09-22 04:46:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 864dedfb-7fe7-3407-8ff9-1b10ce572140 | -6.09339 | -57.6955 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 752a0499-79c5-37d4-82df-5ab34e327b6e | -4.44851 | -55.6008 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 160cce92-cde5-3045-8d8f-43dcc0163483 | -6.62073 | -59.91192 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6e38b913-677e-36b5-b531-d054cef29eec | -8.12421 | -62.87859 | 2026-09-22 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04a75766-b5a1-3f5b-8ac0-9824c2f2517a | -7.48187 | -45.47025 | 2026-09-22 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 14d507d8-46de-3998-98bb-9c521bf17f8d | -4.94343 | -55.82108 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b998da50-ed0a-3390-b4cc-e2bcce658bcc | -6.09251 | -55.56577 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6935d06e-e1eb-37cc-b025-787dca55a450 | -5.9975 | -55.68164 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1419a428-e039-390b-9b8f-f6cbad85aa3b | -5.89579 | -53.64116 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8dbc764-4e31-3306-abaa-cb2d027a66fa | -6.97781 | -47.49667 | 2026-09-22 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49e96dc0-fe37-3cf2-aa8e-c16ce8bdea1b | -11.1479 | -42.84622 | 2026-09-22 04:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e2952d5a-543b-3083-910c-2d3e58c3b619 | -6.15872 | -57.95514 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bfd9a18-88ca-309c-b35d-0bbc3b306803 | -4.07807 | -56.2282 | 2026-09-22 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7c4b57e-d872-397c-adb2-eaeefe43bf82 | -5.93852 | -59.97582 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0dd12e4-6ade-3a4a-8de6-dac3e8c9b629 | -6.3577 | -55.83971 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d10e88e-cc52-3453-9495-da31b85d1c92 | -5.44191 | -48.37067 | 2026-09-22 04:46:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8307dafe-b580-315f-b4a1-e1e5e7d952e7 | -6.05318 | -57.82677 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a057bbfc-ee62-3be4-942c-8bc4daff8b07 | -5.98798 | -57.69625 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 606d82de-57d0-3480-abb5-95017c4f11b3 | -6.52909 | -55.36528 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d9dd3f5-457b-36ea-b8bc-83778fe83d2c | -6.13517 | -59.96378 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6816558e-e06f-3cd2-a333-a76b59418fba | -7.58419 | -57.67527 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6827972f-6849-3f3f-a815-537ca815435f | -3.0595 | -54.41255 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9e567d1-928f-3e60-bbf8-8a50532a07dd | -6.09603 | -57.62456 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9374bd37-defb-32b6-8b8e-53696ada5128 | -6.14383 | -43.84069 | 2026-09-22 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 31c22bb4-88e8-3e41-88f7-45a11c0a3205 | -4.0739 | -56.22758 | 2026-09-22 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 652b851b-7a55-3e56-aaa8-7e17c7a3145f | -7.37277 | -45.42724 | 2026-09-22 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90c25dc8-5762-3c4d-b148-9ffde332c3d0 | -3.36149 | -50.76171 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e5e9300-e972-342d-a6b7-86273179618b | -9.97094 | -50.25347 | 2026-09-22 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e66005f-42a0-3c45-b0ad-0dc78fd37782 | -6.73302 | -55.09096 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bab2d07-f010-3a96-94d5-1da643f47a8b | -3.60018 | -59.44361 | 2026-09-22 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 666ecceb-5397-39bc-98ac-5d4dec90e156 | -5.8754 | -53.63406 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6e83cc4-4622-35e1-961e-b2dc61204e6c | -9.89291 | -48.3997 | 2026-09-22 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cab1c1d-554d-33d5-868b-e9a4b32bbc32 | -9.87772 | -55.7291 | 2026-09-22 04:46:00 | NOAA-21 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| faf31659-1bdd-352e-b42e-457d12f374c7 | -8.61933 | -54.61866 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0b6d57ed-1024-3973-8d3f-d18a3546f8e0 | -10.26347 | -49.98635 | 2026-09-22 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4938b79-304c-3d6e-9db4-f8d5cb3384ec | -8.25222 | -55.27098 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f87a2249-9837-39fc-910e-e1b3a894069f | -5.87905 | -52.12912 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14d1dfec-ec3b-3880-8456-298ec2890495 | -9.0795 | -60.44048 | 2026-09-22 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69191981-5cfb-3036-be23-30dc59c7eea7 | -6.77271 | -55.46796 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3b76fa3-9d7d-390d-9c85-936834d1a526 | -7.35766 | -45.34969 | 2026-09-22 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 59496e38-ec10-352a-aa7f-110d4e41ef85 | -9.53137 | -45.39176 | 2026-09-22 04:46:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6edacc80-3689-32f2-a996-e06508b8ba90 | -3.44411 | -50.60565 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 699c2c9e-be74-3328-b8ad-7d1d5a85ada1 | -6.75046 | -59.06672 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9dbff522-dc6d-3d2c-b0e3-9ce1b86afbc2 | -3.22888 | -53.9528 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2c6d016b-0be7-309d-bd56-b4a3ae34e7b7 | -5.77232 | -47.36327 | 2026-09-22 04:46:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5fc832f-a1ac-32a1-a214-3b05e1bde65a | -3.95808 | -49.04424 | 2026-09-22 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b487ab0f-b4aa-3131-ba4f-ba6e66cd24ab | -9.26239 | -46.23216 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f484a70-d756-3f17-b928-54f8565c570a | -11.10165 | -48.33059 | 2026-09-22 04:46:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 24e2a130-5262-39d3-bcd9-230f03104763 | -11.11112 | -48.31789 | 2026-09-22 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4908d9b6-6789-3db8-a7f7-290b4f1a3e8c | -6.66122 | -50.93893 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65107657-7fcf-3b01-9de6-47aec13db193 | -3.08437 | -61.17173 | 2026-09-22 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc6abe9d-daff-3b22-8640-974daba79699 | -6.70648 | -59.00415 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bad11c23-024a-3918-ac3b-319a80c194ca | -2.91433 | -54.18317 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a479b2f5-9cc3-3fed-a69a-18e12671f5ff | -5.87517 | -52.06725 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 13ec0a71-7e59-3961-a0ae-da844e909b0a | -11.67836 | -43.46634 | 2026-09-22 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cf86880-ac85-3419-9891-bdd0f9b53083 | -11.66308 | -43.46095 | 2026-09-22 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README65.md)
