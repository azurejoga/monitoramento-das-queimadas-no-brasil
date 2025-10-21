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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82261905-0c09-336f-94a1-66c3055bb57e | -17.6852 | -52.2398 | 2025-10-21 01:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| c0abfc76-2633-35d6-9d9c-158ad9f7c798 | -3.3256 | -50.7432 | 2025-10-21 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| ce354bd1-a8dc-310e-8b1e-02849e1621db | -3.9739 | -50.3644 | 2025-10-21 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 1526ba68-51f4-3d87-ac36-c1164fe951a8 | -9.0037 | -65.904 | 2025-10-21 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 6926d6ee-57ad-346b-ac8a-39d5458dabbc | -4.6649 | -46.4084 | 2025-10-21 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 1d11acf1-4fce-3d6c-b1d7-89b905fd4472 | -9.0222 | -65.922 | 2025-10-21 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| e8fc1bcc-d514-39f1-b592-0388bb3ec448 | -9.0036 | -65.9412 | 2025-10-21 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 40111667-d792-3f11-b110-bd52b6d347b6 | -3.4968 | -45.8195 | 2025-10-21 01:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 411.5 |
| 2ca185a6-ce88-3130-9de5-a0235ec65928 | 1.6936 | -55.7251 | 2025-10-21 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 533238b8-f73a-34af-bed4-e08e40c01874 | -4.4971 | -46.4618 | 2025-10-21 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 339bc671-a1a9-3f82-af9e-2313badec9d4 | -9.0221 | -65.9407 | 2025-10-21 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 1fb82a7f-0dff-3142-be4b-fdd64932c01f | -3.4783 | -45.8203 | 2025-10-21 01:00:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 5d1b72ad-82e5-35b1-8e22-161337f85e96 | -6.1932 | -42.5259 | 2025-10-21 01:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| c64a8234-581b-38d0-9a33-2321de59f6a1 | -3.5154 | -45.8187 | 2025-10-21 01:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 183.0 |
| 64efca62-6914-356d-9215-b6c28b854a86 | -4.6461 | -46.4316 | 2025-10-21 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 74.2 |
| aca95ab8-57c1-35af-b7a6-bfcd6b3d6a10 | -3.2321 | -46.7836 | 2025-10-21 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| a6467435-be77-3302-9c47-672494303eb2 | -4.6464 | -46.3873 | 2025-10-21 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a036a84e-c0e7-3279-941b-c286c156f3f4 | -4.4783 | -46.4849 | 2025-10-21 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| ccb29283-634b-38b1-8125-f4844da00b4a | -8.9851 | -65.9232 | 2025-10-21 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 36f4b98b-c50b-3a90-bff8-69206e3db53f | 1.7303 | -55.6851 | 2025-10-21 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 1f8410e7-ad73-3211-b0cb-c85311e02540 | -17.67848 | -52.23958 | 2025-10-21 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 25.7 |
| c709ad9d-b7cd-3fff-91f5-eddbe996f5e9 | -17.68096 | -52.25444 | 2025-10-21 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 3cda8ae1-14b5-3924-8d23-61da945a1791 | -16.53412 | -53.72398 | 2025-10-21 01:09:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1845c255-2749-3e8a-925a-7a86a1bae5e8 | -17.69213 | -52.25272 | 2025-10-21 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7fbb9ed1-92c7-3d82-b921-72e7f9f331cf | -17.68343 | -52.26933 | 2025-10-21 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 42.1 |
| a8ec19b2-f3b8-386c-befe-466c9c51539f | -17.68962 | -52.23756 | 2025-10-21 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f0658756-0bb1-33fe-8043-dd37af91fb8e | -17.44057 | -55.03489 | 2025-10-21 01:09:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| b599ac05-6355-3d56-b537-da63b7fcb943 | -19.09636 | -57.54125 | 2025-10-21 01:09:00 | TERRA_M-M | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 83ca7dab-4c68-3210-ad06-097c104315de | -18.16881 | -52.97415 | 2025-10-21 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 85530212-8297-35e0-be97-c9d60252474f | -18.18972 | -52.97034 | 2025-10-21 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 67a2d339-c433-36bb-9f90-b7f79497f3cc | -18.59668 | -51.72565 | 2025-10-21 01:09:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 824d26c1-f391-3acb-a062-7c28fdfd54d5 | -19.09509 | -57.53183 | 2025-10-21 01:09:00 | TERRA_M-M | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| fe3ab9ee-7eed-3549-be22-815b07ad8f82 | -18.19185 | -52.98359 | 2025-10-21 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 19cfd129-90a5-3cb5-878d-8f4187fcf552 | -17.42344 | -55.04838 | 2025-10-21 01:09:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 27.3 |
| df9a9120-6972-3017-8266-72329bdd9eea | -18.59393 | -51.70951 | 2025-10-21 01:09:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 80d818c3-efe0-3575-bbcf-5f01445adbdb | -4.4971 | -46.4618 | 2025-10-21 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 321.4 |
| 83e356b7-f272-3fb8-8d7a-69fc54a15273 | -3.3441 | -50.7426 | 2025-10-21 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 20734ec6-a2c7-3907-bc54-1a2340196c5e | -4.6461 | -46.4316 | 2025-10-21 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 6cdc56dd-40f1-3b7b-8f78-24377737f03c | -9.0036 | -65.9412 | 2025-10-21 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 47f08d1f-5e4a-319b-bd26-aaee3ce255c5 | -9.0036 | -65.9226 | 2025-10-21 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 227.7 |
| ce9482a9-7e1b-36dd-befc-9ce1787339d6 | -4.4785 | -46.4628 | 2025-10-21 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 10ecbb36-3384-31eb-9e15-f5af2e9ff431 | -6.1932 | -42.5259 | 2025-10-21 01:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| f1fc78c1-09ed-3a2e-9230-8870a56ad95c | 1.7302 | -55.7049 | 2025-10-21 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 8e6a28c6-d526-3365-8795-975a6e51c2a9 | 1.7303 | -55.6851 | 2025-10-21 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 4cb21f85-71ee-3af0-a782-a6421df462cf | -4.3879 | -43.3129 | 2025-10-21 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 8b6176da-18db-39ca-a78e-6b6b56293e2b | -4.6649 | -46.4084 | 2025-10-21 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 80.9 |
| dfecc728-0f13-3338-8906-db0fca93cd42 | -3.497 | -45.7971 | 2025-10-21 01:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 106c0ab8-05f9-324e-b7be-03034e498339 | -3.8516 | -48.95 | 2025-10-21 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| bd9b8815-e269-380d-a3f9-781c1df62cbd | -4.6463 | -46.4095 | 2025-10-21 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 04eaff69-db82-3db1-943d-8e1300b9590f | 1.7119 | -55.7248 | 2025-10-21 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 0cb8eee0-95a8-311c-9ef7-7946d62f0721 | -3.5153 | -45.8411 | 2025-10-21 01:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 4cd7a9ac-518e-3cd1-81dc-1c11f38ccea2 | -3.9739 | -50.3644 | 2025-10-21 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 69dcc88b-681b-3965-b84b-c4a040cf6b9f | 1.7486 | -55.6849 | 2025-10-21 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 557a6a98-df1a-356f-9348-a01f84d0ffec | -4.4969 | -46.4839 | 2025-10-21 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 308.3 |
| 27db5de9-210f-30ff-8de7-f1144364c65c | 1.7119 | -55.7051 | 2025-10-21 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| a02dd9dc-53a4-3036-ae41-6f2a2d4e85bb | -3.4968 | -45.8195 | 2025-10-21 01:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 319.9 |
| a29637f5-b917-3d61-8597-701ecdd4af90 | -4.5157 | -46.4608 | 2025-10-21 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 73ee4f3f-dc56-3bc5-8ac0-3676afd34d8c | -3.4967 | -45.8418 | 2025-10-21 01:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 185.9 |
| 79d8f1ea-8645-3028-bdd2-19d1e2ff8a6e | -9.0037 | -65.904 | 2025-10-21 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 1212c72b-04ae-3a90-9985-1ab600f7c106 | -4.5155 | -46.483 | 2025-10-21 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 48.6 |
| cc071db4-9558-30b8-b062-81be5f34044d | -4.4783 | -46.4849 | 2025-10-21 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 106.2 |
| d1d098f8-4d81-3f1e-81e9-7f70d2d4805c | -6.1935 | -42.5022 | 2025-10-21 01:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 6f2ebcfc-7a03-3ff4-af61-4d6d15449111 | -8.9851 | -65.9232 | 2025-10-21 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| be4cdf67-3f49-3beb-b840-4e785158ac85 | -3.9923 | -50.3636 | 2025-10-21 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 3276f7ca-ec02-3b90-a727-84e9927ec877 | -3.5154 | -45.8187 | 2025-10-21 01:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 192.2 |
| f05d06e0-7bba-317e-ad13-2779275ac1c0 | -3.2321 | -46.7836 | 2025-10-21 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 6eb6efa4-5941-3606-aee0-247315a3a7ed | -9.0221 | -65.9407 | 2025-10-21 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a1c17df3-228b-3f16-a324-0c92ec4e0fd9 | -3.8515 | -48.9714 | 2025-10-21 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 51279797-45b5-3b6c-ab19-20dcd48efd6f | -9.0222 | -65.922 | 2025-10-21 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| e7bb353d-485d-3fc0-84be-4c2296c786c0 | -9.01304 | -65.91923 | 2025-10-21 01:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 174.0 |
| 57c5928b-ffbf-345b-b902-6b72cdf4d32f | -9.11316 | -65.35467 | 2025-10-21 01:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| cc23943b-3463-3749-a69a-7b29a17133f3 | -10.08197 | -65.16653 | 2025-10-21 01:11:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 5b737eb5-0dae-351d-b252-1e32aeb4c7ca | -9.55257 | -57.35725 | 2025-10-21 01:11:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5802cc73-e4ae-361e-9944-1e15c9fe4265 | -8.63996 | -63.05085 | 2025-10-21 01:11:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 899ba713-c055-33d5-b5eb-e05bbdcc7a2f | -9.0024 | -65.94254 | 2025-10-21 01:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| c32b7f87-1e64-3c9b-9217-68f0cd33270c | -9.03924 | -65.7017 | 2025-10-21 01:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 192ec2aa-0b11-3ca7-a3d7-1afadaf674cc | -15.90115 | -59.60336 | 2025-10-21 01:11:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2bee24c0-ed43-37fc-b234-dd6439d228ee | -15.90246 | -59.61351 | 2025-10-21 01:11:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 279fe5cd-1aa4-31cc-be94-1274ec910a04 | -8.9865 | -65.92265 | 2025-10-21 01:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| df901b95-c2a0-31fc-8a2d-e7f425e6d190 | -8.99977 | -65.92096 | 2025-10-21 01:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 202.7 |
| 5ceceacb-7237-3b05-82e5-32c7dff8820f | -11.90677 | -54.82642 | 2025-10-21 01:11:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| b41716ce-5510-374b-8134-70c69c5f6a30 | -9.11554 | -65.37412 | 2025-10-21 01:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 9e8b2acc-cc37-31e2-8cf4-432fe161ba6a | -9.64865 | -65.25154 | 2025-10-21 01:11:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| aea000ad-bce1-3343-bd51-1aca17805f05 | -14.74909 | -54.11353 | 2025-10-21 01:11:00 | TERRA_M-M | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 87b0e939-7875-3f4f-b9a2-2639af15e0fb | -9.05022 | -65.69367 | 2025-10-21 01:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| a0a1e060-c24c-399a-9f01-e30064993cbb | -9.7178 | -67.4824 | 2025-10-21 01:11:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 2263e89a-492a-3c02-aa11-f3fe3f49447d | -9.18552 | -61.37835 | 2025-10-21 01:11:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a143b893-2812-37a8-988f-0f595dd3753d | -9.18689 | -61.38865 | 2025-10-21 01:11:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 9a7a735c-ee64-3f95-85e7-232821a48fad | -9.01569 | -65.94086 | 2025-10-21 01:11:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 9b4f6ff4-35d9-3158-ad69-191f3f4b7954 | -3.32136 | -50.21982 | 2025-10-21 01:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 645a6729-b3cc-3675-bec8-cf1c82c5db12 | -3.3339 | -50.74495 | 2025-10-21 01:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 9fe0b112-ced8-367c-adb7-ebdc63b1eb96 | -2.81583 | -54.38639 | 2025-10-21 01:13:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 6df48f65-6d12-35bf-9d99-2469249ffce8 | -3.34375 | -50.74859 | 2025-10-21 01:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| ab621c4a-3eb0-3510-96d7-3d837deb616e | -3.32415 | -50.21208 | 2025-10-21 01:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| f9dab916-f6a1-368f-988f-7143b27bcdc7 | -3.31898 | -53.35271 | 2025-10-21 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 53c8c8f7-72c7-3f04-8254-ae54d47a50dd | -3.33027 | -50.25067 | 2025-10-21 01:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| c344ecda-2f78-316c-b3b4-fa9641dca75e | -3.58163 | -55.4556 | 2025-10-21 01:13:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1e9c2e97-92f1-3e00-bdd1-16e1876c7e64 | -8.94668 | -65.92766 | 2025-10-21 01:13:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b2fe8b66-e001-3eb5-8062-3339ca7b8e39 | -3.57953 | -55.44083 | 2025-10-21 01:13:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4934d5e3-878e-3852-a556-9ba931c26659 | -8.93722 | -65.9342 | 2025-10-21 01:13:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |


[Clique aqui para ver as próximas entradas](README4.md)
