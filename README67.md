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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee9173dc-ebc3-36a8-ba4a-5666df3cbc47 | -11.43074 | -45.41418 | 2026-09-20 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8994b44a-ee57-3b5e-90d1-7fa68bb41047 | -8.75907 | -48.65731 | 2026-09-20 04:40:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a944dacb-37b5-3bae-b7e3-48a87b281740 | -10.40512 | -48.92245 | 2026-09-20 04:40:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53554b47-46cd-3556-9dee-95daed19a431 | -9.37041 | -48.2907 | 2026-09-20 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 961d9d28-4fe0-34ed-b1c4-19e460ef30a5 | -8.1414 | -46.80514 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e0c7e75-4342-3d03-922a-a24d64535431 | -10.31849 | -50.22294 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8edd529e-a78f-3a2b-ac23-01c35f7059d9 | -5.83656 | -53.52479 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a2c3fc3-a260-36d6-a4b6-d85dfca17022 | -6.65608 | -50.9313 | 2026-09-20 04:40:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83361823-04d0-3ac4-8dee-11a598d5fc97 | -9.2766 | -48.24002 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d25d3ce-7de0-355e-926d-0c129298aa19 | -7.63635 | -45.82199 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea631cbd-66b6-34a0-bd3e-7b98495c259d | -9.03623 | -49.83691 | 2026-09-20 04:40:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| de354a33-6d7a-3159-ba8f-d7ae37fb5e17 | -8.05837 | -46.27395 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f141b54-e48e-31a9-9ed2-7e6b1080bb3e | -9.01894 | -44.91633 | 2026-09-20 04:40:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c402dcb-5e20-36f1-ac17-ef182320d3c4 | -9.26111 | -48.20884 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 992a83b3-8f85-3844-b64a-400ce4e98cff | -9.26442 | -48.20938 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1b1706f-67c5-3e88-9dd1-6d3eb01d5cd5 | -11.86567 | -47.65065 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76c8e5c7-f010-372a-85c9-80401234dc2c | -13.01748 | -46.91746 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d0da4d4-d4ef-366b-8427-edde0e735872 | -7.54711 | -45.38576 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 766b1f31-464e-31d1-bf9f-e1b1ccdce63a | -13.45428 | -51.9143 | 2026-09-20 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98573bf6-8274-32b2-8d63-586dd155d9f0 | -8.88651 | -45.91746 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ce71377-a1b0-3411-8ad7-8a4713eac9e6 | -7.39394 | -47.77371 | 2026-09-20 04:40:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b55257b-684e-3902-ad44-395e0fa3ff93 | -6.13066 | -59.94316 | 2026-09-20 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2749edd3-b9ba-3e57-a790-addc158861a9 | -9.80101 | -48.31617 | 2026-09-20 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69aef710-87d1-3a20-bee0-96299bc663c9 | -9.26829 | -48.2064 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2cf9a75f-94d0-344d-b6c2-d653c3342f80 | -11.85946 | -47.66854 | 2026-09-20 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e9de2345-5015-304b-8c09-c63de31cdf06 | -11.88488 | -48.992 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82ed7943-0c84-30b0-8135-6348f6795aa6 | -8.87398 | -45.95228 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db7804bc-f2bf-35ac-b117-60e90690ee94 | -10.29219 | -50.20404 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0cd691ef-0972-3fc0-b223-9469dba91a84 | -11.02904 | -54.15681 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afc2994f-739a-34c1-b20d-d4db5945c023 | -7.01137 | -45.24738 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f33099a9-b642-3612-b4bd-ac683be34eca | -9.23486 | -45.90974 | 2026-09-20 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 808aba38-ff6f-3d18-8a40-fa06b941e44a | -11.87879 | -49.00907 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d82befe-55a9-3ee0-b6f4-116b3bf19fd4 | -12.54206 | -47.08198 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e881cc43-adfb-3ed1-bfc9-f6af75280184 | -13.60059 | -46.92996 | 2026-09-20 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a81c62e-952a-3f54-a7f8-a5775b71636f | -11.08162 | -48.31026 | 2026-09-20 04:40:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac08bdec-3dde-39c5-bdf8-ae3622d8a56b | -11.73755 | -54.55223 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a49d2a1a-f858-3782-9515-1a008db570c4 | -12.13694 | -47.03511 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bc6145fc-1845-3219-9178-3028e83d157d | -10.41699 | -48.32762 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 157d57a2-7b40-37d5-b25c-b1963809631f | -8.17152 | -54.75993 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f7ba638-77b4-3b5f-83a6-b4ac4436a179 | -8.65766 | -45.43877 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcb4add1-a6c7-3103-8aba-af0472fc6c00 | -8.6661 | -45.43149 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61e8f116-e06b-351d-bbfb-85b713db8e39 | -5.74299 | -57.60595 | 2026-09-20 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b76efdbe-c2a0-3836-9dfa-9c580da421bd | -5.8427 | -53.51404 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05a96c10-63d7-36fc-8032-cf8a67411c96 | -7.40765 | -49.84384 | 2026-09-20 04:40:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aff79e5c-b98d-3692-82d5-502fade488a9 | -6.80479 | -47.82644 | 2026-09-20 04:40:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f1c89e3-bc8c-3883-b732-806f3af2767a | -11.74061 | -54.5608 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7029c84-f173-3f06-a5e2-7a83923bec08 | -7.52839 | -45.43682 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7f5a8f9b-b631-3790-a864-2bf7d32603b8 | -12.88579 | -52.08139 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8acf30b5-9238-3026-bcb8-d1182ccdec1a | -11.87397 | -50.04196 | 2026-09-20 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81fe7088-66e8-3964-902c-d14d5bfc8168 | -9.85789 | -48.34331 | 2026-09-20 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b921dbd4-0aae-3bde-801e-7d8f7c9e948e | -12.56982 | -47.08697 | 2026-09-20 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01b167d5-0f9d-3fca-bf42-92e5e9a862dc | -6.39119 | -55.24975 | 2026-09-20 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83f15669-7f53-303f-ae2b-7caa702d2681 | -7.0179 | -45.25249 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 53f78df2-9f1c-3a6f-9d6f-0f56ff230e45 | -8.17085 | -54.73794 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e0aa76af-ff26-372d-ac0a-96dcf8f1311e | -5.84008 | -53.52934 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 033e0a71-a6f1-32b3-9943-eeb7824fac6a | -8.65345 | -45.44233 | 2026-09-20 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a602b4fe-c84f-3d9a-81c6-cf98e033dc2d | -13.30717 | -51.76746 | 2026-09-20 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8655f04b-9a0b-3d9a-b9cc-1a01f24863a4 | -7.63577 | -45.82587 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebd69894-840e-3bfd-b8dd-e4f972d391a0 | -11.93962 | -55.9221 | 2026-09-20 04:40:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dea2d06-bf47-3cd6-ba83-412c69ab6990 | -13.22742 | -46.93818 | 2026-09-20 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7a0281b-d9b0-3925-965f-10a13888ee9e | -11.04315 | -54.17813 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4131c12-aa29-3629-9bb3-105629925763 | -13.62946 | -48.29302 | 2026-09-20 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60313dc1-5f04-37f7-9365-3c1b26cd9279 | -10.58259 | -46.53395 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbba7f36-d713-3237-acec-a6a4699beb7c | -10.27674 | -50.25707 | 2026-09-20 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8100f3d8-ae05-3a39-a0dc-1cf37b80700d | -7.01682 | -45.23563 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7e23c6ff-8f39-3221-9bef-053635f7da51 | -13.88995 | -48.58162 | 2026-09-20 04:40:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b85facd8-2fb9-3f6f-b8cc-1acc664ff1ff | -5.85039 | -53.51929 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aef65314-515d-30ca-ac21-31720bb728d2 | -7.62604 | -46.1244 | 2026-09-20 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5164676a-8a47-3e4a-8a44-9187a72c2c3e | -12.13636 | -47.039 | 2026-09-20 04:40:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 04811f6b-989d-31bf-85d1-fff26759ab54 | -11.39438 | -51.38663 | 2026-09-20 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eea72fd7-e26c-3667-8839-8b483df5072c | -10.48485 | -46.29253 | 2026-09-20 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8cfc121-ac92-3c50-abd0-6d3fe8bb95d3 | -12.77366 | -52.85624 | 2026-09-20 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e34ca579-d1dc-316d-9b5c-8c864bad823c | -8.62753 | -47.61559 | 2026-09-20 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dec2a942-c129-35ca-a1ea-ba013951abed | -10.69538 | -54.17797 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9a18b34-a413-3af8-80da-e9a9bac16c42 | -5.84817 | -53.50719 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 617e6807-d686-3f12-ba4b-d8d9c990c545 | -12.52773 | -50.03362 | 2026-09-20 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ccdd2271-90f7-3142-af6b-dd28b33e4d78 | -8.47859 | -44.52185 | 2026-09-20 04:40:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da308145-f86b-30c2-88e1-3fe50b53ee94 | -12.32253 | -50.71347 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd298d3c-9805-3887-9ad3-110324071029 | -9.26552 | -48.20237 | 2026-09-20 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b61228dd-d487-3e5f-8f75-de95d95b3ee2 | -8.1752 | -54.73874 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2937765b-6880-3762-8f9e-4e320cb8f2bb | -11.03848 | -48.28506 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0122b52-16ef-306e-9e33-42642caabd00 | -11.29047 | -54.04319 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66c2e832-824f-3a9a-a615-0416e4834ad8 | -11.00349 | -48.31231 | 2026-09-20 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca72bac8-0e58-3a14-972e-e364e0160827 | -6.46716 | -48.43563 | 2026-09-20 04:40:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2872f8a1-368f-30c8-ba97-4e89ff79c495 | -10.87966 | -53.98955 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e82c670-c6c9-3b2c-b6b1-3343ff58c3fe | -8.1451 | -54.80788 | 2026-09-20 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59a5bf56-19d0-3e01-aca2-35e6584828d8 | -7.55748 | -45.43718 | 2026-09-20 04:40:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b9c7c4a-0735-300a-975f-7d2fb9c7fa34 | -12.53323 | -50.04181 | 2026-09-20 04:40:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 523dbad2-8721-3bb3-8405-4de8852ef20f | -13.62609 | -48.29243 | 2026-09-20 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 542ca12d-58e7-35a3-b213-a89ca2f78503 | -11.27961 | -54.11874 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3cd52a58-5d6c-3fd6-9f84-1d07492bf727 | -11.75181 | -54.5662 | 2026-09-20 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24086c5b-7b1c-3e2c-9444-0b851a689842 | -12.69295 | -50.75997 | 2026-09-20 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 167c5ee3-7536-3090-96be-0698543a9998 | -8.29208 | -46.86913 | 2026-09-20 04:40:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01ef2ac7-1bf4-3c14-b799-319df1effbaf | -11.87824 | -49.01259 | 2026-09-20 04:40:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab171b6e-bbf7-3051-b2b2-3a3721bb231e | -11.04564 | -54.15631 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 497f856a-025c-347f-b2e2-0bce810b8a12 | -11.32345 | -47.28256 | 2026-09-20 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fe1e4b9-5bfa-3003-a889-07a1ba38157a | -11.97707 | -44.99263 | 2026-09-20 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3faf627e-12e0-3315-9692-59bb14612c61 | -9.35404 | -50.1134 | 2026-09-20 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b96b7c05-081c-32bb-8aba-a6365dbdaafd | -10.9266 | -53.95519 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cf356a6a-1588-3ab1-8e53-6c6f729f8d38 | -11.13799 | -54.01344 | 2026-09-20 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README68.md)
