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
| b139b25e-c03f-32ef-af27-4b71e68b1fdb | 3.1096 | -60.6512 | 2025-12-07 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| b97fc09d-0542-3aee-9a93-5e9cd5e645ac | 3.1097 | -60.6323 | 2025-12-07 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 310a9ca4-593d-357c-b874-58a9617ec519 | -20.200001 | -52.907799 | 2025-12-07 00:17:00 | METOP-B | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0b20e228-3287-3de9-8a52-733383b355a3 | -3.004 | -45.0965 | 2025-12-07 00:17:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8903811d-e00b-389b-96d6-55602ca92071 | -26.2082 | -51.5597 | 2025-12-07 00:17:00 | METOP-B | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 07de06ca-9a0f-310d-b05a-5d4816c04c6e | -7.0475 | -39.748299 | 2025-12-07 00:17:00 | METOP-B | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 813a2e26-7252-3bed-8f34-bd15993078b3 | -29.0886 | -50.610298 | 2025-12-07 00:17:00 | METOP-B | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 051c5ec6-663d-371f-9b1e-b1ba69396cf8 | -29.090599 | -50.621498 | 2025-12-07 00:17:00 | METOP-B | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c39bdadb-5372-3061-8672-e84b79195f57 | -26.2062 | -51.548401 | 2025-12-07 00:17:00 | METOP-B | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5fb5b070-a345-34d3-bb16-9570b0691c43 | -26.2159 | -51.546299 | 2025-12-07 00:17:00 | METOP-B | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8ea59ec2-84a8-313f-ad18-fb8dc7fb9b13 | -3.8631 | -40.653 | 2025-12-07 00:30:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 5f423e21-8c88-3c26-aa52-3b800ed14802 | -3.8633 | -40.6286 | 2025-12-07 00:30:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 68.7 |
| d233b1ed-444a-3582-9158-abecf3389b35 | -22.4602 | -49.8112 | 2025-12-07 00:30:00 | GOES-19 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.5 |
| 7ffabc2e-472e-3873-8046-57292e86b623 | -3.8631 | -40.653 | 2025-12-07 00:40:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 96046481-037e-34b7-b2f9-499d40f9a4c3 | -22.4602 | -49.8112 | 2025-12-07 00:40:00 | GOES-19 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.3 |
| b473156e-a5f2-30b1-8368-683b72618b28 | -3.8633 | -40.6286 | 2025-12-07 00:40:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 5c36e515-622b-3437-ab11-0c43e6eb5473 | -30.52728 | -51.70617 | 2025-12-07 00:45:00 | TERRA_M-M | CERRO GRANDE DO SUL | RIO GRANDE DO SUL | Brasil | 4305173 | 43 | 33 | nan | nan | nan | Pampa | 5.5 |
| 3fde38b8-c5c4-365f-a7e6-58aaccb1e171 | -30.52866 | -51.71713 | 2025-12-07 00:45:00 | TERRA_M-M | CERRO GRANDE DO SUL | RIO GRANDE DO SUL | Brasil | 4305173 | 43 | 33 | nan | nan | nan | Pampa | 5.8 |
| c7707402-67aa-3b64-9dc1-ace17caae987 | -29.48343 | -54.61918 | 2025-12-07 00:47:00 | TERRA_M-M | JAGUARI | RIO GRANDE DO SUL | Brasil | 4311106 | 43 | 33 | nan | nan | nan | Pampa | 11.9 |
| eca00216-8081-3b1c-b1e4-0f682a443a7c | -29.48499 | -54.63385 | 2025-12-07 00:47:00 | TERRA_M-M | JAGUARI | RIO GRANDE DO SUL | Brasil | 4311106 | 43 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| c3ecbfbe-423d-38a6-b38e-b84a0910c752 | -23.29007 | -47.08878 | 2025-12-07 00:47:00 | TERRA_M-M | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 620f715b-c859-36ee-a1b0-42bb01944270 | -29.0823 | -50.62796 | 2025-12-07 00:47:00 | TERRA_M-M | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 43.2 |
| 87590d78-45fa-30ed-9111-9b45fc194115 | -26.03392 | -51.74858 | 2025-12-07 00:47:00 | TERRA_M-M | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| a0101e14-4d4f-3a4c-ba79-083efd3fa0f9 | -21.95677 | -48.53571 | 2025-12-07 00:47:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e225aed5-fd9e-33a2-8c2e-f9723c014e85 | -21.95869 | -48.54775 | 2025-12-07 00:47:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d7b92fc5-9fdd-3b2d-8a5a-043d724e0e76 | -22.4524 | -49.8179 | 2025-12-07 00:47:00 | TERRA_M-M | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.0 |
| c237f3cd-7c97-3796-a5f7-72dafcb7bacf | -22.45397 | -49.82828 | 2025-12-07 00:47:00 | TERRA_M-M | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| c379a66e-10a9-3276-812a-4f22c2e12703 | -26.21125 | -51.56446 | 2025-12-07 00:47:00 | TERRA_M-M | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| e5425d67-ebde-3c2f-bce4-63c392b213b1 | -24.18197 | -49.60309 | 2025-12-07 00:47:00 | TERRA_M-M | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9990ac47-7188-3f8c-aad7-73659bf9e288 | -20.26304 | -50.66021 | 2025-12-07 00:49:00 | TERRA_M-M | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 702cc7fb-b4dd-39ad-80a8-2f0b301a2ef5 | -20.91369 | -56.36644 | 2025-12-07 00:49:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 10666d33-6add-3646-aa98-7eda4652a689 | -20.19739 | -52.92543 | 2025-12-07 00:49:00 | TERRA_M-M | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e166a663-dbbf-314c-8016-1171ed482c56 | -20.91524 | -56.3799 | 2025-12-07 00:49:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 16617d1e-041b-3f51-87f9-0dd086d37c09 | -22.4602 | -49.8112 | 2025-12-07 00:50:00 | GOES-19 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.9 |
| 768c9e4b-23b1-3668-a8be-fae573cee02c | -3.8631 | -40.653 | 2025-12-07 00:50:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 88.0 |
| 625dc3de-0dd5-308c-8528-f300dc20978e | -2.2993 | -48.5936 | 2025-12-07 00:50:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 7f89c2d7-d903-3090-99b8-eda99968bd1f | -3.8633 | -40.6286 | 2025-12-07 00:50:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 01e188f0-d9c7-322b-bbff-c5834c7b0d8a | 2.00588 | -55.68246 | 2025-12-07 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 50940ffc-6dcb-398a-9b89-62c1c3ebcf26 | 1.96458 | -55.71441 | 2025-12-07 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ec7a1eaa-7aec-3454-8418-db59c9be3824 | -0.96386 | -52.32888 | 2025-12-07 00:54:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7269761f-1757-3a6f-a0b4-638de42e01c7 | -1.96147 | -54.19574 | 2025-12-07 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| bc8142cb-b826-3173-b729-6fa960534636 | -2.43657 | -49.2291 | 2025-12-07 00:54:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| f3152133-18ad-3ebd-b231-a9a5a9188ae2 | 3.9776 | -51.67797 | 2025-12-07 00:54:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e684bb69-08c0-3013-aff1-99bc8634efd5 | -2.38669 | -56.05874 | 2025-12-07 00:54:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d3e848c9-e416-3e0f-b330-e49f2a277d5e | 1.96712 | -55.69588 | 2025-12-07 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1d54eb30-2e29-395a-a194-9f926fe4eb8e | 1.97617 | -55.6972 | 2025-12-07 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 67205197-2088-376e-89c8-aad5148c082d | 2.00459 | -55.69181 | 2025-12-07 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 46f6778f-fcc9-370c-9fd3-8843a7c92c0a | 1.73035 | -56.07894 | 2025-12-07 00:54:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 83dcf56b-fc07-305c-bf03-d2d248700ef3 | 1.97743 | -55.68799 | 2025-12-07 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e2f57c69-ac9d-3836-83a2-f08506bd2f98 | 1.96585 | -55.70515 | 2025-12-07 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 676af2af-3e00-3233-9dec-6dad9ae4af54 | -2.17856 | -53.5606 | 2025-12-07 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ea428383-4f41-3d1b-b1d7-156f923dfbef | -22.4602 | -49.8112 | 2025-12-07 01:00:00 | GOES-19 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.1 |
| b54fc9d8-be1d-3cc2-9f73-c396e5f9f220 | -2.751 | -51.5489 | 2025-12-07 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| f8deaa17-7080-3dbb-bd3a-2ea625ca17ed | -3.8631 | -40.653 | 2025-12-07 01:10:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 90.6 |
| ab133826-103b-34a6-bc2c-94c6dda85c7b | -3.8633 | -40.6286 | 2025-12-07 01:10:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 68.7 |
| f6d1554c-fa60-37e1-bac7-5f30e96cdaee | -22.4602 | -49.8112 | 2025-12-07 01:20:00 | GOES-19 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.0 |
| bcb82954-9e06-3f52-8cf9-e8e8248a8329 | -3.8631 | -40.653 | 2025-12-07 01:20:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 93.2 |
| abea8889-7fba-3cb9-9ae3-f1ef81394c71 | -3.8633 | -40.6286 | 2025-12-07 01:20:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 81.2 |
| a5e9ec73-a20b-31a8-aa57-373740a11c17 | -22.4602 | -49.8112 | 2025-12-07 01:30:00 | GOES-19 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.2 |
| 7c8a666b-984e-3806-8d51-6c78f01ed6b4 | -3.8631 | -40.653 | 2025-12-07 01:40:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 66.0 |
| d2838b7f-9d7f-3a34-b579-30c1c4d2db48 | -22.4602 | -49.8112 | 2025-12-07 01:40:00 | GOES-19 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.2 |
| 5209bc44-5907-3e4b-a530-b194547f8645 | -3.8631 | -40.653 | 2025-12-07 01:50:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 68.3 |
| f4615576-88b6-33f8-9c46-b37a0caa6058 | -22.4602 | -49.8112 | 2025-12-07 01:50:00 | GOES-19 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.9 |
| 8bf6410b-f4f8-3081-a840-a54fd9a35420 | -3.8631 | -40.653 | 2025-12-07 02:10:00 | GOES-19 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 66.7 |
| fd3de7d3-e1a4-3e48-a647-320d5b4baac3 | -4.94042 | -38.00049 | 2025-12-07 03:21:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c51da977-f3ad-3126-a2c1-787010fe2ccb | -3.56009 | -39.13991 | 2025-12-07 03:21:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 01b85f84-17ad-3530-a643-6bf106336b85 | -3.86254 | -40.64799 | 2025-12-07 03:21:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 42e373b4-9414-3257-b17d-8a9381d74b51 | -3.86521 | -40.64571 | 2025-12-07 03:21:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d3bee7d3-bccd-3409-97f3-45a6980ac9be | -3.56066 | -39.13644 | 2025-12-07 03:21:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ac2aa5a5-3ca8-32d3-b2d4-209878f0ae14 | -3.86329 | -40.6437 | 2025-12-07 03:21:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 11c2ef6a-2841-32ef-862d-283ba03c8dc8 | -3.85858 | -40.64894 | 2025-12-07 03:21:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1a578ab5-335a-3f43-97f5-56c3359203d7 | -3.8593 | -40.64464 | 2025-12-07 03:21:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9b69b271-8631-3f0d-b5cc-7c48a8e1deb2 | -3.86449 | -40.65002 | 2025-12-07 03:21:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5f6d6300-0031-3ece-8a58-f22d8bf1e4ec | -3.56246 | -39.13909 | 2025-12-07 03:21:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a5ff09be-6678-3c27-99f5-c2a8faa3a817 | -4.93788 | -38.00178 | 2025-12-07 03:21:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7c863051-a969-33c2-85e0-ccec4bc200e8 | -3.86593 | -40.64143 | 2025-12-07 03:21:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 84cddd3e-f392-3eff-8041-ab8646e357bd | -10.16235 | -36.20836 | 2025-12-07 03:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fdb81349-44b6-300a-a999-ec92f0518e2f | -6.53804 | -39.19847 | 2025-12-07 03:23:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9674ac9c-4f76-323b-ad75-38b7bb628e9b | -10.15913 | -36.20332 | 2025-12-07 03:23:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5373a4d2-74b8-32e1-85b7-4001d3b1d5dc | -8.36151 | -36.06806 | 2025-12-07 03:23:00 | NOAA-21 | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 51c85ad6-ea8c-3e89-86dd-b4f68b759f89 | -8.36223 | -36.06387 | 2025-12-07 03:23:00 | NOAA-21 | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d5d06eb9-05a4-34e2-aa44-20404b4f9395 | -6.8748 | -39.34813 | 2025-12-07 03:23:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dde7d80b-a654-3701-b176-48fa8d4d4a00 | -5.98126 | -36.41277 | 2025-12-07 03:23:00 | NOAA-21 | BODÓ | RIO GRANDE DO NORTE | Brasil | 2401651 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4037c326-9a61-39ee-a5d5-3cea250269be | -5.9791 | -36.41234 | 2025-12-07 03:23:00 | NOAA-21 | BODÓ | RIO GRANDE DO NORTE | Brasil | 2401651 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5b06a264-33cf-3b02-8de6-c07a04b8a299 | -6.53749 | -39.2016 | 2025-12-07 03:23:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3b4ca0d8-5d87-3502-8fd8-0b41d4747317 | -22.02627 | -45.93852 | 2025-12-07 03:27:00 | NOAA-21 | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 563cb56e-16c3-332d-a915-22a066087800 | -22.5893 | -48.67925 | 2025-12-07 03:27:00 | NOAA-21 | AREIÓPOLIS | SÃO PAULO | Brasil | 3503604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 07a0489b-b21d-32e0-ae13-bce9cac94687 | -23.29523 | -47.09521 | 2025-12-07 03:27:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 5c628933-b171-3874-8372-eb337ab24b4b | -20.72103 | -47.35008 | 2025-12-07 03:27:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d49d6922-60f9-360a-a504-728d8877616e | -23.29684 | -47.09398 | 2025-12-07 03:27:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| e00ed77c-fcd8-32a8-87f7-c3c058fe5d99 | -23.2908 | -47.09203 | 2025-12-07 03:27:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 71c4b23e-20d7-3050-ac0f-8748d1312493 | -22.02943 | -45.93931 | 2025-12-07 03:27:00 | NOAA-21 | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| dd11474b-eb2c-3286-8c3d-7f0822b9d75d | -20.72583 | -47.3497 | 2025-12-07 03:27:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a83bef65-b880-3ceb-9896-585496e494b3 | -20.7243 | -47.35597 | 2025-12-07 03:27:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3f84732-c90b-3a4b-b664-cc5b119511af | -23.28915 | -47.09345 | 2025-12-07 03:27:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 02b3d890-f866-32fc-a697-9b523bcfac2d | -29.08461 | -50.62689 | 2025-12-07 03:29:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 9e8d9ea6-33ad-372f-8ade-0e82f17d757a | -29.08212 | -50.62724 | 2025-12-07 03:29:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 0e871b86-96c4-3d96-ad84-02bdcad2d33f | -3.86403 | -40.64701 | 2025-12-07 03:51:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d7a18dd1-371d-3350-938a-aa96e4ce1dcc | -6.94338 | -37.90319 | 2025-12-07 03:51:00 | NPP-375D | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3288f997-6de0-3d0e-8483-0926ef06d619 | -6.53602 | -39.20138 | 2025-12-07 03:51:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |


[Clique aqui para ver as próximas entradas](README2.md)
