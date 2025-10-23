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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8b952ee-5384-3d3e-a409-c4fedab42d74 | -8.62269 | -44.81126 | 2025-10-23 04:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dfba5c7-4919-3751-9c59-1c96dbba7aaf | -3.42139 | -50.36519 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 419fe08c-1a1c-34b5-a9af-ab7204d53515 | -2.98094 | -54.00078 | 2025-10-23 04:36:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb5c1cec-ec87-35cc-bf22-0aad4ad3d8b5 | -2.81547 | -49.13326 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0a6d7c9-c97f-33a7-802b-64196fc2cefe | -6.96657 | -44.00855 | 2025-10-23 04:36:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cdf68fb-2ee9-37f3-9fd6-b34402e12f83 | -5.29225 | -50.56829 | 2025-10-23 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b3e1dfe-2f48-3031-9c7d-bfc8257361f1 | -2.92926 | -48.30824 | 2025-10-23 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 681fb381-db78-3345-80d0-4cfc032a800f | -4.20302 | -48.3592 | 2025-10-23 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e56bc676-ca8f-322c-bfe0-4ab715c52cc0 | -3.14973 | -49.47198 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f9735bb-e03a-3baf-98bd-13fdaa8a727f | -4.93879 | -48.30666 | 2025-10-23 04:36:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bbcdd01-8082-346a-ae51-e821dd59de32 | -2.80556 | -50.27448 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afcdc148-c05f-30ca-855c-67b11a4aa368 | -5.69336 | -45.9705 | 2025-10-23 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d900c093-f746-32a8-bf21-388d46dbb27c | -3.39813 | -51.49947 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 289c2710-c92e-3167-9856-3bf66016f3ab | -2.80604 | -51.35317 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99dbb090-9312-3847-8625-e5753aa2a1bc | -3.21428 | -46.80309 | 2025-10-23 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c377a280-3868-359a-921b-808ccde80929 | -3.80405 | -48.63159 | 2025-10-23 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0df0fdbc-e244-3274-8d5e-77e60fe5d668 | -9.23779 | -45.60187 | 2025-10-23 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a0b229f-91af-32cb-9da5-bd07f5a521cb | -6.85335 | -46.29631 | 2025-10-23 04:36:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5d6f2b10-e487-3892-a763-be8d35ed9a13 | -3.11601 | -51.20956 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a837352d-9f95-3bc5-8c42-3f01304b9f48 | -6.85677 | -46.29684 | 2025-10-23 04:36:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 97b26af0-be53-3578-b7c3-ef6f85ff3f07 | -5.32534 | -48.17482 | 2025-10-23 04:36:00 | NPP-375D | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| badd28a6-1b3d-3969-8e7a-65f675e8d074 | -6.59997 | -44.21894 | 2025-10-23 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7e924f45-8971-3966-989f-601f85a4f440 | -3.59748 | -49.85373 | 2025-10-23 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 49919747-8d57-3f1b-a8a3-6b056e3c0e75 | -6.85733 | -46.29315 | 2025-10-23 04:36:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c7cbf271-5e6b-36ac-8f7e-3066bed388cf | -7.32445 | -45.28308 | 2025-10-23 04:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07089bbf-c577-345c-803a-4d801f60dc62 | -3.38557 | -50.26616 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6006372b-7aa2-3553-9395-47f20d26fd02 | -4.27987 | -48.19189 | 2025-10-23 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 470b21b0-4dff-3fdf-8ef5-a1b702cd25ac | -3.22522 | -49.36606 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 79c02c6f-b46d-38ec-a367-2e18c1d38e2a | -7.27528 | -46.16605 | 2025-10-23 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0fba756-5741-37fc-bd56-f88eae699be5 | -3.03694 | -49.43469 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25e08e3a-0d62-33db-a53d-f9a9e2d0e25c | -6.90752 | -46.12663 | 2025-10-23 04:36:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ecf1b77-cc0f-3065-902f-abdf8124ee04 | -6.69746 | -46.6522 | 2025-10-23 04:36:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02540ffe-c6ea-3c23-829f-c8e519b3ae42 | -9.35759 | -46.24315 | 2025-10-23 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 938cecf7-b468-354e-811b-73abf4886720 | -5.69051 | -45.96629 | 2025-10-23 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5c2d85cc-5e2a-3eb9-ac63-2d1a366e6d72 | -2.86265 | -50.73935 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 314d63fe-89c7-340b-a0ad-a64d1da3a330 | -4.89023 | -39.80737 | 2025-10-23 04:36:00 | NPP-375D | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| f90b87ce-a62d-3527-bf4c-f249a5178372 | -6.64605 | -43.60704 | 2025-10-23 04:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 87453974-4cc6-3422-a013-b40f371cf707 | -3.22583 | -49.36228 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 26ad28e1-5866-3d88-83e9-9994dd1b21ee | -6.32462 | -43.62254 | 2025-10-23 04:36:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d88dad61-823f-382b-9df1-18028433b62d | -2.90588 | -48.98719 | 2025-10-23 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bd6783e-0ef8-3c16-96e8-d724176b94c2 | -3.6792 | -47.63012 | 2025-10-23 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 98b8c80d-9cb5-3be7-bfbe-f90d9fcce5c8 | -6.72993 | -44.15155 | 2025-10-23 04:36:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b4d4406-1e37-34b8-8132-7dd89ee9a763 | -2.87054 | -50.71357 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00f9e8f1-d00c-36d9-b1f6-5ebc5e8d969c | -6.28533 | -47.01461 | 2025-10-23 04:36:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1232d3ad-70e4-350a-a94e-d04086628082 | -3.01912 | -49.47907 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c6a98817-23bf-3d29-8958-628c4b5a59da | -5.85024 | -43.64841 | 2025-10-23 04:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e22696f5-83a0-3143-b7aa-91ea5a44fd48 | -7.80826 | -44.00258 | 2025-10-23 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f327e973-26be-34f8-8cc3-c5f7bc4ed487 | -3.32874 | -50.22403 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b119f500-f411-35f7-b9a8-0270b5d29575 | -6.09743 | -48.18708 | 2025-10-23 04:36:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffebbf4e-c0fc-3fe9-bd7e-c4a0e76c76ad | -3.16512 | -48.60847 | 2025-10-23 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60b7f1bc-69df-34df-b61f-f89eb50cce46 | -3.05048 | -48.71284 | 2025-10-23 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a10d1594-6585-396e-80b2-66580dfc56b4 | -2.9259 | -48.3077 | 2025-10-23 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e2b0447b-e605-3d16-8044-a8fc76d5ed42 | -3.39479 | -51.50093 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95395f92-6d7e-3009-8a3a-b09721c335ef | -2.86985 | -50.71796 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52e6fd71-2a70-32c2-92ed-4dcd3ab72ff3 | -4.63972 | -49.54175 | 2025-10-23 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b8db195-14eb-3cf6-bb10-30d59e474fbf | -4.57946 | -50.16473 | 2025-10-23 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 809c0634-a596-388d-8993-246921406567 | -2.79864 | -48.89119 | 2025-10-23 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd3a3f10-2867-3f97-9b8d-698d55491953 | -3.69776 | -49.56374 | 2025-10-23 04:36:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9fae2b38-0982-3938-96e9-61ade0a43720 | -3.14778 | -50.16436 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca8866af-6fab-30ba-9431-064210c51bde | -3.47522 | -50.07594 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96a15e53-b3f3-35c4-9553-b2e27c23efd3 | -7.32742 | -45.28767 | 2025-10-23 04:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dca78451-da22-332b-a456-6a46d8280145 | -3.14713 | -50.16847 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df0c9873-e2e0-33cc-aa8d-e9c065999b06 | -7.51692 | -46.8807 | 2025-10-23 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7100306-fa12-3b55-ae1a-1a3b51bdcaf1 | -7.00174 | -47.00251 | 2025-10-23 04:36:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| edfef380-69c9-3106-b33e-45b053b1400f | -4.3792 | -50.35205 | 2025-10-23 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 318c0ab3-f81b-331f-8956-f0f6ea65bf91 | -3.04216 | -49.5143 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1af83ccc-f2ef-3678-82c4-d70e533db4e0 | -9.08539 | -47.81656 | 2025-10-23 04:36:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71a28ed4-c030-385e-b6e8-df938f8efd18 | -5.04849 | -46.88312 | 2025-10-23 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a425689f-9175-39a9-8b0d-61d75ef597cd | -3.25038 | -50.12892 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0150b487-7945-33ff-bb89-ad29e2adde20 | -2.98149 | -51.33703 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dc90cc4-ae56-3069-b227-77aa29fb439e | -6.09176 | -46.23738 | 2025-10-23 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 124182e8-225a-36df-b8b8-cc10a96e5c34 | -5.36511 | -48.11345 | 2025-10-23 04:36:00 | NPP-375D | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b2c1a98-f998-3c1e-bf8d-cd9c24c3e134 | -3.99559 | -43.28283 | 2025-10-23 04:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7f2d0d2-4c6f-391f-8904-b5a343b707ee | -7.631 | -44.57116 | 2025-10-23 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fee01b6d-3ba8-3329-bfd5-cd3a11cacec0 | -7.14297 | -42.37455 | 2025-10-23 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| abfac1f4-4446-38ee-950c-313e1946e0f2 | -7.63691 | -42.20526 | 2025-10-23 04:36:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| efc5672b-4ac1-383e-8d89-c0311784e24d | -9.23481 | -45.59723 | 2025-10-23 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65cd1868-0c7a-36d3-ab8a-4e7158da3f7b | -7.18587 | -43.86644 | 2025-10-23 04:36:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ed34e6c-e20e-3158-8d08-3eda8b7097aa | -5.36882 | -46.86867 | 2025-10-23 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcd812b8-e489-32fc-ac31-6f985f3d1240 | -7.68613 | -42.23985 | 2025-10-23 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1b36b03e-c8f1-325a-b511-fddaa5e6a8cc | -6.6012 | -44.21704 | 2025-10-23 04:36:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| eb277378-3fbc-354b-b8fb-b3feda987f77 | -2.91092 | -54.29253 | 2025-10-23 04:36:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f09a112-f1ff-367f-9d6a-b378949f1d3d | -6.73747 | -44.15258 | 2025-10-23 04:36:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d11ff307-ec88-3a53-b096-f4e472f6345d | -5.88854 | -46.28814 | 2025-10-23 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f478409-f90f-301a-af85-fc89c9a69b74 | -3.13953 | -50.44701 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb0d3267-efb6-369a-a7e4-a2a3ce462d8f | -4.70757 | -47.99474 | 2025-10-23 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d73696dc-a183-329d-8516-d941e100261a | -3.14844 | -50.16026 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3475dd9-13b2-3b25-9429-6b7c1477b636 | -7.16883 | -45.17462 | 2025-10-23 04:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3f64559-2678-3aea-8724-5595c9b978b5 | -3.04566 | -49.51487 | 2025-10-23 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 522e8629-2614-3ecd-aa3c-73130ea1ff37 | -6.28923 | -47.01162 | 2025-10-23 04:36:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe10ce6c-8da5-3214-b13a-01db483103ee | -3.13952 | -50.44701 | 2025-10-23 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c456e7ac-e3e1-3f0c-a583-280980456041 | -3.45414 | -50.09317 | 2025-10-23 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a7b06d5-acca-35e9-ab12-aa64e56bd695 | -3.95311 | -46.96527 | 2025-10-23 04:36:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6549f514-0ae1-31f1-8140-e8e5f5a08ef8 | -6.85701 | -46.92939 | 2025-10-23 04:36:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9043176-fe7d-3137-8f62-ae465271a2e9 | -7.07762 | -46.19782 | 2025-10-23 04:36:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39a3f4d8-cdd9-3d55-8ba9-51434abdcd87 | -6.90351 | -46.12983 | 2025-10-23 04:36:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad5622ea-dff4-36ca-a38e-a531e875372c | -3.73758 | -51.37645 | 2025-10-23 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 230921f1-75c9-31d3-99fb-e2821fa1717c | -4.35848 | -48.72199 | 2025-10-23 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d007502-3eb3-3bc3-8bef-159523a87928 | -7.8868 | -43.54763 | 2025-10-23 04:36:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 948c3aa0-8e2e-3997-8b69-e9bddb7d2700 | -5.92734 | -47.31716 | 2025-10-23 04:36:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README18.md)
