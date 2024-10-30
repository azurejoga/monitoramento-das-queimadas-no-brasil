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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee7a278c-e25b-3cc3-b2f5-8553501dbc6b | -17.7445 | -57.54167 | 2024-10-30 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 23e2e354-780b-3014-8d17-3c7f2461f10d | -17.74423 | -57.51978 | 2024-10-30 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 119aaa0e-bf85-316d-a200-bf1d4afd569f | -17.74386 | -57.54398 | 2024-10-30 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3153ac08-7494-3790-b39a-86890a581781 | -17.74049 | -57.51905 | 2024-10-30 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5f3d1798-15d0-332c-82bf-09a543179b0f | -17.74012 | -57.54324 | 2024-10-30 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5613d857-99c7-3595-b43f-20e65697c776 | -17.7393 | -57.54794 | 2024-10-30 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 98fddeb7-7607-3bde-8b8a-5a170e07c908 | -17.73638 | -57.54251 | 2024-10-30 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f7bccf74-73ec-3b21-a1a1-c2541acb3ea1 | -17.73555 | -57.54721 | 2024-10-30 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0fa4ed22-2d2e-345b-ba0d-66563093cff8 | -17.73473 | -57.55191 | 2024-10-30 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 86427a53-ff02-3336-ab6e-5ca8b47a90cf | -17.73301 | -57.5176 | 2024-10-30 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b89b4993-67f8-357a-ac1d-a473f18a23a3 | -17.73263 | -57.54177 | 2024-10-30 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 64ee2d8c-93d2-3935-8baf-f805104aa22b | -17.72927 | -57.51686 | 2024-10-30 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 6179b4d6-24c0-3dcb-99bf-c02a318cc8ef | -17.72553 | -57.51613 | 2024-10-30 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 6a804770-be5b-3367-b33d-d77737bf68dc | -17.72471 | -57.52082 | 2024-10-30 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 834064ba-2e0f-3d63-972f-b15e668b9b0f | -17.72388 | -57.52551 | 2024-10-30 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c54efd7d-2dd4-396b-9ede-f9fdb1356cb5 | -17.72183 | -57.55912 | 2024-10-30 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| ecfc8135-cb53-313c-8b3d-8c5a5da8664c | -22.55107 | -47.70319 | 2024-10-30 04:49:00 | NPP-375D | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9ae7a689-2c0f-3b95-ac08-f01451bf2c1c | -22.51386 | -47.70846 | 2024-10-30 04:49:00 | NPP-375D | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 122cffb6-0d73-308e-a8de-be4c3d3c86a5 | -22.51332 | -47.71318 | 2024-10-30 04:49:00 | NPP-375D | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 770bc69a-ed75-3ed0-84e3-d5e72ddd286c | -22.50935 | -47.70794 | 2024-10-30 04:49:00 | NPP-375D | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3c8ca3aa-f4a9-33ac-ac89-7ae9405bf081 | -22.5088 | -47.71267 | 2024-10-30 04:49:00 | NPP-375D | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 52fa950f-f026-38c6-8532-a92470eda304 | -19.23652 | -48.46658 | 2024-10-30 04:49:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58f3cce8-9689-3d05-b6ef-fbbcdbad0326 | -21.11167 | -48.64668 | 2024-10-30 04:49:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 51c8f6a7-9b36-38ef-93ee-2bb88b70866b | -23.99326 | -54.10931 | 2024-10-30 04:51:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6cd96981-158a-3960-b21a-eefd751f9ac5 | -23.9899 | -54.10872 | 2024-10-30 04:51:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 56daa6a1-3394-32b1-b044-02dfe80f944f | -23.98932 | -54.11257 | 2024-10-30 04:51:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 0b484889-a153-3d95-a5b7-12e6153b0a1f | -23.30453 | -52.61432 | 2024-10-30 04:51:00 | NPP-375D | PARAÍSO DO NORTE | PARANÁ | Brasil | 4118006 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3a777037-9d16-327d-be8c-1f1ecc135c2d | -23.75159 | -54.50266 | 2024-10-30 04:51:00 | NPP-375D | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d6a9579b-ea0f-39ec-a679-8bf43acb9123 | -23.75101 | -54.50646 | 2024-10-30 04:51:00 | NPP-375D | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3a1e96c3-69e9-3310-9540-2925ce92ee0f | -24.00875 | -54.1437 | 2024-10-30 04:51:00 | NPP-375D | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 4ead1345-2895-385e-95c0-2cf85a94c162 | -24.00817 | -54.14754 | 2024-10-30 04:51:00 | NPP-375D | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9b6fd5d4-acce-3184-a071-c9235d601eda | -24.00482 | -54.14694 | 2024-10-30 04:51:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f4d5f9dc-5e37-374a-996a-c6b109b1b585 | -24.00365 | -54.15463 | 2024-10-30 04:51:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e9f87a10-470c-3959-9139-f4390db176c9 | -23.98596 | -54.11197 | 2024-10-30 04:51:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 9f49ce81-d619-3fb5-a63f-75c9d1baf975 | -23.98538 | -54.11582 | 2024-10-30 04:51:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7a3eb4ff-4030-3e99-b241-b61e3d716f76 | -23.98203 | -54.11522 | 2024-10-30 04:51:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 3786d1a3-0f93-389b-84fa-16d533430f0d | -23.85373 | -49.4948 | 2024-10-30 04:51:00 | NPP-375D | RIVERSUL | SÃO PAULO | Brasil | 3543501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 49158b91-2964-3d92-8096-7945924f8882 | -29.81447 | -51.17403 | 2024-10-30 04:51:00 | NPP-375D | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| aeaf669f-5399-3f93-a3d9-dfb4f80fc68f | -23.14704 | -52.66525 | 2024-10-30 04:51:00 | NPP-375D | MIRADOR | PARANÁ | Brasil | 4115903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 621bc048-4b78-3959-9645-13896e06a301 | -23.14645 | -52.66935 | 2024-10-30 04:51:00 | NPP-375D | MIRADOR | PARANÁ | Brasil | 4115903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5e67734a-1b26-34be-857c-54f8f4f76a0f | -23.10521 | -52.09539 | 2024-10-30 04:51:00 | NPP-375D | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fd07fcf7-cfa6-31d1-98cc-3976ebde437d | 1.675 | -55.8634 | 2024-10-30 04:54:56 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| b54731df-75dd-3305-abc0-b046e2048820 | 1.6751 | -55.8437 | 2024-10-30 04:54:56 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| b3a640bc-0387-37a0-a9c2-7f5276d00890 | -2.833 | -49.2413 | 2024-10-30 04:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 1ac93ae4-b763-3a6c-a586-c739a0e0c982 | -3.0734 | -54.167 | 2024-10-30 04:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 638462d9-0115-30d3-ace7-2516445335db | -3.1097 | -54.2865 | 2024-10-30 04:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| cc1b64c6-3d33-3ee5-9107-0c2fbc8d0afe | -3.1098 | -54.2665 | 2024-10-30 04:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| af79821e-2441-3857-a20f-2deed6d6b99c | -3.1281 | -54.266 | 2024-10-30 04:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 219ea38f-b476-3721-a1be-06290cbba603 | -3.1601 | -50.6021 | 2024-10-30 04:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| b4c0bebd-f7a8-328b-a65a-864e46514280 | -3.1602 | -50.5812 | 2024-10-30 04:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 9466aacb-5bf9-3a45-8422-4502bc094b0b | -3.1786 | -50.6016 | 2024-10-30 04:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 571b39c4-7146-340d-bc37-f579356b3f58 | -3.1787 | -50.5807 | 2024-10-30 04:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 3cf02ccc-b6a4-3579-bd3d-28ffa7da576a | -3.2535 | -50.3479 | 2024-10-30 04:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| e9b07b09-90c6-30cb-bc53-22ed5ad6d3e9 | -3.2718 | -50.3683 | 2024-10-30 04:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| a0f27eb8-c0a0-3870-8e04-939c3328fae6 | -3.2719 | -50.3473 | 2024-10-30 04:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 764f568f-bbb9-38bb-8d5a-7f350ce126cd | -3.5631 | -47.3847 | 2024-10-30 04:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| b2b681d8-20eb-34c6-9ced-15434e523245 | -3.5632 | -47.3629 | 2024-10-30 04:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 729c3182-a6c4-3d9a-8e88-e2809b745552 | -3.5817 | -47.384 | 2024-10-30 04:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| e41003c4-25cb-332f-b3ab-74f22c9ead89 | -3.9486 | -48.1291 | 2024-10-30 04:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 5818053c-2a1e-3a03-9bf3-3a4898c051ec | -4.0681 | -50.024 | 2024-10-30 04:55:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| b7324b25-9085-3068-a4f4-0d5ced5fee14 | -4.0682 | -50.0029 | 2024-10-30 04:55:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e70dfa01-6dd5-3e55-942d-210a0f1f4ab8 | -4.0866 | -50.0232 | 2024-10-30 04:55:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 6e61c3a2-3fab-3615-a92c-1a4021b487e7 | -4.0867 | -50.0021 | 2024-10-30 04:55:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 5eb6a230-12f9-37f4-8f38-68795216b04b | -4.2563 | -43.4368 | 2024-10-30 04:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 3ac83c97-cb11-3031-aeef-db29a7adbb9c | -4.2749 | -43.4357 | 2024-10-30 04:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 4a9a29fa-efec-3fbf-9509-898c5d84b10a | -4.2681 | -50.6669 | 2024-10-30 04:55:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 2970827c-8679-350e-88d1-1176d9c872eb | -19.5862 | -56.7136 | 2024-10-30 04:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 116.2 |
| 444eac25-deaf-3c3e-8cbd-964d098a0d60 | -19.6063 | -56.7108 | 2024-10-30 04:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 117.7 |
| 0d12a7b0-b587-3f17-b6dd-0629caf33b2c | -19.6067 | -56.6898 | 2024-10-30 04:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.0 |
| 604f29b3-62d2-3f04-a8a9-80069cc58b7c | -19.6264 | -56.7079 | 2024-10-30 04:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 76.1 |
| 95c35fbc-5730-3810-8470-68a7918c772c | 1.675 | -55.8634 | 2024-10-30 05:04:56 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| ee0012bd-3457-3b03-9156-1117ce02ffe8 | 1.6751 | -55.8437 | 2024-10-30 05:04:56 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 24f7879c-ff66-39fa-95d7-7efc9693d195 | -2.833 | -49.2413 | 2024-10-30 05:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 4ede8a3a-19f4-31c9-8b1e-7af2354444c9 | -3.0734 | -54.167 | 2024-10-30 05:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| b4ed7beb-a37d-3fc6-a446-97f9412cc3c6 | -3.0913 | -54.287 | 2024-10-30 05:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| d79ae139-32bb-3e95-8f99-479c4ee4b4a4 | -3.1097 | -54.2865 | 2024-10-30 05:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| d63c67d7-c739-3baa-aa92-41668e316343 | -3.1098 | -54.2665 | 2024-10-30 05:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 015bffbb-381d-3853-b548-5ba0eb4781a2 | -3.1281 | -54.266 | 2024-10-30 05:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 663e99e6-84ed-3ef5-ae10-e1cae652091d | -3.1601 | -50.6021 | 2024-10-30 05:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 0b394a6e-e808-33ff-a27b-ff1a414474ff | -3.1602 | -50.5812 | 2024-10-30 05:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 4113c435-6f09-36d2-95fa-ee8ab6d2e0f8 | -3.1786 | -50.6016 | 2024-10-30 05:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| def859d2-e671-3433-b999-40e25fc06662 | -3.1787 | -50.5807 | 2024-10-30 05:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 458b619a-12a4-32dc-bcd0-1566721aac16 | -3.2534 | -50.3689 | 2024-10-30 05:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 6989375d-4ba8-3313-bf0e-379b5f9e1188 | -3.2535 | -50.3479 | 2024-10-30 05:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 96a74b8b-3f9c-353e-b045-bf34d1be904a | -3.2718 | -50.3683 | 2024-10-30 05:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 811556fe-cb5a-3f31-a4f0-06a26d65dae0 | -3.2719 | -50.3473 | 2024-10-30 05:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 910a71d6-5ae5-3dc0-9a6b-f8c676dab755 | -3.5631 | -47.3847 | 2024-10-30 05:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 59b21d44-14fa-381e-bcef-eedaa08004c2 | -3.5632 | -47.3629 | 2024-10-30 05:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 89f02da6-6ae6-3286-91d3-ce729d29b73b | -3.5817 | -47.384 | 2024-10-30 05:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 2c8a87c7-d653-3f85-94b2-a9454981f038 | -3.9486 | -48.1291 | 2024-10-30 05:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 15ea20df-868e-3748-9266-c410dd179fcf | -4.0681 | -50.024 | 2024-10-30 05:05:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| d985d4d6-fd95-3f01-b757-f5837fcfb8a1 | -4.0682 | -50.0029 | 2024-10-30 05:05:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 39d56ca3-6f5a-3e85-b3f1-905e1517af87 | -4.0867 | -50.0021 | 2024-10-30 05:05:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 0c626d02-f6df-35e1-ac66-f0d4f03ca549 | -4.2563 | -43.4368 | 2024-10-30 05:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 3e00c4e1-3da4-37d7-addc-820ec4f9f304 | -4.2681 | -50.6669 | 2024-10-30 05:05:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| b105b06f-47e3-37fd-b0a6-ee98411a18bd | -4.2496 | -50.6677 | 2024-10-30 05:05:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| bfe2cdd7-0585-317c-b173-b9fc6b172c5a | -4.2749 | -43.4357 | 2024-10-30 05:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| a17def94-33af-3ed8-ba50-4206bd60208d | 1.60312 | -55.62595 | 2024-10-30 05:06:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bbb19b2-297c-3941-89b1-902be8f36383 | 1.59982 | -55.62646 | 2024-10-30 05:06:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92640a13-ac7c-3197-bdcc-3c4386d8817f | 1.59653 | -55.62697 | 2024-10-30 05:06:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README80.md)
