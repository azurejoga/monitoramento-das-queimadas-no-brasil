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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 720d861f-ab6b-32ac-8eb9-c0e49b40c9f6 | -5.22654 | -43.18058 | 2024-10-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c734103e-c35d-32e8-a1db-60e5b863b4df | -5.22605 | -43.184 | 2024-10-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2cbfd6bc-60f2-30f6-be6a-96f5984eefc6 | -5.22556 | -43.18739 | 2024-10-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8d96bcc-ae7a-39a3-ba0c-f229a5a918ba | -5.22509 | -43.19067 | 2024-10-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6c32f7a8-dc6e-3298-b8f9-ad76faa2c8b7 | -5.22462 | -43.19394 | 2024-10-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b49d2024-b123-30cf-915e-936004d9114d | -5.22072 | -43.18316 | 2024-10-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f213de47-a053-373a-adee-76132151beb2 | -5.22023 | -43.18658 | 2024-10-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e875809-4e39-3870-b9d8-483089d0b975 | -5.21976 | -43.18993 | 2024-10-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0ebf5934-f6a6-386e-84ed-c32975dd7b41 | -5.13026 | -42.7931 | 2024-10-23 04:51:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 511907e6-a5f8-3975-bfd0-fb2892959820 | -6.09347 | -42.59855 | 2024-10-23 04:51:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a1d3fdc0-d907-34ed-84d1-ff2f18a1cabd | -6.3258 | -43.44262 | 2024-10-23 04:51:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 770c14cd-0b34-3b7a-9706-275ac3baa19a | -7.27497 | -43.63056 | 2024-10-23 04:51:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 321b20e8-ef6a-3d40-a7bd-048341f37330 | -7.27452 | -43.63385 | 2024-10-23 04:51:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f96ada51-d1f7-3914-a06c-93d41c799d3e | -7.26918 | -43.63314 | 2024-10-23 04:51:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f7c1564d-037b-31cd-bd78-8d2fa9285bd3 | -7.44643 | -43.62417 | 2024-10-23 04:51:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78f5453c-f95d-3202-8635-803367e8ff87 | -6.68397 | -43.04623 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c764aae4-e396-3cb0-88ec-1a3edaccc8fb | -6.68393 | -43.04387 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73f82db3-7b8a-31cb-8637-c570e7734280 | -6.68342 | -43.04749 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6b7e16a-04a7-3d91-8e88-42bb56599f46 | -6.67944 | -43.03818 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c6112eb-25ba-3d5c-b567-5fb870c798eb | -6.67895 | -43.04182 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0726902a-6ae5-3519-867b-06570a69ffa1 | -6.67894 | -43.03947 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a2d2c3d7-3f00-3e6b-9ba0-b0c5bd8246d6 | -6.67847 | -43.04545 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 58c9c199-4b7a-32df-b3f1-831bc3001ba5 | -6.67843 | -43.0431 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35f65eb4-b920-354e-b21e-b2f740f2a909 | -6.67799 | -43.04906 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d2767aa7-4d36-3bd9-b8e0-1143a3dcec76 | -6.67792 | -43.04672 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fab6453c-6c9f-3e15-ac4a-a9fc14d239b0 | -6.67741 | -43.05032 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e090d882-aaa5-3731-bb4d-fd3ffeb07106 | -6.67395 | -43.0373 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d4086c2a-d67d-311e-9280-6cc9c63b60d3 | -6.67346 | -43.04094 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 27767181-bafd-3259-80bb-861b390aa1bb | -6.67346 | -43.0386 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88bd7537-03d5-3860-a5af-80903c04b7ef | -6.67298 | -43.04457 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cf97bf3a-a396-3904-8517-53598c4159ae | -6.67294 | -43.04224 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 32686552-e39b-3880-bccc-3de47ae24557 | -6.67249 | -43.04821 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e8405045-3439-3605-837b-5cf4ac6f139f | -10.4436 | -44.89925 | 2024-10-23 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 307f9bca-f835-383f-85a6-5fee2500cfdf | -6.67243 | -43.04587 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f061f44d-5a4c-3040-8f64-60ff2155d29f | -6.67201 | -43.05184 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e0aab4d5-c637-3847-9f97-5935aff1497d | -6.67192 | -43.04949 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c2ff8193-4c35-3705-905b-f0e86bd73857 | -6.67141 | -43.05312 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b4aa3a12-828e-3c35-9878-f335c8ded751 | -6.667 | -43.04739 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d257892-d23e-38b6-b190-efa366bc0064 | -6.66652 | -43.051 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f502233c-776b-3813-8481-b9788c927e1a | -6.66643 | -43.04868 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c86f2fa-1cb4-3e77-a37b-ab493e6562e7 | -6.66592 | -43.05229 | 2024-10-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6652e12-1578-3074-b261-c28fa4fc060d | -8.71795 | -44.00903 | 2024-10-23 04:51:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c199c6ff-982c-30c2-810e-d0ef98a554fb | -8.71753 | -44.01223 | 2024-10-23 04:51:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b72ca709-14cd-3a6d-a13c-fa5086ed4c53 | -9.64956 | -43.90776 | 2024-10-23 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7a5f02c6-b756-31a1-b90a-f13e30fde6f0 | -9.64735 | -43.90731 | 2024-10-23 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9fc3a15e-d7d2-3ca6-ace1-104c7cfbf97f | -3.30941 | -43.51584 | 2024-10-23 04:51:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8355b817-16be-31ef-ab5c-ad086de41fee | -3.30433 | -43.51519 | 2024-10-23 04:51:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10a45cbb-333e-326d-bc09-d1ff79b0c197 | -3.49012 | -44.19123 | 2024-10-23 04:51:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 104fbd48-8901-3835-b61c-28f80ddb818c | -3.48791 | -44.197 | 2024-10-23 04:51:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ff57ab7-7ea3-3491-81de-3789c8e32d80 | -3.40602 | -44.15627 | 2024-10-23 04:51:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc20a6a9-ed2e-3915-a6e5-a91c4ca87f5a | -3.40195 | -44.15929 | 2024-10-23 04:51:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1dd2de64-672e-32e3-b712-6e18ed542fd8 | -3.40118 | -44.15548 | 2024-10-23 04:51:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4cf9fc66-7942-3326-adfc-ee2c906b0c74 | -3.30416 | -44.14991 | 2024-10-23 04:51:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b70f904c-40fc-37f9-b8cb-6095c9edf143 | -3.30338 | -44.15528 | 2024-10-23 04:51:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f9d25134-5d90-3ea6-a03d-3a955badbf52 | -3.30077 | -44.14849 | 2024-10-23 04:51:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 85ab4287-a653-3ca1-891c-0483da15eceb | -3.29994 | -44.15388 | 2024-10-23 04:51:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 5d1f490f-4ab1-3c4c-bbdf-7ec54a68d8d4 | -3.29931 | -44.14917 | 2024-10-23 04:51:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e155582e-2a3b-3400-aa0b-766ffa0e1441 | -3.29853 | -44.15454 | 2024-10-23 04:51:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 41868eaa-02d2-3d7d-b5a5-556d705e5a03 | -3.48867 | -44.19168 | 2024-10-23 04:51:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e37063d7-3da2-3b52-8000-01870e84090c | -3.48447 | -44.1958 | 2024-10-23 04:51:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f63608f2-a227-3417-ab93-fc4c3ca37d6e | -3.4004 | -44.16088 | 2024-10-23 04:51:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e315f619-9f14-3aac-88cd-6c2417c1ae50 | -3.24017 | -44.41671 | 2024-10-23 04:51:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 156eda77-1394-3716-8c48-d8a3ef1bed20 | -3.23542 | -44.41598 | 2024-10-23 04:51:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 90b75569-a0c4-36cb-b344-4924b66135f0 | -3.23066 | -44.41529 | 2024-10-23 04:51:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| def29700-2058-3bde-9f81-0f7e0c27b4d5 | -3.96685 | -44.05605 | 2024-10-23 04:51:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2b37b3df-d5e7-301b-9d33-7f74bb8bc867 | -3.64555 | -44.32986 | 2024-10-23 04:51:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fa2ac2e-16a1-31ad-8e62-82d081c2cb6f | -3.64477 | -44.33513 | 2024-10-23 04:51:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9857a0e-5828-393a-895d-26e445dce700 | -4.76566 | -43.36259 | 2024-10-23 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72bccd9a-647e-331a-a9c6-e5db9ae645b7 | -4.7652 | -43.36576 | 2024-10-23 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf28778d-04e9-3f04-8864-543d941e747c | -4.67764 | -44.60603 | 2024-10-23 04:51:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 260b2743-12ac-3611-9145-4cfe1ca678ee | -4.67686 | -44.61136 | 2024-10-23 04:51:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24da1fce-5351-381b-9099-1f30e77d0df0 | -4.67361 | -44.60001 | 2024-10-23 04:51:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac9feb8f-a37f-3c94-a67f-9c46e86e3b39 | -4.67284 | -44.6053 | 2024-10-23 04:51:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9be88f84-83a5-3418-a63c-dd2ad27c6e4a | -4.67206 | -44.61065 | 2024-10-23 04:51:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6352d6a7-a361-3a90-a080-47c7b008de98 | -4.6713 | -44.61595 | 2024-10-23 04:51:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2d2c38e-1447-3af4-8884-39dabf83dfd5 | -4.66881 | -44.59926 | 2024-10-23 04:51:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ac755c8-937e-3dd2-a02e-6b852d303d9b | -4.10544 | -44.23499 | 2024-10-23 04:51:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6cbeda2a-043b-3534-a33a-94fe93a62271 | -3.96357 | -44.05613 | 2024-10-23 04:51:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abb8204a-16d6-3365-8f9d-162aa71d78be | -5.92875 | -44.71819 | 2024-10-23 04:51:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd95efa2-439a-39a3-bdf5-1e3b3e119ffc | -5.62352 | -44.83587 | 2024-10-23 04:51:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 53f5d4bf-7c9b-3319-8e6a-d818d015c62d | -5.6195 | -44.8298 | 2024-10-23 04:51:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 521c84cf-9034-3e27-9caa-23cbf248c633 | -5.61874 | -44.83508 | 2024-10-23 04:51:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fd659a7f-0d7d-3d90-9cdc-a254770ebd86 | -5.58262 | -44.88303 | 2024-10-23 04:51:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 6ebe4b29-4490-39f4-9d2b-7b9d7e8f7e0c | -5.42319 | -44.79862 | 2024-10-23 04:51:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76060984-6523-3c87-8164-e8137748e0f2 | -6.25552 | -44.13948 | 2024-10-23 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9f25934f-90b4-3cbc-950c-044a27c1a014 | -6.25509 | -44.14252 | 2024-10-23 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e16c853b-cf0d-31f4-9fbb-df2d7f38e603 | -6.25466 | -44.14556 | 2024-10-23 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 997e0432-a06f-3124-91e1-733f6111ba18 | -6.25424 | -44.14861 | 2024-10-23 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4e6430a8-f4e1-315e-9af0-87709342022e | -6.25381 | -44.15163 | 2024-10-23 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c30f3d5-3c5d-3714-ac2c-6ee48d131b78 | -5.51157 | -43.69745 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e1e2c2a-9d0c-33c3-82c8-5d9bdb0e3944 | -5.51112 | -43.70057 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6eb3829c-f361-3477-8084-5526b835a92b | -5.51066 | -43.70368 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 695f35d3-f50e-3b34-b602-963c973cb83c | -5.50904 | -43.68912 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d04dcfa6-2b81-3786-93f7-83a6aa4af7b7 | -5.50862 | -43.6922 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0b4490d-f4b1-3611-8303-9f461d3fa8f6 | -5.50819 | -43.69528 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30ffbd44-426f-3f9b-8d97-e54044e8ed4e | -5.50777 | -43.69837 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 746b204e-89f7-34bb-9b6f-2cf6a326cdee | -5.50734 | -43.70147 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0e1b576-9235-34fc-8064-42a81edfaa83 | -5.50729 | -43.69063 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab91e000-087a-3e92-b0c9-67172c48e570 | -5.50691 | -43.70456 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 106c7b5d-aebe-3197-9f3b-70fbcda12dfb | -5.50684 | -43.6937 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README33.md)
