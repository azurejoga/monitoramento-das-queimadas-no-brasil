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
| a344081e-2187-311c-9378-3671ed22b2c1 | -4.15056 | -50.68851 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da4306d9-c5a9-32d5-bd0a-2c0ec5235be4 | -4.64719 | -45.66961 | 2025-11-06 04:44:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c1c11be-4327-3d2f-bf4c-63ed8e7d763b | -3.93241 | -47.69328 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47564fbe-ba3e-310f-a572-b59208f1b3b3 | -4.69359 | -49.62992 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee9558e9-07db-312b-9a0c-fe7deebd6aad | -3.98771 | -47.30155 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 642223fe-b72c-3081-b35b-3bdb123fba8d | -2.44859 | -47.04171 | 2025-11-06 04:44:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90647fe0-8a1e-3748-9fca-4c6e9f75586c | -3.89366 | -42.54475 | 2025-11-06 04:44:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b9dbf4f9-c33e-3017-b010-2b4c613c511b | -4.72192 | -46.42726 | 2025-11-06 04:44:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdec386b-4577-378d-bb4c-31afddbe45bd | -4.18118 | -52.08994 | 2025-11-06 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6786a8f9-4d6c-3dad-91b7-4e633291b5ef | -6.07268 | -43.25219 | 2025-11-06 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a1688598-4ed1-390e-a4b8-5bbd61fbd349 | -2.79016 | -50.31484 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3051adb3-1a13-3f2d-be59-ae42412bc6af | -2.84228 | -49.83128 | 2025-11-06 04:44:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65aa01ac-434d-38b7-b05b-f15b80136f02 | -4.59707 | -43.33736 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2f18d8ed-f9e9-304c-9efe-0d2e8f9fcf78 | -3.24577 | -48.8773 | 2025-11-06 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3576256-3b89-356b-8318-4c15b5f03527 | -4.42878 | -50.60514 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f54fb597-3702-3243-8f63-caf1685e3149 | -3.83719 | -55.97496 | 2025-11-06 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8be91147-363d-3fce-ad75-012acece0084 | -3.0216 | -51.09255 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1371ee02-e9ad-3ad0-98b2-9d4b3d11d106 | -3.98853 | -49.67985 | 2025-11-06 04:44:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3283e52c-efe6-3622-be27-f6d9998fc7ea | -3.0023 | -49.56808 | 2025-11-06 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39895340-8d63-3d87-959d-2e83e045b661 | -3.61374 | -43.5192 | 2025-11-06 04:44:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b321c9e5-034d-3bfc-bf3d-4b7e8e29ac6a | -4.17057 | -54.65862 | 2025-11-06 04:44:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32ccf7e5-9d89-3d9e-9e50-32757eb4b848 | -4.10364 | -48.02178 | 2025-11-06 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38d67f0d-f30f-32c0-89ee-b655f7e1f7fc | -6.28383 | -44.74161 | 2025-11-06 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60097f8b-9ba3-3092-9b15-94e3a4c32a0b | -3.49117 | -50.46395 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9ef022a-2600-32ef-bfe8-75089131eb9f | -3.92723 | -47.6968 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 29b02687-e327-305d-9271-d27c489928b5 | -4.459 | -43.22837 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 245170a3-7a58-3435-91d1-a300d82a65e8 | -3.98957 | -51.08415 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed49fd13-a6fd-3c72-b9ec-9102e3b23991 | -5.86159 | -43.99565 | 2025-11-06 04:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 472ab257-15e5-339a-9954-9cf7fa40ec99 | -2.98296 | -48.70974 | 2025-11-06 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa3a50d7-8634-398d-9cbc-d430a224ece3 | -6.28505 | -44.73323 | 2025-11-06 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2ad5180-0954-3aaf-b6b1-010f9f3e9866 | -4.49259 | -55.80025 | 2025-11-06 04:44:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da3b9a8c-13d6-3567-8d48-c95c11160924 | -2.98052 | -51.35321 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c29435f8-ac6c-37e6-84c4-d9149a4882e1 | -2.83065 | -46.72514 | 2025-11-06 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dcdc0d0-717c-39f2-913a-ca4417bc87e7 | -3.92663 | -47.70068 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 508f1546-79e1-3c79-8a6e-0beda3667674 | -1.63125 | -53.71662 | 2025-11-06 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 992cb378-1dff-3198-83e8-a323ab931c6f | -4.98548 | -48.47297 | 2025-11-06 04:44:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 450c2cd7-b727-354e-818a-9470b9751d7d | -6.04883 | -44.16068 | 2025-11-06 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11cdd9f9-15f7-303d-a8f0-fe557a7a4580 | -2.98411 | -52.82019 | 2025-11-06 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 0a7136b7-e6da-3e28-9ea1-913ad8e034a7 | -3.93182 | -47.69718 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb07c5c2-37f9-39d0-a9d8-ad7c8b37bc45 | -2.83417 | -49.64014 | 2025-11-06 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aaf17acf-6592-3e30-ac64-d912f43ba16a | -4.51367 | -50.1926 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45cc3b0c-3144-373a-9360-ce5d05df108e | -4.25377 | -47.57856 | 2025-11-06 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94a63f99-ea82-36c0-a931-40e53e6bcd05 | -4.01101 | -51.01275 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3c729f55-edf4-310f-b681-6699e07e3c7f | -3.10859 | -51.49381 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b33ae3f6-bb64-3187-ae0b-03e9fd252e5e | -3.45144 | -50.02198 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7048a9e0-2713-31f8-a7b6-ed90aee4c9af | -2.27102 | -55.72869 | 2025-11-06 04:44:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10617241-a417-3043-aae4-e1556cd3a172 | -2.44146 | -45.89997 | 2025-11-06 04:44:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dd1a167-0e95-30b8-ba66-7afd7f37095d | -2.62678 | -49.22646 | 2025-11-06 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 19c51e52-dab2-3f8f-8672-3c5b6a61ea07 | -3.11341 | -51.02849 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcc67d5e-ab5b-34e3-9265-6ef1369541da | -4.41253 | -47.9584 | 2025-11-06 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 628a622b-3e70-3f29-b5a4-43f77ff60691 | -2.43862 | -50.4293 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e5f28f8-f28e-301e-a342-7a1308af2c89 | -4.64322 | -45.66914 | 2025-11-06 04:44:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46eba860-cd86-3831-b3cc-67a74262901c | -5.65652 | -43.01405 | 2025-11-06 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b29c7d3f-c7fe-3765-ae3b-c3d64d2dce0b | -1.65212 | -45.5577 | 2025-11-06 04:44:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3150ada3-dd29-3e51-847c-a2b5958af0a4 | -3.92714 | -47.70442 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6129f102-2bd7-3619-8d2f-50e520f7dc6a | -3.44969 | -51.59089 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a563afc-1625-37d9-949b-560b736a95f0 | -3.8213 | -51.30839 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c21e945-bf63-35fe-b71e-ca7bca85436a | -3.21511 | -50.94453 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08862b5a-4936-3081-b551-6a2bd3b81ad4 | -4.58469 | -43.3326 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| abcf95ce-a784-397b-876f-59c90230480a | -4.92893 | -48.54444 | 2025-11-06 04:44:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 235db336-b6a7-3b05-b2a2-a256a1bab797 | -4.49857 | -50.74698 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbda4480-9ef8-3de2-b4e3-db50bc8ba886 | -4.64245 | -45.67424 | 2025-11-06 04:44:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be301c07-2bc5-35bc-86ed-bd9bc7a6bdbd | -3.46938 | -43.64186 | 2025-11-06 04:44:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad50311f-6b43-301a-b6d7-35f0fb9717b2 | -4.77091 | -42.64276 | 2025-11-06 04:44:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| c13d4f34-18c0-3a5d-92fd-60a28e06ae26 | -3.77735 | -51.67168 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcd0e87a-2537-3760-b09d-dcd358c79fff | -3.49716 | -49.55678 | 2025-11-06 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed603834-f577-396f-90c4-b01c345a2cb1 | -3.92481 | -47.69611 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6e1841ea-49a3-33c2-99bb-6595ceb546c0 | -3.58419 | -50.50027 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8653417-0cd9-3957-ba2b-6035dadf07e4 | -4.46904 | -43.22488 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a1d58eca-6ea5-338a-8176-24fa03231a74 | -2.61575 | -49.23186 | 2025-11-06 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5360e0ad-16be-3b15-b1fb-cffe10984c68 | -4.30878 | -50.56868 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85a8d057-acc7-3ce4-b421-e01499fe99d0 | -4.27571 | -50.54247 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 441b7ebf-0921-3282-83c5-2ddcf8c41561 | -3.83159 | -49.8141 | 2025-11-06 04:44:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f2902be-3e7c-38b9-a315-94df95545d25 | -4.11056 | -48.02283 | 2025-11-06 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 032a8310-b749-3038-b547-8ca44b1bdcb1 | -3.9896 | -47.71801 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6eaf2036-7219-3f3f-bed0-be7c0d0c7905 | -3.1163 | -51.20477 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0ab64315-96ab-39fe-86e7-3b6c8a564ca5 | -3.34215 | -49.91705 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abcd6361-c069-3adf-a4d4-e270b4023ec2 | -3.94068 | -51.04803 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57b11883-19c7-3686-a3db-6e2a9124dab9 | -9.09582 | -44.32117 | 2025-11-06 04:44:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c042f65-a30b-3c07-a785-54415842918b | -4.71814 | -46.42667 | 2025-11-06 04:44:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a43a1d9-b66b-3acf-9d84-d6eb5212502f | -2.39765 | -50.47153 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ab4f3c2-31e6-3fc5-ba7d-a835d5dda13c | -3.00337 | -49.56119 | 2025-11-06 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db703195-9652-35b6-a7d9-bac3f8e9459a | -3.1831 | -49.76176 | 2025-11-06 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ded6804e-3794-37cb-b0ce-7b2d3fb206c6 | -2.80706 | -50.27176 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7dc2a3a0-dd39-3d25-88fd-4832e0d6f7a2 | -3.77053 | -51.7146 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d54bc2e-5cbe-3fc6-9618-1d8617c564f8 | -2.89782 | -50.47308 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0ad54985-de36-3ca6-b5e5-63870934e318 | -3.46874 | -43.64626 | 2025-11-06 04:44:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37e90866-eb7c-3382-b743-b42eb0ff267f | -3.49447 | -50.46446 | 2025-11-06 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fc076f1-43aa-3c49-a086-958eabd1697d | -3.86036 | -47.40262 | 2025-11-06 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9eaa4545-e143-3f87-b636-8ac56534fbd9 | -3.04043 | -51.05959 | 2025-11-06 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d95e381b-a6d6-38f7-8c26-bedd815464f4 | -5.76492 | -40.81187 | 2025-11-06 04:44:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bda7d527-c3f1-3dfe-808d-2012fd3c71d6 | -5.59903 | -45.18763 | 2025-11-06 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23c8655b-9c9e-313c-b19b-6e79b5ef091e | -4.77345 | -49.53139 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd7f3b87-aaa3-3cf8-ab8f-c19c149dec9b | -4.46365 | -43.22908 | 2025-11-06 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3c702ba4-4f06-30fe-9d2f-61fd35d1c354 | -4.57624 | -50.44569 | 2025-11-06 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6731064-1090-3905-8165-4abefeea79a8 | -4.23076 | -51.08675 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 603abfd7-c3c2-302a-a708-86830da7f551 | -3.11186 | -51.21129 | 2025-11-06 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d52ae44-b451-3cbf-9c1f-bb4b218d1373 | -4.87288 | -56.08888 | 2025-11-06 04:44:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6522109-2be6-3ef4-887b-c7e3b4cd2479 | -3.59833 | -52.00315 | 2025-11-06 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c531d2f-02f5-3246-a855-dabc946f9086 | -2.88134 | -49.84082 | 2025-11-06 04:44:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README19.md)
