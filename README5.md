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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2768ca5e-1ca1-3fe3-9c85-d67e560a4782 | -8.03226 | -54.85686 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a86a8ead-6065-338e-9689-7aa0aac04ebf | -2.93465 | -50.38832 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9b3bf267-d193-37c7-ac59-c1643884c25f | -5.86548 | -46.22662 | 2026-09-13 00:05:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| c3487da9-1b0f-30b9-95c6-4974fb222a80 | -5.85046 | -52.1121 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 25028fda-9d74-3f86-80de-130fe6949fb4 | -5.61518 | -44.83723 | 2026-09-13 00:05:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7d7c2070-4a4f-3e83-b918-05f6d7427f28 | -6.78858 | -48.66727 | 2026-09-13 00:05:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 276a4272-74df-3337-b6a1-d64b775b0b77 | -8.12845 | -54.81632 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 54c1ef0d-56d9-3d52-a21c-3173b794dd00 | -8.4032 | -47.69548 | 2026-09-13 00:05:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e4c52912-429d-372f-8bb3-25788add29b6 | -8.32267 | -49.69043 | 2026-09-13 00:05:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| b96ae818-2e63-32a5-99e3-78507330f23e | -3.91385 | -55.73394 | 2026-09-13 00:05:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 66485947-012d-3994-ac03-d79538ff9211 | -2.54242 | -54.66846 | 2026-09-13 00:05:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 7be91d09-fb6e-3ec0-bf72-d039b126947a | -8.21472 | -47.86452 | 2026-09-13 00:05:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 192e280d-36a0-3e73-8378-9abc9d5be1c8 | -3.82003 | -48.99914 | 2026-09-13 00:05:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6a15ba9e-3ae9-37a1-8bc3-ec3c7e1cc82d | -7.37705 | -46.04417 | 2026-09-13 00:05:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a12dd417-c37a-3a44-bd0d-ab9af163baa5 | -6.3849 | -55.24285 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| bff6bcde-2f6f-3933-9055-decb04b885e0 | -8.11751 | -54.80817 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| ec483eb8-6333-3315-9501-ee85512807b3 | -2.61597 | -54.76718 | 2026-09-13 00:05:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 0774df62-3ab1-3387-a417-b70c400ac268 | -7.32778 | -49.76361 | 2026-09-13 00:05:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5885d6a3-9e8a-30e0-b67f-f9b22bc77194 | -7.28343 | -50.7854 | 2026-09-13 00:05:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4fd699ea-615a-309d-8181-61628df870f2 | -8.115 | -54.80203 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 66bdfe0f-a978-3fef-8eb5-5786506b42a5 | -2.95347 | -50.39464 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3ba812a9-5f37-308a-b658-5d89372b69ce | -6.0811 | -57.86591 | 2026-09-13 00:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| ddf02644-b832-314c-ae15-444122696229 | -6.72513 | -50.46672 | 2026-09-13 00:05:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e59a2d15-a695-3c10-ac44-fa39bbf21be5 | -6.2357 | -51.68768 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 4d026a58-68f9-3713-b379-0e69e6da0d64 | -5.16824 | -49.35038 | 2026-09-13 00:05:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 4495a053-63c8-3f33-bb1a-db62d1a973d5 | -5.02722 | -49.99017 | 2026-09-13 00:05:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 125ef330-d409-3d57-82e3-f1ca676740ca | -7.96183 | -43.99823 | 2026-09-13 00:05:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 34635b3d-d1a7-3f27-afe1-690d81b96027 | -6.84905 | -55.57162 | 2026-09-13 00:05:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| e84977c5-6328-332d-bab8-3dc271faff87 | -3.33135 | -42.28237 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| b7ed9ca2-da00-30a5-bd2c-cd2dc75590df | -3.4093 | -48.89788 | 2026-09-13 00:05:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 58f1ff3a-e0e5-3693-8b90-4d98704314cb | -7.17417 | -45.87352 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9c55ce42-feb0-3cf8-a2e7-06415a68fdfb | -6.00471 | -44.27256 | 2026-09-13 00:05:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| d33dd6e2-af93-38f7-adc1-02239d8f542f | -7.16737 | -45.86726 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 6cd15804-5cf4-3702-924f-2b8ec2c5b33f | -6.11531 | -57.68475 | 2026-09-13 00:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| be853ea4-032b-3daa-93bb-2e5d914d9636 | -2.96349 | -50.40219 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| c3b3813a-8c00-38f0-bc5e-0f9fe3536be8 | -2.96227 | -50.39341 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 306d43c6-a13c-34bf-9d52-55c130866e28 | -1.38043 | -49.42144 | 2026-09-13 00:05:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| f9dd502f-0856-33fb-bf5a-e01544e9647d | -3.33366 | -42.30584 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 6920bc3a-8d99-3d7d-b2b9-f2605a7b4d93 | -6.72634 | -50.47557 | 2026-09-13 00:05:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 72d3d789-7718-3ca3-815d-6e975a267207 | -6.85313 | -47.44465 | 2026-09-13 00:05:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 457ab9e1-c548-3b33-8525-2aead8ca9d8d | -1.23184 | -54.1265 | 2026-09-13 00:05:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 17869d23-5861-345a-b0d0-1b1f64fd14de | -8.05255 | -54.84859 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| f33c6fe9-79b5-311d-9aed-0fd091277a6b | -5.49557 | -49.50813 | 2026-09-13 00:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c0aa39c3-ab56-39b0-b300-125824448f56 | -5.61757 | -44.85367 | 2026-09-13 00:05:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 42bd073f-2fcf-3fc2-98cb-afef5c29abec | -2.66596 | -57.50922 | 2026-09-13 00:05:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| b5a9325f-bb2a-39fc-87e9-5687731883ef | -6.23696 | -51.69712 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 6bb977c3-a4db-3915-95ee-c581ff35af14 | -5.80765 | -53.8016 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 0c1762ba-96cc-339b-9df0-3324aeea0ef9 | -4.46283 | -50.16897 | 2026-09-13 00:05:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e1b87abe-d449-3b7b-ba99-9d83cca061e6 | -5.78873 | -53.81643 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4c601bfc-adda-37d4-aa2f-8927467c33b5 | -4.60104 | -46.32674 | 2026-09-13 00:05:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e6561270-a906-333d-8f0d-9f726815b1f0 | -3.40013 | -48.8992 | 2026-09-13 00:05:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fd655967-f2a6-3e80-8b68-dd58cfe54428 | -7.37525 | -46.03164 | 2026-09-13 00:05:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8493a6d6-4d7a-3703-bf15-e23e88095256 | -2.95832 | -50.42976 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a879a724-d0ca-3a3c-bbc2-a631631c889d | -8.42951 | -46.03939 | 2026-09-13 00:05:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3eebda1f-4f56-3f67-aa15-8b017a97c00d | -7.02251 | -44.64239 | 2026-09-13 00:05:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 561a12f2-8e48-3edf-8845-f9175dd394af | -7.36846 | -45.34669 | 2026-09-13 00:05:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 173cd7b8-41f0-3f31-ad9a-2f412a5cccfa | -8.05452 | -54.8643 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 03dea37d-6f33-33b4-a671-a4e8df522dfc | -6.10989 | -55.66893 | 2026-09-13 00:05:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 556c64f1-062b-3598-b183-9bb3da296116 | -7.53277 | -47.34373 | 2026-09-13 00:05:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 43f7166a-ad6f-38b0-8d72-11bf2665bacd | -2.9793 | -57.21479 | 2026-09-13 00:05:00 | TERRA_M-M | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 47804f66-64f8-3788-84fd-9a5ed7b7fbba | -6.59686 | -58.85384 | 2026-09-13 00:05:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 3123fdd0-e7be-344f-b5d1-851bd7e71dde | -7.62403 | -45.98888 | 2026-09-13 00:05:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b4b68462-2be5-3ae2-b9d7-5fe9f249006a | -7.14904 | -44.71264 | 2026-09-13 00:05:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 291317fb-88f0-36c3-b1f0-f684f05c3d82 | -2.6688 | -57.53003 | 2026-09-13 00:05:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 197.0 |
| 5aedee5c-0178-3d75-9c38-ede705a09a08 | -6.70599 | -55.41406 | 2026-09-13 00:05:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| df378132-137b-3109-a0af-d439c99c2dc4 | -1.19292 | -55.72168 | 2026-09-13 00:05:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| eb66b7d9-54e5-3f0a-a24c-4b15f0432dab | -1.72703 | -55.84907 | 2026-09-13 00:05:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2239beb1-9047-30a0-9945-216e79e20779 | -3.3293 | -42.27728 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| cedd6f25-57b6-3593-b67f-c1803e5484b2 | -2.8651 | -49.62538 | 2026-09-13 00:05:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 49affc8e-e2c5-3e20-9002-7507d6983904 | -8.04103 | -54.85006 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 5caa16f9-d7a6-3d2c-9763-41b395133def | -3.38993 | -50.75553 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 98acebae-37d7-3df9-b191-9a6ed18b59e5 | -7.59128 | -46.97114 | 2026-09-13 00:05:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c1654d2b-42c6-3127-8d6c-fa3e6b12da8f | -6.85119 | -55.58872 | 2026-09-13 00:05:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| da2babbb-18f5-3c5d-8839-c9c5c7690a81 | -3.84964 | -50.6164 | 2026-09-13 00:05:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 29dc794a-76aa-3d73-b811-78c15f43eace | -6.06687 | -57.86804 | 2026-09-13 00:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| e82be985-eb37-334a-aae9-0496507c578d | 0.17209 | -51.478 | 2026-09-13 00:05:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b1e352f2-2578-38ad-b12a-3ccbc7a9b842 | -7.15139 | -44.72847 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 4421ed69-34a0-3e7f-8c3d-0a1966f98bf7 | -3.16537 | -48.60714 | 2026-09-13 00:05:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b39b2cae-b26c-37a2-ad68-f6a23f7e7ee7 | -2.94345 | -50.38709 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 91c0f9ef-302a-3229-8d90-26642cbf09ac | -4.39083 | -42.33425 | 2026-09-13 00:05:00 | TERRA_M-M | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 1918185b-25ea-3d97-925e-1027cc8f0f98 | -2.94709 | -50.41344 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 97f6c601-28dd-33c2-9253-d7e52755ccc1 | -2.4702 | -48.04188 | 2026-09-13 00:05:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 237b616b-c6f2-31e6-b35a-72e82ffe63a7 | -2.93919 | -50.48607 | 2026-09-13 00:05:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c85d4a1f-9bc3-322c-8298-fe38a305a122 | -4.9311 | -47.7106 | 2026-09-13 00:05:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1e63a0c8-6f36-35e9-b896-a9dfbc80817e | -3.16676 | -48.61703 | 2026-09-13 00:05:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| da354b8f-56eb-3184-afe0-ebf28b5e8e99 | -8.12649 | -54.80055 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 3fcfd194-41fa-31eb-a98b-631b1d5484b1 | -8.55061 | -54.71589 | 2026-09-13 00:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 7e460342-7b1d-380e-8a05-87b564e320c4 | -5.17899 | -49.35173 | 2026-09-13 00:05:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| f046e708-62a2-3494-98b6-4f97d80e4388 | -5.18789 | -49.35045 | 2026-09-13 00:05:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 8de15349-19aa-360c-813d-f1e2a41dd193 | -5.01963 | -50.00021 | 2026-09-13 00:05:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 1ff7a474-f78c-38c0-aaa8-b05afcb390be | -2.59879 | -54.71813 | 2026-09-13 00:05:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| e9931c4e-84de-3455-a8e5-5b97bccc5da7 | -6.22913 | -51.70446 | 2026-09-13 00:05:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2c19732c-6ae1-3974-86f9-bdaef4a971af | -5.96505 | -57.78402 | 2026-09-13 00:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| b47d36e6-f143-3ee3-a711-21bc59a009b8 | 2.6741 | -51.04326 | 2026-09-13 00:07:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a05e877b-30c0-3b15-af45-22292841b746 | 2.51575 | -50.8534 | 2026-09-13 00:07:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4d0b6846-3261-3b3b-b5ef-0232cbdd955c | -8.6005 | -44.4378 | 2026-09-13 00:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 7bcaa613-fa93-35db-b655-100f3a99e8cf | -10.5286 | -51.3597 | 2026-09-13 00:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 65bec67f-f5d5-3df5-b0c2-e55051ff7ae2 | -10.9707 | -58.9642 | 2026-09-13 00:10:00 | GOES-19 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 6cbab7ce-196b-3860-a973-7153d8cd1003 | -5.8206 | -53.8052 | 2026-09-13 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 84f6a2ed-0a02-3e62-a548-a450f68c035c | -12.8736 | -44.3828 | 2026-09-13 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |


[Clique aqui para ver as próximas entradas](README6.md)
