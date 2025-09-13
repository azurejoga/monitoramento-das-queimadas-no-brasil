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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7747fc5-4688-35d8-b2f3-ebbf150f8a7e | -17.54135 | -44.54762 | 2025-09-13 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f73245d3-867a-3423-9bce-d6c676ced3fe | -16.86495 | -49.36328 | 2025-09-13 04:10:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c797db61-9e4f-3f9e-b549-5b602ead15e5 | -15.7716 | -53.49309 | 2025-09-13 04:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5739c67-6c49-30a1-984f-7a80720a9ca1 | -17.34654 | -42.63741 | 2025-09-13 04:10:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1e79dc4-ab32-3b9b-8449-f8afa5849436 | -15.37559 | -52.10761 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c0de4fa4-08a6-3081-8378-2353c73e9711 | -21.61906 | -46.81839 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 3b3b3fae-0458-31a3-826d-5b5ca5854a91 | -20.29504 | -46.58766 | 2025-09-13 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a511383-c5c2-39a9-9ff0-d385d76fbcb7 | -20.28693 | -46.59421 | 2025-09-13 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e6df0cb-8f80-3c2d-b1e8-b998f5cb4d78 | -16.08438 | -49.96263 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 684e5fb7-ba3c-3b25-a0fb-18407d530b86 | -18.61457 | -48.20551 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04fd842d-477f-3a7f-ad17-44254f3706e0 | -20.08389 | -46.94201 | 2025-09-13 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29a77dfc-d900-3fad-bc64-bfbcd73a9016 | -15.59215 | -54.75513 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e253b585-acd1-3039-be7e-74f6021f1c73 | -16.4972 | -55.11697 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 4d80e8e7-db6e-3690-b8a5-5f09484cae3e | -16.53212 | -51.7423 | 2025-09-13 04:10:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28f12514-8908-334c-9fff-2798eb7659d7 | -18.44993 | -47.1962 | 2025-09-13 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 724f9868-4458-33c1-bee6-a82752b9d05c | -20.01761 | -47.64342 | 2025-09-13 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbde6e48-34c2-37fd-ba74-86763311cab2 | -20.34117 | -46.66813 | 2025-09-13 04:10:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4014cd7-a5da-37b1-9064-a99523630a15 | -17.28019 | -46.09541 | 2025-09-13 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ce8e0e0-aeeb-3b90-b1a9-d002dfee63f0 | -17.41251 | -48.21902 | 2025-09-13 04:10:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7caf2063-5d9e-3bd7-93c9-f4cdcd6b8079 | -17.55072 | -44.55294 | 2025-09-13 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ae75cef-0812-3bd6-a631-dcba4da5ee0e | -20.44739 | -46.45163 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4de854a5-11cb-31de-b563-dee225b160f4 | -20.09 | -46.90617 | 2025-09-13 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fc91873-0532-36b4-a9d6-7d9498d8d2bf | -16.50309 | -55.11825 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| e2fd845f-e5ff-3f73-a4ac-3bc0e740ba3d | -16.25882 | -50.07539 | 2025-09-13 04:10:00 | NOAA-20 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef20c518-d65d-34a1-a3bd-29eb255e260d | -17.28234 | -46.10363 | 2025-09-13 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6da06573-7bda-32c9-bc33-0ea4bcaced52 | -15.12946 | -52.48582 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4999d560-ba67-3b9f-8794-dc40f85d5a12 | -20.33841 | -46.66369 | 2025-09-13 04:10:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bee4becf-4d1d-39e3-8147-18c23e8444b2 | -15.15896 | -50.16071 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59daca04-a1b5-3a39-8515-8b5aa4b77774 | -17.43855 | -49.24908 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c137e339-8e2b-359e-9895-0a08cf360d1d | -20.41305 | -45.51493 | 2025-09-13 04:10:00 | NOAA-20 | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d29960ad-84ac-39b8-93fa-68a18bd79e6e | -20.10519 | -46.92118 | 2025-09-13 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 350ac497-3603-3549-9c61-892dbec3b02a | -15.07366 | -52.48971 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bb2603b-581c-30a0-933c-70db9ada0d51 | -15.10005 | -50.18193 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb3c859b-ad77-3ba8-8264-11df5c53875c | -16.08361 | -49.96678 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1ce5e5dd-9025-37f6-8c72-e60af30002a4 | -18.97455 | -48.60191 | 2025-09-13 04:10:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a65da2d5-3747-3e8d-bb61-6ba7d40c0c88 | -20.09619 | -46.9115 | 2025-09-13 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9296b5dc-afe9-3a50-aca8-aec5b9e362a6 | -16.64292 | -49.76915 | 2025-09-13 04:10:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8a59a2e4-007f-3fa2-b99b-c6b137b35a56 | -20.29034 | -46.59482 | 2025-09-13 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 96573c8b-b3ec-37e4-83f1-a08d3653e331 | -17.41195 | -49.25866 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0823d3c1-a3a7-3d26-b3fb-3eaf1c8b5b67 | -23.31932 | -51.39216 | 2025-09-13 04:12:00 | NOAA-20 | ROLÂNDIA | PARANÁ | Brasil | 4122404 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 226edd67-df66-3140-b37a-2accd10a87ed | -23.70096 | -51.78523 | 2025-09-13 04:12:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 38.8 |
| ef4de885-4bf2-36f3-844e-a6ceff34ead7 | -22.65524 | -53.1082 | 2025-09-13 04:12:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 7f025245-acc1-35e6-963d-8529889cbda2 | -22.66691 | -53.12198 | 2025-09-13 04:12:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b7372e41-6493-38cb-a7e2-df0f519c11b2 | -25.04564 | -49.22038 | 2025-09-13 04:12:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7e4e908e-b100-3983-af79-4f5845647db7 | -22.26364 | -56.80723 | 2025-09-13 04:12:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10d62ae8-c967-3a0d-85af-95729eb8bea6 | -28.45222 | -48.78014 | 2025-09-13 04:12:00 | NOAA-20 | LAGUNA | SANTA CATARINA | Brasil | 4209409 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7a737524-58ff-34c7-9f23-9afdfb678dc4 | -23.27715 | -47.52521 | 2025-09-13 04:12:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| c7eb0a28-e185-3605-8a2d-781996468350 | -25.51685 | -49.10837 | 2025-09-13 04:12:00 | NOAA-20 | SÃO JOSÉ DOS PINHAIS | PARANÁ | Brasil | 4125506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8bf8087b-458c-3eae-8fbd-35522293b6b8 | -23.14158 | -49.65727 | 2025-09-13 04:12:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a5824424-32bd-3f25-8143-78b739d2e086 | -23.27784 | -47.52118 | 2025-09-13 04:12:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 65fe232e-2bb5-37f6-b7b4-c13137acbd71 | -23.13868 | -49.65192 | 2025-09-13 04:12:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 24a99be8-49f3-395e-9d51-4c583ff9a665 | -23.61585 | -51.37789 | 2025-09-13 04:12:00 | NOAA-20 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d94625e1-d1f7-3642-8679-75bd190b0d48 | -23.23141 | -51.00043 | 2025-09-13 04:12:00 | NOAA-20 | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ad11b01a-621a-3d2b-a4cc-ee73597016f1 | -25.05377 | -52.08781 | 2025-09-13 04:12:00 | NOAA-20 | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7151b711-55dc-32d8-83fa-36a8a4809a25 | -22.26941 | -56.80883 | 2025-09-13 04:12:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fedeea7-5aa6-38f3-a3c6-855464a12d0b | -22.57154 | -53.03148 | 2025-09-13 04:12:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d94e4fa2-35f6-38fb-bae7-2173457fecfe | -23.61178 | -51.37693 | 2025-09-13 04:12:00 | NOAA-20 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| d5a6a4a5-951d-39f4-8b33-50f5c92fc06b | -23.34301 | -47.19765 | 2025-09-13 04:12:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 34816614-c9d8-3d1c-8c60-17124c2233ed | -23.23215 | -50.99657 | 2025-09-13 04:12:00 | NOAA-20 | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1b8b7059-54cb-3c7d-b91a-9ac4a47be41b | -25.0421 | -49.21947 | 2025-09-13 04:12:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6b1197c3-5ee4-3068-8e42-b274cfe363e1 | -23.34366 | -47.19376 | 2025-09-13 04:12:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b72ec927-9820-3378-8908-37e41b41a122 | -23.61023 | -51.38475 | 2025-09-13 04:12:00 | NOAA-20 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c82a3254-a820-3100-8d0c-2a9cb453e031 | -28.239 | -49.99694 | 2025-09-13 04:12:00 | NOAA-20 | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8824a358-1643-36c5-84b6-313fb4ada376 | -23.69928 | -51.79375 | 2025-09-13 04:12:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 9e55978d-6455-352e-aed0-8848f73993d6 | -23.7043 | -51.79045 | 2025-09-13 04:12:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 50c75d2f-637b-3f5d-ba58-2919232252a9 | -23.14246 | -49.65247 | 2025-09-13 04:12:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 43790717-7443-315a-a17c-49e69af359da | -22.65877 | -53.11452 | 2025-09-13 04:12:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 7e502b37-2189-3292-988e-f27e136e394e | -25.18306 | -48.99998 | 2025-09-13 04:12:00 | NOAA-20 | BOCAIÚVA DO SUL | PARANÁ | Brasil | 4103107 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ccb7bab8-f0a6-3780-be6a-e8131c4e4899 | -23.23254 | -50.9958 | 2025-09-13 04:12:00 | NOAA-20 | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 78254f2e-303b-392e-bdd2-b3809896d507 | -23.61509 | -51.38176 | 2025-09-13 04:12:00 | NOAA-20 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 35006066-ef76-3dc5-a426-b32418fb14dd | -23.1378 | -49.65672 | 2025-09-13 04:12:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0210169b-ad29-365e-9c58-8bc9d7e93774 | -23.45816 | -47.34942 | 2025-09-13 04:12:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 44d1de02-2d27-3b9c-8bbf-107bb66ec4be | -22.66231 | -53.12085 | 2025-09-13 04:12:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8c75962f-3393-3cf6-b01c-8ab193e78511 | -27.02293 | -49.63625 | 2025-09-13 04:12:00 | NOAA-20 | PRESIDENTE GETÚLIO | SANTA CATARINA | Brasil | 4214003 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bd21cb3c-c20c-30dd-9ab3-2ccd65882b6c | -23.34639 | -47.19833 | 2025-09-13 04:12:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| f71524ba-84dd-38f4-a984-9ae28c2f5f6a | -23.22776 | -50.99879 | 2025-09-13 04:12:00 | NOAA-20 | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 27bcdf8f-360f-3f90-ba21-a7bafb98adf7 | -27.10919 | -50.58307 | 2025-09-13 04:12:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 60c001d5-086f-333b-8349-dcec4f14a32d | -26.04441 | -50.495 | 2025-09-13 04:12:00 | NOAA-20 | CANOINHAS | SANTA CATARINA | Brasil | 4203808 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 62a614d2-0e13-3b2f-8101-a2618f5db422 | -23.61101 | -51.38084 | 2025-09-13 04:12:00 | NOAA-20 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 353bef2a-fefa-36a8-820c-95b13ba9ad0c | -23.70013 | -51.78944 | 2025-09-13 04:12:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 38.8 |
| 51fdde0e-b564-3dc4-a5ff-dcc82701c39c | -24.67879 | -51.04097 | 2025-09-13 04:12:00 | NOAA-20 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a2de0b01-9f41-3a60-9f39-9496687119f9 | -23.34704 | -47.19442 | 2025-09-13 04:12:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| fa68549b-bfcd-3831-b4f3-500e0c98f84e | -23.51856 | -47.61242 | 2025-09-13 04:12:00 | NOAA-20 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ab3338a3-6187-3173-84c3-861cace0f76d | -23.81091 | -50.08777 | 2025-09-13 04:12:00 | NOAA-20 | JAPIRA | PARANÁ | Brasil | 4112306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 9d891342-32c6-31ed-9a83-389eb1336354 | -22.6577 | -53.11971 | 2025-09-13 04:12:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8b223fda-a411-3d2a-a003-a097c5f31fe9 | -31.03261 | -55.16393 | 2025-09-13 04:14:00 | NOAA-20 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 9caa7912-bd46-3785-ae05-5e7f7a01b8ec | -28.95401 | -51.49083 | 2025-09-13 04:14:00 | NOAA-20 | VERANÓPOLIS | RIO GRANDE DO SUL | Brasil | 4322806 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 009b02fb-829b-3a80-8e64-a3cb26408856 | -10.1612 | -64.7213 | 2025-09-13 04:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 84db7d08-32e4-32c7-bf99-10404324cd5e | -2.10434 | -52.02869 | 2025-09-13 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b4ac7d2e-ca46-323d-8401-e7bc46b149e2 | 0.68662 | -50.65086 | 2025-09-13 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe73266b-ffea-3228-a628-fff66adc7d2e | -2.28223 | -43.66882 | 2025-09-13 04:55:00 | NOAA-21 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ab64107-70f9-38a6-9a63-3d8185c2fd2a | 0.69691 | -50.64925 | 2025-09-13 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8794f807-b96a-386d-ad05-8548dcfd0f60 | -2.10043 | -52.03173 | 2025-09-13 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eeb67722-a2ea-387a-ac08-266ca58705d1 | -1.97968 | -47.98011 | 2025-09-13 04:55:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2ee08177-62ba-37fa-8d5b-f7db1a63ae3b | 0.69005 | -50.65032 | 2025-09-13 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 4d633900-0c41-3a23-a125-b6109a2d814a | 4.33226 | -60.32743 | 2025-09-13 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3bfc6f4-b1e5-3ffd-9893-8b453d938ccd | 0.67123 | -50.66471 | 2025-09-13 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bee0fc98-547a-3c33-9b6e-e2e1dab81404 | 0.6929 | -50.64605 | 2025-09-13 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 720af423-b9a6-3202-8729-ebb4bde5dbae | 0.69348 | -50.64979 | 2025-09-13 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 42d4fde9-3b9c-3695-9181-c4adecaaf31d | 1.57484 | -55.72181 | 2025-09-13 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README72.md)
