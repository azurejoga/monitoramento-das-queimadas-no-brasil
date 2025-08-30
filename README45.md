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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17096337-4612-3264-a023-64cac4802f3b | -10.44632 | -51.35582 | 2025-08-30 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2a35073-1408-32b4-9848-dbeffa578416 | -9.44651 | -60.55368 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 49a39dd4-6410-3def-b65e-4d043798cc05 | -7.15378 | -45.16631 | 2025-08-30 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6ac2246e-c44e-3b8f-b4b7-baffc22b4d72 | -11.2206 | -45.0219 | 2025-08-30 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb862d52-1146-3c5f-a42a-40e43b71776a | -8.09353 | -44.9791 | 2025-08-30 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67785d62-b82e-342f-8375-1ec1e870bf9c | -11.58728 | -46.36518 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 04e8cfc9-f5cd-32e4-bfad-193c71a21b9b | -9.45515 | -62.3287 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 42.8 |
| b627d133-d373-33d0-88da-c28a0868602f | -11.92379 | -46.69712 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16d89d3a-6e94-37b4-9a86-67935db904de | -10.27337 | -54.23738 | 2025-08-30 04:49:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc11c397-10eb-365d-a4c2-6615cbb34112 | -9.24859 | -56.8989 | 2025-08-30 04:49:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f8110d1a-53f2-3fd9-9d97-1b146a2b8518 | -9.43776 | -60.54228 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b592821d-7042-3cd8-aabd-77dd366d8fc0 | -11.36123 | -43.5764 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60b4b4e6-d7fc-3c2d-af85-a30cfc1793ad | -6.34265 | -47.7316 | 2025-08-30 04:49:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5829c8cc-409c-3a0b-940f-83f5b9a17d25 | -11.35912 | -43.57005 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9167795c-8e8b-3a76-a42f-c035cae6632e | -8.45929 | -43.64003 | 2025-08-30 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c24193d-239a-3efe-94dd-772bd4fd1af0 | -10.02433 | -48.05907 | 2025-08-30 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53770e28-ab3c-31d3-a3c1-f18dc833957a | -8.8477 | -52.02676 | 2025-08-30 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd2f6caf-9f48-3272-80d8-7b9ed6737056 | -11.83576 | -46.86189 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 904af222-fea2-3009-b245-23d709de73ac | -10.44806 | -57.96793 | 2025-08-30 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef2f1533-ef6d-3403-96db-d10a2059167a | -7.39322 | -60.59199 | 2025-08-30 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f269f5b0-a93f-34c9-8944-bb0c9cdb8889 | -6.63331 | -55.27001 | 2025-08-30 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 521dc4cb-7303-3634-9ca4-3c378f55ad1a | -9.43778 | -60.57215 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 60d75205-11d2-31ab-9982-4c366d2f3af6 | -8.46491 | -43.63543 | 2025-08-30 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f53deabf-6837-3c5f-8566-b7100e7aeff1 | -12.56563 | -44.80246 | 2025-08-30 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67d5e06b-2ec7-32da-8d3b-9b5050f931eb | -8.88014 | -60.72913 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d777bf54-6aa1-3957-a83d-7333be5f3526 | -9.11502 | -65.78911 | 2025-08-30 04:49:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7d1941ca-2167-365e-b5fb-5329dcbe5f70 | -8.67598 | -62.43253 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adcba4ec-ef11-390c-a50a-25c9b0a4dc92 | -11.06719 | -52.05 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c75ecdd-1fee-3d6f-9076-c6e307fa210c | -8.18188 | -45.0474 | 2025-08-30 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2955e4fb-858a-396d-81af-ce893a4e908b | -7.10827 | -44.58788 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2ecc45f-a420-391a-be9a-7f536b09c185 | -10.18871 | -48.9179 | 2025-08-30 04:49:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef2bc0b9-94f8-32d9-8730-fce97cfdbb6d | -10.37829 | -57.82954 | 2025-08-30 04:49:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64816dc0-d9ff-36ea-8484-de552570ebb0 | -11.3024 | -43.62977 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 834e5b9c-e9c1-3434-816e-dc650f114385 | -11.40861 | -46.90413 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae523bd0-11bb-3390-b5a4-17357f92e26b | -11.30867 | -43.62129 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6972c532-0b0a-33cc-99da-835886a2d0c1 | -11.36384 | -43.57383 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7928d6fd-0407-3a1e-a4fe-eb2b2a6e6c1e | -9.43929 | -62.32829 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 326e7536-c6fc-3fdc-9aa1-38f18474f21d | -9.45995 | -48.25768 | 2025-08-30 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 798ac868-1f4c-37ca-bdaf-fd198516c95a | -9.44418 | -60.56665 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1f226d04-4c2f-3f9e-b72a-204d4183fc18 | -9.44112 | -62.37006 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4e5d3dbb-f4d5-3d34-9697-6d0a013edbad | -8.90856 | -62.10194 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 320560d0-1366-37f8-a7a2-23eb7216cfe3 | -9.46176 | -62.32589 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 24dcbd7e-60d1-3317-8dcc-f4a2593b3a16 | -7.41108 | -42.06338 | 2025-08-30 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 827dcf12-3319-3b0b-9c97-ce84bb4ad038 | -7.59301 | -42.7077 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a5680418-4a27-3fdc-a682-e2280fa33ada | -10.38111 | -57.8385 | 2025-08-30 04:49:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 445af81e-a33e-342c-b99d-33c35b8f2082 | -11.686 | -51.68705 | 2025-08-30 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df4ac002-1755-39ea-80b7-96113b11879e | -7.75531 | -45.46186 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef78baad-93f5-3b37-a883-1215e7a44b23 | -9.17058 | -59.57045 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39ebdbf2-dc34-3d55-8ba3-9ff226252ac7 | -9.46877 | -60.31102 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c864fda-9a42-3404-88c7-ca12bcd90c97 | -11.57195 | -46.35113 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 547d2c03-eaf0-36f1-9ca0-81fcac0d8af0 | -8.52819 | -64.00984 | 2025-08-30 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9f28e099-ffe8-3429-8953-6ecc38df453a | -9.46821 | -60.31411 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5940537-951c-38e6-b04e-ec09dc8d06c3 | -7.39259 | -60.59552 | 2025-08-30 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d6c86fb-9166-3d08-a298-df7c37df2515 | -11.83732 | -46.44571 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3330d0d0-10cc-389d-b261-fb974d59044b | -11.84768 | -46.40066 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 27a4e4c2-564e-3ea8-b1c9-21ea2d909633 | -7.40623 | -42.05914 | 2025-08-30 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9efe748b-cc46-3cf9-a49b-837a150a8a4c | -9.51058 | -54.44267 | 2025-08-30 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98c29f6e-cbb6-334e-8922-6415d9fa7cc0 | -9.7755 | -64.25468 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 339969dd-d3d1-3a5e-afd5-edad38702dcb | -11.32471 | -43.61734 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4eba88c8-4466-3812-b7f4-d012011e9a73 | -11.29293 | -43.58271 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efce1120-9e70-36a5-bb5e-9ab9155d1fa2 | -7.58916 | -42.69769 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 69eb63db-a240-3e3e-9542-d0a2cdf51639 | -9.43884 | -60.53614 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c19a6c6d-c512-35ee-ae3e-e13033462a32 | -9.44477 | -60.56335 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 42b65fad-1dc6-3757-846f-f9b0a0688b9a | -7.09687 | -44.60374 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cac4ef47-fff7-32c8-ad74-3e1c7adb89ca | -7.95837 | -46.39215 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7c1d754-bf03-355d-9f98-4a30ef0612c6 | -7.72101 | -50.28805 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a3764350-1dc9-38e3-b4a2-9ed2ed1ec17f | -9.50522 | -45.39515 | 2025-08-30 04:49:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36a0aa2f-b045-349c-9113-9b2888fdb92d | -8.67124 | -62.4367 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e109fde9-fe72-3198-ba6e-b618dabbf7a0 | -9.2812 | -60.45658 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdeb7efe-2f33-3c38-b34c-27bd94225b30 | -7.39879 | -60.59602 | 2025-08-30 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c6f250d-3067-338d-8269-45348cc2d6a8 | -11.29695 | -43.63195 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0061087b-01b4-35cc-945a-32ed4084c69b | -8.04989 | -45.41396 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f981a5b7-9af2-3932-9d5f-23b2d419a84d | -11.8273 | -46.45622 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 6c0f44b7-7a3a-3031-9b51-0a441231ffe0 | -10.0713 | -58.35833 | 2025-08-30 04:49:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90940f34-0609-3e07-9a5d-ca02fa904b1a | -8.56184 | -63.01705 | 2025-08-30 04:49:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7e5398f4-d0ec-3d27-9ccd-970304bf0a40 | -9.45938 | -62.33829 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7f8a8e07-1a75-3ec1-9d8c-f2a445b702d8 | -11.36164 | -43.57332 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b41c307-7e98-3d1c-bf00-7031f81376f2 | -11.07273 | -52.03647 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85045116-80e9-3fc7-93f5-d5bc141473df | -11.33701 | -43.52328 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6c6a58b-2ba7-333c-9731-10383cadc9ce | -11.31377 | -43.66152 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22bac6ff-c40f-3455-a941-74e42d64f9fd | -11.83524 | -46.8656 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd7891c1-5df0-30e8-912e-7b935ff7764d | -12.37165 | -46.39297 | 2025-08-30 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| fd81b26f-ef84-3102-b08c-1ef64ebe4747 | -11.33171 | -43.60349 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d6cf0327-2ff8-37e4-ae27-9ec816421103 | -9.58081 | -54.49472 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f81524e-bdbc-375a-9a6f-5317896051c3 | -9.57725 | -54.49409 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4af04ce4-28e3-364d-a425-fc3a858090d0 | -9.44282 | -62.342 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 43f28d68-64f2-36f0-a842-5fbdab43dc8c | -8.90778 | -62.10613 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7d61411e-ddd1-3b6a-b384-76a968cde7a5 | -9.43887 | -62.36331 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac4241b1-5d39-3f38-89eb-c08d78b6c00b | -9.44358 | -60.56995 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6fe20b32-9004-3a42-9e1c-86ff1ea8aa96 | -9.58641 | -54.48302 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2981fd49-9e9b-3555-90fc-36ee1d3cd046 | -11.83216 | -46.8576 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5eb0b660-4aa0-386e-a200-1271cd26700b | -9.20098 | -59.55104 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afb758d9-452e-30f4-942a-3cd80a80ee65 | -11.87965 | -46.45126 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ec2f691-53d7-383f-b333-73a87f6c118c | -9.22152 | -46.75275 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 56df9e98-db0e-3c00-97be-1bd0d1c522ff | -7.40697 | -49.5174 | 2025-08-30 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50b73bfc-0192-360e-8deb-6dbf439be78c | -11.87977 | -46.38703 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 276c8dce-e19f-3ccd-a4f5-cc62a92e9c2b | -11.85033 | -46.38081 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3f2c00f2-da00-390a-9a44-52862b18c89c | -10.02786 | -48.08717 | 2025-08-30 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e873db18-be94-3eac-a05c-fc1044b88aa3 | -10.53314 | -56.38532 | 2025-08-30 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 510c173d-3cb9-3951-b9de-a9b4446323ed | -11.83908 | -46.43874 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README46.md)
