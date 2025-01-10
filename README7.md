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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7978361-d097-3406-9cb1-da552da27410 | 1.94844 | -60.86514 | 2025-01-10 05:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 077acd80-54b6-39ee-b172-2199e9fd1dbf | 1.94372 | -60.86589 | 2025-01-10 05:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e75fdab7-cf7a-387d-967d-6299cd130157 | 2.56911 | -60.69717 | 2025-01-10 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 319ba0ca-301c-37c1-947f-315d62dacfff | 3.17366 | -60.22543 | 2025-01-10 05:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb92e045-0691-35e9-b417-510cc754ac1c | 3.1741 | -60.22227 | 2025-01-10 05:57:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94e134b3-a316-3b5a-99d7-338d3ddd2d5b | 3.70386 | -60.28112 | 2025-01-10 05:57:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16abda2a-cf8f-3f4a-9709-9fe7bb79693b | 1.92915 | -60.41581 | 2025-01-10 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5e885ae6-0fc9-3ceb-a8a7-a2ec7f8d0ff3 | 1.93312 | -60.40964 | 2025-01-10 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 69bba53a-47cd-3589-a992-c00c8fc8b162 | 4.16386 | -60.67945 | 2025-01-10 05:57:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 758d5ab9-1d73-3c7a-8644-7b948a6ad8b1 | 2.56276 | -60.68789 | 2025-01-10 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22c8f114-8acd-334d-bb9f-258c153709ad | 4.16006 | -60.68497 | 2025-01-10 05:57:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d0133c8-0a49-3721-9741-c0e8485438ec | 4.11372 | -60.8598 | 2025-01-10 05:57:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f08daff-c60a-3301-894e-436b8c6d1f8e | 1.93404 | -60.41519 | 2025-01-10 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 20181ea4-e8bb-3990-b676-448c13e7830f | 3.7047 | -60.28624 | 2025-01-10 05:57:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15281176-57cb-334b-8890-6a6f217ada6b | 1.93101 | -60.41647 | 2025-01-10 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 374e4628-a57d-359b-8a1a-7b3834897b08 | 1.92527 | -60.41168 | 2025-01-10 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 796bb971-7170-32a9-b6b6-14fab6bce536 | 1.93014 | -60.41093 | 2025-01-10 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 608ad627-95cb-3d4a-a92d-7bb5d6f7ad58 | 1.34713 | -60.03304 | 2025-01-10 05:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba989f48-e78e-3b5b-85a3-08c7014dce87 | 1.80716 | -61.21198 | 2025-01-10 05:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7a7f4d9-3fd9-3a98-93c2-d60282d21080 | 1.92928 | -60.40548 | 2025-01-10 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cf12b742-0bfd-3948-b276-352a066defed | 1.34809 | -60.03889 | 2025-01-10 05:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4755fc60-9f87-3c56-820c-40376b5b968b | 1.92824 | -60.41032 | 2025-01-10 05:57:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7b5ed84f-b4c8-34db-8c6e-af2ca343d9fc | 3.48249 | -60.16445 | 2025-01-10 05:57:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 383fa090-600a-3e9b-b09e-bde3818d02ea | 3.31261 | -60.53018 | 2025-01-10 05:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c82e2ef-e87a-3f76-babc-f86f6c24cbd9 | 0.6153 | -60.62235 | 2025-01-10 05:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d58cb0a-921b-31b7-84a6-3fb51751c056 | 0.78528 | -60.10659 | 2025-01-10 05:59:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24a7816e-d96e-3076-bd64-0a332465c6fe | 1.38343 | -60.79765 | 2025-01-10 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0069d0b4-6a43-30a4-8114-6d145e58f718 | 0.61444 | -60.61688 | 2025-01-10 05:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc7156f0-3052-35be-8c09-01dcf1e16ba8 | 1.31108 | -60.41099 | 2025-01-10 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3dedab4d-984e-3f12-9558-c70c230189e5 | 0.78414 | -60.10648 | 2025-01-10 05:59:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c760d78b-d7d7-3691-86de-6330b54b994e | 1.30616 | -60.41173 | 2025-01-10 05:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1485125e-6308-371b-865b-b64a74e6a437 | -7.79319 | -35.63516 | 2025-01-10 11:38:00 | TERRA_M-M | BOM JARDIM | PERNAMBUCO | Brasil | 2602209 | 26 | 33 | nan | nan | nan | Caatinga | 19.9 |
| b2c0d787-8def-3fa5-91f5-26f0e46b95f6 | -9.29599 | -35.72871 | 2025-01-10 11:38:00 | TERRA_M-M | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 2fc8f425-0701-38bf-a0f6-0e39551851fc | -17.6664 | -54.1684 | 2025-01-10 13:00:00 | GOES-16 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 97.4 |
| f05718c4-5741-3170-ac6b-127af29ddf58 | -17.6466 | -54.1712 | 2025-01-10 13:00:00 | GOES-16 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 85034815-215c-3dca-887a-1e717daa994e | 1.9236 | -60.4019 | 2025-01-10 13:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 117.7 |
| f83c37f5-e8da-3fc6-9927-dd7dcbca1110 | 1.9236 | -60.4019 | 2025-01-10 13:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 142.9 |
| 7eb219eb-bcd5-3732-a307-76a3560f23a4 | 1.9236 | -60.4208 | 2025-01-10 13:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 4ed63eb0-963a-38d5-8727-75f6d932c987 | 1.9419 | -60.4017 | 2025-01-10 14:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 8125d2b6-3d2c-3103-896c-97fbb66e5269 | 1.9419 | -60.4017 | 2025-01-10 14:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 84.0 |
| bbf48b74-be66-35e2-9dc3-7b7411197433 | 0.6106 | -60.6195 | 2025-01-10 14:10:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 322fe38f-2e88-3b6f-8cb4-ad191b5c41af | 1.9236 | -60.4208 | 2025-01-10 14:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 89.8 |
| f0e4599f-529c-3154-b916-09d95d7b012b | 1.9236 | -60.4019 | 2025-01-10 14:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 136.0 |
| cb161fac-4f8d-3e26-b893-b4c126b3fdfa | 1.9236 | -60.4019 | 2025-01-10 14:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 141.6 |
| 915e96c1-1b16-3df5-a2f9-9caa00e4eb31 | 1.9236 | -60.4208 | 2025-01-10 14:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 31f1f9ff-178d-3383-8991-b1dbfb9183bf | 1.9419 | -60.4017 | 2025-01-10 14:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 3dac0e4f-1807-3eea-9503-5f329e509140 | 0.6106 | -60.6195 | 2025-01-10 14:20:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 138.5 |


