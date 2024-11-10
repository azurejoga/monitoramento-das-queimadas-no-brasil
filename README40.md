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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f528c272-f6b1-3222-acc8-b49f9f1daa54 | -6.46506 | -40.77829 | 2024-11-10 04:14:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d7b4c2ff-6766-33b2-aa02-f95a36c29a94 | -4.21127 | -48.60792 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31dc9ca0-78e4-39b0-bd15-8c19fbca01ec | -4.05933 | -48.31628 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92d05874-4eda-30e9-a51f-ca2df5185995 | -4.08518 | -45.97932 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de76b7e2-a582-3d69-8fdf-c4a58ce438b0 | -1.05066 | -51.74648 | 2024-11-10 04:14:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f97be425-358f-3eef-94d9-510600141c7f | -4.37636 | -48.58055 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7ecd7695-3716-319f-8c9d-9ffda672e148 | -3.41353 | -42.29517 | 2024-11-10 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21eed77c-3269-32ee-9038-85b671e65bf3 | -2.93286 | -51.48387 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3a0a839c-4736-3f4e-91ec-b71bb9c459cc | -4.20736 | -49.76647 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 85092fd6-8d6c-3ca0-8127-c52b7aa7bd42 | -5.24097 | -46.23525 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76016ad0-e348-394b-8455-f5125730195b | -4.07217 | -50.00952 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 621bd1ed-98ba-3536-90ec-b1e648a8ada1 | -2.7633 | -49.35595 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7b6c1aba-9a75-3d02-b1ec-c8b6108dfdf9 | -6.25009 | -43.5631 | 2024-11-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb63e35c-bcf0-398d-9f4a-91650f0e79ce | -4.38403 | -47.23261 | 2024-11-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f6d4c39c-7497-3e93-98e2-3baebf5aed94 | -1.87406 | -54.1768 | 2024-11-10 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8ffd092f-67d3-3597-8ed7-b23dde0c28e4 | -4.61688 | -45.98876 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9fa3c39e-a7de-314f-a156-0e7ab78e4417 | -2.22114 | -46.43592 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af2d40fa-7e73-3354-a223-8d69726f38e6 | -4.11753 | -46.88389 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 191966f7-b0c5-336e-9d3b-8e346af9825c | -3.21527 | -50.31242 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ae91247-5e29-3578-8964-bce04b9becd6 | -3.59991 | -50.24228 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9a32bcf-5fd8-3867-b26d-e8049dfa06f9 | -2.25222 | -46.50569 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c703a03d-69bd-3ae7-a336-c8349e866d14 | -5.39037 | -40.65291 | 2024-11-10 04:14:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7f2fa733-b265-333f-87e2-2225bf78f364 | -2.09242 | -46.53871 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 657f5c92-8e18-3c39-918c-861babe06f5e | -2.24002 | -53.79659 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36b46ddd-1a94-3251-a5bf-9fcf98826e43 | -2.7292 | -51.73421 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90165d03-f2a6-3fe3-b334-ffbc3e9171f1 | -1.636 | -48.20337 | 2024-11-10 04:14:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4e9c8e1-2cb8-3420-812c-1728ec0012f0 | -5.97561 | -45.36625 | 2024-11-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 23487569-1b7f-37f8-b032-f0c6a86dd58e | -3.34031 | -50.36192 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5fec4987-caa6-35f4-90c7-9b90bbfc2ab8 | -3.23588 | -50.27736 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 64fea463-e505-3715-86c0-07e4a2354185 | -1.27782 | -53.71209 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f17fdef0-2667-3ff0-a799-d854bc456b9f | -2.87176 | -49.44204 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4d2105f9-677a-3feb-b14a-f0ad8d578df8 | -3.11923 | -50.1481 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fc42311c-a022-390c-8cab-110db1bdf6ef | -4.22101 | -45.45053 | 2024-11-10 04:14:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 61c54c57-4ec4-378f-8bc4-7ea7af9a87de | -5.54666 | -41.67402 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6f70a7d5-3948-3068-b2b0-bb9138ee7027 | -4.49348 | -45.6991 | 2024-11-10 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a5e1e42-1e66-3233-849d-68a0a47635e7 | -3.20962 | -50.63544 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fbf21a77-871b-3806-9c4b-eda4f4ddbbff | -2.15852 | -48.53091 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c65fea78-c720-31d9-bab4-0b7363526d5b | -3.2483 | -49.58913 | 2024-11-10 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e3d86f8-9c21-3b31-ad7c-92b72e0d363c | -3.05695 | -51.08991 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ab4228dc-3e1c-350a-bec1-e0c0f48122f6 | -4.15604 | -45.74483 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8e82915e-67ba-3976-92e8-406c87613435 | -2.40389 | -46.78203 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83710b1f-ec60-3fdd-81f7-952417a0f339 | -3.24477 | -46.49159 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 75748d67-7e36-3f33-be9a-cccb8d624e9e | -1.40618 | -52.37037 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bfc2cfcf-be18-3695-ac43-3c2064c3f738 | -2.69022 | -46.80486 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 298c4c40-4576-30d5-884d-c7f6e14fcd36 | -4.11059 | -45.70848 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6258859c-c1d7-38b2-aebd-6c9019cea8eb | -2.87589 | -51.3061 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 873cf600-c5de-3fba-a3ec-7d188d1b54d4 | -3.89975 | -51.92333 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5c88c960-962c-3d08-a822-f625c7371046 | -3.74451 | -49.89549 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9b13dfd-d30a-36ce-8b7a-a8d0513da6a6 | -3.22438 | -50.44185 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c4897d2-d91f-3d9e-97b6-3a37f90df4c2 | -3.52068 | -40.9054 | 2024-11-10 04:14:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f276af4d-da8d-3fb7-9e03-12f9b7fd303a | -2.42761 | -46.3085 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 22b19fee-4e0b-3aad-a65c-23100cd33646 | -3.57323 | -45.82675 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8c5cd58-70bb-319a-9ccc-fd634fcdca3a | -5.08176 | -47.79189 | 2024-11-10 04:14:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33834f14-139e-3ff0-90f5-d3f9feabbe75 | -3.966 | -48.99641 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08ab8cd1-7218-3150-b766-9744ec42e383 | -2.06642 | -46.33347 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2bb5caa5-61c0-3947-ab75-fcb02be55ddc | -3.24699 | -50.30103 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f8400f85-0d9b-3b64-9055-4ade1ebd39a9 | -4.62844 | -49.08804 | 2024-11-10 04:14:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11796a6b-8d20-33c4-9fba-f9e349bd9c80 | -3.95725 | -48.17171 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 50a070f0-c027-395d-b0da-6731269cee30 | -3.11607 | -45.96363 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be7d7dc4-9eef-3e0b-b65b-7ba9f902d45a | -5.45663 | -41.66351 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 54deb95c-a9d7-362b-a711-3bc589243652 | 0.0508 | -49.55032 | 2024-11-10 04:14:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 163f62d1-f15b-3a31-bb4d-81f5645a6373 | -3.6167 | -47.52228 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2252c6b9-d7aa-3c61-aeb3-b9d5b48016a1 | -2.1105 | -46.47343 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 18ecfc9c-ca1b-3a81-87bd-e3bc2953b985 | -3.2296 | -50.45591 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4251772-8667-3005-b0f0-ef12dd394a01 | -2.36205 | -46.79525 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76d720cd-c2c0-3bd7-839f-7c350588e1d8 | -5.68563 | -38.04031 | 2024-11-10 04:14:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5da2d1b2-a156-3d2e-9312-fc7afa599f57 | -3.221 | -50.3078 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0207cb30-2603-38ff-b987-0b74ade0cdd1 | -4.09984 | -49.11794 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a0aa331-a45b-376a-b9b3-49f3c8a72457 | -4.68803 | -48.74678 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3906083d-0f25-3197-b138-ce24656e3b07 | -3.03061 | -50.35302 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b20b442f-f821-3617-95e2-a243d7da7443 | -5.32532 | -45.06081 | 2024-11-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| da813aa1-9e33-30b8-bbd3-84fcffe3213c | -2.18739 | -46.77776 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4008f9b8-1172-3bbd-aca9-bb09ea58c9f1 | -2.21141 | -47.74378 | 2024-11-10 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3aa7da0e-d036-3100-bfb5-5f4b2992ac73 | -2.65471 | -48.47294 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c65addb9-54fe-3521-82d4-5c244719ff14 | -3.30254 | -50.13864 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2ec05b6b-afbf-349e-85bb-bd362366c6cf | -3.23732 | -50.45528 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ae6ce15e-94bf-3025-8819-1cfec4b5266c | -2.93285 | -52.77319 | 2024-11-10 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 062ae7d3-974a-37b3-a279-7860deeb2194 | -2.46596 | -53.69084 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edb46c35-b45d-3670-be6d-fca047bda076 | -3.42286 | -53.0515 | 2024-11-10 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f837920d-6e7c-3ae1-b740-4c8381446a70 | -3.03607 | -50.30099 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fb90a79-8cd7-3c61-88a7-7b74b6ce6731 | -3.29015 | -51.27386 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 472ffdf5-698d-378c-ac2c-1fec52738393 | -2.68249 | -46.80363 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f79926d-ac37-3635-8a07-14ad2f54c1ff | -3.0438 | -49.54487 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 41931ba5-5996-355a-845e-3e5de9c7f32b | -3.25411 | -53.40378 | 2024-11-10 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| efff9abd-68c7-3e9e-b9c9-ba5abf781eb9 | -4.09779 | -49.12937 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df4cf1ad-3fee-3f4d-815a-3cc594775672 | -3.59085 | -50.27081 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 510001f3-3a18-3308-9e56-d2615fdab2d1 | -2.18876 | -46.7754 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54f16564-4c60-35c4-a1bf-aa893ac7a882 | -5.38028 | -42.75132 | 2024-11-10 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| cb930d0e-b212-3289-954e-bba4159663c9 | -2.22567 | -46.43189 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92d9d22e-0105-33eb-be26-30318ac3b298 | -2.94427 | -49.34296 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3499f816-70ba-3190-bfba-c4fa4fb11bff | -4.07688 | -46.07685 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 277a5829-7b12-3f8e-9df3-5c725700599e | -4.77855 | -48.08104 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45127c21-2885-3487-a569-54452f9670f7 | -1.40484 | -52.36918 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aed45493-5718-3b4a-bfbe-2ea1ee88e212 | -5.19959 | -45.95485 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 610ed761-0cad-3c59-a776-34f327f623fd | -2.29267 | -46.4975 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bc8e2ef-7950-33b3-b803-72802b3c3635 | -2.92917 | -51.47319 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0d362be1-9847-386a-bdc8-a51f5bfb623d | -1.47871 | -54.30386 | 2024-11-10 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55889fdf-44a1-3bd5-ac7d-62b54817fed8 | -2.60656 | -47.95951 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a53e19d9-9909-3782-99e0-e01080e075a3 | -3.08838 | -51.12341 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d67ceec-15b3-3601-97ec-7a9e6d1fdc6b | -3.89594 | -50.29679 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README41.md)
