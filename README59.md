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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cba79c01-4fd5-3b01-a0d3-973fedba62de | -5.44855 | -43.4425 | 2025-09-08 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d0349524-70fa-39a4-9c47-e1b772849e17 | -5.99346 | -44.15187 | 2025-09-08 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25f17821-3d44-3840-9aae-23ebdc87f161 | -5.54935 | -43.79333 | 2025-09-08 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a61d6200-0a35-3ffc-bf23-47668906c5f4 | -6.59256 | -44.00614 | 2025-09-08 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98774c0d-9558-3583-87e1-2e606cd5c631 | -8.60421 | -54.6694 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f9ebfc0-d7a1-3b3a-afbd-04dc5d9a9030 | -10.00216 | -51.62223 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82a07421-11ec-3e7d-a4da-3e3979d4de8c | -6.63141 | -53.37239 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24eb73b5-ab72-3ab5-880c-5f5851a57af6 | -4.23759 | -53.55338 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1baa2a98-39bc-38fe-adc9-a474e96456cf | -7.67004 | -50.29241 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 064eb1d7-5898-3b90-bf90-d0f96ca5b063 | -9.18103 | -60.76624 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7fc56c52-a45b-37bd-936b-9d2d38ff4159 | -8.84945 | -49.57127 | 2025-09-08 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d988c1e7-b768-3a50-a227-f5291cb5f80c | -9.61066 | -55.01363 | 2025-09-08 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15fd32a7-f97d-350e-9d99-e933d361a75f | -10.00165 | -51.64902 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a24f2278-8c1f-3bcb-9716-e43d561cd92d | -8.65654 | -45.745 | 2025-09-08 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4c75b59-1c70-3876-89a9-f05665d58b59 | -4.89439 | -42.21343 | 2025-09-08 04:51:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cd4bfede-05ff-3b78-ad94-682454ed294c | -6.10092 | -45.46404 | 2025-09-08 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d1a31559-a03a-38cb-a3bb-cdd158212cae | -8.19706 | -44.78226 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b4a06f37-b710-3c61-b5ce-14442f8f5075 | -11.39321 | -43.54211 | 2025-09-08 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c088bfb2-0ef5-3f54-a022-b1c3a2822a23 | -7.78808 | -52.12983 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1a610bc-4a09-37fe-9c76-79e5a16e21fc | -8.69928 | -45.30976 | 2025-09-08 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5af69be2-b099-3ccc-bea8-6d277a2ee47d | -6.14169 | -44.23214 | 2025-09-08 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f46306c-47eb-3e47-ae24-851d2befc7de | -9.03593 | -49.79665 | 2025-09-08 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b3d9a91-bcae-32c7-8461-50164264781b | -10.45022 | -53.6034 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2db44b26-642d-34ed-800d-fa52a24f0bf9 | -7.00435 | -44.93411 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25d179db-ed27-3a4c-95d6-609814369cdf | -9.33327 | -46.52275 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a4ae741-dbdc-3d8f-81ee-6fc7e7c4f204 | -8.19549 | -50.14289 | 2025-09-08 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b73a78f3-a4f4-3ff9-bd1b-9da86743d1fe | -6.64941 | -44.80736 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35d9684b-5bc2-39e5-b381-ee578571d17e | -10.14016 | -46.19339 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b8f63c13-b3f4-36b1-a3aa-b945a79122f4 | -6.48839 | -41.76954 | 2025-09-08 04:51:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 95ef71c1-09ac-37a1-b734-1490b6cc4f6c | -9.99706 | -51.63295 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e5589f7-116b-36fb-b270-44013a5aed47 | -5.9421 | -45.74967 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f6fc6f0-42ad-36a1-9983-9f03cc5a01cd | -6.21292 | -43.37902 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 395eeb9f-7fac-3eb5-a234-a2e10b3415c4 | -9.71915 | -43.98261 | 2025-09-08 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e33c6ea0-7b18-362f-9936-21d1701355d6 | -10.80911 | -47.25515 | 2025-09-08 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f2eb375-2ffb-30ad-90f4-37bd5a939248 | -9.82159 | -47.77399 | 2025-09-08 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fbca09e7-12b6-3317-b19e-916d41128011 | -9.20649 | -46.04629 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8f213080-5ad3-355a-a2d0-15da37771f63 | -6.18934 | -53.26306 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 288872e0-eb57-33df-91f1-cb0c7c3a09e7 | -8.60413 | -54.69161 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7855d86-ad9c-3bf5-a1f9-a1eeb87a3e64 | -11.03508 | -45.95971 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b202fc0e-1d95-3ccf-91a8-aec310f5adc3 | -9.16791 | -59.372 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10c137b3-787d-38b3-a93d-c1341e65413a | -9.05187 | -50.46729 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aec24ee4-3b7a-3121-a020-8055ba298513 | -8.8772 | -47.90676 | 2025-09-08 04:51:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf92167a-17a3-3608-8d3d-1266329b226d | -6.2134 | -43.37556 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2e0dd84-a48c-3d52-ac11-871579ac4678 | -8.29876 | -45.95125 | 2025-09-08 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b04206a2-45c5-3030-b927-c21c792b0a3d | -6.25808 | -43.71106 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cc22b54-7111-3763-8ae2-5a02a2ba2d4f | -9.332 | -46.53213 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ae0cf7e-e05a-39f6-bdeb-f647f0e3493f | -10.95951 | -46.81783 | 2025-09-08 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 19109879-c338-3751-a64c-1a8ac61cab0d | -7.62452 | -44.66688 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e3fd326-4ad7-3e81-8ee8-584bfdcf3c78 | -5.98833 | -44.15125 | 2025-09-08 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd9dbfb4-1545-386a-8f7a-ca85deaae709 | -6.23917 | -43.50615 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8122c80-649f-37f8-967e-1c67ec0ac445 | -5.94666 | -45.75046 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf5ada48-829b-3d0f-8ebd-ccc5205e3a6e | -8.70261 | -45.30464 | 2025-09-08 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4f133b0c-69b4-3705-b319-1706551dfb4d | -8.04062 | -44.03564 | 2025-09-08 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c112fd58-627d-39e0-a72f-07363a71aa0e | -6.85212 | -44.82261 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 25ba44ef-dfb6-31c3-8851-91d919a05f9b | -6.17251 | -51.51835 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a9e197b-b41d-341c-b891-fc0a0b2b1c45 | -6.06612 | -57.7998 | 2025-09-08 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 543ba29c-a2aa-34db-ba7e-2d08a4ca8c6c | -10.36749 | -46.4907 | 2025-09-08 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38295f53-2d4c-313b-9b65-e72e7c51bd62 | -5.88625 | -43.96204 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6143a893-9d3d-3f13-8e61-59c14b3e7482 | -6.80843 | -52.8088 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| add7424c-9cf0-36fd-ae08-05dead6c6a74 | -8.19132 | -50.14628 | 2025-09-08 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca3b84c6-db05-30de-87a3-1ab2dbaf2c25 | -6.60833 | -44.00735 | 2025-09-08 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27f417f1-d10f-39a9-ad10-81ae91b96068 | -8.09213 | -54.75783 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 302d4eb0-33e9-3dee-92f2-d809e2352405 | -4.42878 | -55.16423 | 2025-09-08 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ba0afb5-3e95-38d2-b95c-bc460d634381 | -7.73891 | -50.31492 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4e4592f-99f4-3cb5-862a-e92bc4819314 | -10.1435 | -46.2044 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 81f08e4d-644e-33ea-a6a1-9ebf055559f9 | -7.73833 | -50.31878 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7561a01-bbc2-3f5e-9aae-1dc3743a3dce | -8.74599 | -46.67999 | 2025-09-08 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 859ed09e-6d2d-3606-a187-b30deeca1f58 | -6.38943 | -43.80992 | 2025-09-08 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0b8dd1a-724e-31de-b078-c4b731fa074f | -7.78863 | -52.1263 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c8cb9d6b-9b21-33b0-86df-d8a84a7c6e91 | -8.19695 | -47.56513 | 2025-09-08 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6248a7c5-db5e-39c9-b41c-83dbf6a398f3 | -7.14236 | -44.57026 | 2025-09-08 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4afb8f8a-c810-3a2d-a5a3-13afbf53e3e3 | -6.07569 | -43.55765 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0abfc602-1feb-387b-8c31-784ca6831983 | -8.19292 | -44.77477 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cba2bab-01b6-3769-98f8-3d6aabccb4ae | -7.99508 | -46.34146 | 2025-09-08 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0aca75b-dacb-37ed-b8fc-9ecc196147bc | -10.14283 | -46.20942 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 51f49b9c-97a2-3428-8317-c299a57498e2 | -11.03299 | -45.93774 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e0114b4-d519-3ab5-b3be-cef1b223077f | -5.98121 | -53.59023 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eefe4fa5-7265-328a-acb3-53f41037f117 | -6.48181 | -41.77291 | 2025-09-08 04:51:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b1416a1e-b2aa-303f-aef3-5f827d3d63b5 | -6.84536 | -52.85759 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4bfef9f-4a96-38f0-b5db-234114e6be79 | -4.49109 | -54.82256 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdb22b46-32b0-337d-ad8e-e7e7d5a9962b | -6.62367 | -53.35696 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91a1acc8-a846-3eb9-9d24-4c38c39b6e86 | -9.44588 | -49.44235 | 2025-09-08 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ed25fef-02b6-3a86-8c82-9ce0ff5741e7 | -9.68583 | -51.06861 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed2e1b98-d6c2-3865-951f-7c353d24efb8 | -5.63255 | -51.35884 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7ed45fa-228b-3860-a4b3-23e2b6cfa7f5 | -11.57476 | -44.65646 | 2025-09-08 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2b30e0a-2434-35f3-a284-a904ad04b358 | -5.78634 | -45.62468 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 458c6dfe-49c5-3af2-9bb1-8458aaae65c1 | -6.28093 | -53.4163 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52df7f88-0ce9-36e2-8702-dbb1af1fcd9d | -9.50671 | -57.7786 | 2025-09-08 04:51:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 430e47e6-4fd9-37fb-b11a-e81dd50705ec | -7.53115 | -48.22917 | 2025-09-08 04:51:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3c133054-7953-3196-ac68-e1a8b83303cd | -11.39177 | -43.55434 | 2025-09-08 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67e25263-88bf-3bb2-92e9-5233466cfd2e | -4.47687 | -48.11737 | 2025-09-08 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2774dbcc-879d-39bc-b8ee-84010dc4b30a | -5.71775 | -43.89628 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6796288b-6d3e-3b59-bf16-e1607ab669d1 | -4.95773 | -55.81406 | 2025-09-08 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 307a7a15-4857-3b29-84b2-fb7cb7d60874 | -6.87725 | -47.92572 | 2025-09-08 04:51:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| aaa11e3a-ebf6-3944-9960-87e5409fc607 | -5.21532 | -43.28116 | 2025-09-08 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4f34d3ee-d999-318e-9b59-f60e991ea5be | -6.19179 | -43.37236 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ebe0901-ec57-3380-9a42-1beee3970b09 | -9.68176 | -51.07201 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8567924-b400-348b-a486-9e5e6c5ae79e | -11.28634 | -46.4645 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9501c10d-895a-3545-acba-1309aeed66e7 | -5.88539 | -52.09729 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87d27de4-9600-378d-a05f-1d3cf4c37921 | -9.2105 | -46.05207 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README60.md)
