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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dc73c58-c400-3f33-900e-51293ceba996 | -5.18635 | -45.29259 | 2024-10-20 00:24:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 64e6f1e8-c110-3fc6-9090-3a7d7e54ef85 | -5.13495 | -46.11444 | 2024-10-20 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 288b25b5-8d9b-3b4a-ab98-2f83ba1abe36 | -5.12969 | -46.16647 | 2024-10-20 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 461933f3-49aa-365c-8083-8b9e07ff3461 | -5.11775 | -46.16787 | 2024-10-20 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| bef6a756-302c-3cd2-8f51-dcd8aecfa99e | -5.10151 | -46.13599 | 2024-10-20 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 28.5 |
| e8c2706b-2229-3e3d-9d0a-34d190500544 | -5.09503 | -46.14339 | 2024-10-20 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 15c6127d-b0c0-3a67-82d5-efb586111035 | -5.09276 | -46.12675 | 2024-10-20 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 8de1ffd4-1f5b-38e7-a93b-a47bb97932c9 | -5.01388 | -50.83559 | 2024-10-20 00:24:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 5ec2208a-97f1-3451-ad74-94abe53988fe | -4.96846 | -45.91088 | 2024-10-20 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 69ce0747-e9fe-3fe1-a015-36436cb81225 | -4.9151 | -45.84227 | 2024-10-20 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 27.4 |
| efa0a16c-1cba-36f8-a088-a1d4acdfb46d | -4.91305 | -45.82687 | 2024-10-20 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 61a034a0-b6b1-3533-9736-070f9db81f12 | -4.90361 | -45.84438 | 2024-10-20 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 27.1 |
| bd690f96-9f8a-3d40-b7bc-644f085d0768 | -4.9015 | -45.82837 | 2024-10-20 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 93.3 |
| adfc1ea0-a9bf-37e8-8a42-6541bf95748f | -4.8995 | -45.81325 | 2024-10-20 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 496a2c3c-79c0-3282-bc90-467c7fe965a5 | -4.89896 | -44.63408 | 2024-10-20 00:24:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 46ae737c-46b0-3dca-8845-8186ed2e6fad | -4.88993 | -45.82975 | 2024-10-20 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| f429e701-3f38-352c-bca3-aefd2d68bdde | -4.871 | -45.86518 | 2024-10-20 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 74fbea12-69e4-36e3-a658-463806d13434 | -4.8627 | -45.87243 | 2024-10-20 00:24:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 31.2 |
| e90ede71-b06f-3809-a05e-1888fea82e94 | -4.73907 | -45.21075 | 2024-10-20 00:24:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f32c776c-28ab-36dc-a58a-6cb10c506dcd | -4.70929 | -45.8508 | 2024-10-20 00:24:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 6e1c3f32-c9af-3f9f-92c4-8b915911a63e | -4.70725 | -45.83524 | 2024-10-20 00:24:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2b1b8631-d3d8-3870-80ae-cc1e39bf2368 | -4.69864 | -45.84297 | 2024-10-20 00:24:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 4609981c-774f-347e-ab5b-b64e6ac7e59d | -4.6978 | -45.8527 | 2024-10-20 00:24:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9664ab75-317b-35ee-9e3d-51107a34c2a7 | -4.69575 | -45.83691 | 2024-10-20 00:24:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 95ce62c9-ed1d-372d-869a-80a466f64d13 | -4.60486 | -47.54798 | 2024-10-20 00:24:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 4862a205-76fa-3a8c-8341-6e2d4d1ca338 | -4.55081 | -45.77478 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 6088befd-94fc-38e8-809a-893af68fd136 | -4.54871 | -45.75924 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 2584dcdb-c428-355c-bc81-3c5e75ee3c03 | -4.49563 | -44.7655 | 2024-10-20 00:24:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| c438d09f-1f33-3f6d-a971-0032a8cec935 | -4.49389 | -44.75261 | 2024-10-20 00:24:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 68700766-0fdb-36bc-a0d7-1304caedad68 | -4.49255 | -44.58544 | 2024-10-20 00:24:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0b848d8d-da1f-37fd-9daa-7c35b63f17c0 | -4.48508 | -44.76694 | 2024-10-20 00:24:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| dcfb5a42-1d89-34b8-8653-ae690de3553c | -4.48336 | -44.75409 | 2024-10-20 00:24:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 368377c7-1304-3907-9858-2616b1198932 | -4.48273 | -50.46796 | 2024-10-20 00:24:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| d644c727-2216-3c37-8a61-ebac223a12b1 | -4.4773 | -50.47367 | 2024-10-20 00:24:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 43d53f8b-8261-33b4-bc0b-8fb3c1b4b5c2 | -4.47646 | -47.75312 | 2024-10-20 00:24:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e3f631ab-4982-31d9-938a-172763bb8f90 | -4.47343 | -47.73071 | 2024-10-20 00:24:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 626251f9-b6b1-3175-ac20-544ac1317ad1 | -4.47252 | -50.43784 | 2024-10-20 00:24:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| d1432e61-e78f-3c05-af77-23eccb768f55 | -4.47153 | -47.74838 | 2024-10-20 00:24:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| abd688b2-8292-3e5f-bc61-c87ad2c7b51d | -4.46869 | -47.72601 | 2024-10-20 00:24:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| feede672-98a0-3a9e-b9b0-6f2f529f60cb | -4.38789 | -45.8401 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 59738127-51a6-3d0e-8724-266ff8c897c7 | -4.37645 | -45.84179 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 27.5 |
| edfc1e73-f71c-3bdb-a6c4-9b5befe158a7 | -4.3479 | -45.63019 | 2024-10-20 00:24:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| e49b1871-c140-32be-8f4e-f1426e93c36c | -4.34646 | -48.57512 | 2024-10-20 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 446416cc-2f15-370a-bc20-73338e75b4a6 | -4.34357 | -48.58233 | 2024-10-20 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| f263d013-a429-30bd-979f-d4e6015ee7c8 | -4.34008 | -48.55693 | 2024-10-20 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| ef92cb14-b371-37a2-a0c5-056cc8f962fe | -4.33864 | -48.62749 | 2024-10-20 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 54c0a88f-a695-334c-a4b5-22bef93b8e63 | -4.33668 | -45.63198 | 2024-10-20 00:24:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1966c1c2-07a1-34a2-8ae1-5a7c3058d7dd | -4.33609 | -48.63446 | 2024-10-20 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| befbbe80-f006-3345-8c68-8a4e9dea7724 | -4.33262 | -48.60902 | 2024-10-20 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 57c2a057-dae4-3ec2-aa34-6eba8e7c02d1 | -4.32426 | -48.62946 | 2024-10-20 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| e43d6c94-4a29-3447-97b5-5dbe67aa1138 | -4.28974 | -44.52398 | 2024-10-20 00:24:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2faa9f4e-e1c8-36e9-8105-2f33ddc35736 | -4.25503 | -50.98064 | 2024-10-20 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 4a212173-c7a6-3fe8-b9b1-45e3937ce033 | -4.19608 | -46.63897 | 2024-10-20 00:24:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 911d5455-f869-3cf3-a2d7-5b82baa52223 | -4.19367 | -46.62091 | 2024-10-20 00:24:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 494201a6-a700-36c4-bf5b-5b1f599a21b6 | -4.19272 | -45.7555 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2bea29f9-ced0-3d95-ba34-d0fbb3cfa2c2 | -4.19067 | -45.74045 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 35.1 |
| c6a4f9a9-d19e-3504-9d5a-a39451da506f | -4.1802 | -45.83436 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0120f283-d178-304b-90d8-934aafdb21c6 | -4.17817 | -45.81919 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 97803132-064a-3427-b94d-948196f562f5 | -4.17409 | -45.78877 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 0512e7fe-3b98-380c-b520-a4c04bcbaa5d | -4.12321 | -46.87367 | 2024-10-20 00:24:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| c0d0bae5-ecd7-345b-84b3-c74ff3c022ce | -4.09708 | -44.23352 | 2024-10-20 00:24:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 0ee83600-8d12-36cd-a825-758aa0c4f26c | -4.09547 | -44.22191 | 2024-10-20 00:24:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 70a68891-00df-3acc-acda-75eac88ba098 | -4.05616 | -44.31084 | 2024-10-20 00:24:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9440142a-b61a-3298-9a53-6880faea27eb | -4.04129 | -46.94715 | 2024-10-20 00:24:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 63e74de8-0756-3121-9f25-a81adf2e57b3 | -4.01064 | -46.02579 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 83ec4c59-8b4f-3b53-a529-157e1ebce6f7 | -3.9679 | -47.9479 | 2024-10-20 00:24:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| d9d7e071-74b6-3f88-a7d1-d64134823dfc | -3.96523 | -47.96555 | 2024-10-20 00:24:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9e542d46-1f67-38b1-9856-b78dbb8c56ad | -3.96235 | -47.94327 | 2024-10-20 00:24:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 170b7197-1e4e-3ce1-8465-e29ef8d1f0e2 | -3.96055 | -45.39985 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8cd1a880-3057-3741-8564-ce14665b7626 | -3.91658 | -45.75068 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 498310f8-3b0b-3e8c-a341-735fe6dcd24b | -3.90863 | -49.9868 | 2024-10-20 00:24:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 4662a83f-16ab-33d9-920b-0719742c0258 | -3.90696 | -48.33156 | 2024-10-20 00:24:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| ffccc865-6d86-3290-9f3f-15e964de4639 | -3.89966 | -49.99327 | 2024-10-20 00:24:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| d1241568-f0cb-37d5-8454-11acece11e22 | -3.89274 | -49.98887 | 2024-10-20 00:24:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 71df2f7d-2252-3193-8846-268dac9f6622 | -3.86999 | -45.83311 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 6b682591-633d-39cc-a0a7-270965055c47 | -3.86945 | -45.82365 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 0ab32313-1fde-3c1b-af26-1fb86a03d965 | -3.86801 | -45.81807 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| fb854186-b3b2-3058-8767-d1a3d07f227f | -3.85863 | -45.83463 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| af7a7923-39c7-3982-893d-c74ee42c4bab | -3.8581 | -45.82517 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 7b9a1d4e-b4e0-313b-a891-6214f85e71f9 | -3.85667 | -45.81963 | 2024-10-20 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3eff62d9-5891-3c1f-94b0-ae966165a444 | -3.84039 | -48.88987 | 2024-10-20 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| dbe102aa-edb9-35d4-bb16-b319f953f31b | -3.83884 | -48.89643 | 2024-10-20 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 7ec6252a-d81b-3f34-bb2f-75f03e982beb | -3.83612 | -48.9711 | 2024-10-20 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| f6040e99-7cb2-3055-ae3e-39411f74ad50 | -3.83516 | -48.97766 | 2024-10-20 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| c2e897d8-e32c-3b1d-8ff4-0e179ca975cf | -3.83516 | -48.86985 | 2024-10-20 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 08515be9-ec6a-3a60-8b48-e689e76f4932 | -3.83267 | -48.94454 | 2024-10-20 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 16a46b5f-2c71-3712-94ab-2478228b4120 | -3.8315 | -48.951 | 2024-10-20 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 901a03d3-e40e-3554-bb65-58dbda6fdbb8 | -3.83022 | -45.87511 | 2024-10-20 00:24:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 649cd716-451a-3cae-8050-7cd81e4fe1f4 | -3.82816 | -45.85992 | 2024-10-20 00:24:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c10c226d-06d9-3c1d-bcdb-a83c4ac7a3a3 | -3.8258 | -48.89162 | 2024-10-20 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 17a040ea-0907-3c26-9123-6d8dc1017956 | -3.82235 | -48.86513 | 2024-10-20 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 6a20649a-cdc6-3855-b5b5-2ac13fda2f27 | -3.8206 | -48.8717 | 2024-10-20 00:24:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| dbca4bc1-e872-3db2-b14b-58b7c28f87ae | -3.80073 | -46.07375 | 2024-10-20 00:24:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8094ba0e-cbb6-3e22-8919-5d1aaf1f552b | -3.79749 | -46.06795 | 2024-10-20 00:24:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b28b8f12-d582-3168-b2b4-ebf1b87e7187 | -3.77932 | -45.91933 | 2024-10-20 00:24:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 85d0404c-c8f5-3f48-b2d1-15d026a4bc83 | -3.77729 | -45.91338 | 2024-10-20 00:24:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 54.1 |
| a8cb38d2-1ff1-30ef-aaf6-ad5a9b690316 | -3.77721 | -45.90413 | 2024-10-20 00:24:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 3d264f3d-f6dd-36b6-ae0a-35b012b4d142 | -3.77704 | -44.43958 | 2024-10-20 00:24:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7d248cd0-a79b-31e9-a08f-a2c3ab99a3d8 | -3.77546 | -44.4277 | 2024-10-20 00:24:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e6a45622-600a-3dda-9c8b-41bcc8980a5b | -3.7753 | -45.89817 | 2024-10-20 00:24:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 24.1 |


[Clique aqui para ver as próximas entradas](README6.md)
