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
| d6d32df7-92c0-3fcf-a73e-a17d59ac4515 | -2.867 | -45.4182 | 2025-11-11 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 226.6 |
| 1a4c2262-cf5b-35b5-9e83-89a619adfc2f | -2.8669 | -45.4406 | 2025-11-11 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 173.6 |
| db4169de-4e0b-3938-8896-132a2ebb7f0b | -2.8484 | -45.4188 | 2025-11-11 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 338b05aa-a404-3781-a54a-1493ec45ac8a | -3.9552 | -43.8004 | 2025-11-11 00:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 201b6772-04a2-3b9c-a614-22bef11e465b | -4.5864 | -44.2943 | 2025-11-11 00:40:00 | GOES-19 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 297d17a0-3322-38f9-84cb-497658ae6872 | -2.8855 | -45.4175 | 2025-11-11 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 127.0 |
| d3960be0-e9ef-3c54-a963-d6184b792aae | -2.8854 | -45.44 | 2025-11-11 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 1dbbb9c9-82b3-3fa6-a8d0-ed75ebdef79a | -5.4241 | -44.6524 | 2025-11-11 00:40:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 2ac12a44-33f8-348c-85bc-31f4ff2932d6 | -2.9227 | -45.4162 | 2025-11-11 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 129.3 |
| fc93cb5d-cbef-3ae2-b745-b8f8ef4f513f | -9.5534 | -40.3254 | 2025-11-11 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 136.1 |
| d8f470bd-2782-3e6c-8a1f-a89e8188cb63 | -19.7219 | -58.0699 | 2025-11-11 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 56658c6e-ec7d-3173-a854-4ba9fcb0aceb | -2.9413 | -45.4155 | 2025-11-11 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 929486bb-8d48-38e6-8922-5f2f4acf2414 | -3.9739 | -43.7994 | 2025-11-11 00:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| a6d95ab8-16d6-339b-b960-0da8ada3b111 | -19.7424 | -58.0465 | 2025-11-11 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 9a664534-2b89-3328-9220-8a101e0b0f36 | -19.7223 | -58.0491 | 2025-11-11 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.4 |
| 3bbc28c6-9dfd-325f-98ec-592ea240d116 | -3.974 | -43.7763 | 2025-11-11 00:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 5d5c1bd0-ace5-3368-a5b4-1f117557bf8c | -19.742 | -58.0672 | 2025-11-11 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| 57ad696c-db22-3c85-b949-e9b90950e2d4 | -4.7204 | -46.4497 | 2025-11-11 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| cdc56060-b0a0-3e46-a1fe-054423b58d72 | -2.9413 | -45.4155 | 2025-11-11 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 3cdf8e8d-2a5c-3168-8a56-6981c1fd7414 | -21.4568 | -48.7989 | 2025-11-11 00:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 890a410c-e4d0-3375-bbe9-802dc2267b39 | -4.5864 | -44.2943 | 2025-11-11 00:50:00 | GOES-19 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 9599ddb6-8cfa-37d3-a0bb-833b3ced3276 | -3.9552 | -43.8004 | 2025-11-11 00:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| d16f1cf1-51df-310b-8c15-e71401d230eb | -2.9228 | -45.3937 | 2025-11-11 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 08b99f66-624a-3c7b-bb9e-9606443d37a1 | -2.9414 | -45.393 | 2025-11-11 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d87e3cf0-dda5-33d5-894d-4c1a26e75c1e | -2.867 | -45.4182 | 2025-11-11 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 210.5 |
| 0555a55a-4914-3f10-a2e2-5e97ea9f885e | -9.9828 | -44.4581 | 2025-11-11 00:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| ae8d9d04-81e4-359f-ba1b-d069c13d3095 | -3.9554 | -43.7773 | 2025-11-11 00:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 4f358ec3-8c8c-3304-a753-59da56876099 | -2.8854 | -45.44 | 2025-11-11 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 428a3bb8-0650-3d69-b7ad-1a680ca59c99 | -2.9227 | -45.4162 | 2025-11-11 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 5936dee4-9d38-3276-b0e7-61c475293936 | -3.974 | -43.7763 | 2025-11-11 00:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 3d377997-8832-34e9-b6f8-6635557ae48e | -2.8855 | -45.4175 | 2025-11-11 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 4da4efd0-dad2-3714-87a2-70db279677a9 | -21.4361 | -48.8037 | 2025-11-11 00:50:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 105.2 |
| ee65694d-4628-3ce7-ad23-0843e94509a6 | -4.5862 | -44.3172 | 2025-11-11 00:50:00 | GOES-19 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| a8178957-bd08-3938-83b8-145ac3169367 | -1.6453 | -52.0447 | 2025-11-11 00:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| b6cf4b86-b3f9-36e8-9e16-10f9eea74cd4 | -2.8669 | -45.4406 | 2025-11-11 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 203.0 |
| 97cbfa15-2df5-3b94-914e-ce4a3e0b55cd | -19.8081 | -58.023899 | 2025-11-11 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ecc6a74e-a824-3650-908f-cb08334962ad | -20.1026 | -54.653999 | 2025-11-11 00:52:00 | METOP-B | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3022ded9-4063-3288-923f-462e29ac8148 | -19.731501 | -58.049702 | 2025-11-11 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 784dfb70-9731-3ab6-b589-815b9c5b6722 | -19.7967 | -58.0187 | 2025-11-11 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 00de94d3-51c9-3e6d-ac3f-8c2e312fbbd7 | -19.8179 | -58.021599 | 2025-11-11 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a91a8a61-fb67-363b-9d9a-7a3f0c390ae4 | -21.4217 | -48.767799 | 2025-11-11 00:52:00 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ce4f9a6b-a7fa-3675-8605-237690aaf4f4 | -19.7299 | -58.042198 | 2025-11-11 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| aeabe3e5-8925-3179-90e9-d2df13fd148a | -19.806499 | -58.016399 | 2025-11-11 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6af9e536-edc0-3c34-8fd3-b0c1a1eabb41 | -19.733101 | -58.057098 | 2025-11-11 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 62dbfc4b-dbc7-3068-8cd0-907f9d12e87f | -17.129299 | -55.739399 | 2025-11-11 00:52:00 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9f4fd6c9-d620-3115-84ed-1e1f2291c619 | -19.739599 | -58.039902 | 2025-11-11 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4617e489-0fb0-3efc-8b45-3e8ef05ea778 | -19.754499 | -58.013 | 2025-11-11 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1a088d44-c2d1-31f8-850d-3b42c317ae6e | -19.750999 | -58.045101 | 2025-11-11 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d81c6777-5b6a-3d61-ada0-051b803c49be | -20.7379 | -49.7668 | 2025-11-11 00:52:00 | METOP-B | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e6347683-e4b4-343e-8bc8-d47dad80f091 | -21.4258 | -48.7831 | 2025-11-11 00:52:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 478f6fa9-d301-3783-8b1a-b149e3ce0982 | -21.429899 | -48.798401 | 2025-11-11 00:52:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 631cc0db-d0e6-307b-82d3-cb85ac0559d8 | -19.749399 | -58.037601 | 2025-11-11 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 25f25841-1f6a-33bd-8493-a091f20e55a6 | -19.787001 | -58.021 | 2025-11-11 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0c5cd3d6-f257-31bd-9370-1f67c8aeffe0 | -18.3873 | -54.9687 | 2025-11-11 00:52:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c3a92abc-0e16-3770-8d56-30cd3f57905b | -19.7855 | -58.013599 | 2025-11-11 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f6576d0d-3acc-369c-8c9d-bf92ee3c6f82 | -16.683399 | -51.818199 | 2025-11-11 00:52:00 | METOP-B | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1d976c7c-7bdb-3e3a-9de2-04e817147677 | -19.741199 | -58.047401 | 2025-11-11 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6c4a3a4e-b354-36cc-8dc1-7d8af527f2a0 | -20.7344 | -49.753101 | 2025-11-11 00:52:00 | METOP-B | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f63e9d98-ed46-3b5b-a81c-979859818e30 | -19.7201 | -58.044498 | 2025-11-11 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0c8347ad-3f53-3c1b-8641-6f119600cc52 | -18.466999 | -53.380699 | 2025-11-11 00:52:00 | METOP-B | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1f9645e4-0ca5-35b7-bf93-8ee5ecd57b8b | -19.762699 | -58.0033 | 2025-11-11 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 54a28cb0-1b5f-30d3-83e9-073723b90893 | -17.127501 | -55.7318 | 2025-11-11 00:52:00 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 219085df-0d9e-358a-91ae-db840da1de68 | -18.4692 | -53.389801 | 2025-11-11 00:52:00 | METOP-B | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 28d64b98-00c0-3604-a61e-3ca4bce1ee30 | -19.7428 | -58.054798 | 2025-11-11 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e0a66a50-1ed7-3652-9a7e-414d44da9633 | -17.5508 | -54.007301 | 2025-11-11 00:52:00 | METOP-B | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4ae55679-55b3-367c-aadb-5f1ed16f6e87 | -20.776699 | -48.3442 | 2025-11-11 00:52:00 | METOP-B | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ea2fc70e-e67a-3fc1-bab6-9da47d816cf5 | -19.764299 | -58.0107 | 2025-11-11 00:52:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a610dae6-570c-3049-8d91-c41560ee501a | -18.3892 | -54.976601 | 2025-11-11 00:52:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| eb0e1531-2542-30fb-b9df-81d97529e444 | -18.471399 | -53.398899 | 2025-11-11 00:52:00 | METOP-B | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cdccf879-826e-37b0-8c58-cabd7fd885ab | -18.391001 | -54.984402 | 2025-11-11 00:52:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 778f9619-0ba3-3ec8-a591-77da5251146e | -3.4756 | -54.026699 | 2025-11-11 00:55:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64101379-e09a-3976-80bb-cabd46adb546 | -2.8669 | -45.4406 | 2025-11-11 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 203.0 |
| 8ca2dbdc-3744-3d60-940c-f85d9a59c5dd | -3.9554 | -43.7773 | 2025-11-11 01:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| bd8d4322-ccd5-3b35-8ccb-5cae936b215a | -9.5343 | -40.3282 | 2025-11-11 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.1 |
| 3a73a20d-e793-30b5-bde3-cb3417d35b5c | -9.5725 | -40.3227 | 2025-11-11 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 142.6 |
| 5d6959b5-ba28-3c6d-9d5b-0fd1ec2c854e | -2.8854 | -45.44 | 2025-11-11 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 86db4603-cc53-35d0-bef0-d386a3f547f8 | -2.9414 | -45.393 | 2025-11-11 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 3f3efb07-108d-3075-a4b8-4b790cf301c3 | -4.9036 | -44.3208 | 2025-11-11 01:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 0a8f1d28-9d39-3eb3-ac4d-bb7a8e418553 | -9.5534 | -40.3254 | 2025-11-11 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 221.6 |
| 3bab1170-017a-3f73-821f-e0ad6f28da17 | -2.6626 | -45.4251 | 2025-11-11 01:00:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| fad62321-6297-3e4f-864a-d9f33066c45a | -4.7204 | -46.4497 | 2025-11-11 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 963effc8-96fc-3c74-9b19-e8ac8b4c8dab | -2.9227 | -45.4162 | 2025-11-11 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| feaf1fd1-80b7-3fd6-a4e5-d148473d1da9 | -2.8855 | -45.4175 | 2025-11-11 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 29269d6e-e8d7-39b7-9559-626172264136 | -3.974 | -43.7763 | 2025-11-11 01:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 1428bb9d-298b-34c2-a444-3c953cffe457 | -21.4361 | -48.8037 | 2025-11-11 01:00:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 24002a7c-b570-3e2a-b9ec-395e3e73e6b4 | -4.5862 | -44.3172 | 2025-11-11 01:00:00 | GOES-19 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 44f2f18c-e972-34ac-80f5-6af94fc002bc | -2.9413 | -45.4155 | 2025-11-11 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 7d0a3add-a01d-34f0-ae35-42539a78748e | -2.867 | -45.4182 | 2025-11-11 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 277.2 |
| 6b9e3209-fa62-3034-9065-df72786efa06 | -2.8854 | -45.44 | 2025-11-11 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 140.6 |
| af730bdd-4a8e-3e03-924b-d9a80c7c7a73 | -2.8855 | -45.4175 | 2025-11-11 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 9a0f6b95-bca8-3567-babf-bffaa7b119d4 | -4.7204 | -46.4497 | 2025-11-11 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| c4c4a79f-4e02-3ecb-bd17-eba653c236e6 | -4.9036 | -44.3208 | 2025-11-11 01:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| bac401aa-9aa1-37cc-8f62-a0e88682abf4 | -3.9554 | -43.7773 | 2025-11-11 01:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| bf17cb4a-40b2-39ed-a546-35d42af30fb3 | -2.8484 | -45.4188 | 2025-11-11 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 11cf79f0-3318-3b2a-b323-85521c5bf32f | -2.9227 | -45.4162 | 2025-11-11 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| aedbfbc8-28f4-33b3-94d0-4b16193b85a5 | -2.8483 | -45.4413 | 2025-11-11 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 2f495bc6-b51e-3077-b83c-a6831a380cf3 | -2.6626 | -45.4251 | 2025-11-11 01:10:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 4338586b-a394-330c-930f-bebf958491d4 | -21.4361 | -48.8037 | 2025-11-11 01:10:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 90.8 |
| c8dbe582-3dc0-3321-991c-1dead90a7437 | -3.974 | -43.7763 | 2025-11-11 01:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 9a397d87-0c32-3ce1-894a-5c9180e6d8e2 | -9.5534 | -40.3254 | 2025-11-11 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.6 |


[Clique aqui para ver as próximas entradas](README7.md)
