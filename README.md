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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82b13407-7d9d-3c70-b621-7e90323c52c2 | -19.6144 | -57.3571 | 2026-01-27 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.2 |
| c428ae33-1d68-3570-af05-459b0d3cfdd2 | -19.6148 | -57.3362 | 2026-01-27 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 309d3353-7486-370e-b5d5-036922329e0f | 2.5442 | -60.3563 | 2026-01-27 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 5a79fb42-34f9-3948-a693-795252863519 | -19.6141 | -57.378 | 2026-01-27 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.6 |
| 74e438f0-8372-3869-a85c-f9826db0502c | -7.1909 | -35.0541 | 2026-01-27 00:10:00 | GOES-19 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 77.7 |
| 0b56d356-bda3-3ef8-80e5-16adf965a29c | -19.6141 | -57.378 | 2026-01-27 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 49643b94-ab6b-3a2e-8048-15d74582c6fd | -19.6144 | -57.3571 | 2026-01-27 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 9565bf7f-5d28-3cdb-881a-b83a30e90ff0 | 2.5442 | -60.3563 | 2026-01-27 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 462a5b6e-b6ce-315a-a8c5-cfac70c681b2 | -19.6144 | -57.3571 | 2026-01-27 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.6 |
| d04c728b-16b1-3e5c-8ee7-19175ad8b0e4 | -19.6141 | -57.378 | 2026-01-27 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 9070a3ce-6ebc-37ed-9ca6-b19b9ea35935 | 2.5442 | -60.3563 | 2026-01-27 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 70.2 |
| e9ac6c9e-8591-3249-91a9-a43da1f273d1 | 2.5442 | -60.3563 | 2026-01-27 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 9e3cafcf-66a6-3a94-a1de-45acfa632c76 | 2.5442 | -60.3563 | 2026-01-27 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.6 |
| ed5fface-c92e-3917-a58f-08056f404971 | 2.5442 | -60.3563 | 2026-01-27 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 83e7810f-909a-38ee-93d4-e5dab1b09914 | -10.1567 | -36.5425 | 2026-01-27 01:00:00 | GOES-19 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 95.4 |
| 84ff07e4-6d45-3401-b69a-4102a0e528a5 | -6.5036 | -35.1141 | 2026-01-27 01:00:00 | GOES-19 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 62.9 |
| 38dc0a0c-d37f-34af-88e2-7f75b49a67ae | 2.5442 | -60.3563 | 2026-01-27 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 46.4 |
| ad9d2abe-e389-3462-a34d-c3df2368dd86 | -7.8567 | -35.263 | 2026-01-27 01:20:00 | GOES-19 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 67.0 |
| d1ca6a91-4c57-3ad3-ab26-fa0e3f1b7e13 | -7.8759 | -35.2602 | 2026-01-27 01:20:00 | GOES-19 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 64.3 |
| a9a7f0f1-53b2-3d0a-ae39-c0bdbe8e4f9e | -19.61309 | -57.38145 | 2026-01-27 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.5 |
| f2a5ad58-d409-3094-b723-08d0a26ff330 | -19.60744 | -57.34837 | 2026-01-27 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.4 |
| fc9ab715-12e7-31ed-b930-716079767d96 | -19.61027 | -57.36493 | 2026-01-27 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.7 |
| 65ab47e4-e664-3730-8598-d9671bd9244b | -10.51391 | -36.75429 | 2026-01-27 02:57:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 985afdbe-989b-35e1-9d62-a2f003ffd30c | -10.51506 | -36.75312 | 2026-01-27 02:57:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| b019ef1e-c8ce-30de-8595-8669d073fda0 | -5.24936 | -35.61236 | 2026-01-27 02:57:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7adac260-6d00-3f59-af92-daf031eac690 | -10.51639 | -36.7467 | 2026-01-27 02:57:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ddca8cb8-e8e7-3da7-a4c2-a6bd9deca419 | -10.51519 | -36.74784 | 2026-01-27 02:57:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e117a6a5-e989-3b75-8f52-9a85671ea8f5 | -5.24242 | -35.61127 | 2026-01-27 02:57:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5bc850e8-5eb8-3085-b4c9-79ee418c0f4b | -6.43551 | -35.45853 | 2026-01-27 03:17:00 | NOAA-20 | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fa7c182f-2bc1-3276-abd3-e7512d1a791d | -9.57386 | -35.85751 | 2026-01-27 03:19:00 | NOAA-20 | SATUBA | ALAGOAS | Brasil | 2708907 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3bdee3ec-01a3-3612-9814-1c36b2e5ff6e | -10.51503 | -36.74975 | 2026-01-27 03:19:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| d337b899-ff35-3a8e-b95d-ea7b57b3946f | -11.60438 | -42.06683 | 2026-01-27 03:19:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 9e333439-7504-33ff-967e-1d4c5c9ed42a | -5.24315 | -35.61495 | 2026-01-27 03:19:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 31590f73-b6df-3e03-9302-90fce29dfea0 | -9.57313 | -35.86168 | 2026-01-27 03:19:00 | NOAA-20 | SATUBA | ALAGOAS | Brasil | 2708907 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 65eac298-1236-30ff-9a72-9758ffc3aa73 | -11.60539 | -42.06189 | 2026-01-27 03:19:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 6b43d1c0-ab23-3964-a4ab-f364c45117c6 | -11.60126 | -42.06278 | 2026-01-27 03:19:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 7a5857d7-f9ea-33b8-8f7f-da83989a278d | -5.24395 | -35.61027 | 2026-01-27 03:19:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 1f5a8be9-9c67-3a33-af70-cf03f77e720e | -11.6074 | -42.06456 | 2026-01-27 03:19:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 58d9fee1-ca38-3ec5-8511-4a2dc36e5abc | -11.60839 | -42.05951 | 2026-01-27 03:19:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f12c4efe-b54f-314e-9c0c-ec4548070e8f | -15.84754 | -43.50588 | 2026-01-27 03:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0c74470-8417-3f06-8d7c-f5efaa5ad7c9 | -15.84637 | -43.51117 | 2026-01-27 03:21:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80cfadef-a792-3f54-9a27-9a52a2fa4205 | -6.43822 | -35.45788 | 2026-01-27 04:08:00 | NOAA-21 | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1b0a49fd-ac8e-3d04-be6b-8d3c0b8426e8 | -7.83969 | -43.13213 | 2026-01-27 04:08:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5cfa4610-097e-3d12-81a3-d5391ff2d418 | -8.09332 | -42.69338 | 2026-01-27 04:08:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0f1ebc6a-33f7-3c83-8493-eff99af72e3a | -7.66141 | -35.17611 | 2026-01-27 04:08:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| cd93dd1f-21fd-3c77-8f68-abe4fe5fe8cf | -8.16118 | -43.1873 | 2026-01-27 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 166dc63c-bcf6-351c-a37b-8203ccba3dab | -7.65798 | -35.17867 | 2026-01-27 04:08:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 251faff7-e4e2-3922-9db0-c65c2aea68c6 | -7.66252 | -35.17923 | 2026-01-27 04:08:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1cceb369-ce76-3d6a-8830-57848d57d5a4 | -7.65861 | -35.17401 | 2026-01-27 04:08:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 88053064-3e4a-3b4b-b07e-ec1c83adacf4 | -4.36677 | -37.90255 | 2026-01-27 04:08:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| db879856-00a6-3d6f-84b3-753b797da55e | -5.24574 | -35.61212 | 2026-01-27 04:08:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 9fbf73f9-29e8-3593-ae4c-6bc600c073de | -5.24631 | -35.60819 | 2026-01-27 04:08:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 7461f2ed-0861-323d-acf6-7f20c950885a | -4.86106 | -37.44834 | 2026-01-27 04:08:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1e363ce3-2c81-330d-b4cc-7d658bf4da0a | -8.16689 | -38.4461 | 2026-01-27 04:08:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 085a26a1-c196-36ff-ad78-7dd89e58dba8 | -4.8604 | -37.45284 | 2026-01-27 04:08:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 58757590-e0a0-3e35-8da2-b3bed7f62ca8 | -8.16637 | -38.44447 | 2026-01-27 04:08:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a7259c53-041c-3df2-abe0-5aafab6b04e5 | -7.66315 | -35.17456 | 2026-01-27 04:08:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0c350ab9-0771-321e-8d52-a46b297c3c73 | -12.0746 | -45.30678 | 2026-01-27 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fda73f7e-8c7f-3a74-8aa4-e17770df4831 | -14.87186 | -45.19222 | 2026-01-27 04:10:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea127218-cb23-3048-b19b-a31c226a1b3e | -11.07754 | -43.34249 | 2026-01-27 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3db8b4af-5161-3ede-8c2f-a15bee3ff698 | -14.86849 | -45.19165 | 2026-01-27 04:10:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c61cebed-f2d0-3c61-9edb-07afb7450790 | -12.09196 | -43.77047 | 2026-01-27 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 974c6cca-b3ef-3f1f-8a10-81d17203a419 | -11.60796 | -42.06271 | 2026-01-27 04:10:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 2aab7638-b213-326a-9e90-e740a279c6e7 | -12.03252 | -43.71654 | 2026-01-27 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14ef96bb-1171-38cb-8ba4-f5277d585207 | -11.3997 | -48.44025 | 2026-01-27 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3106bc67-df50-324c-af0c-3717a6eb653e | -11.61237 | -42.05615 | 2026-01-27 04:10:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 89ab4c97-6527-303d-b9a5-d7154b868a58 | -11.85754 | -38.45269 | 2026-01-27 04:10:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5a1e132b-ad81-3879-a5cc-2bbf5ade443f | -8.45828 | -45.14342 | 2026-01-27 04:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea4a3e98-c20e-3776-afb8-3ebf4f451d64 | -14.34063 | -46.53468 | 2026-01-27 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab7d4cec-af63-364c-a5ce-5d7e8c848140 | -11.60464 | -42.06219 | 2026-01-27 04:10:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1f8e3709-a33f-3567-a3d9-ac22775c8669 | -11.07698 | -43.34601 | 2026-01-27 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 264e6653-1725-3b05-af0e-d1017139aa61 | -9.28623 | -43.15536 | 2026-01-27 04:10:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 255df456-091c-3e7b-bdd9-f5c0b03f7805 | -11.60851 | -42.05917 | 2026-01-27 04:10:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| beecc705-fcfb-36d7-adb8-cdf067a90d27 | -11.60519 | -42.05865 | 2026-01-27 04:10:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 79228135-3ead-3cb6-80a6-bb2a5053453a | -14.80551 | -48.76153 | 2026-01-27 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa80c95b-6668-3979-9268-f7acd6c6d629 | -8.82487 | -44.02116 | 2026-01-27 04:10:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7743a5b-67e4-3531-90f7-bdc9547af6d1 | -13.54542 | -43.70592 | 2026-01-27 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65fa25cf-1582-30b7-a0f2-1aa74a2d4339 | -13.60947 | -43.56062 | 2026-01-27 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 27eaf0d7-3796-3d79-af66-02702cc77edb | -10.3487 | -44.83105 | 2026-01-27 04:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1aa74b0a-f72a-369d-9ae0-980cc4b21937 | -10.97434 | -47.73764 | 2026-01-27 04:10:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7058164f-efbf-36c6-a0fb-1361e3f6d725 | -15.8495 | -43.50576 | 2026-01-27 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d56e113c-af21-3bda-b5e7-2397a2050737 | -12.6137 | -39.2713 | 2026-01-27 04:10:00 | NOAA-21 | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 738caac7-c791-334b-8fd7-7d5d15045534 | -12.07806 | -45.30738 | 2026-01-27 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3359cfc0-0cd2-3eb2-821c-02d78c7c6e30 | -8.45472 | -45.14281 | 2026-01-27 04:10:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0637748-7027-3747-90c5-58c44d7ec19a | -11.98999 | -37.7502 | 2026-01-27 04:10:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 3478315a-6e3b-3108-bbba-46d2b4917870 | -10.7691 | -37.14142 | 2026-01-27 04:10:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 72f5ab3f-ba4c-3666-80c0-6ce7b3c3d23d | -15.32348 | -42.05472 | 2026-01-27 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3a61ab2b-f352-3a2c-99ef-546da030c15c | -15.85281 | -43.50631 | 2026-01-27 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4b42694-ee51-3c90-980b-8a468b71bcc7 | -12.39165 | -43.6638 | 2026-01-27 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58453bad-4459-3362-aa0d-d95390dab161 | -11.8601 | -38.45076 | 2026-01-27 04:10:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d3b2112e-fcff-3d66-b345-34eb2b6f37d6 | -11.40038 | -48.43642 | 2026-01-27 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06550ee4-38ae-3b27-8e0a-2ccf24f8e47b | -12.39496 | -43.66434 | 2026-01-27 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9214bad5-9b92-3c6c-95c0-348547291d16 | -9.28679 | -43.15185 | 2026-01-27 04:10:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0d414fc2-e248-393b-a222-f215b039d2af | -10.41768 | -38.03157 | 2026-01-27 04:10:00 | NOAA-21 | SÍTIO DO QUINTO | BAHIA | Brasil | 2930766 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ba205f81-f65b-3490-a821-bfac58ba61ec | -11.40385 | -48.44099 | 2026-01-27 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0ae80c6-0d3d-38d1-8cde-abec1a98b544 | -11.61183 | -42.05969 | 2026-01-27 04:10:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 0d0a2d4e-8c97-3174-b555-fd869232c897 | -11.02334 | -44.83509 | 2026-01-27 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de924c46-9bec-33ef-81c2-4986b4e37112 | -12.0914 | -43.77398 | 2026-01-27 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52cbe3f8-a3c3-3eca-9e25-0950f8eb85aa | -16.34706 | -41.45248 | 2026-01-27 04:10:00 | NOAA-21 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f13e6e18-f434-3673-bc2d-a2dff77060bc | -12.35468 | -47.89888 | 2026-01-27 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README2.md)
