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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba78e0a4-2f67-3973-a0d3-b4207f5a41ef | -3.5126 | -50.2133 | 2024-11-19 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| c881b396-3cdf-3b13-9dc8-a26909ce3440 | -1.5869 | -53.7933 | 2024-11-19 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 143.9 |
| c8eaaae8-581a-3e9d-8224-9e2b183cce03 | -2.4477 | -54.6213 | 2024-11-19 02:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| ab4606f4-2f95-36f9-808f-2879de1da731 | -4.5616 | -47.9925 | 2024-11-19 03:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| e260bcf7-7889-31fb-a0f8-db254b53b338 | -13.264 | -56.8149 | 2024-11-19 03:00:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| e8ed2d50-fec6-301b-8513-189c24350ae0 | -4.1246 | -43.5833 | 2024-11-19 03:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 869d0722-b572-350e-bcd1-861dd6f07af4 | -2.4293 | -54.6216 | 2024-11-19 03:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 5dcd90b5-d2e4-383b-999a-ecc4137ba703 | -4.5614 | -48.0141 | 2024-11-19 03:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| d9da9288-b219-30aa-ac66-a51a392f369b | -4.3958 | -47.7835 | 2024-11-19 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| bb2f469d-09a1-3135-a40b-408f6db7fab2 | -1.3962 | -47.4667 | 2024-11-19 03:00:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| c1405392-d8e0-3aae-83c4-eb2fc193d538 | -4.58 | -48.0132 | 2024-11-19 03:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| df9fc215-4f71-33a1-9d20-572c0f2f85e4 | -4.5613 | -48.0358 | 2024-11-19 03:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 7e79f163-1387-3523-a425-c9de6225d254 | -5.979 | -45.3395 | 2024-11-19 03:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| d4fd5cdc-5a89-354f-a348-7ac4786b8d07 | -5.9788 | -45.3621 | 2024-11-19 03:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 2fd2aec7-714f-364c-96d0-aadb1a7d7831 | -1.5869 | -53.7933 | 2024-11-19 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 155.1 |
| 4cf29f7a-d62f-366c-acea-2f7264441abc | -1.5869 | -53.8134 | 2024-11-19 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 161.4 |
| fadf3198-edfd-315b-ac5d-086afdda8cc7 | -4.5429 | -48.0151 | 2024-11-19 03:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 94572006-45a1-3b7f-b1ad-216b94614751 | -2.766 | -52.5959 | 2024-11-19 03:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 41e0c0aa-d7d5-3089-93cd-8f2b3823b945 | -4.3959 | -47.7618 | 2024-11-19 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 156cbdc2-1b4c-33c1-8960-d7e10d9cc15e | -1.3962 | -47.445 | 2024-11-19 03:00:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| cfcec1e7-42d6-3a2b-abc5-38c1d464bebd | -3.5125 | -50.2343 | 2024-11-19 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| ac2b806c-dde4-333c-a5d7-15963936d184 | -6.4271 | -35.25265 | 2024-11-19 03:06:00 | NOAA-21 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dde5eedc-8fde-3a38-8b6f-2ad28caa2699 | -7.87752 | -34.83911 | 2024-11-19 03:06:00 | NOAA-21 | PAULISTA | PERNAMBUCO | Brasil | 2610707 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0f7192c7-6d01-3204-b107-c7aea065e61c | -5.53105 | -39.17934 | 2024-11-19 03:06:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 99aa8240-260e-353f-8176-421e68adef72 | -8.51062 | -35.44113 | 2024-11-19 03:06:00 | NOAA-21 | GAMELEIRA | PERNAMBUCO | Brasil | 2605905 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5f7f0e70-ed57-3d06-a803-5c06539d4060 | -5.95102 | -39.66646 | 2024-11-19 03:06:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f71c72a3-5e2e-33d3-9099-d6a2a12c93b6 | -7.37789 | -34.88606 | 2024-11-19 03:06:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a2b9a486-4b67-3036-94a9-3434adf5e7e1 | -5.86342 | -39.66314 | 2024-11-19 03:06:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 561d838c-effa-3bc7-a8b0-53a403bf5226 | -8.51007 | -35.44419 | 2024-11-19 03:06:00 | NOAA-21 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| caf44597-ba6b-3992-beca-86e0711c0284 | -6.42767 | -35.24932 | 2024-11-19 03:06:00 | NOAA-21 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4a4b1ffb-5d3a-36fd-b99b-ee1672106b05 | -10.13761 | -38.52658 | 2024-11-19 03:08:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| b2546c62-0275-341a-aead-caba31ddb48d | -10.13365 | -38.52364 | 2024-11-19 03:08:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 9b63f1c5-d78f-36e3-9c91-b2bba23ecb41 | -10.13848 | -38.52226 | 2024-11-19 03:08:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| d553ef79-7ec9-33ab-99b4-7cd764bee1d0 | -10.1406 | -38.521 | 2024-11-19 03:08:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| da438c18-601e-3836-9494-9d4db36deb49 | -10.13977 | -38.52534 | 2024-11-19 03:08:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 16330533-91f7-35e2-8939-67da69d4c7ba | -13.264 | -56.8149 | 2024-11-19 03:10:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 0c903914-f201-3f1b-81b1-4bde56b57856 | -3.5125 | -50.2343 | 2024-11-19 03:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 97575ef6-59c7-31d3-8e6e-815bf58df0b6 | -2.4293 | -54.6216 | 2024-11-19 03:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 377ff303-0265-358f-8ca2-6c179d5e4a40 | -2.766 | -52.5959 | 2024-11-19 03:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 520a34a8-9821-3963-a74b-c52bbd5bfc2b | -4.5614 | -48.0141 | 2024-11-19 03:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| aa19434b-722f-3075-bcc0-e52bff5c6fa2 | -1.6053 | -53.8132 | 2024-11-19 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 79853002-b5ef-34e2-9963-2863da0e0e99 | -4.5616 | -47.9925 | 2024-11-19 03:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| a67bb111-e0b6-393d-a383-1a53f04ad146 | -3.6063 | -54.2129 | 2024-11-19 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 49d4564e-dd71-3e1b-b439-e9240a62578e | -23.97 | -54.1595 | 2024-11-19 03:10:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 78.1 |
| 06143413-5c92-3bd3-ad0d-3c00109ef573 | -1.3962 | -47.445 | 2024-11-19 03:10:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| e7f90bb3-f113-31c5-ae0f-98cf65a7e4cb | -4.58 | -48.0132 | 2024-11-19 03:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| bd6ff2ea-e952-344e-95fe-770c0dfb7b16 | -1.4147 | -47.4447 | 2024-11-19 03:10:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| d7cd754c-2163-3ec1-8d17-bb18de468fc2 | -1.5686 | -53.7935 | 2024-11-19 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| c5277f14-a0b9-3365-a4ba-c282df2df7a4 | -4.1182 | -51.0486 | 2024-11-19 03:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 177c1265-3ab2-30be-953b-8ebdf8d40a36 | -23.9706 | -54.1372 | 2024-11-19 03:10:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 110.3 |
| df5840b8-b9f5-3be0-8316-5a0545101f05 | -4.543 | -47.9934 | 2024-11-19 03:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| da759a21-1ad8-343e-8b31-50c916e0963b | -5.9788 | -45.3621 | 2024-11-19 03:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 5f7f9929-40c6-3e4c-b00e-0550258add08 | -1.5685 | -53.8137 | 2024-11-19 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 29b9c50a-50d1-35fd-82bb-4ea6d6b78968 | -1.6053 | -53.7931 | 2024-11-19 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 6126932b-ede7-3902-a132-89286113e17e | -1.5869 | -53.8134 | 2024-11-19 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 209.5 |
| 8369b53e-f27a-3c69-ab58-ca1d89f52394 | -4.5429 | -48.0151 | 2024-11-19 03:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 73e15cac-b780-3a28-88ce-e6af13b0c096 | -1.5869 | -53.7933 | 2024-11-19 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 181.2 |
| fea3aae1-12e9-3bde-95cd-498dc129fb8e | -22.67742 | -42.86141 | 2024-11-19 03:10:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e0170d71-03b6-3ad3-b2e7-7c2378c16f14 | -22.67878 | -42.85589 | 2024-11-19 03:10:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 62a55736-cfc6-3d09-beb2-db763fc82685 | -4.5616 | -47.9925 | 2024-11-19 03:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 0e2471a0-9220-3e46-b6af-754b1ea4ffed | -1.6053 | -53.8132 | 2024-11-19 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 85f534d9-f9e4-3e15-a8f3-2251f50f3c83 | -1.3962 | -47.445 | 2024-11-19 03:20:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| ed1671b1-65d0-38f2-9cbd-705e606971cb | -1.5869 | -53.7933 | 2024-11-19 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 2f9097b5-6e96-3f8e-91b4-1aa7835d59a8 | -23.95 | -54.1191 | 2024-11-19 03:20:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 110.1 |
| af7bc51b-2e41-3ee8-9fdb-f8df4a35746e | -4.5429 | -48.0151 | 2024-11-19 03:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 95404cbf-f23c-3948-9a88-aa64894b16fd | -5.9788 | -45.3621 | 2024-11-19 03:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 057f2bc1-c929-36d9-bbb2-6d1e89994beb | -4.1182 | -51.0486 | 2024-11-19 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 61370ee1-7085-3ee1-a393-88e704186b52 | -1.424 | -52.4368 | 2024-11-19 03:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 1b62e076-be46-37a1-b65c-fd63a8b87a8f | -23.9706 | -54.1372 | 2024-11-19 03:20:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 134.9 |
| cc9cbe29-5381-3a9a-a853-b66a0b9820db | -3.5126 | -50.2133 | 2024-11-19 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 82dfed5b-5c8b-3bbc-934d-94311edc6c21 | -23.9711 | -54.1148 | 2024-11-19 03:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 103.3 |
| 9d456b2f-a4fc-3e73-81ab-ce2117ebf817 | -23.97 | -54.1595 | 2024-11-19 03:20:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| a0527f23-1cb0-371e-b0a8-968a94d7ec73 | -23.9506 | -54.0968 | 2024-11-19 03:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 70.4 |
| 65e48b2d-4263-3c7a-a7da-3e98f9164b54 | -13.264 | -56.8149 | 2024-11-19 03:20:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 3091d30f-e35b-303f-8c06-a347f33922e7 | -3.5125 | -50.2343 | 2024-11-19 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ae5aa4f0-7609-3c4c-bf0c-145e89127b2c | -1.5869 | -53.8134 | 2024-11-19 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 24b5b2ce-000b-3194-9246-5a4bd30ba688 | -4.58 | -48.0132 | 2024-11-19 03:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| b94f8058-384f-36cc-8fec-702e5bc5407e | -4.5614 | -48.0141 | 2024-11-19 03:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 165.1 |
| 48568a8f-b080-3144-b44e-cb94ebf5e9b4 | -4.5613 | -48.0358 | 2024-11-19 03:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 0ee8a1dc-2532-3a4f-ad68-255b709ab363 | -5.97941 | -45.36721 | 2024-11-19 03:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 7209b2f1-ea27-38eb-bdb5-76d987df28f2 | -5.97231 | -45.3663 | 2024-11-19 03:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 3743bea8-2e2c-3141-aaba-2069e4247bae | -3.23259 | -42.69341 | 2024-11-19 03:27:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97f47e58-bf53-3dd4-a143-6147a7d17a5f | -7.99698 | -44.37068 | 2024-11-19 03:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7d502e5e-d022-3529-a3b2-2ae055ffe637 | -5.95235 | -39.66474 | 2024-11-19 03:27:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 748501f2-6e80-35aa-a6ac-10c84db15eb2 | -7.39863 | -42.76406 | 2024-11-19 03:27:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| e407ef43-4e00-3f75-bd13-72270b720d5a | -4.80043 | -37.80563 | 2024-11-19 03:27:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e83f6200-425e-352b-9a61-58160edb858d | -5.82051 | -35.38316 | 2024-11-19 03:27:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 8.5 |
| cd948053-fce5-30fc-b1d2-8fbde8920563 | -7.75451 | -34.95846 | 2024-11-19 03:27:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 504107ae-85c0-3ca2-80aa-20966e4ae06b | -5.98068 | -45.36055 | 2024-11-19 03:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 555a0276-ad4b-3bfc-8cc4-56955f3149f7 | -3.29926 | -43.54676 | 2024-11-19 03:27:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7b0764e-1d48-3348-8971-aa095a6575a0 | -4.10881 | -43.58842 | 2024-11-19 03:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| db671098-e488-328a-b13d-51d408a50e2f | -6.93034 | -42.81475 | 2024-11-19 03:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 31206ede-8635-3e44-a870-7752e899c961 | -5.58419 | -44.87626 | 2024-11-19 03:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f8d08cf-9ba0-3d94-bae2-3f910cb6b7ab | -5.39044 | -40.65731 | 2024-11-19 03:27:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 7bdec0d3-1cc3-3cb4-a36b-09a43571b137 | -3.91953 | -42.41885 | 2024-11-19 03:27:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 50038713-c5ec-3a5e-900e-5e55a113b1fc | -5.97658 | -45.36111 | 2024-11-19 03:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| d4cc9eb0-4724-3568-87b7-770a90cebe4e | -5.9877 | -45.36187 | 2024-11-19 03:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8484999-0fa0-305b-94db-83d1a7aad45a | -5.97359 | -45.35962 | 2024-11-19 03:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 1b70d400-43c0-3d66-9c81-5c777e3433a9 | -8.00512 | -44.39567 | 2024-11-19 03:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e615f3d4-3c09-3dbe-99cc-6dc2c22e6497 | -7.89848 | -44.21843 | 2024-11-19 03:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README14.md)
