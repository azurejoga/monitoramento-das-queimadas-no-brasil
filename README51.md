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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afe43388-5e20-3478-a970-24300b41ed1c | -7.31668 | -42.87249 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fd547523-2998-317b-ab3e-d6faa7b9f0c3 | -5.61503 | -51.94074 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4bb9dc7-be1f-31f5-935c-3e6379554ebd | -4.57158 | -46.50013 | 2025-10-03 04:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17d87aba-c4d1-3254-afcc-8ef6372da1e5 | -5.78179 | -45.76102 | 2025-10-03 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c1d90a6-dc45-313a-bec1-e074da087558 | -6.64935 | -42.78776 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 4fcc450a-e8be-3b1f-ba29-3f8d61b26a56 | -5.97518 | -44.15407 | 2025-10-03 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e9f4a2e-e84b-3f5e-aa44-15b9ccabda78 | -4.65727 | -45.80627 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 5c5fc2f9-35bd-3379-9f90-3f9ad79bd690 | -3.84533 | -41.57892 | 2025-10-03 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a818c5d9-05a9-39f8-a5e1-fda5bbeaba23 | -5.75287 | -46.61423 | 2025-10-03 04:10:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4544a261-f41b-3668-9cd5-29eb00aaca09 | -7.75309 | -46.23806 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d7cf69a0-6335-30c6-8f7e-c6bd408e732a | -7.75523 | -46.27299 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 4f58006e-6055-33d4-935a-29deb4540068 | -7.75606 | -46.26805 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 779e3ac9-da3a-3b6c-b5c8-f4cb512b77c0 | -6.36374 | -43.30056 | 2025-10-03 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b659a5c7-3918-3b86-921f-2edc1285a31d | -7.75487 | -42.56156 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| 73f3da1a-577c-360e-943d-d171457d9bf2 | -6.22842 | -44.24186 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d291acb-f3a3-3651-9910-b9a23a6590be | -7.75848 | -46.22972 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8d15aa5c-3c96-3fa3-9d71-3a9a87ea1c10 | -3.45624 | -40.23285 | 2025-10-03 04:10:00 | NPP-375D | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| be67f80d-b443-36f5-9fb6-d7364bc4f9d2 | -7.7543 | -42.56507 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 9329eaf8-265f-3177-affa-082889b538b8 | -6.3569 | -44.75657 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86731b47-44a8-3fd7-be9f-c8d14d2f49e9 | -7.29416 | -44.1922 | 2025-10-03 04:10:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66923d24-dee7-3d71-82e6-5d09e436002a | -5.69813 | -42.83576 | 2025-10-03 04:10:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 55b55a05-c15d-38e8-aeee-cac147b7d591 | -7.76829 | -42.52049 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6a1d48e8-04dd-3ea7-b9ff-8c3b1f089518 | -6.20436 | -45.91877 | 2025-10-03 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0afd4065-be81-3a73-a46b-0e984cdd2e6c | -7.78996 | -42.55636 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4e29243c-203d-30b5-a24f-b70b5cb15e47 | -6.23643 | -44.25981 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb53c4a1-1096-30e4-b45f-1328f48804c3 | -3.842 | -41.57839 | 2025-10-03 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 88253e32-f3f8-3652-a9f3-dfccc11f89da | -6.61497 | -44.26013 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecac39b8-5f09-3752-8462-2bc8f428f2d4 | -7.78103 | -42.56936 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0819d106-d803-3619-a3df-47a6ced7828e | -7.29573 | -45.2676 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4757ef76-f9f1-3daf-82ea-96a31697d554 | -7.79891 | -42.52178 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d0481528-c55e-3fb7-b8c4-5594f5e91c98 | -6.26509 | -43.88469 | 2025-10-03 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6f9aaf2-3b71-3d8b-983d-dc8d70796fe1 | -7.76875 | -42.58182 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dce7de6e-ec24-353a-8970-40a98c4144e6 | -7.74828 | -46.26679 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| e521c29a-579a-3858-9040-0843d8933e3d | -3.09388 | -47.01407 | 2025-10-03 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d9c313da-b052-3878-a22f-85b1402d7671 | -7.30893 | -45.25637 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f8485d2-da67-316d-af21-68cfb71a65b1 | -7.79052 | -47.37284 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 205a1cbd-7fcc-3b55-b30c-016109ff2cb1 | -6.25215 | -43.64732 | 2025-10-03 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d2707a3-0a94-3382-a35c-6a0d80bfadd3 | -7.76211 | -42.55912 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 14576469-a3be-3357-9103-4d75e0aa8858 | -4.67 | -45.80288 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 6b7d79eb-0f10-3cab-8366-6eefaf0cde1f | -7.75877 | -42.55859 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 303f7377-df21-3cd4-aa36-d0285a7931ac | -6.64361 | -41.2737 | 2025-10-03 04:10:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 904ddbbb-8576-310d-b799-df543da414af | -0.90133 | -47.54429 | 2025-10-03 04:10:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a310cf19-6b6a-3071-819b-27433b4ca1cf | -4.85677 | -45.66525 | 2025-10-03 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a49f167-29f8-3715-83f3-4fdf233f11f7 | -6.41711 | -41.7436 | 2025-10-03 04:10:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f47cd31e-0e58-3dce-b3c5-84b2b33d50ec | -8.33571 | -46.22564 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 592710de-3217-3254-b3ae-5fe1121655ab | -7.90281 | -43.52569 | 2025-10-03 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a2eb452b-bd63-3015-8bc5-33b60f0327dc | -4.95438 | -45.77462 | 2025-10-03 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af5d77c2-1476-3ff7-b343-69ba4f3df031 | -7.75655 | -42.55104 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| e7c5eb83-39b0-3b24-82f8-064120f99c8d | -3.49577 | -50.2747 | 2025-10-03 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c3e1c33-ea80-300a-ba87-ab374e370c29 | -7.77107 | -42.52454 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 121d9d52-e483-3b67-ae32-f45747fcb3d3 | -7.77721 | -42.50753 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 96a04374-a406-39a2-b524-61a400da3af1 | -5.18111 | -45.42186 | 2025-10-03 04:10:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0077f1fc-7213-3ffa-a3db-3bf8f938a3b4 | -3.84365 | -41.56793 | 2025-10-03 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 516b5030-9902-3512-880c-270f324c5da4 | -3.09251 | -47.02248 | 2025-10-03 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| ff02c754-fc5a-362b-94f4-e18b6c97f30d | -7.78167 | -42.50105 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 175aad8f-985f-3200-a2fd-c18a96eba639 | -7.80304 | -49.86485 | 2025-10-03 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fde40f4f-81a1-3194-9dc4-31b115986ee9 | -7.77712 | -42.57234 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5a1f2a11-c3e6-397f-b89f-465272c091ed | -5.90783 | -43.90458 | 2025-10-03 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9536aa81-efeb-37f0-a45b-57706a10454b | -8.24561 | -47.04115 | 2025-10-03 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ca80ece-598e-3b32-9a10-31c77558e068 | -4.66452 | -45.78698 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a70f0d0-ed44-3b0f-b21b-3b8c500f1db4 | -5.91728 | -44.26866 | 2025-10-03 04:10:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1dc257df-59e5-3769-b3c2-dd53372e9f8f | -6.64453 | -43.59303 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f9e6843-b795-3470-aaef-640b88630c53 | -6.22642 | -42.93884 | 2025-10-03 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8987d6e2-e9c8-3f26-9522-f5548729b904 | -4.66207 | -45.80181 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 19.4 |
| c24fa9ca-f49a-385f-b138-1289610d4d44 | -7.75764 | -42.56561 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5856f0a4-0ac9-3224-bf45-330c07466d27 | -6.68687 | -42.83389 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 42f2fde4-d02e-3193-8671-5b3d946356af | -4.66918 | -45.80787 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 1fe2ef49-ecdf-34cb-9d37-bf08ecd0a0a0 | -7.24987 | -49.40818 | 2025-10-03 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92e1ebd9-4673-3222-b64f-501a4b8eb935 | -5.47474 | -44.69511 | 2025-10-03 04:10:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| edf218af-b01a-3c0f-9853-b80a0085368a | -6.37784 | -43.87812 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e26c2c03-9b7f-32c4-bcda-252bbd0b8731 | -6.37721 | -43.88198 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6bcc857-220b-3d68-9834-9becd5d0c4b4 | -3.30824 | -44.90223 | 2025-10-03 04:10:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8db576a-b0af-3957-a7ae-d2665a43c0fb | -7.72592 | -46.23362 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f925a3af-8950-37de-b0d0-2890f10d4cd1 | -0.90996 | -47.55067 | 2025-10-03 04:10:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd607ddc-bb91-3c95-b5d9-58e1f2cecdb3 | -6.28496 | -43.63245 | 2025-10-03 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3967779-1553-3806-bc19-a24d28ec11c4 | -7.76927 | -42.59998 | 2025-10-03 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 76adb01b-8dba-30a6-aa07-d41611a6a7b8 | -7.30453 | -45.26013 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ee29d4b-b697-3dd2-a969-c549366661c9 | -4.67396 | -45.80346 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf07fd97-58d5-3efa-acf5-1d443ea0abd4 | -6.79906 | -44.7469 | 2025-10-03 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d9b3797-ceaf-33d6-b682-e364f07ea3ad | -6.10223 | -43.2105 | 2025-10-03 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1e518fc4-4ce3-3c5e-a7c0-4227102b7353 | -7.49872 | -48.85819 | 2025-10-03 04:10:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c94cd81-9ae6-3c36-9b45-7d7bcc482b00 | -6.28409 | -44.05565 | 2025-10-03 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a959695-9483-340b-a2e5-fe5864528cc9 | -4.67244 | -45.7881 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea690ca7-ad5d-3b8a-890d-6a67ea762e39 | -5.64095 | -43.90491 | 2025-10-03 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d40b55ca-a83f-3ca7-ae03-41b094284457 | -6.30257 | -44.42677 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b83f2bf6-72ea-3a54-9b53-fde12bfc662d | -7.77255 | -47.37765 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2144f852-0e45-3df1-8542-a2d74c3bb16a | -8.45295 | -41.89514 | 2025-10-03 04:10:00 | NPP-375D | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1b2705f7-88b4-3192-85d4-788ce12b53d7 | -6.59793 | -44.32435 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f9fd558-83c6-3a51-b70d-ae41942674f9 | -7.7538 | -46.25763 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| a9588f2b-dae4-3934-b385-3919539b4acb | -6.35065 | -43.2947 | 2025-10-03 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c4c9bfc-81b2-3578-979c-e6ee929640e5 | -7.75092 | -42.58618 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9afe60bc-50ab-3952-9ee4-e19a9a5ff5bb | -6.04381 | -44.61586 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 95b438fb-fef2-3928-bfe9-f801cbb63c43 | -7.76271 | -42.53399 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3b5ea7da-12fa-337d-82b4-91f84f44699b | -6.56017 | -43.891 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36abdf1f-f377-39bb-8c88-c2274609480e | -8.23228 | -39.02334 | 2025-10-03 04:10:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6ac17544-3e59-36c1-a1d2-243c5af9c993 | -6.66275 | -42.81188 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a732f5b0-3b47-3b3f-8256-b9b9332e3d36 | -5.62786 | -43.91872 | 2025-10-03 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eed45600-ceb7-3eb1-aba7-ecae62ef696d | -5.64383 | -43.90939 | 2025-10-03 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79e786e8-8624-3ff8-8f00-ac394d589fd5 | -4.65248 | -45.81066 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a9bebe7-4921-39e9-9430-fe8c2af531c3 | -5.31936 | -45.28433 | 2025-10-03 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |


[Clique aqui para ver as próximas entradas](README52.md)
