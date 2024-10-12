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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22f59428-c42e-35d8-9c35-f6897fca6595 | -4.607 | -56.12258 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aae51c49-7430-367e-ac49-cc40b3172f21 | -4.54113 | -56.1501 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecf9a7f7-b986-331f-9073-db2b8e88c7ca | -4.53326 | -56.12565 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f958f233-0110-3124-8366-5f3aecd5a1fa | -4.43302 | -56.30441 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5db6ea0-4d59-3d25-9544-559be2518791 | -4.36224 | -56.37021 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46099da5-481d-3b0d-8866-a33e3eaf700d | -4.36002 | -56.37185 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89ed966d-0f15-31ac-a361-ec7861b97913 | -4.07726 | -56.2879 | 2024-10-12 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e1b38b2-d53b-3cf6-9749-cef1f113c09d | -3.99675 | -56.08299 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e11a3054-c861-3a45-90cf-d59f10193159 | -3.993 | -56.08242 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b319deb3-7ccf-3c8d-a35b-7f964141f1d3 | -3.99233 | -56.08685 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cecf03b-6bef-3263-bb0c-ac3b5cf49aa2 | -4.54529 | -55.77498 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efb6a58e-d50a-36a1-9e7f-2c65a55ec70e | -4.45951 | -55.70677 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 033f8e42-eddd-33cf-8d75-455b843458e3 | -4.33553 | -55.74524 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22566510-a35b-300e-bdd4-9052935f5961 | -4.33443 | -55.74319 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 351f0167-c5e0-3d5b-90eb-1536e7f9f2b7 | -4.3337 | -55.74788 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23ad2bd1-f4fe-34ae-b069-9a4f708118a6 | -4.24168 | -55.96692 | 2024-10-12 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72177627-637b-3048-8690-952324507c76 | -3.97866 | -55.74512 | 2024-10-12 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e51a9fe4-ea1c-3b48-85c5-8a2d922abf03 | -5.25471 | -55.96944 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31d9933c-6ab4-3cef-bcdf-acfdd106237f | -5.25088 | -55.96886 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a12c3a9-091e-3515-9471-208daceb442b | -5.20669 | -56.05397 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ccebfc7-1f2c-37e1-b6f2-67590d46ad03 | -5.18001 | -55.99704 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d1783985-d224-3330-b453-4b813bd44a34 | -5.17932 | -56.00166 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3644d576-80d8-37c8-a234-7f58ed1ca33c | -5.1328 | -56.2634 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00e322cf-b198-37b6-86b7-01516dd9725d | -5.09729 | -56.1946 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ed6b145-d134-3213-b0bc-2dc515fcb4a8 | -5.09659 | -56.19918 | 2024-10-12 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89ed67cb-b92f-37c7-b9d2-7301f8565081 | -8.10762 | -57.67533 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fffd24f-1ad2-32ca-b78c-e8174a1ddc52 | -8.104 | -57.67479 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 963f9ba5-9270-30c7-bbee-8635e186eeeb | -9.94967 | -58.10151 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 871bc272-5f8e-3983-a467-3c4d327a23af | -9.94906 | -58.1057 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb250091-f176-328b-8a60-d725f3e851fc | -9.94606 | -58.10096 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e616fb22-1877-38c3-b412-5f4f1f651527 | -9.94545 | -58.10514 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a0dd173-4a3e-3c98-8b20-8709c0b651fe | -9.94483 | -58.10935 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57723de1-5ef7-3264-a3a2-53adf8f222d3 | -9.94244 | -58.1004 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b3948df-ad8a-302c-a936-512ad1f1b3cc | -9.94183 | -58.10459 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de29a4e4-c743-3b8d-9024-a7ea93665449 | -9.94122 | -58.10879 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ade224a-5cc3-31cb-9b2f-7b8606ff429e | -9.93822 | -58.10404 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 177d2a8b-f7d0-366a-8902-c46ad2d2b5e7 | -9.93761 | -58.10823 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11c391e2-e764-3c90-898a-2313ecac39e0 | -9.934 | -58.10768 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d067186-e1eb-3009-bb52-91bf63909e8b | -9.93039 | -58.10712 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8994df22-e352-3755-a14a-0c5239149c61 | -9.9035 | -57.06552 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5f64853-6c5e-30e0-8ef0-1e93c54dc862 | -9.84903 | -57.75045 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0b6e198-ff59-34c3-86b1-ffa0b92cc5c4 | -9.78858 | -57.45524 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c60d9b9-f9a1-3d81-9f31-1b7a33022a78 | -9.78419 | -57.45916 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69a26147-a6b5-3b80-b9cd-c5bf38de5981 | -9.77055 | -57.92726 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5f26983-29d4-36c1-9354-32e1d9af1bba | -9.68278 | -57.20903 | 2024-10-12 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2e5099d-6b6e-3d52-b3fd-6a2186b47df2 | -9.68006 | -57.22764 | 2024-10-12 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71f9244d-6d7b-36d2-a904-d7dfdd359111 | -9.67899 | -57.20852 | 2024-10-12 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b6f7669-83c3-3156-875d-09b5b22c7d32 | -9.67696 | -57.22247 | 2024-10-12 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0c6db4d-6ce3-302c-b424-44e7ea8e5fa7 | -9.66575 | -56.96048 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f37aacc5-432f-3d87-8f52-b37962f3528f | -9.66505 | -56.9652 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf3d0527-b2e1-31ec-876d-0afae4696bf8 | -9.66386 | -56.96215 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64fa5919-8c5a-3654-9cd5-8481ecb5bf97 | -9.66192 | -56.95989 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a4b5f0e-5280-3e79-9213-f02bf658b0b7 | -9.66122 | -56.96461 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5039020f-36c4-31ea-8908-e5274030082d | -9.6607 | -56.95683 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5029fa68-afde-320a-9c2b-e18e15cd3b03 | -9.65936 | -56.9663 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 016f7891-b272-3ae0-a630-ae9a5b7a2384 | -9.65879 | -56.95458 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66d3b092-0233-30ec-8601-d92ac03e982d | -9.65809 | -56.9593 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06f2e784-d824-3b18-af93-4f8dc0617c44 | -9.65687 | -56.95625 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21666f17-393d-3401-8a3c-c5ac1a33b473 | -9.6562 | -56.96097 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da652a77-7eac-33d0-9005-08af5cc1d0a5 | -9.65496 | -56.954 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b79d41e-2620-3e5c-a2d3-45f25ef5cea7 | -9.65426 | -56.95872 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30789cd5-958b-3d9b-8723-cb5c0e2f9134 | -9.6537 | -56.9509 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b47d913-5683-3601-9c0b-f0b482fd4b84 | -9.65303 | -56.95566 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 853d35cc-22ec-36fb-a3ae-df5701479b8a | -9.65112 | -56.95341 | 2024-10-12 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f50dd2c1-751d-3d1c-a513-e854afb9b877 | -9.47158 | -57.93432 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd529c47-8938-38b1-bb5f-a7c3c9f50917 | -10.12892 | -57.76462 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 049ba1c6-9f55-37de-bea6-7c473e6e2e72 | -10.12829 | -57.76896 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8a2f35b-7587-38d5-ac29-f2122014b741 | -10.12524 | -57.76404 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b76fda29-d4cd-3a9b-b999-4f1434564125 | -10.1246 | -57.7684 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d8bcb052-b5ed-3398-bf4d-715c28c09656 | -10.12219 | -57.75909 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d52d4595-a159-32ed-a273-2f42413ec160 | -10.12156 | -57.76348 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01302649-07c0-35b5-9362-edf09e59951e | -10.11787 | -57.76291 | 2024-10-12 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97e075b0-1195-3df2-8eec-801d60c2f83c | -15.12651 | -59.02582 | 2024-10-12 05:23:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dfd5a25-0abd-3da6-bca8-53496d9164df | -3.62716 | -57.48722 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4f0355b-3198-364a-a18c-5df813bf665d | -3.50304 | -57.73904 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc6dff81-4a67-3810-98fc-20d6ff575740 | -3.44272 | -57.97297 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b803105-6271-3751-b145-19f3029bea36 | -3.1676 | -57.94606 | 2024-10-12 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 394be5dd-74af-3a48-96c9-86da14030bfa | -2.98704 | -57.08467 | 2024-10-12 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a857083-97c8-3c9d-8346-7d69ba373f8e | -2.62247 | -57.57032 | 2024-10-12 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 777009a6-77e5-3077-a421-2a8ef063c849 | -2.62189 | -57.57406 | 2024-10-12 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65101bbc-8d11-3fc3-b168-ae0a799c1346 | -2.62019 | -57.56236 | 2024-10-12 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2a5fb34-f6cf-312e-b47b-867a33bb4ac0 | -2.61675 | -57.56182 | 2024-10-12 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51fb1aa8-cacb-3481-bb4d-6e0e80ccaf5d | -3.89224 | -57.95695 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f176e9e0-c9dd-309b-8c7f-28eb42e6b4fb | -3.71075 | -57.13268 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25de2e78-c8d0-3f29-8d3c-53d8a155d8f8 | -3.6473 | -58.2533 | 2024-10-12 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6ff4531-5991-3244-8ff1-d050ecf940ca | -6.47627 | -58.43653 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5faaf9f7-7ed3-3e1a-8c2f-53a910076f73 | -6.4757 | -58.44025 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c67d0ec-05f6-37ee-91fd-f1a18e82110d | -6.47283 | -58.436 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fc36083-7a38-3f3b-88e3-8130217286e8 | -6.47225 | -58.43974 | 2024-10-12 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fa8cd44-968b-38a7-ae07-0755b134aee0 | -6.35418 | -58.17849 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01e06070-b802-3e54-a191-2f0987251274 | -6.3536 | -58.18231 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3971ab31-a1bb-32c6-ad13-27a1551b48d6 | -6.35128 | -58.17413 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddd88175-6d89-35fe-8651-f7165066fb51 | -6.3507 | -58.17795 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb800117-a66f-364e-8452-ad2f586bef44 | -6.35013 | -58.18178 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a70821b7-9a56-3d48-b872-fddf9e60d97d | -6.34998 | -58.17488 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e6f4e5c-2070-36a0-8405-b581d2520aee | -6.34955 | -58.1856 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0827402-67fe-3f1e-9ec4-7d8299c8175e | -6.34939 | -58.17869 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1c6079f-d0d7-35f3-ad1b-ba69a395fc50 | -6.3488 | -58.18251 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7475bf57-41fd-38ff-a4cd-d91e889a776f | -6.3482 | -58.18632 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06b0b7ef-960b-3d3b-94c1-b20afff513a0 | -6.3478 | -58.17361 | 2024-10-12 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README104.md)
