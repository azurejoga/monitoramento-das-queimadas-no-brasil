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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7cc7bd0-00ae-311f-8637-a97fce12a8f8 | -6.56486 | -55.40796 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a762dfb-e8b7-3715-940b-c7631fbe4a2f | -5.41403 | -49.26977 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f3f8b4a-974c-3c39-9ace-a2682e90a9b8 | -11.12138 | -48.31469 | 2026-09-23 05:04:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7f497b1d-4eca-395d-8b02-d5f8597747c8 | -6.63401 | -59.92737 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| d8bbe96e-e23c-39ff-a777-15e76fc183e1 | -6.61917 | -59.92324 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 7c26fcd4-6edf-35d3-85ba-477644b8c05b | -5.86826 | -51.93942 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8ee9b28-a948-36cc-b6ce-1f3d9816389b | -6.37934 | -42.78461 | 2026-09-23 05:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dff17194-e0ae-32f6-b6cd-e80d4280c77b | -11.63565 | -50.97582 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38292081-ba5c-3e70-8c4a-76ceb2fd09a0 | -9.83791 | -46.38274 | 2026-09-23 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f2ae823-c511-32d5-a72b-a15bef73892e | -7.87913 | -61.17637 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b5b47946-f9c2-33a2-a1a4-67ccb6aa5e2a | -8.80332 | -44.27029 | 2026-09-23 05:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 93b5a067-089e-3d25-9d92-e52148d1fa59 | -6.13857 | -43.8421 | 2026-09-23 05:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbcd4207-d934-3416-abf8-b1c12f5f5f5b | -8.37352 | -45.59127 | 2026-09-23 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a010bd6-5b86-3dcc-ba67-64e708c6a3a7 | -6.12721 | -52.76015 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dd3205b-50f2-326e-bd37-50e9556d9b28 | -5.61941 | -45.23949 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 240ca3ab-15e6-3a31-8cac-a833a20719eb | -6.13769 | -43.84846 | 2026-09-23 05:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b1674541-b0b7-34eb-8dbb-065e3af44985 | -11.01135 | -54.14912 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 75ed86fe-fe29-3fac-9b37-4069dbd12e8a | -6.12344 | -57.75817 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c1081a98-265b-33f7-a202-7830c724846c | -9.26228 | -65.44141 | 2026-09-23 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dd21b15-4ecb-344d-9c5f-1b1504dfd5f4 | -11.35476 | -43.3836 | 2026-09-23 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a79afe8e-f9ac-3483-b336-28ebe293a756 | -5.98005 | -55.37206 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c64f8481-1197-3047-bf13-72c7c5605b25 | -8.33686 | -50.87192 | 2026-09-23 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 596d1ea4-e81f-3a3a-8c10-439db634d530 | -9.10787 | -51.55498 | 2026-09-23 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fe1acb3b-9199-3076-8e8b-530498122a00 | -8.7406 | -52.36566 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60519b04-e396-315d-bd92-75f734736777 | -8.27824 | -54.7608 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c200d1f3-fa80-3ab1-bc81-6dcaab385e21 | -10.26421 | -49.97238 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9d0f5152-de77-3c23-b66d-77d0ec2afe48 | -6.06506 | -57.80469 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da747193-cacd-3b53-8cea-f7d6cf3eeef8 | -7.56761 | -57.67651 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 698f6d9d-b190-303c-9ca7-130802c0b6f0 | -6.67154 | -47.44348 | 2026-09-23 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8148e370-b4d5-31f3-bfff-c0eabb907a36 | -4.55593 | -54.93891 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 272aa8df-70b3-3f08-87e5-a60e097ccea3 | -8.80815 | -44.27424 | 2026-09-23 05:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4b5aeefb-c7ad-36cf-b2eb-1a970d7a6b74 | -6.57473 | -44.15075 | 2026-09-23 05:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 32fa8df2-b8f3-3b70-adf8-6551fe1a3a13 | -10.87679 | -54.09815 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcf8d00b-b6c5-3841-87cf-bf057ccde103 | -6.61823 | -43.72882 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1bf47101-1682-3852-9061-294058fa5bea | -10.29726 | -50.49858 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b141ecf1-c03d-3104-9ab5-a116ec53b9b7 | -4.56304 | -54.94007 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3c09fe2a-94b0-35f8-b050-4958d9dbae5b | -4.54196 | -54.94181 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a17b992-9bad-3e1a-8574-7b2b0b46e58a | -6.58029 | -44.14849 | 2026-09-23 05:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7d092adc-e1e0-3cd3-af43-0d1b8fb0372d | -10.04962 | -50.21545 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c47d5da5-962f-348c-a405-32ec8326b23f | -3.60808 | -60.57994 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cba82cc-9618-3e90-90b3-98af7cf1aee1 | -3.30166 | -57.86095 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a082a15-7f21-30b6-9578-5fe59ceee5a4 | -8.83301 | -50.49208 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ae842d40-6dc2-3aaa-afc8-10c3d1afa4a4 | -6.61247 | -43.73141 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| b9aa7487-22e5-34a1-bb18-597cd422ae59 | -8.20243 | -54.71093 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31047868-d24a-3698-a488-3f9d37f43d21 | -3.82589 | -59.33545 | 2026-09-23 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5f758175-b31d-3961-b17f-b3a006534c66 | -9.71345 | -48.33816 | 2026-09-23 05:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7372488-ea01-3632-8c4d-b879bddef048 | -6.37144 | -55.26756 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9aaf9dd8-0bf1-3197-bff4-0a35699f4e70 | -3.6927 | -60.55038 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db48ecb5-68bf-3ec6-970f-32405f9002b4 | -11.77961 | -50.99137 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 042d2877-c521-3ec6-9061-73c335d30e18 | -6.11102 | -44.1522 | 2026-09-23 05:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96793f9e-1333-3d77-82a9-2ae0db2b44a8 | -6.61363 | -59.92736 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 1c772968-191b-300f-a5a7-d8714dc1d5f0 | -4.34011 | -55.65871 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c36fce1-0aeb-3b37-a033-e62395de31ea | -9.58823 | -46.53379 | 2026-09-23 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f072a4b9-3807-35ef-86ce-51563a1785c4 | -6.42458 | -59.975 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94882fe7-54fa-3faa-a011-38ba3a9e25fa | -7.16541 | -45.81079 | 2026-09-23 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ffcbe3b1-aade-37f0-8b18-5919dde61df6 | -11.64599 | -50.93129 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f9ea86b0-7dc7-3847-a0be-96fb8d46215d | -3.89563 | -60.58755 | 2026-09-23 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a63ee82-7aef-3007-b7ec-f14f87ddd70e | -8.45939 | -51.48644 | 2026-09-23 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82e03c47-6282-3968-b51e-13e74c3241ae | -6.42369 | -59.98002 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6d46ef40-0bf6-3770-abc2-c10fcb6b1878 | -6.30452 | -56.03971 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8cc3acf-d2a3-3a41-93ce-28c74b4f3fab | -6.85924 | -57.65537 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b054ba4b-0dc8-30b4-9823-edb5f1fc47a6 | -6.383 | -55.28587 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6cedfc6-fdd8-36ba-b0c9-a87abe36869e | -10.04127 | -50.22025 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 174a8dc9-d125-3786-8630-04014c83690f | -8.92806 | -61.47861 | 2026-09-23 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 873a15b2-3cf1-3d62-ad8d-3163780db81f | -10.2716 | -49.9735 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c06bed57-8d7c-3c22-bd94-e807e7be2307 | -5.41248 | -60.21813 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b38c6eb5-7a4c-3acc-ba03-7ce9eac8163e | -9.56465 | -46.53627 | 2026-09-23 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a748d5a8-6c40-3c6b-a2c9-56e460e10840 | -12.20872 | -47.28708 | 2026-09-23 05:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28689c37-ef7d-3fe4-a2c4-c91b6e870daa | -5.62084 | -43.35799 | 2026-09-23 05:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fed62e51-3f82-3343-9ada-d3a7f7c808c5 | -11.68235 | -43.44863 | 2026-09-23 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cb06171-0724-3153-9bd2-910ba5ae3982 | -7.49511 | -44.32762 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9ec8502-a684-3f6b-bdfc-f231a77185d9 | -7.09908 | -52.75462 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5846e2d8-f916-3037-810a-ab14abd8f8ac | -10.2666 | -49.9817 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d0161253-8d36-3b61-a9cc-b1f5776e5b74 | -10.30086 | -50.49913 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f26b7b0b-1375-3c49-978f-3b37f480e978 | -6.61832 | -59.92825 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| a5eb8b05-eb58-3bb5-8342-baa5f7ec15c2 | -3.45998 | -58.39848 | 2026-09-23 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff2d953b-7a56-35b0-941a-3b760f5d1741 | -8.94546 | -50.9146 | 2026-09-23 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7990129c-6cd2-3029-a919-0a9ccf60c257 | -7.09576 | -52.75409 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f61c3076-a223-349b-b1c6-69b7920aff07 | -7.04381 | -62.94043 | 2026-09-23 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54f4ee4e-8143-34e3-b3e6-1017368457d5 | -8.25408 | -54.77963 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f4558b27-3de8-3c79-886d-6a1faa92ad8f | -3.66919 | -57.09426 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41c12500-c4b3-3292-a481-a7a7a605da46 | -6.66659 | -50.94827 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57dad676-5ebf-36b9-ac00-f5e01d2a0548 | -6.45848 | -54.99985 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6816238-5cdd-31ac-80a8-5f2af7bb1a96 | -9.93867 | -48.46769 | 2026-09-23 05:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 120e4381-9f38-32b3-8c83-b4d06a03c9b9 | -4.53683 | -54.9739 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37a8649c-eecc-3e20-a197-0edeebd1440b | -3.72662 | -60.57519 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4839662-04c8-3fdb-98f6-f28b0268add5 | -5.76573 | -45.11181 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 84b1f86c-ca1d-3ee9-a38b-fecaa01777a6 | -7.55645 | -55.01464 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 460ab37a-f4cd-38b5-a331-86fce737e60d | -6.1323 | -51.7042 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ba8c71d-a312-301f-9457-9e561777772c | -11.94991 | -50.07814 | 2026-09-23 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 320ece6a-46ad-35c6-996f-3058eee6ae51 | -3.15126 | -57.68884 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8dee9935-8e22-3562-b494-8b74684f9fb9 | -11.63872 | -50.95535 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 707a02e8-c580-3e0c-8624-ffa815a73879 | -11.1054 | -48.33868 | 2026-09-23 05:04:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b8a37b49-a7b6-3103-9b6d-99fa3c2a82b3 | -11.7862 | -50.97139 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be96bbca-6c0f-3da5-98ea-27f8bbb5fa99 | -6.81545 | -59.43235 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ca32ec8-6215-32ee-b1ac-468fb1fa19aa | -6.60537 | -43.74371 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7beb625e-9644-3492-8743-82439a16830a | -4.51323 | -59.81059 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 159f7873-6aba-339f-af3c-7c3dad065b27 | -6.1381 | -43.84548 | 2026-09-23 05:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1b868637-f6bb-3861-8aae-0dae4d0da855 | -5.89336 | -52.10034 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 163bab6e-2a9b-3ccd-8dab-94915fbefa2f | -4.06923 | -56.22638 | 2026-09-23 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README94.md)
