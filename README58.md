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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ce4d9ea-791e-3a64-8654-aa7443f03c1b | -7.38638 | -56.69022 | 2025-09-06 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0a54d69-2a03-3bcd-9b68-0e49ed5ff2b9 | -9.01751 | -49.79763 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 059a5f2a-b436-38aa-8cce-1fa6188bb44b | -5.49212 | -42.15284 | 2025-09-06 04:38:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a86ab369-fc6e-34b3-9110-c0dc751b8a84 | -5.8711 | -52.1671 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb538ddf-b88e-3e37-9071-56e54ee5e8ab | -5.91079 | -57.72943 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 58618810-5ea2-3c55-9b71-bf0c263e282b | -7.27657 | -43.70109 | 2025-09-06 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cfc19bd-f925-3d07-96b3-4c7f588e2ea7 | -6.82894 | -51.87339 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbe8db9f-766e-3857-8736-867406b8ae23 | -5.98015 | -44.72937 | 2025-09-06 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab8a809a-8b9d-3b00-92b5-bce5058c18cb | -5.74709 | -42.75723 | 2025-09-06 04:38:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cad60367-d243-3b81-aa5e-a4bfd08059c9 | -7.32649 | -48.49655 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5b88047-a28e-39aa-af69-566e45904cc3 | -3.24267 | -50.80489 | 2025-09-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a7dc2a2-16c4-3625-b9f9-2860b0fb90af | -6.01757 | -46.68989 | 2025-09-06 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd6302ed-d9cb-3cd0-ae3d-86b3af9f3525 | -6.5371 | -49.50358 | 2025-09-06 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d99cda53-195f-34db-a2d5-1085e564a81a | -3.80358 | -50.03362 | 2025-09-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd9d9d5e-f9d6-3aa3-ba85-f4db5ea54cf7 | -4.80026 | -47.26091 | 2025-09-06 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3446621-b4db-3157-a766-55253ac1d256 | -6.86198 | -44.26197 | 2025-09-06 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a18c37a-e076-36be-b765-d61964b434ad | -6.26713 | -43.49646 | 2025-09-06 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75211ff1-6616-3977-af1e-5eb9a8b55578 | -5.68839 | -48.13477 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b6ab5ba-c834-337e-985a-28161e03489f | -9.0796 | -47.01805 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 8f60e11c-3581-3479-b533-e7aac49a2e7a | -6.16476 | -43.19097 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8c23a2ff-602e-3ae7-b09a-6dd4ce702922 | -8.15813 | -54.92397 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ecc61ab-fe76-361c-b732-6e26f57fa6df | -6.26846 | -53.42449 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 130e7872-0791-3b4c-a2a4-e939404d9f2d | -6.54095 | -49.50064 | 2025-09-06 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce81e12e-4895-30ce-a55e-d0595a10584a | -5.76003 | -53.77268 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7d35fa6-b137-3538-88af-bad093f6e5b6 | -8.34902 | -52.54729 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7ba8765-647c-3c01-bfcf-60d4585796c8 | -5.95066 | -53.78892 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e444ad37-2b57-3cb1-818d-ecd00ef8c92c | -3.79302 | -47.58173 | 2025-09-06 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2ac84fc3-9f22-3e04-84be-9dc82417ad99 | -8.37622 | -52.5357 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fda08ab-3424-3f3f-989d-5564fc20d0ef | -8.49284 | -45.0673 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46aad9c0-7f3c-376d-8cd8-fe0cacbbd78f | -5.79029 | -45.64285 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76d897ee-abad-314c-bf1d-ba9fa8f2771d | -5.94844 | -53.79644 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3cac160c-60cb-32b8-a83f-eadc29287fce | -2.47192 | -47.77367 | 2025-09-06 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9dc9ce4c-eb08-3a7d-8e27-c1d599dd113d | -2.91132 | -48.6734 | 2025-09-06 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be1321ec-19e9-3c33-a6b9-b90930d11f71 | -5.9881 | -44.72789 | 2025-09-06 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e4c33c43-0d1e-3cc4-93f1-cf9884b03090 | -5.1027 | -56.1459 | 2025-09-06 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8961dba1-3ce4-32d6-b2ec-655adca8f171 | -3.16007 | -48.60349 | 2025-09-06 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48fbacd9-a5d4-3fbf-b146-3a39196b8504 | -6.81218 | -52.81227 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2f5bb920-66fe-37f8-8e42-68b1a59bd619 | -8.1011 | -45.33608 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d1f40502-fc95-34d5-b950-79c85e1821f8 | -8.05413 | -52.37997 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4325e45-c8b2-3e2b-91ee-4941c5eb85f5 | -8.76786 | -49.63643 | 2025-09-06 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37986c80-acde-3caa-9c7a-2f72f918456a | -7.83722 | -46.21031 | 2025-09-06 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0e6d4b7-b45a-344b-a0d2-2c97c2f3a76b | -6.16537 | -43.18684 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 371afbce-3450-36a0-a3bd-5722000a3278 | -7.05495 | -50.865 | 2025-09-06 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e066a1d-3ccc-3636-9626-a3623f502408 | -5.96829 | -53.60141 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 45ddb161-c56c-316c-9e5e-4a40070f84d2 | -3.67974 | -49.01318 | 2025-09-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07db061e-65ce-3e39-bb75-430e916cb455 | -4.45684 | -44.14227 | 2025-09-06 04:38:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c33afa7-d000-3d34-aa92-6d92e087354b | -7.7289 | -50.32267 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 33ed2393-0716-3267-8427-c5e1657452ba | -8.03856 | -44.06879 | 2025-09-06 04:38:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a5bee3d-367a-35b8-9efa-5d00c05a3138 | -3.32732 | -54.90924 | 2025-09-06 04:38:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49ff78af-dace-3f40-8579-83d18a15f156 | -5.84454 | -44.11885 | 2025-09-06 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed7e4e42-bd19-318f-bb10-690e983e2126 | -2.47138 | -47.77715 | 2025-09-06 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b890923-cf87-32d6-b761-48f220adaa18 | -6.91463 | -43.81409 | 2025-09-06 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d34fbba-19f5-311c-8150-95b4305a81fb | -7.07497 | -43.86861 | 2025-09-06 04:38:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d77375e2-d85d-3b56-9033-8e8400ee60ce | -6.14731 | -43.18818 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e8aaacb1-071b-32f1-8482-01fcd4255535 | -4.27164 | -48.18587 | 2025-09-06 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6740f8d9-60c1-30f0-92bc-82fb798f2fa1 | -8.88143 | -47.25241 | 2025-09-06 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1eabf92-338b-36b7-bd2e-edd6dcfad3f0 | -8.06952 | -52.37393 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f918f0ae-d7eb-37c9-a704-012d3fc54c29 | -9.08637 | -46.99759 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 29724eab-a9e0-3e64-89c0-63d188eac9f1 | -5.82031 | -47.77375 | 2025-09-06 04:38:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46f9ff13-493b-3a61-ad3d-96074da26549 | -3.75437 | -49.0567 | 2025-09-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11dec4a1-57d4-3e69-9888-d428026e6e90 | -8.07402 | -50.20271 | 2025-09-06 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e964d9a-5491-3846-bd79-cf9382c7b67b | -7.30526 | -43.73307 | 2025-09-06 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8da55b8-4f21-30ab-866c-8c765f025e21 | -6.00813 | -46.70463 | 2025-09-06 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0abeec59-9420-3e04-9bde-d65e40ab8544 | -6.28279 | -53.43159 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8dd617e1-dac4-349b-bd4f-c28f02ef7398 | -5.83746 | -44.11044 | 2025-09-06 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 284d1e5c-ef93-3a05-aa8e-08d683f29e8d | -6.18074 | -53.2528 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eea0ef23-80cc-36cd-8870-74663da758e5 | -4.01137 | -48.93454 | 2025-09-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ea96b921-2717-3ee6-a594-16215e9733a7 | -3.48038 | -48.94282 | 2025-09-06 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66afe5f6-f2f3-3757-9fb4-eb8beed79141 | -6.21108 | -42.62175 | 2025-09-06 04:38:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c15f1606-a6d6-369a-9a5c-6978f72b5a5c | -7.06224 | -50.86242 | 2025-09-06 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 265b1545-04ff-37c9-947f-afb63904ab44 | -7.72447 | -50.32913 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7c823b3a-6cb8-35f4-9563-f614e39e45e1 | -5.73103 | -43.90425 | 2025-09-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98a510d5-b4bb-3026-8efb-60815f3840e5 | -6.21769 | -43.53489 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c5bdbd5-60f2-3936-89a4-af191beff01e | -8.3459 | -46.94999 | 2025-09-06 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9878d3d0-eea1-3171-bccb-2f35fd4a4ca0 | -6.73718 | -51.96551 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8af0de8b-e17f-379c-b0c2-2fe0677bea70 | -6.54182 | -49.5183 | 2025-09-06 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39efb93d-1f69-3bd4-8132-369123723c26 | -5.98514 | -53.59451 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cf473d4-7e66-3625-b4e7-9d865a5dcbf0 | -5.72587 | -46.44384 | 2025-09-06 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b3d177e-1641-3498-bd33-1729e5ad3aff | -8.37229 | -52.55952 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02e55745-c8bf-3a5e-9010-13f0ee51f350 | -5.91228 | -57.72071 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2252d9ce-eec5-3212-9b91-881708438668 | -4.61144 | -41.5428 | 2025-09-06 04:38:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fdb553a1-33ca-3399-b1eb-cad23ef50c73 | -8.89065 | -52.05222 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 658c9262-5b97-3f3a-85e3-766d83b26658 | -6.54041 | -49.5041 | 2025-09-06 04:38:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 709a08c0-f26a-3150-9af2-bc6e33fe41a0 | -9.00648 | -49.80302 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d050c5a7-1270-34c0-821f-db94b9e570ce | -7.67926 | -50.29288 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b4d99fd7-aac0-345b-9d85-7b73441597c5 | -7.97988 | -44.51154 | 2025-09-06 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72785907-bb76-38f9-acd0-d2bdd669c0ee | -5.98199 | -43.61049 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 55fda71f-6c14-3970-a988-c1bb349bb95f | -6.15105 | -43.19314 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ed34491e-4b43-320c-bc44-374c98da07b3 | -2.56532 | -48.97181 | 2025-09-06 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05336a31-7185-3fc1-b5ed-f9a5092b31fd | -8.90605 | -45.11311 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b50632b-89f4-35ab-9449-f2b7e377a6f1 | -6.40262 | -46.08971 | 2025-09-06 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 377adc68-17dd-3157-9cb5-4a573f5a045a | -3.96391 | -43.23943 | 2025-09-06 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfc3f9b0-f01e-3923-b8ef-981b23d411a7 | -6.21285 | -43.53816 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9baa4369-a21a-3210-8aae-fc58f766e600 | -5.99615 | -44.15968 | 2025-09-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d76ca92e-14da-33de-b024-b17a15bdd73b | -6.01285 | -46.69728 | 2025-09-06 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75b98c80-14c8-3111-86b6-718358a7c102 | -5.79382 | -47.78814 | 2025-09-06 04:38:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7763064e-66e2-3731-8702-655bc86bbebc | -7.3332 | -48.49754 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3409a704-b571-396e-9b7b-a7ef0c090c3e | -6.32546 | -58.17544 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52cb6cb3-3bd9-3f09-ab8c-2e51ea569676 | -5.82633 | -46.35984 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bdf1964-6be8-3638-a18b-d167e32a461a | -6.38504 | -43.00482 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README59.md)
