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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 157e1969-d065-3bbc-885a-ea07a85a76f7 | -4.99152 | -49.90057 | 2024-11-08 03:59:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 261459af-dfb5-3f05-82c9-ab7afb87121b | -6.01413 | -47.34307 | 2024-11-08 03:59:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b52665c6-998a-387e-94a6-7a4eb8c0d510 | -6.28156 | -44.7344 | 2024-11-08 03:59:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2363563c-53c1-3d87-9397-ec4f6e76f0f6 | -5.43675 | -46.3607 | 2024-11-08 03:59:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ddbdc8f-5dd0-318e-95d7-e3e4d3678c3b | -9.94197 | -47.82963 | 2024-11-08 03:59:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad803d5f-035c-3492-b8e2-1d450586371e | -9.58409 | -35.76323 | 2024-11-08 03:59:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0bf0256a-1d9a-3780-a11c-5fc9c6436ef1 | -6.98619 | -40.03856 | 2024-11-08 03:59:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5172d143-574b-385d-a67a-8d0f0c0f23d8 | -6.52201 | -47.01545 | 2024-11-08 03:59:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bd852cd-dc5e-3b34-9f16-07f67f53a37a | -7.48362 | -43.56131 | 2024-11-08 03:59:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3fa31e9c-60c3-3977-998d-4e35f7c9d610 | -8.30048 | -43.60824 | 2024-11-08 03:59:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a241a42-9408-3546-b424-3837ec65e811 | -5.05156 | -47.67101 | 2024-11-08 03:59:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e61f116c-f581-3f46-9186-73647fe96c36 | -5.64139 | -44.2499 | 2024-11-08 03:59:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b64d98ca-30c2-3797-9196-e546fdee4280 | -11.80414 | -40.32728 | 2024-11-08 03:59:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ea28ca31-a102-3e3e-bc69-3facf8aaec3e | -5.65895 | -45.20184 | 2024-11-08 03:59:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f905213-7841-3057-a2b6-db10c28b92ea | -5.92924 | -43.65491 | 2024-11-08 03:59:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04cccce6-fca6-3d9c-ab0f-f3b6c9caac96 | -5.44197 | -46.35704 | 2024-11-08 03:59:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0a4e9dd-3135-368c-946d-65b5c82a1303 | -6.16995 | -43.59122 | 2024-11-08 03:59:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 30649f7c-9672-39e2-a6a9-dadc310b4603 | -4.98713 | -49.89937 | 2024-11-08 03:59:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36f6f160-3285-3a97-a837-94c59713612f | -6.66092 | -38.90351 | 2024-11-08 03:59:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 74d83896-bec9-34a4-8f5a-1454eec1345c | -5.94055 | -43.77944 | 2024-11-08 03:59:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e48e37c5-0da4-3b3b-8a1a-def86e042a3c | -5.68407 | -46.43752 | 2024-11-08 03:59:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10577a6d-f342-3e52-9686-a6a1ab6e3b74 | -11.86737 | -38.35671 | 2024-11-08 03:59:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ee01c3da-a9a3-388c-bbbe-7b2b6f9b684d | -6.72243 | -46.07785 | 2024-11-08 03:59:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5509b77f-c046-3287-894c-cfa87310dba9 | -5.68287 | -46.32083 | 2024-11-08 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d1c9681-41aa-32a5-a16a-71eddc56c640 | -6.75528 | -39.25611 | 2024-11-08 03:59:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4ae242ce-7a65-3cc2-bc9c-a38b1e699a6a | -8.1371 | -42.87885 | 2024-11-08 03:59:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 79f6bb28-b871-3f8b-a1fc-5675acff0337 | -5.37521 | -46.26299 | 2024-11-08 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 867f0ab6-b4c1-3550-8f98-785bc45cab17 | -6.9653 | -45.46967 | 2024-11-08 03:59:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0282f537-3f03-34e1-94f7-582cffa73843 | -8.07942 | -43.63065 | 2024-11-08 03:59:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fe11b86-6318-3197-947e-94f4f6ee6be3 | -5.44123 | -46.36147 | 2024-11-08 03:59:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d0bdae49-a9f9-34cb-a96a-4275c98a4465 | -5.9698 | -45.36744 | 2024-11-08 03:59:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 728593fe-753a-3407-bb2f-2769f3696d2f | -7.47999 | -43.56068 | 2024-11-08 03:59:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 20d42393-64d1-31f7-ae16-ff9948df751b | -5.37646 | -46.26473 | 2024-11-08 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2f7b44f-d617-332b-935e-e260b390b261 | -5.9954 | -46.09713 | 2024-11-08 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba808916-3ebb-37ec-8559-5700532dd57b | -11.69239 | -37.64813 | 2024-11-08 03:59:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 678b9ce6-2962-3b4f-a13a-3f54907dc996 | -5.98475 | -45.36567 | 2024-11-08 03:59:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6fb79977-be35-34a4-836d-94a7f7f69f7b | -6.39624 | -47.14766 | 2024-11-08 03:59:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c12e316a-83a6-3858-afaf-9aad7cbb3fe7 | -8.1406 | -42.87943 | 2024-11-08 03:59:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cc40a028-e285-3946-af7e-ff7742b1fecf | -6.2924 | -42.03825 | 2024-11-08 03:59:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4b8cfe72-737a-3bfc-80c5-044e6bd799dc | -7.89733 | -46.67994 | 2024-11-08 03:59:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd966680-2d97-3702-8579-9c2a68be80b9 | -5.37443 | -46.26753 | 2024-11-08 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a77b582-55ae-3e00-907f-5fa1cfaf2827 | -5.59489 | -46.25279 | 2024-11-08 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c41110af-44da-39ea-9613-fa9025026443 | -6.16547 | -43.59525 | 2024-11-08 03:59:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8fb10850-c95e-3b13-888b-f0a7e1ada44f | -10.72656 | -49.83145 | 2024-11-08 03:59:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06f44d5a-7f8d-36e3-b1b3-b52e102b1200 | -8.93507 | -37.95783 | 2024-11-08 03:59:00 | NOAA-20 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 31068c3e-64f5-3390-9abb-0864f81e8284 | -6.85525 | -38.89724 | 2024-11-08 03:59:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e50a09f4-b303-35da-8868-92f34c7d43fc | -9.94654 | -47.8306 | 2024-11-08 03:59:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7845d54a-b730-3099-a3fd-a74ebd6c7230 | -9.56151 | -35.69194 | 2024-11-08 03:59:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a2526341-dcf1-3c61-93f1-1298a9fd1e12 | -7.03019 | -44.84488 | 2024-11-08 03:59:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56be0932-d81f-3a36-b2c1-1b1a20012e83 | -5.92148 | -44.87142 | 2024-11-08 03:59:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 76a3a5c0-b262-3c02-b9b5-3d00fd673102 | -8.52619 | -40.72324 | 2024-11-08 03:59:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 68092101-1437-3a42-9f0e-9c7d33dac785 | -5.63448 | -46.97444 | 2024-11-08 03:59:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cf8496c-456a-30da-9037-6d3739f94f04 | -5.43157 | -45.11098 | 2024-11-08 03:59:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83f16807-313d-3768-8a04-71558c950e90 | -8.57644 | -40.38278 | 2024-11-08 03:59:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d2b9c4c3-d2c3-308e-8ba1-75f6122204ae | -5.99612 | -46.0929 | 2024-11-08 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aecc8de0-301d-3827-9536-c13a7a3cacb6 | -7.39847 | -35.24322 | 2024-11-08 03:59:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 858116dd-1741-3a9a-8e29-9dc633d7de55 | -6.00047 | -46.09366 | 2024-11-08 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3711837b-19e5-3e0d-8870-e8bde70ff539 | -5.98539 | -45.36192 | 2024-11-08 03:59:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5577a79-c100-3189-9688-d9ad31e0a1a3 | -5.72817 | -43.82001 | 2024-11-08 03:59:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b9736ca8-9962-3b07-a03d-a714c2f0ca6a | -5.93012 | -43.65677 | 2024-11-08 03:59:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3320a22f-f571-346a-9530-24074da685d0 | -6.18768 | -43.18828 | 2024-11-08 03:59:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6c50ded8-820f-3f10-b9d1-97fe276659e6 | -4.521 | -45.658 | 2024-11-08 04:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 274a9546-6397-3866-9a44-a4c6086f065b | -4.5207 | -45.7029 | 2024-11-08 04:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 33531803-dc0d-3f0c-9929-1a1c863fac03 | -3.5447 | -47.3636 | 2024-11-08 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| a249162c-3466-30ba-aac1-86ea6425bf16 | -3.5631 | -47.3847 | 2024-11-08 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 33e144c2-0e7f-34f7-9b30-2d3b29d61d8a | -3.9669 | -48.1716 | 2024-11-08 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| e22d8d54-f69f-37ee-b1be-6aaecc179b36 | -4.5209 | -45.6804 | 2024-11-08 04:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 196.0 |
| d0b622ce-836a-353b-85f4-202d3c2036f8 | -4.5022 | -45.6815 | 2024-11-08 04:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 50fdb1f3-3a3c-3821-8387-b55497936d25 | -3.5446 | -47.3855 | 2024-11-08 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 48056285-ee35-3533-bf11-f871546becea | -3.5632 | -47.3629 | 2024-11-08 04:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 7b7d3c68-ca31-3973-8ad9-a3a23d3ab20d | -3.967 | -48.15 | 2024-11-08 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| dbbadd4d-60a4-368e-90e9-67912be5edca | -17.67432 | -44.15908 | 2024-11-08 04:01:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44b1b768-f898-34c5-846a-eb9de8379fbe | -14.9554 | -42.26146 | 2024-11-08 04:01:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b0008b8e-1532-3632-9541-b06e79f5b3f5 | -15.41 | -42.20206 | 2024-11-08 04:01:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 40b82168-bdb3-344f-af05-116e3f0913c6 | -14.82269 | -42.19921 | 2024-11-08 04:01:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 658d77ab-336e-3b6b-9280-df777103859b | -14.13484 | -41.69275 | 2024-11-08 04:01:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d3f49d6f-da45-347f-bfc3-15d24cdcd8f3 | -15.47261 | -42.93785 | 2024-11-08 04:01:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba720890-7700-39f0-ac46-ec657f8f6be4 | -15.33985 | -42.19375 | 2024-11-08 04:01:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1cb25f4f-028a-3341-b391-c30c4163324d | -15.8224 | -43.33794 | 2024-11-08 04:01:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14b356b4-b4f7-322b-ba03-b95d90229fa1 | -15.58776 | -42.98383 | 2024-11-08 04:01:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8d1ed1a-d9d1-33e0-937a-92c56472b251 | -19.7169 | -40.35241 | 2024-11-08 04:01:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e3c3947d-718a-3683-a356-aa4cb2b6ff69 | -21.68367 | -41.81215 | 2024-11-08 04:04:00 | NOAA-20 | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c52918ec-7505-3b62-9b67-0b2c6a169a8e | -21.68311 | -41.81593 | 2024-11-08 04:04:00 | NOAA-20 | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7fc23b92-8bf5-3155-8d74-ec0fa6276831 | -4.5022 | -45.6815 | 2024-11-08 04:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 102d098c-ad6d-351f-b15f-a6f8bae5592b | -3.3833 | -50.2177 | 2024-11-08 04:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| f54a8bfe-d545-3fbd-94e7-c9e429948b5a | -3.5446 | -47.3855 | 2024-11-08 04:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| f44aec3f-0dc8-330d-8056-11b8c5c33235 | -4.521 | -45.658 | 2024-11-08 04:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 2e68f33e-5d01-38af-99a9-78c8721dfde7 | -3.9669 | -48.1716 | 2024-11-08 04:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 2a3ccb3e-4b1d-3106-a95f-cf85aac7e26c | -3.967 | -48.15 | 2024-11-08 04:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 56c478ca-6885-3a85-afb0-e08889e4f382 | -4.5207 | -45.7029 | 2024-11-08 04:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 7099ce51-0e74-34e5-b532-0f0c1685ece6 | -3.5447 | -47.3636 | 2024-11-08 04:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 005ff029-bd2d-35d2-8e8a-3c70645714b4 | -3.5631 | -47.3847 | 2024-11-08 04:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 871257bc-6522-3fae-ab0f-a177cbb126e4 | -4.5209 | -45.6804 | 2024-11-08 04:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 185.1 |
| afe40072-fce0-3448-8dda-e3770908e9e3 | -4.5209 | -45.6804 | 2024-11-08 04:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 2bad73eb-a09f-398c-a2b9-8e02433696d5 | -3.5447 | -47.3636 | 2024-11-08 04:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 50bd350c-5b41-3ef9-8745-1e146a2ce2f0 | -3.967 | -48.15 | 2024-11-08 04:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 5dadc6cf-750a-3c90-951d-6b78e5883a50 | -3.5446 | -47.3855 | 2024-11-08 04:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 5fb293d5-a921-3536-8c23-9322186bb3e2 | -3.5632 | -47.3629 | 2024-11-08 04:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 7f4d5938-7cae-32a3-b319-94a45da2898d | -3.9669 | -48.1716 | 2024-11-08 04:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| a8ab838f-7182-3517-a742-cecaece718e8 | -4.521 | -45.658 | 2024-11-08 04:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |


[Clique aqui para ver as próximas entradas](README19.md)
