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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a0ba5f1-dd25-388c-8fa8-c7b417db9a7a | -2.88791 | -49.40264 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a78ae4d-a048-3ed9-a99e-adc803b49bc0 | -3.04048 | -50.37568 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b662fabf-2198-32e9-a8cc-52ac4dce008f | -3.96302 | -48.1199 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3fe3c78-0f5c-3b13-a1cf-4375f72c3532 | -3.44834 | -50.75099 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87c150b0-6ae8-3975-8842-5f43fd948219 | -2.77115 | -49.35532 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 101329fc-78b7-3424-98aa-7b3098127621 | -2.27314 | -50.67261 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cfbf3ad5-fe6e-3e71-a8d7-bbd7dd772083 | -2.9348 | -51.48093 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ef814461-38aa-3c76-8fc9-8a1251ca29a4 | -3.99213 | -46.41224 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 80806c46-d304-302c-8975-7ba044eb9995 | -3.37115 | -46.39901 | 2024-11-10 04:38:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4e16ce5-fe23-348d-bbe5-adb598716829 | -3.20526 | -50.63702 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 60d84e7d-31ef-3388-8bdb-fae5b46b1d6f | -7.79748 | -49.32193 | 2024-11-10 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8d97df97-1818-3f6e-85a1-b5166da8737e | -7.63484 | -43.55875 | 2024-11-10 04:38:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 59f6bd05-c662-3950-9c0e-fea6548d316c | -4.7184 | -50.84694 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d19b48d9-dfe5-3943-b4d4-470bf3f6f47b | -3.08772 | -49.5736 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b10d88b7-6bf2-372c-a0f5-bb54abf9a170 | -2.81069 | -52.54477 | 2024-11-10 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c4d37b3f-69ff-3462-82f1-1d15ab98a359 | -2.43558 | -50.51155 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e2218f7-91c6-3284-803d-aa2c0faf81ba | -3.33924 | -50.07918 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0958cf2-ddb2-352a-9a06-b1bfe0ed70c5 | -2.15475 | -50.51508 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e56c319-96fd-3030-bf56-6ac484b40ee9 | -2.87343 | -49.51537 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a36bfa4-1473-3cda-99f9-299f5c10fecd | -2.847 | -49.43231 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a554adf-4288-3791-a499-740302f71605 | -2.25025 | -50.44917 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fc016e2-222e-3965-a093-1b8af0952290 | -2.67313 | -49.89107 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d85d7cd3-217a-32ed-b52f-41a45cef96c0 | -4.10047 | -49.12259 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 949c284e-9f15-390c-b365-345cd8fd67a4 | -3.96988 | -48.18511 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c9f58b53-a37b-3081-b623-cc6502781dc2 | -4.37791 | -47.22346 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11e2d127-6692-3013-9dc9-904ea9b30322 | -3.93922 | -49.75394 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a642281-3444-3ef1-8927-567f67ce2a73 | -2.06995 | -53.28145 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d0ade76e-d7f8-34e6-9be8-20924ce527e2 | -2.90459 | -49.36225 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40d5aa54-a0ed-342a-9b6f-bfcbd1e18837 | -2.94431 | -48.59865 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ffee502-22bd-39f0-b5f1-363711e7bad5 | -5.08203 | -47.7952 | 2024-11-10 04:38:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 990e81f3-04f2-3929-8ec6-c4a3fc15ea1f | -3.59491 | -44.93263 | 2024-11-10 04:38:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d09dd6a-8f15-3e75-a865-29b85273e406 | -2.83866 | -49.44178 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07f95679-e3c1-3f29-9809-cb245ccf862a | -2.92363 | -49.50163 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f27f9283-d1e0-3c86-b25e-073d1fc3678f | -3.1797 | -50.57553 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8e4bd00-ae62-3c3b-b0ec-04cd74316123 | -5.13455 | -48.24436 | 2024-11-10 04:38:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e19cbfa-d52f-3ebb-8378-bef1a0b34df9 | -3.23415 | -46.5415 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a75d9d57-c258-3202-b24b-5da17c0df35d | -2.65312 | -48.55613 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b7929b4-c396-34b2-9047-5a0dd898659e | -7.43615 | -39.761 | 2024-11-10 04:38:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bd2cc397-0ea0-342f-81f8-5d22a2913f47 | -5.24114 | -48.4503 | 2024-11-10 04:38:00 | NPP-375D | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81ac7faa-8116-3fec-a607-8d65039c58e1 | -4.08412 | -45.97753 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f014078b-a0f2-34c0-bcc2-58d656c46c7d | -4.10205 | -49.09096 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a07145c-dea5-3929-9bc5-f550a18faa61 | -3.96044 | -48.18008 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| eb7be005-dbe2-388f-b09c-c656ab72b8be | -5.14014 | -48.25239 | 2024-11-10 04:38:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20104ef7-ca26-36e6-9183-91639d31f041 | -3.44377 | -50.43031 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55985822-e06c-3dc8-b137-162dff99f7d0 | -3.3396 | -50.36176 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd7ce428-31ad-3724-8053-e20978d1cee1 | -3.30765 | -50.08156 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 545bfcc2-3b0b-3d21-a148-0d4a0dea9190 | -2.7255 | -51.71679 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2798a541-a9ff-3892-87a5-daa60a9ff87c | -2.84802 | -49.82694 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a06f638-2d4a-3a41-8f4a-86f7ab6a4ef1 | -3.03833 | -48.04388 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ae4cbad-90ab-397f-af42-3a4427eccee4 | -3.03669 | -48.05427 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ab66fe5-4430-3a01-869f-16c94c736a47 | -2.64825 | -51.87389 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eaf1a8a4-1f45-3f80-bec6-a57703284535 | -2.66016 | -49.90742 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af517b79-7059-3190-9db8-a9fde37506ee | -5.16479 | -50.67917 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 658ba77b-78b0-339d-a8e7-26e5cc2a5e7d | -3.07769 | -49.52882 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a19a397f-de25-3748-a0eb-06328a4ecfa1 | -3.95153 | -48.99318 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f97ef38e-14b3-37c3-8a56-96e792a95781 | -6.6107 | -51.13879 | 2024-11-10 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b2151f6-a440-30e0-824a-7c6746e2bc15 | -2.21456 | -50.45124 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9170fbc-15bf-3a5c-9bec-cd993374a3a0 | -2.14281 | -50.76725 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d41a5495-35b1-360a-83b2-8f9edab97d80 | -5.24128 | -46.23315 | 2024-11-10 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f65d151c-c839-3a21-bb76-45e9aa22f960 | -3.09487 | -51.2907 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a92932e-d240-3baf-a89e-f5d47f79e8d3 | -2.71918 | -49.18637 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fdd78b0-fbd3-3b32-a69c-e0122489619a | -3.58744 | -49.90213 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 038121b8-ed22-35d7-b164-150f166ce2a1 | -3.24631 | -46.46244 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ca34279-14a6-3ee1-be9f-0973c1b01e5d | -2.88349 | -48.29543 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef7767cd-2359-3f57-b6ef-8a42130341ed | -5.56189 | -47.78074 | 2024-11-10 04:38:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 713b10d9-b79e-336e-b0b4-ad7e38fd0fc1 | -3.25033 | -46.48238 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a466fae2-1148-3337-a1eb-de067a17d92c | -7.14383 | -41.10558 | 2024-11-10 04:38:00 | NPP-375D | CAMPO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202133 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b8268bf4-b57e-35c5-ba7d-cc0933eed775 | -2.95697 | -54.14907 | 2024-11-10 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4101e4b7-32e5-3432-bb00-9116d335029e | -4.85601 | -46.97795 | 2024-11-10 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88c721c7-0716-316c-b284-e4f1edc28855 | -4.06554 | -50.00953 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee69f4d1-34b2-35f6-b05a-bc15060b9bde | -3.94984 | -48.1606 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 074df0bc-6910-319d-8778-704fdcb65adc | -5.05588 | -44.27736 | 2024-11-10 04:38:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e87b4eaf-ed8d-3743-a5b5-9b0d976e0bcf | -4.16708 | -48.24407 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f16bb740-a0d0-3382-b39a-6bcb7b65eda4 | -2.90063 | -46.8249 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed4e8a4d-0a38-379b-9b76-ba4684f11b75 | -4.8112 | -48.75673 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2b2998e-6e76-33c2-93a6-34314e801e2e | -5.52381 | -45.40295 | 2024-11-10 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0faf19a-8ed5-3933-9902-2874a36e0776 | -2.38477 | -50.6079 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c1b4e78a-e663-3612-b12b-6c2b084e976b | -3.11972 | -50.14151 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39503f8b-2caa-3bb2-8514-260771e4e5ac | -4.61652 | -49.58106 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8714ebae-9fa5-30ed-9f44-afef1564d96e | -3.01634 | -53.26858 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b360710b-173b-3b15-9348-c1abfa8ce2dd | -8.40223 | -44.10465 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72d16e69-851f-3da9-8a7f-31810e82a0c5 | -3.27168 | -49.62798 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fbe3d995-8a16-3dc2-9965-9c907e299d54 | -3.33861 | -50.10493 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a413359c-8510-3e91-af26-6a2ea2861db1 | -3.2453 | -50.27251 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e195988-48cb-3c45-a577-239e09903bec | -2.23199 | -50.16511 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 697cc604-e62b-3a43-aac1-2e794ac04144 | -3.65698 | -50.1656 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b13f80f-2f94-3afc-a4c1-b72f65349897 | -2.37841 | -50.41092 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 768b1725-8927-3d58-bb4d-b9d31da9ad88 | -3.73154 | -54.22191 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f3f6416-543d-3ba0-b8f1-cde0192a2fd2 | -3.24515 | -46.47002 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ee22caf-9ce2-3752-9644-c470d51a67b5 | -2.92405 | -51.47925 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 96a2acf4-8cf3-3011-989e-cf56df8aa915 | -3.87022 | -51.97719 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72b46a40-a1d7-3b60-808a-bf59d9dd671a | -2.33108 | -50.57661 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98d08199-043f-340f-830a-a534a8daf74a | -3.19212 | -54.31998 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ec0aee4-fe94-3acc-b28d-b705896b5b68 | -2.83368 | -49.47337 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 95cd60e6-8c63-39bb-b0bb-cbdc750855d3 | -2.81284 | -46.65025 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01b8fcfe-68db-301a-b5c9-b0eb78ee3d6d | -4.05516 | -48.31218 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8ad841e-3adb-33b9-a497-6796949472e9 | -2.72723 | -49.84126 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68b64b45-09eb-3b6e-83e7-19e974930041 | -3.84146 | -49.97079 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63b13601-e2c7-359a-9b89-af99eb3c92e4 | -3.02237 | -48.08044 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8cea7ca-a8b2-3d0b-a8c7-d227ed591e8e | -4.38633 | -48.57344 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README93.md)
