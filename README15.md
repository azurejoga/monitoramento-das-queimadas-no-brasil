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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e81b9d3-97de-3c4d-91fd-7fa193f54232 | -17.4222 | -39.9353 | 2024-10-27 00:56:41 | GOES-16 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 119.7 |
| 534a3c45-5301-3c50-a4df-efdb61ad6443 | -17.4229 | -39.9092 | 2024-10-27 00:56:41 | GOES-16 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 77.4 |
| cf8689a7-dbc4-301c-96e7-2787fb62bde7 | -17.4424 | -39.9298 | 2024-10-27 00:56:41 | GOES-16 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 69.3 |
| 4ff1812e-3a83-30e7-8469-6cb1a936ed99 | -0.9815 | -53.7192 | 2024-10-27 01:05:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 440f2194-68c0-3abf-b7bd-ad5b642cd6d8 | -0.9815 | -53.699 | 2024-10-27 01:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 208.0 |
| fc8dd690-9a42-3070-ae71-eb87899cc1b7 | -0.9815 | -53.6789 | 2024-10-27 01:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 1d1bb9d5-cfc7-3879-bd7c-8eafec0e91d0 | -0.9998 | -53.719 | 2024-10-27 01:05:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| b0c94c21-1190-3474-a1ec-7c63970a4fb2 | -0.9998 | -53.6989 | 2024-10-27 01:05:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 228.6 |
| 615dad77-2f32-34f7-aace-692fcfea3273 | -0.9999 | -53.6788 | 2024-10-27 01:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| aa485ce7-609d-3996-bd49-8d79ee105d88 | -1.1831 | -53.8985 | 2024-10-27 01:05:12 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 69202622-ef49-3b96-bae4-12258985934f | -1.7874 | -46.4065 | 2024-10-27 01:05:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 459f0dd3-99cd-388f-bd31-8f9193053424 | -1.7875 | -46.3844 | 2024-10-27 01:05:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| a9f9fd5f-c6ae-3c61-ae78-e786ab011a65 | -1.8059 | -46.4062 | 2024-10-27 01:05:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| a5043b91-b754-3ad9-8c0d-1c2a69d86f42 | -1.806 | -46.384 | 2024-10-27 01:05:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 3e265079-418b-34fb-b922-949a0df58c14 | -1.9243 | -59.9837 | 2024-10-27 01:05:16 | GOES-16 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 305a8bd4-dc28-3b42-8574-b8fd945b1990 | -17.4272 | -39.887402 | 2024-10-27 01:05:17 | METOP-C | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5e8029ed-769e-32c3-a120-017b4c4221ab | -17.434799 | -39.913898 | 2024-10-27 01:05:17 | METOP-C | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 641ad960-5114-3c6a-819f-0f9e10d4451a | -17.4177 | -39.8904 | 2024-10-27 01:05:18 | METOP-C | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| df38de4e-910f-38f8-9826-b540d32a0430 | -17.425301 | -39.916901 | 2024-10-27 01:05:18 | METOP-C | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a69fa586-f6b5-35ff-9919-b0bfac0c8c93 | -17.4328 | -39.943298 | 2024-10-27 01:05:18 | METOP-C | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e2e40dcf-998d-32c9-a105-91adec10c40e | -17.4158 | -39.919899 | 2024-10-27 01:05:18 | METOP-C | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dfc04045-aaac-3fb8-8872-8e2b836c5eda | -2.3578 | -47.6641 | 2024-10-27 01:05:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 5abbe38b-a103-30cf-b4a3-93148557012a | -2.4567 | -45.8567 | 2024-10-27 01:05:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 94586c10-dc02-35e1-bfb6-3acc0f4c14d0 | -2.4568 | -45.8344 | 2024-10-27 01:05:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 8cab365a-524c-3428-9304-b2ac2343124b | -2.4598 | -50.412 | 2024-10-27 01:05:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 05d04d6c-9a68-3058-b744-e899505e5de5 | -2.4753 | -45.8561 | 2024-10-27 01:05:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 3514fc8f-c895-3abf-a9c9-d213339c4da5 | -2.4753 | -45.8338 | 2024-10-27 01:05:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 32ebddcc-9279-3582-ade6-b218bfed5caf | -2.4786 | -50.2858 | 2024-10-27 01:05:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| c6b1c4aa-f5e5-39c1-be67-a41a0c76461f | -2.486 | -48.0507 | 2024-10-27 01:05:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 4b5391da-60fa-3585-abe8-fe19f09b2631 | -2.6297 | -49.247 | 2024-10-27 01:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 2b2166c6-308e-3e3c-9375-661401fcc3d3 | -2.6321 | -54.2975 | 2024-10-27 01:05:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 78979157-c85c-3d95-a98b-871dd9592fff | -2.6482 | -49.2465 | 2024-10-27 01:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| b941f99d-3ee2-3e1e-826c-cd0a136ae417 | -2.6483 | -49.2253 | 2024-10-27 01:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 77683080-3adb-3dfe-9d65-09d8f3482b7b | -2.6505 | -54.2971 | 2024-10-27 01:05:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 3057c07e-2d9a-39d8-b064-378372eb76d6 | -2.7033 | -49.33 | 2024-10-27 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 1bd80661-1264-3321-9079-3081b9b7b6a6 | -2.7034 | -49.3088 | 2024-10-27 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 3183ff68-bb79-3411-85c3-b3a32cfc2e7e | -2.8145 | -49.2418 | 2024-10-27 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 739b7eaf-d817-3808-a0ca-6b5484bff3c9 | -2.8329 | -49.2626 | 2024-10-27 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| e35810e5-2b27-354c-9a4b-cc74a2aba04f | -2.833 | -49.2413 | 2024-10-27 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 93a01bab-4335-32cb-b93b-ccba93b7e6da | -2.8501 | -45.0131 | 2024-10-27 01:05:21 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 317e3fc9-9438-3e02-bae1-8a3e9f9c9a80 | -2.8502 | -44.9905 | 2024-10-27 01:05:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 19c23bcd-99ff-3e6b-a0f2-9e1b4e53d174 | -2.8687 | -45.0125 | 2024-10-27 01:05:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 100.4 |
| c0240c2c-e829-3b7e-a988-8fdc299c3128 | -2.8688 | -44.9899 | 2024-10-27 01:05:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 2b3e8372-64c9-33c5-9da0-76917badb323 | -2.916 | -51.7716 | 2024-10-27 01:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 2794f8da-3f2d-3a13-bbc7-efd5c95fbe48 | -2.9161 | -51.751 | 2024-10-27 01:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| e032c1fa-dbdc-3e9b-850b-8ead9e5147ac | -2.9214 | -50.295 | 2024-10-27 01:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 36477d1e-98be-3efa-b60c-782b5309cfe3 | -2.9215 | -50.274 | 2024-10-27 01:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| df39b80b-023d-3a7d-a1c6-a57f046b6867 | -2.9345 | -51.7711 | 2024-10-27 01:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| c6179c2a-9df5-3523-af64-3bd23d533344 | -2.9345 | -51.7505 | 2024-10-27 01:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| ef205d2d-3091-31d8-81e8-062551cd1394 | -2.9399 | -50.2735 | 2024-10-27 01:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 9c78d948-ad5b-31db-9919-bbfaa7e89fe9 | -2.9669 | -53.0389 | 2024-10-27 01:05:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a3f942b1-55ec-384c-949e-45b10ddf4ef0 | -3.0888 | -45.6568 | 2024-10-27 01:05:23 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 25200112-bc8d-3b54-9e3b-cd8fe953165a | -3.1106 | -44.9809 | 2024-10-27 01:05:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 100.3 |
| efc225d0-697a-34ed-8006-87573fdc6d3c | -3.1292 | -44.9801 | 2024-10-27 01:05:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 866a7387-a5e6-3853-997d-a1adc48689e9 | -3.1242 | -50.3519 | 2024-10-27 01:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 66c8c1e2-f3d6-3a47-b1b1-306a2dde3fb6 | -3.3256 | -50.7641 | 2024-10-27 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 2f1ef215-6ea6-32aa-8583-3c2709ffa050 | -3.344 | -50.7635 | 2024-10-27 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 45cb0b93-5999-3cfa-89db-ded00f07aef0 | -3.3441 | -50.7426 | 2024-10-27 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| ff4d46fd-816f-3c67-a7fc-e9ef4643cd38 | -3.4762 | -54.5772 | 2024-10-27 01:05:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 3279c536-6c34-3e3c-9467-51f7b4217c44 | -3.4763 | -54.5572 | 2024-10-27 01:05:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 86884bf7-d66f-3380-a1c8-806a50870361 | -3.5626 | -51.4217 | 2024-10-27 01:05:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| d7c3d159-2cef-32dd-b31b-e6ef731ac622 | -3.6615 | -54.2113 | 2024-10-27 01:05:26 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| b47f67eb-0538-34f9-80e3-091f4a4bb63a | -3.6798 | -54.2107 | 2024-10-27 01:05:26 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| b1ef27af-4bef-396f-beb0-337baf8c07e0 | -6.1487 | -47.2651 | 2024-10-27 01:05:40 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 2b56ed8e-d403-38fb-9575-4611ef7276bb | -6.1672 | -47.2858 | 2024-10-27 01:05:40 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 92a2e3a3-7151-3fe1-b44c-90e791511d1a | -6.1674 | -47.2638 | 2024-10-27 01:05:40 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 886b9072-c5a7-3c1f-aa6f-73ccc79ce54a | -6.1861 | -47.2625 | 2024-10-27 01:05:40 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| f19ddf1b-3895-3385-b027-cf4c07449a4f | -7.2264 | -46.0498 | 2024-10-27 01:05:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 2bb00b86-67c7-3af8-bb46-579bb07aa903 | -7.2452 | -46.0482 | 2024-10-27 01:05:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 90304b89-a402-302d-97ee-3580a67bcd01 | -10.5424 | -45.1463 | 2024-10-27 01:06:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 0cb2eebd-df29-3e2d-b3f0-53e83433a9a4 | -15.5522 | -49.757702 | 2024-10-27 01:06:29 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b1c90e51-5e2e-3155-ac6c-a3c4f98b87e8 | -13.073 | -42.108101 | 2024-10-27 01:06:37 | METOP-C | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b6bf2c84-7ba7-310c-a34b-19a3b5d0deb3 | -13.0634 | -42.110802 | 2024-10-27 01:06:38 | METOP-C | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1d3228b0-2d8b-3622-8477-a6b740453946 | -17.4222 | -39.9353 | 2024-10-27 01:06:41 | GOES-16 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 154.8 |
| 1dc3f5b7-f1ad-39eb-b3db-ecaa1dec3832 | -17.4229 | -39.9092 | 2024-10-27 01:06:41 | GOES-16 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 90.1 |
| ebaef330-e407-34dc-b483-c9d05ef00409 | -17.4424 | -39.9298 | 2024-10-27 01:06:41 | GOES-16 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 122.5 |
| 958a68bc-b407-3a42-b768-9cbd8d892f80 | -17.4431 | -39.9037 | 2024-10-27 01:06:41 | GOES-16 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 72.3 |
| e61a0fcf-3f81-3ff8-8eab-ecb7cb045b9c | -10.6059 | -44.2635 | 2024-10-27 01:07:26 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 802abe05-baf7-3d62-a023-ee23d572252f | -10.5917 | -44.248299 | 2024-10-27 01:07:27 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a2c61fd6-fc68-3ee6-acc3-e103790225f0 | -10.5963 | -44.266102 | 2024-10-27 01:07:27 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 25fb35d3-7fb5-30ca-9154-7443fa3b4020 | -10.5724 | -44.253399 | 2024-10-27 01:07:27 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e08da6fc-1b7b-3033-bd69-19a73649b432 | -10.577 | -44.271198 | 2024-10-27 01:07:27 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fac7efa6-b5a5-3971-8c8c-d7798f7f75c4 | -10.5627 | -44.255901 | 2024-10-27 01:07:27 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 85ee37a6-d2f7-383e-bfc4-e54874009d7a | -10.5673 | -44.273701 | 2024-10-27 01:07:27 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6eb1286f-46f9-39dd-b681-190dbf832185 | -10.4422 | -44.549599 | 2024-10-27 01:07:30 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8cc5c350-9aa2-3ab3-82f7-1fd3e15b020a | -10.4466 | -44.5667 | 2024-10-27 01:07:30 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 29e5dd98-d5a5-34e1-94a5-8f44ee8d4905 | -10.5363 | -45.1199 | 2024-10-27 01:07:31 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| df46ae1b-7010-358b-8836-9bccf7136041 | -10.5403 | -45.135601 | 2024-10-27 01:07:31 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| db8391fc-5515-33a6-bfed-8daea8249cd0 | -10.5443 | -45.151199 | 2024-10-27 01:07:31 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ce0c6522-ddbe-32fa-a093-636dec3572d7 | -10.5306 | -45.1381 | 2024-10-27 01:07:31 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bfbbfddc-4941-3618-91e1-951b1ff40b89 | -10.3766 | -45.060398 | 2024-10-27 01:07:33 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 45e8b6c0-f186-348c-8e1c-71cd8b0c2626 | -10.3806 | -45.076199 | 2024-10-27 01:07:33 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 24134a80-e062-30ca-bdfb-5d01365a3818 | -7.2357 | -46.020901 | 2024-10-27 01:08:28 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d13e86f-123c-3e91-bf85-8cad98499725 | -7.2395 | -46.036301 | 2024-10-27 01:08:28 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 739a09e1-ee66-339a-a349-40feb9ce7a60 | -7.2433 | -46.051601 | 2024-10-27 01:08:28 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9201c86c-663f-3c82-b466-86be7731f607 | -7.2298 | -46.0387 | 2024-10-27 01:08:28 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 896734e5-f21d-3e7e-bb95-966e7713bb6d | -6.8232 | -44.450901 | 2024-10-27 01:08:28 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a3dddfd3-6cac-3c3c-9629-ae108c9ffe38 | -6.8135 | -44.4534 | 2024-10-27 01:08:29 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85abd8e8-2c46-36dc-a537-1b9acfe04ba1 | -6.8185 | -44.4734 | 2024-10-27 01:08:29 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09ccd33d-cb17-3667-824d-4986d0deb6d7 | -8.1825 | -50.272301 | 2024-10-27 01:08:29 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README16.md)
