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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a1c60f0-f446-335f-ab31-316547c694c3 | -3.8225 | -44.1522 | 2024-10-28 13:15:27 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 95a9b94b-e9af-3501-8014-c07b3f828b31 | -3.8412 | -44.1513 | 2024-10-28 13:15:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 9d080e1e-8f66-30d6-a202-a8288d6e3c63 | -4.8619 | -42.4622 | 2024-10-28 13:15:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 109.2 |
| 8451c3e9-52a1-3671-a625-e935775813d1 | -4.8617 | -42.4858 | 2024-10-28 13:15:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| c2701180-67eb-3e2f-b6ce-1f01139f1424 | -12.8883 | -44.6143 | 2024-10-28 13:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| be4238ae-df29-3d7f-adfe-8f63ddf90552 | -13.1898 | -43.0957 | 2024-10-28 13:16:20 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 105.4 |
| a1a06cba-e9ce-30ae-9d46-73f93f2689a7 | -2.3762 | -47.6853 | 2024-10-28 13:25:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| dfda0656-1743-3844-bc66-c457c641af3f | -2.3919 | -48.5484 | 2024-10-28 13:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 146.5 |
| bb058003-6f94-3df0-9003-55656f281afd | -2.3763 | -47.6636 | 2024-10-28 13:25:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 525cbcaf-a199-3df5-8e0b-a13b970f8893 | -2.3578 | -47.6641 | 2024-10-28 13:25:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 95eca0bf-a84c-3ee8-973f-6f252a9f95c1 | -2.2513 | -46.2405 | 2024-10-28 13:25:19 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 66.2 |
| e7cb37f3-2c19-3e78-8641-eb3059e0e418 | -2.4104 | -48.5479 | 2024-10-28 13:25:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 146.1 |
| 130fbb3d-c520-36ea-a7bb-4faee9090194 | -2.8515 | -49.2408 | 2024-10-28 13:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 178db130-0530-3b55-9a71-faeb050aec8a | -2.8885 | -49.2397 | 2024-10-28 13:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 156.2 |
| f842ca37-1220-3eaf-b672-f61146025cbe | -2.8739 | -53.3252 | 2024-10-28 13:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| e570836f-e89b-3621-8228-2c6a44325a1f | -3.8225 | -44.1522 | 2024-10-28 13:25:27 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 061e8b66-2831-327d-9d25-946d80b9aba2 | -3.8412 | -44.1513 | 2024-10-28 13:25:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 1b7a8876-f40b-34b5-be42-0becc1108b70 | -3.8413 | -44.1283 | 2024-10-28 13:25:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 1bcd56f8-ef48-3fff-a67c-6b09f54d3522 | -4.8617 | -42.4858 | 2024-10-28 13:25:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 97.7 |
| 9a31a11e-7559-33ac-8280-1f3b45bb478c | -4.8619 | -42.4622 | 2024-10-28 13:25:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| d833156b-1153-3b31-bf3b-8e60a6737ef8 | -5.455 | -43.2192 | 2024-10-28 13:25:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| d0348acf-6b02-3aa2-9500-d964b97013dd | -12.8883 | -44.6143 | 2024-10-28 13:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| d7e7be38-8d2b-34f4-aaeb-f38d371fc753 | -13.1898 | -43.0957 | 2024-10-28 13:26:20 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 114.5 |
| 20bcc0a6-c15f-3ada-9775-9bf8be916239 | -13.8157 | -42.8597 | 2024-10-28 13:26:23 | GOES-16 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 0b8b25ee-0e49-3c09-b74e-3ce98b2e64eb | -1.4892 | -47.2035 | 2024-10-28 13:35:14 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 5bec035f-d134-3cef-b3d1-ec78f75bbf0d | -2.3763 | -47.6636 | 2024-10-28 13:35:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 0079e35c-46cf-39e5-a4f0-7732c654671e | -2.3919 | -48.5484 | 2024-10-28 13:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 198.7 |
| ab59efd3-0118-33b2-8eea-b4b23cbf8d8e | -2.3762 | -47.6853 | 2024-10-28 13:35:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5bb35ffe-2b37-3f1d-bcff-0bb4acd3e958 | -2.8146 | -49.2206 | 2024-10-28 13:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 8688054a-ead4-32a8-a2b7-9b2557beb5a0 | -2.8556 | -53.3256 | 2024-10-28 13:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| daa2e709-8e34-3ead-ad22-79fd554561d9 | -2.8515 | -49.2408 | 2024-10-28 13:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| fece0016-ee7e-38b0-b0ab-f5c64ef8570c | -2.87 | -49.2402 | 2024-10-28 13:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 697.0 |
| 73b456b1-8f7d-30f4-81b6-39c08cc365cf | -2.8739 | -53.3252 | 2024-10-28 13:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 374c49c1-3d8e-3560-a010-34d3cbef0f56 | -2.8885 | -49.2397 | 2024-10-28 13:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 245.9 |
| 0e9558b9-6e19-3bfc-af5e-9cf0ac86e109 | -3.8225 | -44.1522 | 2024-10-28 13:35:27 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 94740779-74ee-3024-b66e-227da81c9e1b | -3.8412 | -44.1513 | 2024-10-28 13:35:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 153.9 |
| 2ffa6e60-a3b4-3f6a-b868-4cf3ade28f8d | -4.1639 | -43.2792 | 2024-10-28 13:35:29 | GOES-16 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 5baf17b9-79f0-3aa4-83e2-8bfe8b257f4e | -4.8619 | -42.4622 | 2024-10-28 13:35:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 106.2 |
| bc98cb03-22ad-3da9-a409-18472f188565 | -4.8617 | -42.4858 | 2024-10-28 13:35:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| 068f67cb-12d3-3343-8aba-47ce2b839db7 | -5.455 | -43.2192 | 2024-10-28 13:35:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 2203d22b-238f-3768-9dad-01eaf44086bd | -6.225 | -41.2548 | 2024-10-28 13:35:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 180.2 |
| 12360d02-9235-383b-bfa3-c03813c6ab40 | -6.2439 | -41.2531 | 2024-10-28 13:35:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| b46685a4-c12b-3a1d-8113-691992d656e3 | -6.6813 | -40.8958 | 2024-10-28 13:35:43 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 786c9f06-6e69-34c9-a685-aa4862ea808a | -12.8883 | -44.6143 | 2024-10-28 13:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 6750270e-7dc9-3014-ba29-0f341032188c | -13.1898 | -43.0957 | 2024-10-28 13:36:20 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 97.8 |
| 26ca628b-3169-3cd4-b97c-4f1f0467cfd0 | -13.2685 | -53.7062 | 2024-10-28 13:36:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 36ca49de-91d1-30c8-a741-ede7beffb764 | -1.3932 | -49.0387 | 2024-10-28 13:45:14 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| d3b3ca78-ff0f-35c3-ba80-82de5e589aa7 | -2.3919 | -48.5484 | 2024-10-28 13:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| d5ed12c6-a1c0-3dad-a736-50b9399c2418 | -2.3763 | -47.6636 | 2024-10-28 13:45:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 164.0 |
| ae5561c4-d53f-3311-b51e-862d05a37219 | -2.3762 | -47.6853 | 2024-10-28 13:45:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| afcd29e0-07b6-3795-a99f-e3b6fad65ae3 | -2.3578 | -47.6641 | 2024-10-28 13:45:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 06ec53e7-70ab-3fdd-a53a-4e4c2c2576da | -2.8146 | -49.2206 | 2024-10-28 13:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 62a1d8d2-0c70-3fc7-8991-470437ff1b88 | -2.833 | -49.2413 | 2024-10-28 13:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 4ec3cb7a-fd00-3fb0-871b-902bc1bf6c42 | -2.87 | -49.2402 | 2024-10-28 13:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 984.6 |
| 2226f1e3-6154-3642-813d-1c934e4225f2 | -2.8885 | -49.2397 | 2024-10-28 13:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 470.6 |
| 6b22b02f-a4fa-368e-bb65-ec4a5097bae5 | -2.8515 | -49.2408 | 2024-10-28 13:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 211.4 |
| d7c896f8-cbd7-3973-925f-b7c7a6a32f1c | -2.8556 | -53.3256 | 2024-10-28 13:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| dab8136c-1192-3c89-b4db-402989788185 | -3.0917 | -54.1666 | 2024-10-28 13:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a11cd596-9e5a-35cc-97c5-104ce349a6e4 | -3.8225 | -44.1522 | 2024-10-28 13:45:27 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 8f863a7f-b990-30d4-9fb7-2881bfdb3592 | -3.8412 | -44.1513 | 2024-10-28 13:45:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 195.8 |
| 8a47504f-df9f-3c58-a87b-576042bbb8ea | -3.8411 | -44.1742 | 2024-10-28 13:45:28 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 2acccbb7-ae40-3561-9d51-8fe333008082 | -3.8413 | -44.1283 | 2024-10-28 13:45:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| dcc3d156-44e5-32a8-a563-c85767b51699 | -4.447 | -42.8889 | 2024-10-28 13:45:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 1d3ccc49-a217-3e2a-bcd0-b740cee77bd5 | -4.8617 | -42.4858 | 2024-10-28 13:45:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 109.0 |
| 5cfdf39d-152e-339b-83f2-3844caff4ad7 | -4.8619 | -42.4622 | 2024-10-28 13:45:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| a214aa02-3c9a-3402-ac79-7c83e39ccd0d | -4.9496 | -43.2078 | 2024-10-28 13:45:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| d0bb4347-21d7-3b8b-b1f1-ade812b34ad0 | -5.455 | -43.2192 | 2024-10-28 13:45:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 0a903a2c-a67c-3656-b05b-b7cbe3ff6a11 | -5.68 | -43.2024 | 2024-10-28 13:45:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 8ec7d074-7592-381f-b33d-2aa2343b461f | -6.0782 | -44.719 | 2024-10-28 13:45:40 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 01c1cd24-8164-3e6f-b998-17d72c9e4426 | -6.2248 | -41.279 | 2024-10-28 13:45:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 740297f2-b37d-37e0-8626-631808b0bb8a | -6.225 | -41.2548 | 2024-10-28 13:45:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 82.4 |
| b266fd55-bb40-3e9a-bfd5-eccc7e1b44f2 | -6.6813 | -40.8958 | 2024-10-28 13:45:43 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 36c66dd2-1e2e-31b4-b88a-8964e3b252b7 | -12.8883 | -44.6143 | 2024-10-28 13:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 1710e6c6-fc21-39af-9c61-5e62530146e4 | -13.1898 | -43.0957 | 2024-10-28 13:46:20 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 114.3 |
| ae901878-e4c5-3ca4-a3da-79a52acf1b80 | -13.2685 | -53.7062 | 2024-10-28 13:46:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 2d1c57cf-f07f-32bf-a36f-614d395abe24 | -13.2874 | -53.7248 | 2024-10-28 13:46:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 7d0cce16-149d-398c-8bb0-9138371569bd | -1.4116 | -49.0384 | 2024-10-28 13:55:14 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| fbe9c9e1-5f0d-34b9-9416-20fa91193a47 | -1.3932 | -49.0387 | 2024-10-28 13:55:14 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| c344e3cf-2ed9-397c-9a6e-459fea251a20 | -1.4707 | -47.2038 | 2024-10-28 13:55:14 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| f7681f18-98b3-31d1-b3fe-14ae7378232e | -1.3747 | -49.039 | 2024-10-28 13:55:14 | GOES-16 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| fcbaa4ea-b1e5-31a8-aca7-d6dabd912be7 | -1.3743 | -49.273 | 2024-10-28 13:55:14 | GOES-16 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| a0ef4d83-f1fb-397b-9b2d-9f12851bcff5 | -2.3578 | -47.6641 | 2024-10-28 13:55:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 6e051aa7-f35d-32cd-9f1d-bd08c10efd52 | -2.3055 | -46.6811 | 2024-10-28 13:55:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| e2db5297-884b-3160-afd2-8c2e3e7eec54 | -2.3762 | -47.6853 | 2024-10-28 13:55:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 365f77d0-022f-353a-bad9-a2119bb5b75e | -2.2664 | -53.7221 | 2024-10-28 13:55:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 137.1 |
| d3a4b3b6-9c67-3e13-a102-104ec3f005fc | -2.3763 | -47.6636 | 2024-10-28 13:55:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| d315c012-6c8b-36a2-a558-2a8b1e627a19 | -2.3055 | -46.6591 | 2024-10-28 13:55:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 2b8b0d5f-bd22-3f05-a510-0b3db1df2d96 | -2.3919 | -48.5484 | 2024-10-28 13:55:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 85cbbc6f-6c3d-3cc1-8859-0764082eae02 | -2.4104 | -48.5265 | 2024-10-28 13:55:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 1ff90e0e-42da-3f51-9c11-5fc2b159fff3 | -2.8885 | -49.2397 | 2024-10-28 13:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 186.5 |
| 89e57119-a838-3602-aee4-597ecec11454 | -2.87 | -49.2402 | 2024-10-28 13:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 329.1 |
| 81d05ee4-6c50-38a9-9426-53646072b082 | -2.833 | -49.2413 | 2024-10-28 13:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 3323a8ff-ce3b-3e4d-9616-58b30596a911 | -2.8515 | -49.2408 | 2024-10-28 13:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 3b19eace-b1d4-3e64-af92-1911f3afeb3a | -3.8225 | -44.1522 | 2024-10-28 13:55:27 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| a083d29f-5515-3b29-b640-0e683a349b31 | -3.8412 | -44.1513 | 2024-10-28 13:55:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| b2262a09-ec77-3180-99ed-a520577750d0 | -3.8413 | -44.1283 | 2024-10-28 13:55:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 917d067f-20a5-3dcd-b8aa-bb78c91b3d1e | -4.447 | -42.8889 | 2024-10-28 13:55:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 29bff26e-d10a-3779-97d5-d5d914b53eda | -4.8619 | -42.4622 | 2024-10-28 13:55:33 | GOES-16 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| 5681708a-526a-3e00-85ee-80f4e2982353 | -4.8617 | -42.4858 | 2024-10-28 13:55:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 125.6 |
| 4ce55862-9974-3681-b0bd-a494e61da628 | -4.9498 | -43.1845 | 2024-10-28 13:55:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |


[Clique aqui para ver as próximas entradas](README87.md)
