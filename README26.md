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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 477aace3-208e-35d0-b42c-cadd33bd3786 | -5.76195 | -46.66766 | 2025-08-18 05:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ad92869-c56e-3a7c-9473-d246756e57fc | -8.22411 | -47.29907 | 2025-08-18 05:12:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fc4c498-4350-338e-ae49-1eb2feab39c5 | -9.29438 | -50.27273 | 2025-08-18 05:12:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a04ed97-c732-3532-99a0-4f4a2cf6246d | -8.79784 | -52.06622 | 2025-08-18 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18ff08eb-7be3-3a80-a88e-1777bad5de74 | -8.19557 | -47.33585 | 2025-08-18 05:12:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6552fdc-450b-3af7-84fa-ccc56155883e | -8.2363 | -47.86278 | 2025-08-18 05:12:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5d41654-265d-3a86-aa6b-059ffe398ee3 | -7.07569 | -44.94069 | 2025-08-18 05:12:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1bbe827-bca1-34dc-bc9f-4878420fa431 | -6.43077 | -44.78476 | 2025-08-18 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8e7b53ad-1af7-3d79-9c49-bc9d8cc88c00 | -5.45147 | -60.12815 | 2025-08-18 05:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7954aa58-f3be-3a96-980f-e2d6fa476cbb | -6.13646 | -57.93533 | 2025-08-18 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8003ac9d-774a-3bb0-90cc-bde8e00f780f | -6.19142 | -53.51572 | 2025-08-18 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb49b50d-76cb-34bd-8fad-e05b49cb6b79 | -3.41126 | -52.60402 | 2025-08-18 05:12:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b14cee6-13b0-33c3-a9a2-4ed7a4e8306c | -7.54883 | -45.43367 | 2025-08-18 05:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9d392b9-c6f7-39e1-9502-ed3bfce89ff3 | -6.13312 | -57.93478 | 2025-08-18 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9cb17ad-b82c-35cf-9e3d-b18b97e29881 | -5.4547 | -60.1543 | 2025-08-18 05:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61899fdd-d6f4-3d65-b2b9-d46e706b7d96 | -6.1398 | -57.93586 | 2025-08-18 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c881cafb-2f69-3b7a-8ed0-d3af7db5cb73 | -7.91585 | -51.37288 | 2025-08-18 05:12:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5eb54446-ca3a-3570-af5e-48d691595a5e | -8.09057 | -54.99033 | 2025-08-18 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 084bcd17-0f6e-31f1-a32d-48bceb62e282 | -6.43742 | -44.78558 | 2025-08-18 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f4de77bc-e787-3bc3-9f25-8d4dd7b5f90d | -7.50782 | -44.98719 | 2025-08-18 05:12:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55b9f6f9-2f0f-3fea-af04-81b73b0ff5db | -5.45871 | -60.13197 | 2025-08-18 05:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dc5e31d-329a-3fcd-8e98-b68edbc76179 | -6.19076 | -53.52017 | 2025-08-18 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 94634a55-7ffc-3752-bc23-ec0adaac3020 | -6.13368 | -57.93128 | 2025-08-18 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 488bca19-5711-36d9-ba85-f7fe0a22fa9e | -6.14266 | -57.93327 | 2025-08-18 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3e63c2f-d4c2-3d63-ab01-e8579a433922 | -5.45013 | -60.13646 | 2025-08-18 05:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94f026dd-4e33-38c6-a331-be9a1e803fe7 | -6.43427 | -44.78502 | 2025-08-18 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 8ed2ee6a-377b-31ec-99dc-504ea96299ae | -9.86816 | -44.68782 | 2025-08-18 05:12:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4c21c55-3901-36f2-bbd9-53e141ed8561 | -8.82284 | -52.0423 | 2025-08-18 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc2e2296-69df-3d78-aad4-9562830ca7c9 | -7.55582 | -45.4351 | 2025-08-18 05:12:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e4871a6-0e48-32ac-bb30-53ba6600d988 | -8.49932 | -44.73944 | 2025-08-18 05:12:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a8bb2357-bf1e-399e-b894-7b177d01b398 | -8.22906 | -47.3013 | 2025-08-18 05:12:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1ac0f03-509c-3d2f-80d8-5728238651f9 | -6.56389 | -44.47511 | 2025-08-18 05:12:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0f2d4894-369c-352c-835d-4e8f2ce996c6 | -4.29567 | -48.06622 | 2025-08-18 05:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7bdf7584-b45c-3d25-81a7-108a7118a712 | -4.30135 | -48.06373 | 2025-08-18 05:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc8d49cc-2816-3e0e-9c81-a0dd4f6189a9 | -6.57152 | -44.46961 | 2025-08-18 05:12:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d7b1faae-f868-3500-918c-49885d5ef624 | -3.58978 | -47.52968 | 2025-08-18 05:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10a69865-07bf-3412-a019-1908bea0d784 | -6.13757 | -57.92831 | 2025-08-18 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfbd31de-8250-3cb6-ba1b-cc2e4d32c8da | -6.14878 | -57.93784 | 2025-08-18 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 546e78a9-ce30-34f6-b124-504d5100052f | -6.42058 | -53.37204 | 2025-08-18 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61e8dd46-fd3c-306f-a464-a766fa816302 | -8.82227 | -52.04625 | 2025-08-18 05:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2e8d15d3-b43e-30c7-b9c1-10a7e1d8bcd5 | -5.45832 | -60.15489 | 2025-08-18 05:12:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10bea1d1-ab72-305d-9b5b-3b1e25f4d189 | -3.59513 | -47.53043 | 2025-08-18 05:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df4f79e1-71ec-31a3-a666-2b5dc00a7764 | -3.73688 | -51.80655 | 2025-08-18 05:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c929f37e-dd5b-3304-9356-824fddafd48b | -5.76138 | -46.67181 | 2025-08-18 05:12:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b1911d50-f664-33e3-9aca-6d1cc0863db0 | -6.43 | -44.79047 | 2025-08-18 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 26688dd0-68a3-3e50-adc7-af08ebb02710 | -15.61166 | -54.30725 | 2025-08-18 05:14:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0385e403-bfe4-370c-b82a-460c0ca91c49 | -12.63755 | -46.89904 | 2025-08-18 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e7f920d-0830-321b-89ed-b282b4dae7cd | -17.09726 | -49.87563 | 2025-08-18 05:14:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0d64942-1236-3efd-816a-52f754174a83 | -13.23004 | -50.75718 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| cfe0d9b3-c6d0-3e92-8e78-e20b140d454e | -13.22091 | -50.75026 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| cea93cfb-1909-330e-8cdb-ae04ecd4fdaa | -13.59608 | -47.74445 | 2025-08-18 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd33335f-b707-361d-94a9-8133d3525448 | -13.1684 | -54.91778 | 2025-08-18 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c6442b45-8824-39ef-97d5-b90ff9cbdfe1 | -16.80088 | -50.09634 | 2025-08-18 05:14:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 390b8a99-aa55-3606-9b81-15ac57e2a520 | -13.58626 | -46.98804 | 2025-08-18 05:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34f70766-6b2c-38a5-a440-349fb2d70191 | -13.02036 | -56.85714 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf683622-be50-3e81-a2b2-82c42ca0b953 | -11.31061 | -55.21501 | 2025-08-18 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85b979d7-c1cf-3c4c-9166-1ea65f23f7f4 | -12.92896 | -46.11676 | 2025-08-18 05:14:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79914b38-2511-329b-a5ed-b489b1501d80 | -13.096 | -46.84704 | 2025-08-18 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aad670b7-cf04-301c-a225-e9e2ba7ddb17 | -12.98778 | -56.84507 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9abd2842-8edb-30b0-86de-6e5224330cac | -9.51555 | -60.53978 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a89ac36b-b136-353a-83b9-d79abac47f9d | -9.51183 | -60.51874 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c3f46c6-4f24-33d4-9fe7-502784b7c806 | -13.20538 | -50.75392 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 839bd357-31ec-3d79-adc5-8b33cffa02d7 | -13.22866 | -50.74066 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1d145832-2ebd-358d-b460-a8e37f953a33 | -9.51907 | -60.54037 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6492920a-1264-37fb-8817-1858319fd6b0 | -13.21889 | -50.77935 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 74229fd7-6d57-32ac-a87a-c7d2c3d11c8e | -13.22165 | -50.75688 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| cfe3375a-7207-3671-b090-2acaa5594718 | -14.6333 | -54.9113 | 2025-08-18 05:14:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9925f6e-eadb-3464-9d6c-947405057fff | -13.14037 | -57.1484 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3b64b73-f92e-317c-b955-82306bd7b594 | -15.00666 | -54.79839 | 2025-08-18 05:14:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2415602d-752f-3ada-81d5-6588f7480a89 | -12.92716 | -46.11413 | 2025-08-18 05:14:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0ad2130c-2540-366c-8d5b-51c61e89d619 | -13.58917 | -47.75142 | 2025-08-18 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59bec075-e254-3d29-93f8-b44b7261b6c6 | -12.63421 | -46.89765 | 2025-08-18 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2de4d10-7787-3c3b-8764-968a1619d010 | -12.98892 | -56.86073 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ea205574-4fea-3f1a-9c2f-e51097925fdd | -13.17149 | -54.92291 | 2025-08-18 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f889983b-7f1a-3aa8-b030-09191c2bf180 | -12.63188 | -46.89264 | 2025-08-18 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f807dc6-c869-307b-9daa-0f91cde63c2a | -13.23151 | -50.74596 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 6c709b74-23eb-3229-b399-0d1d8d080b05 | -13.01811 | -56.85362 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 657795d7-c1a5-33ab-bf57-f1cb1c4407ea | -13.22589 | -50.76316 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| f5a32ff5-7f28-3f3a-83ac-5c472e13d3c4 | -11.3152 | -55.21478 | 2025-08-18 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28290587-a225-39b5-a871-45cdf3f29d3e | -13.00152 | -56.84718 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84369c07-0238-3826-a94b-a27c48c79e4c | -12.99179 | -56.8418 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6385cfac-8a18-3b2c-afaa-54fba802056b | -15.72659 | -48.41957 | 2025-08-18 05:14:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7736662-b519-3770-86ee-7bf282e8ad40 | -13.14606 | -57.1569 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4849bf52-f13a-313e-88b7-7f67f0da6b49 | -14.9925 | -54.78656 | 2025-08-18 05:14:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 066f814f-0943-31fa-aa8d-1231ab76fe5d | -14.73209 | -59.67418 | 2025-08-18 05:14:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a81fd6ef-6c58-35de-aa65-0fe75ad9b1fc | -13.22727 | -50.75193 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| e1825cde-2974-3fbc-9f13-2aa4d0a00635 | -12.62862 | -46.89088 | 2025-08-18 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d374122-ee46-3ef3-bb3a-6be1c9971982 | -11.85468 | -51.58865 | 2025-08-18 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02b4f653-83e2-37b6-ae8b-32585dfa99f4 | -14.63464 | -54.90162 | 2025-08-18 05:14:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b447dbc2-6cf8-3700-992d-a6d0642c747f | -12.98949 | -56.85696 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dbf9d513-64a6-393f-84dc-faad605320c0 | -13.58267 | -47.75485 | 2025-08-18 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dece7073-c5cb-3ef4-8fd8-ef5ca30fa5ce | -13.0124 | -56.84496 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4eacde70-5859-3b91-908c-0deb03306bc0 | -13.02093 | -56.85336 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34ac93d4-e4eb-3a34-80c7-ad11dca6ca68 | -10.99897 | -45.65415 | 2025-08-18 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c254ce0d-44bc-3309-a1c0-2d6d68316aa4 | -11.75462 | -51.70872 | 2025-08-18 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 297fb263-9c51-315d-8cd9-0acfeecec8eb | -14.87027 | -59.60853 | 2025-08-18 05:14:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 390424ce-2be5-3c74-bda9-bd766124c5e6 | -13.12444 | -57.11541 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ab12391-fad9-3edd-8e10-3e9a3669a3f3 | -14.62879 | -54.91565 | 2025-08-18 05:14:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 04be7527-a15e-31ff-b99f-f0db2406cc85 | -13.22218 | -50.77893 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 10a770bf-ce10-3200-ab12-fd4319ffd52c | -12.99236 | -56.838 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README27.md)
