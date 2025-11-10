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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0651b23-624b-3f02-88e4-fadaf3bd36d6 | -3.7027 | -54.67675 | 2025-11-10 04:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0356a368-ecb0-384d-849b-6311f74e5039 | -3.69673 | -50.19253 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 156a6cf1-0ac7-3c75-ae0f-7de4e389ce7c | -3.3185 | -50.10172 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f9edb038-9c63-3e9c-ba51-9787e333db8e | -11.02508 | -44.81203 | 2025-11-10 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4e095dc9-c65e-35bd-b13e-060536d5dede | -4.8567 | -45.78664 | 2025-11-10 04:21:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae4fcaf2-8a65-3f5f-a9e8-aab67c91285f | -3.30825 | -50.16422 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 230db341-9b1f-32ef-b17b-d7f5fb9d6eaf | -5.63031 | -43.911 | 2025-11-10 04:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f19a7155-b26a-3d82-8d94-c97084233130 | -4.91764 | -46.73205 | 2025-11-10 04:21:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 262bf948-aa90-3344-b9a7-85b739048824 | -7.98613 | -38.67052 | 2025-11-10 04:21:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 25823aa8-c81b-3cb9-9250-a49e48eb8b43 | -7.93092 | -55.01911 | 2025-11-10 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb782bb4-1731-374a-b7c0-b62c77241ed5 | -4.20485 | -50.63601 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| d01f2faf-833c-35f8-b03c-6a9008e28733 | -9.23734 | -40.62965 | 2025-11-10 04:21:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7b303f59-fd0c-3a11-9fa4-084ad75d64e8 | -5.28236 | -44.95288 | 2025-11-10 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2fdae809-f240-33ca-ab88-496f0a25ab13 | -6.15204 | -43.63902 | 2025-11-10 04:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5c7e219-2f3e-3474-b316-fbe33831a509 | -3.14073 | -50.27694 | 2025-11-10 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7b3f079b-afe6-3575-9cc0-c1247c01527f | -4.89512 | -45.27284 | 2025-11-10 04:21:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6a9e034-f881-3642-8878-52945344ef39 | -3.87145 | -50.97287 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65a5ed84-c753-3db4-864d-5a660e0a4382 | -3.33021 | -53.25138 | 2025-11-10 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 504d0061-290f-3b8c-bfc1-89f950ff8db0 | -6.85989 | -40.15727 | 2025-11-10 04:21:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 760d5159-0994-3b89-b9ed-7290afa8d7d8 | -5.37595 | -44.72686 | 2025-11-10 04:21:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e353d859-1f16-3249-acd8-707d2492e62b | -8.08641 | -43.64603 | 2025-11-10 04:21:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8652dab2-b56d-37b0-a36f-5ba3036a3622 | -3.60866 | -50.77192 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9cd4b9d-09c7-3871-802a-5ae0e7d8e43d | -4.68119 | -45.8483 | 2025-11-10 04:21:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab020f62-6a5b-3066-9cd8-494e152611b5 | -4.1342 | -48.82322 | 2025-11-10 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d849ee0b-a4c3-321a-968e-212c75ff90ed | -5.19733 | -46.21715 | 2025-11-10 04:21:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10eb5a69-2452-38d5-918d-116c467b882b | -11.91142 | -43.82224 | 2025-11-10 04:21:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 96f40c01-b268-3d85-9c5f-6749c5c1181c | -9.87959 | -44.58109 | 2025-11-10 04:21:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22866057-635d-302a-b1fd-04e1b9ea45c3 | -5.7481 | -50.22215 | 2025-11-10 04:21:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9c589eb-0c06-3188-a4c0-17dffb8515a7 | -5.16749 | -38.74445 | 2025-11-10 04:21:00 | NOAA-20 | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5a2f87fb-0aa6-3a4d-b50e-f473013c510f | -4.45478 | -50.48966 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b81abcc-e829-3cad-9b37-a774db4782e6 | -5.19308 | -46.15615 | 2025-11-10 04:21:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5835509e-5112-3856-8e3b-71675d3cb34e | -4.2051 | -49.77325 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 803df723-21f3-32fd-8e89-5d0f0758e9c7 | -3.33138 | -53.24448 | 2025-11-10 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 657c0d72-5b8d-36da-89f5-0e6e1fadf236 | -7.89097 | -48.39381 | 2025-11-10 04:21:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f133966-5600-30a9-8b54-52425a824fff | -4.73669 | -46.15937 | 2025-11-10 04:21:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27985c97-29fe-340e-97b1-68d4768a1a7a | -11.16862 | -43.57092 | 2025-11-10 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f2f00f2d-058a-3770-a7d1-898eb55737f9 | -9.1278 | -50.08644 | 2025-11-10 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ce55022-31de-3cea-adc5-dc60cb15f380 | -3.35019 | -50.21271 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ef47503-b1ce-309a-93de-673f9ca3c627 | -4.67838 | -45.69279 | 2025-11-10 04:21:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f30173b4-c11a-3e36-bf84-c2ed1ca00588 | -3.77618 | -47.61132 | 2025-11-10 04:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 595addaa-4006-354e-a8e5-eba94d4f02b8 | -3.30894 | -50.16003 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74ee1895-d211-37b3-b96b-e2c071d9e66a | -3.86368 | -49.8946 | 2025-11-10 04:21:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f854d57-8ce1-3fa6-a355-11fa2c523840 | -3.69742 | -50.18836 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f47c34e5-5af4-323c-9c25-698cc4acb6c6 | -9.91241 | -44.21413 | 2025-11-10 04:21:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 301b18a1-a219-3993-b2ee-b934fc40b531 | -3.25887 | -50.07572 | 2025-11-10 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d61eed2-ab98-33a1-9f27-bdaf74ce5217 | -3.80463 | -51.09118 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 04cce627-34b1-3d33-816d-4659c480f430 | -5.92586 | -43.97538 | 2025-11-10 04:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfd492a4-5c53-3b5f-b730-2b95eb6d50e4 | -3.59534 | -55.47645 | 2025-11-10 04:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a096eafb-216d-3bcf-9dec-5cb94b33f659 | -5.28957 | -45.65777 | 2025-11-10 04:21:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b0baa44-4764-358f-bde9-58a1ecf992ef | -6.40683 | -49.91299 | 2025-11-10 04:21:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffe945b6-aed6-3f6a-8537-45e3172bfdd2 | -3.94048 | -51.03733 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e6f9d6f-47b1-3fed-805d-70eef3a8d5d4 | -6.5904 | -44.65413 | 2025-11-10 04:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8055957d-c6eb-3302-a9dc-9d941d1f8a46 | -4.58378 | -46.66823 | 2025-11-10 04:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4dc49aa7-289a-3f7f-954c-55f23f36bac8 | -5.83545 | -38.35184 | 2025-11-10 04:21:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 542a5e32-42b9-3d97-bb95-7a6fad8798af | -3.85863 | -51.04799 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd0c55db-dd0c-3971-99de-8fba9396adf5 | -7.88439 | -48.38824 | 2025-11-10 04:21:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49ed910c-09ad-3dcd-a150-2032348a2aa9 | -3.40574 | -50.45103 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 06c23e7e-4285-341c-9624-244e4ebc49d2 | -5.37155 | -44.73325 | 2025-11-10 04:21:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d29d1edf-2285-38fa-ada3-3a4e8e9554a2 | -8.01407 | -41.60276 | 2025-11-10 04:21:00 | NOAA-20 | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| eb6d3d01-3b8f-300f-b100-afb80bbf136d | -4.63663 | -49.59305 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 55c2d0d1-ec4b-3dd9-9d11-a67a938d89b0 | -8.44589 | -40.53872 | 2025-11-10 04:21:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 92bce14a-1df1-366f-ad3c-75bd0dbdb49e | -4.7401 | -46.1599 | 2025-11-10 04:21:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b06b2f4-e41d-37b8-8d0a-e46d14b62f34 | -4.44497 | -46.42437 | 2025-11-10 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05987584-455a-300c-92aa-c28a387aaffb | -3.874 | -52.27777 | 2025-11-10 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ead24e4-a805-37c1-9901-3442a5e9c9ec | -3.34133 | -50.2086 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93634473-bdb0-3e6a-be6f-c98cac632366 | -4.05513 | -46.43093 | 2025-11-10 04:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 362e5883-2d64-340f-888a-f3e56ab68986 | -3.77686 | -52.24527 | 2025-11-10 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 952af55a-3db6-34fb-93f4-d4dab599b3a0 | -8.01539 | -50.25331 | 2025-11-10 04:21:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67ab013e-4f2c-3fe7-b25c-2d3e23133425 | -6.14283 | -44.86259 | 2025-11-10 04:21:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43a8d6f0-aacb-3a7f-b737-ffbf5e3a7527 | -4.12473 | -52.06488 | 2025-11-10 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ac068f5-5115-3dba-99f8-cf70596a8c3a | -7.81414 | -41.95801 | 2025-11-10 04:21:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2923d324-49c6-33a4-8d33-b27269f07173 | -3.69239 | -50.19183 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 26873f4a-70c2-3a81-a5b9-b0db9820af75 | -3.58148 | -50.28643 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5da3f52d-b0f1-3baa-b3f5-aff590a9aa27 | -5.88995 | -43.96624 | 2025-11-10 04:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c4a89938-84f8-36a3-8107-a74c12cffe42 | -4.5928 | -45.54733 | 2025-11-10 04:21:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af7cb951-fde0-370a-9375-19e2a64c7f8f | -4.26132 | -46.71074 | 2025-11-10 04:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b514e9a4-1805-3612-bd65-159c10569b83 | -5.19366 | -46.15248 | 2025-11-10 04:21:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b12d450-a650-3211-820b-2f9d85d2c789 | -4.09243 | -46.28547 | 2025-11-10 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d64750a5-5513-3d67-9482-42784ecaf506 | -5.12035 | -44.73206 | 2025-11-10 04:21:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2800cd23-aa5b-39e9-a9eb-bde4fbaba100 | -6.44251 | -46.98118 | 2025-11-10 04:21:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ca4f633-4f3e-3bf3-be9b-f8f43a980c76 | -4.1111 | -47.27991 | 2025-11-10 04:21:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d766c7b3-7138-3fd2-ab5b-20fb0c661a8c | -7.31029 | -43.34566 | 2025-11-10 04:21:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b4b77e2-0581-3905-8d00-014f977aeee3 | -4.90558 | -44.88554 | 2025-11-10 04:21:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb2d88a8-1234-33f1-9125-92464d7faf61 | -4.75086 | -49.50625 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e46e740-7838-3d43-bb28-18e76bd70c74 | -3.25706 | -52.06233 | 2025-11-10 04:21:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0c600652-be21-3613-b257-fd8c36a626f2 | -5.60445 | -41.07673 | 2025-11-10 04:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 64b7688b-db88-3932-83a3-f9c4ebbbdf08 | -11.53083 | -44.02691 | 2025-11-10 04:21:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b5bfe69-516f-3512-99e5-2d12f0a0bbca | -4.75621 | -42.66082 | 2025-11-10 04:21:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 289dd4b4-d797-3e72-a29b-ec28b44b3acc | -5.12475 | -44.72569 | 2025-11-10 04:21:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9120eee4-0883-38a5-b5c1-d207272d7b17 | -4.43494 | -50.60931 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb4f9f60-a319-3312-9829-9790796eb09c | -5.61941 | -46.91271 | 2025-11-10 04:21:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 512b81ac-8117-3a37-b6ca-1a377e9cc1df | -10.37453 | -49.91413 | 2025-11-10 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f65e45e1-9ee8-3823-b292-373fe4933aa5 | -4.67501 | -45.69228 | 2025-11-10 04:21:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b915754-752c-35f6-8c27-92c46dc4e17c | -6.17394 | -44.38667 | 2025-11-10 04:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 315ba9cd-6350-3bdf-af92-c380c4832752 | -5.56453 | -51.20919 | 2025-11-10 04:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3da8eeab-b80c-3cc5-adf1-d529c82d9370 | -6.71058 | -48.68755 | 2025-11-10 04:21:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d38d87a-68e6-33b5-9928-f17ffdf21459 | -4.33078 | -43.59768 | 2025-11-10 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 981a2701-444b-3a66-84aa-ba73c0e4e559 | -6.05742 | -44.69317 | 2025-11-10 04:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33a107b7-ffeb-3fd9-855e-4ee77d15ee20 | -4.2056 | -50.63149 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| c0462e2f-735d-31c8-a86f-d5277a568cf3 | -5.36934 | -44.72582 | 2025-11-10 04:21:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README12.md)
