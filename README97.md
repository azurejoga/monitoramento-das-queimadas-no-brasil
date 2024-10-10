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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9d68a69-03e1-3a39-aacd-3aa916010788 | -6.42044 | -44.43245 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eea7d948-8be9-3f24-a46d-8e5bb6fd6eda | -6.36123 | -44.55815 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af163bc2-454e-32db-897b-28f7fcb992de | -6.36059 | -44.56257 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d7e0027-423b-396f-94e3-d05f8bef13d7 | -6.35618 | -44.56184 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fabd3c8f-cc8e-3f23-a8af-5aab423c166e | -6.28893 | -44.56327 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39e1d616-2470-320e-8ee6-1152d2b532c6 | -6.28831 | -44.56742 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56508487-c5b2-3bb2-875f-42136b9a209b | -6.26074 | -44.179 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2809408-3b29-329c-91d0-74dbadcd8779 | -6.21575 | -44.10594 | 2024-10-10 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ddc93f12-3da0-3949-97a1-78006fcbe917 | -6.21473 | -44.20878 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea72ee0a-cbaf-3d6c-aa43-0b8baf236478 | -6.19299 | -45.03474 | 2024-10-10 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25785355-727a-39ef-9c61-2a9c5b15ea12 | -6.18923 | -44.38348 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c52b5b01-867d-363a-8d86-fe1aeb9a05d6 | -6.18814 | -45.03807 | 2024-10-10 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd5ba5e3-e6cf-3a1b-ad26-157df71c75cc | -6.18477 | -44.38278 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ab7933d-1246-3ba2-92dd-9640217fede8 | -6.17941 | -44.45068 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffd738af-5488-3b2e-8f3c-a79b57aca899 | -6.1695 | -44.10421 | 2024-10-10 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abefc5c5-1165-3678-ad8d-294d8ec5f085 | -6.07536 | -44.64155 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5473fd91-0dc4-33c1-8cf3-d2d05da669c1 | -6.07481 | -44.64308 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 01a3fed5-7f3b-38ad-88ca-bda04d65bec7 | -6.07477 | -44.64573 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6ed090e-bade-31e8-9d8b-ce270f40f653 | -6.07039 | -44.6451 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a5012e9-439f-39c9-a7da-973448ade37c | -6.06981 | -44.64663 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22e04091-2f6e-32b3-86df-aa1b10467053 | -6.06542 | -44.64603 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bb11862d-df5d-30b0-98b9-6bb9ab0d20fe | -6.06539 | -44.70625 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c5f9047-7365-379b-8212-1a8575513360 | -6.06479 | -44.65026 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 998c2a52-6e57-3e86-b154-df3afc185cba | -6.03887 | -44.23492 | 2024-10-10 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 985e2fb6-e454-3377-990f-8179a37c2620 | -5.95122 | -44.85123 | 2024-10-10 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 459a3d13-cb31-3013-868d-8725b281b3ae | -5.94919 | -44.7412 | 2024-10-10 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2473861b-24e7-3e89-bdbc-dfc73af6d506 | -5.94757 | -44.74182 | 2024-10-10 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93dbf94f-a25e-3e3f-be45-a4298f403fe5 | -5.93313 | -44.5368 | 2024-10-10 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b5683d8-a809-3f09-8cfc-6512ce0a1ebe | -5.92872 | -44.53618 | 2024-10-10 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b22f4225-1243-301e-b6fe-65c4a907cb88 | -5.70254 | -44.78927 | 2024-10-10 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 994b44fa-aa8d-3048-923d-d61a0d050e79 | -5.63818 | -44.08895 | 2024-10-10 04:44:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e66a73f2-8627-39e7-96e0-f68baffcb553 | -5.58175 | -44.87669 | 2024-10-10 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc0a1e0b-c30d-3ee9-aeab-95cb4b79e17d | -5.49328 | -44.2842 | 2024-10-10 04:44:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e7d2fe9-ba68-3d9e-ad62-751fca6293d9 | -5.49265 | -44.28859 | 2024-10-10 04:44:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eed0767e-a624-375d-b1ad-054fd9d05969 | -5.4906 | -44.28129 | 2024-10-10 04:44:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6cedabc3-b495-3bfa-9a2a-3429ae1d320e | -5.48993 | -44.28569 | 2024-10-10 04:44:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05b52001-2ce3-3689-98a5-040bce64dd08 | -5.48929 | -44.53044 | 2024-10-10 04:44:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ae4e227-14b3-3017-a0e8-099a8bc6895f | -5.48928 | -44.29006 | 2024-10-10 04:44:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 564d6cd1-bd37-389a-9a64-e2b10a4d3da0 | -5.48882 | -44.28358 | 2024-10-10 04:44:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef3433fb-48dd-38dd-8e1f-82a47dc3684c | -5.48868 | -44.53468 | 2024-10-10 04:44:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e48308b-2e5e-35a3-8f7f-e456eae57fc3 | -5.48374 | -44.28735 | 2024-10-10 04:44:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36876e42-fb01-357b-b8af-d8dc8ef46806 | -5.48103 | -44.28442 | 2024-10-10 04:44:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9635fc6e-c3ff-34fd-add6-00f684e2032a | -5.47991 | -44.28228 | 2024-10-10 04:44:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 862887cb-f656-32c0-919a-499df5efb8d4 | -5.47659 | -44.28374 | 2024-10-10 04:44:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f6ca277-a4b9-3709-92fe-2a75be032bb4 | -5.47547 | -44.28159 | 2024-10-10 04:44:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 782af302-30eb-3fcb-873b-bc3ea37351b4 | -5.47484 | -44.28601 | 2024-10-10 04:44:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac9d2d64-bbb4-398e-af12-f252a4b383c4 | -5.3269 | -44.84457 | 2024-10-10 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bb16dc9-b357-3472-945f-31030e8a070a | -5.32633 | -44.84851 | 2024-10-10 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f499523e-bc7b-3930-84f8-f717922ce360 | -5.27012 | -44.21056 | 2024-10-10 04:44:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 662197a8-9b3d-32e0-a0eb-3b19c0eb3cb1 | -5.26666 | -44.60808 | 2024-10-10 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cf14ded-b6d5-3c84-bda3-f16064c50c7d | -5.23906 | -44.79605 | 2024-10-10 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a2b17784-538b-336d-9873-f5bfd97bb11d | -5.23849 | -44.79997 | 2024-10-10 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 0ce87ad2-b3ad-32f5-8b19-2ba6b678de06 | -5.23421 | -44.79934 | 2024-10-10 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b29aa5e7-3a1a-31bf-bbeb-bbb18b9df107 | -5.22993 | -44.79868 | 2024-10-10 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f73dc104-3125-373f-9849-b5d06069c676 | -7.61183 | -44.85419 | 2024-10-10 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eab06740-72cf-318a-9882-fcf22d460946 | -7.61121 | -44.85854 | 2024-10-10 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1f1bc44-d94f-38a0-b5c9-3b650343e7c3 | -7.61059 | -44.86288 | 2024-10-10 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5cae6017-ba26-3b65-961a-214898408af7 | -7.20436 | -44.00067 | 2024-10-10 04:44:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f001553-2e85-3a44-8b50-0cb69e198c7e | -7.20367 | -44.00554 | 2024-10-10 04:44:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ec40a4e-e9f3-3ae5-9ff2-b2603a120e8f | -6.9288 | -44.06018 | 2024-10-10 04:44:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 502ba4eb-6676-337c-844c-11ef15b29cb7 | -7.6301 | -45.2672 | 2024-10-10 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1cc722f-9820-3f29-a3a5-645aefe3260f | -7.6295 | -45.27144 | 2024-10-10 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4f12879d-b02c-341b-a579-9ce811ab0d56 | -7.62522 | -45.27074 | 2024-10-10 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c54c78a2-4f02-3a70-bb14-be61ef696baa | -7.30794 | -44.96874 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2c53559b-e88e-3c7e-b7e5-f59dd0ee3417 | -7.30731 | -44.97307 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 568b88ab-63c1-3fbf-974b-38f50432428c | -7.30669 | -44.97736 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 34d3709a-bf35-3235-aba8-1fae56b83663 | -7.30607 | -44.98161 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 36ed3b51-ddc9-3592-bc75-384c26be1be4 | -7.30294 | -44.97252 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 80fe2cb8-0c31-3a29-90a0-680543114702 | -7.30232 | -44.9768 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f139d66e-72bf-3345-a8cf-1aed349a36c9 | -7.3017 | -44.98101 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2584a5b5-11e5-3e02-8231-ef4ff7442102 | -7.29795 | -44.97622 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6a99c2a3-b82b-30e2-bb53-45d3d1b42bc4 | -7.29734 | -44.98041 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2ff06cf5-7ecf-357d-94a1-64816cebe1c2 | -7.19866 | -45.0383 | 2024-10-10 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f4b9c3c-6cfb-3a74-9983-635b338f10ea | -7.08968 | -44.67589 | 2024-10-10 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c93341a4-98c5-341f-8c2c-84f1b921e2a6 | -7.08905 | -44.68032 | 2024-10-10 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b8a1857-5517-3c96-afd2-b8d2ad989be4 | -7.04475 | -44.80207 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c36bd55-5b8d-3bce-aa38-79e3b465d026 | -6.94187 | -44.61513 | 2024-10-10 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f558b1f-98ce-3a00-b9a3-9972a5aa6d7f | -6.94099 | -44.61204 | 2024-10-10 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 779a5941-939c-33ff-b535-a9a4b1c2cf38 | -6.94038 | -44.61643 | 2024-10-10 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdeace38-ff3e-353f-8810-e2a8e397c05f | -6.94037 | -44.84075 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a5050e13-023b-3784-8f67-f34d755ce0f6 | -6.9374 | -44.61464 | 2024-10-10 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe0c39f0-7e02-3393-b480-b9ac6e57fe25 | -6.93651 | -44.61161 | 2024-10-10 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a61d6aaf-487d-3e14-8ce5-3ab56cb2e379 | -7.62892 | -45.27561 | 2024-10-10 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1644433c-2f5c-3be3-8742-8ce9a4e5fed6 | -6.64637 | -43.87367 | 2024-10-10 04:44:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7aca7f4-d988-3091-bfca-6df37252497e | -6.64203 | -43.80248 | 2024-10-10 04:44:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a4a46ac-0ca2-3903-9d49-e15d36401645 | -6.64007 | -43.80031 | 2024-10-10 04:44:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09ba5e9b-aed2-320e-b69c-cf35647c8727 | -6.63732 | -43.80198 | 2024-10-10 04:44:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0c729a3-4a43-394d-bd59-b2c376a99a7e | -6.62166 | -43.76252 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbc1407e-4243-3a4b-8ddb-5644e0dac495 | -6.61696 | -43.76188 | 2024-10-10 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a50cc1a8-eb2c-3cdf-9ccb-4a54b3d79cb7 | -6.72898 | -44.56542 | 2024-10-10 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f3ac884-549c-3974-bab0-3a104754fe1e | -6.72794 | -44.5632 | 2024-10-10 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2999c12-fded-3987-99d7-35966b7f414b | -6.52611 | -44.57078 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4ad2581-d4e0-319f-b56e-a7ccfb9e6adc | -6.52544 | -44.56874 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 108398bd-3ead-3ec4-8dd5-c5be97421239 | -6.52168 | -44.57016 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5cd383c-1f57-3b8b-9271-2bb836bce10a | -6.521 | -44.56812 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30691d9d-1a5d-3a26-a20b-a67c7ca7e338 | -6.50963 | -44.341 | 2024-10-10 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fb60e4c2-3dbe-3256-943c-1a977ecb548a | -6.50899 | -44.34542 | 2024-10-10 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f95da7e-0cfb-3a57-a17b-7baf84bc919d | -6.50804 | -44.69228 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f553ddd5-e6a4-39f7-a0ea-e4e63f1824f7 | -6.50769 | -44.69479 | 2024-10-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d560fecd-7e5b-3f4c-bed1-ba1875c2f5e6 | -8.35966 | -44.12655 | 2024-10-10 04:44:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README98.md)
