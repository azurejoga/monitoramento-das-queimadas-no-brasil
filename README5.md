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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09fcd936-8bf5-3854-84cf-90e318ecae44 | -4.15075 | -43.89062 | 2025-10-30 00:35:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7eed4057-3715-365e-9021-82e0a658848b | -2.76866 | -45.40697 | 2025-10-30 00:35:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 47.8 |
| d76e44c7-9494-30b6-a566-47c1fab6c45d | -9.94093 | -47.18375 | 2025-10-30 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7a2d8087-6112-3c24-8125-78eec629306c | -9.27532 | -45.21886 | 2025-10-30 00:35:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c0c7bddd-0254-3246-82f1-cd2fb583018f | -7.27661 | -46.06594 | 2025-10-30 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 58418a6e-7b1c-3b25-a90f-61ac7431408a | -4.03418 | -47.7743 | 2025-10-30 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 47487691-ca7b-311d-b449-466df96139ca | -5.68528 | -47.82219 | 2025-10-30 00:35:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9d5def1f-dc2f-3f17-a2d2-840d6dd66527 | -3.12128 | -45.71486 | 2025-10-30 00:35:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3dd9ea54-8338-3561-aba0-241a09dfcfd6 | -3.60815 | -50.62543 | 2025-10-30 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| de20b0f7-b392-31d6-84f1-d3764b757fed | -3.60112 | -48.9943 | 2025-10-30 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 14c7fbcf-895b-3b3b-aa69-b6da8c023ab6 | -8.544 | -47.7208 | 2025-10-30 00:35:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7df2dd88-4c6c-3601-b291-8c8dffa71f7f | -8.32539 | -47.92864 | 2025-10-30 00:35:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 341.4 |
| 2bc2170c-1a42-397d-973a-7c2ce82ce366 | -6.61998 | -47.17485 | 2025-10-30 00:35:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b95d3d7d-99c5-346d-8dbf-9a28af150d6f | -1.76821 | -55.74136 | 2025-10-30 00:35:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d5ae1eef-f176-30b1-8a5e-4b480cd3d098 | -7.92381 | -46.01286 | 2025-10-30 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 6b956ef1-652c-3cd4-a000-9ac3bb514453 | -3.73212 | -52.13966 | 2025-10-30 00:35:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 181a11c9-8524-3cb9-bbf7-4fd1cb8386bd | -8.90935 | -47.63236 | 2025-10-30 00:35:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b416665f-96e2-34a5-b20a-0416c6bcb345 | -3.8219 | -50.17373 | 2025-10-30 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8734fe6f-65d5-3de9-b506-d8139b8df3d0 | -4.26293 | -59.67766 | 2025-10-30 00:35:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| c26994d6-5edc-394a-90c2-e2b4cc5690ad | -3.43 | -46.18877 | 2025-10-30 00:35:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 18398bbd-db4c-3fb4-b90c-41855b617b5a | -4.27907 | -59.67556 | 2025-10-30 00:35:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 392fdec5-5c0d-322c-809e-e5cbda63c6b8 | -3.68442 | -47.62959 | 2025-10-30 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 81ad33e3-4e4c-3985-9b6a-1fc71f220dd2 | -3.0752 | -51.11101 | 2025-10-30 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7a4216db-87ea-3fde-9994-eb44e52efc0a | -4.476 | -43.42999 | 2025-10-30 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 96a13a2e-aaf6-309b-a918-4f36d7b4852d | -5.38291 | -47.19842 | 2025-10-30 00:35:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 3724d78d-83ec-343b-a997-81fe96e72eaf | -5.96585 | -44.72617 | 2025-10-30 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ad3280ea-c2f6-3951-9c90-e9169a4079cc | -9.87937 | -47.44594 | 2025-10-30 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 696e90b8-f453-300e-9f2d-8acc9cc7e309 | -3.74255 | -52.14793 | 2025-10-30 00:35:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4f7ef240-a777-3bda-aafa-daf19badcf76 | -3.4059 | -52.70803 | 2025-10-30 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9105c942-9fa7-3040-b612-73e6720c95a4 | -6.48541 | -46.88847 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 8466b261-a7b4-3fb5-96aa-c6e41015ddc7 | -2.31992 | -45.65048 | 2025-10-30 00:35:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 40c0ff9a-a0bb-344c-af30-b3dc6ff9131f | -8.70163 | -47.91653 | 2025-10-30 00:35:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6cf723a6-e8c4-3efd-a721-910de806f064 | -5.65637 | -45.98328 | 2025-10-30 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2eeefd98-facc-3a56-81d6-10db3c4be51e | -3.83848 | -49.37256 | 2025-10-30 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a39a5d3a-5e1c-30f4-b411-0db6790790b8 | -3.61345 | -51.07113 | 2025-10-30 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| aa1fcf91-7455-3a63-91b9-4c75b75986c3 | -3.67463 | -47.63094 | 2025-10-30 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 974bf896-2dde-399d-a99d-f1dd129ed723 | -4.04396 | -47.49681 | 2025-10-30 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| f783c947-bb72-358f-9dc6-6f5bc66e6912 | -8.51428 | -48.94246 | 2025-10-30 00:35:00 | TERRA_M-M | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 418aec88-422a-3869-8b73-acb8582345ea | -6.13875 | -41.70816 | 2025-10-30 00:35:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| c765cf8f-5c07-3e01-a441-1cac6829136b | -5.6457 | -45.9848 | 2025-10-30 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 811035a3-ffff-38eb-8ea2-fa1ecf1810b3 | -8.72419 | -48.00965 | 2025-10-30 00:35:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 973bcfd2-d67a-36cb-8598-a6868dec4ec8 | -4.37787 | -43.29365 | 2025-10-30 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 2cdbec00-18b5-34da-8817-ea3bd0949d31 | -7.1476 | -40.45797 | 2025-10-30 00:35:00 | TERRA_M-M | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 31.8 |
| 360c015f-5d23-3c0b-a371-086acb7590fa | -7.93292 | -46.01761 | 2025-10-30 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 34a2e9ca-9a07-312d-85e1-0fc51feacdd6 | -6.52901 | -43.57095 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 05bbccb7-0709-3efa-84ae-30f6ccffe2e9 | -2.15102 | -47.2807 | 2025-10-30 00:35:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 255d3b92-9210-3b7e-8d06-9a16e43e0303 | -9.50988 | -47.25945 | 2025-10-30 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a7b07897-f54f-32ef-9773-a9cd3e00c2c6 | -7.32579 | -47.25456 | 2025-10-30 00:35:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| da75c888-7f49-3182-b8aa-17f3599b4d3f | -5.40631 | -46.01132 | 2025-10-30 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 366377a9-5ba6-3e8e-b27f-3bd25dbe4768 | -5.92287 | -47.3156 | 2025-10-30 00:35:00 | TERRA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8f3b7473-573b-3f16-8edc-b98fe212a157 | -3.46232 | -52.86808 | 2025-10-30 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 2912f974-0bca-3f67-88ec-4c965c3bfd8e | -7.93107 | -46.00535 | 2025-10-30 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| b9e7106f-743d-3674-a3c0-d2e9fe31ab3b | -7.49076 | -46.00227 | 2025-10-30 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2566b04e-89fe-3fc3-be9f-fb615326836d | -4.45995 | -43.22835 | 2025-10-30 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c94322b6-51dd-3031-b7e7-3a4563daa6fd | -8.54541 | -47.7305 | 2025-10-30 00:35:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9d0ba20d-5ca2-3a7d-9a9f-af9ffcadb5d5 | -9.8874 | -47.44873 | 2025-10-30 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 071f0c85-43a6-3aff-ae7b-84e3ce938180 | -7.48891 | -45.98985 | 2025-10-30 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a705c022-2f7f-3851-a179-cda3acf42bfd | -4.04787 | -44.25933 | 2025-10-30 00:35:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 814e050a-62e9-3163-9aa5-3926ab6d25ad | -4.32827 | -47.89525 | 2025-10-30 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 102616b2-1380-3769-ab2f-9fe0f88de596 | -9.48096 | -46.99587 | 2025-10-30 00:35:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ebaaaccd-c501-3b7d-84b7-540b85b94439 | -9.2359 | -45.56181 | 2025-10-30 00:35:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 97ccd952-d281-30b2-81fc-07158ab8e3e1 | -2.76382 | -45.40185 | 2025-10-30 00:35:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 29.0 |
| b78034f7-a60c-3bfd-88ad-75aa0aa01dc4 | -9.28178 | -45.22432 | 2025-10-30 00:35:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2761086d-1c42-35ba-9cfc-d1dac57a5b62 | -9.51132 | -47.26937 | 2025-10-30 00:35:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 58c166e9-dbf3-3ab9-9098-116b7fb938c2 | -5.37468 | -47.21088 | 2025-10-30 00:35:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 5646efa5-d632-35a5-8ea5-30788688eec7 | -4.26626 | -59.63624 | 2025-10-30 00:35:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| dd920009-9c0a-3f3f-ac76-08bd1e9a66af | -3.69882 | -49.56171 | 2025-10-30 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 71aef7f9-3818-350f-9b0b-5e46f9e4b00e | -7.80465 | -46.46023 | 2025-10-30 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 82f22ab0-8b5b-3539-a030-8020a8072df5 | -9.51923 | -46.92702 | 2025-10-30 00:35:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 809b404a-a7ba-3a6c-b554-b96bbce7ef37 | -9.74163 | -49.28586 | 2025-10-30 00:35:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1e0d447d-0486-345d-b1e5-006d2f777397 | -5.27721 | -47.24356 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 123b0071-f170-3417-ab0a-225954d84a92 | -1.14179 | -48.0965 | 2025-10-30 00:35:00 | TERRA_M-M | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 6bc60163-bbf3-362f-a53a-b19cf2c7f077 | -9.83138 | -47.00168 | 2025-10-30 00:35:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| da6afc47-cfea-3035-ba1c-2b255794581a | -4.2477 | -49.85754 | 2025-10-30 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f7f477b9-8742-398b-a453-fae73a66262c | -9.35366 | -50.62193 | 2025-10-30 00:35:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 65746ab4-f73f-3b35-8053-3e6baa45a536 | -7.28901 | -45.66714 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e5cc7226-78bb-3c0e-8a9b-be453fbf7135 | -4.84894 | -45.42123 | 2025-10-30 00:35:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 1f06f936-6ee2-338f-aa06-813cb9813fdc | -7.02978 | -47.62683 | 2025-10-30 00:35:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 45814def-5dc0-3c6f-a0b6-a9152cbf7360 | -3.70007 | -49.57072 | 2025-10-30 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ba24d73c-e541-3f81-aa85-d6d8dacb4dee | -2.76638 | -45.39075 | 2025-10-30 00:35:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e5f53f61-442c-3e3c-b14f-6996364dac32 | -4.76092 | -46.85964 | 2025-10-30 00:35:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b1a7f007-89db-3bc2-a131-71de57d46085 | -5.67682 | -48.81326 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 73024cc9-8bd3-3a57-8f3a-72e041186d51 | -6.19773 | -43.28837 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| f97c097a-2af5-3b11-a3f4-56d3f3bea4ab | -5.8435 | -45.53135 | 2025-10-30 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 19dae4c3-d490-3a61-8160-5c64a4cf2fc5 | -3.78625 | -43.90756 | 2025-10-30 00:35:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 6a856bdd-98cf-38b6-9a4b-4964ac6735c1 | -4.682 | -46.53634 | 2025-10-30 00:35:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 717c45ec-734f-33c4-bfbd-3a5179a9eb6a | -1.45985 | -46.71964 | 2025-10-30 00:35:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ca93450f-375f-3ccf-a069-882a820ccc3a | -6.62156 | -47.18559 | 2025-10-30 00:35:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 62a9b8c2-3a24-3cfb-b545-c0ccb63985ae | -7.80335 | -46.45519 | 2025-10-30 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| f236c6e5-f88d-36dd-b8e4-66949e471608 | -7.33664 | -46.89811 | 2025-10-30 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4474ef38-8290-3329-88c9-19c406385346 | -7.07642 | -44.93054 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| e60180fc-bde1-3410-b603-9b13cca378e8 | -4.49257 | -43.4497 | 2025-10-30 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 9f70d2ab-01b3-394f-9d8c-c7e8adf64836 | -4.36349 | -55.76011 | 2025-10-30 00:35:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2588f084-ae3d-3f26-86a1-7c4eccef9542 | -6.48486 | -46.89437 | 2025-10-30 00:35:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0d6f4dc9-ce6a-3951-a572-5cab4e6e71d3 | -3.25043 | -52.91556 | 2025-10-30 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 8b31603b-8d22-32a5-be74-3ae842294d17 | -3.92785 | -45.64865 | 2025-10-30 00:35:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b4a6b299-f743-3d29-8b98-bf261f2775a5 | -3.75378 | -50.9491 | 2025-10-30 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9f0ec9f6-2e8a-3b80-9148-0ca3b013e6a5 | -6.61761 | -47.18152 | 2025-10-30 00:35:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6255c492-bbe0-3e03-94e2-3ff223340f90 | -5.38449 | -47.20939 | 2025-10-30 00:35:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 160741d6-ede2-3bf2-85a8-707da2e01a50 | -4.24407 | -50.70574 | 2025-10-30 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README6.md)
