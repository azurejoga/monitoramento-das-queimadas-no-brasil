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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 261537cd-b3f1-3181-8053-1d4b969335ef | -12.09604 | -44.99498 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6ad544fc-221e-304e-b033-f2a1e6af9e0d | -12.91823 | -45.83908 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a90d95a5-afa7-3122-ac2d-ac282ceef75c | -10.56146 | -50.37062 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 41dc16f5-60d3-341e-8197-55db5ace20ed | -9.83167 | -46.35888 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9c81638b-5f67-3fef-923b-9074609fe899 | -10.02571 | -45.56637 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e49cf553-67ad-3ab1-97be-5c8126194deb | -8.73315 | -46.45836 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 235a9fc2-53b4-34b5-b6dd-54dd4b599bea | -10.02081 | -46.16134 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 81dee0f9-7825-3051-9e53-bbf8b0d87788 | -12.0727 | -44.98576 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4f9c9d4e-4021-34ae-b205-54f533008139 | -12.38411 | -48.16237 | 2026-08-31 16:50:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| a37db7c1-a126-3f63-8db6-3964aa88d793 | -6.17584 | -45.90949 | 2026-08-31 16:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0378f983-dea5-36be-ba3c-abf9f053d303 | -13.54104 | -59.74853 | 2026-08-31 16:50:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7ab822dd-da59-33bc-bfc2-f569a29a52b3 | -5.58706 | -42.3272 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 04634964-b450-337a-bbfe-f969ce9ddf68 | -7.4203 | -44.25722 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| aea1da95-4888-3088-b2ab-195e335210b1 | -11.37186 | -45.22141 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 00a7c266-691b-38b1-b04c-c8b77562f5cd | -7.29177 | -56.6861 | 2026-08-31 16:50:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3374d9c3-3916-3f11-a966-817919ac58dd | -9.8956 | -46.62767 | 2026-08-31 16:50:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 030b83e0-954a-36e6-b0f1-953c417168e6 | -6.72913 | -45.06946 | 2026-08-31 16:50:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 839f7abb-c944-3c4d-8ff0-3ee2569e69d9 | -9.96796 | -46.77801 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7d83c339-d701-3fef-b760-e72e004817fa | -10.12654 | -50.31094 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| b99f8512-83da-3c36-afd5-c3a53994eb5e | -12.08761 | -44.9879 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 55f303c4-5303-3a54-addc-4d335d0d1490 | -7.04273 | -45.40739 | 2026-08-31 16:50:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bc9f03ea-6a86-34f6-bd19-be946471245e | -7.28672 | -52.53988 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ee8ca4fe-9821-3807-b6ef-cd5306d88a30 | -6.52009 | -51.43893 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| bf6dae1f-9300-3b9b-bf89-fa042742b082 | -10.5775 | -50.38389 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 9fb670a0-dee5-3fbd-9dee-071e497f1841 | -10.55103 | -43.92308 | 2026-08-31 16:50:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 016d00e4-8970-3e59-af72-96a4883baba2 | -11.04802 | -49.68025 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ea188573-3f83-35eb-81c4-f3b5044b500b | -10.06018 | -48.69736 | 2026-08-31 16:50:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| fb434479-8321-3665-933b-72d18c17f67e | -9.20078 | -48.00289 | 2026-08-31 16:50:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 2962a1a9-1bc8-3cb4-a7da-daf5668daced | -12.07509 | -47.20808 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 0d1a4810-29a7-3716-a298-089464f928c3 | -10.13098 | -45.74952 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6a5f853f-ebf9-3e20-a542-b575097472b6 | -13.44248 | -51.76203 | 2026-08-31 16:50:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1318118e-cebe-35cd-aa8b-32421361356c | -7.02835 | -45.86023 | 2026-08-31 16:50:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e07f8d17-64d8-3c43-a3ca-f6eae1f66cc0 | -7.58899 | -61.34222 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f34f8e43-c467-33e2-b75d-75d58926d973 | -11.25502 | -45.10163 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 31f75316-3b5e-32f0-a9e3-465243c301ae | -13.38644 | -51.77174 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 67d1a8a5-5aa0-3d8c-a4e3-b2d23ea59681 | -7.79078 | -44.06364 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1dbd3aea-3f1e-3ca1-add9-e316186c1887 | -10.86059 | -45.37484 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 81605135-d739-32bf-acd8-641c1f3231ae | -11.04518 | -49.68444 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c399301c-99fa-3f2c-82b4-29649e321241 | -11.91781 | -45.08202 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 4e4ae7c2-e22f-3a54-b245-d709bf6060b0 | -7.63678 | -44.83196 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b4fa95c0-53cc-3f8e-8197-35a07d95c60f | -9.15514 | -59.50254 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 28a3a193-117e-3256-a935-3554ae283dec | -5.77263 | -44.11986 | 2026-08-31 16:50:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3662ca30-9a6e-38f4-af64-858cc5913925 | -8.21979 | -50.77903 | 2026-08-31 16:50:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5642e7c6-c5f4-38c4-bff2-4ff4aef926e9 | -5.76102 | -44.12541 | 2026-08-31 16:50:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0e19ae9f-68d7-38d4-ac7b-7900148c0d55 | -6.2396 | -44.85098 | 2026-08-31 16:50:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df2c7f8d-2937-30c9-a6c6-f21c7896f852 | -10.46882 | -46.55308 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 69dbcc19-8abc-36ff-8478-150d61d758c6 | -10.85415 | -45.33453 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 95d6c43d-b54a-32d1-908e-fdb314fce1b0 | -5.76799 | -44.11687 | 2026-08-31 16:50:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 12f09779-30a2-3d84-af62-afc90576b133 | -8.64213 | -47.30967 | 2026-08-31 16:50:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| ddf34183-a3a2-3472-8003-85f7063e4675 | -11.26574 | -45.06223 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0d805aa0-cb75-3e44-bab0-add0c3016188 | -9.15536 | -59.55281 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| c834b221-7916-3a5c-8cb6-a4622d26d270 | -10.56175 | -46.16705 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 39afba64-7b3e-31a4-84b8-fc72df904433 | -11.93291 | -45.06333 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f7e763a9-a03b-3d82-90fe-20cf616e3f7e | -7.10205 | -45.7806 | 2026-08-31 16:50:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 497c5ace-e6d2-317f-80bc-3e9cb74cc905 | -10.31463 | -49.99537 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 871819d1-c266-37bc-9d6f-796a96a1a765 | -10.82621 | -45.36393 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 64125caf-a1f5-373c-a534-4ff540bde6f7 | -9.80268 | -59.4419 | 2026-08-31 16:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 10fa00fa-44c0-334f-adf9-60129884b8e8 | -10.50519 | -45.04295 | 2026-08-31 16:50:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 58c05f0a-faf5-3422-90e2-31a8cbfc9a43 | -11.84335 | -41.51044 | 2026-08-31 16:50:00 | NOAA-20 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| df3411f4-7a00-30f7-813e-5b31d880f94d | -11.20376 | -50.6233 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| caa0484c-6370-3e91-a0ef-f47a2041b259 | -8.86605 | -47.07664 | 2026-08-31 16:50:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 296daf15-13ef-3e2b-ac1e-34dd873d7528 | -10.84372 | -48.33873 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2defce94-f874-3f30-8250-04c053336b65 | -13.96904 | -54.40657 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 130.0 |
| da7a2c9f-2a2a-3bb2-b65c-5aa662980f61 | -8.91897 | -44.17119 | 2026-08-31 16:50:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9b513c97-019c-3dfc-996c-75968e64027a | -11.79685 | -47.66994 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 39c863e2-746a-3d81-a8e2-5adb31577ca5 | -13.8279 | -54.03371 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9d3de5f0-e7c8-3407-b0cd-97a9e82da926 | -6.81317 | -43.4977 | 2026-08-31 16:50:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 7800871c-8cee-3384-86ff-eab3e1e1f2c8 | -6.93538 | -55.64261 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6a8ede3f-c414-3023-8be3-7291e62b4634 | -11.19854 | -46.11327 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| a5ffaa2f-d133-34ec-a1ac-7d2b92854949 | -10.09908 | -50.28806 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3e48809d-11ed-396f-bfd9-41a88dc90e7e | -7.62859 | -44.92612 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a1a1eac5-bb71-3db9-bf3f-27d9ba82a4cd | -7.79328 | -44.07885 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 40.2 |
| c8e81370-27af-339f-a19b-e4bfdcd18e6d | -12.09317 | -44.99976 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 8f7f5442-d365-3ea3-a7bb-f92d3d639e0b | -12.09887 | -44.98993 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e0f65d22-9768-3c70-922c-4167904b45d5 | -11.21598 | -46.11349 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 2287edb3-fd10-3c07-98e5-80a7087a2674 | -12.07408 | -44.99427 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 31.7 |
| c38db879-f6e2-3ff5-85ad-923da0c98a22 | -7.49113 | -44.89001 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 14027f74-c835-3b30-a638-5eca5e2cec66 | -11.23326 | -45.37169 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c6afeddd-a4af-31d8-8c4e-917945739d43 | -11.05535 | -49.68291 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93f665d6-0c8d-3de9-82bd-d33c267f4921 | -9.68701 | -47.94195 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 106ef318-a406-3be8-81da-a23ea911e73e | -11.91445 | -45.06165 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a22ea54-bdb7-3190-be67-832e6726ce2c | -5.44968 | -42.6563 | 2026-08-31 16:50:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 0e11fd3c-f3e9-3441-8494-eb69e10ed5fe | -7.11908 | -42.20041 | 2026-08-31 16:50:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| dd096578-9683-33b2-b62c-199d613bf457 | -12.08829 | -44.99208 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 586f364a-227d-3c83-bbe5-61e6ed3d17ca | -11.22606 | -45.14848 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d66967cf-a28e-3701-9f32-95598b3b5edd | -7.65058 | -46.72827 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 430ccb82-85ad-380c-be2a-bb2ca0efe0a3 | -7.62628 | -44.9358 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4a203460-172c-39fe-a4d0-0773c2d7fd96 | -11.20939 | -45.11332 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f01fbe3d-4018-3c23-876f-7553367fe180 | -6.34759 | -35.24675 | 2026-08-31 16:50:00 | NOAA-20 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 1c0e3b3d-7673-36e5-9944-ca40469e65ac | -11.34293 | -45.22211 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a8c62e40-d2bd-3129-95ff-e45a703ff840 | -5.57864 | -42.33323 | 2026-08-31 16:50:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| f54d4620-baa0-31ba-90b0-9df6c752a6f2 | -7.50337 | -34.909 | 2026-08-31 16:50:00 | NOAA-20 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 3bf27647-af0c-3430-b6a0-d3a7c90db395 | -5.58384 | -45.74162 | 2026-08-31 16:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b3c3c5d4-747f-3310-aa0c-c7c7a2699330 | -7.36057 | -55.90542 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| d83da683-38f2-370b-b261-a1ecbbefd40c | -7.92913 | -44.29544 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| da865bc1-3ef1-3479-95c7-de33443fc5e9 | -9.42075 | -45.67958 | 2026-08-31 16:50:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 7d6737ec-a98e-37f9-9001-c4844340d818 | -11.15734 | -45.04157 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 0410d1a3-d93d-344e-9eed-b7970f4dbdd1 | -7.62197 | -55.29564 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d8e56016-7af5-31fb-8284-c6f8bea2b2d0 | -11.22621 | -45.37276 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fd1dec8d-892e-315c-bc86-edce4352b0ae | -11.96466 | -47.74721 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 37.8 |


[Clique aqui para ver as próximas entradas](README156.md)
