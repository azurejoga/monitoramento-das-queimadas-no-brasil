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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc845275-d950-3fa9-8d85-7de81d79b2b5 | -3.97611 | -46.7315 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc8eaf13-a7bc-3768-b433-d0787001ea33 | -4.23161 | -45.76937 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 093cb40a-fe98-3701-856d-fc6aba0d7e01 | -1.71147 | -52.76897 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f7e1549f-f06d-3e1a-ac24-e9304e927307 | -1.08817 | -53.3955 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e5c1bc4-c2ec-3085-84dc-e85bda24cfd8 | -0.2697 | -51.63567 | 2024-11-29 04:04:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e2c956a1-bf55-3686-9c2d-7c37fa05df63 | -3.89728 | -49.82237 | 2024-11-29 04:04:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17591908-7190-3ffa-952f-d7cd8b2c9dc9 | -3.27154 | -50.62158 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65849ed5-4567-3561-b0fd-8deaec1c6bb8 | -2.98511 | -51.3302 | 2024-11-29 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24e7689e-bb15-3096-bfdf-76bc862acb6c | -1.58582 | -52.28709 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5eab6859-897a-30ad-9e07-21cc2c44b11e | -4.10058 | -46.11397 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 373223b9-77fc-375c-a583-4e6da0fbb82c | -2.69926 | -48.65346 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2991a8e4-da73-32a3-8018-a7742359a7c8 | -4.04478 | -48.3382 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 351bbc2d-2af8-36ae-be85-406ab3ea6961 | -4.17184 | -48.63282 | 2024-11-29 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f71e7e19-c6a0-35af-8970-e69c828cb53c | -2.53617 | -47.32471 | 2024-11-29 04:04:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0651140-a3e4-3fd5-919d-b2aae46ca576 | -2.83606 | -46.81304 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac0c4a25-b5f6-33f0-ad13-6036501bda6e | 0.74087 | -50.87585 | 2024-11-29 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71103a67-5cdc-3e8c-8bf3-65d10d08ec9e | -4.69289 | -47.18477 | 2024-11-29 04:04:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb225818-b643-317e-936a-6bf06f201eba | -5.39396 | -46.11029 | 2024-11-29 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce16c475-08cc-386d-b352-bc673ea37d45 | -5.54086 | -41.42442 | 2024-11-29 04:04:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3d97978c-7689-3eea-b485-a0f563f4e791 | -4.8683 | -41.27219 | 2024-11-29 04:04:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4333ffc2-b806-36bf-bb0c-00906e23520a | 0.98303 | -50.26337 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8d29a00-7249-3064-9c46-7e1190355e89 | -4.10833 | -48.24991 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9dd56514-4625-3a52-809f-d98e4f80654f | -6.18588 | -43.9561 | 2024-11-29 04:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e149e5d-ea72-3e45-af2b-9cc188437b14 | -3.09487 | -50.36163 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2512ac5b-d670-3f93-878a-27ebeb30238c | -3.97413 | -46.74374 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1103b76-68db-311d-89b0-f269aab9c3ed | -3.24452 | -50.62283 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c985d8c7-d88c-30df-b645-3a0a59e90e09 | -3.16733 | -48.5889 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9c9252f0-07e0-302a-bb1a-53e96c1fd090 | -1.69662 | -52.46112 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| e04d81e7-7b8d-33b7-968d-b9d9116ef965 | -4.00121 | -46.31382 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02561c22-6372-3226-aaf1-dd362f3ce053 | -3.08935 | -50.3607 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96f238db-e27d-3435-9999-d8e33f31bde1 | -5.20597 | -41.2872 | 2024-11-29 04:04:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 19caeb25-1169-3cc1-8f77-e3c43f222bfe | -2.66182 | -48.78378 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| efe141f6-c5e3-37ab-8330-dfa983a416a6 | -4.18391 | -50.68377 | 2024-11-29 04:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa3a8109-4c6c-3cea-a1c4-8fd30ea485da | -2.58516 | -47.4855 | 2024-11-29 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f97029e-1d92-34c5-98c6-be3e676ff6d5 | -2.98085 | -53.28896 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 2528cb35-0ee0-3ce4-b4b1-26fc45800ee5 | -2.85899 | -45.541 | 2024-11-29 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1295290c-30c9-3c82-8084-3ef2ffa64f1e | -2.85499 | -45.54039 | 2024-11-29 04:04:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f88e99d7-672f-35ab-af0d-225d37a8dd69 | -2.80054 | -48.68765 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80306e3a-4b4d-3c83-b869-faafb2a59536 | -5.63212 | -46.96605 | 2024-11-29 04:04:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dba2bd3-13c3-33c2-bda3-6c872eca9352 | -3.95207 | -52.20894 | 2024-11-29 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c34081bb-c853-3816-80eb-280af58f7442 | -1.68358 | -45.79978 | 2024-11-29 04:04:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f54fa194-b91b-39f1-bee7-93c89db72dac | -2.57199 | -49.99986 | 2024-11-29 04:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddba9a30-57d0-341d-a81a-2b685bcb6b6d | -1.99155 | -45.9048 | 2024-11-29 04:04:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f084ee46-d9c4-38ff-865d-c34dd821a1e8 | -3.93883 | -46.69273 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05a56433-e833-3daa-833c-b675714a0530 | -2.82551 | -46.85019 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21385c2f-1a67-3a38-a8cb-b7b38be6f09c | -4.30215 | -48.23998 | 2024-11-29 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e87dbe09-90f4-3ccf-ab5c-e4e44d37af02 | -3.33232 | -46.69591 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 954b278d-27a3-3be5-9de1-18b61ea04b25 | -1.94535 | -53.3452 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e72dccbc-4512-30f1-8a72-806650c78f4f | -3.87774 | -49.8422 | 2024-11-29 04:04:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a3705ad-6f82-3e60-968a-869a282f9fce | -3.86832 | -48.36285 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5cd4172d-c39e-35af-bfea-864740a4f76a | -1.67406 | -52.43245 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a00503d6-fdfc-38a6-964c-8b9ba4415388 | -3.16653 | -51.09946 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc2cc8d3-b9bd-39a7-bd2f-1c45416131da | -3.95754 | -48.08823 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ed5a6ac5-2bc1-373e-91d2-fd7de1444b7a | -3.41513 | -50.16958 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74b380f1-5a86-3829-bdc0-b7d9c57dd9e4 | -2.85443 | -45.54386 | 2024-11-29 04:04:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce1349ba-8fce-362c-922c-322b7b1c83e4 | -2.06196 | -46.38202 | 2024-11-29 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1903f9bf-be63-3da3-b60e-d41657c35f0c | -1.95211 | -53.34644 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f29e513-7cde-34e2-9239-525323f3f1b8 | -5.5491 | -41.41512 | 2024-11-29 04:04:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c8be821e-433e-3f7a-9ab1-e1caf0ab8408 | -4.8774 | -44.64582 | 2024-11-29 04:04:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f02a56c7-4610-3847-8f6a-3fabea4ba787 | -4.02553 | -48.89332 | 2024-11-29 04:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7a344f6-4774-3bd5-8f07-2982c0e3352e | -5.98044 | -45.35823 | 2024-11-29 04:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d9a0b48-8889-361e-9bc0-37b148142788 | -3.24328 | -50.59527 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 846900f1-a361-37ab-a29b-ef8ced6c5f2b | -3.14662 | -49.21245 | 2024-11-29 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 164b435f-a91d-3f6f-8455-be9fc140f6dc | -3.24245 | -50.58961 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dad0fad2-6a24-3800-b8fe-ca7e8b017e84 | -3.97479 | -46.73967 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2eb562a-ef99-3287-b471-65b1c8e1b8e5 | -5.39876 | -41.5506 | 2024-11-29 04:04:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0442a68c-e55f-3e19-9b14-4552888d08a1 | -3.33391 | -53.2289 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ae61523-b46d-3032-9c7e-5f82676122ac | -4.33919 | -47.57154 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 421eb5f5-988d-38f5-ad84-0fbcc44a799e | -1.0813 | -53.39626 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 25eb48e0-b1cc-3e8e-b982-c5f7cf1a31a5 | -3.38904 | -54.28683 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de006b00-3cab-36d8-9341-eae86dda6d50 | -3.97252 | -46.72674 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f18aabc-1506-3b7f-926a-b52fcbf8ac7b | 0.04298 | -51.11227 | 2024-11-29 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9ad2b690-e919-3b93-879d-da809ef28782 | -3.1738 | -46.30769 | 2024-11-29 04:04:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 622fdd18-f2a7-37a9-a85a-cce90c0164fd | -4.22848 | -45.76351 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6b63ae2-1439-3ead-a504-52b395977fef | -5.54924 | -45.19781 | 2024-11-29 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 518b3a44-25ab-35fa-a957-ffa3c9963074 | -2.06624 | -46.38272 | 2024-11-29 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27eb338a-6651-38e9-a66d-8f3d3fc28e3c | -3.33487 | -53.22323 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32033db7-0382-3c7d-9458-fa42c64be248 | 0.9456 | -50.74079 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3eb8f2df-6658-3d67-9a5b-1a17fe378473 | -3.19632 | -46.59565 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a2325c6-1133-3374-92c5-aa61c12dc688 | -3.4724 | -50.53667 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e5cf984-6365-3d9c-944f-6acc0a2b0496 | -4.19911 | -50.68918 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9cddd5de-3f8d-3bb2-944c-cd773a84baf2 | 0.97373 | -50.12781 | 2024-11-29 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64f5e90a-a883-3769-9134-9a9dc264bb96 | -3.88947 | -46.67793 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2757472c-5e82-320b-bec5-e6794a4d4ee6 | -5.57329 | -47.1343 | 2024-11-29 04:04:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8ce563e-7c17-337c-b01a-916f6dc176f0 | -2.98459 | -44.96333 | 2024-11-29 04:04:00 | NOAA-20 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ba98f29-1b4e-3c3b-b4dc-63b10a572925 | -1.80164 | -48.77398 | 2024-11-29 04:04:00 | NOAA-20 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3546d3e3-2cbe-3b48-ab34-e2f1b8ab2222 | -3.47176 | -50.54034 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3535a031-51ea-3800-aaba-af5eba5a771f | -6.06733 | -44.15229 | 2024-11-29 04:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0b9128e5-df85-3b5e-a4dc-b3a66976b62d | -6.85861 | -39.4357 | 2024-11-29 04:04:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1e0cee18-30d6-307a-837e-e9c4978cfbb2 | -1.95687 | -46.44475 | 2024-11-29 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aa6f9be2-bf87-3b05-851d-c19c9950893a | -3.41029 | -50.1651 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6441562-2ed1-356e-816d-96e00f3b5bc7 | -5.43967 | -45.58236 | 2024-11-29 04:04:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 698e19fa-0809-3a06-b512-d125c6a84efc | -4.50744 | -42.07396 | 2024-11-29 04:04:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cdd21a17-f958-3634-a7e7-4b592ff453de | -3.09136 | -41.14484 | 2024-11-29 04:04:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 42c876ab-a8b1-34c2-ab29-f5d71a84d2b3 | -1.21141 | -53.75918 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| d9e3c2f5-b9ce-3ac5-9949-b39262842f20 | -2.20149 | -52.10835 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b65d9ce6-26a4-3bb6-a980-0c6cf7e16317 | -4.26182 | -40.70126 | 2024-11-29 04:04:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a3018abf-9cf9-3990-a3ed-cc6eae95d08b | -2.33849 | -46.87861 | 2024-11-29 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 29afe8c2-5c8a-3d8b-9855-df18b9a3da05 | -3.97971 | -46.73627 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9094b1a1-458a-3ced-9d66-a0a05a41b789 | -3.00117 | -40.22826 | 2024-11-29 04:04:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README28.md)
