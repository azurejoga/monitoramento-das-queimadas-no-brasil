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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90b8b1af-33da-30b1-a0ad-bb550b2da923 | -3.97727 | -45.51046 | 2024-10-18 00:43:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a756b79d-5fc5-31b7-a92e-02606c1ea5b7 | -3.92393 | -48.35146 | 2024-10-18 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3bb305f1-257f-3787-aa0d-78159c0cf8e2 | -3.90583 | -48.36522 | 2024-10-18 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 060b5bf1-9d4c-3559-b0b6-2d731d9255a0 | -3.90443 | -48.37169 | 2024-10-18 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 04946d87-ab8c-3928-928e-8f3ef15ee668 | -3.90288 | -48.36065 | 2024-10-18 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 57e97036-028a-3eba-8800-f33c59b9f922 | -3.90288 | -48.34312 | 2024-10-18 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| bbefd210-16cf-322d-93e6-2e21d15fdda2 | -3.90143 | -48.33229 | 2024-10-18 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| df212b70-03c3-3b4a-8318-ddafbfb9aaa8 | -3.89981 | -48.33868 | 2024-10-18 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| fdc8960d-9cb8-317b-9242-cdeec3bca141 | -3.79293 | -45.91396 | 2024-10-18 00:43:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9a8b95fc-ac1d-324e-9cf5-083777d6ae45 | -3.79071 | -44.38305 | 2024-10-18 00:43:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 150b9d24-f1c4-3e6d-a9df-ab6f52cb4517 | -3.78265 | -44.77877 | 2024-10-18 00:43:00 | TERRA_M-M | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 21f2d472-ab8b-3c47-b74b-b7bbc8ac86da | -3.7814 | -44.76986 | 2024-10-18 00:43:00 | TERRA_M-M | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c9b5d530-13b5-3a26-84d6-c61bd5c6b699 | -3.71325 | -51.08322 | 2024-10-18 00:43:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| e5f7edc0-5ddb-3364-a8bf-ec2308cbdd36 | -3.70972 | -45.91398 | 2024-10-18 00:43:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 70f81dbe-76ab-3f56-9716-fc9e4a192487 | -3.70849 | -45.90513 | 2024-10-18 00:43:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 42.2 |
| c1561167-6379-35e3-bcdc-7bc87cfcc46f | -3.70814 | -51.09035 | 2024-10-18 00:43:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| da6b0d39-ef1d-335b-8987-d93c4f112da1 | -3.70088 | -45.91522 | 2024-10-18 00:43:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 24.2 |
| fc025eba-37c7-3798-81db-008c8e534ffd | -3.69965 | -45.90638 | 2024-10-18 00:43:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 145.5 |
| f33e4572-0101-3b99-95a7-894131e5340c | -3.69795 | -47.62049 | 2024-10-18 00:43:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| a62e3ee8-0674-32ea-93e3-d9d9ef82c6d1 | -3.6908 | -45.90763 | 2024-10-18 00:43:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 069a8a09-024a-3196-b0ab-09ec1fe2a2b5 | -3.65436 | -45.25776 | 2024-10-18 00:43:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0d6ae3fa-92ae-3c19-a477-3235e470ad09 | -3.59046 | -50.57624 | 2024-10-18 00:43:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 0f0c8e02-f929-3baf-ba8e-edb6673a2ecd | -3.54018 | -45.76136 | 2024-10-18 00:43:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 2c49239b-3122-34b0-ab5c-b859e51d8f8c | -3.52633 | -48.06076 | 2024-10-18 00:43:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4d47e5f5-2bb2-3289-a1b0-1f953a6966e0 | -3.47465 | -49.24705 | 2024-10-18 00:43:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 85ec469f-e7e2-3f92-b4d4-6eefd7e296a1 | -3.47263 | -49.25346 | 2024-10-18 00:43:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 58ae5c14-aa32-373c-b356-78b4e57afd4b | -3.47252 | -45.66331 | 2024-10-18 00:43:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e1d334ec-222d-3030-a402-5b570e1aaa20 | -3.46418 | -47.67542 | 2024-10-18 00:43:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 1dabd5f2-60a3-3b57-a85b-e2e5305f4532 | -3.46283 | -47.66548 | 2024-10-18 00:43:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 837b26ab-de71-3ddb-8292-d25008c0fea1 | -3.45782 | -50.60664 | 2024-10-18 00:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0530d515-3b5a-3fb9-812e-4cacbd43d95f | -3.43529 | -45.52522 | 2024-10-18 00:43:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cc1b0229-6594-37ff-88af-a0e054c98bdb | -3.36005 | -50.31276 | 2024-10-18 00:43:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 586e54f4-c82c-3882-875c-0266bd80282e | -3.35809 | -50.29808 | 2024-10-18 00:43:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 650791f0-72c4-34db-b8c9-42e0ab3e28e9 | -3.34402 | -45.33786 | 2024-10-18 00:43:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9a50af09-dfad-3bb5-917e-c18b8f8374f7 | -3.31617 | -44.15345 | 2024-10-18 00:43:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b5d4c1a7-afb8-36af-8987-41e0043cc131 | -3.31119 | -47.02787 | 2024-10-18 00:43:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5a0dfbde-fca4-3a19-86ac-73247c460b9f | -3.30605 | -46.9907 | 2024-10-18 00:43:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a4b89413-cd52-3101-96a9-e35a95cbd009 | -3.2907 | -46.08433 | 2024-10-18 00:43:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 96ec5c2b-6d45-31ad-8576-fdef6b2f4ddb | -3.28898 | -47.13587 | 2024-10-18 00:43:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5e281f8d-4c1d-3e4d-9605-4b703da6cffd | -3.2877 | -47.12648 | 2024-10-18 00:43:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 0c3e8b54-77c6-36fc-a36a-45dc20bcda9f | -3.27987 | -47.13712 | 2024-10-18 00:43:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6ac0684c-8ebd-30cf-b445-e52421216511 | -3.27859 | -47.12774 | 2024-10-18 00:43:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 9436eded-b3c8-3029-b0e1-18bec1593335 | -3.26989 | -50.65999 | 2024-10-18 00:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 3c6807e0-f14f-30dd-86fa-77adff364966 | -3.26851 | -49.08994 | 2024-10-18 00:43:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| db80f0af-b4e1-3e51-950d-376182b1cc19 | -3.26784 | -49.09594 | 2024-10-18 00:43:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 96b15ead-3e54-3227-999d-c2c433278159 | -3.26625 | -49.08402 | 2024-10-18 00:43:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| fb905c45-e66a-31ce-b52e-9cd0d2cca0da | -3.2326 | -46.52599 | 2024-10-18 00:43:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 02339f17-4e22-38d7-acf7-07141b74eedf | -3.22368 | -46.52726 | 2024-10-18 00:43:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2739634b-963d-31d8-865a-a4ba52afbf3a | -3.21708 | -50.35924 | 2024-10-18 00:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 9eaaa8e0-1d71-352d-a731-e721a6708387 | -3.21518 | -48.92931 | 2024-10-18 00:43:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 6d90a94f-e676-3d11-a489-6f9e1356482a | -3.21357 | -48.91767 | 2024-10-18 00:43:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 457748de-463e-3f6d-b5ff-9a866ebbb233 | -3.14243 | -48.69493 | 2024-10-18 00:43:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 58d9f267-7d2c-3d31-9307-d3d84f689801 | -3.14091 | -48.68372 | 2024-10-18 00:43:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 11a3c1ba-5a03-34d2-857d-f754e24960aa | -3.13637 | -48.65022 | 2024-10-18 00:43:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a5e1e560-eba6-3180-a5a6-f0b3564180eb | -3.13058 | -48.98248 | 2024-10-18 00:43:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 5e0138ce-5153-38b6-bf10-b2b1f76451ab | -3.1265 | -48.6516 | 2024-10-18 00:43:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9a1d4d84-9365-36d3-a870-93bfbbe05653 | -3.11984 | -45.90786 | 2024-10-18 00:43:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 748cb399-037c-34a1-836c-10e7596cdc5a | -3.08697 | -45.94528 | 2024-10-18 00:43:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6d7006c1-c8a6-3a98-b115-0280f008e10c | -3.07936 | -45.95533 | 2024-10-18 00:43:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d99725ba-07ae-35ad-9ee1-e663eaf0f9ec | -3.07813 | -45.94652 | 2024-10-18 00:43:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 22066ff6-ac14-3ecd-a3b9-d33ac8309473 | -3.07497 | -45.79451 | 2024-10-18 00:43:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1c0110c4-fdb1-35a2-a127-cf12ffe00595 | -3.06391 | -50.49818 | 2024-10-18 00:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7bfc4b92-fad5-3914-a94a-3cc51f19e14d | -3.05915 | -53.23496 | 2024-10-18 00:43:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 38607369-3fe2-3e19-8540-bf2a56b07c36 | -2.97603 | -49.27102 | 2024-10-18 00:43:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e36a67d7-8c81-3838-a90e-33c23aa5c3af | -2.9674 | -49.28458 | 2024-10-18 00:43:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 91f4fc4d-47b0-34d8-86a3-38d89672ace4 | -2.8973 | -51.67571 | 2024-10-18 00:43:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| f6332790-ade2-3182-af30-3d1fc7849b97 | -2.88945 | -51.68915 | 2024-10-18 00:43:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| dfd4b93d-658d-3e90-8cc3-d7c3447d6ce6 | -2.88745 | -51.69588 | 2024-10-18 00:43:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 2518ebb8-d845-34b5-a1fd-e936c968dd96 | -2.88701 | -51.67071 | 2024-10-18 00:43:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 699b79d0-6d90-304e-bec9-beff0bf90232 | -2.88487 | -51.67745 | 2024-10-18 00:43:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| f76ebf8f-2a79-3e6a-a8ec-ee6da6d92236 | -2.8772 | -51.62267 | 2024-10-18 00:43:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| ba4fdef7-e2e8-384d-95e8-c05792be3cd6 | -2.87559 | -48.91182 | 2024-10-18 00:43:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 491765aa-a510-3eb5-9a7c-bada33af58d4 | -2.87457 | -51.67242 | 2024-10-18 00:43:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 3ccd5a56-00f7-35a3-9557-a8599acc6b13 | -2.87457 | -48.90665 | 2024-10-18 00:43:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 59eb4141-5254-3a3b-af33-1fc1a083b06e | -2.87405 | -48.90033 | 2024-10-18 00:43:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6437c517-6435-35d7-8d7c-6fd0970f5fff | -2.87243 | -51.67914 | 2024-10-18 00:43:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 6f1c81f8-7414-353c-8f47-2cdbfed4d040 | -2.86988 | -51.66079 | 2024-10-18 00:43:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| dfa30381-6044-38e2-b045-0cf052675f1d | -2.86739 | -51.61769 | 2024-10-18 00:43:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 8bee709b-911a-312e-8825-010785ee9da3 | -2.84006 | -49.54192 | 2024-10-18 00:43:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| aaeea6d0-d242-3ae8-907c-c74476d7552f | -2.83831 | -49.52929 | 2024-10-18 00:43:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 60fc17e2-952f-30f1-bc91-113a50a37a3a | -2.8133 | -51.34237 | 2024-10-18 00:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 85fdf920-6cba-3434-9594-789825f70327 | -2.71499 | -54.65015 | 2024-10-18 00:43:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 85d6c2c4-1f91-3680-8000-90f16018eced | -2.70963 | -51.34488 | 2024-10-18 00:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 0fb93fd5-3bfb-3a59-a07c-1155ce7ae6d0 | -2.70528 | -54.65805 | 2024-10-18 00:43:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| fe406a2e-76bc-3d4b-be1f-10cf627268af | -2.63124 | -49.07031 | 2024-10-18 00:43:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d8c95a37-b38f-34c0-b838-ccfa3e95bfd1 | -2.61616 | -49.48281 | 2024-10-18 00:43:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 3433380a-17d7-35b9-9dae-9a72f8025611 | -2.60746 | -49.49672 | 2024-10-18 00:43:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 13f02aad-78bf-380b-a81e-7545d6954cec | -2.60578 | -49.48426 | 2024-10-18 00:43:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| cf85aa69-f209-3104-b5fe-57ff0498fbd4 | -2.59589 | -46.11708 | 2024-10-18 00:43:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9cfe9c1a-1983-3696-af4c-8ebc88928a19 | -2.57112 | -49.22855 | 2024-10-18 00:43:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| ddd5137c-a593-3787-bf25-15acf2db8f32 | -2.5695 | -49.21664 | 2024-10-18 00:43:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 448fb5c7-3ab1-32ba-82b7-46e6ab94e1fe | -2.569 | -47.05742 | 2024-10-18 00:43:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 730851e9-9eb1-3796-8a59-112583f2759c | -2.55798 | -48.45595 | 2024-10-18 00:43:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aabdf7de-1a7c-36fc-8e61-06ec68176244 | -2.54835 | -51.24051 | 2024-10-18 00:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 48afe4a2-9ad3-342d-9274-89aeaee3aa74 | -2.53765 | -47.22856 | 2024-10-18 00:43:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 16410cb4-f074-3e84-a02c-59c17e969860 | -2.53635 | -47.21923 | 2024-10-18 00:43:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 6bc29e69-30cf-3f4f-a401-19b44d0b5776 | -2.52185 | -46.05256 | 2024-10-18 00:43:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c310ba10-380a-39fa-86c9-949edc1f4c36 | -2.50607 | -46.19852 | 2024-10-18 00:43:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 27758694-755a-3f1a-91d1-4f1ff96829b2 | -2.48936 | -49.38144 | 2024-10-18 00:43:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 177b46f3-1e0c-350b-9ec3-971a24b2cfe2 | -2.46223 | -48.35638 | 2024-10-18 00:43:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |


[Clique aqui para ver as próximas entradas](README7.md)
