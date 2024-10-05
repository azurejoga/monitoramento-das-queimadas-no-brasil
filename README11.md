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
| 1f2868ae-de14-3ee6-9c7f-cba47723a742 | -8.6558 | -49.0868 | 2024-10-05 00:25:55 | GOES-16 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| b7299457-a697-3020-8b45-298ac5150808 | -8.7769 | -49.9763 | 2024-10-05 00:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| b2255db9-5e87-34fd-8158-b05ad4b06eae | -8.7772 | -49.955 | 2024-10-05 00:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| f03bc3d7-5a71-3c67-9139-60a9e49f35c2 | -8.7957 | -49.9747 | 2024-10-05 00:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 457724d8-5a86-3acb-ab41-c526cd71d13e | -8.7959 | -49.9533 | 2024-10-05 00:25:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| e549b5db-8d5a-3251-81c4-06adf7875d8d | -10.4424 | -50.7336 | 2024-10-05 00:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 3e2be317-6578-395b-84bf-1da4187208c8 | -10.5757 | -64.0248 | 2024-10-05 00:26:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 66fbd63c-aeae-3456-a833-6a8e99fcbf46 | -10.5943 | -64.024 | 2024-10-05 00:26:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 94.3 |
| bc280544-0b8b-3abe-b903-7515c16bbc30 | -11.0966 | -54.2336 | 2024-10-05 00:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| f9426461-6867-3de9-94e4-908b1c769a37 | -11.0969 | -54.2131 | 2024-10-05 00:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 53222235-588c-3e0e-9db9-8b3b72ac57ec | -11.1155 | -54.2319 | 2024-10-05 00:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| b43a7f44-bc52-3ffe-a168-e583e3185bf9 | -11.6995 | -47.8131 | 2024-10-05 00:26:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 234fc98a-b764-3d1a-90ac-8d842a5d67b8 | -11.7187 | -47.8107 | 2024-10-05 00:26:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 492e8e36-89ee-394a-9d67-e31cb5df6d73 | -11.719 | -47.7884 | 2024-10-05 00:26:12 | GOES-16 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 96a12218-a020-301f-9b9f-936430622475 | -12.2668 | -45.958 | 2024-10-05 00:26:15 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 93ea9450-a8a5-3582-800d-c1a0ce86ea8b | -12.7623 | -50.5782 | 2024-10-05 00:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 142dbd0e-d7de-3403-9813-ddacb43ca72b | -12.7627 | -50.5567 | 2024-10-05 00:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 136.5 |
| c087c43c-43da-319d-bf84-fd0db8d61ba5 | -13.1351 | -51.1955 | 2024-10-05 00:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| a0731654-ebc9-3a5d-ac35-5231a847f039 | -13.1543 | -51.1931 | 2024-10-05 00:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 1b1ae2d3-dc22-38cc-bac3-4b66db8222c0 | -15.5597 | -57.4553 | 2024-10-05 00:26:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| a492ee75-8f22-3057-a79c-c01aef8eb78a | -15.5791 | -57.4532 | 2024-10-05 00:26:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 151fdbd2-3f6d-3f53-b597-19c5cc36c280 | -15.7151 | -57.4184 | 2024-10-05 00:26:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 115.9 |
| c232bb72-c688-31f3-84d9-2af457e9c9d4 | -15.7346 | -57.4164 | 2024-10-05 00:26:35 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| b1d81544-aa2f-3f82-b045-0f2664453b95 | -16.0629 | -57.5231 | 2024-10-05 00:26:37 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 4a2f79db-2691-3d70-9655-a6f8f9d641e5 | -16.0823 | -57.521 | 2024-10-05 00:26:37 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 111.6 |
| b2ed63d0-4f07-3258-835f-6be7aa32001f | -16.554 | -57.2237 | 2024-10-05 00:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 180.7 |
| 0a04abf4-67e4-3c5e-800b-9d5bbd1bb55f | -16.5544 | -57.2032 | 2024-10-05 00:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.3 |
| 9484048d-5b96-30fa-9fb3-26cbb974d04f | -16.5736 | -57.2215 | 2024-10-05 00:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.0 |
| 4d7f3ea5-b986-3fee-baee-962416eaa7e5 | -16.5742 | -57.1805 | 2024-10-05 00:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 197.7 |
| 53e8d582-2a26-3ef4-9269-b34603ae25d0 | -16.5745 | -57.16 | 2024-10-05 00:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 226.3 |
| b765a4c1-cfed-3570-822c-ad3b8bed6bbc | -16.5938 | -57.1783 | 2024-10-05 00:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.5 |
| 715dce05-42fe-3f2e-bd06-f1df222096bb | -16.5941 | -57.1578 | 2024-10-05 00:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 552e8353-c98b-3630-875b-15581dbbe1b9 | -16.6594 | -55.5427 | 2024-10-05 00:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| f180b49f-a20b-3b02-b53d-34a1fa3004e0 | -16.6598 | -55.5219 | 2024-10-05 00:26:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| 8b8619e8-f0a0-3632-aaf1-7247dc82fcdf | -16.679 | -55.5402 | 2024-10-05 00:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 5fcbc09b-8a62-306f-b836-bbcb50d7a321 | -16.6797 | -55.4985 | 2024-10-05 00:26:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 765457f1-1e80-3712-b38d-4880377c48e8 | -16.6871 | -57.4536 | 2024-10-05 00:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.0 |
| fa3f87c6-a42e-3c57-82da-5c759e69a254 | -16.7647 | -57.4856 | 2024-10-05 00:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 149.8 |
| 799b96c5-9381-3b79-8cd1-463a805b0bc7 | -16.765 | -57.4652 | 2024-10-05 00:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.8 |
| 45776f7c-a75f-3d51-9a71-347583db609a | -16.7843 | -57.4834 | 2024-10-05 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.2 |
| b25a6609-426b-3c0b-84d9-6d5c265bec20 | -17.0888 | -56.7915 | 2024-10-05 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.5 |
| d0fbf863-79e8-3e24-93a6-3449dbb100c6 | -17.0892 | -56.7709 | 2024-10-05 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 137.0 |
| 3fbc8bb3-3cd9-39c3-8bfe-9d8069b4f2b9 | -17.6062 | -43.2578 | 2024-10-05 00:26:43 | GOES-16 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 74a05e22-4993-35e6-abe1-863762eb7efb | -17.6263 | -43.253 | 2024-10-05 00:26:43 | GOES-16 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 0f3a8d3a-cce1-3c54-ae6e-a08e743eba15 | -18.2985 | -54.2231 | 2024-10-05 00:26:48 | GOES-16 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 103.9 |
| f0564648-703e-3ab4-b862-c4f4b52dbb9b | -18.4867 | -52.8009 | 2024-10-05 00:26:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 2f54bbfd-b690-3050-b85d-16ad1a6c1fcb | -18.4872 | -52.7792 | 2024-10-05 00:26:49 | GOES-16 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 102.1 |
| fe62cb14-9fb6-3c4a-9919-e7a055eef997 | -18.8809 | -43.6032 | 2024-10-05 00:26:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.0 |
| 96bf07c8-fa1e-3a93-8ef7-14ebe39f381f | -18.8816 | -43.5785 | 2024-10-05 00:26:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.0 |
| e5cff67b-cf81-37d5-8801-14a37acc664d | -18.6582 | -57.2967 | 2024-10-05 00:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.4 |
| 484c15c0-ef6f-35fe-b4a0-7a5eecce8cbf | -18.6586 | -57.2759 | 2024-10-05 00:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.8 |
| bc6640ef-e448-341c-8631-d8a981b52a2c | -18.6782 | -57.2941 | 2024-10-05 00:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.0 |
| d06c2781-f586-3a6a-a239-f8ae67a31ae3 | -18.6785 | -57.2734 | 2024-10-05 00:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.4 |
| 5e862e4f-f341-384f-8105-bd542b305a5a | -18.6981 | -57.2915 | 2024-10-05 00:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 79427b00-9a8e-31ef-851b-932e44406306 | -20.5904 | -51.3907 | 2024-10-05 00:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 156.0 |
| fe4cd6e0-9f27-39b5-a317-dd990e95e4cc | -20.5909 | -51.3683 | 2024-10-05 00:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.0 |
| c37458eb-a78b-3591-b504-3099da68c101 | -20.7901 | -47.7465 | 2024-10-05 00:27:01 | GOES-16 | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 07bea8c9-e6ca-356f-87fe-8a3418a6c16d | -1.1942 | -46.5935 | 2024-10-05 00:35:13 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| da43772a-0da4-379b-bb1b-e286cf8a8120 | -2.8829 | -50.7147 | 2024-10-05 00:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 063f8d9a-09da-32ac-888d-2e81362e829d | -2.9014 | -50.7142 | 2024-10-05 00:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 38432dfe-dd90-3685-849c-af548740a222 | -2.9015 | -50.6933 | 2024-10-05 00:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| f77a96a9-560b-3f0d-8ff7-79c41292bbe9 | -3.2349 | -50.3695 | 2024-10-05 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 333ddcb7-c93f-31fe-9df7-ba7bc7a4653a | -3.239 | -49.3986 | 2024-10-05 00:35:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 544e5b87-13a8-33c2-9365-6258927be5fa | -3.2534 | -50.3689 | 2024-10-05 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 2fc76be7-7220-3692-8b2d-40cca57b5f15 | -3.2575 | -49.398 | 2024-10-05 00:35:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| de2ae156-53f6-3fe2-9d13-e9b8e9a26b41 | -3.3127 | -49.4599 | 2024-10-05 00:35:25 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| cb8bbabe-753c-3215-af00-260648ba056c | -3.5994 | -47.5359 | 2024-10-05 00:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 15fa74d6-44c1-39b9-94cd-a865825b01b6 | -3.5995 | -47.5142 | 2024-10-05 00:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| e7af53e6-8d1a-33ed-aacb-15f3f17ad5a6 | -3.618 | -47.5352 | 2024-10-05 00:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| e606edcf-3eca-3643-8a42-e456e28cf526 | -3.6181 | -47.5134 | 2024-10-05 00:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 161.4 |
| 8a4f8d55-c754-3bec-a065-2250a76fae68 | -4.0148 | -43.2408 | 2024-10-05 00:35:29 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 1e6f6d89-37e7-37a9-9b48-f1f366e05013 | -4.0608 | -47.9511 | 2024-10-05 00:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 8af65535-68d8-32ab-a38d-f525651a2c9e | -4.0793 | -47.9719 | 2024-10-05 00:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| dad44809-e8be-33ce-ac8b-9650e0c455b5 | -4.0794 | -47.9502 | 2024-10-05 00:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 253.7 |
| 8538bdbd-05e1-3563-9bf7-ba6b140d9ca1 | -4.0979 | -47.9494 | 2024-10-05 00:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 46142874-f14e-32af-9d1b-b3e9c8d49941 | -5.3911 | -46.4322 | 2024-10-05 00:35:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 43621059-1919-3cd3-8de2-5a3cfa85363c | -5.8214 | -44.1426 | 2024-10-05 00:35:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 97c88e57-1e66-3553-9697-8b43e49df1c7 | -5.8216 | -44.1196 | 2024-10-05 00:35:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 7a802f79-e6cf-3a63-92ce-9a2c8285009d | -6.8851 | -35.0941 | 2024-10-05 00:35:44 | GOES-16 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 118.5 |
| 1fc4262d-3f43-35dd-ac98-6ab25978df73 | -6.8847 | -35.1216 | 2024-10-05 00:35:44 | GOES-16 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 125.9 |
| 9b05f2f7-e726-3061-82e0-b850895e6e30 | -6.9514 | -59.0666 | 2024-10-05 00:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 5fe1eba4-6a45-35df-9213-da06c2eb5273 | -7.0233 | -59.3918 | 2024-10-05 00:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 3c68a00a-d960-30ad-9679-d7b364375109 | -7.1346 | -59.3099 | 2024-10-05 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| f443725d-0c5c-3f46-be87-1dbc83d4340f | -7.1347 | -59.2906 | 2024-10-05 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 1a5aeff8-503b-38ab-97dd-a9fc83933189 | -7.153 | -59.3092 | 2024-10-05 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 18c75672-fc43-377b-8adc-99696d0b47cf | -7.1532 | -59.2898 | 2024-10-05 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 7e9f98a5-4ebc-31bb-9f5d-d32ef03a6bbe | -7.7362 | -49.2297 | 2024-10-05 00:35:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 194.8 |
| 837e12ce-7d1c-3099-bff2-ae6482fcfc9a | -7.7364 | -49.2082 | 2024-10-05 00:35:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 197.8 |
| e6f0a1ed-06e6-3ca7-adbd-42f4b40d24f2 | -7.7549 | -49.2282 | 2024-10-05 00:35:50 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 162.9 |
| c568f224-52da-337c-856c-33cfcb2cf7bf | -7.7551 | -49.2067 | 2024-10-05 00:35:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 172.1 |
| f77f9bf5-c4fd-3363-b6c6-4a9c912e4e51 | -8.2323 | -61.2205 | 2024-10-05 00:35:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| d27b05e1-ddf6-3446-8648-a828ed269329 | -8.7655 | -44.8106 | 2024-10-05 00:35:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 382de65d-6e1a-3716-9a16-d44b584eb00a | -8.6555 | -49.1083 | 2024-10-05 00:35:55 | GOES-16 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| fe27672c-e11b-30d3-bd32-49c1bf554a28 | -8.6558 | -49.0868 | 2024-10-05 00:35:55 | GOES-16 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 7c34ab3b-de89-35f6-842d-dbcd953589b0 | -8.7769 | -49.9763 | 2024-10-05 00:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| bb7b0580-9bfd-30d7-85c6-da29ca05b199 | -8.7772 | -49.955 | 2024-10-05 00:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 32eb3cda-5dee-333c-be83-d2d842d315c5 | -8.7957 | -49.9747 | 2024-10-05 00:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| c254a1ee-170f-31e1-8143-2a6f5cfb7356 | -8.7959 | -49.9533 | 2024-10-05 00:35:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 0b174a58-b297-38b9-bc31-41b635f21502 | -10.0677 | -36.1546 | 2024-10-05 00:36:02 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 62.9 |
| 21df939f-be66-3fa8-ada9-e17753d67b47 | -10.4424 | -50.7336 | 2024-10-05 00:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 42.7 |


[Clique aqui para ver as próximas entradas](README12.md)
