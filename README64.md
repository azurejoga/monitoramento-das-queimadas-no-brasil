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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c8fc124-20f5-3ce5-9f4e-bdd329f4aafb | -6.53166 | -51.19777 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20d5621a-d1be-3788-85f7-da11e9a3a920 | -3.6474 | -54.05891 | 2025-09-16 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 882050ce-93ec-3e3b-aec3-834939425ba4 | -7.56276 | -43.95696 | 2025-09-16 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe7a4bdc-edd3-36cf-b6da-dad86faef593 | -7.26479 | -46.60981 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 937d412e-3e6f-35de-a026-9ebb6fecbb9e | -6.5215 | -51.19649 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1f175b5-77a8-38c5-b4c5-a2849845ae63 | -5.53178 | -42.65982 | 2025-09-16 04:49:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 6d7c662a-fa2e-39f9-bf24-792799ba08a1 | -6.96711 | -44.56959 | 2025-09-16 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 112a28bb-3e28-3474-87b5-801e3b3d02bf | -7.42161 | -44.8631 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 19018c9e-b739-34a4-b1d7-e07926500a28 | -6.69153 | -45.50451 | 2025-09-16 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 390b1d4d-2391-36b6-a94c-b3132c7c16b3 | -6.17683 | -41.22065 | 2025-09-16 04:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b37fd66c-ecd2-3f06-8141-f4c1b27382d5 | -5.77875 | -45.89328 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6663e2e-1d3c-3724-9409-3efeeefd9da7 | -3.81053 | -41.57223 | 2025-09-16 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a921a149-6401-3037-b79a-52411688baf7 | -8.00805 | -45.67112 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f52a9af2-ee47-3a3b-9271-72d1a6eeaa7d | -2.65365 | -49.75838 | 2025-09-16 04:49:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2f53c38-4888-3e08-b8bb-5ad5b6d59dca | -7.13944 | -47.98779 | 2025-09-16 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 40f266ad-d6c0-3850-b2a7-df951bc4f3e5 | -6.40278 | -42.65807 | 2025-09-16 04:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6c350912-9b61-351c-9314-2250d964d1b6 | -7.44444 | -46.16451 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0f30134-aaf1-309c-95c2-e3747d8eb9bf | -3.83825 | -44.09838 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d1dd6fd2-17f5-3161-b526-8f9fdb5d5500 | -6.18727 | -41.19596 | 2025-09-16 04:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0bbcb2e2-9e65-3b2d-ae16-35129c554027 | -5.64494 | -45.94787 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb0c27a9-13ca-35af-b54e-1863484a63db | -5.79521 | -45.93653 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0ef2299-5e03-332e-a740-11500b2699fc | -5.79111 | -43.93998 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19ea6902-f6fa-32c3-acc3-06e90c3a413d | -3.85745 | -52.39748 | 2025-09-16 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eae30ed9-4e38-3f0c-a194-451662f677d1 | -8.00146 | -45.66851 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c65a0182-2cf0-3c9f-a22b-6b06dc45ba51 | -4.48706 | -48.11114 | 2025-09-16 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20cb8f62-80cd-3aa4-a669-1899dfbcfc2d | -5.88965 | -45.74562 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ab1e8f5-d743-38aa-bda5-05c6ca810d14 | -5.8055 | -44.86779 | 2025-09-16 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ccee7229-91a7-3f9f-8918-b4a119a0c569 | -5.7939 | -43.93808 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e70f1bff-f937-3f73-b0d6-732ac35ee8f0 | -7.51762 | -44.35801 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8337d5f-1592-31ed-b8de-7d33d68b702e | -5.98213 | -45.85015 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d86589e-cc7e-3cb2-b07c-e75f3ff29190 | -6.26193 | -43.46585 | 2025-09-16 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f19b097d-7035-3b37-88d6-5eb152095007 | -7.67391 | -46.29029 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bb6fda8-c45d-38d9-8f46-c03c4188a774 | -6.40962 | -43.33366 | 2025-09-16 04:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b687c44-5600-3162-adb0-a7dedbcf8207 | -6.1771 | -41.22343 | 2025-09-16 04:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a7adf871-c3ed-34da-8f5a-0dfd31c9526d | -3.73554 | -49.04406 | 2025-09-16 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f5129460-4816-3766-9ed6-3c31e86d6b99 | -5.56116 | -44.97039 | 2025-09-16 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 914b7076-c659-33f1-97a9-d53c03b89b23 | -6.17422 | -46.81671 | 2025-09-16 04:49:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe0ce976-9f7b-322c-8d3b-d13d9fb57308 | -6.37114 | -44.41273 | 2025-09-16 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3242142c-f6f9-35c4-a690-7a0f50c293ef | -6.6794 | -46.30811 | 2025-09-16 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5e6f0c37-a927-3b0b-aaa0-b54aa985bba4 | -7.21282 | -44.3872 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c065812c-372b-3c6e-a529-735aae71f107 | -5.7775 | -43.92575 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 04b3a48e-8ed0-3ebc-b455-1703309e1297 | -8.18188 | -47.13424 | 2025-09-16 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1bff7fc-2196-315b-9ea9-4bec786b7d97 | -6.4469 | -44.09069 | 2025-09-16 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2adfb499-23d1-3d58-8f9e-e8709c218cc1 | -3.89317 | -42.51353 | 2025-09-16 04:49:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4b50f861-3e28-3397-9522-3b497899f1b7 | -6.54491 | -44.00634 | 2025-09-16 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59a11c19-c4df-33d0-b1d8-17dc7cebaaf2 | -6.21725 | -43.89886 | 2025-09-16 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6fb7430e-d4a4-3ca2-a119-d2072cb2d151 | -7.31739 | -43.95188 | 2025-09-16 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3109ffc3-d2f9-3b73-a587-3434af20cb0d | -6.52885 | -51.19367 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f865a9f-1c18-3855-aa5a-c2079728e6de | -6.4432 | -46.1133 | 2025-09-16 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f560d7f7-84e2-36f0-afa8-aff1f0cdd9df | -6.44384 | -46.10906 | 2025-09-16 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e379ef27-8067-3d17-a254-fccc6974650f | -5.78711 | -43.94937 | 2025-09-16 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da932b0a-53c9-33d6-9271-76e8322ba3af | -5.90582 | -45.72982 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e283625-f365-36d3-8d11-74b78e1ddd54 | -4.60006 | -43.32388 | 2025-09-16 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a347990-a03c-319d-aebf-e5082b59805f | -3.96791 | -47.57295 | 2025-09-16 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad63718d-1ea8-3f24-bedf-9ec8737c4d6c | -6.96633 | -44.53935 | 2025-09-16 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c66f291-3ccc-3ad0-8c6e-df926adadca4 | -6.25521 | -52.87286 | 2025-09-16 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 56ecce0d-49f8-3845-aaba-ad1e62a2032e | -6.97592 | -44.54363 | 2025-09-16 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f40703d-225c-3be4-b2ec-c5709726c04e | -7.09236 | -39.67363 | 2025-09-16 04:49:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f88edfec-f4ff-3c25-902f-51b789654e9b | -3.88813 | -52.07408 | 2025-09-16 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 074813b2-033a-3628-ab8f-a678a5f7305a | -7.27413 | -46.60667 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69dc9f56-563c-3556-8e89-abf2b2162a94 | -5.8317 | -45.26687 | 2025-09-16 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58a09687-b213-3926-9300-948ec5cbe89b | -7.85434 | -46.10653 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3dcbc51e-fc17-3852-aa5a-6bd8ed0be155 | -7.5632 | -43.95377 | 2025-09-16 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcfa8497-f21e-30b2-a792-dbc2b027a919 | -6.31788 | -47.73878 | 2025-09-16 04:49:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab209da1-6314-3ca8-b3dd-70f97563cd06 | -7.50443 | -49.47358 | 2025-09-16 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 418721c6-a84f-3c0a-b76b-25dfd9a68bd8 | -5.98279 | -45.84558 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c52df6d-7476-3bbf-8a89-e99c392827ac | -6.52943 | -41.8289 | 2025-09-16 04:49:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 31536297-f119-3738-bec1-50cdd455b3f4 | -7.26537 | -46.60575 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e0d06ebb-691f-3ab4-bc15-c40545e4b3fe | -1.64335 | -48.5175 | 2025-09-16 04:49:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9600a474-b2f4-39a9-b9fe-7f43fb24b811 | -7.04783 | -44.11352 | 2025-09-16 04:49:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f9bb449-4736-398e-b5ff-6ccde5c51fe3 | -7.26715 | -46.59322 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d8c0196f-8d8e-35b2-b473-ca392b0b3b94 | -6.56258 | -50.88695 | 2025-09-16 04:49:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 417a4d36-4c1d-3ce9-b38c-daf3cfd83fdb | -3.83489 | -44.09922 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e948d568-9c34-38f1-b260-b29b6225bd54 | -8.41593 | -45.74421 | 2025-09-16 04:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fb9fcb2-a02a-33a1-bdfe-a6a236f44677 | -2.9588 | -52.04444 | 2025-09-16 04:49:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c60de3fb-9db3-37fe-bbc5-cc719c8bc986 | -4.81242 | -47.34122 | 2025-09-16 04:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c039ef65-3d1e-387e-95a7-26fea6c28a33 | -5.05176 | -45.20038 | 2025-09-16 04:49:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d61f7b2-2a40-33e1-a031-f7839879b3a5 | -7.6741 | -44.47562 | 2025-09-16 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74b7072e-68a4-31c8-acb5-74821cbb398c | -7.14417 | -47.98326 | 2025-09-16 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| d5983d8e-2187-3049-b774-b4251dd5bfe5 | -3.81636 | -41.57307 | 2025-09-16 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9ea01293-022a-3c3c-8173-ef32ba4c84b2 | -6.53004 | -41.82462 | 2025-09-16 04:49:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4b679d10-5337-35cc-9482-33f26800a312 | -7.44895 | -46.16511 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c571c51-2c32-31c7-8606-7a9a7887d9c9 | -3.137 | -44.42859 | 2025-09-16 04:49:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27680da8-a3ce-3c25-8f2a-917ec40d7796 | -7.27473 | -46.60246 | 2025-09-16 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f653c05-ef6a-3d6a-827f-a991d9a37a44 | -6.6838 | -46.30877 | 2025-09-16 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2423258d-f60d-3021-bbe7-afd3da55e92a | -7.08788 | -44.54589 | 2025-09-16 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49916bd9-aa9d-372b-8e67-4b1aabc02fc3 | -6.62053 | -44.73915 | 2025-09-16 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0595a6df-f012-328c-9c0c-f2d91b5a0287 | -6.83108 | -47.85292 | 2025-09-16 04:49:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 04e739bc-2a7f-371e-b1f3-e9af265b7493 | -3.81293 | -41.55569 | 2025-09-16 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| d6dc79f5-d42f-3967-8338-5128eef8b0a1 | -7.43968 | -45.83604 | 2025-09-16 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 098fedc7-8420-30ff-8276-3ec3ced93236 | -5.79141 | -45.93141 | 2025-09-16 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2659d739-c58a-34fe-9b3c-87d8380d7d12 | -6.22241 | -43.89969 | 2025-09-16 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d6ceea8-0897-32b5-b760-8b25c559833f | -8.12351 | -48.26056 | 2025-09-16 04:49:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45205353-ddce-390d-b77a-e9d3234a2e75 | -6.54451 | -44.0092 | 2025-09-16 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae8aa349-1889-31f9-9735-f6abc1373030 | -7.70846 | -49.55806 | 2025-09-16 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 91437ff3-cb51-396b-8403-c40e71a4cd27 | -3.82348 | -44.10869 | 2025-09-16 04:49:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e4502d0-ccea-3972-b0da-f8bbf39dcddc | -7.13623 | -47.98211 | 2025-09-16 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5fcb8af5-8813-31d1-b783-e57bd1df7ddf | -5.34274 | -44.82308 | 2025-09-16 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8521ff3-bd56-3cc5-95cd-4f4fce509b98 | -7.73139 | -45.30294 | 2025-09-16 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 73af154a-a3be-3ce5-8c1e-1bde7d8a52c8 | -2.88943 | -49.48545 | 2025-09-16 04:49:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README65.md)
