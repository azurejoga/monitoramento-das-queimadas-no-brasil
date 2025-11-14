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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a89a7238-45cf-3e6e-be8b-7f19e19cafdf | -7.8587 | -44.2925 | 2025-11-14 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f3f73323-357d-34a4-88e4-554649311265 | -7.1492 | -41.247002 | 2025-11-14 00:38:00 | METOP-C | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 58bffd6a-54d9-3bde-ba85-1404924a0c37 | -9.1207 | -43.952 | 2025-11-14 00:38:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1c6585a0-3092-35ae-8ffc-b2f63139602a | -12.0218 | -43.725899 | 2025-11-14 00:38:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bdaa89c9-8dcc-38d1-b96f-b9d665e2929b | -7.4906 | -47.333302 | 2025-11-14 00:38:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c370180-4c3d-301e-af13-b2e44e659a48 | -6.1562 | -48.037102 | 2025-11-14 00:38:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b5481be-48d6-336b-bcda-e0e51c70b4ea | -3.5094 | -45.5485 | 2025-11-14 00:38:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 97ea1b89-a205-34db-b3e9-fad5163f35fb | -7.0652 | -48.363899 | 2025-11-14 00:38:00 | METOP-C | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d39513ef-8cb3-3d08-acc8-45abf4d88a62 | -4.7084 | -46.448399 | 2025-11-14 00:38:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4e808e0f-3b91-3f84-915b-9195c3bbc2b0 | -11.8506 | -49.214699 | 2025-11-14 00:38:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6328e624-33ff-33a5-9e0c-0cf1f53d0867 | -2.1695 | -48.369202 | 2025-11-14 00:38:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b233871-94cf-3fdd-95ab-5ee6ff0ecc3f | 3.146 | -60.7075 | 2025-11-14 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c8b283ed-610e-3215-9de4-9e805b514f79 | -4.221 | -49.1267 | 2025-11-14 00:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| f76f9dac-aeba-3bab-8cb9-7d0a2e6363e0 | -7.8665 | -44.3077 | 2025-11-14 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 44c0c865-e844-3f92-82d4-d18655e7df34 | 3.1094 | -60.746 | 2025-11-14 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 61.5 |
| f0b0a8e0-f486-35eb-a3d2-e44bbdc608f8 | -4.7206 | -46.4276 | 2025-11-14 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| bb4a2c84-a9d5-374c-b354-f3ac3063d01b | -12.6992 | -45.4335 | 2025-11-14 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 5ccfb5cb-3f07-36d1-ba0f-8e1b608df606 | -11.8486 | -49.2218 | 2025-11-14 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 273.5 |
| 50d640c6-934e-3e0c-a3d1-d78d8919b4f4 | 3.0911 | -60.7653 | 2025-11-14 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 257.6 |
| 7100f078-51df-3598-af65-8704dad2779a | -12.7189 | -45.4074 | 2025-11-14 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 2da6ce36-74bf-3610-b668-34fd29a8c7ae | -6.1606 | -48.0507 | 2025-11-14 00:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 16d23145-84c5-3652-a4f8-e2b3c130732d | 3.1093 | -60.784 | 2025-11-14 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 7b2d43bc-df23-306b-81db-295b704cd82f | -9.6295 | -40.3392 | 2025-11-14 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.5 |
| db1abbec-e7ff-380a-9a0c-edf8e6eb74b8 | -4.7204 | -46.4497 | 2025-11-14 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 6575409c-4dcd-383d-8f3a-648dbe3102f6 | -2.9434 | -49.3655 | 2025-11-14 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 52a222da-a54e-3b70-974f-419e77eed0db | 3.1094 | -60.765 | 2025-11-14 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 265.5 |
| a9a330ad-f1b3-3534-8125-2164599e2d21 | -7.8479 | -44.2865 | 2025-11-14 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 351.1 |
| 18e9ad54-b478-32f2-ab15-3c1d2b01fda3 | -12.6996 | -45.4104 | 2025-11-14 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| e6b7ab5e-4ed7-37e2-959d-ee5df8a1bb37 | -4.0976 | -48.0144 | 2025-11-14 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| e0009a2a-bc9b-3053-b50d-bc0b2a3042c0 | 3.0911 | -60.7843 | 2025-11-14 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 94.4 |
| b24e82c9-cd77-355f-8161-f9b2e0215879 | -7.8668 | -44.2846 | 2025-11-14 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 4df6472d-c103-3af4-b922-e5b019d22011 | -7.8476 | -44.3096 | 2025-11-14 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 90b2ee9b-2039-323f-968b-57aeb4a581b5 | -11.8681 | -49.1976 | 2025-11-14 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 32636853-b1d9-3eee-96ab-c9b9b65fe2b6 | -4.7018 | -46.4508 | 2025-11-14 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 0cf8350f-bcbe-3d21-831b-d2db1174988e | -7.829 | -44.2885 | 2025-11-14 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.4 |
| bf2cc32b-31d9-3a54-814a-b30802bcf6f9 | -11.849 | -49.2 | 2025-11-14 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 546784d0-6be2-3b8c-bdbc-07de632e05bc | -11.8483 | -49.2436 | 2025-11-14 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 7989b753-8c72-3758-8fe4-26329726dccf | -12.7185 | -45.4305 | 2025-11-14 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.2 |
| fd7ce825-d83e-3ff4-8056-61137ea6cd77 | -2.8295 | -45.4868 | 2025-11-14 00:40:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 2db609dd-620a-362c-8907-cdc6640208e0 | -11.8677 | -49.2195 | 2025-11-14 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 234.5 |
| 827fd15c-cc62-37a3-b230-49b62ed3c37a | -4.702 | -46.4286 | 2025-11-14 00:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| baa18f80-8499-38d7-bf19-e577383aeab7 | -11.8674 | -49.2413 | 2025-11-14 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 17b354e5-2efc-386c-9262-abe610c7bb1f | -2.8861 | -45.2826 | 2025-11-14 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 567410df-b94a-37d2-8ff0-1333634700de | -9.6295 | -40.3392 | 2025-11-14 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 420.3 |
| 8da38c9f-83cd-3b58-9bcc-5c9d3c0e9bbe | 3.0911 | -60.7653 | 2025-11-14 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 327.3 |
| 7cc3282f-0a94-3a25-9e53-ae65993b4451 | 3.1094 | -60.746 | 2025-11-14 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 687bbe4c-32ea-3a47-86ba-c5e0416dea1e | -9.6291 | -40.3641 | 2025-11-14 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 75.6 |
| f2548174-2884-3d01-8697-ac4bb7d3aadc | 3.1093 | -60.784 | 2025-11-14 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 653a468e-8a4b-32f8-b128-5fdc568d8b44 | -12.7189 | -45.4074 | 2025-11-14 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| a99bc85c-96dd-3f58-bfcc-276c030fcfc1 | 3.0912 | -60.7464 | 2025-11-14 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 82.5 |
| adcddbf3-da16-3a1f-8e56-4693d523ef57 | -12.6992 | -45.4335 | 2025-11-14 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| bc7d664d-d22a-3567-9efb-ea78d9ebc653 | -7.8668 | -44.2846 | 2025-11-14 00:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 128.7 |
| b61a5f2d-7635-3d5d-82fb-c3428cfa554a | -14.9534 | -49.7755 | 2025-11-14 00:50:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 7b211090-f3d7-3f78-ba74-45a6870f7a58 | -7.8479 | -44.2865 | 2025-11-14 00:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 237.7 |
| ced6dc5f-5ae2-3d23-996b-f43232419259 | 3.0911 | -60.7843 | 2025-11-14 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 102.4 |
| bf751432-25ca-3eb2-8c1c-38b525cce00c | -6.1606 | -48.0507 | 2025-11-14 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 6411e7a0-707e-34f0-a7f9-5aeffce7e32e | -4.702 | -46.4286 | 2025-11-14 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 8965e94e-e300-35df-8284-fc2622a39cef | -7.8476 | -44.3096 | 2025-11-14 00:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 19b7e7e4-b30a-3823-98f8-99504e2261e8 | -14.953 | -49.7975 | 2025-11-14 00:50:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 135106b0-b318-3396-94ae-2a821ad44a4f | -11.8486 | -49.2218 | 2025-11-14 00:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 399.2 |
| d7401ced-0f1d-3625-96b4-7220b1319998 | -9.6299 | -40.3143 | 2025-11-14 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 59b3c326-62ab-390c-a68a-b946d063e57d | -12.7185 | -45.4305 | 2025-11-14 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| c728d726-fea8-3264-b770-61b61724b83c | 3.146 | -60.7075 | 2025-11-14 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 177978c8-e139-33d4-ada4-6540a1448cd8 | -7.8665 | -44.3077 | 2025-11-14 00:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 08fd52de-a678-3a24-b5f4-0fc2d579a00e | -11.849 | -49.2 | 2025-11-14 00:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 2f5a4722-8d26-34f1-b5a6-85f788170ef3 | 3.1094 | -60.765 | 2025-11-14 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 216.2 |
| 1fee9ed9-b6c2-32ad-9718-f53ec6971524 | -4.7018 | -46.4508 | 2025-11-14 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 168.9 |
| 50e2605b-607a-346a-a275-d71ca9a9829a | -11.8483 | -49.2436 | 2025-11-14 00:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| d6ed6803-a951-3073-8283-b1868650690e | -4.7204 | -46.4497 | 2025-11-14 00:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 97.6 |
| ff7feeb3-d6f9-3567-87ea-e33cf658abc4 | -9.6487 | -40.3364 | 2025-11-14 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 192.4 |
| ddf71e2c-0282-3969-b791-a3b0c725760b | -12.6996 | -45.4104 | 2025-11-14 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| ccaf9983-a615-3d9d-908f-6ec0a11dbf02 | -11.8677 | -49.2195 | 2025-11-14 00:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 72fcc0c5-d1cc-381c-982e-dd056a3633be | -6.1606 | -48.0507 | 2025-11-14 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 947cb7c5-fe9c-3426-a94c-a7802e9ee844 | 3.0911 | -60.7653 | 2025-11-14 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 223.4 |
| 0e823875-c278-3e09-a6ee-cf43f42e1674 | -11.8677 | -49.2195 | 2025-11-14 01:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 211.3 |
| d7ec35f3-3106-30ac-a1a5-bb73b7442c44 | 3.1093 | -60.784 | 2025-11-14 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 040c98d1-7439-3162-a694-157d81fcb4ee | -7.8476 | -44.3096 | 2025-11-14 01:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 51871704-40a7-3d1f-bfb3-6340dcc57386 | -11.849 | -49.2 | 2025-11-14 01:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 98d5de64-4afe-3a56-b390-4927f8a7770c | 3.1094 | -60.765 | 2025-11-14 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 321.7 |
| 307083d7-f2d7-3e7c-85db-82b87c6cf5d6 | -7.8668 | -44.2846 | 2025-11-14 01:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 0245af02-5fa8-32e1-895b-415e93e3dc60 | -7.8479 | -44.2865 | 2025-11-14 01:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 224.9 |
| 9fd2d3a0-3f74-3ae3-99c1-1bacd5e61acc | -11.8486 | -49.2218 | 2025-11-14 01:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 238.6 |
| 41d39d31-e489-337f-a8c6-da2b4d0e8410 | -4.7204 | -46.4497 | 2025-11-14 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| b2aa07ad-fda2-3450-8f6d-b458c5b8a00f | -11.8681 | -49.1976 | 2025-11-14 01:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 358f3851-e079-377b-a9b1-0efe87961eb2 | 3.0912 | -60.7464 | 2025-11-14 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.7 |
| c66c2b73-9926-336b-819b-cf27e96f11e3 | 3.1278 | -60.7078 | 2025-11-14 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| cd44ebf8-3884-3705-b8cc-df8d2b4a9247 | -4.7018 | -46.4508 | 2025-11-14 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 123.0 |
| f2891b07-cba1-36a5-bd30-4308cf01eec3 | 3.0911 | -60.7843 | 2025-11-14 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 92.8 |
| da407327-05d5-37d3-8c45-d9d14f394bc0 | 3.1094 | -60.746 | 2025-11-14 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 98a9eb17-a84d-3bf6-a7ee-554e0aa2df29 | -3.0171 | -49.427 | 2025-11-14 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 2e815958-f2f4-316a-9a63-36c79a6f81b5 | -7.8665 | -44.3077 | 2025-11-14 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 1412af5c-5ad6-3714-a37a-6e12cf7fc78e | 3.1094 | -60.765 | 2025-11-14 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 223.4 |
| 0f522c97-04ee-371c-b4fb-aeacd23c63ee | 3.146 | -60.7075 | 2025-11-14 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 6eb54a7a-e1cd-3c30-a12f-edd6317733c4 | -11.8483 | -49.2436 | 2025-11-14 01:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 1ace89c9-4bf2-30a6-b9a1-f52a9f31fa8d | 3.1093 | -60.784 | 2025-11-14 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 8bef9329-9677-3f73-b85a-fc15f08c616a | 3.0911 | -60.7843 | 2025-11-14 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 766b2a29-ea6f-3c4d-b4d0-61582f9df124 | -6.1606 | -48.0507 | 2025-11-14 01:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 836b43cc-02c5-3616-a039-991546b70db7 | -11.849 | -49.2 | 2025-11-14 01:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 2f64d9ba-8720-34c4-bb5d-d8f18aa9c993 | -4.7018 | -46.4508 | 2025-11-14 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 8d116228-a23d-35d9-8a5b-e91a96bee9ca | -3.4576 | -50.11 | 2025-11-14 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |


[Clique aqui para ver as próximas entradas](README11.md)
