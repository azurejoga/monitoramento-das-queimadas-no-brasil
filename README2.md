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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e398005c-1fb3-3b6f-a1e5-e5c52fae58c0 | -12.3779 | -54.7472 | 2026-05-01 01:00:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 72f6c33f-a25c-30a9-8839-fd16a6bf542a | -10.9978 | -45.069302 | 2026-05-01 01:00:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 68282d15-d776-33b5-b83d-380721f7fd33 | -20.0599 | -50.458 | 2026-05-01 01:00:00 | METOP-C | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 41837000-c349-3ca5-9d0e-6a1bb0a9df5e | -12.3876 | -50.035301 | 2026-05-01 01:00:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c609aa64-e30c-37d3-a209-f25873760763 | -11.4381 | -55.101002 | 2026-05-01 01:00:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d2fe3e0-5999-3a9d-9abc-d3b4fa126ce3 | -12.376 | -50.029999 | 2026-05-01 01:00:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d7af14d-99b6-3951-8df9-7c0c16be8555 | -10.9811 | -45.1104 | 2026-05-01 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.1 |
| d903b772-b9e4-315b-9363-08ebe4838eff | -11.0006 | -45.0847 | 2026-05-01 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 4839df72-3dc9-348c-a0ac-873e5a884e54 | -10.9624 | -45.09 | 2026-05-01 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 337ab928-3584-35c7-be0d-15fcb49284c2 | -10.9815 | -45.0874 | 2026-05-01 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| b402a1d8-9d28-3e34-b843-7403f696fb3e | -10.9819 | -45.0643 | 2026-05-01 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 9c43fcf7-22bf-3e83-bf48-16c6bc6072e4 | -11.001 | -45.0617 | 2026-05-01 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| bf70897d-a89f-3fa9-b1aa-c724507cc087 | -10.9624 | -45.09 | 2026-05-01 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| db08a556-eb5c-3dff-aa71-ae1697f811c0 | -10.9819 | -45.0643 | 2026-05-01 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 60cba330-5797-3222-8e36-16ab957ef6b1 | -10.9815 | -45.0874 | 2026-05-01 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 207.5 |
| bda5bf80-7564-3fb5-9477-9367ac718791 | -11.0006 | -45.0847 | 2026-05-01 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| df6aeb1e-b9ba-3445-92e6-acd3ca2b3b23 | -10.9624 | -45.09 | 2026-05-01 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 29ea1125-33c2-359a-8cb3-9112772394e0 | -10.9819 | -45.0643 | 2026-05-01 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 6a1dbd23-c8ec-3859-a1c8-3bdf11677a2e | -10.9811 | -45.1104 | 2026-05-01 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 18792f43-4c99-3102-b326-022a1ead271c | -11.0006 | -45.0847 | 2026-05-01 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| aa0d7a20-9b9b-34c5-a15e-cede1173778d | -11.001 | -45.0617 | 2026-05-01 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| d7121c1e-ad70-39cc-a99e-6c0ba27b8a28 | -10.9815 | -45.0874 | 2026-05-01 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 326.9 |
| 091da5dd-308a-3acc-b075-ef9e413ebc6a | -10.9624 | -45.09 | 2026-05-01 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 1fa1a72a-cbce-36f2-bbe7-dd878005d4f5 | -10.9811 | -45.1104 | 2026-05-01 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 906cf754-ba64-37ac-bd5e-8cadd790fe6d | -10.9815 | -45.0874 | 2026-05-01 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 373.1 |
| 15b55a32-1501-327b-93ce-8a6560239510 | -11.0006 | -45.0847 | 2026-05-01 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 19c8b728-3903-3bf9-a929-ad3cfb65ebdb | -10.9819 | -45.0643 | 2026-05-01 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 1166d32f-d94e-31bb-9afd-580a000682a9 | -10.962 | -45.113 | 2026-05-01 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 0baa7299-23da-3250-9d10-e50a21402259 | -10.9624 | -45.09 | 2026-05-01 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| c49ac503-28d3-3e48-957b-9385f35728ce | -11.001 | -45.0617 | 2026-05-01 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| d6bed4cd-52e7-393f-8acd-813caffc817b | -11.0006 | -45.0847 | 2026-05-01 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 9c8ef3f8-0bf9-38ad-872d-89f67e4d85a7 | -10.9811 | -45.1104 | 2026-05-01 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 06a33b0c-a92e-37a6-8741-44f89bc3f85f | -10.9819 | -45.0643 | 2026-05-01 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 4cd8a33d-080d-35ce-951b-8943a1c38cf5 | -10.9815 | -45.0874 | 2026-05-01 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 359.8 |
| 1d302fbe-d92a-313d-b207-63da461a6036 | -10.9819 | -45.0643 | 2026-05-01 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.4 |
| e8295767-3a17-3867-8155-2ae35af31263 | -10.9811 | -45.1104 | 2026-05-01 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 51b6c4bc-c604-3480-a8d5-2af14e97581b | -11.001 | -45.0617 | 2026-05-01 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 55b0a0d0-3c3f-3d45-a327-72ec0cb4097a | -10.9624 | -45.09 | 2026-05-01 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 433c6293-fd3a-3978-87b4-d9a2c0deb6f0 | -10.9815 | -45.0874 | 2026-05-01 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 383.7 |
| 3e7b3356-df67-3063-ba15-1c1f6941b7a7 | -11.0006 | -45.0847 | 2026-05-01 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| efeeba40-f555-3e5e-b93a-755b6ae12c32 | -10.9819 | -45.0643 | 2026-05-01 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 0d006712-462f-3938-b6e5-4e82c8988414 | -10.9624 | -45.09 | 2026-05-01 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| b5148fa5-0340-3eeb-a3a5-5bbe08e91c9b | -10.9815 | -45.0874 | 2026-05-01 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 394.3 |
| d555430b-63d2-3e3e-9336-83d3c72e7548 | -10.9811 | -45.1104 | 2026-05-01 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 0089d9cb-c444-351e-824f-97bfb7a76948 | -11.001 | -45.0617 | 2026-05-01 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 4eb71ba6-3c81-3410-919b-08dce2079a42 | -11.0006 | -45.0847 | 2026-05-01 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 20aeb3da-7350-3ac1-a72f-e4208d9f08d7 | -19.09497 | -40.66823 | 2026-05-01 03:08:00 | NOAA-21 | ÁGUIA BRANCA | ESPÍRITO SANTO | Brasil | 3200136 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 232d478c-0045-3669-88d4-b16859a0c237 | -18.89708 | -39.9254 | 2026-05-01 03:08:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 95f5e450-aa1e-352a-9bb4-e64862c2fa5b | -19.09619 | -40.66637 | 2026-05-01 03:08:00 | NOAA-21 | ÁGUIA BRANCA | ESPÍRITO SANTO | Brasil | 3200136 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 931618fc-7e22-3400-be98-572ce9bc67cb | -18.89121 | -39.92399 | 2026-05-01 03:08:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c50608d8-5d56-32e4-95e8-fdda0db1ed83 | -19.09514 | -40.67101 | 2026-05-01 03:08:00 | NOAA-21 | ÁGUIA BRANCA | ESPÍRITO SANTO | Brasil | 3200136 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 06059551-a507-3e8b-9a86-d0ad10c0dde1 | -10.5457 | -37.20533 | 2026-05-01 03:38:00 | NPP-375D | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f1280a74-820d-3083-b098-d0a17638dc3b | -8.22982 | -43.88361 | 2026-05-01 03:38:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2f554a3-ba7a-3b4c-960e-6838717681b1 | -8.22895 | -43.88829 | 2026-05-01 03:38:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 80708657-7e72-3f74-b18f-d8ea2c994391 | -10.9815 | -45.0874 | 2026-05-01 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 361.5 |
| 1955d05c-58ba-33d5-bac2-7293e9dcf03e | -10.9819 | -45.0643 | 2026-05-01 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| ca9c92be-b745-3fb6-88bb-3227edc34c5b | -10.962 | -45.113 | 2026-05-01 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 585fcecc-e9a3-352e-906b-a59a0861d240 | -10.9624 | -45.09 | 2026-05-01 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| a2888cf3-486c-3264-a1af-978efbc41edd | -10.9811 | -45.1104 | 2026-05-01 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 3c7065b5-bc4b-344c-9d86-6cd9c6ad2d67 | -11.0006 | -45.0847 | 2026-05-01 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| b71eda02-6631-3650-8612-f822909e7419 | -11.95174 | -43.38751 | 2026-05-01 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7d8be86-a19b-32c3-bcf3-3121f875d910 | -10.74712 | -44.3102 | 2026-05-01 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0b35afc-628d-3e23-a59d-f6084052194a | -10.98381 | -45.08779 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 0f13f32c-6003-3e23-8581-8418b3cd470c | -10.9722 | -45.0806 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 11db0652-aaeb-372c-97c7-1a1f2a89860b | -10.9671 | -45.10613 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| dd055e4e-91c0-34d5-a9b2-04ba2be1d909 | -10.97119 | -45.08566 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 9a871f4f-2773-3466-8bcb-8a587da37b29 | -10.98909 | -45.09404 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 186340f6-1a18-3da0-82d7-2d2b15faec67 | -10.98179 | -45.09796 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a6df5a2b-c0e9-3905-bb90-c15dfcfd97eb | -10.97949 | -45.07674 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 985f64fd-83fa-3b88-8935-bcfa214af5af | -13.36595 | -39.91312 | 2026-05-01 03:40:00 | NPP-375D | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8e3f7e4f-a840-39fd-8f8c-c6f35b787290 | -13.36679 | -39.90855 | 2026-05-01 03:40:00 | NPP-375D | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 1f9f1748-0152-3f2e-9671-8ea8706914ac | -11.94768 | -43.37875 | 2026-05-01 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcc8b141-2d7e-3db8-8b49-a6ac27c42fb6 | -10.96388 | -45.08961 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95fe397f-9c91-3e56-b34c-15492ff9d9d3 | -10.54605 | -44.33522 | 2026-05-01 03:40:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0b0d3b92-06bd-3ef7-9e12-345a1f08a256 | -10.9901 | -45.08895 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| b4f47fa3-c658-368e-b12e-a7edea16284e | -12.28154 | -44.62825 | 2026-05-01 03:40:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5102e01c-f3b5-312d-9ef4-3b8eccdfb13c | -10.97851 | -45.0817 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 8b41e325-676b-351f-9339-cb79b2dd4958 | -16.78011 | -45.8092 | 2026-05-01 03:40:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9961d26-f2b0-3f17-80b3-23539b8ed731 | -10.9848 | -45.08284 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 3227dd74-1fbe-3cfa-8b58-8aa9724e25b7 | -10.97019 | -45.09069 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.6 |
| d8c536f9-2208-3503-b461-57ecb3b6b8ee | -10.96814 | -45.10092 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 204f2083-57e3-39fc-9c12-d521142c94ee | -10.55206 | -44.33653 | 2026-05-01 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b0f7fddc-1e28-3b56-91e9-0436f9a92cb8 | -10.97751 | -45.08669 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.6 |
| addce195-1b7e-3f43-88a1-fc6503ec6a0c | -12.28273 | -44.6305 | 2026-05-01 03:40:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ca912e7-e5ad-3aed-a997-c82b60158cc3 | -10.96918 | -45.09573 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 2a507a9b-3c7b-3635-bc24-b83a0eede7ac | -10.99109 | -45.08398 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 3b440d82-de56-3fde-aec1-9f497eabac7b | -10.55116 | -44.34108 | 2026-05-01 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 621663a7-411e-3661-a76c-c7a3b6a96ae0 | -11.95247 | -43.38375 | 2026-05-01 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78144777-2258-3848-bce2-a4653ea05fa7 | -10.98281 | -45.09283 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| b85f45af-4cd4-3cb9-8998-28d135c2bf0b | -10.97549 | -45.09681 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.6 |
| a605a1a5-075d-3921-b31e-9a4c6846c7e2 | -10.74531 | -44.31224 | 2026-05-01 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 982934cb-95a2-3d15-acc3-a23cde521ef5 | -12.28365 | -44.62607 | 2026-05-01 03:40:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44c2cc21-c8e4-3682-b61c-adffce27c16e | -10.97445 | -45.10201 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.6 |
| e58410b6-b328-37bc-ad46-d1c8f6ae4bb8 | -10.9734 | -45.10727 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 06ae3c3f-0f5f-3877-a0a8-61c41a55d35f | -10.97651 | -45.09172 | 2026-05-01 03:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 0575cbff-2f0f-367a-addc-37a978cfb3ab | -10.55807 | -44.33785 | 2026-05-01 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d6cb94a6-068d-35a8-9fc5-9ce49b57e11c | -20.21235 | -46.45746 | 2026-05-01 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a5f37e5-8a17-381a-870f-9d68a6a3ddfa | -20.21282 | -46.45492 | 2026-05-01 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c10d4f28-0081-372f-9dd4-02e3fd896307 | -20.20514 | -46.46231 | 2026-05-01 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c2fc60a5-5987-358f-8c54-5f25e29dc014 | -21.94971 | -48.04397 | 2026-05-01 03:42:00 | NPP-375D | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README3.md)
