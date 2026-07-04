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
| b72244e1-62a0-365d-a267-17980c30dfce | -4.141 | -48.836601 | 2026-07-04 00:36:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 149a7dfa-64d7-3f6d-a376-c06f0069bb47 | -2.7718 | -48.5723 | 2026-07-04 00:36:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f05ec542-5cb3-33da-8b51-8f3c00025ac8 | -6.9374 | -43.7127 | 2026-07-04 00:36:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1e36dc8c-8c07-3cd4-97de-b9597ebe3956 | -5.4195 | -45.2906 | 2026-07-04 00:36:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de7e46df-6104-345d-8c96-a54f1a996fd7 | -4.2894 | -48.3564 | 2026-07-04 00:36:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a31ca1b5-28e9-3da8-b101-26aaebd9429a | -12.7442 | -44.5256 | 2026-07-04 00:36:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 84227add-2a90-370e-9fd1-857358bc4a4a | -6.4233 | -43.719898 | 2026-07-04 00:36:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 76af4895-f62f-3b52-aa93-8739884accb0 | -5.4712 | -45.4244 | 2026-07-04 00:36:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a61def05-3b09-38c9-a6b8-611817130d48 | -11.9181 | -43.379799 | 2026-07-04 00:36:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 43a10b1f-67c4-3157-aaf6-5fcc8c89ed87 | -4.0169 | -48.065601 | 2026-07-04 00:36:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81b1249e-e258-3d31-9702-c0938c501363 | -7.5092 | -49.5299 | 2026-07-04 00:36:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45918972-5c23-3612-ba9a-753dd876141c | -10.9262 | -43.032101 | 2026-07-04 00:36:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 84f955b8-617e-3033-9ea1-9c155440b1a4 | -7.0129 | -42.7715 | 2026-07-04 00:36:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f471b6ff-0dbe-3088-aa52-1c13517737bd | -8.0887 | -46.7103 | 2026-07-04 00:36:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7de61a43-e978-3560-a1c5-c44b2d571633 | -12.7621 | -44.513599 | 2026-07-04 00:36:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c71463c-776b-3804-85ef-a6caa41b09ea | -4.1508 | -48.8344 | 2026-07-04 00:36:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fee0094-1b90-38d7-82e9-12b02bb4cb49 | -4.1425 | -48.843498 | 2026-07-04 00:36:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d334e02-b321-32eb-9352-feadb8bbd9b9 | -10.9813 | -43.699402 | 2026-07-04 00:36:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| db9cf015-3375-3b11-a92b-c8cc3ecb2b00 | -10.9304 | -43.0494 | 2026-07-04 00:36:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3c1def8-dd79-3176-9588-64e2c41f8f36 | -8.4475 | -51.562 | 2026-07-04 00:36:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17c5428f-9668-394a-a9af-b20cc928dcd4 | -12.197 | -43.686001 | 2026-07-04 00:36:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e7fc1506-e465-33a9-b0d4-1fca1154e90e | -7.8072 | -45.221401 | 2026-07-04 00:36:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3f0ce0cf-022d-3fd1-bd1f-46563c40137f | -12.751 | -44.555 | 2026-07-04 00:36:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e9e2f9b7-2803-3bda-9d23-2484fa2b664a | -11.3044 | -54.466499 | 2026-07-04 00:36:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1eee723f-7a2b-36d6-8c55-cea0ed46ee85 | -4.2878 | -48.349602 | 2026-07-04 00:36:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c812a7fd-f936-3a74-ae26-5fb1469b6da4 | -8.0324 | -46.240002 | 2026-07-04 00:36:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09191f91-460b-35de-8e35-640c9e2134f8 | -7.8055 | -45.213902 | 2026-07-04 00:36:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 82582ca7-3c11-3c29-9757-63bca6345d1e | -21.2024 | -48.597099 | 2026-07-04 00:36:00 | METOP-C | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 37383d2f-3860-3550-8f88-e0beaeab74ee | -8.0365 | -46.7076 | 2026-07-04 00:36:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 789dfafc-4372-3de7-b239-5724e46c353c | -4.3423 | -48.951801 | 2026-07-04 00:36:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 920bc555-b2a4-3614-8219-207200f9728c | -12.5284 | -48.2901 | 2026-07-04 00:36:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b273eec-cab9-3655-8854-231d3d0b5ce2 | -5.4213 | -45.298302 | 2026-07-04 00:36:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7300f258-4e93-324f-9947-d0254ce486c1 | -3.4952 | -48.0387 | 2026-07-04 00:36:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbd250d7-dd72-3e21-98ad-16f117975083 | -3.505 | -48.036499 | 2026-07-04 00:36:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f74a36fc-5d73-37aa-afe5-9a57dc496145 | -18.775101 | -47.630798 | 2026-07-04 00:36:00 | METOP-C | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1aaae9f2-f3c5-30db-ba47-79c730b78d07 | -20.0327 | -48.2943 | 2026-07-04 00:36:00 | METOP-C | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 205786ea-7ae8-3b1b-8625-a798cfa1f676 | -3.5163 | -48.0411 | 2026-07-04 00:36:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf857a52-84e1-32f9-9e9e-137355887dc2 | -18.7153 | -47.539501 | 2026-07-04 00:36:00 | METOP-C | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d6003abb-a9a8-342a-9545-39c615a24254 | -8.4496 | -51.571701 | 2026-07-04 00:36:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cf4c2f0-4a5d-3d06-b235-87ff6623fe7f | -11.4612 | -46.583599 | 2026-07-04 00:36:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c10f2269-fbb3-3a84-a4ec-79d5cf1b3d59 | -12.7493 | -44.5476 | 2026-07-04 00:36:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6eddd24a-f701-32ce-820c-281f316219f2 | -18.7733 | -47.622398 | 2026-07-04 00:36:00 | METOP-C | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cae916b6-c0e9-3d36-9c8a-94de4f18bce7 | -10.9832 | -43.7075 | 2026-07-04 00:36:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 281f27f5-8fbe-3878-aa64-916336a74dad | -5.4365 | -44.655998 | 2026-07-04 00:36:00 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb7be81e-7a0d-314f-8335-25c772b52a09 | -6.906 | -43.710701 | 2026-07-04 00:36:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 49c848da-7e5e-31b9-a6ff-e5093a64bb85 | -11.3142 | -54.4645 | 2026-07-04 00:36:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f843b3c-08bb-33da-9e4e-403ef4873062 | -12.6769 | -48.2174 | 2026-07-04 00:36:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b00930bc-2552-3bd1-96c1-969ac51e39df | -11.92 | -43.387901 | 2026-07-04 00:36:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cbc81ba6-2169-3ce8-95d2-9d2edccd273e | -3.4233 | -41.710201 | 2026-07-04 00:36:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 11664666-f43f-3d12-a222-b4fbb7291b9d | -7.0153 | -42.781502 | 2026-07-04 00:36:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 33e8caf7-86ef-3614-9b79-cbd602506ead | -10.9206 | -43.0518 | 2026-07-04 00:36:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4c49de5b-a4a4-36e9-8029-4bfd3593b39d | -12.3589 | -47.4235 | 2026-07-04 00:36:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a22cb80-f6c3-3a84-9d2b-5b27ccf83d1b | -20.030899 | -48.284901 | 2026-07-04 00:36:00 | METOP-C | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a74ffbfc-98dc-3c05-8bdb-67fcf5545450 | -8.0871 | -46.7034 | 2026-07-04 00:36:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7aa6bc5a-3a87-3386-9bcb-ec71d55a0186 | -5.7949 | -43.635899 | 2026-07-04 00:36:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c28eeb3f-cc4d-3149-8b9d-e783965d6d96 | -3.4201 | -41.696999 | 2026-07-04 00:36:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ea9caec8-4be3-3a49-b5f9-d06b4079a80f | -3.5148 | -48.034302 | 2026-07-04 00:36:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e463f894-334a-38da-bd6c-e4b7517da42a | -9.439 | -40.3158 | 2026-07-04 00:36:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 602d8735-6175-3554-b7ee-49978cfc9e70 | -5.3154 | -43.570099 | 2026-07-04 00:36:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f6c80f4-34a3-3dd5-8150-fa513214f6eb | -7.9017 | -48.248901 | 2026-07-04 00:36:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4a0e2a8-ad4b-3ed9-9286-42ce85f54b1b | -2.7702 | -48.565498 | 2026-07-04 00:36:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| befc1438-3ef0-3b01-9df6-f597b6437d54 | -4.5751 | -48.0271 | 2026-07-04 00:36:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a670885f-c62a-3798-9d1e-27fe28f68355 | -5.3132 | -43.560699 | 2026-07-04 00:36:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65f38111-97a6-3b78-a910-920dc5442cf1 | -12.7408 | -44.510899 | 2026-07-04 00:36:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 44a3b7c8-42d5-3ca8-b79f-8d5e061454e2 | -18.7136 | -47.5312 | 2026-07-04 00:36:00 | METOP-C | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| becbbebd-0abc-3d21-8d77-0d29ca9b00bb | -10.9851 | -43.7155 | 2026-07-04 00:36:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8517ba18-2798-3567-a94a-e6dcef517ce6 | -5.6026 | -39.542 | 2026-07-04 00:36:00 | METOP-C | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8e398d59-966d-3068-a281-739f9ac0ae1a | -4.1394 | -48.829601 | 2026-07-04 00:36:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d15cff81-1532-3a77-a0fe-01cbe2d63e5e | -6.1978 | -45.754799 | 2026-07-04 00:36:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a54cc2a1-8baa-32ca-99d5-5c7928991bcb | -10.9185 | -43.043098 | 2026-07-04 00:36:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 998c2432-f22c-35d8-84b1-fe375b31dfce | -11.3202 | -54.4792 | 2026-07-04 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 2a32c38d-5249-3065-89cb-d165e737681f | -12.7553 | -44.5194 | 2026-07-04 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 96e02632-40c5-3dfa-8f55-cceebc035a07 | -10.9209 | -43.0384 | 2026-07-04 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 236.1 |
| 063c164b-d878-3027-bb06-ee9e5f5a326f | -3.4259 | -41.714 | 2026-07-04 00:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 35.1 |
| 80f687b5-e84b-3710-a87f-71d0012faf41 | -10.9401 | -43.0355 | 2026-07-04 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.6 |
| ab644574-d334-39da-b50b-990ab8445ade | -10.9397 | -43.0593 | 2026-07-04 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 06dba4da-2cb8-3075-ae54-299bc98c8896 | -12.7548 | -44.5428 | 2026-07-04 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| cfb45c27-3cb9-3cb6-a5ea-64f300ebded5 | -10.9205 | -43.0622 | 2026-07-04 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 12ead497-5dd6-388d-93c3-b2a12f906f44 | -10.9401 | -43.0355 | 2026-07-04 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| f0d4a1db-119e-3603-b83e-88bf6cd9c972 | -12.7553 | -44.5194 | 2026-07-04 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 0ba8238f-86d2-3d5f-8ed5-843d3e2d6822 | -13.2206 | -54.3737 | 2026-07-04 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 122.1 |
| c38e5fd6-c27a-33e3-aeb5-c5768fd22559 | -11.3202 | -54.4792 | 2026-07-04 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 8f077b08-1db0-3197-bfb6-84d44fbf7bf5 | -13.2395 | -54.3923 | 2026-07-04 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 9cc5d3e5-0170-3c23-81b3-e9517cb46afe | -13.2209 | -54.353 | 2026-07-04 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| d489c307-fd0a-382e-8836-6d4b87a3b3b9 | -10.9205 | -43.0622 | 2026-07-04 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 468303ae-9bb0-36f7-a922-dff8dd956806 | -13.2589 | -54.3696 | 2026-07-04 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| fb407593-3f1c-3f29-880a-3883c22e94b7 | -10.9209 | -43.0384 | 2026-07-04 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 227.7 |
| 40cab4f6-8ad8-3156-9ee4-38dbc2cfd908 | -12.7548 | -44.5428 | 2026-07-04 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 59c0a65f-0dd9-3502-ac27-e44e79178076 | -13.2398 | -54.3716 | 2026-07-04 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 249.0 |
| fa092768-19e1-3cf6-b53c-6fcfccbe414f | -10.9397 | -43.0593 | 2026-07-04 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 03298754-a93e-36e2-a1b2-dbcda0d1ce19 | -13.2401 | -54.351 | 2026-07-04 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| e01a276f-8d78-307b-8ad4-48198d3434d9 | -13.2398 | -54.3716 | 2026-07-04 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 132.7 |
| a6eb89d5-8c76-3b55-b9b1-3ce6d0cd8401 | -13.2206 | -54.3737 | 2026-07-04 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 7873bfe5-120d-3497-87fa-ccaf933fbba7 | -13.2401 | -54.351 | 2026-07-04 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 7ffb3f14-5406-3760-a369-f30e39b9bc48 | -11.3202 | -54.4792 | 2026-07-04 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 30080ad4-c5c7-35bf-be15-a65db2863b13 | -10.9401 | -43.0355 | 2026-07-04 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| a4ebd503-3089-3821-b022-fc549c46ea8e | -12.7553 | -44.5194 | 2026-07-04 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 840a0339-015a-3b1f-8f94-0a49dd6096bf | -10.9209 | -43.0384 | 2026-07-04 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 253.7 |
| dae5f45d-7743-3afc-96f7-c57bb926391a | -10.9205 | -43.0622 | 2026-07-04 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 215.1 |
| 3c806e2d-f756-3542-9351-efe8a9b49383 | -10.9397 | -43.0593 | 2026-07-04 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |


[Clique aqui para ver as próximas entradas](README4.md)
