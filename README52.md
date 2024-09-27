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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b0d0aea-bd15-3cb5-b685-f89e16bb87c7 | -7.29628 | -43.38792 | 2024-09-27 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9192985c-2a90-3991-b1f8-af9e0a892e71 | -7.29618 | -43.31661 | 2024-09-27 03:47:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4d49ff0-6d62-3ac5-9db1-ce43843f3d14 | -7.29175 | -43.31583 | 2024-09-27 03:47:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df46274d-3111-3056-8ef0-9783169a145a | -7.27754 | -42.28821 | 2024-09-27 03:47:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9fd85aab-e6af-3089-9047-491b7b5dfb3d | -7.2755 | -42.28771 | 2024-09-27 03:47:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c39870d7-65d3-3c95-8eaa-cc2f15110cb7 | -6.87961 | -42.84663 | 2024-09-27 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| b76709b1-e732-3ec7-8e7c-64cb6afe0789 | -6.6881 | -43.51858 | 2024-09-27 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3212c934-233d-377d-b755-12a77cfef853 | -6.68357 | -43.51775 | 2024-09-27 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1fd1bf88-f331-3bff-a51d-f687b5066a77 | -6.643 | -42.08861 | 2024-09-27 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 57b318e3-085b-33ae-8ca3-98c1e27c538a | -6.55156 | -43.15561 | 2024-09-27 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 082cf06c-ff8c-3bba-a2d4-a7aa6a465b3c | -7.96341 | -42.85391 | 2024-09-27 03:47:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 34cd251b-5b29-35a5-ac56-c062970335e3 | -7.8683 | -42.70152 | 2024-09-27 03:47:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 69899a9b-6786-32ec-885e-275a275e41ef | -7.86544 | -42.693 | 2024-09-27 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dca21977-ae6d-342b-b437-2f49d49e9889 | -7.58574 | -42.28957 | 2024-09-27 03:47:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d7697269-58db-3948-b649-4c765d142fdb | -7.58513 | -42.29324 | 2024-09-27 03:47:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 00a4d10e-505c-3c0d-9766-158c335c0819 | -7.58164 | -42.28878 | 2024-09-27 03:47:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 209d2744-a65c-37d6-a346-f74843eec413 | -7.48422 | -43.71091 | 2024-09-27 03:47:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 65fb4f3d-8d27-3fec-9c15-919dcb88daf2 | -7.37077 | -43.32788 | 2024-09-27 03:47:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| faccac88-3fb8-36df-9006-0e1689e4b14a | -7.37002 | -43.33223 | 2024-09-27 03:47:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fb34a49-3437-3759-940f-12c72d5f8f09 | -7.30074 | -43.38865 | 2024-09-27 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57d12139-65a3-347f-9a15-8a033df71972 | -7.29761 | -43.38959 | 2024-09-27 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8fc5e13-228f-325c-b45d-27f91d22bdab | -7.27692 | -42.29196 | 2024-09-27 03:47:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2cb8a8b4-46f7-3066-b808-4365ad3306f8 | -7.12751 | -42.51495 | 2024-09-27 03:47:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 20e21856-3a30-31d2-bf22-ae352ca0bd31 | -6.78009 | -42.97839 | 2024-09-27 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bc3865bc-17a0-3e22-9566-0f841dff3fbf | -6.66515 | -42.58383 | 2024-09-27 03:47:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9b2f1a5a-cb5b-30e1-ac66-73e626021da0 | -6.6609 | -42.58307 | 2024-09-27 03:47:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e3ad38ae-3794-379b-84eb-a7562ca54c2d | -6.64711 | -42.08939 | 2024-09-27 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 10143dfa-85e1-381a-8bea-348a091a2eb4 | -6.64238 | -42.09232 | 2024-09-27 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 51c1200c-e2ca-3a35-ba82-266501d06a25 | -6.55599 | -43.15641 | 2024-09-27 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a6a7dbc8-3779-3424-b936-88de6e711a59 | -8.07328 | -42.89736 | 2024-09-27 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8c990ea3-b019-3323-bed1-1bc801712d6b | -8.06833 | -42.9007 | 2024-09-27 03:47:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e973da23-5c15-3142-aeac-08cf82d62534 | -8.07259 | -42.90139 | 2024-09-27 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 453037d4-42aa-3372-8640-c899c77c4a03 | -8.07111 | -42.8846 | 2024-09-27 03:47:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2080720f-6875-30b1-b7c5-1c855d3021c8 | -8.07042 | -42.88858 | 2024-09-27 03:47:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7a0bcc6b-3712-36a3-be56-03d070ed33d1 | -8.06405 | -42.9001 | 2024-09-27 03:47:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4f82f481-748e-37be-9c8d-cc81f152c2ef | -3.48443 | -43.3609 | 2024-09-27 03:47:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b2903e37-348b-3f9f-9f8b-7af5b302efe1 | -3.25552 | -43.05918 | 2024-09-27 03:47:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c3eca3e-7c74-3f72-b14a-d017ed3f56d7 | -3.2531 | -43.05613 | 2024-09-27 03:47:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5306ba8c-8afc-39f7-858f-45d0d89abc4f | -3.25232 | -43.06104 | 2024-09-27 03:47:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e5369a5e-8007-3701-8ea0-1097bbae7166 | -3.25168 | -43.05356 | 2024-09-27 03:47:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff478f00-dd08-3fa1-a8d2-4f7d04bfb38c | -3.25086 | -43.05846 | 2024-09-27 03:47:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 28f9b05a-b7a1-3b0f-aab5-def607872f81 | -3.24844 | -43.05539 | 2024-09-27 03:47:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5cde45a3-f250-36fd-beac-88ff32fdb8ac | -3.35349 | -44.19086 | 2024-09-27 03:47:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6f41611-5bb1-345e-a1ad-a355e913cceb | -3.35302 | -44.19373 | 2024-09-27 03:47:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e75ba81c-9fcd-32e9-bf0f-1745d68c0846 | -5.02216 | -43.80076 | 2024-09-27 03:47:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 88795b79-e579-3a5a-9669-acef16aa2a4e | -5.01828 | -43.79473 | 2024-09-27 03:47:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 35fdc699-d2f8-3902-a745-a45ed0978b7e | -4.82667 | -43.70655 | 2024-09-27 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9eb8c72d-f17c-3908-809b-28124863d4f7 | -4.78613 | -43.71534 | 2024-09-27 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f24b5f53-f3a1-3245-a020-641a66c34b40 | -4.78137 | -43.71456 | 2024-09-27 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8827da39-bc1b-3ea1-86fc-af281370cd40 | -4.78051 | -43.71963 | 2024-09-27 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3c863678-a72c-3b72-a9ad-ca5de4bea2e3 | -4.66049 | -43.76104 | 2024-09-27 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d18f43e7-487e-3f9f-8582-07345712f8ac | -4.66032 | -43.81988 | 2024-09-27 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0fbbb41a-d28d-3fa0-acda-a17d95a814a1 | -4.65961 | -43.76622 | 2024-09-27 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2bdd011-1355-3c38-acf1-4ae93cc8bb23 | -4.65571 | -43.7603 | 2024-09-27 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f3b08dac-be61-3938-a1a8-a487f9decd65 | -4.54317 | -43.57967 | 2024-09-27 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3f1b298-85b8-3819-ba81-46b8a046e84a | -4.03895 | -43.24367 | 2024-09-27 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e5fe910-4ba8-3b43-b0b3-06da685717fd | -4.0343 | -43.24287 | 2024-09-27 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 012cde94-5967-3420-8dc5-adbb97f1e65f | -4.02965 | -43.24209 | 2024-09-27 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23c7c8ba-c465-3554-addf-125509c4bd84 | -4.02499 | -43.2413 | 2024-09-27 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2437b93e-6de8-3aaa-852c-ea436a9eea04 | -4.06039 | -44.05209 | 2024-09-27 03:47:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8628ea42-a443-3b40-aace-cce351c2b2a0 | -4.05904 | -44.05065 | 2024-09-27 03:47:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5f1f85de-649e-3cfc-9891-e882759ed0bc | -4.05813 | -44.05624 | 2024-09-27 03:47:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 707cc45e-6786-3406-8fa6-99890845387f | -4.05546 | -44.05129 | 2024-09-27 03:47:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| eb561c5c-427c-368e-8a92-4aee3392c3f3 | -3.21571 | -46.78542 | 2024-09-27 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 495be460-95b7-3c65-aa3e-c68559a25219 | -6.94005 | -39.42283 | 2024-09-27 03:47:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b99b756f-0dd5-3ac5-84a5-5e604452d54f | -7.00104 | -35.19955 | 2024-09-27 03:47:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 861abe57-31bb-3e81-93fc-5b12df423dc4 | -7.00047 | -35.20319 | 2024-09-27 03:47:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| cf60d4d3-ff67-3a39-8474-85e89a613a89 | -6.99709 | -35.20268 | 2024-09-27 03:47:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 20cb7057-967f-3da9-9db9-42664e4bc18f | -6.63341 | -35.04353 | 2024-09-27 03:47:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3578db9e-4c2d-3e52-8bd8-262c4c571578 | -4.81488 | -37.80826 | 2024-09-27 03:47:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e0b861c0-c997-37af-b878-326cba7496ad | -4.70539 | -37.79087 | 2024-09-27 03:47:00 | NOAA-20 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 44bd3b1f-ce84-316d-93b9-f846160109ef | -4.70085 | -37.79757 | 2024-09-27 03:47:00 | NOAA-20 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 636cebcb-f92b-3922-8503-2609053569f3 | -5.15253 | -37.73499 | 2024-09-27 03:47:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7a2b3874-1a28-3b3f-9666-fb9d0d122864 | -8.12551 | -38.64308 | 2024-09-27 03:47:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fca7626c-0430-3a64-a056-fce8da860bb2 | -4.33025 | -39.1379 | 2024-09-27 03:47:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 02be50d4-f37b-35d5-b2ee-c87e0c517fae | -4.32667 | -39.13734 | 2024-09-27 03:47:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bd95a4aa-339f-30ef-826f-20319ccc2a88 | -4.326 | -39.14142 | 2024-09-27 03:47:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1820d7b3-63d8-3221-b10a-e15e5f75a8a7 | -6.0995 | -39.68558 | 2024-09-27 03:47:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| faf9f4a7-4796-34b8-8bef-d7cffd4dc370 | -6.6121 | -39.59153 | 2024-09-27 03:47:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 434a5a6b-1535-3d84-a002-577208cc72ce | -6.60853 | -39.59101 | 2024-09-27 03:47:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9aa3eff1-eb02-3247-8c6e-b2673ce393de | -7.24655 | -39.85881 | 2024-09-27 03:47:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 80ab4cb5-d0c3-3f27-b58e-a8b71997b95c | -6.94357 | -39.42339 | 2024-09-27 03:47:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| adfcfb18-41a0-3ab1-8a01-e18a8c134d7f | -6.94292 | -39.42741 | 2024-09-27 03:47:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e709dad8-7535-3b23-9abe-72a1c62ce2d6 | -6.9407 | -39.4188 | 2024-09-27 03:47:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| febd0ab8-0060-31cf-afc9-1d8976b93b79 | -6.61927 | -39.59245 | 2024-09-27 03:47:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1638f203-e1b8-3f6e-9c93-5c167e2b98a0 | -6.61568 | -39.592 | 2024-09-27 03:47:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2ac1143f-e0f5-32c4-a0fb-1865a914b12c | -6.60919 | -39.58689 | 2024-09-27 03:47:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3ebd321e-454f-3a93-acf3-d026160db474 | -9.24919 | -40.19657 | 2024-09-27 03:47:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 24a57f05-7602-3341-bf14-330c868ed0d6 | -8.78881 | -40.3608 | 2024-09-27 03:47:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3f769365-899b-3f4b-bae1-d9e437c26720 | -9.25122 | -40.19905 | 2024-09-27 03:47:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4fe2e943-3a77-32da-a025-ceeeadcbe140 | -9.16378 | -40.53756 | 2024-09-27 03:47:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 0230edfc-858e-341a-980a-8ae9fd3a1e6a | -8.99536 | -40.4207 | 2024-09-27 03:47:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 508ba685-a20f-316b-99ef-53d45a7d9dff | -8.78757 | -40.36211 | 2024-09-27 03:47:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9d3b3e4b-561e-3dc6-ad06-61b3d67045b9 | -8.47719 | -40.51864 | 2024-09-27 03:47:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dae11718-c28c-387d-a0a6-f11f62ed7cb3 | -9.49507 | -40.86632 | 2024-09-27 03:47:00 | NOAA-20 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| d88b455a-4357-3235-ab5e-afa72d563ba6 | -9.42927 | -40.31263 | 2024-09-27 03:47:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0279fa17-e9e0-3d42-b870-dab4cae0128b | -4.13888 | -40.25699 | 2024-09-27 03:47:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e7a7cbd0-f2e8-3f2b-9cf5-5a5104d61349 | -4.1357 | -40.25855 | 2024-09-27 03:47:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6dc612fd-6b23-38ce-8416-4c5dfde99360 | -5.65769 | -41.73767 | 2024-09-27 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c76ee793-cf26-391d-97cd-d9793d915773 | -5.65101 | -41.25045 | 2024-09-27 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |


[Clique aqui para ver as próximas entradas](README53.md)
