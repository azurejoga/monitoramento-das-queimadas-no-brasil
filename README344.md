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

## Dados Diários - Página 344

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3a404b0-a75f-372a-b165-5ba008aee614 | -3.29089 | -42.28861 | 2026-10-08 16:39:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| ab592657-fcd0-3c22-96c9-f93b51c3eabe | -6.14039 | -51.7632 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| ecf09f82-1b92-340a-9a97-2bc4c9f30581 | -3.77473 | -59.25352 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 879dee55-193f-3132-99f6-026c8ad20c87 | -1.6301 | -55.12646 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6dcd72d5-b85f-30f6-9026-788d03ed9de5 | -1.94838 | -45.24418 | 2026-10-08 16:39:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a13a480e-55b6-33d1-9bc0-29cc423527c2 | -2.61397 | -56.47735 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1f8c44a7-7130-3bba-8fd9-86e1175f9a0e | -3.59231 | -54.69095 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 31a4ca2a-6b33-3d81-9946-ff7b4ee31d63 | -2.03407 | -55.62857 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 36df6031-b02c-3d94-a050-791ab05734e2 | -3.94627 | -44.39277 | 2026-10-08 16:39:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e84d28e0-009b-3829-863e-8ea737bcfc26 | -2.22716 | -58.10857 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| af917e86-7e32-327f-bef1-10f9340f570b | -4.24957 | -50.74477 | 2026-10-08 16:39:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e5bcb42d-8863-3460-8263-7073412beceb | -3.9426 | -55.32774 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b35e8b59-a8ff-3013-8662-341ac17809e7 | -6.14497 | -51.7344 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f34d6c1a-2d7d-3817-a02f-788246320d29 | -3.17025 | -50.5913 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 7b643f6c-0fc9-3bfe-8d30-b923468eb892 | -3.10777 | -57.66527 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 694bce71-77b6-30d6-94bf-5e4617e796d0 | -5.96133 | -46.15737 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 44dcf6b9-76d8-35d6-82f2-6058179bf75f | -3.23345 | -57.87842 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cc48c2fe-effc-3e84-a9bf-f3ef23c0eb49 | -1.20432 | -55.6866 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2dd4797a-ab24-305a-87d7-2f83315a44ad | -6.07285 | -53.60056 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 17783ef7-aafe-3303-864d-a2c737df147a | -5.45418 | -45.59383 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 26c113fd-ea48-393f-a693-755ec05e8649 | 0.52727 | -50.802 | 2026-10-08 16:39:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d04033f1-b86d-3708-9611-8111ff27c144 | -1.18608 | -55.67075 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c98ef2ae-75ad-3e73-a432-6b8be147c104 | -5.30128 | -45.72543 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e82df4a9-992f-3298-91e0-6f33a981d138 | -3.25436 | -50.40135 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 262a714c-04bd-3a5f-960c-656eb97438e9 | -3.03592 | -54.23197 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 83525456-7e91-34a1-ab9e-1c51df12a8f1 | -2.45196 | -56.78294 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e558a5e-c5a7-36a6-8a4f-b9add53ca710 | -1.20947 | -55.68591 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 94efd58a-c8d4-3133-9cae-2dad54a712f1 | -5.67873 | -46.35126 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| eb88d58e-2e0b-30e7-a397-ad2677da2221 | -4.37022 | -40.41111 | 2026-10-08 16:39:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 1eaa9810-e526-35c8-a46b-b78253fad9b9 | -4.74782 | -55.64989 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2adc81af-0766-3a36-aedc-82ddea9ba20d | -4.15245 | -43.19368 | 2026-10-08 16:39:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c34c1fd-4981-3595-a693-9dcd10cdae3b | -3.09455 | -53.9575 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 729fd708-2c8a-3b13-af8f-710c14b74669 | -2.57734 | -57.13556 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a1ff2d2-86fe-3723-9307-c851b45740b1 | -5.38166 | -44.20359 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| eff9c7bd-d951-347c-ae39-3ec0f1750065 | -6.39553 | -52.7218 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d6ea7251-e1d3-3d87-87f2-3d2f17bdea84 | -5.94895 | -45.69973 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8d6d94ca-3614-3a67-8c58-bf607cd65cb1 | -6.11536 | -51.73799 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 09bfdfb2-35b4-31dc-9b5a-045ce0353742 | -7.31814 | -55.00231 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 01593cfc-d035-33e1-981a-d6b100e3743e | -3.05458 | -54.02647 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6c9a7b2e-2207-3462-bb7c-e430852da333 | -2.93608 | -54.14951 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 28ad262d-af56-3ae0-9d9b-f9b2909f3f2a | -4.34712 | -43.79217 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a6f099f0-3856-3b3e-b172-92e44fc5ca82 | -3.09311 | -53.94748 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| e0168dbe-12ae-30ee-a30c-88f726b7d13f | -6.75582 | -55.07835 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 75fd0fae-9936-34f1-a279-0c77d8877418 | -2.0396 | -46.32391 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5915fcee-a6c0-3427-a35e-ca9953f0fbe7 | -2.99303 | -59.04166 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 4002eb03-0998-3277-8ab3-0d4273f631de | -5.92903 | -44.27626 | 2026-10-08 16:39:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae373cb5-b85d-3d04-b452-ff1958460c0e | -3.40666 | -57.99427 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0b11558c-ea56-3df3-a478-d2bb5b0540b0 | -3.25533 | -43.58664 | 2026-10-08 16:39:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bc28b5ee-ef2d-3113-a38d-d1f107fcd403 | -3.81702 | -44.59608 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 00b17442-3637-3ae8-9770-bde6b46cc7ae | -2.71584 | -57.47057 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 6a1326a4-abed-3df9-8f82-e156705ff573 | -3.10394 | -53.956 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 63eba9b4-80e1-3424-9e0b-69e0f7a0c76d | -1.42556 | -55.71508 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3d8f207c-6cf6-3bdb-b7db-8fd604688f90 | -2.5663 | -56.1633 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4ba2f130-10fa-3d6d-b009-f9061e41930f | -2.2647 | -56.59222 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 320093ad-1eb4-32ee-9dca-c7777d090d12 | -4.75471 | -55.65976 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5e9d093e-dd6e-3a24-b248-26aef7071362 | -3.00729 | -54.10024 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 278b8bc8-d522-3e2d-a6aa-506d7976c9fd | -5.71041 | -53.44956 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1ce8e611-015a-3a71-a180-67b4277d987c | -6.30703 | -53.56395 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9ea0e76e-a447-3e3f-ae9d-6412e48deb40 | -1.41061 | -52.72548 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 1524f3e2-ae77-316a-8e61-073e01a6b0af | -3.57589 | -54.68305 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 4f5fa70d-f95f-3871-9e3b-415fa2245bff | -4.44433 | -41.47782 | 2026-10-08 16:39:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 18cf579b-439c-33ea-b1a1-9174ca6e8493 | -5.26794 | -47.9256 | 2026-10-08 16:39:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b77093b-0a2f-3d3d-bcb6-9f0b3ef2021a | -1.89628 | -53.98235 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 41491188-0d0a-3ee7-bfa9-adccd29da603 | -6.10214 | -53.49532 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 765064e8-788e-3c5c-b6a9-5d1cff348ad5 | -4.73615 | -55.65854 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| ad5cbbe5-9726-36a9-b415-3e2228bae77c | -4.95233 | -42.73476 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e5e18581-1e92-36bf-b106-c84e3c90c435 | -5.06648 | -46.18711 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 28.9 |
| c9a70c8f-0691-3aa0-8b77-5a2a7e41e3a9 | -5.68068 | -53.48679 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ea9dd7de-7b53-39dd-9e81-bfd9d0a78a4b | -2.75269 | -56.60939 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a2b609b6-3222-3f42-91ed-afba8763ae8e | -2.71521 | -57.46627 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 10d651e3-b758-3a2f-8de1-fd4d393044d2 | -5.81721 | -53.83187 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 78e53f79-5a88-3398-91d2-e9d2c578493d | -1.42662 | -51.61842 | 2026-10-08 16:39:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a07e662f-0c11-367e-b9ff-710ece108379 | -1.25897 | -55.75418 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 3ebcfc19-3a3e-3ff1-8d88-52cb1eaf3efe | -6.11902 | -51.73354 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ae78f8a7-7465-3128-b52a-d187190136e0 | -4.08898 | -44.1342 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| f81afd88-f990-31bf-8474-7a932a8ece81 | -2.10434 | -56.61674 | 2026-10-08 16:39:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ef012aea-7b57-3a14-8c50-a9c7161ca42d | -3.30725 | -54.69698 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e78b8ffd-2e92-35d2-bafc-3f97b6e7bed6 | -5.94842 | -45.69627 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 591b3178-7b6b-3b72-9999-b1a8f5532499 | -1.64234 | -55.27431 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 477d9c5b-653e-35c0-afb8-54137e521cd0 | -5.87735 | -53.49414 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 804b0958-3a4d-3dd7-8293-6eb9dfc14bb2 | -3.44938 | -45.09523 | 2026-10-08 16:39:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cb039b61-b88a-326b-8760-794000214a88 | -3.10702 | -53.92705 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bcbfb0de-9e66-3cde-b669-9ab4ee9443df | -3.74279 | -58.49334 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f5ef1abb-f4fd-34be-85b2-57bc05f48c69 | -7.33538 | -55.08731 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0aec8b13-b8f8-3423-b545-850fad910f90 | -4.09698 | -45.90591 | 2026-10-08 16:39:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 93fad809-019a-3a86-b4e3-d3f9fa8ff4b7 | -6.10356 | -53.50541 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f68a6407-e524-32df-8555-523d4a8bb1d2 | -6.1809 | -53.43012 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 78cffc92-562e-3c24-a83f-f195f5a57441 | -5.54283 | -43.22516 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 299d2b4a-094a-3daf-8176-b80cf1506862 | -7.19616 | -55.13229 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 2c8ec91c-4cef-3ce2-86ee-7de70cd7784b | -2.03064 | -57.05682 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d8f7f4f1-e8ca-3ddf-bc44-d7b2ecc3f67c | -6.47239 | -55.0064 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| af6a4689-6b73-3e27-95b9-2a29679a61e3 | -2.7205 | -57.46111 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 63f9cf46-329b-3b39-b972-ffe9867c74e8 | -2.21288 | -56.92359 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 69d042e1-e360-3102-8c9e-7ecce4f44686 | -2.48583 | -56.1437 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5b73c1d4-8709-35cf-814b-6ec32534a9f1 | -5.48114 | -44.59797 | 2026-10-08 16:39:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0bb0799c-9b0a-3661-b357-32ebeb658706 | -3.79112 | -59.31836 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d5325de8-0c53-391f-a805-530adda5dd4d | -4.57555 | -55.99052 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 265a4185-c41e-37f3-a3e4-a6a557205e12 | -5.28018 | -55.95922 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 25cf9c8d-75ea-398a-951a-e4dfa7d03918 | -3.23276 | -57.87371 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9a53ce60-9c1a-3e7c-8117-40ef8dd9ceae | -6.34257 | -52.5717 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README345.md)
