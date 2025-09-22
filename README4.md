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
| 41e2cf64-ecd1-322f-b679-96df664568aa | -4.45429 | -46.91179 | 2025-09-22 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 699162d7-cc5e-3c1e-979a-81d7c7ca9d14 | -5.03501 | -43.60369 | 2025-09-22 00:13:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3af3461e-c016-327d-aa5c-3b8dc4492368 | -4.26093 | -48.60265 | 2025-09-22 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 93e2f4e3-8fae-32ca-acdf-a0aa6254e9a4 | -7.62981 | -46.82618 | 2025-09-22 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f7c576e4-71ab-3f39-b3b6-45d82b9c478c | -4.87676 | -45.80286 | 2025-09-22 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4c91bf3f-2fdc-3b7b-8b08-dd7bf000fe51 | -5.57668 | -49.00494 | 2025-09-22 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1862d6ed-6fb0-31ab-b981-9a35a39900d9 | -7.36049 | -44.55259 | 2025-09-22 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 72d95e73-d418-3fb3-bcb4-b34735cfa5e2 | -7.38193 | -44.57713 | 2025-09-22 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d3c05b12-2f9f-3884-9ff5-03e070a7c23e | -4.4507 | -46.91809 | 2025-09-22 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1a159c68-5f7e-3436-9b91-d43f696c1f3c | -3.70071 | -49.56961 | 2025-09-22 00:13:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| a1f4a35d-16ed-3b12-926c-9865483e5f62 | -3.70313 | -49.57507 | 2025-09-22 00:13:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 252e29e3-c955-3a95-ab4f-ab248c743d28 | -6.89988 | -44.76372 | 2025-09-22 00:13:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 3cceb56a-c9af-3fd7-8ca7-efab240d1bca | -6.97166 | -44.74797 | 2025-09-22 00:13:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f5897bda-1a4c-3ab5-9736-3d50426dc8d9 | -4.99149 | -45.15882 | 2025-09-22 00:13:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| dbab5a88-c68a-3c76-9ab3-cb96eeeb9387 | -7.42108 | -46.39108 | 2025-09-22 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 224.4 |
| c9780076-7fcb-3f7c-9164-12223d9f205f | -5.56038 | -46.2818 | 2025-09-22 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3537cc13-9ec4-3833-bed4-f9a9ca8dad63 | -4.4529 | -46.90134 | 2025-09-22 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7a8a8c28-49dc-3c26-b124-c7e1f99ccb97 | -5.11016 | -46.16726 | 2025-09-22 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e6210a14-dcf4-30c3-9602-b9ce185a3d6b | -7.4307 | -46.3898 | 2025-09-22 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 7eb4013f-9f8e-3f5f-a80f-fb9e3e4d62b1 | -5.03625 | -43.61256 | 2025-09-22 00:13:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| f9cb0f58-cfe7-3891-9c8f-e87ef4526b62 | -6.05138 | -46.39384 | 2025-09-22 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4b41ea95-717c-3aa7-a02b-9cf997318417 | -0.94256 | -47.35286 | 2025-09-22 00:16:00 | TERRA_M-M | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 03aee2f9-9ae0-3a87-8882-68ec524a6410 | -0.95195 | -47.35156 | 2025-09-22 00:16:00 | TERRA_M-M | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8c219ff8-2756-37e2-b24b-16911aed5966 | -0.95334 | -47.36162 | 2025-09-22 00:16:00 | TERRA_M-M | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| fffdfed8-0d7a-3e5d-8300-e0651996dd92 | -11.3217 | -54.3564 | 2025-09-22 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| c2e8c59e-3edb-32cd-b2ab-0ce71d1ea6d5 | -18.3998 | -42.8395 | 2025-09-22 00:20:00 | GOES-19 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.9 |
| a2f8d253-ce24-3764-a46c-5bb2eb725ecd | -20.2735 | -55.5141 | 2025-09-22 00:20:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 53157a89-cea3-31b0-abeb-313ccf16a59a | -11.6247 | -52.8624 | 2025-09-22 00:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 02df795c-d3dd-3a38-8db1-b088ab7b5230 | -15.9969 | -59.4651 | 2025-09-22 00:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| c2c44294-2cee-3700-b27b-84d532985bef | -10.4129 | -46.142 | 2025-09-22 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 304.2 |
| 9acdd089-1905-3398-a18b-1ec41c30fa89 | -10.2991 | -46.1335 | 2025-09-22 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| b88761c4-74d4-30f6-9fe7-6d650d3675d5 | -20.2537 | -55.4959 | 2025-09-22 00:20:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 17edd758-2d03-3d1b-868f-a4172fd6ceff | -11.6436 | -52.8605 | 2025-09-22 00:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 46d775ab-2f8d-33e2-88aa-68eb43edbafd | -10.3375 | -46.1062 | 2025-09-22 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 41f8c7c3-0aa0-3615-bad5-0f41b1357fd0 | -22.9828 | -48.3559 | 2025-09-22 00:20:00 | GOES-19 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.4 |
| 22a7c536-9dd1-31d6-990d-91780a4ad070 | -4.3197 | -48.0908 | 2025-09-22 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 734105c6-0988-383b-9656-d26528bcf788 | -19.6274 | -57.7504 | 2025-09-22 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.4 |
| 3881a242-cb2c-38a3-b900-6e12881726f9 | -10.4132 | -46.1194 | 2025-09-22 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 400.3 |
| 7c9f8624-b777-34dc-8c18-9284187d50b6 | -10.4322 | -46.117 | 2025-09-22 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 303.0 |
| d2fb9de4-0c51-3752-b581-d31a39c0c93a | -19.6278 | -57.7296 | 2025-09-22 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 9ce5c4c0-4b10-3d4d-b701-80112d90ae68 | -20.274 | -55.4927 | 2025-09-22 00:20:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 3c37e171-c328-366d-b595-6adf129ee005 | -11.6439 | -52.8397 | 2025-09-22 00:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 122.9 |
| d6b37ce0-fad9-3360-9294-ec8107d215dd | -16.0163 | -59.4633 | 2025-09-22 00:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 54307196-5b00-3ad5-a730-8692d5e3716b | -7.6596 | -61.1297 | 2025-09-22 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| ac69de71-bd24-3807-872e-e105c6461951 | -18.399 | -42.8644 | 2025-09-22 00:20:00 | GOES-19 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.7 |
| cf82e4ae-6166-3ef6-844b-3a60a4de8044 | -21.8351 | -53.9546 | 2025-09-22 00:20:00 | GOES-19 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 114.5 |
| bf6d59de-f14e-3d86-b8fd-c5d40d3912b9 | -19.6478 | -57.727 | 2025-09-22 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.1 |
| c417e13e-c5e8-3530-a927-9147b4ca4a87 | -11.322 | -54.3359 | 2025-09-22 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 7d3dfcff-d092-3f3f-85e1-c954a13d8c92 | -10.4319 | -46.1397 | 2025-09-22 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 269.0 |
| ce0da977-92fe-3041-9aa0-ddcb09689f33 | -11.6249 | -52.8416 | 2025-09-22 00:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 575d081a-d0ca-37a9-a3d1-9c6c4b30c1dc | -19.6475 | -57.7478 | 2025-09-22 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 8d4591bd-4eb1-31b0-b174-e5d842ccd947 | -11.6439 | -52.8397 | 2025-09-22 00:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| eb652211-76ac-30fd-a83a-00343d003c60 | -11.322 | -54.3359 | 2025-09-22 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 73b439cc-2d73-3afc-82a9-091ba3c139ad | -10.3181 | -46.1312 | 2025-09-22 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 2e6f0ff5-78c8-3b88-a2b3-604c578b4019 | -19.6478 | -57.727 | 2025-09-22 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.4 |
| 7865caff-4bdb-3a58-97cd-6738860ae6a2 | -4.3012 | -48.0917 | 2025-09-22 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 283b3c6a-7da7-3800-8191-2bb3b866dfa9 | -11.6247 | -52.8624 | 2025-09-22 00:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 02ad6174-8495-33bb-b075-669d32a2e53a | -10.3945 | -46.0991 | 2025-09-22 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| c5e6814b-20c1-3e94-8dea-ec783ff61f1c | -20.274 | -55.4927 | 2025-09-22 00:30:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 8564c28a-b8ae-34af-b268-ed3fbab43664 | -5.5762 | -48.9934 | 2025-09-22 00:30:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b033e3e9-a61d-3a35-9d68-f69178597c96 | -11.6436 | -52.8605 | 2025-09-22 00:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 116.7 |
| bd28bdb8-1b37-3766-a693-c8a0e331fcb2 | -23.1872 | -52.0855 | 2025-09-22 00:30:00 | GOES-19 | PRESIDENTE CASTELO BRANCO | PARANÁ | Brasil | 4120408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 95.7 |
| 75455994-a38c-3226-9a7a-eaf543e5a7f4 | -19.6679 | -57.7243 | 2025-09-22 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.6 |
| 8cd555c5-6995-3ce2-8526-4550aaf43e7a | -19.6278 | -57.7296 | 2025-09-22 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 158.0 |
| 8975ebd6-4a05-377a-9a5d-bed75b3706a5 | -22.9262 | -48.1581 | 2025-09-22 00:30:00 | GOES-19 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 09577fe6-bb1c-3e84-9854-5e8c0ac0a1c1 | -21.8351 | -53.9546 | 2025-09-22 00:30:00 | GOES-19 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 08527744-b03e-39f8-8aff-f21fed58048f | -20.2533 | -55.5172 | 2025-09-22 00:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 56.2 |
| a5409af1-5105-3046-b403-a896bac83a7c | -20.2537 | -55.4959 | 2025-09-22 00:30:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 15552897-8ef3-36ce-a11a-67a4708a8d7c | -4.3197 | -48.0908 | 2025-09-22 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 7fd24dd6-bec8-37b1-89de-95a8fdde3793 | -19.6676 | -57.7451 | 2025-09-22 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.9 |
| 408a6c7b-5349-378a-94fb-15e9a3f6b1c2 | -22.9044 | -48.1873 | 2025-09-22 00:30:00 | GOES-19 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 118.0 |
| acfc2acf-aeb9-3d0a-85a2-c60ca865f202 | -19.6274 | -57.7504 | 2025-09-22 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.4 |
| aa2b2d30-a203-33d3-a249-47f7789c5548 | -11.3217 | -54.3564 | 2025-09-22 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 410ba102-6ffb-3728-88e6-a371e9f174d8 | -22.9255 | -48.1819 | 2025-09-22 00:30:00 | GOES-19 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 461efeac-a1cc-369f-9f17-7ea4afc64ff1 | -15.9969 | -59.4651 | 2025-09-22 00:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 6b1e4163-2afc-34cc-bbbd-8e720bd58f6c | -18.399 | -42.8644 | 2025-09-22 00:30:00 | GOES-19 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.9 |
| d28a14a2-1734-3c44-8bdf-b26418225bc4 | -20.2735 | -55.5141 | 2025-09-22 00:30:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 007baabb-d767-3957-aca5-f6af33db362f | -10.3375 | -46.1062 | 2025-09-22 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 1079e32e-d073-369c-a045-f5fed5f0ca7a | -4.457 | -46.9056 | 2025-09-22 00:30:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 5209b63f-0e02-3ec3-a842-c7158e739a5f | -10.3184 | -46.1085 | 2025-09-22 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 69e814ce-525f-3d85-90cc-4975195ff505 | -11.6249 | -52.8416 | 2025-09-22 00:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 451e048c-0fcb-34e8-a331-da11bd68cb7b | -4.3196 | -48.1125 | 2025-09-22 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c7cbf6f8-9b9b-356c-9a49-155dbf38643d | -22.9052 | -48.1636 | 2025-09-22 00:30:00 | GOES-19 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 76.5 |
| a65292ec-d498-34ea-864f-2f0b634cc468 | -19.6475 | -57.7478 | 2025-09-22 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.7 |
| c50f008e-0a5f-3ceb-abc4-d14f38cb01fb | -10.3572 | -46.0585 | 2025-09-22 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 176.3 |
| eed288e4-b2d8-31fd-ad97-2ce6e16f833d | -4.3012 | -48.0917 | 2025-09-22 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| e07e5279-86a7-36e3-ba91-5c2fe99fa8bb | -20.2537 | -55.4959 | 2025-09-22 00:40:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 5b8964c5-2fa3-3b56-aa49-e4af1b2a34bc | -11.6247 | -52.8624 | 2025-09-22 00:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| dcd87f66-270e-300e-9ea2-880f42f20590 | -11.6249 | -52.8416 | 2025-09-22 00:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| dbd9dbf3-0b72-3d7b-9a2a-d56ad487040c | -21.8351 | -53.9546 | 2025-09-22 00:40:00 | GOES-19 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 65b56026-f084-3cd0-a6f3-a8d5d15c9f4c | -11.322 | -54.3359 | 2025-09-22 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 127af55e-65cc-31b6-a25a-75e21da935ad | -4.3197 | -48.0908 | 2025-09-22 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 162.7 |
| 06c6a5a1-27ba-38a3-a43a-d210d307cdcf | -19.6478 | -57.727 | 2025-09-22 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.5 |
| d9b9569f-6ca1-3394-9b11-b0ffbaf07dbb | -22.9044 | -48.1873 | 2025-09-22 00:40:00 | GOES-19 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 109.5 |
| f6e6e43e-1bd6-381e-a907-e15d54d22fba | -11.6436 | -52.8605 | 2025-09-22 00:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 052b57ec-aa69-397f-befb-68ee611c6615 | -10.3378 | -46.0835 | 2025-09-22 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 859e443f-3cd8-3c91-ada2-b523fb86d7e0 | -19.6679 | -57.7243 | 2025-09-22 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| 19dd78db-f51c-3487-9db9-754f60ff792b | -10.3759 | -46.0788 | 2025-09-22 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 168.0 |
| fed7c123-2e46-3713-baee-3697ad1d3520 | -5.5762 | -48.9934 | 2025-09-22 00:40:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| bb488171-3460-3162-9dca-f57b0fa05172 | -20.274 | -55.4927 | 2025-09-22 00:40:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 77.2 |


[Clique aqui para ver as próximas entradas](README5.md)
