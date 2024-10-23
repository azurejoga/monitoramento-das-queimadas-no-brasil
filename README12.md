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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b4d437a-0a88-36fe-aec8-2031599d40a6 | -17.0188 | -57.4973 | 2024-10-23 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 5ae799d1-0688-3cb8-b5f5-d5f312115ab9 | -16.9988 | -57.52 | 2024-10-23 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 425290cc-02c0-30c3-851f-68a9ac212dee | -17.0184 | -57.5178 | 2024-10-23 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.5 |
| e5eb52c3-be5f-3b5b-98ca-57b0fc75f5e8 | -17.6868 | -57.4593 | 2024-10-23 02:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.0 |
| e1bdb057-69d2-3b33-bec0-4cd3caa89fae | -17.6865 | -57.4798 | 2024-10-23 02:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.9 |
| 3ffa06a5-704c-32ba-ba12-97f2d5efa362 | -17.764 | -57.5526 | 2024-10-23 02:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 8f7f0bf6-2f77-3b15-b369-89a724cf9415 | -17.7637 | -57.5732 | 2024-10-23 02:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.4 |
| b81060ba-cf2a-3a56-899e-27b1c4302804 | -18.3207 | -56.1986 | 2024-10-23 02:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.6 |
| da90b1b6-f535-3b82-bf53-485fbd10cf2e | -18.3203 | -56.2195 | 2024-10-23 02:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.5 |
| 0bb4fc30-7e3b-3fce-8df7-790d9378bb16 | -18.3004 | -56.2222 | 2024-10-23 02:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.4 |
| f5549156-2890-32bb-8d61-3073dd7039f9 | -18.2637 | -56.0603 | 2024-10-23 02:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 53403ef1-9da2-3b0b-bf45-330ba4c3d0c0 | -18.2633 | -56.0812 | 2024-10-23 02:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.9 |
| 76893728-e3cc-36f0-94df-b08b65680dd2 | -3.1102 | -54.146 | 2024-10-23 03:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 7fac4eb2-3f45-3b00-865a-fd860ffe5dd3 | -3.1101 | -54.1661 | 2024-10-23 03:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 86119de1-4372-3a4c-8e98-40ab8516cd11 | -3.0917 | -54.1666 | 2024-10-23 03:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 01ab5ad9-85d8-34a9-9e07-65974ddba365 | -3.5491 | -54.7351 | 2024-10-23 03:05:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 3e355ab8-f6b3-35e6-b66d-06e0e568f9df | -4.1306 | -45.5663 | 2024-10-23 03:05:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 2a00731f-1c0e-3415-9135-cced62015ab2 | -4.1305 | -45.5888 | 2024-10-23 03:05:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 554.1 |
| 00592e55-f2b2-3167-8012-0171a8d07b8b | -4.1304 | -45.6112 | 2024-10-23 03:05:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 235.6 |
| f87aed1a-377f-3151-979d-a14d5924c93b | -4.1905 | -47.9885 | 2024-10-23 03:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 8d59f503-a419-34e0-9b16-908b39559512 | -4.1719 | -47.9894 | 2024-10-23 03:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 7e5808cb-bf8b-361a-9c8d-50846c673d3b | -4.1491 | -45.5878 | 2024-10-23 03:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 171.5 |
| 438ecb39-407e-3bf8-975c-ddcf8bd2b7c8 | -4.149 | -45.6103 | 2024-10-23 03:05:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 600a0182-65e6-3237-b4ed-c49b71646dec | -5.5671 | -43.2576 | 2024-10-23 03:05:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 9061e8de-e97e-3f9e-be9c-a716d388abe7 | -5.5858 | -43.2562 | 2024-10-23 03:05:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 2bfb1dcc-9e67-3915-a174-15845c96ed07 | -17.764 | -57.5526 | 2024-10-23 03:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.7 |
| db3d120c-0cf2-3d35-8b81-ba4ab3cb9c17 | -17.6868 | -57.4593 | 2024-10-23 03:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 8e381133-513b-3595-a23f-1b1c4ff8c88d | -18.3207 | -56.1986 | 2024-10-23 03:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 703ab692-f27d-34c2-8be0-d6161732fa20 | -18.3203 | -56.2195 | 2024-10-23 03:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.0 |
| d52e7a42-6d7b-306c-857d-1e04a0a0c154 | -18.3004 | -56.2222 | 2024-10-23 03:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.5 |
| d62412fa-92c9-30e5-ad83-8f32986da767 | -18.2637 | -56.0603 | 2024-10-23 03:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.5 |
| 59c8d8e0-a0e2-36db-ba11-b2c36ad070b5 | -19.5469 | -56.6773 | 2024-10-23 03:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 583ac8e7-1ec0-372c-98c9-bd8d8d12cfa0 | -9.34116 | -36.00958 | 2024-10-23 03:13:00 | NOAA-21 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 3369ebfe-51f5-389d-b685-fadfc0acb7ab | -8.88452 | -35.39801 | 2024-10-23 03:13:00 | NOAA-21 | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| f3243fe8-162b-3370-8dca-8c3bdc4dc38d | -8.88357 | -35.40322 | 2024-10-23 03:13:00 | NOAA-21 | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| cea964d7-f59c-3624-b69d-1eb6c9815e3f | -6.99644 | -38.77179 | 2024-10-23 03:13:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 67bd0c65-8eaa-327a-a5db-caa867ede345 | -6.71689 | -37.51499 | 2024-10-23 03:13:00 | NOAA-21 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 3.8 |
| db211120-e10b-3e9a-83a1-7114dfcc9af2 | -6.30158 | -35.21568 | 2024-10-23 03:13:00 | NOAA-21 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fce27cb4-be0e-3aa8-a45c-79d581eb6db2 | -5.75071 | -39.78217 | 2024-10-23 03:13:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5f703b91-6eae-3547-950d-0ecc46bd976c | -10.65628 | -40.81709 | 2024-10-23 03:13:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d91a29e6-e246-30e0-b58b-cb5888b00cff | -10.50128 | -36.72289 | 2024-10-23 03:13:00 | NOAA-21 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 82217d5f-ddce-36f7-b150-d8e1a892e5ae | -15.84806 | -43.49805 | 2024-10-23 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4efece27-164d-3cfc-aac5-13053e2c6525 | -15.8465 | -43.50488 | 2024-10-23 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed6d53d8-7831-3af0-987c-205705a0ae30 | -15.52038 | -43.13526 | 2024-10-23 03:15:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 6388516c-b59a-3908-a8c4-1a3b39d05fdd | -1.3879 | -52.0072 | 2024-10-23 03:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 3ff4ac81-ab20-3fc5-8247-fe154842514b | -1.388 | -51.9867 | 2024-10-23 03:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 872048b7-1eaf-33c1-8809-23ed7728a737 | -3.0917 | -54.1666 | 2024-10-23 03:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 9246ab2d-8a1e-306e-a915-f9474241d0cd | -3.1101 | -54.1661 | 2024-10-23 03:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| c3c9729c-6558-32ba-bb9a-3da6c27249e1 | -3.1102 | -54.146 | 2024-10-23 03:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| cded7d51-a505-3c09-a0a5-ae003c59a30e | -3.5491 | -54.7351 | 2024-10-23 03:15:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| d3ff2a2c-ebbb-3f73-9766-451a676ce317 | -4.1304 | -45.6112 | 2024-10-23 03:15:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 414.1 |
| 196eecb5-bc67-3513-ab89-191911c8ee98 | -4.1305 | -45.5888 | 2024-10-23 03:15:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 956.6 |
| d732d902-1c90-3521-9cff-02de2f5a501a | -4.1306 | -45.5663 | 2024-10-23 03:15:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 71c28604-1917-3775-9bdb-7a9cb65812cc | -4.1119 | -45.5897 | 2024-10-23 03:15:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| c517b850-12b2-34f8-8074-80d76260bdb0 | -4.149 | -45.6103 | 2024-10-23 03:15:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 126.3 |
| ef9c9f67-29e0-3c63-961d-d84ac2253f36 | -4.1491 | -45.5878 | 2024-10-23 03:15:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 278.3 |
| 254bf83a-9f99-31ff-96f6-a2375c448dd4 | -4.1719 | -47.9894 | 2024-10-23 03:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 409bf47a-4277-3e1a-a7a4-d799be938eb1 | -4.1905 | -47.9885 | 2024-10-23 03:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 55dbe3b1-203f-3b26-8397-3d5f028dd419 | -10.6725 | -58.749 | 2024-10-23 03:16:07 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| e3db15ed-c63c-3173-aad5-3f7c051baa41 | -17.6868 | -57.4593 | 2024-10-23 03:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.6 |
| a0837cfb-2cd8-3aae-9f7b-946e0e3b8240 | -17.7637 | -57.5732 | 2024-10-23 03:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 34dc5801-6b6b-353e-aeec-3ec4606f1680 | -17.764 | -57.5526 | 2024-10-23 03:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 4edbcda2-f5ce-384e-8bad-d6f454207257 | -18.2637 | -56.0603 | 2024-10-23 03:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 4c8d727e-a143-37b4-bef1-f12f6e3a61a4 | -18.3004 | -56.2222 | 2024-10-23 03:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.6 |
| b7fa72e9-7fe3-3f47-9778-1a3b29f3e5e2 | -18.3008 | -56.2013 | 2024-10-23 03:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 17435224-ebc6-3cfa-ac8b-b14ccfca73f9 | -18.3203 | -56.2195 | 2024-10-23 03:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.7 |
| 269a7771-4b6e-3792-9c28-9d5129aba6b5 | -18.3207 | -56.1986 | 2024-10-23 03:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.9 |
| 372f2369-a22d-3293-99b6-3c0972927dd6 | -19.6245 | -56.8129 | 2024-10-23 03:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 52.8 |
| f0286d9d-4aaf-3cb2-bb76-57a7a6df15e9 | -19.6249 | -56.7919 | 2024-10-23 03:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 70.7 |
| bf524a4a-ab93-3a0c-a828-1d39e41a5ccd | -19.6446 | -56.8101 | 2024-10-23 03:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 64.5 |
| a21a3db4-2ff1-32fe-b732-f493a72aff0c | -19.645 | -56.7891 | 2024-10-23 03:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 30fd9d30-443b-3251-9784-dbcd1511e969 | -1.388 | -51.9867 | 2024-10-23 03:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 6a18b905-6e73-36a0-813a-00d27f6f4384 | -1.3879 | -52.0072 | 2024-10-23 03:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| c1511f48-e8c4-3718-bacd-0bea6caf2d4c | -3.1102 | -54.146 | 2024-10-23 03:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 0f775c83-ffd3-34bc-9c4c-ed925ca14d85 | -3.1101 | -54.1661 | 2024-10-23 03:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 14558486-a613-3e99-955b-668548b96edf | -3.0917 | -54.1666 | 2024-10-23 03:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 30359af5-c006-3e7f-9d3e-7b3c094ded94 | -3.5491 | -54.7351 | 2024-10-23 03:25:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 18fbbc99-322c-3317-91ab-a4376442aa51 | -5.5858 | -43.2562 | 2024-10-23 03:25:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 87f18116-b59e-3058-a341-fd7c48179e2b | -17.6868 | -57.4593 | 2024-10-23 03:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.0 |
| 5a968893-2dd5-37ac-becf-f3217dc51470 | -17.7637 | -57.5732 | 2024-10-23 03:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.0 |
| b13be5e1-e3fc-3b16-95e9-be3c36d979af | -18.3203 | -56.2195 | 2024-10-23 03:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 1d245f49-aefc-31cd-b41b-5e69d984cf69 | -18.3004 | -56.2222 | 2024-10-23 03:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.5 |
| 60dc4cdb-8236-3148-a9e0-f1df2277675c | -19.548 | -56.6143 | 2024-10-23 03:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 49.9 |
| cb5a214a-3481-35bd-ae8f-14b458be1a26 | -19.5473 | -56.6563 | 2024-10-23 03:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 26cbf7af-0ccb-3cf8-b979-180415cd2358 | -19.5469 | -56.6773 | 2024-10-23 03:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 8e857965-64b4-31dd-baaa-d84774748160 | -19.5465 | -56.6983 | 2024-10-23 03:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 50.1 |
| 25951f7d-53d8-38bd-a587-f1a594ab9928 | -19.5272 | -56.6591 | 2024-10-23 03:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.5 |
| 1872e97c-d296-3e5b-a859-f9c9c6c4654b | -19.5268 | -56.6801 | 2024-10-23 03:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.9 |
| 5952a2f7-fef5-3e13-a493-eda0298075b5 | -19.645 | -56.7891 | 2024-10-23 03:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 62.6 |
| 3c1e89f4-23e0-34c1-ad67-51a12d3562b5 | -19.6249 | -56.7919 | 2024-10-23 03:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.7 |
| 4f9f6f75-7083-31e4-93b9-14f10aec19fa | -5.75054 | -39.77692 | 2024-10-23 03:34:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c5361548-7ba6-33a8-9699-0a717fb10c37 | -6.73198 | -40.49419 | 2024-10-23 03:34:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1b9d84e9-81f6-33e5-b4d4-b1b0171fabf7 | -4.95035 | -37.42492 | 2024-10-23 03:34:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bcf8b545-21f3-3292-91d7-0f2974860cda | -4.94856 | -37.42729 | 2024-10-23 03:34:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| cecbfc95-d5f7-3b34-b94f-bf5897f61637 | -5.26161 | -41.18786 | 2024-10-23 03:34:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bc656e11-02bb-38a2-8760-9a480ea5bd20 | -5.26065 | -41.19355 | 2024-10-23 03:34:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d7aa9f86-0324-36ec-9531-8fa9106634a7 | -3.80644 | -42.5474 | 2024-10-23 03:34:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c6b47a2-e830-3ec3-bdd6-5a0a10f66f2c | -6.19578 | -43.43021 | 2024-10-23 03:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f93f1420-f3f2-358a-82a0-d8659c38a664 | -6.19504 | -43.43429 | 2024-10-23 03:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a806e30-8fb6-320c-bc0d-70cfe590cdd4 | -6.19374 | -43.42949 | 2024-10-23 03:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README13.md)
