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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7a8437a-0ed8-3d17-89d1-3d650e4fb57a | -5.87991 | -46.09765 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a26233db-e071-3b95-a481-e1ac267da749 | -4.67134 | -41.01295 | 2025-09-08 04:00:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 27660478-a136-3821-b452-ca5e1266c18c | -6.3918 | -43.21826 | 2025-09-08 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 830bd482-cc2f-3823-a8b3-7ec16b731b58 | -6.48047 | -41.77594 | 2025-09-08 04:00:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 05dedab2-cf6f-384f-a5f1-f48d7fb849f1 | -6.61347 | -44.00976 | 2025-09-08 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fbbf6752-48ea-3f5f-b6f5-6ea390e84fc5 | -6.15 | -43.18297 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e2519c13-6c6f-3e95-98ed-37d9e36cf23a | -7.00242 | -44.93297 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4937237d-a351-3cf5-8d84-45c56fff1bb0 | -6.14222 | -44.23193 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ad6be89-9247-3fe5-ab68-71de6f75de5e | -8.61893 | -40.20129 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 3728d642-3a42-39e2-bb9c-0f9dd89e4d56 | -6.13295 | -44.24007 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d2219c9a-d993-34c9-983a-2493b35cc768 | -6.07103 | -43.32313 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 457baca0-9b19-3e05-a0f0-bc1c1e131218 | -5.82656 | -44.12265 | 2025-09-08 04:00:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c72bd5f6-7fea-31ca-9400-0377e517bb8e | -6.10121 | -44.1463 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2410d956-6923-3f60-b1ca-625091a3206e | -6.38686 | -42.61066 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 48cd845b-e2c4-3339-9abe-f55528727d97 | -7.17382 | -46.18338 | 2025-09-08 04:00:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4034f09-c319-318f-9d66-9ab950a01c55 | -6.25887 | -43.50231 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e34f7ab0-1284-35f8-8667-48fa0fff1f6e | -5.21479 | -43.29067 | 2025-09-08 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 530ce063-dd40-31fd-a523-a71e504a55ba | -5.94397 | -45.75239 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 557b0c13-4c4a-3f9a-92e8-6b2385c4b873 | -6.66827 | -43.84128 | 2025-09-08 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f3706b3-dd00-3797-a686-1b9317cb7777 | -6.1762 | -44.77868 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f43f29d-4f7e-321e-b572-e899c6031d8e | -3.79131 | -48.87469 | 2025-09-08 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3db4acd-a839-3be9-b863-1c2b8782a594 | -5.42454 | -42.85087 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3af00f78-8a4c-3b46-b1d7-ece40d76e1be | -5.44398 | -42.79876 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6278742f-c2c4-308d-b4e8-0cf84455c934 | -6.35863 | -42.5822 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5704c9a3-33b1-32ae-9edf-7605abc69729 | -6.40684 | -43.87551 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c3a2e51-c7f6-39f3-a93b-c4a29a456ae7 | -6.88235 | -44.25802 | 2025-09-08 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 612e9684-1b6b-3a46-a458-89c6c2654709 | -6.63979 | -42.96662 | 2025-09-08 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81a37cb0-1bc1-382d-a14d-33db34dc7dcc | -6.80753 | -52.81461 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25af5ad8-086d-3adc-aa4b-5dd89a666d40 | -5.35254 | -42.64653 | 2025-09-08 04:00:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3198f256-7ab0-33cc-9b70-fa5993a35383 | -5.87078 | -43.45049 | 2025-09-08 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5dc91bef-e9c1-3ca2-aa02-b6749294952e | -6.46148 | -43.94345 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b4c4f41-98b1-3b0a-b914-37935418d93d | -5.41597 | -42.8581 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f5f2c420-1db4-3e36-927a-02a74d4ca906 | -3.85781 | -39.33606 | 2025-09-08 04:00:00 | NOAA-20 | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4b003936-6d03-38e4-85c3-33fa9cb3259d | -6.26228 | -42.57442 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 40f2d061-accb-3a53-ba2a-1d499ede0eac | -7.3277 | -43.93408 | 2025-09-08 04:00:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a65ff66a-abf8-3dee-a0af-ea05374a9ad7 | -6.43299 | -43.64874 | 2025-09-08 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c4db3e6-a9fd-361e-bbd1-1039ad07d92d | -7.31775 | -44.37043 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddaa56e5-869f-3622-9d4c-94f68983df1e | -5.42892 | -42.68687 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9177a3b0-2bb2-3602-8a8b-c48ad5bcd2ba | -6.00179 | -44.2557 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9699985a-7fa5-3a91-9b96-0955952e8195 | -6.19655 | -45.03442 | 2025-09-08 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83dfa56f-b7b6-346b-ab3e-aea3aee12431 | -7.39264 | -43.98943 | 2025-09-08 04:00:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b04d020b-e5d9-3100-b6bd-00307c94c0d0 | -6.24772 | -43.70955 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 49581cd4-4287-3804-addf-80c9db4e118d | -6.26638 | -43.6891 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c23839f1-cafe-38bd-9fe0-e0460bc0ab3f | -5.71599 | -43.89907 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2860ab5d-8351-3f2b-933b-4a1440be515b | -6.25221 | -43.70555 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a080e9f-fb13-30df-a097-a9ddb4aaed35 | -6.40306 | -43.87502 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c09a2b55-9f52-3e47-89cf-06bc26025c7d | -5.44758 | -42.79932 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4924ecc2-5016-3334-ba74-11c8cc3b918d | -6.61499 | -44.00058 | 2025-09-08 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2cc90a03-8cc0-3bac-a984-9c1125df1989 | -6.30833 | -42.19585 | 2025-09-08 04:00:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2978fd4e-c4fc-3749-97d4-462ad4d6f20e | -6.20468 | -45.03561 | 2025-09-08 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab18ff84-5d43-3030-b84b-30dd74fcdacc | -5.91338 | -49.67164 | 2025-09-08 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e0140b9d-b46a-3039-ab68-540222a52d0e | -6.39125 | -43.80706 | 2025-09-08 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59ad5556-7da6-3800-a33b-0092a4eb30d3 | -6.40264 | -44.45621 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9bce0424-ba05-3b63-bb01-4ca67314171d | -6.84009 | -44.87405 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c18e8d5-65e9-3b4b-8033-e0ac8e7b0ace | -6.31599 | -42.20414 | 2025-09-08 04:00:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3daaf6ac-1491-3ee0-b897-48cfdad13848 | -7.24699 | -44.84204 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3d808596-d4e2-3f49-b1b6-1b347dd60d1f | -6.48105 | -41.77227 | 2025-09-08 04:00:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 03316632-6a53-369c-9645-a0b5cf6c5e07 | -5.08178 | -42.41547 | 2025-09-08 04:00:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7e2fd53f-33c5-3657-b588-156dd987dd17 | -6.05991 | -43.29931 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 701210f0-572d-39d3-a60a-5cf9e8b86ce2 | -6.79034 | -44.78169 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f9f39e01-5d27-330d-8618-5d351d81951b | -6.63912 | -42.97067 | 2025-09-08 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a745a143-fc8c-3286-a809-7f10d4830dca | -6.04751 | -44.41402 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8577623-a8cc-3ad9-a8e2-fe4dc458e5c7 | -5.86362 | -43.23972 | 2025-09-08 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d103b431-4a4f-3168-b15d-030912c0ed27 | -5.06691 | -48.42085 | 2025-09-08 04:00:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d7a3e1b-8254-35f7-a15f-cc2dee08118d | -6.46723 | -43.95582 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e012a5d5-9426-3e24-bdbb-e3d51e8f6b9f | -6.30591 | -43.82844 | 2025-09-08 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81d4ac7b-85ed-3d27-995e-3aefbb371042 | -5.75983 | -43.14111 | 2025-09-08 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fdc572f1-7cd0-308c-b7e9-5b83b32b71d7 | -4.89972 | -42.22038 | 2025-09-08 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5677812e-fb41-32ba-a6b0-5cd07ab21bdc | -7.24475 | -44.83124 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2a970560-fdba-31fa-96a8-4426df9ff196 | -6.08854 | -43.71283 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d1100ff-f50b-3186-bb5c-d6f72d62225f | -7.99189 | -46.34264 | 2025-09-08 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8e1df2e-84c2-33d0-b2ed-e9a0e2a97e62 | -7.57006 | -44.66779 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 35d2431d-077b-395c-88b9-b2c2a5acd4c3 | -7.85387 | -44.79799 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| afcedc8f-07cb-3557-be59-b82afcc10015 | -6.23833 | -42.76386 | 2025-09-08 04:00:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dc57f67f-8364-3959-9271-84fe432a8e4f | -6.63319 | -53.36705 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fb4cd949-8b2a-3dc1-88ca-bbd2b1419d4a | -6.63373 | -53.36516 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1f5e7138-1a74-32c1-acda-9a44bccee2d8 | -6.84214 | -44.8767 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f7d3d9f-30d2-3be9-9d2a-239d71441162 | -5.87768 | -43.95562 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e534e6cd-62a5-36ad-bc50-cee1e1e8e204 | -4.89555 | -42.22374 | 2025-09-08 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 69e44b3d-6616-37e9-b29e-7bd00ba7d353 | -7.31597 | -39.15448 | 2025-09-08 04:00:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4954db86-19c2-3ae5-a228-53e4f8c8445e | -6.62803 | -53.35746 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be208cf6-3abd-312c-ae10-413100579a2a | -5.45053 | -44.13854 | 2025-09-08 04:00:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8875ede3-ca00-3baf-bfcd-624f321ddaeb | -6.40446 | -42.98547 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fb45501-c127-3f0b-92da-50b829fb6353 | -7.81964 | -45.43438 | 2025-09-08 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba65512c-4366-3c0d-9e86-88dd364c2201 | -8.4557 | -44.71162 | 2025-09-08 04:00:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acc9d7df-51fa-35b2-b341-7ad994e88b6a | -7.01659 | -44.94606 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 269931d1-7fcf-3996-b376-a42972cf1913 | -5.95203 | -43.22567 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a77c3737-6e01-37a6-b99d-061eb66b33ea | -3.24684 | -50.81544 | 2025-09-08 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce5d50fd-a33f-3995-804a-a931dace8bd2 | -7.36604 | -44.31557 | 2025-09-08 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8989447-4258-36bd-a14a-43923db2ff93 | -7.542 | -42.52344 | 2025-09-08 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b8885b07-46ae-39a3-83c6-0fe1786a73cd | -7.2248 | -46.20784 | 2025-09-08 04:00:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9ef2e794-dc3c-32d7-a1c6-9e9a5bed94ed | -7.73556 | -44.73278 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ddd02510-0573-34d8-bcc6-136de62f2216 | -6.95458 | -45.51964 | 2025-09-08 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbc43d85-008f-3312-82f4-d7819a701a4f | -6.7811 | -43.42507 | 2025-09-08 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 68ab498d-4e10-349a-a497-cd14ec481e6f | -7.38668 | -44.00225 | 2025-09-08 04:00:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f888c2bb-2478-3ca9-8fb4-12e3df041a3f | -4.90036 | -42.21644 | 2025-09-08 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 48ad8899-78d5-34fb-8362-85e8a608dce2 | -5.77881 | -45.62855 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cd32eff-5e68-3303-add7-37f05093371f | -5.73989 | -45.37026 | 2025-09-08 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eccb198d-834f-3d05-99b4-bcf3f12c8646 | -6.40455 | -44.42112 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf9b6a0d-2dd6-3a89-b661-fe1c0d40b93f | -6.20818 | -44.53664 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README33.md)
