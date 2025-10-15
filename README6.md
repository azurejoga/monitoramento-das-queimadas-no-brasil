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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9d324ed-5e64-367a-bcb6-b9786ee24810 | -3.0796 | -47.7293 | 2025-10-15 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 5b51e888-2dea-3af2-895f-65c7bc539f9b | -3.0981 | -47.7286 | 2025-10-15 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e6340f7a-29bc-317d-93b0-b332e58dad08 | -14.2621 | -51.6053 | 2025-10-15 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| ce8305bf-9815-3bb4-b3c5-c5851ccb58ee | -12.9179 | -47.1078 | 2025-10-15 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 297e02c8-fee7-3dcf-9422-5f1ad82e7935 | -7.9442 | -44.115 | 2025-10-15 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 7ed789e5-39fc-3d76-8caf-c7cd4503663a | -12.9372 | -47.1049 | 2025-10-15 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| bc7b1e9d-964e-33c7-a0fb-8894067b15bc | -5.3919 | -44.0356 | 2025-10-15 00:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 969074cd-4639-3ae4-82d1-00339ac6e849 | -7.9439 | -44.1381 | 2025-10-15 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 9e8d887e-9a73-3a2c-9b34-1696815379ea | -11.0626 | -51.009 | 2025-10-15 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 2ccb8ad9-7c75-38be-bb8a-388015b8321c | -14.2431 | -51.5865 | 2025-10-15 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| a50bca5b-98d4-3b3d-99b8-e9165b559ba9 | -12.9376 | -47.0823 | 2025-10-15 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| c374fc70-7f6a-37aa-885e-aae351c1d7c2 | -4.8915 | -43.4678 | 2025-10-15 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 325.0 |
| e3931635-c2b6-3c9c-847d-82b660b5f1fe | -12.2113 | -50.4096 | 2025-10-15 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 2ca997f3-0c39-389e-b3d9-fa451f0c9e99 | -8.7215 | -43.868 | 2025-10-15 00:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| d057008a-5f08-3e70-96e0-60aec7a959f3 | -3.686 | -45.2276 | 2025-10-15 00:40:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 943b1214-30ec-3232-9b64-d7b6d0cae4e4 | -4.9102 | -43.4666 | 2025-10-15 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 210.9 |
| 57ba9d65-1b08-39a9-b362-4ed07bedb17a | -14.2428 | -51.6079 | 2025-10-15 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.5 |
| dd5e3fc6-2d7b-32bb-9132-65801c57898e | -3.6674 | -45.2285 | 2025-10-15 00:40:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 0927b454-9458-3488-bcd3-f691eadefb98 | -7.9628 | -44.1362 | 2025-10-15 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 4be81aed-c65d-3b9c-850d-e424c40832e7 | -4.8916 | -43.4446 | 2025-10-15 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 248.5 |
| a5d6eca8-3132-34eb-ae21-07fc07cc0d48 | -3.6675 | -45.2059 | 2025-10-15 00:40:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 532d1213-61db-3942-9661-b06f1de8d0b4 | -4.9104 | -43.4434 | 2025-10-15 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 1a48ace2-fdea-3227-885d-444ad29f57d6 | -4.6511 | -43.1104 | 2025-10-15 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 90e451eb-c688-3429-a80c-f8a254e97c4d | -4.6698 | -43.1092 | 2025-10-15 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 0835b681-8305-30ff-9258-3a7f7c19722a | -5.4465 | -44.2159 | 2025-10-15 00:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 77bd9d95-83ac-32be-82a5-0b2be6e93d45 | -5.409 | -44.2185 | 2025-10-15 00:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 8b122d21-3774-307e-89aa-6fb6eaa8c3ce | -14.2621 | -51.6053 | 2025-10-15 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| c08d5968-03cc-3fc1-b790-882d13b2217a | -7.9442 | -44.115 | 2025-10-15 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 082bb092-32e2-33e5-a175-ea77b987999f | -5.4278 | -44.2172 | 2025-10-15 00:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 292a54c6-66c7-3937-b084-1d2a4c54d851 | -4.6509 | -43.1337 | 2025-10-15 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 197.4 |
| b9dbf6ae-eb30-3459-8241-a44c97294d5f | -7.9439 | -44.1381 | 2025-10-15 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| b530c6e4-7a50-3146-a4e1-e0ee50d85961 | -4.9102 | -43.4666 | 2025-10-15 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 254.1 |
| ee877cd9-686c-3364-bbfe-c0d486ba85dc | -7.9628 | -44.1362 | 2025-10-15 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 4802a13d-487b-35c7-be13-4d769f38e267 | -3.564 | -51.1104 | 2025-10-15 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 0dbfbb1a-1159-3027-bae3-b646451cd5a0 | -14.2428 | -51.6079 | 2025-10-15 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 7d1b34c9-c84a-3e35-8147-c6274bde2580 | -4.6696 | -43.1326 | 2025-10-15 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 932ea663-9755-33e6-b166-ea485ca96c46 | -12.9376 | -47.0823 | 2025-10-15 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 790b51c3-3ecf-36c9-8590-c509d66efbf4 | -14.2431 | -51.5865 | 2025-10-15 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 81417470-6a8d-31bd-92ba-24c0339a02d2 | -5.428 | -44.1942 | 2025-10-15 00:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 9f6c2a1e-4ab2-36b6-903b-4861bf86f3af | -4.9104 | -43.4434 | 2025-10-15 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 055c130d-bc2f-3882-a065-6537fd91a783 | -3.6674 | -45.2285 | 2025-10-15 00:50:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 112.8 |
| e4eb4899-3601-30e4-a7fa-6b1a37048f1e | -4.8748 | -45.6827 | 2025-10-15 00:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 132.3 |
| ac5aea2a-b0c1-3628-abf2-29b3840e7303 | -5.4276 | -44.2402 | 2025-10-15 00:50:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 0f90d687-f793-3bf1-9d15-6a4600386ce5 | -4.8916 | -43.4446 | 2025-10-15 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 33d869e9-38a4-3874-b4a0-2d779069a68b | -3.6675 | -45.2059 | 2025-10-15 00:50:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 8023f60f-0263-3a14-b577-1083258f87a7 | -6.4543 | -44.5749 | 2025-10-15 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 839d445d-2285-3e16-b886-1e063d90b979 | -3.5639 | -51.1312 | 2025-10-15 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 7c3093ed-a20e-35f2-886b-05896328a18f | -4.6511 | -43.1104 | 2025-10-15 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 1aa968e7-14ad-370a-963e-3d634cf2c4ea | -3.686 | -45.2276 | 2025-10-15 00:50:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 3c42f4cc-bac7-33ae-9ffc-27e0e8d4591a | -4.6698 | -43.1092 | 2025-10-15 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 809129df-b801-3c2a-b1e2-b14355540bb8 | -4.875 | -45.6603 | 2025-10-15 00:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 62918777-eae0-3daa-9d33-29e8ec540585 | -4.8915 | -43.4678 | 2025-10-15 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 253.8 |
| 7b5459ad-179f-387d-97df-d8cce50d0a40 | -5.4465 | -44.2159 | 2025-10-15 01:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| ed43bbe2-5e93-3b3c-afc0-d21d754e41bd | -12.9376 | -47.0823 | 2025-10-15 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| ffad8c12-a975-3b91-87a6-e2ae2f3967a2 | -7.9442 | -44.115 | 2025-10-15 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 60d756d6-86b9-3301-938f-3e8a01ae0926 | -4.875 | -45.6603 | 2025-10-15 01:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 2929c652-020e-314f-a6ea-25b2a038f03b | -3.5639 | -51.1312 | 2025-10-15 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 3f894cb1-2543-39e3-a7d7-cdb0d30e11ae | -5.4278 | -44.2172 | 2025-10-15 01:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| eb2e72b2-13cd-3ea7-b186-146af9d4726a | -5.409 | -44.2185 | 2025-10-15 01:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 9cb75096-af59-387d-88fa-b252868d358e | -4.8916 | -43.4446 | 2025-10-15 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 3dd964f7-82bf-3333-b65b-5d1d0ebdfd75 | -4.8915 | -43.4678 | 2025-10-15 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 265.5 |
| 780533b2-c72e-31e3-96e6-884e7913e18a | -4.9102 | -43.4666 | 2025-10-15 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 263.8 |
| 0888cf8b-4888-32e2-989d-20e91a85eea0 | -3.564 | -51.1104 | 2025-10-15 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 140.1 |
| 78c919ee-e124-3ee1-a4b4-a0cdd15a3eda | -6.4543 | -44.5749 | 2025-10-15 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| c1b3d228-c3e1-35a4-ad3f-22682baf6080 | -4.6698 | -43.1092 | 2025-10-15 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 0352a719-3176-3f9f-a6c6-d7fb5108008b | -5.4467 | -44.1929 | 2025-10-15 01:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 79197be2-95a5-32bb-aaf9-dce2758ad1dd | -4.6511 | -43.1104 | 2025-10-15 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 7db5242f-d687-38c2-8551-7784b81f11e8 | -7.9439 | -44.1381 | 2025-10-15 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 52619d2c-36da-31f0-aefb-339de355b0af | -4.6509 | -43.1337 | 2025-10-15 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 17945519-e4cb-3607-91fb-705cd1bea28f | -3.6675 | -45.2059 | 2025-10-15 01:00:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 0bba8c8e-0a4d-3178-a54b-57949fa2d10b | -4.6696 | -43.1326 | 2025-10-15 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 4a4d30fd-737a-3638-b762-f9edd66e21b5 | -4.8748 | -45.6827 | 2025-10-15 01:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 188.6 |
| 834f60fb-3b7a-36e7-ba37-472279e1adfa | -3.6674 | -45.2285 | 2025-10-15 01:00:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 87.5 |
| e53d6812-6f86-3bfb-853e-25ed88987819 | -12.1356 | -50.3758 | 2025-10-15 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 86a17888-3089-3758-8cb3-da5d0e0914bc | -5.4276 | -44.2402 | 2025-10-15 01:00:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 1bf7f4f3-dc76-3311-9d74-5b361d4dacac | -4.9104 | -43.4434 | 2025-10-15 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 176.9 |
| 5e6387ed-0004-33de-ab5c-9b6879f4eff0 | -12.1352 | -50.3973 | 2025-10-15 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| b60b8b3d-93ed-319a-b6ca-032748c40b62 | -4.8562 | -45.6838 | 2025-10-15 01:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 1e0a3386-d3f2-33a1-8e91-c657c6e5e63e | -5.428 | -44.1942 | 2025-10-15 01:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| d6793233-5978-3d64-bb8b-a08778e00ad0 | -7.9628 | -44.1362 | 2025-10-15 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 46.7 |
| e980d97b-5731-3c40-bc80-4b925c7aa851 | -3.5639 | -51.1312 | 2025-10-15 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 2f910520-c8fa-37cd-ad99-bbbbf1a1cfbd | -7.9628 | -44.1362 | 2025-10-15 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| e6452f64-43e8-3087-9aa9-c7e4c492fef4 | -4.6696 | -43.1326 | 2025-10-15 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 111717f3-1f7d-36e3-9dae-3f48d6ccbfb4 | -4.6511 | -43.1104 | 2025-10-15 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 2115f248-1c48-3481-932e-a14a809db096 | -4.9102 | -43.4666 | 2025-10-15 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 328.0 |
| 83bb7ad2-1d91-3262-a618-3293e5fa028f | -7.9442 | -44.115 | 2025-10-15 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 6f6aacb0-5cb7-3814-bd15-127c06debb01 | -7.9439 | -44.1381 | 2025-10-15 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 30025981-3ef1-3d18-a240-0126dbee2a27 | -4.8916 | -43.4446 | 2025-10-15 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 193.0 |
| 79585d23-3f56-3356-889b-87b5004ce29a | -3.6674 | -45.2285 | 2025-10-15 01:10:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 19cc72af-cfce-39fc-9ce4-5ecd50fc54e1 | -4.6509 | -43.1337 | 2025-10-15 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 8abf7a02-22ef-32cd-80ee-3b5973d723f4 | -4.9104 | -43.4434 | 2025-10-15 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 227.4 |
| 7fcd32fd-d1ff-38ff-8871-2df5fb463030 | -4.8915 | -43.4678 | 2025-10-15 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 276.1 |
| 75225696-86ba-37a7-96df-19353ca09ca1 | -4.6698 | -43.1092 | 2025-10-15 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| d1f1b053-7af2-391d-a768-0c1bbc7e4634 | -3.564 | -51.1104 | 2025-10-15 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| bddab0d7-29dc-343f-9002-fef25e4e39cf | -7.9439 | -44.1381 | 2025-10-15 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 9dcd60a0-2569-392d-99e2-f39c2864d249 | -5.409 | -44.2185 | 2025-10-15 01:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| fd5498bd-1b26-3c0d-b85b-f6ba2863480d | -4.8915 | -43.4678 | 2025-10-15 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 235.4 |
| ac4f2a38-5573-3ba9-8f85-e5e1064ba8ca | -4.9104 | -43.4434 | 2025-10-15 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 1fbcd501-4757-3493-8a8f-c878cdcbc35d | -3.6674 | -45.2285 | 2025-10-15 01:20:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 430b77c5-a203-3379-becf-8ed54ba17326 | -5.4463 | -44.2388 | 2025-10-15 01:20:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 194.7 |


[Clique aqui para ver as próximas entradas](README7.md)
