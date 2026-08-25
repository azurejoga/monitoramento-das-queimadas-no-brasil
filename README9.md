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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47dbee26-f954-3b41-ac41-27312a67284e | -7.48534 | -55.36353 | 2026-08-25 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 282b3405-c2a1-3466-aaeb-fb094f60dcc8 | -9.15012 | -58.33207 | 2026-08-25 00:48:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 60c8e790-a38b-3d4c-879f-44d49833f828 | -10.06954 | -60.49754 | 2026-08-25 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| fa83c061-0d7f-330b-bbb9-ea6b8e2b66c7 | -8.59826 | -54.74235 | 2026-08-25 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 39be1cc2-91fa-37f8-ac4b-36618baa1453 | -9.06628 | -65.39806 | 2026-08-25 00:48:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 2519f9fe-c89e-3a52-b86f-ce75c9026d4a | -10.93932 | -51.08628 | 2026-08-25 00:48:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 39900903-338d-3ade-98e8-4921ff4141ab | -13.91718 | -54.03739 | 2026-08-25 00:48:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| cc0f558a-8e51-3d8e-8968-0d4da5ac28f1 | -8.56864 | -55.28587 | 2026-08-25 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| a88c9e89-7764-3637-ad7a-0f793c70d2ea | -10.07076 | -60.50648 | 2026-08-25 00:48:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 57444862-7422-301c-a200-b4e069a6f736 | -8.60742 | -54.72327 | 2026-08-25 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| b4d46cbf-01fd-3603-ae1a-e4d0db284de1 | -14.91916 | -52.63534 | 2026-08-25 00:48:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| f6c50418-ab46-3411-8bb0-ff06c1349ac6 | -10.90661 | -51.06688 | 2026-08-25 00:48:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 077db2b6-cecf-328a-b5c6-b330ea564db3 | -11.15858 | -53.99413 | 2026-08-25 00:48:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7c7419b9-1b98-34aa-b228-0315d0928f7d | -10.77767 | -50.94045 | 2026-08-25 00:48:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.7 |
| cb537557-07ea-3612-83c5-9c6a10154017 | -10.46759 | -50.44723 | 2026-08-25 00:48:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| f924a188-9503-3f01-bb55-509dc4d7bd28 | -7.48811 | -55.36961 | 2026-08-25 00:48:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 65a20da2-7a26-323a-aef0-2749b37f17d8 | -7.38969 | -55.18882 | 2026-08-25 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 6b4965e7-57c8-3cc5-8b01-71c7fb27b0e7 | -11.16623 | -54.00426 | 2026-08-25 00:48:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| e94a1be0-0370-3b1c-bd22-a964dc80ddc8 | -8.60404 | -54.74707 | 2026-08-25 00:48:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| bd1b9407-9168-3fd5-8cbf-bdd5c3784898 | -9.16986 | -58.33902 | 2026-08-25 00:48:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5186da47-aa5c-3e83-b36a-0696e8d71df5 | -10.79303 | -50.93769 | 2026-08-25 00:48:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 38.7 |
| fc44186c-ae5a-31ef-b943-f7317062376e | -7.2471 | -45.8685 | 2026-08-25 00:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| e6d6d787-563d-375b-8dcb-6edb96b88895 | -7.2713 | -45.37 | 2026-08-25 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 709790f0-801f-3d87-a9aa-8cb961cdcae9 | -11.1447 | -44.4632 | 2026-08-25 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| c395b3e2-38f4-3206-9edc-c99a7c9514aa | -7.4286 | -43.1182 | 2026-08-25 00:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 130.3 |
| d612440d-8c68-3fe0-87c9-9a5a5eee770c | -12.7986 | -44.278 | 2026-08-25 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| f2b51e93-024b-3a7d-bfcf-1894bd7ed94c | -7.2661 | -45.8443 | 2026-08-25 00:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 2aabe5c4-21eb-33df-9a0e-ad41c6c3f9df | -12.7792 | -44.2812 | 2026-08-25 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 82ad4d5d-2f7d-3b49-830a-56822db0aa55 | -7.2525 | -45.3717 | 2026-08-25 00:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 9f756b8d-8666-35dd-ae8d-bee5ba4a6cb6 | -10.9101 | -51.0886 | 2026-08-25 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 79398532-682c-3db8-b67f-be8a5cf9e0e4 | -6.1464 | -57.9359 | 2026-08-25 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| d9116a99-86f9-36ff-82d6-2df082d46ef2 | -10.3723 | -45.0767 | 2026-08-25 00:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 171.4 |
| 2f6a6f42-66bb-3e2a-b2e9-9b6305619667 | -8.0695 | -44.6552 | 2026-08-25 00:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 4cb08e1e-e732-3809-a99c-3c31f52d388f | -7.5475 | -61.3627 | 2026-08-25 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 7d860934-cf3b-3ac6-8dec-c3b9ad17bcfb | -10.3536 | -45.0561 | 2026-08-25 00:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| f067ffd6-56ae-360b-b685-8ad303e8b1f0 | -16.3946 | -49.9191 | 2026-08-25 00:50:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| ef0374ab-d61e-3619-b8a8-067648698d14 | -6.6411 | -58.4793 | 2026-08-25 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 93ace26d-baa8-3aab-bef8-29cf5ee4726a | -7.2856 | -44.0875 | 2026-08-25 00:50:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 08666a7f-bcf5-3800-9053-21e2b877e16f | -12.7797 | -44.2576 | 2026-08-25 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 230.3 |
| 69c028a4-83e8-3311-ba1d-76b698b065e6 | 2.5983 | -60.697 | 2026-08-25 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 2ef13a37-cc34-3e9d-8f0f-af67fac45718 | -3.5407 | -48.1673 | 2026-08-25 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 6fc53f62-aa11-36b5-a311-181ac0e65309 | -10.9294 | -51.0654 | 2026-08-25 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 142087fb-1cbf-3251-8fa3-1d5d600e9ce1 | -12.799 | -44.2544 | 2026-08-25 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| e6f29096-c674-3a2e-8c5b-3b0084d74a36 | -7.2901 | -45.3683 | 2026-08-25 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 82b8c2a7-25c9-3e6e-ba3f-592fd144e62b | -7.2659 | -45.8668 | 2026-08-25 00:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| d2fed806-6bed-3cbe-b815-5542b2355162 | -7.2903 | -45.3456 | 2026-08-25 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 53f798e4-c620-32f2-93c2-dc6b1e06f859 | -10.9291 | -51.0866 | 2026-08-25 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| a38900b5-9cb9-35d3-90b7-626cf6b841b9 | -7.0057 | -59.2575 | 2026-08-25 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 01ad184b-6da8-32c5-8c51-ab7080750565 | -11.4302 | -44.5382 | 2026-08-25 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 8a618f7e-f3b1-3d42-9ddd-f448add29c27 | -10.9104 | -51.0674 | 2026-08-25 00:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 3269de39-f03f-30ef-9401-adcc4892dfdb | -6.641 | -58.4987 | 2026-08-25 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 234.6 |
| 2385e401-d692-32d3-9854-793f15f5241c | -7.2474 | -45.846 | 2026-08-25 00:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| d55e726f-894f-3375-ae40-7ef3734d351e | -7.0058 | -59.2382 | 2026-08-25 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 61bb9328-f804-376e-8a88-65a793194e5b | -6.6226 | -58.4995 | 2026-08-25 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 192.4 |
| 3c0a2ac6-9f16-31ee-b111-912dc7261eb7 | -8.5973 | -54.7352 | 2026-08-25 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| e8050186-a4dd-3bb0-a96b-1e1e8444eff8 | -10.3918 | -45.0512 | 2026-08-25 00:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 70cc70bd-491c-3fbe-a76d-8adff89f41aa | -3.5406 | -48.1889 | 2026-08-25 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 2ee0350d-ca2c-301c-8492-76c47891c64f | -7.2858 | -44.0644 | 2026-08-25 00:50:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 6c56d46e-e441-37c6-950c-7ef9c35b62bc | -6.6227 | -58.4801 | 2026-08-25 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 37664860-2064-36fb-8c21-4bd9dea8bc27 | -10.3727 | -45.0537 | 2026-08-25 00:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 478.2 |
| df4a4e4c-fddd-306b-b1ab-5a5ff8e29dde | -10.3731 | -45.0306 | 2026-08-25 00:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 4221923f-f6a3-3ead-a327-89998d8801ec | -7.529 | -61.3635 | 2026-08-25 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| ee317f95-93c7-3e5a-bcd8-cfbe663ab37d | -11.4306 | -44.5148 | 2026-08-25 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| e5b27b29-f59e-31c4-ad3a-e8ac6fa277b9 | -3.5222 | -48.168 | 2026-08-25 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 1a1ff093-ac6e-35d8-8f42-d90edf8b785e | -3.5221 | -48.1896 | 2026-08-25 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 716130be-910d-3333-9464-1101b45884f4 | -11.1443 | -44.4865 | 2026-08-25 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 69ef35d7-7f80-3d82-8010-18580e98cd3f | -7.0032 | -59.25389 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 0ee237f7-110e-3ada-a4fa-0b2e416ece01 | -7.54387 | -61.3616 | 2026-08-25 00:50:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 472b8f76-6e9c-3aa6-a0ac-0b268b5f4155 | -6.13518 | -57.82797 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| ef5c90ee-1c89-313d-8b13-e7d748c91084 | -6.35217 | -54.78119 | 2026-08-25 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 0a5e5943-4c2a-346d-8959-ee9d0a7f8d0a | -6.95368 | -56.49478 | 2026-08-25 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 94c8a6c3-e9fc-3111-b86a-d9f23880dd5e | -6.80128 | -59.45522 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6ddff4fa-e89c-3de7-9f83-2a379918b16b | -6.73998 | -59.6746 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5caeaccd-decc-3b36-bc50-169ddbab5654 | -6.15105 | -57.93768 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| ce64a913-ea40-32a6-baaa-5fb5c46b409c | -6.26458 | -55.42604 | 2026-08-25 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 06e94290-59a2-3e52-9d8b-070b0f5b467c | -7.43657 | -59.77954 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ec17e739-3b9e-3cb9-903f-2f10b5083a8b | -6.8061 | -59.69281 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 9a3bccc2-cc86-3192-94f7-1c38883392d4 | -6.81696 | -58.65535 | 2026-08-25 00:50:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 3ebb9765-4995-3788-a19b-9f2ac4e6ded5 | -6.13677 | -57.83894 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 95dbba8c-7eec-3b6c-a5f5-49b73ed7faf4 | -6.7578 | -59.67207 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cfb04eba-87ab-37bd-b44a-aa2af30df8f5 | -6.81556 | -58.64548 | 2026-08-25 00:50:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c12ab456-14f4-333c-933d-344ebaf781df | -5.78648 | -57.61566 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 48fb312a-939d-3fd8-9511-9a603aae3fcf | -5.78994 | -57.5679 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 42bc4d4d-4184-39d4-9e7a-8ff2eb15ce69 | -7.01991 | -59.242 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0fb3d736-9ec3-35de-9f13-12d9828a48b4 | -6.14698 | -57.70082 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| c228e31e-60d0-386b-af94-2a42664d1b10 | -6.19236 | -53.4954 | 2026-08-25 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 2338eaff-a0d5-3444-9400-e52be6410505 | -6.43444 | -54.96445 | 2026-08-25 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 8350496c-2019-387c-8283-6bdc304dbe45 | -7.00189 | -59.24458 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| cdc01f39-4308-31b2-b7c1-e76ec367bd92 | -6.5497 | -58.52021 | 2026-08-25 00:50:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7311c179-2286-3d60-b223-3678191fa74d | -6.79089 | -59.6488 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 324850ff-3d2a-3890-b697-048c75f481d1 | -5.79781 | -57.61941 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8fa5cfce-60f9-3277-985d-5464746deb08 | -6.13997 | -57.86106 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 77adfd75-c41e-332b-935c-2fd3912dcbdc | -6.13837 | -57.85002 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| cc828f0a-ec14-33ae-bf57-8478c992c880 | -5.93694 | -57.73274 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 38ae536f-384a-3ba0-baa9-bea626d997c3 | -6.43715 | -54.98208 | 2026-08-25 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| ce579756-b0b5-3cbd-b280-106597a2e716 | -6.84735 | -59.45793 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 28ab546d-78b3-3f8e-8a1c-2a98024cdf97 | -6.63916 | -58.50119 | 2026-08-25 00:50:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 226.0 |
| 07467ce2-5bdc-37ce-99dd-d06ee391bef8 | -5.95428 | -53.60632 | 2026-08-25 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 5501030f-d3d3-3042-826a-b54a284e6ea4 | -6.86014 | -59.41867 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6825b33a-dcad-361b-818d-be7e8993c562 | -6.26208 | -55.4093 | 2026-08-25 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |


[Clique aqui para ver as próximas entradas](README10.md)
