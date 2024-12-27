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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3940839f-a41a-37a2-8783-4e9d80e23ae8 | -3.0794 | -41.8955 | 2024-12-27 00:02:00 | METOP-C | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| af24a8bb-f28c-353b-8f43-7f9d185c24b7 | -7.2 | -35.046799 | 2024-12-27 00:02:00 | METOP-C | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4159811e-9053-3719-b78c-370ae4701c1f | -5.2185 | -41.254601 | 2024-12-27 00:02:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4995e800-0b45-30c2-aac9-7cd67fc49986 | -10.8707 | -37.2691 | 2024-12-27 00:02:00 | METOP-C | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 622edf50-1efb-3e7a-a207-2f16bc70d666 | -5.6135 | -38.990299 | 2024-12-27 00:02:00 | METOP-C | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f01026f3-c296-3782-9e1c-06b2343c8e71 | -3.0063 | -48.0466 | 2024-12-27 00:02:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdbbf497-891b-355b-a5f2-b0afc052adb8 | -7.0251 | -39.3559 | 2024-12-27 00:02:00 | METOP-C | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 77d15492-7837-35a9-93d6-3349e8b85e24 | -10.8723 | -37.2761 | 2024-12-27 00:02:00 | METOP-C | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f6dcd08f-41de-3bdf-96df-d72562eec933 | -3.0315 | -40.323898 | 2024-12-27 00:02:00 | METOP-C | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2ec22f37-8f92-345f-94b6-9de2a7c5c350 | -5.134 | -43.226002 | 2024-12-27 00:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c556afa-c87d-371b-b22b-a64614e8f0de | -12.2021 | -41.353699 | 2024-12-27 00:02:00 | METOP-C | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6f0f21fb-975e-38c5-a199-91a58acf6590 | -4.2025 | -43.693501 | 2024-12-27 00:02:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fca6f540-e361-3236-869d-1779a340f351 | -3.4162 | -44.898701 | 2024-12-27 00:02:00 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9aee74ef-a574-3382-8861-a8f4749868dc | -3.868 | -45.365398 | 2024-12-27 00:02:00 | METOP-C | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 851248f3-db66-3c12-a242-576ae672d723 | -7.0235 | -39.348801 | 2024-12-27 00:02:00 | METOP-C | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4dbbd3f0-af51-33b1-ab9a-f07f8c2484f4 | -5.3661 | -39.352699 | 2024-12-27 00:02:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 094f630f-488a-37ff-99b9-71a5d5979afc | -4.5364 | -42.064098 | 2024-12-27 00:02:00 | METOP-C | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8f39e36c-084c-389f-9bc1-ce18fcc4a878 | -7.3957 | -42.794498 | 2024-12-27 00:02:00 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 77daacba-056b-3a05-8d0c-e66148d3b2bd | -5.3997 | -42.943802 | 2024-12-27 00:02:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 9943088d-e4b6-30b9-90b8-401b17ac61ab | -5.232 | -41.2687 | 2024-12-27 00:02:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e8d55bad-cb1c-3b2e-86b1-82d6c5480ce9 | -5.2338 | -41.276798 | 2024-12-27 00:02:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2ae1b346-9334-3df2-bcc2-802f3bf9553a | -2.5851 | -45.983501 | 2024-12-27 00:02:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b8a710c1-4dc0-3437-9d26-15679b81db52 | -9.9966 | -36.016499 | 2024-12-27 00:02:00 | METOP-C | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 617bfe05-7269-3081-b0db-3bc7a792b85f | -7.3934 | -42.784 | 2024-12-27 00:02:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f86e1778-8ab0-3dda-be5e-7a38940a732e | -5.9182 | -43.483299 | 2024-12-27 00:02:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d410647-e4fc-381b-a01f-1b41a4f00eb2 | -9.8314 | -36.374298 | 2024-12-27 00:02:00 | METOP-C | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a8ab9893-ea8f-3a8e-a2c6-01a0e08681de | -4.4361 | -46.551399 | 2024-12-27 00:02:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 49e2009a-8aae-3d02-b6dd-ea372c53d02c | -2.0386 | -46.462101 | 2024-12-27 00:02:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d32814aa-cde4-3317-a160-4cc24fd7728b | -10.8048 | -37.160198 | 2024-12-27 00:02:00 | METOP-C | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 77d818e3-2d1a-3720-b234-a69754987a02 | -8.6318 | -40.474499 | 2024-12-27 00:02:00 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 69d6ee3d-585a-367a-9a04-3a121af62206 | -2.2865 | -45.5667 | 2024-12-27 00:02:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 31442b0f-354a-3ced-b237-e8878f2ff51d | -3.9506 | -46.982899 | 2024-12-27 00:02:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3c7a97d1-49d7-3bfc-9733-4b8c6002ce19 | -17.730801 | -40.196999 | 2024-12-27 00:02:00 | METOP-C | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 04267d61-5da6-350e-8942-74599eb50540 | -3.4134 | -44.886101 | 2024-12-27 00:02:00 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2411be28-41e5-385e-8ba3-378695ef144a | -5.3976 | -40.678001 | 2024-12-27 00:02:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 918141fa-ae86-3890-83f8-321bcd9b88c1 | -2.0483 | -46.459999 | 2024-12-27 00:02:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 258a089f-3bf1-3ceb-ad4f-55344ab41b90 | -3.9272 | -46.969299 | 2024-12-27 00:02:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2a59f46b-e39f-30bf-be8d-a6ba8d3f8d7b | -5.6664 | -39.3596 | 2024-12-27 00:02:00 | METOP-C | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 35694c57-0bf7-388f-9f3e-dc9187cc951a | -5.2496 | -41.393299 | 2024-12-27 00:02:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0eb9b879-586a-3e01-8654-c5e0d2ad2b24 | -7.6655 | -38.678699 | 2024-12-27 00:02:00 | METOP-C | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 2ec77411-09bd-3f9b-aff6-aeb8bb7bba71 | -4.2569 | -41.917599 | 2024-12-27 00:02:00 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 03c80769-706c-3b83-b9ac-8c1ef40ef6e7 | -10.544 | -36.9646 | 2024-12-27 00:02:00 | METOP-C | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7775899c-53b3-3069-8e25-b7da8ad9e694 | -10.8032 | -37.153198 | 2024-12-27 00:02:00 | METOP-C | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d0fc5a73-7e7f-3427-a7dc-9dff1984459a | -4.0372 | -46.175201 | 2024-12-27 00:02:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 38086665-0c02-3577-81c3-d15d99d2cbe0 | -4.0337 | -46.1595 | 2024-12-27 00:02:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 95bcd377-d866-31e6-b131-b5562e3e975f | -6.0376 | -39.7714 | 2024-12-27 00:02:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 416a450a-00f1-3111-9223-75f0dee4d16b | -9.1916 | -35.572201 | 2024-12-27 00:02:00 | METOP-C | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 26ec75e2-a56e-3fff-ad13-008560426ddc | -7.259 | -38.9314 | 2024-12-27 00:02:00 | METOP-C | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| da73a172-d107-3d83-9eed-2507d783af73 | -4.5345 | -42.055401 | 2024-12-27 00:02:00 | METOP-C | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ba3c018c-fc89-3aeb-a95b-dbfbb64e4ea6 | -5.6496 | -43.705002 | 2024-12-27 00:02:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 190957c1-458e-3356-8839-26e0914a2eba | -5.6448 | -43.729801 | 2024-12-27 00:02:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7ca7b0d-5672-3685-a707-c8039c836efd | -3.0356 | -40.0252 | 2024-12-27 00:02:00 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2d3abd73-6820-3a12-ad5c-f8147301629a | -2.2895 | -45.580101 | 2024-12-27 00:02:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 768ce9ee-32dc-3123-bab5-e2b32ee50cfd | -3.0017 | -48.026199 | 2024-12-27 00:02:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f92d7f1-1964-36c0-8196-bb517249c255 | -7.31 | -34.987499 | 2024-12-27 00:02:00 | METOP-C | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fa524854-768e-3978-a21d-a4ab005971bd | -9.82 | -36.369598 | 2024-12-27 00:02:00 | METOP-C | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c08c6b29-2e86-30f5-b63d-53977fb773c7 | -4.2588 | -41.926102 | 2024-12-27 00:02:00 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5c320f65-62d9-3906-bb52-9328375ee90d | -10.5424 | -36.957699 | 2024-12-27 00:02:00 | METOP-C | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 14ca1d4d-8e4b-301b-b819-78c7c0c29280 | -10.4997 | -36.996601 | 2024-12-27 00:02:00 | METOP-C | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ca5b0320-9ce2-3106-926f-7ba788ff5ea2 | -5.1538 | -39.370399 | 2024-12-27 00:02:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b2bea729-348e-3e62-9f8d-3ec28cf7c20d | -8.7837 | -41.2621 | 2024-12-27 00:02:00 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a816c8a7-dadc-3bd8-8971-e61e14d34318 | -4.5266 | -42.066299 | 2024-12-27 00:02:00 | METOP-C | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e844537d-8b26-378d-a64b-3f7fde292755 | -3.1993 | -45.988201 | 2024-12-27 00:02:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f7e6ace1-da5b-3147-8277-cb0e7e7bdee3 | -7.3216 | -34.993198 | 2024-12-27 00:02:00 | METOP-C | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c8b56544-ae35-3da1-b10d-7968e344ca7e | -3.7076 | -43.406601 | 2024-12-27 00:02:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8ffa5d8-121c-3602-961c-c15dbeff0292 | -4.5305 | -42.083801 | 2024-12-27 00:02:00 | METOP-C | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6670e893-e8af-3b72-bf9e-57d89db8ddea | -8.7857 | -41.271099 | 2024-12-27 00:02:00 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e70ade73-cb24-3d1b-8aab-5c04787c55fa | -3.196 | -45.9734 | 2024-12-27 00:02:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 32b3fc85-d94c-338b-b08c-bb2f2db5f5fe | -10.2863 | -36.4683 | 2024-12-27 00:02:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1a3b4944-7a39-3962-9dba-cc59393ce650 | -10.7299 | -37.148102 | 2024-12-27 00:02:00 | METOP-C | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fb25e95e-6799-304b-ad5c-0fd2dd5b7d2a | -5.3629 | -39.338699 | 2024-12-27 00:02:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ca62faa9-1f29-3d78-80a4-881c7954e9ca | -4.43 | -46.570499 | 2024-12-27 00:02:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d81eeca8-f194-3436-97dd-600501f6fb5c | -5.6151 | -38.997299 | 2024-12-27 00:02:00 | METOP-C | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 51bacc80-c71a-37b6-9f02-b6069432a477 | -5.906 | -43.4743 | 2024-12-27 00:02:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de0f5f41-cadc-3ef5-9b52-a3e2e3b5f2cc | -5.6594 | -43.7029 | 2024-12-27 00:02:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d45f3a87-4dd9-3f1d-9fd7-990d760f9b33 | -3.9409 | -46.985001 | 2024-12-27 00:02:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7f0714b8-3336-3a7b-8d3f-4a1c65359bd6 | -3.9369 | -46.967201 | 2024-12-27 00:02:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eb85a13c-a84f-3a72-bd84-12f24bc60909 | -9.657 | -36.1101 | 2024-12-27 00:02:00 | METOP-C | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6840b7a4-510d-3d0f-9f76-ce962f8dc6c6 | -7.3119 | -34.995499 | 2024-12-27 00:02:00 | METOP-C | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 21d623a0-8df6-35ef-8c71-e5d0ac5f20bf | -2.9865 | -54.617199 | 2024-12-27 00:41:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33292115-ed5d-3c60-ae1d-3a8c8a3f40a6 | -3.9339 | -46.9697 | 2024-12-27 00:41:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dd8db76f-c428-3985-a147-2071f82ebe48 | -4.5158 | -42.054699 | 2024-12-27 00:41:00 | METOP-B | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 33e7d503-8740-388f-9a0d-c66280d1a1a8 | -3.9272 | -46.984901 | 2024-12-27 00:41:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9905a12f-d54b-3006-87a9-1c6e648870b9 | -2.985 | -54.610199 | 2024-12-27 00:41:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16b460fa-3323-3e9f-9aea-2955540df839 | -4.1921 | -47.9851 | 2024-12-27 00:41:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b06f5e2-238c-3e67-b7c3-f88f684e5e95 | 2.9213 | -60.290199 | 2024-12-27 00:41:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5201e495-7cf2-301f-8fb9-af1872e79829 | -5.64 | -43.679798 | 2024-12-27 00:41:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed55ede2-1883-360d-b1ea-62d976f7120e | -2.2849 | -45.579399 | 2024-12-27 00:41:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a16e16c5-7b15-3f16-b306-1afd8dcb843e | -1.5607 | -53.500599 | 2024-12-27 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 629a617a-39a5-32b5-8c98-49908fab9490 | -3.9369 | -46.982601 | 2024-12-27 00:41:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d7c80da6-aaf0-3d3b-9ed2-9e4be5c2056a | -2.2596 | -46.392601 | 2024-12-27 00:41:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2cbf4b73-973d-3d64-b7e5-5b10f7f25920 | -5.133 | -43.239601 | 2024-12-27 00:41:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 003165ad-c50f-3ca6-8bbb-26079cd5cc9e | -5.9092 | -43.4827 | 2024-12-27 00:41:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 970b8245-bd70-3007-876d-4f7c00e42d74 | -5.8996 | -43.485001 | 2024-12-27 00:41:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 820f1c78-ecf2-32b4-a2a1-6de258dcb895 | -4.4879 | -44.335701 | 2024-12-27 00:41:00 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 694e4522-82fe-36da-8acd-2a373decaa41 | -5.1275 | -43.2173 | 2024-12-27 00:41:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 588fba10-6017-386b-b013-5e5df1040d60 | -5.6352 | -43.702499 | 2024-12-27 00:41:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f597ca27-3ad3-376d-9cc7-4e06835fe373 | -1.4954 | -52.391102 | 2024-12-27 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77670298-d43e-327e-af90-48af30d2456c | -1.6115 | -53.3601 | 2024-12-27 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39e4f232-4c2d-363b-9382-ccaf3f75f906 | -3.9242 | -46.972 | 2024-12-27 00:41:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
