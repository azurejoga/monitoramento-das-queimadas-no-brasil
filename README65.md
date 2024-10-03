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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e6e870c-817f-33a2-a845-13b4944a1d16 | -7.70424 | -42.99105 | 2024-10-03 03:34:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 808dcc28-ba5d-3af4-907f-b4fdfd8e5283 | -7.70365 | -42.9944 | 2024-10-03 03:34:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| b9045e24-9f93-3651-9642-f2c62614db31 | -7.69893 | -42.99006 | 2024-10-03 03:34:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9a3531bd-9a0a-3244-9629-6393225c0227 | -7.69831 | -42.99353 | 2024-10-03 03:34:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 71339ef6-4d72-3c3b-a940-feeeca3f7acf | -7.69362 | -42.98905 | 2024-10-03 03:34:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e198c4a7-d2e8-3125-b796-5107e78eed77 | -7.64225 | -42.42904 | 2024-10-03 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6ad7d088-41bf-37d6-bc56-6fce7db8b80f | -7.64073 | -42.46716 | 2024-10-03 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a1c26f57-579b-3873-8c90-06d69e1cd1db | -7.63656 | -42.43126 | 2024-10-03 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0fa41a43-181f-3b2b-8906-009dfdd54dc7 | -7.63559 | -42.46623 | 2024-10-03 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a47f344d-886b-342a-8c16-fd8f37bd283e | -7.63544 | -42.43754 | 2024-10-03 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7ab64c1b-7ada-38fe-b3dd-a511d612c6de | -7.63487 | -42.44069 | 2024-10-03 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 64429e3d-9ba3-3687-9dde-514fc7d2f9a8 | -7.63047 | -42.46521 | 2024-10-03 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 90a73419-da68-32ea-9210-425d2c2804fd | -7.6286 | -42.44614 | 2024-10-03 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e688a0ad-a3dd-39da-be1a-255dfdf22f8e | -7.62589 | -42.4612 | 2024-10-03 03:34:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bd960a8d-d3fb-371e-b4f6-e318227fd160 | -7.48962 | -43.93466 | 2024-10-03 03:34:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 460eee3b-589f-3e31-94c3-9aa7ac6984f6 | -7.48894 | -43.93843 | 2024-10-03 03:34:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb8484a5-9c93-380f-9dd0-b29f0f4fa86d | -7.39758 | -35.19951 | 2024-10-03 03:34:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| 377ff9b4-6ef5-377a-9e2d-bb3124c7af3d | -7.39421 | -35.19896 | 2024-10-03 03:34:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0e03f780-7fdc-3064-ac96-81534961b0e6 | -7.33289 | -35.19289 | 2024-10-03 03:34:00 | NOAA-20 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eb516ca2-468b-3003-bb56-71cb38cfbf60 | -7.29387 | -42.25354 | 2024-10-03 03:34:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a69040e3-697c-302d-ab7a-959753103c8d | -7.29334 | -42.25657 | 2024-10-03 03:34:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 92eb1bea-9bff-309d-90bd-fb33daf00a2b | -7.29281 | -42.25962 | 2024-10-03 03:34:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5c3869e3-2db6-3b11-9f2b-34c911ee24b0 | -3.3854 | -42.2866 | 2024-10-03 03:35:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 119dd8a4-a445-3330-95a6-3f89d2601cfd | -3.404 | -42.2858 | 2024-10-03 03:35:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 339.7 |
| 687ffa3f-909a-3ae1-ae0b-52940f94c3b3 | -3.4042 | -42.2621 | 2024-10-03 03:35:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 234.6 |
| 89092101-52a6-3cb8-a887-7e9a0045a020 | -3.4227 | -42.2849 | 2024-10-03 03:35:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 6c8c3047-374b-306f-bc1f-1f8503cced54 | -3.4229 | -42.2612 | 2024-10-03 03:35:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 8050388e-617b-3c97-bbae-d0ca49b336b3 | -4.0949 | -48.4894 | 2024-10-03 03:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| d7515658-161e-385e-91c4-fc3de279c2e3 | -4.095 | -48.4679 | 2024-10-03 03:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 4419f9e6-2858-3a14-a037-5947e91d269f | -4.1134 | -48.4886 | 2024-10-03 03:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| cb4a7537-551b-3abb-8243-3f3d99871d0a | -4.4657 | -42.8877 | 2024-10-03 03:35:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 90540687-6210-3835-b174-a6c3de060377 | -4.4844 | -42.8866 | 2024-10-03 03:35:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 187.3 |
| 0f61a6d0-d064-3b7e-9bdb-80687abdeebc | -4.4845 | -42.8631 | 2024-10-03 03:35:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 2739d459-1f45-39d5-b048-069acefe6fae | -4.5031 | -42.8854 | 2024-10-03 03:35:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| ece2d1c2-77bf-331d-a069-f84121e2edb4 | -4.5033 | -42.862 | 2024-10-03 03:35:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| c250e499-fdf2-3338-b6b6-b760d303a1f1 | -4.5373 | -43.3273 | 2024-10-03 03:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 51496aec-2130-3a5c-b534-702dd77486fe | -4.5375 | -43.304 | 2024-10-03 03:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| dad03921-f03c-3d1f-978d-11c8aacf1770 | -4.9264 | -43.79 | 2024-10-03 03:35:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| a11ca11b-b8db-3653-928d-bed1f1f2cef7 | -6.6529 | -45.3324 | 2024-10-03 03:35:43 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 407c4012-4c7c-3e92-b819-5c3de3e81a73 | -6.6716 | -45.3308 | 2024-10-03 03:35:44 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 00e8442a-b5a8-3a8e-bf63-b557b7cc3083 | -8.8506 | -45.5086 | 2024-10-03 03:35:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 408fe5fe-e03e-3770-881a-5e9992af04d4 | -8.9791 | -67.4099 | 2024-10-03 03:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 7f8cbe86-58c7-3e0a-b275-8b9d5bb0fb5e | -9.0515 | -67.871 | 2024-10-03 03:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| b8ac327d-9df3-3d00-a9c5-e27cbce2604d | -9.1566 | -61.6758 | 2024-10-03 03:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| de90958d-5f49-36e7-9e6f-f511cd648dea | -15.40257 | -47.42412 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2c69812-a36c-38f7-97f9-2338aa8979c7 | -15.40169 | -47.4283 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1f44160-eb36-3792-a48c-8eeab1204361 | -16.50681 | -39.11171 | 2024-10-03 03:36:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c086e6ec-28eb-378b-a542-02b4299e42d4 | -16.3357 | -42.29856 | 2024-10-03 03:36:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e6e21e08-46c8-380b-8228-7956f2fe2da2 | -16.33488 | -42.30288 | 2024-10-03 03:36:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6ffcca68-e055-3005-9b49-8bbabcede0b4 | -16.33132 | -42.29783 | 2024-10-03 03:36:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3c8d4842-1f6d-35da-b0c8-23726083a99a | -16.28452 | -43.58472 | 2024-10-03 03:36:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06c51f5c-178f-3c1f-b01a-0d5ecc5d875e | -15.81006 | -42.49024 | 2024-10-03 03:36:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14b2d429-3911-3543-b91d-c0b84083520c | -15.80643 | -42.48497 | 2024-10-03 03:36:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 153cb887-e6bb-3b98-874d-a2643ef4ab4b | -15.71898 | -48.38429 | 2024-10-03 03:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04db5bd8-a0cd-3007-804f-dc877e5e90a0 | -15.71779 | -48.3898 | 2024-10-03 03:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 704f8318-b5f3-3452-89f7-10301fb7194d | -15.67683 | -39.21893 | 2024-10-03 03:36:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a1eded7f-42fa-3343-b5cd-dd363f9b36ad | -15.65982 | -47.20381 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4aaf9cc2-d8ca-3408-82c4-7a8559b655f1 | -15.65918 | -47.20034 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4562ea42-56a7-33d5-8727-48a096da6e49 | -15.65824 | -47.20484 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6c500ad-e2ab-30fb-8717-f17d6c87913e | -15.65786 | -47.2129 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4b44dc71-36de-3fd4-b205-ef9823abb5d8 | -15.65729 | -47.20939 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 580c152c-6ab0-34b8-a11c-324d9093a4e6 | -15.657 | -43.91713 | 2024-10-03 03:36:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbbe618a-0078-3327-89a9-f9dd7ecf8d1f | -15.65633 | -47.21396 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc50a5f8-fbda-3de3-9021-4ecf27f53c17 | -15.60065 | -48.55275 | 2024-10-03 03:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58431044-69c1-3973-bbd3-f51aa516a29f | -15.59164 | -48.78002 | 2024-10-03 03:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31519330-5ced-3e84-b4ea-b34d987a70f6 | -15.59074 | -48.78409 | 2024-10-03 03:36:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4aa7ab18-76b4-3edb-a0f9-8d92aeee4fcc | -15.51689 | -42.23838 | 2024-10-03 03:36:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e94fbfc4-dab4-3517-a41e-4381b4f8f9d1 | -15.51601 | -42.24309 | 2024-10-03 03:36:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| caad92fc-8dc7-3178-a741-42c24cf3eace | -15.45506 | -42.13311 | 2024-10-03 03:36:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdee12a6-1d9a-3147-9012-cc2da5bd03b9 | -15.44162 | -41.14252 | 2024-10-03 03:36:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8d36c743-c4f4-3b19-94fb-64e518bee0ab | -15.43961 | -41.14002 | 2024-10-03 03:36:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9acc0daf-3d1a-3e41-92b5-383a031ebff8 | -15.43893 | -41.14385 | 2024-10-03 03:36:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a4258e21-d47f-3c8e-ac8e-edbd6183f56a | -15.43825 | -41.14766 | 2024-10-03 03:36:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 87fd40d5-8e04-3114-a574-29d60dc18c0a | -15.43751 | -41.14174 | 2024-10-03 03:36:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9cc297fc-b06e-3ca5-9e7e-bac66d832dd8 | -15.4368 | -41.14555 | 2024-10-03 03:36:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7f305836-51cc-369b-b4b4-744130e1e306 | -15.42068 | -47.4263 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc53ceb5-08d9-3c4b-8906-001a48fc02b7 | -15.41456 | -47.42496 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55d65a81-abca-3dc2-b2a9-0c702a98ce79 | -15.40876 | -47.42515 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab6af69c-b347-3c37-8bb5-cd1fc3468725 | -15.40847 | -47.42347 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40ed4a78-4103-30dc-b41a-b39c90aedbd1 | -15.40135 | -47.42674 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| beaeb9ae-6963-3ee3-a06b-821c51df4595 | -15.39451 | -47.43201 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa51b091-5b07-326a-a576-10657d9c167a | -15.39411 | -47.43055 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7d0a177-7679-327c-afae-3c4f4c5da32c | -15.38881 | -47.42871 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a015517b-0ff2-345f-a967-562a4977809a | -15.38838 | -47.42743 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8827f811-af6f-30f2-8a44-6e569502f80d | -15.38245 | -47.42853 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ff1082b0-1351-375b-8347-d2395a2297f1 | -15.38202 | -47.42717 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf9017a0-2522-3f7c-a375-91af98c41b44 | -15.27707 | -47.50837 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bbfcec48-987a-3ed0-b752-88f090a7a52b | -15.27636 | -47.51171 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f160b5c1-f4d4-3168-81e0-960e3b524c29 | -15.27497 | -47.51008 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b5f92ea8-f93d-3fff-815e-ba35c21054ad | -15.26835 | -47.51078 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 875e8c6a-88bc-3a2e-9af0-7988bfd6a09d | -15.26224 | -47.50916 | 2024-10-03 03:36:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77af6607-da2e-3f85-ab01-6b2a0f28b49a | -15.2613 | -47.51349 | 2024-10-03 03:36:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 076edca5-296d-363e-b180-817dc16e9a78 | -15.25141 | -47.50756 | 2024-10-03 03:36:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87988f8d-a904-3e6c-b997-7516d8a12c12 | -15.25037 | -47.51245 | 2024-10-03 03:36:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa00183a-7f60-3187-b2ec-ac8c0692cf07 | -15.24999 | -47.5061 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 70dca998-ed12-327f-a5ed-74ac5dd65de2 | -15.24894 | -47.51093 | 2024-10-03 03:36:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6e10b5c8-5bd8-30c7-89b7-119631c6b4cd | -15.24533 | -47.50575 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| facdd52b-9844-342e-a55e-48ef12b7bbbd | -15.24388 | -47.5045 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8d9e3263-10ba-36d7-b1d1-b2c3a1152af0 | -15.23915 | -47.50446 | 2024-10-03 03:36:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac2af5f1-938f-38d3-a7e1-420f941fce0e | -15.23817 | -47.50909 | 2024-10-03 03:36:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README66.md)
