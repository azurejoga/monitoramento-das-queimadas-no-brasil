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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9699e8d-2e85-3c5a-9bae-842dadee8903 | -18.8675 | -53.6434 | 2025-06-03 00:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 85.4 |
| b99342d3-c80e-348c-8d44-7cc7dd1d617a | -18.8875 | -53.6402 | 2025-06-03 00:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 06d672da-dbf4-38a5-95d2-81a8b19349eb | -11.2546 | -49.5098 | 2025-06-03 00:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 130.5 |
| bb702e4e-7b26-3797-899d-a3356410a029 | -11.2359 | -49.4903 | 2025-06-03 00:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 01030e3c-c5cb-3b06-b463-f124f3184ec0 | -6.9602 | -42.9052 | 2025-06-03 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 07347def-5f02-30d2-aabf-8ddab35f81f4 | -11.9027 | -54.7931 | 2025-06-03 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 0744b617-db1c-3c17-93b6-5f0792dac9de | -11.9029 | -54.7726 | 2025-06-03 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 83691c13-65a1-3488-9b66-1e4bfd908335 | -11.2549 | -49.4881 | 2025-06-03 00:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 235.6 |
| 50891c18-008f-37ba-9f1c-ca08b385c409 | -8.9074 | -50.05 | 2025-06-03 00:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 14af3143-f96b-3585-bf13-6b531c9d0570 | -11.274 | -49.4859 | 2025-06-03 00:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 12129699-ed7e-3904-b942-e57c2843ee07 | -7.2214 | -43.1153 | 2025-06-03 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 40151c15-f10c-324c-aa76-2dc1b999ac20 | -7.2211 | -43.1388 | 2025-06-03 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.0 |
| 094fd1d8-bf10-3cfc-9463-13dc70c03f65 | -13.637 | -52.1746 | 2025-06-03 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| c938c581-1ae1-3745-8413-64a06c735288 | -18.888 | -53.6186 | 2025-06-03 00:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 9e0e489a-f36c-3ea1-89a6-c57003f6ed7e | -6.9791 | -42.9034 | 2025-06-03 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.3 |
| bdcfae73-fce7-35ab-ac9c-156cd77091c3 | -18.8679 | -53.6218 | 2025-06-03 00:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 664d37dc-0fe5-3094-afd1-229c95bd5ba9 | -18.8875 | -53.6402 | 2025-06-03 00:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 164.7 |
| d0c83dac-dbb0-3353-9673-5e27c925472f | -11.2549 | -49.4881 | 2025-06-03 00:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 26671965-e152-3df4-b1f1-fe8b3e73c811 | -11.2546 | -49.5098 | 2025-06-03 00:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| b8cab6d5-2b2c-3898-b014-e0999314d22e | -18.8675 | -53.6434 | 2025-06-03 00:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 189.8 |
| f5d317b2-3911-37fd-9ac5-cdc43f03dd4b | -7.2214 | -43.1153 | 2025-06-03 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 63ea2679-8cfe-335b-856f-9030d0962c85 | -7.2211 | -43.1388 | 2025-06-03 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 8eb4fd17-5ff1-393f-a513-658f7b48d662 | -10.462 | -47.9428 | 2025-06-03 00:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| d1789aa0-0fb6-3b7b-afc2-e39f6f71b023 | -18.8875 | -53.6402 | 2025-06-03 00:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 1a34efa5-0977-309e-89cf-7daae1bb8eab | -7.2214 | -43.1153 | 2025-06-03 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.9 |
| 05cbc1cc-dec5-3d7b-85aa-c7bfd8c6e5aa | -11.2546 | -49.5098 | 2025-06-03 00:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 714cc027-b122-3b93-abc7-4b1a5a1e6f30 | -7.2211 | -43.1388 | 2025-06-03 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| b5a09dc7-76db-3e96-b46b-8c3b306de44e | -18.8679 | -53.6218 | 2025-06-03 00:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 72.3 |
| ec998fa0-7b56-33b7-b238-54a02f2b8ec0 | -11.2549 | -49.4881 | 2025-06-03 00:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 3d5c2431-fe9d-32bb-a99e-9a1ff9b79586 | -18.8675 | -53.6434 | 2025-06-03 00:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 0f8d1b38-971d-345c-86c7-0c3f1cb34d8c | -8.9074 | -50.05 | 2025-06-03 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| e01ab8a7-54b8-37c0-856a-f9f6f9366f1d | -8.9074 | -50.05 | 2025-06-03 00:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| d1bb6af2-6d64-3909-a0cb-46882e44ab2f | -11.2546 | -49.5098 | 2025-06-03 00:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 4cbf7b4c-734f-3736-81cc-e29f786e3283 | -18.8875 | -53.6402 | 2025-06-03 00:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 137.8 |
| aaaac271-9d52-3200-a06c-b47144882848 | -18.888 | -53.6186 | 2025-06-03 00:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 437508e7-89a7-3a74-b8a9-7260af763bf9 | -18.867 | -53.6649 | 2025-06-03 00:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 64.2 |
| a76fbcf6-26ec-36ab-8b4b-03a5768c3f4e | -18.8679 | -53.6218 | 2025-06-03 00:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 9461cbbb-f7d4-3a50-b83f-a5e911a8f28c | -18.8675 | -53.6434 | 2025-06-03 00:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 195.9 |
| 6a3355dd-96f6-38a6-8a8a-1e3fcd244a4d | -11.5617 | -56.4221 | 2025-06-03 00:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| e10093fd-e638-3a4e-8366-b93691d722b6 | -11.2549 | -49.4881 | 2025-06-03 00:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 23e68fe5-ac04-3937-a7d5-9a07308f6df2 | -7.2214 | -43.1153 | 2025-06-03 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 24b9b622-3d61-3f41-8781-b5035f1c3b95 | -7.2211 | -43.1388 | 2025-06-03 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.7 |
| 234fb46c-8786-3b51-aee6-3dcd9017fbe0 | -11.2359 | -49.4903 | 2025-06-03 00:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 2a80bb6a-4b53-39a0-a0ba-7fdf78afcaba | -11.2559 | -49.500702 | 2025-06-03 00:31:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65a089e7-2f71-3f6f-b8e7-ad69f8ae51cf | -8.4762 | -46.5061 | 2025-06-03 00:31:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 860d40f0-fa78-36ea-b4e2-81f8772c5c98 | -18.875 | -53.633701 | 2025-06-03 00:31:00 | METOP-C | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 29979f10-bbe7-3bbe-82fd-dab2d6b054db | -10.1441 | -52.1329 | 2025-06-03 00:31:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c53b6ae2-6d75-3bad-b358-dc3dbb0be3b4 | -8.9165 | -50.040901 | 2025-06-03 00:31:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad2ebd90-e725-3455-8ad3-288a9731bd40 | -9.0736 | -47.151699 | 2025-06-03 00:31:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40704892-d008-399c-8537-153274f006c9 | -11.5847 | -47.450199 | 2025-06-03 00:31:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae44074c-3f0f-31f6-b9dd-ae90acafa43d | -10.4621 | -47.950298 | 2025-06-03 00:31:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28ed064c-6f99-37e5-b6d6-3764f984fc92 | -7.0245 | -44.5742 | 2025-06-03 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bcf70038-d634-38eb-b76d-77425abccc81 | -9.3977 | -48.433601 | 2025-06-03 00:31:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c2f32250-0f8d-3672-b03b-c83897a93c43 | -7.2339 | -43.125702 | 2025-06-03 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4a5377d9-d8d3-37ce-bb13-a690573c6083 | -10.6738 | -44.384701 | 2025-06-03 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 20683f8e-55ed-3cd9-af57-076354fce078 | -10.2333 | -52.220699 | 2025-06-03 00:31:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d6b90ec-d4f8-319b-9aae-a9dee74ca07b | -11.9104 | -47.437698 | 2025-06-03 00:31:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 25188906-c2ee-35cf-b60f-a770afb57d2e | -9.1971 | -49.680599 | 2025-06-03 00:31:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 622b9e38-be14-3627-8742-c9bd3a2b075d | -7.2222 | -43.120201 | 2025-06-03 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0042becd-475b-3b98-bd32-d29449c20b04 | -8.916 | -48.9049 | 2025-06-03 00:31:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a18ae323-19d4-385b-baa1-e9b6d15ef8fa | -4.8091 | -45.2551 | 2025-06-03 00:31:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef3e369b-9a51-3adc-9001-9e5aaeaad915 | -7.0262 | -44.581299 | 2025-06-03 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0770f410-4daa-3895-9516-fd418c4e048b | -5.8366 | -46.361099 | 2025-06-03 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00d16f3c-3f96-3848-b2ef-90026d295605 | -11.6835 | -43.7953 | 2025-06-03 00:31:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1a3adf07-cdc5-399a-b94d-1088b97b580a | -8.0783 | -43.117001 | 2025-06-03 00:31:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 38f4311f-e216-3a6c-acc6-19043f18301c | -8.9068 | -50.042999 | 2025-06-03 00:31:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0182fc9f-9f91-3297-baa1-5eb97621d2b4 | -23.4527 | -47.684299 | 2025-06-03 00:31:00 | METOP-C | CAPELA DO ALTO | SÃO PAULO | Brasil | 3510302 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 60d90730-e535-38bd-bdcd-4ca09d8ec184 | -7.2259 | -43.135799 | 2025-06-03 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f5c631e3-b2e3-33d8-be90-a53c7b1e086c | -9.1992 | -49.6903 | 2025-06-03 00:31:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4fb5267-f44c-3ead-9aa1-cca291a05763 | -7.2241 | -43.127998 | 2025-06-03 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 015fbbb9-323b-39fd-8f10-f84a67046563 | -11.2635 | -49.488499 | 2025-06-03 00:31:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d8810912-2b25-3b31-aef2-71eaa5a3a8c8 | -11.2656 | -49.4986 | 2025-06-03 00:31:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 25178fa8-31ab-3539-8f08-0aac5d20207f | -7.0196 | -44.597698 | 2025-06-03 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e361e62-33ac-3b24-83a0-24c4b4677012 | -3.0432 | -49.433498 | 2025-06-03 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f30cd265-0af6-345f-9288-e41a9508c878 | -7.2357 | -43.133499 | 2025-06-03 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a4f5eab8-08a4-3302-a61f-4b709377b796 | -4.8206 | -45.259899 | 2025-06-03 00:31:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0fc587ab-e2a7-38bd-a63a-3e6e1ee3e7af | -11.5829 | -47.4422 | 2025-06-03 00:31:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1ae8d34-7989-37f9-8b1e-cb494920c155 | -12.3816 | -45.93 | 2025-06-03 00:31:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9560b78e-675e-3aba-9953-d3eccd8202f0 | -7.9015 | -50.364101 | 2025-06-03 00:31:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 674fe9c2-cd61-37a6-91d4-4a797d0cc522 | -6.249 | -43.370499 | 2025-06-03 00:31:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4861a03-0895-38dc-b0f4-f4408a8d66f8 | -10.6722 | -44.377701 | 2025-06-03 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eb8cb301-816d-3b22-9812-b361857a2e41 | -12.38 | -45.922798 | 2025-06-03 00:31:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 48034ccc-923b-34fe-9ed6-3da52d67df6a | -9.3843 | -48.418999 | 2025-06-03 00:31:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3916b55-9119-30c5-b4a2-99846f1afb90 | -4.8108 | -45.2621 | 2025-06-03 00:31:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c855c08d-df19-3fed-9536-fd795f8b1dee | -10.4603 | -47.942101 | 2025-06-03 00:31:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb78129d-19ed-3045-bed0-918c87636b01 | -6.9768 | -42.91 | 2025-06-03 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5fa9fef0-245c-33ab-95dc-07ca53933e35 | -23.454901 | -47.696301 | 2025-06-03 00:31:00 | METOP-C | CAPELA DO ALTO | SÃO PAULO | Brasil | 3510302 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5626b12c-beeb-37c4-80fa-1c0e05f0303b | -10.4585 | -47.933899 | 2025-06-03 00:31:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f5b5adf-b38e-31be-ab11-b18c6b97d2ac | -10.1343 | -52.134899 | 2025-06-03 00:31:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d9fefbb-c575-3da8-96cf-bd69929f8e80 | -10.4719 | -47.948101 | 2025-06-03 00:31:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ff8728f5-6e6b-3798-8a00-c05f16291c26 | -10.4701 | -47.939899 | 2025-06-03 00:31:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef98ffcc-46d7-32b9-b91e-014c92212469 | -8.1976 | -49.794399 | 2025-06-03 00:31:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3124b4e0-d43e-3573-827d-c938705864e2 | -6.2508 | -43.3783 | 2025-06-03 00:31:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d380f4e0-e536-3428-83bf-5826ce8e6d74 | -7.2138 | -45.350899 | 2025-06-03 00:31:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8cb7fb9c-5e9b-37e2-999f-cba51f03029a | -9.1894 | -49.692402 | 2025-06-03 00:31:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75953bf2-0243-3bc7-a9ec-447e23760317 | -7.5543 | -43.303699 | 2025-06-03 00:31:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c1c483bc-2cf0-3c69-837c-80e29082633c | -11.5749 | -47.4524 | 2025-06-03 00:31:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d771c32b-a09d-3913-aaee-b0eadf1bc1a7 | -13.427 | -43.751301 | 2025-06-03 00:31:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cd5a2f56-bcba-3cba-8067-688485c70c96 | -3.0414 | -49.425598 | 2025-06-03 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aef0a957-e20c-3ee9-9759-afbf51c98260 | -12.3784 | -45.915501 | 2025-06-03 00:31:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
