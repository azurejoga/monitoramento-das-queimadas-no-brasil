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
| 6f9b5f58-9392-3eed-927a-83afba6b9291 | -6.58274 | -43.08625 | 2025-08-19 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a996a2d-8864-3f6d-8434-1e07f55b0bd5 | -6.9338 | -43.59129 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4dd68a08-6dd2-3f17-b09e-39e07dace8f1 | -7.26176 | -39.67016 | 2025-08-19 03:36:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8c536bf9-72dc-3366-80f4-73b7ef3744b8 | -6.95107 | -43.59065 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb9008bf-9710-3fd5-9442-8fc5883ffab0 | -6.74224 | -41.53695 | 2025-08-19 03:36:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c231b08a-65f3-38da-898a-3c2fa8cdb3bc | -7.0122 | -44.27422 | 2025-08-19 03:36:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42a63c58-b3c7-3245-bfb4-a4f61d642419 | -7.57904 | -45.43839 | 2025-08-19 03:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcc9ba6a-d45d-34d7-9fdd-afc75f925e98 | -7.01194 | -44.27567 | 2025-08-19 03:36:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 557b0e77-23c2-3c0c-9c52-8d7fde687d51 | -5.97388 | -44.13294 | 2025-08-19 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8b2b887c-2797-3c4e-86c8-cee8721ef289 | -11.80618 | -44.26236 | 2025-08-19 03:36:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 88bd9ed6-caf8-357c-ac67-04cff7586f67 | -6.68128 | -43.67884 | 2025-08-19 03:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18043180-eb42-39cf-b989-db8e482bb88d | -6.06454 | -44.12738 | 2025-08-19 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bdcad5bb-ed73-3aa0-b194-18a748f02cdf | -6.15162 | -42.6961 | 2025-08-19 03:36:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0e87f86b-977e-3449-afa0-c050548e624f | -9.48757 | -40.3795 | 2025-08-19 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9e5a0377-3bcb-3aea-a1c1-1136da563d7b | -7.29111 | -43.68868 | 2025-08-19 03:36:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9badf078-09f9-3010-9a38-03df3a0268fd | -8.76182 | -46.69004 | 2025-08-19 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 153b5672-8b65-3da8-9a3f-52aaafcd4ff6 | -6.9415 | -43.61192 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b12e6a0-bee0-36c9-b12f-2580dc15335c | -5.97501 | -44.29431 | 2025-08-19 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bbb12a83-d718-34f4-959b-c31476cd5a5c | -9.48829 | -40.37542 | 2025-08-19 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cb80e8cc-73b3-3223-ab97-84d86e33311a | -6.93934 | -43.59228 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b90c1d35-e395-38ab-992e-fa05eb6990c2 | -6.93559 | -43.58678 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1a8a356a-a23f-3755-b957-9baa8aa0117e | -6.51666 | -43.45074 | 2025-08-19 03:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a1da723a-5db8-36dc-9171-3e49cd1610de | -6.16427 | -47.2815 | 2025-08-19 03:36:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0db58034-cb36-3b7a-be4c-f3bd1fa1eb12 | -6.0591 | -44.12667 | 2025-08-19 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5584241-7dc6-30a3-b869-675b4cdab8db | -7.13733 | -44.60723 | 2025-08-19 03:36:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffac96a4-e807-36df-a214-28d6e40eb188 | -6.95661 | -43.59166 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a35e2b6b-038d-3cd3-a75f-1d05e81114b0 | -6.93043 | -43.60981 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1d07471-5345-3cf1-a061-e74bc6039f7a | -6.54949 | -43.99176 | 2025-08-19 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aad4cab9-a17a-3346-a6a1-61b20ce3b6f5 | -7.59872 | -44.40209 | 2025-08-19 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7b5acf3-1a88-394a-89b6-b5bd4c3e3938 | -6.74899 | -41.56508 | 2025-08-19 03:36:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6762de13-493f-3903-a57a-f34d2965c6c5 | -7.14382 | -44.2097 | 2025-08-19 03:36:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ea60fe7-f2f6-3b9c-96e6-48778f9ec81d | -10.82591 | -45.04185 | 2025-08-19 03:36:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b1927a5-1c8f-3ea1-a671-4295cd8c7017 | -6.51787 | -43.44782 | 2025-08-19 03:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f300e909-8169-370d-b8d2-a8c6132fbad3 | -9.85135 | -44.69022 | 2025-08-19 03:36:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1922737c-6393-32ed-a10c-7f71dbeba3cf | -6.9318 | -43.60231 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6c192ab-015b-3c0d-afc7-31573026302b | -6.93527 | -43.61469 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 746c7a41-0dea-33e0-b9ab-0e142947369b | -6.92826 | -43.59031 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 814b6bdc-4e5b-366c-9af0-07262bc4abd7 | -6.95526 | -43.59911 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e1e7adae-8d53-3ffe-9505-733193634d5b | -9.85211 | -44.68623 | 2025-08-19 03:36:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e403e39-291e-37ef-bab1-55acc5e2fc4f | -5.97518 | -44.13048 | 2025-08-19 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 42672167-2adc-3b2a-8548-5d3c4574bd38 | -6.969 | -43.5863 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 8b4a7281-0979-340a-aed1-0b922092b731 | -6.95261 | -43.61377 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 82f56510-b975-33d7-ac03-dcdc80247eb3 | -6.96834 | -43.58996 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 49c54353-42c9-38dc-9cd7-cf98cca8bba9 | -6.93433 | -43.59404 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 44427ba8-ebd8-3624-a2bc-77087e47dc2f | -7.30516 | -46.28983 | 2025-08-19 03:36:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8ae06e68-5539-39bb-954e-a27c4af287eb | -5.97878 | -44.10976 | 2025-08-19 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| db9c26c6-a6db-39b4-8615-e1a733e1d515 | -6.95594 | -43.59535 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a7900a9f-970e-3749-8df8-287a34889658 | -12.04357 | -44.01382 | 2025-08-19 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44fbe270-51d1-31ab-9a89-30e4e4f3eef2 | -6.93446 | -43.58767 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c6481b91-507a-3b71-86b7-2aeef999f64f | -6.58334 | -43.08291 | 2025-08-19 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f5e57e5-3b7b-3b11-a2f0-f6e1f13820b0 | -6.55022 | -43.98774 | 2025-08-19 03:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17b95970-c722-31d7-bb37-cde71582ebcd | -6.75392 | -41.55555 | 2025-08-19 03:36:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e66cc496-2b52-3d6e-aa52-2bbccd0da43a | -6.96215 | -43.59264 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 49b10f42-be71-3c73-80b0-b1933e69e513 | -6.53098 | -43.43789 | 2025-08-19 03:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9b872e1c-e49e-31bd-aa34-62bb0ef44c69 | -6.93496 | -43.5904 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 92859568-7157-3023-946b-ade20770b574 | -11.81149 | -44.2634 | 2025-08-19 03:36:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aba0cb3c-ae87-3b6c-8d30-d1e1d2e64a79 | -12.45622 | -38.19336 | 2025-08-19 03:36:00 | NOAA-20 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f903d6f6-a4ce-3bc7-89e9-e3da06746549 | -7.30406 | -46.29584 | 2025-08-19 03:36:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 25a03ff3-a928-3a14-bb4f-75baf1449bc8 | -11.58287 | -44.85741 | 2025-08-19 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0735d7e6-3ca3-3ca1-bcc0-301cf1e8afa9 | -6.92974 | -43.61359 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a21ff7c-c52f-376a-871f-f71c1eef116b | -6.74387 | -41.53638 | 2025-08-19 03:36:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 39bad2e3-4e66-3b7b-8dfc-b3f5dd7903fc | -6.68061 | -43.68268 | 2025-08-19 03:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b1151c7-0002-3c75-bf88-913d960bb1f4 | -6.93314 | -43.59492 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b8bfa99b-1c6a-3487-b421-b88a5ff52785 | -6.94066 | -43.58504 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0becf67d-790d-3956-9bdc-4cbf17c0f21d | -9.489 | -40.37135 | 2025-08-19 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 48e70f7e-9111-3d13-bb89-6296c54e4c0d | -7.75165 | -35.25172 | 2025-08-19 03:36:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7c0d7002-94ff-36f4-9edc-746cadf5f3d7 | -6.938 | -43.59967 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c3efbfb-3883-3f5c-b024-2b5d1e9ad9bf | -12.99203 | -45.19398 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1e7a0e0-8acd-36d2-9610-1c7205ceeda4 | -13.42203 | -45.91396 | 2025-08-19 03:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf2d1c54-d7be-350a-a211-8ad533bca167 | -13.86664 | -45.55215 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 966bb97e-bcbf-34ec-a50f-ab1bbe4c96e2 | -16.47051 | -43.49232 | 2025-08-19 03:38:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1aa00125-ed64-3829-8829-2b8b03277b80 | -17.41096 | -46.71487 | 2025-08-19 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7ea1ee3-d08c-3f3c-b259-443641bcc248 | -13.58912 | -46.98825 | 2025-08-19 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b92c588-e022-3004-b9f6-54d37e768c5b | -12.98935 | -45.2034 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| baaaf39a-0d2c-31de-92cd-84a8c66fc717 | -19.19689 | -46.84744 | 2025-08-19 03:38:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b83afae-ff1b-38a7-930e-c8ff411d989d | -18.28178 | -49.61937 | 2025-08-19 03:38:00 | NOAA-20 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 44624b8e-56c9-3531-a091-e09c7e66ad9c | -17.33899 | -47.16707 | 2025-08-19 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37b37166-2240-3aef-850a-6057bd40fabf | -19.30667 | -46.84305 | 2025-08-19 03:38:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9adbfe6b-a124-32b5-a911-50d974d5c389 | -12.99562 | -45.20082 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 888a5896-f426-33cb-8886-ce4d72f1b209 | -16.47986 | -45.09949 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 011470bd-e24e-3b50-82cd-35ac92d5214a | -16.5004 | -45.10408 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cca2dc17-b62b-3cdd-b9f9-9a4da67e4634 | -17.81451 | -44.49248 | 2025-08-19 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 451e9eca-afa9-3bd3-b48a-13000abe0392 | -12.49432 | -45.56905 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b2a8f84-a97c-3f04-a8be-1b80fb71c1d8 | -15.92227 | -43.51672 | 2025-08-19 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f4448c6-a5c9-311f-ba15-81401bb5e77b | -20.24683 | -41.89494 | 2025-08-19 03:38:00 | NOAA-20 | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b8bff9c2-b98e-3089-aef2-4532f3e0fd35 | -16.50619 | -45.102 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3d150a2-3cfc-37a1-b0eb-d65fe724f5c3 | -16.0078 | -47.78784 | 2025-08-19 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff658328-a996-38a5-a681-85c0e47e04dd | -16.01387 | -47.78943 | 2025-08-19 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 336cc168-8072-3c72-beb2-aa35ea69f76a | -12.65656 | -45.80672 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6650d10d-ea98-3a61-b058-8d1634b80099 | -17.48174 | -45.85764 | 2025-08-19 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a88482c1-4255-31c5-976c-984dacc1f92a | -14.86627 | -48.04649 | 2025-08-19 03:38:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2f96f1a8-2d89-3131-bdc4-154acb445502 | -17.28583 | -44.89042 | 2025-08-19 03:38:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e967e1f6-4af4-3169-b11c-be205ede3a28 | -14.50539 | -45.94067 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6cec4b4-4314-37a9-aa35-3cd4de0a7eda | -12.63201 | -46.8897 | 2025-08-19 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0737229-187b-3800-94ae-49690d92bfbb | -16.47424 | -45.09357 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc91c508-0257-3bea-8202-f3dc7d3c409f | -12.99609 | -45.20266 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7631c7e6-ff4a-3c2d-ab3f-79237895442d | -12.99058 | -45.20147 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5e355a54-7079-3299-9b85-d1c3d03ac62b | -17.33838 | -47.16935 | 2025-08-19 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 897054ea-9135-36ce-81fd-fc8de08d895c | -17.40065 | -46.70828 | 2025-08-19 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d958ca3-0425-379e-8e2f-c58fa4714ade | -18.75633 | -44.40711 | 2025-08-19 03:38:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README16.md)
