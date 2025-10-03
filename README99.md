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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdd66f7e-2c86-3b21-8025-b03bf03dc215 | -7.77648 | -42.57255 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7d309d95-e630-3379-baa5-1416ea8b79d6 | -6.72657 | -44.55142 | 2025-10-03 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b21fef0-61a0-3256-8848-c64b077a724f | -11.86839 | -48.00675 | 2025-10-03 04:32:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7685829f-5971-37ca-ac84-f9a017eea661 | -7.05798 | -43.22921 | 2025-10-03 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fbe97363-8eb7-30c3-8bee-0af365a0bacd | -5.63341 | -43.91953 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 9a2c68b7-2de9-3762-b9b5-065c6a994fae | -7.76003 | -42.53901 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fe818be6-e32b-3def-889b-dbb361b836b7 | -7.75854 | -46.24377 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| f4a98db2-3bb8-317f-bdaa-d1cb5e1c9449 | -11.5521 | -47.65516 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d0894ed-5928-335d-8476-46ff9451e885 | -7.75058 | -46.25032 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 020664fe-b47b-30a0-8530-96b07d58b886 | -11.8365 | -45.02145 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51e014fb-d537-38dd-822e-f597f3bd061f | -10.89548 | -46.69722 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dffcd02e-bb24-3161-a4fd-783d00f09a39 | -6.22283 | -44.24815 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 95e01ad1-8009-3c7a-9cb2-834f45f8c210 | -7.79493 | -42.53256 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4a31db03-0f8e-3be4-957d-598cef8fc897 | -5.63475 | -43.91059 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a2a5b261-2e3f-3a5b-bd78-58b9a57b8bda | -10.60968 | -48.72002 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72b4685d-42aa-3336-bf53-c28c58cdffdc | -10.84706 | -47.21943 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82fe0c11-229a-3344-a307-864d5e43bf5d | -11.59999 | -42.87413 | 2025-10-03 04:32:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9bf53836-7dae-37af-b0f1-bea89a971567 | -4.67183 | -45.7999 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1688573-c720-3498-b938-a5e968b15f06 | -7.76025 | -46.25549 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| a71f6e0d-e22d-3c44-91e0-f0bc8593b1b0 | -10.24469 | -44.94688 | 2025-10-03 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 322c7644-13e0-34b7-8d70-cbd51f27a722 | -7.75533 | -42.55796 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 37.9 |
| 6fbd5037-3acb-33c8-b144-2674f0df9204 | -7.29897 | -44.1894 | 2025-10-03 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98a37b7d-f9c4-3ecb-8792-3351835da71e | -10.90119 | -46.72913 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac4bbe27-baff-316f-9641-e841d1578e9c | -9.06804 | -46.6524 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 86c83757-9e3e-32b4-9ab7-c4556a63eb4b | -5.82774 | -46.3613 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d352bb5-fa2f-34b7-bdba-6191651f1e8b | -5.54492 | -44.65208 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08f4d83a-a727-3d24-bd57-c3813b2e20ec | -5.46342 | -44.99733 | 2025-10-03 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c6c2ac6-6f7c-3e48-8e31-c3109831aad0 | -6.6542 | -42.78354 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a76410cd-6e0a-3a9e-8046-ebef165cb638 | -11.5913 | -47.66869 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43022c29-10d7-3688-894c-2e848b583e70 | -10.76963 | -45.3394 | 2025-10-03 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d72600d6-e0ba-38a6-9b04-ab1194cd61a9 | -7.90672 | -43.52961 | 2025-10-03 04:32:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1240b3d9-4e6e-392f-900e-cdf4d8703eaa | -10.65702 | -48.48382 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03e82b9a-427d-3f3f-9663-dcb8cc3bb1e1 | -5.87169 | -44.12608 | 2025-10-03 04:32:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cae9d5e5-bab3-35c5-82a9-69ac316cfebe | -9.92284 | -50.90318 | 2025-10-03 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 11bfa01f-81e5-30b6-83fb-5a3f0787bcd5 | -10.28668 | -50.30725 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e4f349f-7f40-383e-9487-cfabff16d52a | -9.34351 | -45.72501 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf733abf-d63a-3da4-88c4-5e9cd12c2ef1 | -11.7958 | -47.92937 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 977e6fb7-86e5-37b7-8585-bf33a8f7a670 | -9.94476 | -43.74652 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 56f13663-50fb-3231-ae35-4121b5df60d7 | -11.68114 | -47.49654 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b121de63-ed50-3aa0-8adc-16053222c7b3 | -7.30155 | -45.27035 | 2025-10-03 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b26717ab-f2d2-3ca9-9dc7-4da53b11dae1 | -10.44096 | -49.35425 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c58d32bc-6e84-39c3-a6a0-f2418ab5073c | -7.19387 | -45.38367 | 2025-10-03 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24a34f1e-e5a0-3d5c-9efe-13ec5e4e8ce7 | -10.90407 | -46.71019 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1826d398-18a2-3405-9af9-10ca8b1f7d8f | -8.62327 | -54.97745 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 136f6733-9923-39bd-929f-69438c300c30 | -11.72169 | -44.46784 | 2025-10-03 04:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 424c7e21-48b6-397f-b2da-95f28921f353 | -6.4162 | -41.74226 | 2025-10-03 04:32:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7694dd40-3fe5-3ea0-a6a7-12f57247428f | -7.74256 | -42.58691 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7365ff23-407b-395b-8c73-0e6347268885 | -5.74241 | -44.26172 | 2025-10-03 04:32:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e8fd3a6-b837-32b3-8032-e4148c68923d | -11.58123 | -47.66711 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48c68cdb-e840-3f55-8958-58cce14aea71 | -7.73208 | -46.23243 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2786a15-10d1-364f-a85c-8a25b574120d | -6.64793 | -43.59478 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01e6e640-0913-358d-8be5-3f9a24863370 | -10.75377 | -45.34584 | 2025-10-03 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e18b21ca-896d-30c3-a795-4f61d422f2f5 | -11.11741 | -47.85962 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 269c403b-b5b8-31a2-b083-639186803742 | -12.22468 | -43.77026 | 2025-10-03 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b23ba2ba-2256-31b0-9c65-c9700f2d5dcb | -8.86845 | -47.67571 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 355d79c9-63b2-3f24-bac0-7ac8516a0b25 | -11.48965 | -45.013 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c6bc97c-f147-3f7a-85e4-c2fd7efe7682 | -5.6931 | -42.7058 | 2025-10-03 04:32:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b586b4c9-213f-31fd-acfb-7746ae3f41e1 | -8.59016 | -44.77916 | 2025-10-03 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa9c67d7-f7ad-3cef-a8b4-d3147e36621b | -10.26644 | -50.34561 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 139f00f5-5021-3e0a-a574-bd96a27b2572 | -11.13977 | -47.18473 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6430d19-7f7c-3a94-9a92-122191ccb09a | -6.03904 | -44.62924 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6b51ec5e-27ee-300c-adaa-f958a22aa08a | -6.37418 | -43.87408 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 210936ea-400e-38da-9fa8-604a558f8dac | -10.88689 | -46.70751 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e51c6532-9562-3598-84c2-f001c8ef0075 | -10.29503 | -47.93358 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 205fb749-6e19-311d-9b3d-a725d643ea43 | -6.04447 | -44.61751 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 4c9a7601-95a3-3b13-b49d-12366df9834b | -9.33603 | -45.67921 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9230f109-f232-3dce-bc0d-c5c0ba3e1f82 | -11.0852 | -47.86907 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2c424b2b-b299-3996-ab25-048cb0bb63ee | -7.89625 | -47.31477 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 869f51e1-1bda-31f3-8093-5d9c9e004b58 | -6.00749 | -52.38343 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a592403-5658-335c-a489-480c54093a63 | -11.09079 | -47.70516 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4699827d-4a15-3737-85d5-bab723fcfbdc | -6.31905 | -43.88377 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5300a89a-3aba-33f9-acd5-0afa80e68e13 | -11.81866 | -44.90326 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ac16b2f-6d65-3b5a-8cbd-fcf0edc2670b | -9.16096 | -50.55989 | 2025-10-03 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e09ca113-35b3-388f-b2bf-78d6120f6254 | -10.86274 | -45.41771 | 2025-10-03 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d47098f-8294-39c4-babd-efc16eb4c06c | -7.76252 | -46.26347 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 1dcda832-6e72-3b11-9f7d-32bb23e39128 | -11.63118 | -45.05357 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fde4bfa6-bdd8-391c-8196-9b75b20639b2 | -4.66507 | -45.79882 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43720365-5d57-38be-88c2-36b2fd00723d | -10.85835 | -47.22082 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 673d48a6-03db-3804-8270-fd36d047467a | -5.97662 | -44.07384 | 2025-10-03 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c143d4f2-8234-3acd-bda8-235013b5324b | -7.79117 | -47.37723 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7adc0679-3973-3b2d-be4e-168ca5ed8cef | -5.61697 | -51.94304 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20d2b08c-f68d-3c13-ae68-2584842dfdc1 | -11.67832 | -47.49234 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aba5f72a-6936-36e7-97f5-010569e2df37 | -5.84049 | -45.80426 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5157a098-ac46-35b9-9845-138517d75a05 | -9.3414 | -45.71534 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21e01f81-0edd-3abd-8018-293a36fdfdf6 | -6.7279 | -44.14674 | 2025-10-03 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 97527070-7dcf-378c-98e8-5a074d918789 | -7.30689 | -45.25895 | 2025-10-03 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 02ed205a-b333-3fdd-b206-4167ff7fd1a2 | -10.34434 | -48.18204 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e264771-d5cb-36df-9a9c-a9c4d020c4c2 | -4.65324 | -47.54954 | 2025-10-03 04:32:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7a27e9a-d1e1-3ad9-a743-0f19358e982c | -5.56025 | -47.22608 | 2025-10-03 04:32:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d3f866d-3f4b-3b4d-bab9-722347057561 | -7.79273 | -42.54789 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 00134b49-484b-3a68-b331-c6c8b79229aa | -10.29698 | -48.28932 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5485a34-45ad-33d1-bf67-643f0e318c85 | -11.17792 | -47.75584 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 25975dc0-ee10-3bb7-8a29-f1816f6af057 | -7.00676 | -47.18294 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef1ea654-67ac-305d-8d72-778ce028242f | -7.7754 | -42.5801 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| ef56cfb9-8923-3df7-b6aa-6b65b1da3e0e | -10.92642 | -46.7208 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67327a32-fecc-366f-93ed-02a1d2636747 | -9.9048 | -43.7146 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0e3d883f-b60a-3d75-9d45-f5f063e78524 | -9.91365 | -50.50558 | 2025-10-03 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5f85757d-ecf7-3139-85c9-38808672907e | -9.94582 | -43.75936 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 55af2fa9-9e3b-3af8-b7a6-5e6cf7ec29e4 | -6.55428 | -43.88752 | 2025-10-03 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 585e4742-8086-3c9d-befe-3a2bd8f25b7c | -11.18625 | -47.74624 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README100.md)
