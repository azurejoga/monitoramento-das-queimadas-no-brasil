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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d7d7451-309f-3063-b633-870e18ee7341 | -2.78649 | -49.48039 | 2024-10-30 04:19:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88db2333-9bb6-3865-86df-05385fcf61f2 | -3.5654 | -50.03258 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12a81e11-a493-3abe-accb-602e4861493a | -3.36035 | -50.16112 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64b9a470-fe76-339a-9ad5-43a425cb3c4c | -3.3245 | -50.12667 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0965356-407d-37e6-98ad-2773096e6326 | -3.22835 | -50.1904 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33d54e54-747c-3c5a-819c-cdc2beb2af0b | -3.22535 | -50.18116 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0533ad58-6cf6-3d3f-be5e-f649986afbfd | -3.22399 | -50.18961 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 61439a08-d567-3b0a-a32e-90392a1d5e91 | -3.12514 | -49.29285 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 84c1dbbc-0df9-3b23-b85c-432513afa6f6 | -3.12453 | -49.29661 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c804fd01-e61c-375d-98e6-5b0f634b3fed | -3.12041 | -49.29595 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6846012-c93d-3a7b-851e-33e06fcfe3b3 | -3.11628 | -49.29532 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24755886-a115-3c32-b262-262d116745c6 | -3.00447 | -49.58545 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6769e8e4-4f44-34dd-b6dd-4ceb7ea5e18a | -3.00383 | -49.58931 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4a433b03-f626-3d25-a10b-7720e7cd2421 | -2.97216 | -49.10247 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab9cd0f5-7373-3042-845b-0d6ef7900472 | -2.97159 | -49.10606 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7bfbad3a-286b-34cc-8765-ea9ade41af79 | -2.90696 | -49.45938 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95d7940d-d8c1-3348-a580-fedefe0a8bf8 | -2.85357 | -49.39217 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa9aec9e-0c37-34c4-a2a0-61dbeb2ee303 | -2.84173 | -49.24046 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 91ccd0bd-2fad-37a9-9160-bb715247c496 | -2.84114 | -49.24418 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3b5b1109-4a19-35c9-840f-416bacdc272d | -2.8382 | -49.23607 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0eab5294-f3db-330f-ad82-336101a5d769 | -2.83407 | -49.23542 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a870d0d9-73ab-3cb3-996d-01f6e0b69c09 | -2.83348 | -49.23914 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4171b6a0-4f1f-3d34-b2b9-bf6f160a7242 | -2.82641 | -49.23039 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8def6feb-4119-3be1-8794-a380cb951d30 | -2.82582 | -49.23411 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 454c970a-afdc-38de-9e6e-c3f50dc6dca7 | -2.82169 | -49.23344 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 301b27e5-c1f3-3a45-a0c3-de182a664df5 | -2.81169 | -49.21669 | 2024-10-30 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1d30f1a0-cd84-3fa2-b8fd-3cb505c1b659 | -3.51583 | -50.47466 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca4176e0-0f60-353c-93b0-7eeef2cc583f | -3.51271 | -50.47126 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac9b443e-5d86-3d19-9898-ddae5ac6a473 | -3.51138 | -50.47401 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c3e9fc59-1504-3d05-8300-7857d327db42 | -3.3566 | -50.26456 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6135dfb5-44f1-3222-9b4f-c1c1583e52ab | -3.31867 | -50.30253 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76800eaf-be03-38dc-a49a-0a5d4f345e4d | -3.28918 | -50.23373 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91bf37dc-c507-33b3-9863-a625779f3de8 | -3.2885 | -50.23788 | 2024-10-30 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 042e16d6-d452-3ed2-91bc-f04c3808d104 | -3.26661 | -50.34425 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 28786188-9612-33e0-917d-6be35ab7a46c | -3.26219 | -50.34356 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e6d34ff7-1a48-37b2-89e0-8783ff068ec7 | -3.26148 | -50.34789 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a286bbab-8457-34c4-9e79-c62b5490a06a | -3.25777 | -50.34285 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3a259d4f-b3c9-3b95-974f-575ca2b99916 | -3.25706 | -50.34719 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 465c868f-4b7e-3863-b76a-9ad0b362656b | -3.25634 | -50.35152 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 57e6f563-e688-386d-a05a-72b20f632989 | -3.25121 | -50.35511 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a23ea8bb-f3bc-3452-a5e3-946fcb0ecee8 | -3.23211 | -50.58315 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 203694d5-d30b-35a9-94aa-75f1fbb0f2b0 | -3.23064 | -50.59215 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f2b11c85-462e-3776-b6ca-6e9f8da4558c | -3.18408 | -50.38166 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 624ab143-2755-3a29-8067-4e2bbc83bf1a | -3.17815 | -50.59024 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 36f430a3-dddf-3540-ba9b-286afff8cc10 | -3.17682 | -50.39841 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 276994a2-06fc-3e2e-9951-b9c0242b0221 | -3.17591 | -50.58807 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 290cb7aa-6816-3072-8d45-c18b4ea982ac | -3.17438 | -50.585 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 79ce9a02-c10f-3346-b8f6-d65b5f1612c9 | -3.17365 | -50.58952 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5958486e-4335-38e8-9a07-7cc2d51af05a | -3.16988 | -50.58427 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5e2c8377-1769-3d41-b7da-b78895a21ee8 | -3.16465 | -50.58806 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 55b90833-60a8-3943-87be-2d9f0095ab74 | -3.06896 | -50.50904 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d62b15e-69b4-3854-a346-b82a80e6bb25 | -3.06792 | -50.50362 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ab51915-85dc-340a-b60d-06fd97e3375b | -3.06717 | -50.50808 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5bf531b8-4f7e-3d52-a324-100aa920bd13 | -3.06519 | -50.50388 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54483b67-ff18-34a7-9f37-e2e228d9e6f9 | -3.04379 | -50.40944 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26f30bfe-84e4-35a6-bb2d-c7b902bf766a | -3.04307 | -50.41386 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72956c05-bbab-344e-bbe7-e8894c074b7e | -3.04234 | -50.41834 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3532c505-0052-3002-bbc4-bbc6dbd9607f | -3.02525 | -50.41097 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 138b32b9-4732-37b8-8502-e799cdb263c0 | -3.02453 | -50.41538 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f10da014-2a66-395e-9633-b0294b7952fc | -2.97323 | -50.47585 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae90aaf2-43af-3af4-aed0-453aa76e7b47 | -2.96522 | -50.48068 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1e84cd2e-8228-327f-814f-e4a6563c4aa2 | -2.96354 | -50.47877 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbcf6281-101b-359c-9ebe-0c313e3df96d | -2.96278 | -50.48333 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3935fb1-d235-3110-9787-96a68d16430a | -2.96075 | -50.47988 | 2024-10-30 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e7b0102-afca-3089-8824-e8a56ea0766d | -4.97619 | -49.7703 | 2024-10-30 04:19:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc5dce44-599d-3638-bd47-20f6410e2084 | -4.84652 | -50.76465 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 267b6313-157b-307d-943a-4d946a1d339d | -4.71043 | -50.73886 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2a08219-df27-3545-8f16-fa98923386b2 | -4.60431 | -50.56318 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3da68155-0bcc-347f-aac6-e2aa0d2936c5 | -4.56599 | -50.41068 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9e5d6d89-20a0-3788-a23e-26d1110090cd | -4.5653 | -50.41486 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5c173832-867e-3102-afbf-d5af37bd8164 | -4.56166 | -50.40989 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22046052-400c-3336-bbe5-01b484004f67 | -4.55884 | -50.50831 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bacda9a6-9e10-371f-ae5d-2e59c24745ab | -4.55814 | -50.51258 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c6aa54b-436a-358d-912a-2e10fcd961bc | -4.50226 | -50.19308 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6d41adee-bcbd-3a8b-8bd2-2a4595feb9a4 | -4.49796 | -50.19246 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d3f44e35-c3eb-327c-8903-62c7449c8aff | -4.47365 | -50.25964 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b365822-6ec5-3225-a87f-71bcfe289494 | -4.42914 | -50.15681 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d909fee8-fc62-3a7b-a1e7-ec6e355e334c | -4.42845 | -50.16084 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f28780a-b965-3ce2-9262-ebc40f1a4e63 | -4.42601 | -50.46598 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb1f236e-552f-3d69-ac83-d674ca463547 | -4.40252 | -49.63177 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0a9b12b-4e8b-3c33-ae9b-529a52b2c2a8 | -4.39507 | -50.32016 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45d1ecc4-f8d9-39a4-a9e5-b5f2f9d2b0ff | -4.29472 | -50.73971 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 897dae8e-3aef-3c8e-b105-522a824125d2 | -4.26621 | -49.96441 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 883a17a5-748d-310c-ae98-13a70de975ee | -4.26566 | -50.6671 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| b20e2297-6f28-3cd3-bcac-694765fc7f3f | -4.26492 | -50.67149 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| f33ebd39-4614-32bc-aa6f-db98eb7cb35d | -4.26416 | -50.67597 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 00d9ce23-497d-3ae4-9400-6bced5cdae9c | -4.26194 | -50.66208 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 7ef12439-83cc-397c-9e35-3965fc3dbabd | -4.2612 | -50.66645 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 5974326b-3cf6-3a81-9e0e-f9f19f68f7d8 | -4.25971 | -50.67529 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 78ef280e-a5da-3603-9891-f34522d5c7bb | -4.08174 | -50.52434 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2bfb9be-cb53-3a80-9c9c-a0249c93ab2b | -4.07733 | -50.52362 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f90fafb-4430-3f4f-b3bb-5b48a1c18bfe | -4.0748 | -50.01963 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 884468ef-f9a2-3844-920a-3c111cffbca7 | -4.07252 | -50.00691 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 335636ba-4925-34f1-8d78-1f84333e969b | -4.07053 | -50.01899 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| e96db603-c990-3803-80b5-61384768973b | -4.0676 | -50.01025 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2ec41da-448f-33d8-8987-4633e52ddb93 | -4.06658 | -50.0429 | 2024-10-30 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f68cc248-c55b-301c-bb73-3f77327aa705 | -4.06627 | -50.01826 | 2024-10-30 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4625af96-e9ae-347b-9086-eb12aa28f541 | -4.04055 | -50.55334 | 2024-10-30 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c97b6798-eb27-30db-b25c-a41f8c61d514 | -3.87094 | -49.99252 | 2024-10-30 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec99aa7b-69c2-39d3-b7e6-aa86ff9df7a1 | -3.86668 | -49.99176 | 2024-10-30 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README44.md)
