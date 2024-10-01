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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dea9afb-7e46-31e7-88a1-548e9b67e6d5 | -16.96552 | -48.95243 | 2024-10-01 04:14:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ea8f502-763c-3878-a58c-636d9736d13f | -16.96543 | -48.95447 | 2024-10-01 04:14:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| beda61ec-f485-3447-bfe3-401206d3d0f5 | -17.96603 | -47.70295 | 2024-10-01 04:14:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a07a161-a7a8-371a-9604-bb90f5962056 | -17.15717 | -47.60619 | 2024-10-01 04:14:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18240116-32cd-35e7-8fcb-6f322cab49bf | -10.78116 | -48.75216 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 572aad1b-e42a-3c7c-9082-895f5e4c4978 | -10.78029 | -48.75729 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b71b80d1-b951-36d2-a3ec-148185581f11 | -10.77722 | -48.75148 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 628d28e9-b45a-3e89-b957-7e0ea7547c23 | -10.77635 | -48.7566 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5072a5af-e8be-3aaf-8daf-287a4b052d47 | -10.77328 | -48.75079 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1814a13c-2170-3d89-9283-45933ea37843 | -10.77241 | -48.75591 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 574c1faa-dbbb-300e-b30d-c5d2321f2928 | -10.76935 | -48.75005 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf000e0a-3a4d-3009-99f3-4f6170edb453 | -10.76847 | -48.75521 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 092e7978-9523-3ed1-a1aa-11ceaa0d95c3 | -10.76759 | -48.76037 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9229bf3e-2c9d-3482-8898-640166314b0b | -10.75313 | -48.77369 | 2024-10-01 04:14:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d623f86-ee6a-3ed9-a511-3809c532810a | -10.74918 | -48.77301 | 2024-10-01 04:14:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01d0a3ff-0fdd-3ad0-891a-3d8949f1959c | -10.71609 | -48.72948 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69507fc8-4b26-394d-a3f2-d8be56376602 | -10.71214 | -48.72889 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63cf457f-2ba0-319f-a708-7635ad8122ef | -10.71119 | -48.73433 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93e5183e-b469-36f5-ac0a-2a1ae894431b | -10.7435 | -47.98632 | 2024-10-01 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28e0f78b-fb54-3bb1-9154-c442c0d9635a | -10.74274 | -47.99078 | 2024-10-01 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a302fb3c-3e39-3cdb-81d6-01e0cf0e882b | -10.73977 | -47.98551 | 2024-10-01 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 019dad95-7ba4-311a-92a5-95dd9d43442b | -10.73602 | -47.98474 | 2024-10-01 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 647aeb9a-7096-33d3-b6a9-4b1a0c3a3771 | -10.46058 | -48.22982 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0c9be8fd-e0a1-33bc-bfd1-5208355b5019 | -10.45973 | -48.2347 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9477cf46-16f0-3ec0-b2a5-0bf1f2a90e4d | -10.45679 | -48.22889 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 42fe689b-1b07-3868-9ae4-9b8d3ca1cc16 | -10.45593 | -48.23388 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3fc551dd-e5ba-3274-869d-19c00c11b891 | -10.45508 | -48.22583 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 11c19879-033a-314f-9209-0ae3fcdea815 | -10.45452 | -48.20553 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4b5ee02e-0357-3acd-905e-d9f6f2c332c3 | -10.4538 | -48.22336 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bfa1e2c0-6a91-37b8-bc7b-b7db3b0a2386 | -10.45343 | -48.20279 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 58c01215-03c5-30c9-9461-a972aba0ed11 | -10.45342 | -48.23581 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72254739-d42b-313a-b8ac-b79406892f89 | -10.4521 | -48.23316 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7301a963-6abf-3568-9e35-5925fd1c9f9a | -10.4516 | -48.1993 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3883fa4f-9be5-3cc4-9913-f3ae787106b8 | -10.44967 | -48.20176 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ab88f409-df63-3e78-a5d4-e57190a29342 | -10.42884 | -48.17081 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 70a33b15-7c16-3ed5-ac52-c2af7cea13f1 | -10.42496 | -48.17046 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 52ded9ef-68bc-3333-b78f-5b9b7479a1f6 | -10.41309 | -48.19411 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3cc54442-5266-3f5c-9bb7-e122c0971cab | -10.40925 | -48.19354 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da61a242-6a64-37ec-9f7a-b45aa436bb58 | -10.40624 | -48.18807 | 2024-10-01 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7155709c-ec78-39fc-89b3-2957c0eeb09f | -11.43971 | -47.82096 | 2024-10-01 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ebf0a18c-67ee-32c3-8652-a08954d46c63 | -11.50816 | -49.24568 | 2024-10-01 04:14:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 187116e4-7e9e-3d30-b62e-75a1c99acfa2 | -11.50416 | -49.24488 | 2024-10-01 04:14:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ceaea814-e29b-31ff-91f1-e1772bd7f230 | -11.24501 | -48.90862 | 2024-10-01 04:14:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62d111da-ecab-3482-a025-c016a2fad39e | -13.51089 | -48.59138 | 2024-10-01 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 0c1e690a-da0e-3d1f-b99b-073c25ddf8a9 | -13.51009 | -48.59609 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b5cb8cdd-a923-351b-9e27-b0bfe6e55d90 | -13.50715 | -48.59069 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8a719dc2-6e26-331a-98eb-a169cda1bff9 | -13.50633 | -48.59546 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f06a829a-3649-3dc1-9223-3173a35328b0 | -13.50424 | -48.58516 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 54df94d7-b0e8-39bb-b9fc-ae14c5fa0394 | -13.50341 | -48.58998 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c9586f53-cbe3-3196-b164-2c0a89f545f3 | -13.50258 | -48.59478 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 9d158f66-316b-32de-9840-ba24488dcaa1 | -13.5005 | -48.5844 | 2024-10-01 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1c129170-1d30-35e2-82d8-3997bad21ece | -13.49967 | -48.58926 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 329d57e9-0b25-3f46-8b19-f5aca05f68ef | -13.49885 | -48.59401 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0c9935bb-bc47-39e1-b7a6-0e381a6f11f6 | -13.49677 | -48.58364 | 2024-10-01 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6a7a3874-d918-3a19-b5a9-cc28751195af | -13.49593 | -48.58853 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d4e19de5-b908-3eb4-8080-b46260abae85 | -13.49304 | -48.58288 | 2024-10-01 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2783076e-e7d3-3e4b-8a35-f47ff96601ed | -13.49219 | -48.58781 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 39816dfa-3b0d-3044-91b5-ae58ded49880 | -13.48645 | -48.62109 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab33a7ce-fa05-3f41-bb7c-01dd4afa560f | -13.47063 | -48.62305 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0a892027-5d6c-3826-86af-d21daa6ed5b1 | -13.46688 | -48.62232 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dcc63df4-a7c2-32c8-8aed-bc893467fea1 | -13.46605 | -48.62708 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b41d83c0-15b7-3a30-a06e-057c8e1b4bff | -13.46523 | -48.63181 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fafad2bf-fc18-34f7-aaa4-c37b84be3019 | -13.45645 | -48.61551 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0303fd57-d536-309f-84c5-a7c57a015d13 | -13.45564 | -48.62019 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 55158c05-6217-368b-8e96-c1a165bafb46 | -13.45398 | -48.62965 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2866323f-1c97-37e8-9603-f8cc4b7826f1 | -13.45022 | -48.62901 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc6a309b-52d5-3867-a02d-01489b3f53c8 | -13.44893 | -48.61421 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5169cc2-6953-3639-ba13-65c45879a6bb | -13.44811 | -48.6189 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fa7d26de-f4d0-3ed3-9c1f-c5c41a48377e | -13.44728 | -48.62363 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| afb27aee-f5ed-3762-a5bd-7ae9ee4cf7df | -13.44645 | -48.62838 | 2024-10-01 04:14:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 973adb0e-c2db-33e2-8c7b-ccdf8ccc1a2a | -13.22245 | -48.55343 | 2024-10-01 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| caa469ce-d329-391b-a2fd-01dd8386e8ed | -13.22108 | -48.58324 | 2024-10-01 04:14:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 283de1e7-f455-3dd2-adf0-d1e6fceb19e6 | -13.2204 | -48.58516 | 2024-10-01 04:14:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b65d1f3b-1e12-3e47-aa45-20f7a03925b1 | -13.22027 | -48.58787 | 2024-10-01 04:14:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b846b754-43e2-3d64-aeeb-948f740bed85 | -13.21872 | -48.55265 | 2024-10-01 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d7d2dc3b-d8e3-3965-ba59-7421fc05e56e | -13.19339 | -48.51643 | 2024-10-01 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb20e80f-b3ce-3ed8-86e9-273943868107 | -13.19264 | -48.52078 | 2024-10-01 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50066099-dde0-37e6-8061-5e0910392b72 | -13.18963 | -48.51583 | 2024-10-01 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a913bf5a-0846-32a3-b01b-b3e34c9afd2e | -13.18665 | -48.51067 | 2024-10-01 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee5d6b41-bccc-3a43-89b8-ce127e720c27 | -13.22567 | -48.57919 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 213202c5-3c5f-3cad-bc0d-381153774983 | -13.22484 | -48.58389 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a1b78975-7389-3f5f-9ae3-e2e37a25c1ad | -13.22274 | -48.57378 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c7a224e6-cbc6-3fc8-8e44-80d1d87a808d | -13.22199 | -48.57573 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9955b0d3-b7de-3a85-869b-c61fe69b9ef6 | -13.2219 | -48.57856 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 02ac2f25-4fbc-3c0f-9df9-8754083a4749 | -13.22158 | -48.55838 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b80951e-35fa-3d58-94ca-7850b8c15a3f | -13.22156 | -48.55532 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9047855-f23e-369a-8013-be9ff4e3c9d9 | -13.22119 | -48.58049 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 62113e02-ef79-3ce9-a703-58a2046059ee | -13.2207 | -48.56042 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05464d56-4dbb-3973-8db4-734781e9bddb | -13.22069 | -48.56344 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7328c913-4979-39f7-9ff6-885261f6376b | -14.77273 | -48.78041 | 2024-10-01 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85f577c2-dc96-374d-8e23-624d1f8126f2 | -13.21898 | -48.5731 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c9363a82-bc01-3323-97a5-0d7f912518c6 | -13.21823 | -48.57506 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ed9129b5-a600-3fec-8f18-d252ee0945d5 | -13.21814 | -48.57789 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 62a0a67f-763b-3b67-9773-247f052bd410 | -13.21782 | -48.55452 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4004a435-b0a4-31ad-8a91-d4b204ad6d15 | -13.21742 | -48.57983 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8784723c-6abc-3d46-9416-0cc715ac3925 | -13.21693 | -48.56275 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8202a916-7f7b-3066-b061-f3661deafba4 | -13.21522 | -48.57246 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f57df9de-88e4-31ba-b749-844fb42324ca | -13.21447 | -48.57441 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21691e71-78f9-337c-9a3a-5baebda5e739 | -13.21438 | -48.57722 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59502313-949e-3b97-83b7-b8d394d641f4 | -13.21366 | -48.57916 | 2024-10-01 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README78.md)
