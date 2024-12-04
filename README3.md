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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2aef4bc5-aaf9-35b0-a100-d6b9ba21d550 | -3.8621 | -50.879398 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e39fcf29-44f8-36a9-bf33-0d1d4316b477 | -3.1659 | -44.43 | 2024-12-04 00:17:00 | METOP-B | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 17f2b471-7444-3ad3-9b1b-37cd4aec6acd | -2.637 | -45.729801 | 2024-12-04 00:17:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fdbe12f1-e5bb-38be-9d80-8f06960c6138 | -4.322 | -48.087898 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33df0c53-e53a-368f-8d83-3daa4a78a537 | -5.5744 | -45.138199 | 2024-12-04 00:17:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 735bd239-da3f-3a3f-a588-ce9e8cd94193 | -3.2473 | -53.623501 | 2024-12-04 00:17:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd613321-70f1-3a2b-9d9e-3fb9d90ea341 | -2.823 | -49.809601 | 2024-12-04 00:17:00 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77cab37c-1d7e-3410-b56c-80c1f7e42a9a | -3.678 | -50.232899 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32e504fa-0b94-37e2-96d0-c515c5ee134f | -2.6735 | -45.209499 | 2024-12-04 00:17:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c2af45a1-98fc-3d2c-aee2-5720d09b5ac6 | -6.2505 | -43.540699 | 2024-12-04 00:17:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10f5caf8-213d-30a5-bb2f-8111d18c42da | -2.8245 | -46.7407 | 2024-12-04 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4db5d01-6cef-3370-9d21-7c454ff9de79 | -3.3264 | -50.038101 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20daea61-f488-3611-8845-368014480129 | -2.662 | -46.113499 | 2024-12-04 00:17:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0d0027e3-131a-3618-9680-5c110e373be8 | -2.6354 | -45.722698 | 2024-12-04 00:17:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 21e962db-4e5c-31e3-86cc-8a8d5e97d517 | -2.6768 | -45.224098 | 2024-12-04 00:17:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dcd5f6a3-591e-3454-883a-451879960f17 | -1.4791 | -53.769798 | 2024-12-04 00:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18dedc74-1f97-39d3-bd2d-84d12ed79622 | -3.3282 | -50.046299 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d746f79d-01b7-3e57-8794-a2114007d0b0 | -3.3436 | -49.745602 | 2024-12-04 00:17:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3e0c3be-e6d7-30b8-8441-95f4204331ef | -3.7021 | -50.434898 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8f9ff01-9c33-31e9-9ee3-67b8b5eab8a0 | -2.3975 | -45.355301 | 2024-12-04 00:17:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 04bcbb13-e281-3c85-90ab-a44ed9dd17a6 | -5.694 | -45.029301 | 2024-12-04 00:17:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8f5623d-da9d-3b4c-91f6-921537fd2afc | -2.6507 | -46.108799 | 2024-12-04 00:17:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fa1879df-3f59-3b0b-b3f4-b93d371190fc | -2.4667 | -46.526001 | 2024-12-04 00:17:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5301c82e-ad01-3537-bf46-c954f0464c87 | -3.7515 | -45.599201 | 2024-12-04 00:17:00 | METOP-B | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 91b0e307-1b89-356f-b919-1613f5de56f5 | -2.675 | -46.125198 | 2024-12-04 00:17:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b1c0d0be-0c28-34ed-a2f8-87955122fd77 | -2.8793 | -51.771999 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc5bbcfc-b057-3ffe-aef7-2e004a550e4a | -3.5147 | -52.141399 | 2024-12-04 00:17:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 235ea735-e4eb-3e9f-b9da-2846ab569d97 | -6.0931 | -48.045502 | 2024-12-04 00:17:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de73b911-adc7-335d-a79a-47cf4c09cb85 | -2.6912 | -45.650799 | 2024-12-04 00:17:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 60d875a7-d40d-3b30-9fa7-1f5438d2c9e7 | -3.5864 | -50.514999 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af50e53d-7cb3-3872-91f8-9f2bcd19f7eb | -3.9357 | -46.916302 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 90ef8f39-dd7b-35ac-8920-43642703d5dd | -1.4723 | -53.785 | 2024-12-04 00:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51c5b81e-f965-3548-86f4-1d916c572b12 | -3.4707 | -50.224899 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2e08498-6209-3346-8519-e8cb60b38751 | -3.7823 | -46.692699 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad2cbfc9-300c-3d70-9f8e-ac9555bbae9c | -4.3075 | -48.068699 | 2024-12-04 00:17:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a30f87b-5ba3-3c0c-beb2-52a0ce70fa81 | -2.6766 | -46.132099 | 2024-12-04 00:17:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ca8a86c7-12f0-3904-8b0e-b6eca5f6303f | -2.6795 | -46.600899 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2d238b8e-de3a-371a-92ea-1f4e6737d9b4 | -2.0975 | -46.579201 | 2024-12-04 00:17:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54bfbcda-d804-39e2-a8a3-26817c3c108a | -2.8135 | -54.113201 | 2024-12-04 00:17:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d61ae74-7c5a-3b5e-af99-5854baf9c615 | -4.0351 | -46.8083 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1e4a5621-b799-3e12-afb8-e7ecb9fd5a3e | -2.5901 | -46.5704 | 2024-12-04 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25d3d9ba-6884-3c0c-ae2b-8bc53cbfc078 | -3.476 | -49.971001 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e14ae4ab-f2c8-374a-96ef-0d72f73e5d8c | -2.8078 | -45.4828 | 2024-12-04 00:17:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3abe84a8-f757-3710-a46a-c553b4117baa | -3.1739 | -44.420101 | 2024-12-04 00:17:00 | METOP-B | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 028a6799-fed6-3a7f-a7fa-a0aba4c56800 | -4.4193 | -46.730202 | 2024-12-04 00:17:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 468ce1a6-31ac-3a33-ac13-d3752ed2b5f4 | -4.3685 | -43.337002 | 2024-12-04 00:17:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98bd8521-25da-3cac-9a5a-6a5be62ae7b5 | -4.3803 | -43.343102 | 2024-12-04 00:17:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 70cb878b-fadf-30b5-a99f-2a14e6904514 | -4.3626 | -43.355999 | 2024-12-04 00:17:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 083ccf35-84b1-39ea-b5da-9f0780a64d52 | -3.3945 | -50.2062 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a940be40-390f-354b-8400-0f3d2eecc3e8 | -3.1169 | -45.983002 | 2024-12-04 00:17:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4d50ed6c-be1c-39ab-a662-cb9f473e1520 | -2.6149 | -45.4053 | 2024-12-04 00:17:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4d7b5f03-e797-30ae-9fcb-fd150cc3396d | -3.8435 | -46.507198 | 2024-12-04 00:17:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 608b39dd-0aaf-378a-8167-5d6b1923c44d | -2.681 | -46.6077 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1d8e396-4bc4-36b3-a5d1-c5a51cbcb89f | -2.1978 | -45.656502 | 2024-12-04 00:17:00 | METOP-B | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 30580c1e-d118-3955-8127-b76866203ee8 | -1.2345 | -51.579601 | 2024-12-04 00:17:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 775f522f-de88-33cc-bb7d-5a7842928063 | -3.8649 | -48.3456 | 2024-12-04 00:17:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bfa4560-b491-312b-b9e3-c5b86f680dc9 | -2.5281 | -45.567799 | 2024-12-04 00:17:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9855b647-292d-33c9-9c49-bdcd88fb96bc | -3.1677 | -54.2841 | 2024-12-04 00:17:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd2e82d6-5ccc-3328-b4b9-4c262f844b25 | -2.0215 | -45.515099 | 2024-12-04 00:17:00 | METOP-B | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6264d75b-8c07-3735-ab5e-e64d89a43e63 | -3.4963 | -49.923698 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c77b38a3-f1b1-35cc-9d29-d3574beec2de | -3.0985 | -54.572701 | 2024-12-04 00:17:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebdae273-83ca-3827-8563-533f1030a271 | -4.0082 | -48.8032 | 2024-12-04 00:17:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53f9bb49-13c3-3275-ba1f-fb727ec60ac3 | -3.5379 | -50.157299 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa064c72-5e46-3fa2-8318-916ef5876e9c | -2.6661 | -52.428902 | 2024-12-04 00:17:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d28b99a-7140-3f59-a944-41982a340283 | -4.3165 | -48.201302 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b304e54-d7ba-30d7-9436-693660cd3274 | -3.8496 | -52.126598 | 2024-12-04 00:17:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 516f002b-455c-367f-b472-27d68ee7bafe | -1.4664 | -53.758801 | 2024-12-04 00:17:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ded6135-276f-3965-bcdd-ffb6a7f8f05b | -2.6521 | -46.570999 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2e793953-3bbe-3e5f-aca1-3e2009e19186 | -2.6712 | -46.609901 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c9f1cb26-496b-3ed0-b911-043add99437a | -2.9702 | -44.9734 | 2024-12-04 00:17:00 | METOP-B | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4101e54d-18b0-3a2f-8c80-641a9deed273 | -3.805 | -46.931 | 2024-12-04 00:17:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b19cdb38-7f2a-3201-8530-d0b6a28cb81d | -5.9732 | -45.3507 | 2024-12-04 00:17:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c67b3da-e1ef-3716-a999-d1100a071150 | -4.0065 | -48.7957 | 2024-12-04 00:17:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b8bed6b-de39-3244-a577-bdbce3823ee3 | -3.9689 | -50.3405 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de7bc98b-0e2c-3756-9f0c-359a05e0336c | -6.2744 | -44.725601 | 2024-12-04 00:17:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 811c3286-5bd1-39e3-a080-4f32fb0a188d | -4.3861 | -43.368301 | 2024-12-04 00:17:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c821959-f401-31a9-846c-8458b12f9833 | -3.5098 | -51.2827 | 2024-12-04 00:17:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7d6104a-fcb1-3e11-9e38-f3bba5bbb185 | -2.5788 | -46.5658 | 2024-12-04 00:17:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec7924cd-1d43-31e1-8122-d47e5a8c213e | -2.0493 | -46.503399 | 2024-12-04 00:17:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f2d239e-6a21-3421-8d32-2a80c474ebe2 | -3.7002 | -50.426201 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 820239f3-cd5c-305f-9473-11c0b56e8b37 | -4.9165 | -47.845501 | 2024-12-04 00:17:00 | METOP-B | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9dfac7d1-583d-3647-aeaa-17b3c0d17b72 | -1.6567 | -52.730598 | 2024-12-04 00:17:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfa8f703-a9c6-3144-9e0b-78a07bb72b10 | -2.6734 | -46.118301 | 2024-12-04 00:17:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cafc2b9f-4e09-3025-ac35-01cee4c0aaab | -3.5477 | -50.155201 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e6914c1-6835-3aff-9547-52d4cdb9af15 | -3.7842 | -50.945 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67f87e3a-1532-307c-bb62-5d34ee1e001d | -4.3841 | -43.359901 | 2024-12-04 00:17:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30489ff7-3b14-3ece-b8d3-a55234949474 | -5.9693 | -46.292 | 2024-12-04 00:17:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ba90516-827a-346b-9c39-6daca5537f29 | -4.3067 | -48.2034 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c83005b5-fe72-3d1d-b1cc-63c179f843cf | -2.7972 | -53.020699 | 2024-12-04 00:17:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 182e565a-849a-3324-a038-fb1c1c0fb643 | -3.3733 | -51.083099 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecaa9916-cb43-3301-9b3c-15162c7a2a72 | -4.6832 | -45.6623 | 2024-12-04 00:17:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bb0080b0-f2ff-301d-ae46-2dc0ad9f7da8 | -3.1001 | -49.437599 | 2024-12-04 00:17:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5250c14-29a1-375d-b45b-916ac65c827e | -3.2879 | -49.172798 | 2024-12-04 00:17:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 086c39dd-3a7f-30ec-86fc-c043524d0de9 | -2.9614 | -45.206299 | 2024-12-04 00:17:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 62171909-ecce-3259-8e6a-1dd7d99a2bb4 | -1.7272 | -52.587101 | 2024-12-04 00:17:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 083d0285-0a31-33bf-bc33-92740ff4d7bf | -3.0456 | -44.987499 | 2024-12-04 00:17:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3219ac7e-76db-30e9-bee4-15e1c08f02e2 | -3.3222 | -50.2043 | 2024-12-04 00:17:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f291d326-8f8a-344d-986a-bda44b266230 | -4.3318 | -48.085701 | 2024-12-04 00:17:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d302c41-1109-32c6-a9a5-820092a352a0 | -1.508 | -46.753101 | 2024-12-04 00:17:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d85797b6-46fa-311a-abf8-55e84beff158 | -3.1983 | -50.617802 | 2024-12-04 00:17:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
