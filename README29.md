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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d9d1e73-ee5f-302e-89be-fda2fdf57b07 | -6.56657 | -43.71205 | 2025-09-02 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb3e9585-a389-3331-806b-7de1ea9e9ad3 | -3.22729 | -47.12704 | 2025-09-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 8c41ced8-9878-3306-a6f6-89fb3ce33aec | -6.32854 | -43.5636 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 333f3dbc-81df-350e-8f25-edd5c6ee9a7e | -6.22993 | -41.81328 | 2025-09-02 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6936de21-3243-33a1-9723-da6c9793fca2 | -6.72045 | -42.25925 | 2025-09-02 04:12:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 681b6594-b866-39ed-b821-f0bb554d0d90 | -3.21767 | -46.83662 | 2025-09-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 569dae32-d6c3-343c-8eaa-2eeb98be4e2b | -6.29367 | -43.61158 | 2025-09-02 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62557d7b-b2d7-3e6d-bb5c-acd8a6d13fc3 | -6.28204 | -43.57772 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9209ace5-d6a6-3dce-8004-61d0378cb90f | -3.21458 | -46.83115 | 2025-09-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5df54920-7051-3646-b77b-6f479cc1bc99 | -6.19346 | -43.3437 | 2025-09-02 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bafe5a1d-159b-3249-8755-b905f9470202 | -6.16556 | -44.1182 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14e6534b-f249-3c54-b649-9cd8a325b01c | -6.25259 | -42.62303 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9ea8d614-f6c7-3b85-8d3b-6a384b4c7a21 | -6.26579 | -42.60377 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ea5dc523-8f19-3244-a9dd-85740510b694 | -6.19651 | -45.39057 | 2025-09-02 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebef6cf4-9d63-39e4-9c5e-e59a9f57b22f | -3.22601 | -47.12866 | 2025-09-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fb4aec3d-6ef2-3f83-8018-de41bddd001a | -6.2559 | -42.62355 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0c07c1d9-1909-3a9a-a8cb-973b4b4cb482 | -6.1206 | -44.05684 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55fdb8c5-29da-30e9-a121-dde533dddf1e | -2.90745 | -48.2938 | 2025-09-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52675707-1ad1-38e7-ab56-cc35e74cc16a | -6.26653 | -43.52554 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 830bbb47-184b-3693-bd76-f3438e7e97a0 | -5.96181 | -42.95952 | 2025-09-02 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fbab4f6e-45b5-3c01-aa0b-2fc38d2dd0f8 | -3.04658 | -47.02313 | 2025-09-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da58cd2d-4a0a-3333-a111-c892392b698c | -6.37212 | -43.00714 | 2025-09-02 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 523fd2c1-2e2c-379a-93c9-c11e1edfb740 | -6.54331 | -42.97721 | 2025-09-02 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97997038-8c5d-376f-a552-1bef8515dbd5 | -3.78601 | -47.57181 | 2025-09-02 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 81b9e7c1-4f30-36c6-baba-1182de2a3a25 | -6.23336 | -42.42023 | 2025-09-02 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3a9cf496-4225-3182-8d93-b49e9d7783e5 | -6.3379 | -43.526 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c24e193-0199-32f9-95d2-19f822241f2d | -6.24873 | -42.62598 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 46e5fd5c-188b-3539-8644-e72b2b822dc9 | -4.22628 | -47.20733 | 2025-09-02 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b05698c-689b-38a4-99d2-11d6e79b16a1 | -6.27473 | -44.51465 | 2025-09-02 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eefec21f-a50d-371d-8348-902cfdf6c550 | -6.56766 | -43.66227 | 2025-09-02 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7cc7de84-74b8-326c-99fb-06710366e9ac | -2.44442 | -49.36662 | 2025-09-02 04:12:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e3e62a3c-b03f-3de6-ac27-ae3d9dcc69dd | -3.39956 | -46.90563 | 2025-09-02 04:12:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afef1b80-c83c-3399-88ad-6e1afb694020 | -6.18161 | -44.1896 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea39ec80-42c2-3f42-858b-d513f9f8c154 | -6.56878 | -43.71954 | 2025-09-02 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ea6755a-4d31-3b16-b756-9c71b42b0882 | -4.29897 | -46.26346 | 2025-09-02 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30b056c1-f1b3-30b2-a969-391b07a01655 | -6.27672 | -43.28956 | 2025-09-02 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41d8c164-4e0d-3d75-95d6-efe3b855ba67 | -6.31552 | -44.41122 | 2025-09-02 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7674c803-4985-386d-a577-383d6219e6c2 | -2.87831 | -48.86364 | 2025-09-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2f5a793-f2ca-3d9c-b223-bedc5671cdcc | -6.4223 | -43.957 | 2025-09-02 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35791cf6-2652-354e-87c3-56a1ab542e4f | -4.06927 | -47.9613 | 2025-09-02 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c033a6bc-9552-3139-a3c6-f17d5e74193e | -3.22254 | -47.13147 | 2025-09-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04abeccc-cc84-398e-ac9c-f8326d1d6e15 | -6.31306 | -43.51139 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79243ec9-4975-3f73-870c-be25d58177a0 | -5.16491 | -37.98001 | 2025-09-02 04:12:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 87bc9b40-f838-338d-86d5-0d425731bc37 | -5.57389 | -47.42308 | 2025-09-02 04:12:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97ae00a1-a60a-380f-8437-6aa2882a6a7e | -6.18495 | -44.19012 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04f33429-419e-37cc-b002-f2a9dd450205 | -6.12263 | -44.1296 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c68e2eb8-1b52-3f7f-912d-765626b494eb | -2.25641 | -47.84634 | 2025-09-02 04:12:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43374474-9999-3dd1-b3c3-622a0d388314 | -6.4748 | -42.4402 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8aff9421-6d53-3e12-9b31-abecb96e0d6c | -6.12116 | -44.05336 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c88aed7-08ae-3359-8001-412f0af19624 | -6.1271 | -44.12305 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e3d3c65-2e64-3c63-851f-80139c4382a5 | -6.31361 | -43.50793 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76018984-718a-345d-8afc-49243e2b0d61 | -6.30299 | -43.55262 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ea80733-a4f5-32d8-b9e0-c536d4c24f6c | -6.52106 | -43.50528 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 497c64a4-dc99-3106-8d35-4ec3b6f72ad7 | -5.45076 | -42.58185 | 2025-09-02 04:12:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6fba23d3-bdf3-354a-9127-112e789244ba | -6.31637 | -43.51191 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9d7a270-251c-380b-ab84-b6a4aa376f57 | -6.5278 | -42.94641 | 2025-09-02 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0339f127-8c7d-3bae-8c92-26390e9c347f | -6.2743 | -43.56224 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35469118-dc80-3d0a-9403-30f5d4cb1e76 | -4.91219 | -43.19715 | 2025-09-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd880d39-439a-33fd-be3b-bd51a378715f | -6.4803 | -43.56989 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba1a458e-675f-3136-b771-3523e6519788 | -5.57276 | -47.42592 | 2025-09-02 04:12:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab098876-0059-3091-939b-8cdf7f60ad0d | -6.67403 | -43.18244 | 2025-09-02 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3aa84432-e27e-3e5a-9020-08092b88c5b6 | -6.1883 | -44.19065 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a900a7b5-d9ca-3473-9485-914a49800eaf | -6.72099 | -42.25574 | 2025-09-02 04:12:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f6a4646b-260e-3c86-9af8-9e864c393318 | -6.47366 | -42.42573 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 61f08e5a-148e-3396-9452-693b5fd6031c | -5.69679 | -45.95378 | 2025-09-02 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08314283-63fa-3e8f-9f46-9b4a1f190855 | -6.2006 | -45.38728 | 2025-09-02 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 703edb23-6dcb-3b26-a8a2-3d4827043fe3 | -5.69744 | -45.9497 | 2025-09-02 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfe9bb4c-4327-362d-a085-c8b38570206e | -6.19713 | -45.38675 | 2025-09-02 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ac97aed-57ef-369a-8b47-b3e8af83f9d5 | -3.22206 | -47.12803 | 2025-09-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| daf34239-c0ac-3d20-8ff5-b7aa66a47b64 | -6.31913 | -43.51591 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bc8c270-d7c2-3619-b6aa-4e01edfbddac | -5.45131 | -42.57838 | 2025-09-02 04:12:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 49f7af93-ea85-3e16-bb86-08cd5643ad3c | -5.78141 | -42.59509 | 2025-09-02 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 0afc3d83-cc21-3c22-9858-3e5c3c609612 | -5.50279 | -42.63961 | 2025-09-02 04:12:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 90d564e3-e412-3834-97db-e999be094d18 | -6.33183 | -43.52148 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15e5d011-f004-3448-b9fa-13d3bbc1a87e | -6.2691 | -42.60429 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c2f091d9-1690-3a90-8015-c3c6a4132940 | -6.44199 | -42.38867 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 63bbf470-2152-3d46-aa2f-1a5b923b60c4 | -5.00952 | -47.64735 | 2025-09-02 04:12:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fc2e6839-c4d5-3430-b584-888a4a67bb4b | -2.34109 | -47.58863 | 2025-09-02 04:12:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07762d30-75cb-375e-b11d-0952f8549725 | -4.76 | -47.91626 | 2025-09-02 04:12:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d96464e9-88f1-3888-add2-2ed734caa38e | -5.96757 | -42.96788 | 2025-09-02 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d604e88e-cd68-3da0-849b-7858969f8abf | -6.32799 | -43.56707 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24e3aeb1-e018-3023-8ccb-37340eb19f33 | -5.72884 | -43.93669 | 2025-09-02 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4850697b-1af6-3c75-825f-1d453d0e1291 | -6.25421 | -42.61262 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e4f9ad93-1750-3233-b538-f828ca7a8317 | -6.27242 | -42.60481 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 841b58f3-0d0f-3d4b-a677-de1eb19028a9 | -6.25976 | -42.6206 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ec1ba2ed-217e-32a2-aad6-4a159ee6b02f | -5.51272 | -42.64117 | 2025-09-02 04:12:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b9295d9a-6cfe-3a18-8fa2-927749d24473 | -3.22996 | -47.12928 | 2025-09-02 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 899976aa-feab-3ce3-a609-376620609cbe | -4.9155 | -43.19768 | 2025-09-02 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2041ecc3-edd9-3189-a83c-63197acdd2f5 | -6.47643 | -43.57284 | 2025-09-02 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14227bb5-4aec-3c35-9ad7-b873d44de64f | -6.71936 | -42.2662 | 2025-09-02 04:12:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0bba61c2-6c78-3e97-906c-bb29fb95542c | -5.85879 | -48.15832 | 2025-09-02 04:12:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e7e819c-5f81-379b-852a-32b69548d01a | -2.65859 | -48.8004 | 2025-09-02 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f47914d6-0524-31c5-9f29-e6a6f0e0ee9f | -6.1689 | -44.11872 | 2025-09-02 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a2af2f4-7a01-37f7-a36f-de2b5510ded4 | -6.57265 | -43.71657 | 2025-09-02 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d96cd40-8aa0-3d54-9a8d-01743bfe6c4d | -2.19374 | -47.99329 | 2025-09-02 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a13b6a0-ec9d-3fa3-8239-778351ed0fca | -6.25361 | -45.10093 | 2025-09-02 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18b08cc0-2b3a-3ecf-a3bc-e9b868ad6087 | -6.34083 | -42.55855 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9280e65b-a02a-35dc-816b-e4c7825c8f5a | -6.23832 | -41.80361 | 2025-09-02 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b33fddfd-1b05-39ce-8ace-043aaaa36ad5 | -6.25036 | -42.61557 | 2025-09-02 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 104d1b66-2090-3091-9c4a-b9df082ce395 | -3.59369 | -49.45827 | 2025-09-02 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README30.md)
