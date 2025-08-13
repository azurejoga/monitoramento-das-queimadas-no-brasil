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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b945b14-9b1f-35d9-8260-95fa710f3501 | -9.1894 | -59.6558 | 2025-08-13 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 420581fb-63ce-33a1-8d93-92445f2958ab | -20.8549 | -49.0745 | 2025-08-13 03:10:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.2 |
| 79ade166-ee9c-3b5c-88f8-fccf7b909314 | -16.3153 | -52.9201 | 2025-08-13 03:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 68afe16c-3ad8-3847-a457-e16a73f2a391 | -18.5297 | -46.0651 | 2025-08-13 03:10:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 33e15fe3-4744-39b0-bf4c-0e3af1baa52e | -7.1299 | -60.1182 | 2025-08-13 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| ee179bdd-26cd-31ab-8d50-0d4b9aed1f34 | -7.1298 | -60.1374 | 2025-08-13 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| b7ca2a48-5f46-3d94-a66c-16471c31ddeb | -7.0935 | -60.0237 | 2025-08-13 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| b559c17e-ccd0-3142-9773-223d374825a5 | -18.5499 | -46.0606 | 2025-08-13 03:20:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 9fb2f522-fc73-3963-963e-4f2e07fb1d18 | -7.1298 | -60.1374 | 2025-08-13 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| d0d9d742-9802-3ff0-bc3a-0e8685752fe4 | -18.5505 | -46.0369 | 2025-08-13 03:20:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 58.8 |
| e9018946-48e1-3fea-812a-cb58739d5dbd | -7.1299 | -60.1182 | 2025-08-13 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| e69130e0-6a03-3ca9-9866-1f72d263379a | -8.106 | -55.5701 | 2025-08-13 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| f1c42c42-cbd4-38e1-a7a2-5dccefad345f | -2.9108 | -48.254 | 2025-08-13 03:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| a3996c8e-cc71-3a54-a5c5-53a2c187c05b | -9.1894 | -59.6558 | 2025-08-13 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| a5e4ad16-763c-3743-82ad-b86d139e7fc8 | -8.1246 | -55.569 | 2025-08-13 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 89c68751-84fb-3bb5-a609-511890081a6a | -5.45046 | -43.57291 | 2025-08-13 03:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 75839897-1a31-3121-a95b-fff806f901ee | -5.44928 | -43.57935 | 2025-08-13 03:23:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 85bd0965-5da8-30df-b101-359c50ed1833 | -6.89268 | -34.95966 | 2025-08-13 03:23:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4f08b967-e2b0-3e44-8f88-505ff036dc15 | -5.18435 | -37.65903 | 2025-08-13 03:23:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 163b82b8-4c74-3700-9d9e-8ec31501a79e | -5.26235 | -36.17207 | 2025-08-13 03:23:00 | NPP-375D | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6050560d-41a5-364d-8fa0-bbef2f058a23 | -6.61113 | -43.88477 | 2025-08-13 03:25:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 829465ea-3c08-32bc-9bb4-7a4fe10bda01 | -6.61437 | -43.89139 | 2025-08-13 03:25:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00977bca-0234-3877-95ba-6f09af65f935 | -12.31334 | -46.04911 | 2025-08-13 03:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f252692-edcb-33d8-9bba-391e28f3c9e1 | -12.32192 | -46.04903 | 2025-08-13 03:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 31182899-476c-309d-a9c0-1b05e7479098 | -12.31306 | -46.05507 | 2025-08-13 03:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de311324-477c-3074-a05f-f62ce4d6dd78 | -6.61566 | -43.88464 | 2025-08-13 03:25:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8c8e1219-e117-3502-9447-c1ac09c408ba | -12.32054 | -46.05059 | 2025-08-13 03:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8e7a0bbb-7eb0-35db-8010-2d2ba9b356d3 | -6.60989 | -43.8915 | 2025-08-13 03:25:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8f9702c-e142-3e68-baaf-3aee129edb28 | -6.44881 | -44.55693 | 2025-08-13 03:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1799eccc-618e-345f-9e30-38eff2788d8a | -12.30613 | -46.04767 | 2025-08-13 03:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bdbd319d-cf19-31da-af0b-d1f10efc95b5 | -7.39146 | -39.68344 | 2025-08-13 03:25:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 25ae9f03-240c-3e62-b6e7-4b7a7d1218f5 | -7.39414 | -39.68353 | 2025-08-13 03:25:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cb912ee6-63e7-3db3-aa47-2fa7b09c4b5c | -7.06666 | -44.36512 | 2025-08-13 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 647bce24-5321-37c1-989e-31ead762eb00 | -12.32029 | -46.05642 | 2025-08-13 03:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0875c744-4ec8-3dc1-8e61-fc6f447ce682 | -6.45472 | -44.56554 | 2025-08-13 03:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f30de37-9f97-3550-b2f4-15fbee85c31d | -8.9866 | -40.62611 | 2025-08-13 03:25:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f4f6dd93-f26e-3783-a4f4-d61d32c7788b | -7.05962 | -44.36328 | 2025-08-13 03:25:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0403186-605c-392e-9e92-5d796d3de24a | -7.48637 | -43.93303 | 2025-08-13 03:25:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4ade0258-34f8-3562-b05d-f215cf0d822a | -19.08169 | -48.14923 | 2025-08-13 03:28:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4400f9e7-26bb-3734-b968-a3d600c650a9 | -14.115 | -44.32048 | 2025-08-13 03:28:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d961be4d-f6c7-30d9-a099-9b5d666ff88f | -19.73063 | -45.60424 | 2025-08-13 03:28:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1f9a65c-426f-3692-b9e8-ae0ac3dc0c7a | -18.54465 | -46.06106 | 2025-08-13 03:28:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 26.3 |
| a90c1d65-e366-3422-b4eb-1cab68dbcfaf | -16.59606 | -47.03803 | 2025-08-13 03:28:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd39d865-9283-3033-9e07-b8be16e08cee | -19.08307 | -48.1529 | 2025-08-13 03:28:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aaf3ee62-2d6b-3b7c-8b95-4d5b570c8e78 | -18.53697 | -46.06493 | 2025-08-13 03:28:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 33.1 |
| a7066942-31ba-3659-ae21-3cdf1bb4afca | -14.1224 | -44.31684 | 2025-08-13 03:28:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6441b446-3692-354d-b309-2f5c43dbd8a5 | -14.11974 | -44.3201 | 2025-08-13 03:28:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 346eaf8c-9115-3498-8f81-49ab6dc448de | -14.12083 | -44.31485 | 2025-08-13 03:28:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e67ff5c8-6bca-3ab1-8a49-cfe4f8aa4cc7 | -19.07992 | -48.15656 | 2025-08-13 03:28:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fca5a38-914f-3712-b7f5-915d7da238c6 | -18.53313 | -46.0521 | 2025-08-13 03:28:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 29066555-c508-3e61-a677-4a1d3589c4ef | -19.07601 | -48.15084 | 2025-08-13 03:28:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8780cd76-8d10-3d85-acae-45b2e8758db1 | -19.76132 | -46.43415 | 2025-08-13 03:28:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 377eb943-d627-31f5-85ce-e560da57875b | -16.59254 | -47.03511 | 2025-08-13 03:28:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67e4396d-4c99-37a1-b118-9ad3aa3948f6 | -14.11611 | -44.31535 | 2025-08-13 03:28:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b81dc7b6-9a2f-3bf5-b7b3-87cc7b81ecd1 | -14.12127 | -44.32209 | 2025-08-13 03:28:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af750afb-f891-36fe-84fb-c5ed1c3057f4 | -18.53828 | -46.05922 | 2025-08-13 03:28:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 522a0570-dff7-3685-8e3c-b61134b8d4e8 | -18.53187 | -46.05758 | 2025-08-13 03:28:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cc7de3ba-d540-3978-9c65-483358742b2f | -18.5459 | -46.05561 | 2025-08-13 03:28:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 26.3 |
| bf2f644c-ace9-3212-a72e-24be93b94476 | -21.15885 | -41.62864 | 2025-08-13 03:28:00 | NPP-375D | BOM JESUS DO ITABAPOANA | RIO DE JANEIRO | Brasil | 3300605 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 37fdaf57-657a-33dc-937b-ad7eb0556f27 | -18.53953 | -46.05379 | 2025-08-13 03:28:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 47ec451b-06a4-371c-b361-cf6c0b189ecc | -16.59958 | -47.0367 | 2025-08-13 03:28:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4bdf779-7a7c-3bd9-a0e1-c1eaf08f2563 | -21.16045 | -41.6254 | 2025-08-13 03:28:00 | NPP-375D | BOM JESUS DO ITABAPOANA | RIO DE JANEIRO | Brasil | 3300605 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1e91036a-044a-31d8-accc-c5070c0115be | -12.4981 | -46.9666 | 2025-08-13 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| a24a2342-c161-3088-850b-fb78d2072f92 | -7.1298 | -60.1374 | 2025-08-13 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| dcd12b71-35b3-3655-9d38-96173752ee51 | -7.1299 | -60.1182 | 2025-08-13 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 14a9c505-1f95-3695-945e-ef90eb5f7345 | -21.76163 | -46.59779 | 2025-08-13 03:30:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c31136f3-11e5-3f0f-b04c-ebb6ef0f1ce6 | -22.38004 | -45.47964 | 2025-08-13 03:30:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| eb197424-0ae2-300a-8ce7-a5c034cb0567 | -20.8557 | -49.07734 | 2025-08-13 03:30:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 43aa96da-051e-3074-8b65-44284e9dd18b | -22.38231 | -45.47007 | 2025-08-13 03:30:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b7762fdc-2f92-344f-868d-c35ffd01f70d | -22.37717 | -45.47221 | 2025-08-13 03:30:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0d2137c5-6df9-352e-98e8-c87077a0d180 | -22.75155 | -47.19834 | 2025-08-13 03:30:00 | NPP-375D | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfc8e308-b767-3cf8-b40a-74f61decc7e8 | -22.38184 | -45.4785 | 2025-08-13 03:30:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d73948f2-56f7-3d42-a686-3b1866eb7a0b | -22.38116 | -45.4749 | 2025-08-13 03:30:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0bba76fe-ae4f-3d0e-99d3-e2ce47322c50 | -22.38294 | -45.47371 | 2025-08-13 03:30:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| eb355888-0dc9-36fc-9725-278d734eaa89 | -22.38765 | -45.47981 | 2025-08-13 03:30:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 39532b97-5907-3bf8-b446-078abc72dc0e | -22.38695 | -45.4763 | 2025-08-13 03:30:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fa96fbb3-46d3-3c6a-a599-f2f13bd7f9c2 | -22.75046 | -47.19626 | 2025-08-13 03:30:00 | NPP-375D | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67d29023-38c7-398c-8dd7-5aa5f3f1596d | -20.85782 | -49.06919 | 2025-08-13 03:30:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3baec8cf-2318-3015-aeb0-99e83cc25d88 | -22.38874 | -45.47506 | 2025-08-13 03:30:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b4942596-a5f4-30a6-9894-cdc431acbbfd | -7.1298 | -60.1374 | 2025-08-13 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 78c3f42b-77d6-3873-bbb5-dcecfe9c706c | -7.1299 | -60.1182 | 2025-08-13 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| dda58c0f-4a36-38ce-ab52-ac846bb6aa32 | -9.37017 | -40.70815 | 2025-08-13 03:47:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e1505151-dfcd-3af0-9748-19f64e40b142 | -7.06151 | -44.35877 | 2025-08-13 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b286b4fd-934a-31b4-888d-221cfb1a7f34 | -7.74943 | -37.62714 | 2025-08-13 03:47:00 | NOAA-20 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7cb8bde0-43f2-3dd1-9ec8-9ef08381e89b | -8.98574 | -40.62707 | 2025-08-13 03:47:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ae4edd14-298b-36a0-ac23-b95120e89950 | -7.0581 | -44.36001 | 2025-08-13 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8f1a5ec1-f534-3bf7-9bdb-96c36a9ca0ac | -7.07379 | -44.95122 | 2025-08-13 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a0beb9c9-62de-32ed-8270-71c621a3ded7 | -7.1541 | -44.39281 | 2025-08-13 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f57be018-f6e5-38ce-b673-0f2f0592a682 | -7.07175 | -44.93363 | 2025-08-13 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 46556029-a568-34c0-8acb-df6dcbefd714 | -7.07178 | -44.94744 | 2025-08-13 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3dd85352-1c37-3682-b1be-e5a8e1a1aaad | -7.07672 | -44.94803 | 2025-08-13 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 01e5e268-d04d-39f7-8682-cd4e35650de7 | -6.61515 | -43.88094 | 2025-08-13 03:47:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9f98df59-052c-3522-86e2-c92a4b4024ff | -6.60975 | -43.88484 | 2025-08-13 03:47:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 677cb725-bf71-31fc-8a95-ccadac7c6582 | -7.87052 | -39.41931 | 2025-08-13 03:47:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 512befd6-756d-3dad-8401-b590080c0758 | -6.5905 | -44.55359 | 2025-08-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36e1ae3b-2514-3c84-9574-b16eb9e15a52 | -7.0738 | -44.93614 | 2025-08-13 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cdbe4757-f0f2-3c14-930c-519a83286eca | -6.61057 | -43.88015 | 2025-08-13 03:47:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| df59ea54-4cab-32a3-97db-f4bf0104d4fe | -2.9012 | -48.25712 | 2025-08-13 03:47:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b30f8245-0019-3c8f-b086-1ce2a1f14233 | -7.06887 | -44.93553 | 2025-08-13 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02ad13e3-2c20-3d0d-bb68-edfeaf7ffac4 | -6.45174 | -44.56281 | 2025-08-13 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README12.md)
