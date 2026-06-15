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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6a57983-69b9-324c-b6bf-ca9e28836156 | -14.37292 | -45.54343 | 2026-06-15 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a3a3565-c758-39fa-8462-35e60b8103c8 | -12.73174 | -46.28962 | 2026-06-15 04:38:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c318003b-c45b-329a-a9f0-3dfd20df73d5 | -11.06233 | -52.45229 | 2026-06-15 04:38:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cb05e7f-9fec-3b66-ae2f-05a6391dc84c | -12.73118 | -46.2933 | 2026-06-15 04:38:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb67878f-9649-3f1c-be22-f1bf4bcb26b7 | -11.82761 | -51.62094 | 2026-06-15 04:38:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d892869d-b8bf-356b-9ce7-7d0919dd78c8 | -11.34301 | -51.40088 | 2026-06-15 04:38:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ac994ab-6e22-36cd-a88b-4f6581dd03da | -11.26744 | -53.95808 | 2026-06-15 04:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aed1392e-ae75-33e5-ada3-2b4abe6b7b8d | -12.44749 | -44.74787 | 2026-06-15 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e280767-0434-397b-9611-5ed88a5978d5 | -11.02649 | -44.69455 | 2026-06-15 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1c614fd0-d9ab-3864-a072-010d3e367374 | -13.81303 | -43.65346 | 2026-06-15 04:38:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 50607ac7-558e-305e-93af-ac6a9017a02e | -13.80912 | -43.65288 | 2026-06-15 04:38:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 89abd003-16d5-368e-b055-56c251db1b6a | -10.80424 | -54.17348 | 2026-06-15 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc9e64c0-0ba7-3409-8c94-52e7e62d281a | -13.54658 | -47.85102 | 2026-06-15 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1928d489-7833-3055-9339-ce570b9c1576 | -8.43477 | -54.72861 | 2026-06-15 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85093e95-603d-3b5e-b7fb-46aa3322e3ff | -12.71533 | -54.2053 | 2026-06-15 04:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 010416cd-76a7-3ee5-b951-01d4f9d59be3 | -8.43487 | -51.54994 | 2026-06-15 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf91face-a999-3a35-ad0b-9c56f1d56ed5 | -10.15109 | -56.60674 | 2026-06-15 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d699c636-914e-33a1-8277-487ea3965720 | -10.7685 | -54.10399 | 2026-06-15 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ee8e119-de35-312c-88bf-0bdee7338e8e | -10.28823 | -47.60059 | 2026-06-15 04:38:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bf8fbd7-e76a-39c2-a652-38fcbd0d1834 | -10.80343 | -54.17797 | 2026-06-15 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| baaaa5e5-84e3-3955-b046-b723724ad58b | -10.15173 | -56.60333 | 2026-06-15 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 45b87475-9e35-397c-a446-189757ef53f0 | -11.82386 | -51.62023 | 2026-06-15 04:38:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bafa646-fea8-33e4-b43b-f8346ec5db51 | -11.06631 | -52.45304 | 2026-06-15 04:38:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 52491137-006b-3a62-93f5-c21cde0efd6a | -12.73458 | -46.29387 | 2026-06-15 04:38:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8294a636-eca4-39b0-8748-8cf4859229af | -10.15705 | -56.60442 | 2026-06-15 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 75214b2f-7f11-3228-a911-510270595fff | -12.71968 | -54.20609 | 2026-06-15 04:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a387f7c-4d98-3771-a1f8-7d74d88aa394 | -10.83543 | -53.72657 | 2026-06-15 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e79d041-a823-3f70-9f42-5470fa111b96 | -10.586 | -48.37811 | 2026-06-15 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e52ab92-4e44-3382-810b-1d74228d6cae | -10.40576 | -49.44234 | 2026-06-15 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbe8f1d5-cb1c-3b60-8de7-cbfda22ac025 | -9.26815 | -50.66197 | 2026-06-15 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 12631a22-d6e3-3169-81a5-15e7015cf64c | -10.79976 | -54.17269 | 2026-06-15 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bc3c87e-7f61-39a2-abdb-9ddce3aadae2 | -10.40755 | -49.44171 | 2026-06-15 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| baaaca4e-f3a4-34c0-9761-4f0d9731c6ca | -14.04498 | -47.04889 | 2026-06-15 04:38:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c8a37fd-7e3d-3e12-9e3b-ca51b181b8d2 | -10.15641 | -56.60781 | 2026-06-15 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1cb8f608-12c7-3be3-8d25-af4c974e233c | -10.77218 | -54.10925 | 2026-06-15 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9f157d1-38e0-3ef0-a74e-7438610f3983 | -10.90087 | -54.13495 | 2026-06-15 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 226c02f9-72f6-3d66-826d-e26ba96a760b | -8.43577 | -51.54802 | 2026-06-15 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 276e3f0a-b323-373c-8461-dd0950c0b857 | -13.50941 | -47.84853 | 2026-06-15 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13c86b99-6dc8-3580-a70f-013791d83fd8 | -10.51378 | -50.40453 | 2026-06-15 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9146f754-d832-3657-a2a7-badb67ebebcb | -13.50608 | -47.84797 | 2026-06-15 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 893dfe7b-b6e4-3027-8eb4-99c8db5923a9 | -8.96418 | -46.9102 | 2026-06-15 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e1e2718-92e1-39e7-a5a2-519fdb68fae6 | -8.98498 | -48.09568 | 2026-06-15 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7d7e200-d0c2-374a-89d0-6423bfd101d3 | -10.41825 | -44.95947 | 2026-06-15 04:38:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 851c5879-97ff-3780-9d73-6627d8acf27a | -13.54325 | -47.85049 | 2026-06-15 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9e32f3ce-3e7e-3612-babe-b83f22a3f00e | -13.50997 | -47.84497 | 2026-06-15 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f3ac6cf-68ff-3fd6-b5fb-81c20389ebcc | -8.88385 | -48.50799 | 2026-06-15 04:38:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 880ccb38-a1b6-3f75-8853-ece02562aaad | -8.9675 | -46.91073 | 2026-06-15 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ae8cd74-7edd-3030-942d-3ee56edd7812 | -11.09105 | -45.29345 | 2026-06-15 04:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45b9f9cb-3794-37d9-bad3-7be67ec0465f | -10.15832 | -56.59768 | 2026-06-15 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3bb6a6c5-2da1-39e8-b0df-48a0b27287e5 | -10.83754 | -53.74003 | 2026-06-15 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83dd103b-94b1-3147-800c-5758aac2535e | -11.26666 | -53.96238 | 2026-06-15 04:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d32d9d1c-b3b6-3d07-bb51-635263f4a19d | -11.02354 | -44.68989 | 2026-06-15 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38f2ba72-70c5-3478-8ead-7467568cb903 | -10.15768 | -56.60106 | 2026-06-15 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7ee85e4d-1c39-3079-a58a-0f79876af44d | -13.22662 | -41.97432 | 2026-06-15 04:38:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d10cdc73-2ebd-30ff-bf55-51d58a81656b | -11.02711 | -44.69046 | 2026-06-15 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c1371a57-cc09-348d-af63-85ea60661bbd | -14.36936 | -45.54287 | 2026-06-15 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17559619-765c-3c4d-bb07-f89e05da43b9 | -12.71518 | -54.20268 | 2026-06-15 04:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| feffeec4-6e66-3916-b523-60bfd5f49b53 | -10.77297 | -54.10477 | 2026-06-15 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0a9f717-7fb3-361d-8133-2ba8cff5b6ee | -11.03068 | -44.69102 | 2026-06-15 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f7615879-3384-36ce-903c-bdf7c9f88720 | -13.76757 | -42.69278 | 2026-06-15 04:38:00 | NPP-375D | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 54adcf85-26c7-3ace-ae86-facabb2d8269 | -12.71084 | -54.20185 | 2026-06-15 04:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0961f2c5-488c-3605-8737-0b7c0a8ff6e1 | -10.29156 | -47.60113 | 2026-06-15 04:38:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee8ea431-647b-33fc-9058-e56d5756ebb5 | -8.88724 | -48.50855 | 2026-06-15 04:38:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fdf8627-25c5-3bd6-b1e6-63de1739cc51 | -13.20263 | -53.26287 | 2026-06-15 04:38:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a3610aa-1761-37ba-9aec-72dba6dcdff6 | -8.98556 | -48.09211 | 2026-06-15 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| be4281d7-83c1-3c8d-b415-20c1b97a28c9 | -11.7316 | -49.0442 | 2026-06-15 04:38:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f41094ca-794c-32b5-9c48-49797dd45c77 | -12.71878 | -54.20768 | 2026-06-15 04:38:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6411b2b4-b01a-396a-9647-da60b056a8a4 | -11.5097 | -56.12957 | 2026-06-15 04:38:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63980f76-eeef-3ffa-87f6-54a0027aab37 | -13.50552 | -47.85153 | 2026-06-15 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d328dd8-eb8d-38b7-bd41-2459106f017c | -11.03006 | -44.69511 | 2026-06-15 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7c467648-b906-3ecb-83cd-c104b252149d | -10.83469 | -53.73078 | 2026-06-15 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b7caf4c-87ce-3231-a679-d42f90d899ee | -10.57107 | -57.31732 | 2026-06-15 04:38:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77e7e8c5-7bb8-3670-8330-52cabfc85d53 | -9.77696 | -48.9692 | 2026-06-15 04:38:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48cf8ae3-06b5-34be-b078-b9f2bc4f1abe | -10.83034 | -53.72997 | 2026-06-15 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8bdbe5c-40e2-3656-95c7-26969acc029e | -11.19692 | -49.68438 | 2026-06-15 04:38:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 259cb89c-dbbd-30c1-996a-96427636e902 | -11.71957 | -54.49081 | 2026-06-15 04:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67f49955-8646-37ae-b6aa-731bd71767b7 | -8.96806 | -46.90724 | 2026-06-15 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b2d8785-0547-3d05-b7e9-dd73725dba60 | -9.695 | -47.69905 | 2026-06-15 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f4f55d9-6ea4-3b63-89ec-e79e9f1f9beb | -10.90629 | -49.49627 | 2026-06-15 04:38:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e33ae12-f24b-30d5-859c-a186b385a4a9 | -10.8332 | -53.73917 | 2026-06-15 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed541878-1951-3859-bff0-d7c5042ffd61 | -10.15237 | -56.59999 | 2026-06-15 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6b6787b8-6ebf-343f-9201-47c1db9e2aa1 | -3.51224 | -48.036 | 2026-06-15 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0895248e-26ce-3b18-90b0-5879437f4493 | -4.70991 | -48.30354 | 2026-06-15 04:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b9da03e-adec-374e-a2d4-d554bd49eca6 | -3.58451 | -50.26376 | 2026-06-15 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a392efd5-0c94-37f2-b210-89d997a6e574 | -5.28949 | -43.95567 | 2026-06-15 04:53:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4396ac02-7a1a-3501-9254-c49208d04420 | -3.50475 | -48.03686 | 2026-06-15 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 857d86aa-354f-3a67-8172-33464daac59f | -5.5449 | -47.57608 | 2026-06-15 04:53:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 026c48ef-55a2-3761-98e1-0a8752c21805 | -5.93973 | -43.65463 | 2026-06-15 04:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff1851d5-16c5-315b-9f53-5809b9afc147 | -3.51298 | -48.03349 | 2026-06-15 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 923a362c-e54f-321c-93f6-08b287b0a01e | -3.51297 | -48.03139 | 2026-06-15 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03b2e0a3-e00a-37e1-b89a-c561418bed0e | -5.93447 | -43.6539 | 2026-06-15 04:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1700e68-160a-3d4f-9dd2-4fe0c2429d43 | -3.49647 | -48.03809 | 2026-06-15 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f26c628a-42d4-3f94-b4ee-38e7f51684a3 | -3.50848 | -48.03538 | 2026-06-15 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 758cac6a-d780-3e6d-ba50-0aa7f493c284 | -5.93928 | -43.65778 | 2026-06-15 04:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba2e6a36-2cea-3776-a5b6-25c55f1c0405 | -3.50921 | -48.03077 | 2026-06-15 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75eb2920-d240-33ef-bcbf-fe45d15c4001 | -3.50922 | -48.03286 | 2026-06-15 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ff0e4df6-2893-3352-b5a1-5afa3fab45be | -5.28904 | -43.95869 | 2026-06-15 04:53:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66320982-5db8-3368-b663-b3d2fb7dbe1a | -5.93494 | -43.65064 | 2026-06-15 04:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5029c5fc-bae1-358e-a21d-3a6260033b67 | -3.504 | -48.03931 | 2026-06-15 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0669b4a5-42e1-30f5-abe5-f9311c4c136d | -13.80955 | -43.65627 | 2026-06-15 04:55:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README4.md)
