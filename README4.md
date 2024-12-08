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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5c5a3f9-ed0f-3ed8-84b7-abbc4ec18dc2 | -7.98779 | -45.7921 | 2024-12-08 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e69bda20-8c7e-324c-bcc5-847e738d4ae9 | -6.5045 | -42.91507 | 2024-12-08 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 962d8336-9a15-32ab-afdf-c40ef2956d3c | -7.88445 | -44.20024 | 2024-12-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58b941b1-7e3e-3194-8ffc-bf0d9589808e | -7.47704 | -34.84164 | 2024-12-08 03:49:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0172411e-6d32-34d2-bd86-467f49565c31 | -6.05274 | -44.05021 | 2024-12-08 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dcf14e01-0306-379d-9685-74d2258083ab | -5.57953 | -45.2156 | 2024-12-08 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e38a09f9-d482-3dd5-8474-969d4f256128 | -7.80771 | -46.22907 | 2024-12-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| faeb2807-a220-381f-bcf0-79fdedb6219d | -4.56428 | -38.48054 | 2024-12-08 03:49:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| af97b176-6eef-38bb-bc57-7db36ee8c4cc | -10.00264 | -36.33417 | 2024-12-08 03:49:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f591867c-f223-3002-93e6-700e970c4c2d | -5.24838 | -37.5029 | 2024-12-08 03:49:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cf9fad2d-dae5-3a27-8ad0-bf3ac7f5e62f | -6.99024 | -47.08766 | 2024-12-08 03:49:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7c886148-d131-3507-84e6-ff6a1c9d2464 | -7.7967 | -46.20034 | 2024-12-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 638eff88-a91e-30ee-adcf-95f21d53414c | -5.51147 | -42.8778 | 2024-12-08 03:49:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 91ea0f2f-884f-337f-bc5f-b444a0a6becd | -9.99785 | -42.17453 | 2024-12-08 03:49:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 44ee22e3-78f9-302a-b8a4-11119b92863d | -10.9301 | -38.81328 | 2024-12-08 03:49:00 | NOAA-21 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8f765517-2f3f-30a6-b439-0792a548e8f0 | -9.98955 | -36.51014 | 2024-12-08 03:49:00 | NOAA-21 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 9d14c2f3-ed7e-3b1c-a73d-d3511b66406d | -8.07298 | -34.97511 | 2024-12-08 03:49:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7a9bc97e-c403-3512-829a-791ab0ce43ec | -5.47619 | -39.41314 | 2024-12-08 03:49:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 87fb3402-b3cd-3a0f-b051-d29f0bd52960 | -10.00545 | -36.33839 | 2024-12-08 03:49:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bc01c465-8b32-3af5-b550-2628763c5c74 | -5.15239 | -40.48961 | 2024-12-08 03:49:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 459a4a0d-77ac-361f-9fbf-aa32078b167c | -4.91215 | -39.01226 | 2024-12-08 03:49:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0fd97ecf-f24f-3ed1-afd3-ed968738cc28 | -6.68352 | -47.66338 | 2024-12-08 03:49:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1616527-4f81-329f-8d29-e182a289f6ef | -5.58106 | -45.20673 | 2024-12-08 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c7e8a73d-e93e-356b-8cc0-6238906814db | -5.9238 | -48.02673 | 2024-12-08 03:49:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a15bf44-bd79-3a64-a778-85d77314c26d | -6.87278 | -47.23907 | 2024-12-08 03:49:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 98faef10-3b40-3876-a499-86a931d72daf | -5.81515 | -42.49386 | 2024-12-08 03:49:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0d6299cc-43b3-3fa3-b94d-51c310c26748 | -5.58004 | -45.21264 | 2024-12-08 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bcb12f7f-0d6d-31d9-99c9-7cdd3487be14 | -5.2628 | -44.77602 | 2024-12-08 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5698d7f1-7ad1-36a3-8ecc-20279b4e3c9c | -10.00882 | -36.33891 | 2024-12-08 03:49:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 86c8a02a-9e19-34ae-901f-23ff88b1961b | -5.2517 | -37.50342 | 2024-12-08 03:49:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 9cbd8815-c4ea-330f-8d41-849033306cc0 | -6.87209 | -47.24291 | 2024-12-08 03:49:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3f9719fa-e5b0-3b71-aba6-bb7548d88f5e | -5.69905 | -39.40321 | 2024-12-08 03:49:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 610bd225-7a6b-3968-91ef-821e11e20c68 | -3.85745 | -40.44964 | 2024-12-08 03:49:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b414c5c5-c05b-3077-bc12-dcc6e9533d6f | -5.36364 | -40.86013 | 2024-12-08 03:49:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d9626219-43e7-3aeb-aec3-8775b94f54f3 | -6.05355 | -44.04537 | 2024-12-08 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9a056441-fcfb-3184-91af-35e6ce63c4db | -10.45724 | -36.39566 | 2024-12-08 03:49:00 | NOAA-21 | PIAÇABUÇU | ALAGOAS | Brasil | 2706802 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c2d6089a-2c36-3bbc-a543-2ac829b82fc5 | -5.42441 | -44.71135 | 2024-12-08 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 81f9f2da-0718-3bc5-8de1-e2b82e34aefa | -7.8791 | -44.20408 | 2024-12-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9491a267-a187-3512-b662-5bd15a9b1002 | -5.47971 | -39.4137 | 2024-12-08 03:49:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 228141aa-21d7-3afa-bbd7-7de3556e63c1 | -4.91562 | -39.01281 | 2024-12-08 03:49:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 579aae1b-0047-3d85-8451-8c902d220511 | -5.90391 | -48.03326 | 2024-12-08 03:49:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 144e380e-3657-3dce-9559-31216be143b6 | -7.80828 | -46.22584 | 2024-12-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5b3cc04-23d1-3e4d-b965-f8a416930479 | -6.05186 | -44.04772 | 2024-12-08 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d86a4b2b-2cd8-3fd3-844d-78cd1b915cf3 | -6.69007 | -47.66033 | 2024-12-08 03:49:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc5a4de6-4df6-30cb-98f6-e25583ac66bb | -5.23693 | -39.3681 | 2024-12-08 03:49:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 41141dba-e4a7-3e52-a371-90e1b522b7ac | -6.29346 | -43.84836 | 2024-12-08 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8e2e668-72e4-37ef-90f4-3fcfe1baee7c | -8.09911 | -35.10938 | 2024-12-08 03:49:00 | NOAA-21 | MORENO | PERNAMBUCO | Brasil | 2609402 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a20e4f02-45e7-301a-8499-7036dd4ae446 | -6.87141 | -47.24675 | 2024-12-08 03:49:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cf4e2907-2d15-34f1-9801-38338b68b16b | -10.00827 | -36.34255 | 2024-12-08 03:49:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5fce2a39-cce4-3edf-9e34-e5adc6725370 | -5.53375 | -42.87714 | 2024-12-08 03:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d9f39988-8577-3f6a-a086-97a0c136619e | -7.13537 | -44.95205 | 2024-12-08 03:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9158ba59-a604-3642-bb6f-7116229962a2 | -5.53807 | -42.87783 | 2024-12-08 03:49:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1a459737-0111-3b8e-b825-3cf492f66115 | -5.52723 | -46.96203 | 2024-12-08 03:49:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 54c29e49-d83b-3075-9eb6-81fa35f1d51f | -5.90962 | -48.0272 | 2024-12-08 03:49:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bee8692c-901b-3b9a-89e3-ffd2c4a976d8 | -6.2048 | -46.06544 | 2024-12-08 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 126c8f7e-1ca2-3104-9d03-a4a6df59159b | -6.98466 | -47.08659 | 2024-12-08 03:49:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72fe3fb9-a10b-36ef-be5f-8a31029ec572 | -5.92299 | -48.03122 | 2024-12-08 03:49:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ac69355-4522-363a-9431-366d000fdfc6 | -7.99233 | -45.79585 | 2024-12-08 03:49:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f855207-d5f1-3c61-af3c-2b0deb0912d6 | -5.91 | -48.03408 | 2024-12-08 03:49:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5b613fc8-ddd7-3ed5-995e-94e214342a8d | -5.42537 | -44.70575 | 2024-12-08 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7837f2ef-077f-34a5-953c-20c5ad38a3a2 | -6.05269 | -44.04297 | 2024-12-08 03:49:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60bee370-9cb4-3704-907d-65cbd26540c7 | -11.752 | -54.7255 | 2024-12-08 03:50:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| fc6ec714-debb-3bb7-8e8b-13ca9815f67a | -15.76519 | -45.08588 | 2024-12-08 03:51:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dd74dff-4968-3d62-b69a-eb2f94e8173b | -15.60765 | -39.32694 | 2024-12-08 03:51:00 | NOAA-21 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0b083211-5150-3c82-8d98-52c5830aa04b | -15.2587 | -53.57374 | 2024-12-08 03:51:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 77645e5f-192f-3aa2-8b30-7055adb59ea2 | -15.95308 | -43.404 | 2024-12-08 03:51:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d448b696-c04d-31c1-9f5b-0cbeefa34e3a | -12.8622 | -51.94076 | 2024-12-08 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2054b39a-c1dc-35f6-92cc-a9b8d2033c07 | -14.14475 | -44.67522 | 2024-12-08 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a98a7cb-dfb6-3eb9-b69e-62b2fa46dc25 | -13.52152 | -43.51549 | 2024-12-08 03:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aaffe4d1-8675-3026-839c-e5317efa1378 | -12.68969 | -46.76193 | 2024-12-08 03:51:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ced5b06d-46fa-307f-a5e3-877fcc0d6d34 | -12.85543 | -51.93928 | 2024-12-08 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58d9453d-3dca-3a81-8c80-70ce27cfd26c | -15.36837 | -53.1228 | 2024-12-08 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 97b264ef-e3bc-31f9-81d2-7a518e175981 | -12.86165 | -51.93663 | 2024-12-08 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 742eef9f-6fb9-39f0-92f5-5848b520343f | -15.56934 | -47.85678 | 2024-12-08 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a870ffa9-9809-3922-9a8a-eb53503873b3 | -18.04044 | -39.92503 | 2024-12-08 03:51:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 31595c9a-815c-3804-a71b-3fd87d5a1b86 | -17.67636 | -42.74144 | 2024-12-08 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0530a923-9c82-3bf7-bcf1-9d416943eb80 | -17.0063 | -39.7751 | 2024-12-08 03:51:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ff567034-4def-3f60-8dea-1399e0a0a850 | -12.85356 | -51.94141 | 2024-12-08 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a372ebec-c1b8-3aac-8842-f2168799552a | -12.53904 | -48.32676 | 2024-12-08 03:51:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44364c77-469a-3a75-b0fa-8e9910f15105 | -16.3504 | -43.69663 | 2024-12-08 03:51:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 952b4fa5-22e2-3a47-bb72-901c4427f109 | -15.76591 | -45.08187 | 2024-12-08 03:51:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f35c67d5-bf5b-34d3-8c31-25160fa793aa | -15.35135 | -39.87247 | 2024-12-08 03:51:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0305d9d9-9def-363c-8b2c-7ebb2bc5947a | -12.53974 | -48.32313 | 2024-12-08 03:51:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d324d55b-5dba-3629-b235-71f703eec43f | -15.76571 | -45.08491 | 2024-12-08 03:51:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0d8e3a5-b173-3f0a-b5a3-cb1e1a903e09 | -16.34926 | -43.6938 | 2024-12-08 03:51:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ec1cb3c-4e17-35d3-a1c7-bf9f8063a1d0 | -17.09449 | -43.80452 | 2024-12-08 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6788952-5f78-3db0-aff8-d2089ba10097 | -16.75637 | -41.05485 | 2024-12-08 03:51:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b262156c-b854-3fc5-b70f-ae22c3cf3259 | -16.2886 | -48.0176 | 2024-12-08 03:51:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3082215-4668-30b1-9a98-3866c1e2157f | -15.35192 | -39.86888 | 2024-12-08 03:51:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 45ea6243-669b-3421-9617-5e2d3f8389c4 | -12.85618 | -51.92899 | 2024-12-08 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4a8ad05f-389b-30ad-b06f-ebf8fab0dac9 | -16.288 | -48.02069 | 2024-12-08 03:51:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 829d42db-58a2-3b95-bbae-cec355b16835 | -15.09643 | -41.1026 | 2024-12-08 03:51:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2d90e876-dbd9-35ff-b3cc-f5355befb4e9 | -12.85677 | -51.93311 | 2024-12-08 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b07a712-1df3-38a0-b030-f6d637761f59 | -15.2603 | -53.56673 | 2024-12-08 03:51:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a498114c-d2b2-3f77-b611-47a15eb5fc5c | -12.69465 | -46.76286 | 2024-12-08 03:51:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f776b331-a5d3-3027-9396-c7f62fe0358d | -12.85489 | -51.93512 | 2024-12-08 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b222ebd9-c678-38d8-a125-53f52160594d | -12.53898 | -48.3264 | 2024-12-08 03:51:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6780ebcf-3ff1-3ef2-bfea-1b0abe829ac1 | -17.13256 | -42.41283 | 2024-12-08 03:51:00 | NOAA-21 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57584f3c-26e7-3d88-b931-3172970650d6 | -16.2874 | -48.01851 | 2024-12-08 03:51:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e2a391f-0803-3a70-b0b0-8a107be83abb | -12.86034 | -51.94289 | 2024-12-08 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README5.md)
