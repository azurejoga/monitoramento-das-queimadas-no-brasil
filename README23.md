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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3500c89-138d-3c3b-a9cb-8b5f54daf65c | -10.18234 | -40.95496 | 2024-11-16 04:04:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 88d39a0d-091d-39aa-b69b-2a4701b174cf | -9.12027 | -44.4222 | 2024-11-16 04:04:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96bfa917-38ea-3b17-8b5d-60d0272fe691 | -9.85279 | -38.96735 | 2024-11-16 04:04:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 12f45e02-e7a5-3e70-9052-709351bddf86 | -8.52197 | -40.74316 | 2024-11-16 04:04:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| af22cbaa-493d-3762-9e40-d6e4330337ad | -9.86532 | -47.52914 | 2024-11-16 04:04:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa8a54ca-1092-3738-b6d7-cadfbeb45b57 | -8.27997 | -45.97059 | 2024-11-16 04:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31926257-0d8f-3171-95e7-492b8690dcce | -12.13688 | -43.4859 | 2024-11-16 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4aeeea6-e486-3f39-913e-e30d217c0f4a | -8.62291 | -45.69544 | 2024-11-16 04:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9022ecbb-6765-300c-8dd2-9fe0cd398a1c | -10.66658 | -44.49599 | 2024-11-16 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2ff0955a-d6ae-3248-ac3e-bb35c2bfade1 | -8.2903 | -45.97711 | 2024-11-16 04:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9e3d0fe-600c-3102-b104-a5a1e545cfd6 | -11.87464 | -38.34787 | 2024-11-16 04:04:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e0e3751b-d890-3a85-8f8f-5eb23be905e4 | -10.54309 | -44.67337 | 2024-11-16 04:04:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ec864d5-59ec-3acf-a786-5dca7483f86a | -10.53869 | -44.67714 | 2024-11-16 04:04:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ef7e06b-ddac-3bee-afd7-05f71c3e68a1 | -7.25338 | -46.78199 | 2024-11-16 04:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7818fd00-522e-3db4-ae3c-21e9b4d5a2ee | -7.43999 | -46.93452 | 2024-11-16 04:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0f0b2ad-9f48-341f-97c0-4dd3307673ae | -9.93018 | -42.12158 | 2024-11-16 04:04:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 492308e0-4564-3769-be65-298b7a1aeaaf | -10.66294 | -44.49538 | 2024-11-16 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3950c5c2-8ff3-31ca-872f-8652f4c9f6b3 | -11.87403 | -38.35201 | 2024-11-16 04:04:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 53eda8e2-cc47-3c84-aac7-258208d59e4f | -11.53469 | -45.00573 | 2024-11-16 04:04:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3007087f-245b-3ff2-aa60-f0aaf6a0ccb3 | -8.11587 | -44.14285 | 2024-11-16 04:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5a99ead-46f6-3f69-ab9c-4be9f48661d0 | -15.36858 | -43.1839 | 2024-11-16 04:04:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6f577415-f4fb-3402-a57a-54bd4a2cc805 | -10.83446 | -44.46091 | 2024-11-16 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f89e4bb9-019a-31d5-9e47-93efccb1f4c8 | -7.49989 | -47.35708 | 2024-11-16 04:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff38dac3-f47f-3028-81d7-26b08cd6e23a | -7.86565 | -42.50597 | 2024-11-16 04:04:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 38ca6c79-1e2e-352c-8a5c-9bf5dbd3d34e | -17.66462 | -57.55087 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| efda32a7-2d52-3732-944c-053efb23c7d4 | -17.5843 | -57.46469 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 447f0d3a-6e94-3671-a28e-6d3973cf4050 | -17.67966 | -57.56277 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| d603be43-0d40-3993-a899-e5656878ebdc | -17.67614 | -57.54626 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 54e7f435-d3e6-36f5-8cf8-2cb89a0ca9a6 | -17.57257 | -57.46515 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 6e7a7ff5-5a35-37bd-a725-7d9630083426 | -17.83113 | -54.54662 | 2024-11-16 04:06:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b0aaf33d-8935-33d9-bab4-8db4817c7184 | -17.65754 | -57.54904 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 2f8dbfc3-41f3-3126-ace6-46bfb93a1eab | -17.58315 | -57.48339 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 3258ab2b-abbe-3bd0-b404-2a8ce786753e | -17.64337 | -57.54542 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| a4259aae-596b-3b13-a9ec-b0417d3a85af | -17.70481 | -54.08722 | 2024-11-16 04:06:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30a4f10f-80bb-3959-8460-51e7259b8b1b | -17.6876 | -57.54893 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| f7d25c83-2144-31a2-83eb-7fd7f1988207 | -17.57018 | -57.46106 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 002aef69-d0d5-38d0-8ff4-4683f192fe40 | -17.56123 | -57.43563 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| acda1ee3-3e14-3138-a8e3-01a03fe57de7 | -17.66726 | -57.55184 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.5 |
| e921fa02-14dc-309e-a536-d8070a3653f6 | -17.70088 | -54.08565 | 2024-11-16 04:06:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89eb8481-74a6-398d-82ba-9221a737f44d | -16.26766 | -39.55432 | 2024-11-16 04:06:00 | NOAA-21 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 718f58cb-78c0-3a6a-b663-5ca0eb58b962 | -17.57611 | -57.45055 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 2261f180-7108-392f-ace7-5d2a17a36edd | -17.82617 | -54.54041 | 2024-11-16 04:06:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 06e6e721-ff26-341b-8d81-fa095340b5c8 | -17.58257 | -57.47208 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| d75f9ff2-96e8-3ca2-a30c-8860fec2a248 | -17.83215 | -54.54193 | 2024-11-16 04:06:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd2af417-bc97-342b-8d98-bb1e65ea8e9f | -19.83936 | -40.0801 | 2024-11-16 04:06:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 354ab6f9-ae78-3cae-bbc2-8b7d3188e965 | -17.56829 | -57.4374 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| cd89b535-d334-36a9-b18e-4dae70cdade9 | -17.68144 | -57.55539 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 42591b61-315d-3cf9-8b6a-e9f6edcfeb0f | -17.57191 | -57.45374 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 9e2de7ea-de34-3014-963d-c2beb88b0dac | -17.58084 | -57.47941 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 0f3bdc35-f815-3b14-b839-8560ae725574 | -17.65488 | -57.54092 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| c88de71e-e3a0-3590-b9ad-3056e315c7f3 | -17.67343 | -57.54533 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 3574adcf-2a85-38dc-86a7-5f850a49a9fe | -17.68586 | -57.55631 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 0b9c9df5-617b-3d76-ac83-716327e80de1 | -17.69991 | -54.09015 | 2024-11-16 04:06:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 826fa726-c673-3e84-a077-86144bcc695e | -20.79289 | -41.12999 | 2024-11-16 04:06:00 | NOAA-21 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bc4b9ad9-660d-3931-aa10-d0f1386225e7 | -17.5655 | -57.4634 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ef7e445b-be42-3935-8fde-f39b96ab488b | -17.23572 | -57.18942 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 3a3891c6-3207-3481-a618-fcf65b3a7fa4 | -17.5755 | -57.47026 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 7f3acb5d-9b71-39b9-abc9-64b3e2a3a4e4 | -17.82708 | -54.54307 | 2024-11-16 04:06:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5edd14c4-7ee6-397d-ab37-c079d6fcee2f | -17.66018 | -57.55004 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 97a2d2d1-0bee-3c3e-9eb7-acbae3ef3bcc | -17.57725 | -57.46284 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| fe879061-e528-379b-906c-7bed1d29df96 | -17.70375 | -54.09196 | 2024-11-16 04:06:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91c95a64-360f-3f71-a2af-e1177ac2fede | -17.65309 | -57.54826 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2ece302b-7a1d-32c5-9e8d-81bfd8bff6d1 | -17.65928 | -57.54167 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 916bb95a-9bf9-340a-8ee9-f3c722274284 | -17.68675 | -57.56453 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| e9bd00d7-62b9-3ec0-9f0b-47adf89090e9 | -17.68853 | -57.55718 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 9dc0650d-2ddf-32f8-858f-50720b624724 | -17.57363 | -57.44647 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| f5ae09e4-76a9-3e41-8616-ef0c5352e940 | -17.68323 | -57.54803 | 2024-11-16 04:06:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 65e4ce62-7f32-3ff5-bd5c-b1ddb6f9ee5a | -19.27577 | -39.89599 | 2024-11-16 04:06:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 235ad2bd-b08a-3196-8ba5-4c86d32357ae | -17.82513 | -54.54519 | 2024-11-16 04:06:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a280dc41-720c-353e-89b1-036ef7582b41 | -22.27671 | -56.10322 | 2024-11-16 04:08:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e39c1c2d-f911-3f85-98d9-19d84be789b9 | -23.95242 | -54.08544 | 2024-11-16 04:08:00 | NOAA-21 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3e9a2496-8ef9-3af4-9032-45994d2aff35 | -20.99541 | -51.79356 | 2024-11-16 04:08:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7bf7fe5f-6218-3691-9d2f-002ab701ad03 | -22.27641 | -56.10797 | 2024-11-16 04:08:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ef69a2e-d6c9-3a48-bb97-f9029f94ad9f | -22.05477 | -56.01361 | 2024-11-16 04:08:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 074be8d4-a5bb-308f-b79d-7bb943bcc3c5 | -22.27758 | -56.10312 | 2024-11-16 04:08:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9818e64b-85c3-36c7-baf2-cb138c88bdc6 | -22.05436 | -56.0113 | 2024-11-16 04:08:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 23dd17ed-0614-3232-bfef-162f0d703e23 | -22.27558 | -56.10809 | 2024-11-16 04:08:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b386bfa-39d0-33bd-afee-904d990d5328 | -22.05596 | -56.00864 | 2024-11-16 04:08:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06fbaec3-0b29-3886-b5cf-ca6436db5ee4 | -3.2009 | -45.5405 | 2024-11-16 04:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 54.0 |
| ac564cdd-d9c5-33ee-bd1e-9a4b4b51c504 | -3.2753 | -45.5151 | 2024-11-16 04:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 1d8715ca-9576-3f45-a762-bfedfa3798e7 | -3.2754 | -45.4927 | 2024-11-16 04:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 6830b00f-f294-3096-9b7b-abadee1a0082 | -3.7394 | -45.6523 | 2024-11-16 04:10:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 211.0 |
| c0e5b0cb-60f4-369a-9ae4-a035853c2ffa | -15.9028 | -59.254 | 2024-11-16 04:10:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| d3def6a6-adf6-358a-886d-6baeb3330846 | -17.2543 | -57.4698 | 2024-11-16 04:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| 33e52587-392d-3270-99ba-a7395ce33632 | -17.5882 | -57.4711 | 2024-11-16 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 8fa5d0bb-a886-3ea2-9523-fd0ebbdd8aa2 | -17.235 | -57.4516 | 2024-11-16 04:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.8 |
| 3f9c56bb-ecc1-3d6f-b654-5c8af31edd21 | -17.5675 | -57.5351 | 2024-11-16 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.6 |
| 939c9e2e-1a29-3c56-ba6d-32178f0a21a6 | -15.9219 | -59.2722 | 2024-11-16 04:10:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| bbce94ef-b84b-3c4d-84ca-f82f2d8d13b6 | -3.7393 | -45.6747 | 2024-11-16 04:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 100.8 |
| c4b68f51-bf8e-3cbb-b691-c1dc4c24a537 | -17.5478 | -57.5375 | 2024-11-16 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 8c6827c9-2552-38a4-9d38-79cd25162966 | -2.7801 | -48.5592 | 2024-11-16 04:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| ed65e228-a70f-30f6-989e-3ac49f1142d7 | -17.5678 | -57.5146 | 2024-11-16 04:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 4c883f95-c5ee-3c3e-890a-e297e5923b03 | -15.9025 | -59.2741 | 2024-11-16 04:10:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 1c9ac398-410d-3610-90da-939b35389d22 | -2.78 | -48.5806 | 2024-11-16 04:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| f803ecf7-6f74-3157-94a0-95f614ec6f0e | -17.2547 | -57.4493 | 2024-11-16 04:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.6 |
| ca497e10-6b13-3b49-bfa8-a86aa97da25e | -5.6796 | -35.6418 | 2024-11-16 04:10:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 46a10287-e148-334e-9ad3-d7b9e872c954 | -2.0271 | -53.9477 | 2024-11-16 04:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| a14b0613-9005-3621-b3cf-0c4f44c70996 | -28.40072 | -51.35263 | 2024-11-16 04:10:00 | NOAA-21 | LAGOA VERMELHA | RIO GRANDE DO SUL | Brasil | 4311304 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5742942a-b38d-398e-9a88-330f6833c0c6 | -29.61063 | -51.99224 | 2024-11-16 04:10:00 | NOAA-21 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1298af1d-56e5-3e80-92c2-b4c61411f8db | -29.6288 | -51.96623 | 2024-11-16 04:10:00 | NOAA-21 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README24.md)
