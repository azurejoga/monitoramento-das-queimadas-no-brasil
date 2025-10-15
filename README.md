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
| 756c3bd5-474f-317b-bfb3-fce6550a2f23 | -7.9442 | -44.115 | 2025-10-15 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 9e5c59b9-053b-3e4d-a997-aa894d53e331 | -2.9435 | -49.3443 | 2025-10-15 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| d90d00dc-d728-3ade-a8c9-03e1836891ed | -4.2797 | -48.5887 | 2025-10-15 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 02fc0b42-27c1-3290-ac78-bac848832cd0 | -4.8916 | -43.4446 | 2025-10-15 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 216.9 |
| 3ef39951-e8ff-3511-9de8-4629f5201575 | -8.2927 | -43.4258 | 2025-10-15 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| 5ac75c81-c379-381e-b139-c0fd39a1bbce | -7.9439 | -44.1381 | 2025-10-15 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 192.2 |
| a7009c1b-42f0-394e-a357-781c1ff2f035 | -7.9628 | -44.1362 | 2025-10-15 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| aefb7cdd-2216-3abc-87dd-2775606bcde0 | -5.409 | -44.2185 | 2025-10-15 00:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| c887c5dc-ea0a-301d-8980-eda008f51528 | -2.246 | -47.8838 | 2025-10-15 00:00:00 | GOES-19 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| ab06fb7f-b394-3c93-8855-203c80d2c1bc | -5.4278 | -44.2172 | 2025-10-15 00:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 346.2 |
| 11bde21d-6f79-38be-8a00-1d0721c815ca | -4.6509 | -43.1337 | 2025-10-15 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 293.0 |
| 7aa3258c-e969-3fb0-9a4f-39a939b0a656 | -4.9102 | -43.4666 | 2025-10-15 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 86cfa99b-4ad7-31b4-bf7c-f873da7c044d | -4.9104 | -43.4434 | 2025-10-15 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| d9f336d4-43a2-3bd0-9519-abd90d415756 | -2.2461 | -47.8622 | 2025-10-15 00:00:00 | GOES-19 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| d58e543f-925f-3abf-bb70-24c23da696b8 | -8.7404 | -43.8659 | 2025-10-15 00:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| a567cd72-51ab-35b4-9930-258f9154993f | -4.6696 | -43.1326 | 2025-10-15 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 206.4 |
| 844cdf34-dc51-3fc5-8d24-7c5d738a8407 | -17.615 | -46.684 | 2025-10-15 00:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 7c5ff4b7-a84c-3b07-89c0-08bd4fc60d30 | -4.8915 | -43.4678 | 2025-10-15 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 360.3 |
| d25382b6-a298-34e6-9cdf-702fd5cba715 | -5.428 | -44.1942 | 2025-10-15 00:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 01c3cc15-1603-3a47-b16f-412e18eaf3d8 | -8.2734 | -43.4514 | 2025-10-15 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 63165bb4-059d-3e30-898b-38db0b03b8db | -1.4925 | -55.4508 | 2025-10-15 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 09f0f5aa-2f3f-3980-a8f2-d42d0873e435 | -4.2608 | -45.5821 | 2025-10-15 00:00:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 39eb244b-7ecb-38e9-86ed-3fe73e5eb40f | -5.4465 | -44.2159 | 2025-10-15 00:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| c9d3c6a2-3591-3a78-bccb-ca8ed85b4230 | -4.6698 | -43.1092 | 2025-10-15 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 96f55725-e4bc-346c-96de-765e16b33200 | -8.2924 | -43.4493 | 2025-10-15 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| f906d59f-f527-3116-8a97-03786ddcb3c8 | -8.7218 | -43.8447 | 2025-10-15 00:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 6420018e-4760-3f97-9b65-f54e3ea4a2a6 | -4.6511 | -43.1104 | 2025-10-15 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 202.2 |
| 6550e470-8a40-3988-8fac-56523c78652c | -4.6694 | -43.1559 | 2025-10-15 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| eb04f82a-7679-360a-89cf-77906ed465e5 | -8.7215 | -43.868 | 2025-10-15 00:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 04cec124-2687-3d03-892d-6f1f211ce962 | -3.0981 | -47.7286 | 2025-10-15 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 5c085650-28d9-34b8-b23a-99b4288dba94 | -5.8802 | -43.8613 | 2025-10-15 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 29bef0d4-b234-30f3-ad50-7e7ddfb1c186 | -8.7408 | -43.8425 | 2025-10-15 00:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 62e508da-c5dc-3862-8985-2e6890f41be6 | -5.4276 | -44.2402 | 2025-10-15 00:00:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 176.9 |
| c5712e8f-7dbb-321f-b9b9-01f8c68e2dc5 | -1.4926 | -55.431 | 2025-10-15 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 824cc311-a210-367c-baa1-923f90e6fde0 | -8.2738 | -43.4279 | 2025-10-15 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.2 |
| b8075fbd-4d2a-38af-9296-5d624516b55e | -11.0626 | -51.009 | 2025-10-15 00:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| deaac73a-9787-32df-a2d7-db1c2dbcb286 | -4.6507 | -43.1571 | 2025-10-15 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| efb67289-72d0-37e6-9762-a64718cae625 | -5.8614 | -43.8627 | 2025-10-15 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 38238c7f-c45e-3176-9db7-54573b599eae | -10.0497 | -43.821 | 2025-10-15 00:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 63.4 |
| cbf87908-ceb5-3e66-8889-91ad09abe6b2 | -5.4465 | -44.2159 | 2025-10-15 00:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 21370839-cfb3-39d3-b750-656a49b2e8b0 | -8.7218 | -43.8447 | 2025-10-15 00:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 49.9 |
| f00f21f0-0951-362d-8edc-aec555cfc432 | -11.0816 | -51.007 | 2025-10-15 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 69c604cb-0878-3c5d-84d2-0351b5651579 | -8.2738 | -43.4279 | 2025-10-15 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.2 |
| 8e9323cf-7ae6-3dbe-9829-e1e8ddad6e40 | -10.0539 | -48.7106 | 2025-10-15 00:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 61e973a0-528c-37e8-96cd-d96f325334cc | -11.6419 | -47.8428 | 2025-10-15 00:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 82c6694d-96b6-38a1-8b30-194c90738f37 | -4.6509 | -43.1337 | 2025-10-15 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 288.9 |
| 24e5ed39-a9bc-3a09-93c2-955317e54989 | -11.0626 | -51.009 | 2025-10-15 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 125.4 |
| f0fe7c53-6201-37cf-a1ab-44191e63c378 | -4.6511 | -43.1104 | 2025-10-15 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 172.2 |
| d43537bf-5d75-32bb-8d51-fc57f3ec8f3f | -8.2734 | -43.4514 | 2025-10-15 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 47.9 |
| bbcde183-78b9-3e4d-baa3-9b3b53900563 | -2.246 | -47.8838 | 2025-10-15 00:10:00 | GOES-19 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 1494d89d-bc01-3ef8-b6ab-7fd1af63083a | -8.2924 | -43.4493 | 2025-10-15 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 51.8 |
| bcdfec4d-95fb-3a5e-be54-63ab7f82bcd2 | -5.4276 | -44.2402 | 2025-10-15 00:10:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| d2eb58aa-9d35-3d5c-b442-6227cf02a0ae | -7.9628 | -44.1362 | 2025-10-15 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 9d8fbcb1-c199-3e10-9560-210abfb44d9d | -4.6698 | -43.1092 | 2025-10-15 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 2f84af26-3647-3818-9ebd-2b22c5b10f5b | -5.4278 | -44.2172 | 2025-10-15 00:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 145.2 |
| a714fd16-f033-3db1-9c0a-976ec25432b7 | -4.9104 | -43.4434 | 2025-10-15 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 94e37b1a-7743-34ed-8b45-5afbd0f68d37 | -8.2927 | -43.4258 | 2025-10-15 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.9 |
| 70226e80-2a89-3cae-ab87-8f1fa154b4a8 | -5.8614 | -43.8627 | 2025-10-15 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 03ba459a-5122-32f1-9848-261960d0bf1e | -1.4925 | -55.4508 | 2025-10-15 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d93bef8c-933f-3ba4-a87e-986240ce841d | -1.4926 | -55.431 | 2025-10-15 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 0e5af5b5-0b2a-339c-8b7a-500642613ecd | -4.8916 | -43.4446 | 2025-10-15 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 171.7 |
| cc6cd43f-f5a6-3734-ba78-8da95b66e2fe | -7.9439 | -44.1381 | 2025-10-15 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 98188a69-db7a-3212-ac3a-cf0ca1f4de13 | -5.8802 | -43.8613 | 2025-10-15 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 5616280b-2285-394f-93e5-27fa1b515148 | -4.9102 | -43.4666 | 2025-10-15 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 24ebb92d-764a-3340-8158-d5cbc867a0fa | -4.8915 | -43.4678 | 2025-10-15 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 246.8 |
| 9225ec3c-0b78-3cd9-b139-e95c651e36ce | -3.0796 | -47.7293 | 2025-10-15 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| a8cca918-42e1-33a1-861e-d001853d8e8d | -5.409 | -44.2185 | 2025-10-15 00:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 6a66aaec-15ce-3aac-8b86-6095c5670695 | -3.0981 | -47.7286 | 2025-10-15 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 3b84a153-a055-3360-99bc-4a9b6a59e155 | -8.7215 | -43.868 | 2025-10-15 00:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 3bc24ee8-eb6b-36f3-9f52-b242ccdd6fe1 | -7.9442 | -44.115 | 2025-10-15 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| c2f5d193-60dd-3eb7-925c-5fd09cd672ab | -4.6696 | -43.1326 | 2025-10-15 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 214.2 |
| 40508a11-5c25-3c3a-8742-b466e0dc5d94 | -8.7404 | -43.8659 | 2025-10-15 00:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 539a8d82-de90-3472-b642-9df803da7247 | -4.2797 | -48.5887 | 2025-10-15 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| f0568c22-2685-3862-bdbf-34ee529d0339 | -17.615 | -46.684 | 2025-10-15 00:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 94.3 |
| b303ff7d-08e3-3fa7-91eb-d92686777d53 | -7.9628 | -44.1362 | 2025-10-15 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| c4d4125e-3a70-3fd1-aed6-7f30ea7cb587 | -5.0143 | -44.4969 | 2025-10-15 00:20:00 | GOES-19 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 153b8a69-f343-3733-b73f-2505dade2aa6 | -5.1543 | -45.7107 | 2025-10-15 00:20:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 467880eb-fb3e-349d-94bf-013f15daef78 | -5.3264 | -42.9242 | 2025-10-15 00:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 6b55d9eb-b94e-3447-8423-ccc013aceee3 | -8.7215 | -43.868 | 2025-10-15 00:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 1b8763df-70ab-3fb6-9603-23c23f2a4221 | -4.8916 | -43.4446 | 2025-10-15 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 84600b41-06a4-302a-9732-f8e9d5131e49 | -4.6511 | -43.1104 | 2025-10-15 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 47901ad9-f6d3-3662-ada1-5fc8cd821b65 | -4.8915 | -43.4678 | 2025-10-15 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 287.9 |
| 7f2134d5-ca71-3491-a493-603cf338b144 | -5.3077 | -42.9256 | 2025-10-15 00:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 2baa4245-538b-3e33-9e0f-3e3bf93e97ca | -7.9439 | -44.1381 | 2025-10-15 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 4a02158e-64fd-34b7-9aeb-3089745fc5dd | -7.9442 | -44.115 | 2025-10-15 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 1a56561d-c766-3fc9-8d58-9b95bc5256bd | -4.6696 | -43.1326 | 2025-10-15 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 6c1b29fc-5fa6-3af2-a5a5-d1a30fa1764a | -4.6509 | -43.1337 | 2025-10-15 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 231.2 |
| 9e09269d-b758-37c5-a7a3-62b508a84325 | -5.8614 | -43.8627 | 2025-10-15 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 922eb955-bb86-3c9b-bfdd-df02f957807e | -3.6674 | -45.2285 | 2025-10-15 00:20:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 7c9785d9-fc5f-3db2-9bb9-cc3b701b45ca | -1.4925 | -55.4508 | 2025-10-15 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 39f49c4d-c5fc-34c3-9253-a78f61917154 | -5.1545 | -45.6882 | 2025-10-15 00:20:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 153.1 |
| c4b56865-7b32-3b8c-861f-89ca2ad310b7 | -3.0796 | -47.7293 | 2025-10-15 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 47c9c582-a14a-3c0e-b7a6-b14fce5e2d43 | -4.6698 | -43.1092 | 2025-10-15 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 184df1b4-1b01-35fd-a784-e0b2fb81c373 | -11.0626 | -51.009 | 2025-10-15 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 788d93af-ecbf-3fc3-a4cb-79049911fcf8 | -4.9102 | -43.4666 | 2025-10-15 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 252.8 |
| d9722274-5c34-3771-a6a6-e786b356351a | -4.9104 | -43.4434 | 2025-10-15 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 4a734390-24e5-39d4-852d-4002a26c7478 | -5.1545 | -45.6882 | 2025-10-15 00:30:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| cfff1d9e-d4b7-3d54-91de-e54ec1d083e3 | -3.6675 | -45.2059 | 2025-10-15 00:30:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 82.1 |
| c2bc59d5-8df2-35c0-8213-1ebdf84c6906 | -7.9439 | -44.1381 | 2025-10-15 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| c388b064-1a92-3b27-a0f3-de45eaa17e16 | -8.7218 | -43.8447 | 2025-10-15 00:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |


[Clique aqui para ver as próximas entradas](README2.md)
