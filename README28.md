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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf100050-fae5-386c-86f9-5a8cfbd7d9a4 | -2.66629 | -46.17568 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5921cede-2aae-3b45-a913-ace4b1a04bca | -8.3211 | -42.10784 | 2024-11-17 04:06:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5d85b7c4-5d99-3ca1-8cbb-32395e439f63 | -2.1576 | -50.70773 | 2024-11-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17a3eb82-de5e-3b6f-9f5d-83bf610e2e25 | -2.67222 | -46.19171 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba2617ef-b5b4-397f-8061-527bbe402930 | -4.18088 | -46.81961 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 914e31aa-8028-3f17-9f2c-6066512fdaab | -0.90598 | -51.74221 | 2024-11-17 04:06:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d90a46c-44dd-371c-84c9-773c605ff66e | -2.6698 | -46.2082 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c7c5a94-b9a7-3860-8039-c738348af62b | -2.67939 | -46.85873 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8220a51e-649c-3fc2-bc7d-54a6ecc65eee | -1.13904 | -51.69728 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 4ffc0cde-376b-33fd-a893-006fd8834b84 | -5.27982 | -47.51265 | 2024-11-17 04:06:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1d64d83-aee4-3eee-a3f7-f166ca2f1136 | -3.01745 | -45.39915 | 2024-11-17 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3aa2e12-4dd3-3825-ac5f-18ad4be2a79b | -2.95636 | -45.8059 | 2024-11-17 04:06:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 717e34f3-9c64-3ebd-ab79-011abe7ddec5 | -3.98754 | -45.85439 | 2024-11-17 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e66eb1b-51be-36e0-b2b5-b5367289bad7 | -4.40079 | -45.52205 | 2024-11-17 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb1b2e5f-cd0a-3ccc-a811-5cefd1da3e7b | -1.75431 | -46.35172 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b46534f-d6a8-3d9b-ac35-440f5fee8b75 | -4.54082 | -45.25367 | 2024-11-17 04:06:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e248335f-ed4e-3e88-aaf6-f7d895b7e6eb | -2.66993 | -46.17937 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac1c2f3c-1ea5-3b7e-ae16-fda3d92a906d | -5.13617 | -41.4281 | 2024-11-17 04:06:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eba2b8e4-0620-33da-a684-18b5894ee9ba | -2.81894 | -46.66154 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96757664-d24e-3610-940f-0326a6ff2cf0 | -2.34978 | -47.46353 | 2024-11-17 04:06:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d5e36290-9257-30a3-844f-80f3232d62d5 | -2.98675 | -52.60667 | 2024-11-17 04:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c72668e-6405-335d-ab90-9c5110c949f9 | -2.2257 | -53.60761 | 2024-11-17 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef58c230-06df-3ae3-8d19-a342d6a98ff7 | -3.65912 | -42.26423 | 2024-11-17 04:06:00 | NPP-375D | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 944cae7c-6950-3be2-ad04-3da7e1fbf605 | -2.66013 | -46.21454 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e93dbe35-dcf0-3644-8b77-c19b8234755f | -3.00284 | -45.42511 | 2024-11-17 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4158ef9b-4d38-30c0-9495-497a76565057 | -3.49743 | -43.78317 | 2024-11-17 04:06:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 902e66d0-2062-301b-91fe-abfd9f302e7c | -3.34362 | -53.30853 | 2024-11-17 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4717f94d-8c2a-3a41-be70-6992e2a1c432 | -2.67341 | -46.21279 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c5a55f77-faa1-3423-933d-4eb97b54c047 | -2.1312 | -49.50454 | 2024-11-17 04:06:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 03bd83e3-faea-3f50-92f6-ddb0c1f05b98 | -2.66964 | -46.20727 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44e0e7d2-128d-331e-9147-17ef978102a8 | -2.35441 | -47.46428 | 2024-11-17 04:06:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c37bcc59-a311-3082-b832-fe8e8b7f6f45 | -1.90437 | -45.60926 | 2024-11-17 04:06:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2ef44c0-dbba-3514-8413-ad9ba82304c3 | -2.39279 | -46.18463 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c72fd2a-1274-322f-bd78-422f54e248c5 | -2.67092 | -46.19951 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27247b09-d1f6-3813-9fbe-7601f82c74c3 | -3.5206 | -50.24846 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 6092e4a8-c0ac-3960-983e-23bb841d3c7f | -2.66413 | -46.2143 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb115fc7-33c0-3c8d-bd50-5272725e04d5 | -5.27619 | -44.9095 | 2024-11-17 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fffd452e-7d6b-3024-a71a-e7ece8d7d735 | -3.94308 | -46.71185 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c2e4874-7436-38b0-a502-b77f1516c659 | -2.27794 | -47.91493 | 2024-11-17 04:06:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 000938de-c137-3eb6-8897-05831c6d832d | -2.67411 | -46.18091 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe85c2b5-e072-3a93-8cc1-bf6ae5443c9a | -4.29643 | -48.0962 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7e8bc151-54a3-32b2-a7c2-85ee9749e17f | -2.60325 | -47.5665 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0eda7a12-4105-3b77-84c0-9ffa94e3290a | -4.03844 | -45.46509 | 2024-11-17 04:06:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2e7b5d9d-ecea-3c11-ae35-d905481053c5 | -5.51719 | -43.72933 | 2024-11-17 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed2733f4-9c00-3f14-8976-8f470a484c0f | -4.10486 | -46.87825 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 666af378-7091-3f10-bb4a-15aa1f54cded | -2.32948 | -53.57631 | 2024-11-17 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b5ef4fd3-9116-34f3-945d-2f0ed5461387 | -2.98674 | -52.60643 | 2024-11-17 04:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cd28378-36f2-3cf6-ba63-ab0cea2c5819 | -4.29562 | -48.10113 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7567ba64-8acf-359e-93cd-57114cbf1345 | -2.67643 | -46.19241 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9f5202d-9ac8-38ec-bbac-4bbf58dcac8a | -3.07453 | -45.46318 | 2024-11-17 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 391f6f3b-3937-3152-912e-fd94d7542b5d | -6.94583 | -42.8177 | 2024-11-17 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cc65ed7d-e8ec-393d-b7c4-7f5eeeede22e | -5.33872 | -44.99866 | 2024-11-17 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c474f8a6-129a-387f-b1fb-4150bf724431 | -1.84258 | -46.28113 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ceebedfb-ceaa-363f-a04e-ae865047cd2d | -6.47757 | -47.50703 | 2024-11-17 04:06:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84034e00-f1d4-3012-9eb1-f7e5ce80281c | -3.46187 | -44.5419 | 2024-11-17 04:06:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8fbcdffa-e365-3044-ad64-665677f45010 | -2.24812 | -46.85068 | 2024-11-17 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea411f85-a345-300a-b408-b47460ca148b | -4.13473 | -43.92796 | 2024-11-17 04:06:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63ff77f6-3543-3865-ac6c-2db038c77c67 | -4.29919 | -48.06376 | 2024-11-17 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7d01799-4b88-3b7c-acc8-f9cd80ca6a54 | -0.96043 | -52.41515 | 2024-11-17 04:06:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b64d7fb7-0029-3a88-877e-c90fcfdb99ef | -3.07102 | -45.38349 | 2024-11-17 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef36013e-46d7-35e4-999a-3a58482397c2 | -2.81843 | -46.65854 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aeb5581c-7a4d-3a14-8b0d-c2aa46a7401e | -3.01347 | -45.39851 | 2024-11-17 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39b017eb-ec19-3375-971d-8ac75d75a2b8 | -2.06037 | -46.54484 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5243f69e-a392-3dc1-8b9e-5c952383dea5 | -4.55815 | -48.00611 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| a0e20ce6-88a0-3756-935f-bd46eba326ac | -3.52675 | -50.24554 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 59c4c4e5-809f-3e63-8b20-4a76ba181b53 | -7.93136 | -39.55585 | 2024-11-17 04:06:00 | NPP-375D | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ee56a1d7-9bbe-3524-9d72-2a75d0132e93 | -7.05121 | -40.4144 | 2024-11-17 04:06:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d4d10701-acfb-3ad0-b284-e821d950e43f | -2.35859 | -47.11662 | 2024-11-17 04:06:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7ab09be-0e6e-381e-855a-a85158ae71da | -3.34981 | -46.43285 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fb38303-0037-35ff-b7b1-4b8206478d44 | -2.67103 | -46.20042 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b8b0902-0c8d-340a-a3d1-f0a7fdaef080 | -2.99326 | -52.6073 | 2024-11-17 04:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 936d1710-8eb3-3b43-b406-8bfe586f0607 | -3.51873 | -50.25955 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05a18102-5eea-318b-ba4e-0c6f53cdb020 | -6.1609 | -42.93887 | 2024-11-17 04:06:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0fff1d79-828a-3091-b6ca-211c745de2d3 | -3.53705 | -50.25135 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7891702d-fa49-34ca-884c-9e8c6afe58a9 | -0.95327 | -51.72961 | 2024-11-17 04:06:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1629bf4-ee5f-3952-b40c-9a45e06a9bb3 | -4.80902 | -44.48157 | 2024-11-17 04:06:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8ef134ab-fe4a-3a68-975b-1b9a858fe1b6 | -1.67074 | -47.97881 | 2024-11-17 04:06:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08b61df9-1a78-3f9d-92fd-3e27fa66cdd2 | -5.42425 | -45.34525 | 2024-11-17 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| faae8186-fc82-3bc0-abce-87bdb0a22aca | -2.3474 | -47.46624 | 2024-11-17 04:06:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6c25bbe4-aecf-3ee4-ad30-7f0dd2335e6b | -3.00369 | -45.41997 | 2024-11-17 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 45a8dace-e7d5-3f97-bfc1-929cce84c00d | -3.62731 | -43.1614 | 2024-11-17 04:06:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 464c53f1-f342-3f7b-845f-944ada69a664 | -2.6599 | -44.27057 | 2024-11-17 04:06:00 | NPP-375D | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b604acff-f5b6-39e7-866b-fdde5d4fbf9b | -2.3477 | -49.12398 | 2024-11-17 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ae3cfef-5763-3be8-bf13-15aa20432bce | -4.21871 | -47.22247 | 2024-11-17 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f04ac20b-95fc-3149-86d3-7e1034cd73c5 | -3.78591 | -46.04348 | 2024-11-17 04:06:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cddd5eb1-fb72-3aec-a7b3-0815a7ad64e4 | -4.44752 | -45.91107 | 2024-11-17 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7461b7c5-d2c6-304b-9a5b-78031baa3a98 | -3.89648 | -46.62248 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb7c88ff-f000-3e9d-ba92-1a8e882f300e | -3.7791 | -44.6593 | 2024-11-17 04:06:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a84f16ad-f61f-3ed9-89ac-aed6b8642067 | -1.65068 | -47.88903 | 2024-11-17 04:06:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc83f046-7315-38a4-b875-0a5b73a5f294 | -4.23701 | -41.93093 | 2024-11-17 04:06:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d6707542-7744-3996-a8f5-0587f65ec495 | -4.30114 | -42.18461 | 2024-11-17 04:06:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 586c9642-d026-344c-a53d-646a255cfc7b | -3.51992 | -50.25225 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2150cabf-f91c-3ac2-9e50-fe0dad59f32d | -3.24412 | -53.5202 | 2024-11-17 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a17a1c33-6451-3b79-b8b6-531c40fae40c | -2.27764 | -47.91233 | 2024-11-17 04:06:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3121e6d0-828a-3a7f-a0c7-65a3dad3113c | -2.42623 | -46.53478 | 2024-11-17 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2761d763-4a7e-34cf-983d-0b5b2ee24368 | -2.35283 | -47.46217 | 2024-11-17 04:06:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 39d2c53c-60ac-3595-b3af-133057f8eb4a | -4.74519 | -48.11834 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8000af79-e575-381e-ae07-b142c1cdeac3 | -2.67772 | -46.18462 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fc9dd66-0baf-3bbb-8ef3-36ee8a78729c | -4.00719 | -46.57876 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1429ac4c-2035-3250-af9c-b42b4530c528 | -6.37169 | -41.55231 | 2024-11-17 04:06:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README29.md)
