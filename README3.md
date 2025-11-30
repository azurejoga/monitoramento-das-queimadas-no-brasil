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
| d4bfdb5d-4635-3ddc-9338-30608d690cc1 | -11.0714 | -54.7664 | 2025-11-30 00:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 0ed4adcc-4d02-397f-8aba-5091e252d7b7 | -19.8473 | -57.7835 | 2025-11-30 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 230.6 |
| f5cb1e37-6a1d-3b61-8eda-0bfe0f7528b2 | -5.7309 | -39.8286 | 2025-11-30 00:20:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 238.8 |
| a7fbb914-cf2d-32dc-880f-4c797d0a3b43 | -2.532 | -45.5862 | 2025-11-30 00:20:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 596afecd-1647-385e-94bb-b4e43f00f52f | -19.8678 | -57.76 | 2025-11-30 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 2d5625a8-387c-377f-bd32-8a0ad1dc82fb | -3.5946 | -41.6577 | 2025-11-30 00:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 476259dc-e199-3d5b-b3bb-eb38db116164 | -5.7306 | -39.8534 | 2025-11-30 00:20:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 2bcd6358-b3d9-35e5-b23c-58c6a5e1ec52 | -12.0004 | -49.2683 | 2025-11-30 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 79b1e378-68af-35d9-be50-5f91ed7985a5 | -2.6507 | -48.5629 | 2025-11-30 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 725f110a-0739-3e3d-808c-abc369e6a197 | -2.4524 | -47.0726 | 2025-11-30 00:20:00 | GOES-19 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 250268f4-7bf7-3f61-b7d5-137009c2cb18 | -8.0321 | -43.1257 | 2025-11-30 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 218.5 |
| 8b2903fe-39e9-372a-953b-d28b5303ed3b | -5.7498 | -39.8269 | 2025-11-30 00:20:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 2082c749-4dc4-398b-a911-7fe004795798 | -7.5014 | -37.4242 | 2025-11-30 00:20:00 | GOES-19 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 02bcce75-d5e1-300e-8d56-45de6dae454b | -12.0195 | -49.2659 | 2025-11-30 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| e87911c4-8216-38c1-b04b-0500ad9a03ec | -2.6322 | -48.542 | 2025-11-30 00:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 9fb796dd-55e1-3d4e-bb2c-ebdb58f19adb | -8.0324 | -43.1022 | 2025-11-30 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.7 |
| 4a139eb3-e2df-335c-a90b-37edc5b2712c | -12.0195 | -49.2659 | 2025-11-30 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 875bdcce-8f3e-33a8-9e7b-750ce1fa8487 | -5.7309 | -39.8286 | 2025-11-30 00:30:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 280.0 |
| 80281ed2-b469-3399-9cf9-66c9472b8d05 | -2.4018 | -45.6349 | 2025-11-30 00:30:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 711648bd-e2da-36fc-8deb-46b1f56fe6a6 | -5.7306 | -39.8534 | 2025-11-30 00:30:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 9e38ba21-bf29-30f2-bffd-e49c9a4c4a98 | -5.7498 | -39.8269 | 2025-11-30 00:30:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 95.4 |
| bf7028af-e2ca-3115-8775-2b4c6223c70c | -5.712 | -39.8302 | 2025-11-30 00:30:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 43.0 |
| 42dc9d21-2058-36d2-b161-694756ec79ce | -2.6322 | -48.542 | 2025-11-30 00:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| fd6df716-a08b-3938-aca5-f7fbb3595828 | -7.5014 | -37.4242 | 2025-11-30 00:30:00 | GOES-19 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 9776140c-60a7-3fe3-9c9f-4e899d8e459f | -3.5946 | -41.6577 | 2025-11-30 00:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 71be7943-477d-3ef1-acb6-1757d6987ad7 | -8.0321 | -43.1257 | 2025-11-30 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 206.8 |
| 6d85964d-2769-39f5-b6e9-c92b2f4f02b1 | -5.7311 | -39.8037 | 2025-11-30 00:30:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 39.9 |
| 7987a2e1-c4b3-3724-9200-bb476e9dd817 | -2.6507 | -48.5629 | 2025-11-30 00:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 1e511bc9-2d63-37a3-8774-8a3e8ca30a9a | -12.0004 | -49.2683 | 2025-11-30 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| ee91f552-7459-3762-af43-216c00398ce3 | -8.051 | -43.1237 | 2025-11-30 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 250.8 |
| 25bd4a1d-615d-367d-9bd4-6b39eb7230d9 | -2.6507 | -48.5414 | 2025-11-30 00:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 458aa7ce-9478-3851-921b-fc21fade20e2 | -8.0507 | -43.1472 | 2025-11-30 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 5fd7461b-9758-35dd-bbe2-e049d7472659 | -11.0714 | -54.7664 | 2025-11-30 00:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 4bac7ed1-9328-37a2-b15f-a911968917cc | -8.0513 | -43.1001 | 2025-11-30 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 0c269c1c-3b13-376c-abca-0377a1c3a0bb | -8.1822 | -43.2034 | 2025-11-30 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 6127ebd4-2e03-379d-848f-39f3fe2670e1 | -2.4204 | -45.6343 | 2025-11-30 00:30:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 114.7 |
| b6aa6971-ad21-32af-af48-893c3e0a5e38 | -8.1633 | -43.2055 | 2025-11-30 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| f85e24c5-34c6-30f2-aba2-9eca0454e2f0 | -8.0513 | -43.1001 | 2025-11-30 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 06211e37-3add-362c-981a-2f5cf03bd60d | -7.5014 | -37.4242 | 2025-11-30 00:40:00 | GOES-19 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 67.5 |
| fb76856c-1d12-354e-bc7f-dc0c695e24f2 | -3.1506 | -44.3883 | 2025-11-30 00:40:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 52.9 |
| e6f4dc49-053f-348d-97ba-2a6efac08c52 | -5.7498 | -39.8269 | 2025-11-30 00:40:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 6b61ab61-cf59-36ce-bbc2-be34cb8855dc | -5.7311 | -39.8037 | 2025-11-30 00:40:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 54.1 |
| 7b5b3a37-fcd0-3184-9dfc-5abbe84fc059 | -2.4524 | -47.0726 | 2025-11-30 00:40:00 | GOES-19 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| b0afa3bc-7443-3b19-8070-947a2256a9ce | -11.0714 | -54.7664 | 2025-11-30 00:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| dc7609dd-6468-3a69-b466-25494526b44c | -23.6237 | -52.959 | 2025-11-30 00:40:00 | GOES-19 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 86.0 |
| c6fe0f17-f1e9-3f73-9d5c-75b94931f94c | -12.0195 | -49.2659 | 2025-11-30 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 156ca200-bb92-339b-ae98-e97b23eb128a | -3.132 | -44.3891 | 2025-11-30 00:40:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 0cae5942-1589-3991-9164-61222383ca72 | -2.6507 | -48.5629 | 2025-11-30 00:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 44aa0bae-350b-3404-9c07-baae13bf6363 | -8.1822 | -43.2034 | 2025-11-30 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| d572cc12-54bc-3244-b5f7-4d5354e75a81 | -3.2825 | -44.0852 | 2025-11-30 00:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 43.1 |
| de1dbd6b-a423-3963-96be-45899a0bc142 | -23.6243 | -52.9365 | 2025-11-30 00:40:00 | GOES-19 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 79.4 |
| 5da72a5f-fbb4-30f0-903f-66e143e2d61f | -12.0004 | -49.2683 | 2025-11-30 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 03eda75d-49ec-326f-a6ac-bf1c3990674f | -5.7306 | -39.8534 | 2025-11-30 00:40:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 1d682906-e7c0-35e0-9c02-4ca9b4dcea53 | -8.0318 | -43.1493 | 2025-11-30 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| e8dc87a4-34a8-39c8-ae8f-4566e084a313 | -2.6322 | -48.542 | 2025-11-30 00:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| aedb16fc-5309-3e30-b82a-4558aa26df73 | -8.1633 | -43.2055 | 2025-11-30 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.9 |
| 98cbe26f-1bd9-32b2-bb27-d5b53ce4042f | -8.0324 | -43.1022 | 2025-11-30 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 9f8ef83e-dce9-3f46-a0dd-51b962dca64c | -8.0507 | -43.1472 | 2025-11-30 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| f950123d-0a86-3c24-bc3f-a5099a4dc23b | -3.5968 | -44.5289 | 2025-11-30 00:40:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 5606305b-9a3d-3d6b-9cb2-2962c50e6237 | -5.7309 | -39.8286 | 2025-11-30 00:40:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 257.1 |
| 43d7fcf3-0723-363f-ae0e-93c2e97426d5 | -8.0321 | -43.1257 | 2025-11-30 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 152.7 |
| 6f0933ca-9d6d-3b4d-b231-3c28789852d7 | -2.6507 | -48.5414 | 2025-11-30 00:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 157f7f4e-3c07-32c0-b57b-6c48c58dc0d0 | -8.051 | -43.1237 | 2025-11-30 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 208.8 |
| 5485a136-340c-3ab7-879c-c49e7ad1a42e | -7.5014 | -37.4242 | 2025-11-30 00:50:00 | GOES-19 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 66.7 |
| 520f6d3c-d7a5-3810-a56c-24f0f63968c0 | -5.712 | -39.8302 | 2025-11-30 00:50:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 148.6 |
| 646ea1e8-2cae-3f36-8fda-4ab5a1a066d4 | -2.6507 | -48.5629 | 2025-11-30 00:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| dcaef07d-8892-3142-be5f-3b8cd5bf114f | -3.1505 | -44.4111 | 2025-11-30 00:50:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 963baa51-d911-3419-8635-01a5d34c6645 | -3.1506 | -44.3883 | 2025-11-30 00:50:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| f683fb8b-d49c-3c6a-8c05-afcac204381a | -2.6322 | -48.542 | 2025-11-30 00:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 54bfcbf1-c38e-3ec9-ae51-94f3ab3961d3 | -4.4358 | -44.486 | 2025-11-30 00:50:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 3fa29a94-e959-3509-b913-5968a5e074a2 | -5.7309 | -39.8286 | 2025-11-30 00:50:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1075.1 |
| 68c32b47-6467-33a5-b4c8-aca2fb10859b | -8.0321 | -43.1257 | 2025-11-30 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 143.4 |
| bb093881-2304-381a-9373-7904de2645e9 | -8.0318 | -43.1493 | 2025-11-30 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| 7fbdecf2-e93a-3616-a114-4dd168ea17e2 | -8.051 | -43.1237 | 2025-11-30 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 193.1 |
| 60dfe736-69ff-3326-b2db-b8630234810d | -5.7495 | -39.8517 | 2025-11-30 00:50:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 69.3 |
| ac0156b0-8446-302e-b1ac-1c19b691bb01 | -4.4544 | -44.4849 | 2025-11-30 00:50:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 8912ac20-8005-3146-905b-4a3de5622d9b | -23.6454 | -52.932 | 2025-11-30 00:50:00 | GOES-19 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 78.8 |
| 8593deec-d177-3558-afcb-691736b810dc | -11.0714 | -54.7664 | 2025-11-30 00:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| d0416189-06fb-3966-8251-e6b1782aa558 | -2.6507 | -48.5414 | 2025-11-30 00:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 7c8d19af-8ba0-3645-bdfa-097fefedce29 | -8.0507 | -43.1472 | 2025-11-30 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| a67c4499-0407-3f9c-82dd-82f73cd62e3f | -8.1822 | -43.2034 | 2025-11-30 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.7 |
| b5578acf-a3bf-3e70-b612-8fc78a37c0c2 | -12.0195 | -49.2659 | 2025-11-30 00:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 8f1f1520-5fe4-3291-851b-a3659912b75c | -19.9936 | -47.8375 | 2025-11-30 00:50:00 | GOES-19 | DELTA | MINAS GERAIS | Brasil | 3121258 | 31 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 957d165c-52c0-38ee-b41d-07808066c8c7 | -3.132 | -44.3891 | 2025-11-30 00:50:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 822fd2cd-c212-39fc-b082-7f489d3fc8ea | -3.1319 | -44.4119 | 2025-11-30 00:50:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| f5715612-ad26-3eca-97e1-dc48377ab607 | -5.7311 | -39.8037 | 2025-11-30 00:50:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 125.8 |
| 8f9ecb34-659f-3679-8d4f-4144ecdd1c26 | -5.7118 | -39.8551 | 2025-11-30 00:50:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 66.5 |
| ca5d1a53-0971-3104-a109-7151502297d7 | -12.0004 | -49.2683 | 2025-11-30 00:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| be8a45cb-c650-3d45-a001-f2afac48d668 | -8.1633 | -43.2055 | 2025-11-30 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 28c03ca4-37ea-3cc5-b52c-b91636779545 | -5.7498 | -39.8269 | 2025-11-30 00:50:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 153.2 |
| 4657eb85-0090-3d74-a304-6d557b7b80cd | -5.7306 | -39.8534 | 2025-11-30 00:50:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 409.9 |
| 084a0f0f-9df7-3a97-9eef-4ece5b1811d6 | -8.0321 | -43.1257 | 2025-11-30 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.3 |
| 93f7a3aa-9b5e-3346-b20b-9808d9ac7c44 | -11.0714 | -54.7664 | 2025-11-30 01:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| b8d72b7f-0795-3954-b808-f1006c6b6249 | -12.0004 | -49.2683 | 2025-11-30 01:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 5eead5ce-921b-35ae-8eac-06c93a9b558c | -2.6507 | -48.5414 | 2025-11-30 01:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 5ad6eafe-3b8c-3dcb-885a-9507970e51a6 | -8.0513 | -43.1001 | 2025-11-30 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.4 |
| e963759a-f35b-300c-a8e7-8f39d70f140f | -8.051 | -43.1237 | 2025-11-30 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 161.7 |
| a879089a-a8ef-387d-a497-0fbf7be582d2 | -5.7495 | -39.8517 | 2025-11-30 01:00:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 46.1 |
| 325d0f6c-2400-3d8f-9234-32e64f60ba26 | -4.4544 | -44.4849 | 2025-11-30 01:00:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 52262a4f-1fe3-311d-86ba-2875e547d1bd | -19.9936 | -47.8375 | 2025-11-30 01:00:00 | GOES-19 | DELTA | MINAS GERAIS | Brasil | 3121258 | 31 | 33 | nan | nan | nan | Cerrado | 61.6 |


[Clique aqui para ver as próximas entradas](README4.md)
