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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f803b685-c4d8-3b81-8787-f58a69d59381 | -12.871 | -47.01527 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff595057-6f38-3014-9e5b-ddd1573256cb | -13.07539 | -47.09226 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8257559-1aae-3437-a482-e0589581e8e9 | -12.74892 | -46.90414 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00eed7f8-8f37-3775-80e3-89c188a4bffd | -15.24537 | -48.08532 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81358264-a5d9-369a-b1fb-6d03b4b9e392 | -18.88928 | -48.29129 | 2025-10-02 04:32:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1130e62-38c2-3c2e-8baa-86877f12f2a5 | -13.66246 | -48.08849 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd4c9e6c-f097-399b-8851-3d0f89ff46e9 | -11.86475 | -48.08207 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cbf814cf-0b27-3f9a-8222-553eb10fa978 | -13.19719 | -47.84874 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5416483-b79e-30d3-ac60-8c2e152d953b | -13.84373 | -47.51616 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e37f4fe5-7dc3-3565-aeb1-0335f8c05c47 | -15.24301 | -46.9864 | 2025-10-02 04:32:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 966c45dd-ac43-3280-878d-667d92d39a5a | -13.18166 | -47.8389 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 27b5fd4f-6fff-371f-b47d-d2387caeda62 | -14.89205 | -48.10098 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34a20e4d-f485-38e9-99dc-4134393f8977 | -13.30368 | -46.99189 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6aeef8bb-b03e-3773-bbf1-a8937fa903c3 | -16.06589 | -51.00909 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fb34f19-85dd-3607-8727-1f0c8dfe1141 | -14.87606 | -48.28894 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1652a11c-5153-36a7-aa57-96cdc49774c5 | -14.31071 | -45.98053 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 419e9fd6-7442-3956-a192-d9d5ccea6bd5 | -17.11486 | -47.11614 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4494858-bc8a-3445-98fb-c257edf05378 | -13.29196 | -47.24423 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07db7269-f586-3ae7-8f8a-e820317c664b | -14.30841 | -45.99601 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 129e1ba8-1418-39ae-acd1-ab9b0336417d | -17.17465 | -47.01981 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28520191-47d0-3ff7-8ab5-389ca853e441 | -13.78099 | -48.04655 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12d3c136-146c-32a9-920e-278b9e2220e2 | -13.06232 | -49.17038 | 2025-10-02 04:32:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c38f62ea-06d1-3e5a-bd0b-afaa6d745f5b | -12.80911 | -47.01629 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3ad9347a-a744-320f-96dc-108cc8a80064 | -13.95426 | -48.10379 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b4fc2e9-0859-351f-9430-860635f58075 | -13.91904 | -48.07267 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84700a31-52b4-329c-9779-239d63b86341 | -17.32259 | -49.38034 | 2025-10-02 04:32:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d97c8e9-baca-3358-a285-44aa1d31ace6 | -13.34548 | -47.32975 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1077abd3-cd41-3cc7-af05-1356f065ad94 | -13.14889 | -47.85172 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed63412e-a66c-3ecd-8c3d-d0942d1d4d07 | -13.1722 | -47.85555 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e8ccf22-1b71-36d8-a80f-25f4b4a3379c | -17.11434 | -47.12087 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20ed19f9-ef2f-3b08-bbb2-42c4764e7e30 | -13.85453 | -51.25035 | 2025-10-02 04:32:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3452880-77e0-396f-b2ca-b50312ebe989 | -14.36449 | -45.95319 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b8ab79d-a308-36cd-a0f6-ca33d0c685dc | -14.47285 | -48.438 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 26551150-0aab-3a4d-bdd2-d4f569689164 | -16.36815 | -47.07829 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9f354d5f-ba55-3206-a70e-6dc27b876724 | -15.25835 | -49.30543 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b474e55-9b6d-3386-aab6-f9433f5821b8 | -15.94953 | -43.30783 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea1713e6-141c-3a5f-b9c3-09f358321aa5 | -12.68713 | -46.91668 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eddce77b-d4e8-3006-820a-5209c91a1f4f | -15.24296 | -46.96385 | 2025-10-02 04:32:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82600a74-79d8-3e16-9113-2b4b9296eb43 | -15.40102 | -49.18789 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04e132e3-4b99-352f-a264-f631157d89b4 | -13.2287 | -48.43774 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4128d25-fab0-3c9d-86b0-d735caa03a0a | -15.93762 | -43.33554 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fb0c819-9952-39fc-9f2c-dde87a43aa65 | -13.46175 | -47.25674 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bbbe6517-ae7e-3e82-bdd6-12f9fe62f745 | -15.25708 | -47.90728 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9119291a-8211-326f-9af1-3c6feb04b2f3 | -13.68027 | -48.06225 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cd9e62d-7dd6-3112-b839-dd6b1b3072f3 | -13.32013 | -47.81833 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd142ac9-dd5c-3d73-8335-3a75c6492383 | -19.95632 | -43.65063 | 2025-10-02 04:32:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 207c9bab-d64d-3d40-8943-3c0bc26d9aa7 | -15.18453 | -46.42214 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 116cfe5d-dca3-3623-9424-6130e3a237db | -16.00054 | -50.90298 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c81591e0-a4e4-3455-847e-1b09c7692b9d | -13.74659 | -48.70299 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0888e5af-e25a-35cb-84dc-01fab860a334 | -16.03712 | -50.85651 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| be470109-dcfa-3290-9696-63edc1cd542d | -13.78497 | -47.99975 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 649969dc-ab2e-3d08-911d-4ced9dd9606a | -13.34331 | -43.67316 | 2025-10-02 04:32:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 725767d2-0aef-347f-9640-fa501419fc0a | -13.32692 | -43.10306 | 2025-10-02 04:32:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 82e57e30-cca7-362a-a5bb-ff9ed0cb9d11 | -13.32155 | -47.32952 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d1bece47-ad13-3b57-b84c-450bcd1b6177 | -13.07311 | -47.01833 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73065956-45f8-3d31-b286-4378c1a886e5 | -15.31186 | -46.29188 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3416a07f-b80f-3929-8ec1-e355dd3c289d | -13.30651 | -47.57934 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e22ac2f0-edb3-396f-a8f2-69e099f67564 | -15.23929 | -50.10616 | 2025-10-02 04:32:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe04e9f3-e6d0-3f73-9c7e-157e28b2f7bb | -14.8644 | -48.298 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 448a9684-f16b-3d88-8e8a-473db38ac5a7 | -14.47123 | -48.42673 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4128eb50-e32d-3bf2-9a23-1e45afc06583 | -15.15917 | -48.00879 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4ecf88be-2bef-3999-91e3-d0c5db0de8af | -13.75672 | -47.96223 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d05f822b-bfad-3896-a41d-3412390443a3 | -12.93878 | -46.942 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a8e84ee-1a22-3f98-a08c-be3b35938440 | -13.77156 | -48.04134 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f6b9a7a-1c69-342d-8a3a-04746b0cc228 | -12.81859 | -47.0215 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8de2a525-e8db-3999-9583-0ca604bb347a | -11.93829 | -47.05339 | 2025-10-02 04:32:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af074fb8-a9b7-346b-90aa-eadcbba075c6 | -13.21812 | -48.4396 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 43b8b93d-3827-33ff-bb7c-36524b863ec3 | -15.74197 | -43.68225 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25ae6e54-3a05-3dac-88a1-2e1d12c117a4 | -15.27819 | -46.40063 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7ad7001-8bd5-3711-a1cf-43fcf42408de | -14.43492 | -46.35976 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95548cda-ee68-33ff-8ac4-a56951a3b617 | -11.94162 | -47.05392 | 2025-10-02 04:32:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3017dd0d-1d14-38ab-b1e2-f8cae197b152 | -15.0322 | -48.06472 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e59acf3-b3fa-335f-9f8f-3babdcdc5acf | -12.58238 | -49.89721 | 2025-10-02 04:32:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21c57fb0-581c-3620-a4bf-a980695482d7 | -13.16887 | -47.855 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9867e48-6a1c-3287-9146-43df32a1a649 | -12.81976 | -47.05831 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 00b71f76-330d-3d3d-8815-de10dfa9238f | -14.28294 | -45.97649 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aaf6c66a-de83-330f-b9d2-e1428761a7e4 | -12.9504 | -48.43888 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8145b031-4bb1-3776-b272-16c73eae96c1 | -17.32476 | -49.38818 | 2025-10-02 04:32:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b49591b-ef22-3cad-a04b-e76525f1ab35 | -12.79806 | -46.85294 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54ba2874-afdc-3e94-b0c4-d30a8b0a283c | -13.75507 | -47.951 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 240a504a-62f6-3915-9c15-682c42e95cf3 | -14.41784 | -46.07951 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45a7c57d-8aef-3dc3-bf98-d4e1a7e0e60d | -13.36875 | -46.33926 | 2025-10-02 04:32:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44fd9ac3-7772-3c7d-bf59-dcbf21f6c418 | -14.61408 | -48.23116 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efb161cf-6941-3a38-a232-8eef68d5a42e | -14.35077 | -43.84759 | 2025-10-02 04:32:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 071816ea-7195-3f1e-b0f2-1a43aa6e07c0 | -13.47231 | -47.25489 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 922eeb0a-9941-30d8-afcf-d2870b71cdce | -15.31531 | -46.29243 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 028b73d0-e597-3792-a2a6-4ee250d1ad54 | -15.84453 | -46.23901 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 608b1899-98a4-3379-a212-4eab59a2cbbe | -15.25651 | -47.91087 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| aced9521-6737-3427-97b6-47c0da8b975d | -15.40837 | -47.0468 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30a3d535-e1d5-3df0-83db-343a11ece192 | -16.06937 | -51.00979 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ada70256-1a38-3e6e-86f6-cce66a547f90 | -16.36599 | -47.07087 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5e6f7ea-aca5-3a70-b8ad-e7e0492fdb95 | -12.8025 | -46.8686 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66a42c0a-ccb1-3b85-ab4b-cc07f05a6622 | -11.58971 | -50.17191 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3eaa0344-b707-38f5-8eda-7e0998692fa1 | -13.86209 | -47.95736 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b6af8123-0568-3220-bf0c-d3465f39cf8b | -19.97002 | -43.71313 | 2025-10-02 04:32:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f0b7d470-78b0-3ba2-a479-cc4bb2f2b106 | -17.55025 | -44.47969 | 2025-10-02 04:32:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5b42a8a-30d7-37ef-ba67-4b6590603b3b | -11.98163 | -47.01669 | 2025-10-02 04:32:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 476bd2ad-4b91-323c-a56a-f0de6967abed | -13.39709 | -47.77975 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 627fe5de-7dcd-3093-abad-36c871c35aaf | -12.76527 | -47.7564 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5532374-1af3-38c2-8edc-309c03097a0d | -13.31039 | -46.99296 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README100.md)
