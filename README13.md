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
| d00f595b-a3fd-3c61-8d00-3cdcb3724eaf | 3.1094 | -60.765 | 2025-11-14 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 50c58e1a-7942-34ec-a071-0105a70850d8 | -7.8476 | -44.3096 | 2025-11-14 03:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| bca685b0-7e86-3f53-b9b5-d9911a68a534 | 3.1278 | -60.7078 | 2025-11-14 03:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 0bbd087a-decf-3080-b7eb-5706fdaaadd2 | -11.8677 | -49.2195 | 2025-11-14 03:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 1698c51f-8916-326d-95b0-a6443f2b8a42 | -6.60294 | -35.25112 | 2025-11-14 03:04:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| af6754c8-b6d8-3f4b-8fd7-fe062694c3f6 | -6.48174 | -39.35075 | 2025-11-14 03:04:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| f01f5834-f3c8-3c55-b2b0-21b864947149 | -6.60233 | -35.25459 | 2025-11-14 03:04:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 48af365e-49cc-37ff-b607-3ceb6b5dc8a6 | -9.95589 | -36.26775 | 2025-11-14 03:04:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| c0337c9b-137c-3735-9684-0af00b4a13e9 | -6.59686 | -35.25378 | 2025-11-14 03:04:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d7665b1a-3452-378c-9f88-a3fae9ecba63 | -9.95656 | -36.26414 | 2025-11-14 03:04:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 96b2dbf9-2138-36b5-a87d-55188a437035 | -9.94278 | -36.21626 | 2025-11-14 03:04:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| c5da7efc-f3f2-36b4-b79c-3d6746b0f74e | -9.94211 | -36.21986 | 2025-11-14 03:04:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| bf5f8b66-127d-366c-aeb9-5b1199493441 | -6.59839 | -35.25015 | 2025-11-14 03:04:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b98afc1f-56e8-3964-80bc-1c84c4e453a4 | -6.59778 | -35.25353 | 2025-11-14 03:04:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 65516917-0895-3c7e-bbc5-37470583cee6 | -6.47697 | -39.35018 | 2025-11-14 03:04:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fcf964a4-4608-355c-9d9e-315ff5d70322 | -9.94825 | -36.21733 | 2025-11-14 03:04:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6431f3fa-2dac-30f6-a8ee-4a862660169a | -6.59744 | -35.2504 | 2025-11-14 03:04:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7313c825-2286-3194-ab41-6c1f1913d10a | -6.48394 | -39.35168 | 2025-11-14 03:04:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a3734ca0-5da8-3e57-804b-e54a6ad273cd | -17.62596 | -39.92411 | 2025-11-14 03:08:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 49bb254d-4e00-3660-8352-9673a7ab02bb | -16.5885 | -42.2212 | 2025-11-14 03:08:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| c33f2be2-57df-3c57-b492-8eb3e9335c3f | -17.62495 | -39.92871 | 2025-11-14 03:08:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| aab0be79-a51a-377b-95a4-41b06295d376 | -20.10046 | -41.67888 | 2025-11-14 03:08:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| dd60d91d-868b-37f6-a592-69fc650ab0b2 | -20.39314 | -41.96077 | 2025-11-14 03:08:00 | NOAA-20 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 66b0d495-40d2-3a55-9520-bb279a486664 | -20.39177 | -41.96652 | 2025-11-14 03:08:00 | NOAA-20 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9310f138-d2d9-3be2-bac2-3038adbce957 | -20.09793 | -41.68063 | 2025-11-14 03:08:00 | NOAA-20 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| c7759de1-5e12-3112-a40b-e61b672300f5 | -17.36599 | -41.71803 | 2025-11-14 03:08:00 | NOAA-20 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 848a7f79-20fc-31aa-b6f2-77266e483c72 | -20.0994 | -41.68335 | 2025-11-14 03:08:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| b2ae9797-e5f2-3d08-8ea0-ea37f6472103 | -20.10418 | -41.68247 | 2025-11-14 03:08:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 18e5a03a-a924-3c14-917a-45a4daf528d9 | -16.58692 | -42.22009 | 2025-11-14 03:08:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| bdcb19b2-3678-3f11-bc19-d889cfa3b3ad | -2.9434 | -49.3655 | 2025-11-14 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| e5c6ef79-6426-316a-a222-ff53d509368d | -7.8476 | -44.3096 | 2025-11-14 03:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 303291c5-b4d7-3dd1-a0e0-fa830616fa93 | -11.8486 | -49.2218 | 2025-11-14 03:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 8786821b-28dd-3f8b-b6fe-ce1418915886 | -11.8677 | -49.2195 | 2025-11-14 03:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| f4f59e81-4213-3a75-ba94-271f3e3c2186 | 3.1094 | -60.765 | 2025-11-14 03:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 686869dd-5699-326f-a611-2fcc7303f0eb | -7.8479 | -44.2865 | 2025-11-14 03:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 4c602f42-ca9f-3d87-98f9-a38d7ed673c3 | 3.0911 | -60.7653 | 2025-11-14 03:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 28baa3e2-d616-36ac-be36-2a14b7c88a87 | 3.0911 | -60.7653 | 2025-11-14 03:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 8e0b3c54-275c-3487-8747-374a68c88bc4 | -2.9434 | -49.3655 | 2025-11-14 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 86e4182d-f99f-348c-a5b9-bcc015ab02e8 | -11.8486 | -49.2218 | 2025-11-14 03:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 154.9 |
| c6e5161b-7dac-39f2-b5e2-ce10df0fd5ba | 3.1094 | -60.765 | 2025-11-14 03:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 994aea1e-c143-3a98-8cf8-dda7da449bd3 | -7.8479 | -44.2865 | 2025-11-14 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| fb8673ef-32f9-3ac3-81e3-c77c91d91396 | -11.8677 | -49.2195 | 2025-11-14 03:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 369435ee-a822-3899-b881-e4397bc587da | -7.8476 | -44.3096 | 2025-11-14 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 7a62dc59-dab2-3a94-a940-f42a5b52b8a5 | -14.7066 | -46.6164 | 2025-11-14 03:20:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 83ec018d-1d01-31f3-be7b-fa485bd4b429 | -11.8677 | -49.2195 | 2025-11-14 03:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| a034e41c-bcc3-3c33-82d9-39c93c2d72aa | 3.0911 | -60.7653 | 2025-11-14 03:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 47315516-4054-3df2-83ce-a91db15de362 | -12.7185 | -45.4305 | 2025-11-14 03:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| f9ec9d26-5a7d-38e3-8743-640a82f77d03 | -11.849 | -49.2 | 2025-11-14 03:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 41fa442f-912f-3f45-baba-db24d5a230f1 | -7.8479 | -44.2865 | 2025-11-14 03:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 4bf8dc14-2166-39a3-a4e7-0b263d2ea27a | 3.1094 | -60.765 | 2025-11-14 03:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 2aba3ea8-f8de-3915-af11-c4ed18f32f63 | -14.7066 | -46.6164 | 2025-11-14 03:30:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 889e4c8b-06ae-346e-a244-b800dd19cdd5 | -12.7189 | -45.4074 | 2025-11-14 03:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 6fb6b500-6a17-3dad-804d-063bb6d10b3a | -11.8486 | -49.2218 | 2025-11-14 03:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| ba9e1a14-ed3a-3969-9cf2-862037256c3a | -2.9434 | -49.3655 | 2025-11-14 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 0926044f-25a3-3b0b-9d97-cf36438fa158 | -11.8677 | -49.2195 | 2025-11-14 03:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 201942d9-7321-3c33-a717-f10424abb12b | 3.1094 | -60.765 | 2025-11-14 03:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 71150226-713d-369f-b476-ba7bde7d5252 | -2.9434 | -49.3655 | 2025-11-14 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| abd58c08-0b2d-34f1-97fa-7ad606068793 | -11.849 | -49.2 | 2025-11-14 03:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 89da1c50-88ff-3180-9776-6ba3aa9c1b7a | 3.0911 | -60.7653 | 2025-11-14 03:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 4cc9b78f-f82a-3ed3-9f25-7fb3669b3193 | -11.8486 | -49.2218 | 2025-11-14 03:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 26553fe5-3e5f-322c-ab45-e7a6e4117a39 | -11.8486 | -49.2218 | 2025-11-14 03:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 8585ea71-482c-36a9-811e-f7e85d584534 | 3.1094 | -60.765 | 2025-11-14 03:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 90.1 |
| b5f2eedd-5b8a-371d-9dd8-fe7764c218cd | -2.9434 | -49.3655 | 2025-11-14 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 676174af-23af-38cc-9693-b74fe756ae8d | 3.0911 | -60.7653 | 2025-11-14 03:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 7795021e-a8f0-3142-a920-9a995e8271a3 | -14.953 | -49.7975 | 2025-11-14 03:50:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 77dc21f9-8fda-31ef-89c8-cfe71515ae73 | -11.849 | -49.2 | 2025-11-14 03:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| f174352a-b249-3577-95f5-3999bdea989f | -11.8677 | -49.2195 | 2025-11-14 03:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 408662f6-6fdd-35fa-a89a-915670a41f68 | -4.98232 | -43.88678 | 2025-11-14 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 54b15907-ac9a-3f8c-a9e1-4c5b63c41fef | -4.7004 | -46.45092 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b2fbc66f-9f98-3435-aba4-046b614ab821 | -6.48051 | -39.34256 | 2025-11-14 03:53:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f31b8af7-1d71-3197-96e8-58b160b80867 | -5.49448 | -42.16721 | 2025-11-14 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 212cdf5a-ba60-360e-ba24-678918bce991 | -7.93247 | -44.81212 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 546cbdb2-4232-36db-a708-35e00869bc11 | -6.0978 | -41.60664 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 13e967d3-ecc2-3103-bafc-e7532e7bb855 | -5.47089 | -41.39967 | 2025-11-14 03:53:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 377093b0-4db9-37e1-81c5-7b36b9020812 | -5.25658 | -46.1792 | 2025-11-14 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96f68e5c-a6c7-3028-be36-1a56ed0a51de | -6.5465 | -41.7093 | 2025-11-14 03:53:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5f70208d-ac41-3541-9152-ed34d2c2b427 | -6.10854 | -41.58658 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 90ba4009-a03f-3b4b-a751-ae554b431314 | -5.41469 | -43.26314 | 2025-11-14 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cc347718-66be-33b2-b746-4cb9e7b60f41 | -6.66849 | -43.49025 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a49f03a-30fd-3366-a3c3-b57f0f58356e | -5.72879 | -46.54584 | 2025-11-14 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb2a6faf-4647-35fc-b482-0d3833ed8dbf | -7.45254 | -42.56864 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 28c71008-b4b4-346c-801e-4a6c40e2bed6 | -7.85031 | -44.30009 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 96984756-b0db-33eb-8f07-f8a195aff78f | -6.28364 | -41.73281 | 2025-11-14 03:53:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fb28d8b9-a316-3403-9f17-588d6d4d84b4 | -6.90262 | -42.08224 | 2025-11-14 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8d80a20a-904e-329f-8f04-23feda1d2e7a | -6.24048 | -46.24511 | 2025-11-14 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fddf39eb-d708-3456-9d5c-32b4d10c547d | -6.1139 | -41.53013 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 51514ebf-f84f-35c9-b9ee-c692473951d6 | -7.37477 | -34.92539 | 2025-11-14 03:53:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e655b6fd-3422-389f-b42b-b50007469ad2 | -6.14707 | -43.70718 | 2025-11-14 03:53:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f4748b0-6ef6-38cc-87d2-c912cf3762c4 | -5.84516 | -47.68389 | 2025-11-14 03:53:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1c9a361-b3cf-35c7-9c1c-30071586f0ea | -7.5074 | -43.015 | 2025-11-14 03:53:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7f7b0ee2-dc53-3f3f-98cd-b04fefc0a227 | -5.41967 | -43.25636 | 2025-11-14 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 036ea4d0-508a-39a1-a03a-693dd0ea559a | -6.42747 | -47.30299 | 2025-11-14 03:53:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2522ff4e-e5a2-3cd8-ad58-900bd89dd55a | -6.89437 | -42.06262 | 2025-11-14 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5cb34ff8-5f9a-3f62-8586-15b3cdd6e4fe | -7.85228 | -44.28833 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e625658e-8ad9-3c44-b928-3d68000265f4 | -5.97445 | -42.59476 | 2025-11-14 03:53:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 55d0a795-ed39-3309-ba2f-8ee9dfef0013 | -7.4715 | -42.57183 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 85eaec7f-5282-33e1-a694-f135246e18d5 | -5.85595 | -47.5832 | 2025-11-14 03:53:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3577ad5-643a-381f-bd3c-2736974ccab5 | -6.07967 | -41.62586 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 53dd4b57-0c2f-3133-b86d-b91125e7edcb | -7.14849 | -46.29639 | 2025-11-14 03:53:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35699424-2385-3cc6-a4c9-5e0fdf822168 | -6.47308 | -48.37204 | 2025-11-14 03:53:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README14.md)
