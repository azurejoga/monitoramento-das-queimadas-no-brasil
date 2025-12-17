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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53c7b3d6-6ebe-37fb-804b-8588d2bfbd8b | -2.9249 | -48.22677 | 2025-12-17 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f07c4201-c0d8-3484-b209-aad91268b079 | -2.22721 | -45.71814 | 2025-12-17 04:04:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2476d19f-b527-3971-9d97-ab70fabc215b | -1.45256 | -46.87877 | 2025-12-17 04:04:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 224d4012-bb42-33f4-918d-cad3cc48ec9f | -2.90358 | -45.58796 | 2025-12-17 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76cc57d4-748c-3b7b-b268-ff8f4885949f | -3.87376 | -40.44923 | 2025-12-17 04:04:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2a501090-629b-3e45-b89c-60b24b740c19 | -3.03213 | -45.34678 | 2025-12-17 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e39636a-18f2-3452-8a12-37aa8ec652bc | -3.20033 | -43.18694 | 2025-12-17 04:04:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e599a5c-10e2-30ec-b496-f4d1aba93438 | -2.62061 | -45.2253 | 2025-12-17 04:04:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 78b97132-2aa1-375f-b777-e7cb570da360 | -2.67109 | -44.94002 | 2025-12-17 04:04:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d55318e9-4bc8-303c-97c0-503d3a31d90b | -3.46654 | -44.93274 | 2025-12-17 04:04:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22407e80-c0f7-3941-81ad-aa64c16e7627 | -3.20987 | -45.57976 | 2025-12-17 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ef1c150-bd90-3ef9-be31-db1c541ab2ca | -2.434 | -47.19696 | 2025-12-17 04:04:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15b2e09c-c561-3080-b25b-53d4bd95302c | -2.9257 | -48.23411 | 2025-12-17 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8eac20d-a67e-36a2-8eb4-ad6dd637e359 | -2.9291 | -48.23414 | 2025-12-17 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4439388-8a36-3c8d-8eb6-0c144c5cc088 | -2.46738 | -48.11532 | 2025-12-17 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bed10182-4754-351d-8c28-49e911c6a526 | -2.88199 | -45.47028 | 2025-12-17 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 624f9438-6773-3e47-b854-fc03e3562d09 | -2.36725 | -47.68352 | 2025-12-17 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83a8d782-d63f-39b3-95db-aebaf0be9d49 | -3.34184 | -41.7966 | 2025-12-17 04:04:00 | NPP-375D | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9088bf3e-ed25-3ec5-89b3-beea49474105 | -2.41165 | -48.2866 | 2025-12-17 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3dd2057-d88c-317e-8420-ebea5a0ee32a | -3.36905 | -43.36203 | 2025-12-17 04:04:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2755968e-9abb-3125-a182-ee160d72d545 | -2.908 | -45.58871 | 2025-12-17 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 45f34bc3-64bb-310d-a00e-1cca73fb4c28 | -3.02644 | -45.35432 | 2025-12-17 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 348fb8bf-813e-33e6-a8f9-6c050cfe0e92 | -2.88638 | -45.47102 | 2025-12-17 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f00df24e-3577-38ea-a7d2-802392bdf473 | -3.42001 | -43.16424 | 2025-12-17 04:04:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 621ff020-b205-3156-9784-4b2983f9b8f0 | -3.31223 | -45.5048 | 2025-12-17 04:04:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5cf8e3aa-745e-31b5-8949-06d8f821399e | -1.4225 | -46.06802 | 2025-12-17 04:04:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 556e9799-635f-3937-bbff-4cd50d5dc20d | -3.35434 | -44.56248 | 2025-12-17 04:04:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c12b7172-2b20-3a74-bdbe-250f65426a63 | -1.41782 | -46.06725 | 2025-12-17 04:04:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ce1218d8-84eb-327b-b659-e815125e6174 | -2.36776 | -47.68046 | 2025-12-17 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9164aea5-91b4-35fe-9ef8-b2e24fe6b80f | -2.93077 | -48.22429 | 2025-12-17 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5bc58f4f-ccf2-3fcb-a863-4db9a2781f89 | -2.93344 | -41.14815 | 2025-12-17 04:04:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 00516fdd-fb42-3a33-8f8f-7aea89f7bbc2 | -2.93496 | -48.23171 | 2025-12-17 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09a6b218-a130-39f6-b4a2-202b40fdd0ef | -2.94419 | -40.4445 | 2025-12-17 04:04:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c3dc444b-a9f3-3126-affe-cec229540060 | -3.86984 | -40.45222 | 2025-12-17 04:04:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d8c60894-056c-380d-82fb-b1897eb7783a | -2.73418 | -45.30158 | 2025-12-17 04:04:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe08f10b-24af-38b2-a1ef-74c9777d5ce0 | -2.3662 | -47.68312 | 2025-12-17 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e8fd12a-486e-30d6-b47b-307beea3e43d | -2.04537 | -45.45227 | 2025-12-17 04:04:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffafa0f4-9bdb-3511-8c60-f178f993a6b1 | -2.23057 | -51.93924 | 2025-12-17 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1fb537d-a447-3dc2-b168-f888ec2a8b86 | -3.03146 | -45.35089 | 2025-12-17 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8452d65-d33e-33e5-afa7-61ef2c75501c | -3.95196 | -40.93794 | 2025-12-17 04:04:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aafe158c-2856-3f16-be87-7ffd48d1c938 | -2.92545 | -48.22352 | 2025-12-17 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 973724db-e0de-3675-81c6-c7910fc34c41 | -2.88268 | -45.46608 | 2025-12-17 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a84b7b9-074f-3d55-b25e-08ad4b451b8c | -2.43897 | -47.19784 | 2025-12-17 04:04:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a12177f6-580e-36bd-9316-b7b39942fa03 | -1.66083 | -45.89314 | 2025-12-17 04:04:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad2e73ae-df1d-3d0c-b4f0-cd8353133f3b | -4.33472 | -39.14658 | 2025-12-17 04:04:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d94203b1-63c9-3734-9546-05d7aa66af84 | -2.9273 | -48.22425 | 2025-12-17 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a6d4fe2-553f-317a-8d5f-41486bd9c475 | -3.02768 | -41.12505 | 2025-12-17 04:04:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 01813065-9d16-37e4-9cbc-cd38546ca525 | -2.92677 | -48.22752 | 2025-12-17 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7b2bdb8-db43-3a4e-8c79-801e51358b3c | -2.3667 | -47.68004 | 2025-12-17 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88ff91cb-dd99-36b6-bd49-c5cf25795850 | -2.23281 | -45.65459 | 2025-12-17 04:04:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d8985da-0fa1-3e4b-b2b5-1fbab5107ad7 | -3.20384 | -43.18882 | 2025-12-17 04:04:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a61cb56-8ac1-34bc-8d0a-8bdbb1b19a97 | -2.63415 | -45.66716 | 2025-12-17 04:04:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d131dab7-c5af-3672-a887-be93ba8de799 | -2.61995 | -45.22938 | 2025-12-17 04:04:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f5556518-5913-30f5-9ba5-aa1d1ce9e68c | -2.43856 | -47.19859 | 2025-12-17 04:04:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1048fbb2-dd6b-3321-a49c-87d251c8294e | -1.41938 | -46.05745 | 2025-12-17 04:04:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c875fa3-fca3-3bca-9b56-5853bcdf0798 | -3.46235 | -44.93206 | 2025-12-17 04:04:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13d2d695-4525-3202-9cc6-b4c6bf42e10f | -2.93403 | -41.14444 | 2025-12-17 04:04:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ebe69eb9-3349-3596-b427-5cb91bd6b03b | -3.33094 | -45.41814 | 2025-12-17 04:04:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58dd3f25-743c-3ef6-ba9e-09a13d7dc361 | -2.92624 | -48.2308 | 2025-12-17 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23e6fb82-ffb4-3b68-8182-d112ecd4c033 | -3.03647 | -45.34749 | 2025-12-17 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1e769ee-d835-389a-a7a0-1188c229be58 | -3.33026 | -45.42228 | 2025-12-17 04:04:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5981733e-ad8d-3226-9ea3-dc15cf23b30d | -1.4186 | -46.06236 | 2025-12-17 04:04:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ceb57a1-40f6-3499-a139-de48ee9ac237 | -2.62969 | -45.66641 | 2025-12-17 04:04:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c6c99ab-baca-3a43-bcc5-7ee7fec72cfb | -3.25358 | -41.4197 | 2025-12-17 04:04:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 339a7bb2-458a-307f-b9a6-8986bec7340a | -2.05051 | -45.44865 | 2025-12-17 04:04:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84138b17-cc7c-367b-81b1-66173877624d | -2.47213 | -48.11956 | 2025-12-17 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a68cefc-2233-3489-8328-9f044b1f840c | -2.94755 | -40.44502 | 2025-12-17 04:04:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4736e887-5ba3-3b58-95f4-8220e4726578 | -3.42376 | -43.16484 | 2025-12-17 04:04:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6afd8ee-2b30-3671-b778-18e76afa4c8d | -2.41221 | -48.28324 | 2025-12-17 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ca28830-a6ff-3dbf-9926-b95aacbbb076 | -3.12174 | -40.99664 | 2025-12-17 04:04:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 02672a73-8e0a-3c1c-bf3d-da66f6fa5e7e | -3.30839 | -39.27898 | 2025-12-17 04:04:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6f38214d-eb70-33e3-896d-0b2f1699a122 | -2.20393 | -45.71883 | 2025-12-17 04:04:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09b62134-34ee-3aea-986e-1000dc298c18 | -2.90427 | -45.58367 | 2025-12-17 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca36db7c-42e7-3360-b78e-56f0799937c1 | -2.93022 | -48.22755 | 2025-12-17 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8fb9078-8b80-3bd4-8abd-72a396203e78 | -2.43359 | -47.19771 | 2025-12-17 04:04:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4bcd0118-e369-30a6-ab0a-3c12c0c4db5b | -3.02712 | -45.35019 | 2025-12-17 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88df59f8-94cd-3489-a1fe-e68f8f6dce1c | -2.9704 | -41.74932 | 2025-12-17 04:04:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1982808f-2dbb-3f0d-b44a-c963df4283c1 | -3.95592 | -40.93487 | 2025-12-17 04:04:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 65cedff4-be83-3bc9-b009-9da56e2dc97e | -4.33526 | -39.14312 | 2025-12-17 04:04:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 29d78eaa-5ff1-39fe-8f59-cbf28483dffe | -4.33139 | -39.14606 | 2025-12-17 04:04:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c2a3b0ac-6041-3037-8dab-39b7f3808faa | -4.43512 | -38.46357 | 2025-12-17 04:04:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 39357780-ba4a-3cc0-b912-5b7b30cb0bde | -2.89916 | -45.58722 | 2025-12-17 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1eaa0536-89bc-3e32-96bc-a70bd29c6637 | -1.91691 | -45.24379 | 2025-12-17 04:04:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80d0b02c-f369-3209-ada5-d22b58953dd6 | -4.33055 | -44.82149 | 2025-12-17 04:06:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8d50028-b7c1-3bb8-af1d-44b26a22b4d7 | -5.90645 | -44.35857 | 2025-12-17 04:06:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 908df6f2-d82d-3282-85ef-4e78e02f30e3 | -5.3641 | -36.84105 | 2025-12-17 04:06:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 883276df-43fe-37d8-8a7a-5940c7457e32 | -9.26439 | -44.314 | 2025-12-17 04:06:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 140af117-e9e3-37e5-b920-4fae97bb4f7a | -5.47864 | -45.4072 | 2025-12-17 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8871a9fc-ba95-38c9-be01-6f7c6fac2632 | -4.33333 | -45.87998 | 2025-12-17 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b41806b7-8252-389a-866e-b76720afbfef | -3.21706 | -49.36659 | 2025-12-17 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d24fb07-6825-3369-9d04-72404709a920 | -3.84265 | -47.06097 | 2025-12-17 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9be92854-1e01-3eb6-aaf7-ba831eb44882 | -5.44547 | -43.51809 | 2025-12-17 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6ff945c6-3f23-3e25-b148-451ac801dde7 | -6.20774 | -39.73598 | 2025-12-17 04:06:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5d08c879-e592-35a7-923f-59380947772b | -9.16735 | -35.68739 | 2025-12-17 04:06:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3064adcd-2765-3f6e-a18d-0b72506f6102 | -9.81794 | -43.9312 | 2025-12-17 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26ab691f-726f-3b45-b594-05450ed92430 | -5.5722 | -43.59285 | 2025-12-17 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4a3bce5-c22d-3971-b574-b4dc271fe0ad | -4.32995 | -44.82519 | 2025-12-17 04:06:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b83bd003-8c33-3a5a-a4e7-57f4e8e45b7d | -5.5546 | -35.72449 | 2025-12-17 04:06:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eaae4418-1b9e-3264-b882-6ba99c2f1143 | -9.81722 | -43.93541 | 2025-12-17 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64c1a6dc-11a4-3b29-8343-73520bd9b90f | -9.0049 | -45.9245 | 2025-12-17 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README6.md)
