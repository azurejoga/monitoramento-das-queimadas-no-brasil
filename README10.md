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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a02366f-b6b4-3cda-bb06-6f6df252f942 | -21.4931 | -53.05885 | 2025-06-11 04:51:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 19143d46-f9a9-382f-ace5-3393c0db5087 | -16.30314 | -54.88216 | 2025-06-11 04:51:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2607d24f-bed6-370d-ae34-1eedd5739400 | -21.81511 | -57.54742 | 2025-06-11 04:53:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e3b96c0-7a14-3a54-9931-31d7547ef754 | -23.40673 | -46.5556 | 2025-06-11 04:53:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 778e04db-b09a-30b1-b75d-5993565a1d0d | -21.8286 | -56.26522 | 2025-06-11 04:53:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 847e6ef5-3904-3feb-8163-3e4fedfdff1c | -21.50728 | -53.05727 | 2025-06-11 04:53:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 79c384df-775f-3496-a46d-b52153ee3034 | -22.53922 | -48.81346 | 2025-06-11 04:53:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3579919a-2428-3b38-a23d-d83a827e4695 | -22.69785 | -53.95027 | 2025-06-11 04:53:00 | NPP-375D | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 14c64a8f-417c-32b3-b3af-a182b9c03e72 | -22.69728 | -53.95408 | 2025-06-11 04:53:00 | NPP-375D | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 775ddba8-9ccc-369e-a4ab-b7461ac99b27 | -21.81865 | -57.54813 | 2025-06-11 04:53:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8aef42b7-98a6-37e2-bc48-743f1e163675 | -21.50446 | -53.05279 | 2025-06-11 04:53:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d43ab28-a668-330b-97a6-765fc3073927 | -21.81437 | -57.55166 | 2025-06-11 04:53:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 915bc175-429f-3e55-87a5-be68a26ec266 | -23.33811 | -46.77406 | 2025-06-11 04:53:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e3cf160c-1b0d-3f1c-ad72-effcbbffbe1e | -2.91879 | -48.24022 | 2025-06-11 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b2409b8-0d3b-3021-8261-a5f1a474f97c | -5.77325 | -43.61298 | 2025-06-11 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9e448029-7ed9-31ed-8129-31fa1d7007d1 | -4.24777 | -47.5872 | 2025-06-11 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eba8071f-2b23-3aa0-9156-305f4a054e49 | -6.05956 | -48.12443 | 2025-06-11 05:08:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e45838f-c705-3474-9d5c-fb052178637b | -2.91561 | -48.23563 | 2025-06-11 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 296a620a-a3b3-3d48-bb92-62fa7e908622 | -5.9171 | -43.4621 | 2025-06-11 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc7efee1-94f1-3931-bc42-fb09838833f1 | -3.32425 | -48.71481 | 2025-06-11 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13559363-14b1-3279-b338-3a468c35c5f1 | -4.54854 | -48.02213 | 2025-06-11 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a28c0a62-f858-32b6-9872-031d64da1465 | -2.91922 | -48.23728 | 2025-06-11 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b433a128-2183-3467-8d6b-ec70edc7c94d | -7.47259 | -45.50727 | 2025-06-11 05:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f356ecf4-7d5a-3f91-8b10-3d03de35035f | -3.62692 | -47.51264 | 2025-06-11 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1bb2645-56bd-32cb-a614-d637a6a5a9dc | -4.49118 | -43.77724 | 2025-06-11 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0f35ab07-66a2-3868-bb3c-f6db084565c6 | -7.46677 | -45.50916 | 2025-06-11 05:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9acd339d-4f21-38c0-8f2f-5a398cede662 | -1.41271 | -48.38261 | 2025-06-11 05:08:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a62e06bf-437d-3c35-9896-1284ffd6a3e3 | -4.55333 | -48.02604 | 2025-06-11 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5859aed-36c4-31d2-8ff4-b47c133efbe8 | -3.62156 | -47.5118 | 2025-06-11 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ffb71cf7-d086-3606-8b24-6311474450cd | -6.0591 | -48.12778 | 2025-06-11 05:08:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 629f7b99-67d1-3991-915f-26d86a95e7fd | -7.45184 | -45.51511 | 2025-06-11 05:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c35e7b76-d6be-31b5-88a7-f2b22e1e396f | -7.46542 | -45.51173 | 2025-06-11 05:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1090947b-49fc-366f-b6db-40fa7ae402d5 | -2.92067 | -48.2364 | 2025-06-11 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a67541ab-5929-3740-a514-ba9557c8143c | -5.90998 | -43.46092 | 2025-06-11 05:08:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f27b17ff-dfc1-351f-b8b1-21ed7da5b42e | -4.54823 | -48.0233 | 2025-06-11 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efbd62d6-8786-3959-8ce1-2b74c94d94d3 | -7.47321 | -45.51006 | 2025-06-11 05:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 67e55671-c33a-3104-ad3a-bb77ceb79a40 | -6.9897 | -47.08273 | 2025-06-11 05:08:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df0bd8ee-ef5f-3986-8cb4-6d9cf5038a75 | -7.45254 | -45.5178 | 2025-06-11 05:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e0f11199-1429-3ad5-9dba-e61f848385f1 | -7.45321 | -45.51259 | 2025-06-11 05:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2fe42ffd-0c0e-3bb3-a68f-d4e22aca1f29 | -3.57593 | -49.49445 | 2025-06-11 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e840e53-a375-302f-ba3c-bfc129b793a6 | -2.4467 | -47.47811 | 2025-06-11 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d25947c2-1c45-3db0-969a-1793bb5ce477 | -2.91516 | -48.2386 | 2025-06-11 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2673ea81-35fb-3a06-9746-a97a1f928161 | -3.62743 | -47.50925 | 2025-06-11 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f741452-7fd6-3858-a985-aa7e5cd1388b | -3.57333 | -49.49708 | 2025-06-11 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 464f3424-89aa-3be0-b651-dfc4fa74dcee | -7.46615 | -45.50634 | 2025-06-11 05:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f7f66861-528e-3c6f-a48b-e0371ea984b8 | -7.4647 | -45.51703 | 2025-06-11 05:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7fd9b40f-1763-3239-919c-6c2ffc531807 | -2.92022 | -48.23933 | 2025-06-11 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a3c2f5e-f1f3-3162-b12d-54c76710c820 | -5.91432 | -43.45869 | 2025-06-11 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5d642572-9194-3440-aa68-0dabdc4bc7e6 | -3.31932 | -48.71409 | 2025-06-11 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5beb7afd-43ab-330b-833c-ebbb9a81daaa | -4.12949 | -54.89851 | 2025-06-11 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b4e4cb1-1f22-3e10-a0dd-955e93ffb62c | -4.55396 | -48.0208 | 2025-06-11 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ee03b86-38e9-3a33-ad4c-1473a8349f70 | -4.54806 | -48.02535 | 2025-06-11 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccd261f5-45c2-3a0d-aa8b-1fdb4aad1aa0 | -3.62206 | -47.50843 | 2025-06-11 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 91ec01c3-7ae2-316b-b3f3-251bdf5a292e | -2.53167 | -53.95609 | 2025-06-11 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80cf0d10-2a23-3edb-aef3-8c209f3b7a32 | -2.44622 | -47.48131 | 2025-06-11 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac58c6ea-c6fc-3ada-a18f-895dcbf110fe | -7.46608 | -45.51451 | 2025-06-11 05:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f7bad6f3-0aed-3d2f-82d1-4a965180974d | -7.47187 | -45.51258 | 2025-06-11 05:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bfd337e4-55df-38f6-aafe-7761345f87ac | -7.45114 | -45.52029 | 2025-06-11 05:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 76d94463-ace6-36cf-8d61-d2de8f75a5eb | -4.54868 | -48.02009 | 2025-06-11 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 285e3aa8-f46e-3c76-8dbb-d6247a969504 | -7.45255 | -45.50983 | 2025-06-11 05:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b885a1c7-78cb-3a29-a833-892919bdd899 | -4.5535 | -48.02401 | 2025-06-11 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb01a796-edc5-3807-b0dd-319555a664f2 | -3.9887 | -48.40693 | 2025-06-11 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcc8c184-05d1-3579-b28f-b9e1869c6e9a | -3.57521 | -49.49939 | 2025-06-11 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 956480c7-ee9f-3677-93e0-1892623b0b53 | -2.91416 | -48.23652 | 2025-06-11 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3ec51c45-40d2-339f-baeb-2de66d210b1d | -10.65829 | -49.42926 | 2025-06-11 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c5b51eaf-d9b4-3989-8316-fdf27a980740 | -10.3675 | -57.50488 | 2025-06-11 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0dec89c2-275a-3dfd-91da-771b2bfa2a4b | -13.2278 | -57.12384 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d879de0-6b94-369b-b2ae-03af815c83c6 | -10.87542 | -54.74532 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c88cf45-4cfa-38c6-bf3c-e7cf79e96298 | -10.63656 | -49.43277 | 2025-06-11 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3880cd0f-586b-3e8d-966e-25de132b91ac | -11.65485 | -58.26167 | 2025-06-11 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6045fb75-90bf-387e-b87f-69a56bfc6692 | -13.22724 | -57.12758 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 025f689c-405a-351e-a515-f7eb1ac87584 | -12.20256 | -54.26624 | 2025-06-11 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2450b405-a611-3bb8-a6d8-c2bc254ced8c | -13.09016 | -47.43208 | 2025-06-11 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8a08349-9813-31ad-9c32-d86f8a28dc97 | -12.20325 | -49.62351 | 2025-06-11 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 335ed723-00e3-36a8-a6e8-9f3adbf964cc | -12.20366 | -49.6202 | 2025-06-11 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8aeeee46-86c8-34d1-b0eb-267b16b23410 | -12.77906 | -48.72768 | 2025-06-11 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df67aa9c-335e-3db4-bdb6-cba457fc4c3c | -9.40104 | -48.43682 | 2025-06-11 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb981368-bb57-3d0f-9102-53fd243725df | -11.57019 | -54.56312 | 2025-06-11 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e864f6d6-a637-34b8-92ad-510d39017cb3 | -11.77055 | -54.37726 | 2025-06-11 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce101479-641a-389d-8026-dcb666a34d7f | -10.84348 | -53.77852 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f41ade9d-37d8-3245-89e1-7ba1f88f2a21 | -11.88219 | -56.41421 | 2025-06-11 05:10:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1a937a8-812c-306e-b243-7eed60161dcf | -10.36085 | -57.50383 | 2025-06-11 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 567309f6-8c17-309a-b19e-83ff09fc1de3 | -10.1869 | -49.60026 | 2025-06-11 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a0be666-3d28-3a24-b76c-4df8d12b6969 | -9.39603 | -48.43243 | 2025-06-11 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 491b46de-c56f-38f1-a26a-fb6b44c83817 | -11.83257 | -51.28817 | 2025-06-11 05:10:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e57e059a-1cdb-38d2-ba74-be8849fc6629 | -10.87179 | -54.32018 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e062ec30-81b9-3b92-b412-2407d4c45970 | -12.84028 | -47.38585 | 2025-06-11 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f6db0bd-64c6-308c-8733-725766a39425 | -10.65785 | -49.43255 | 2025-06-11 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2dda39f0-bfc2-3114-b8fa-feffff974ff1 | -10.50861 | -53.62952 | 2025-06-11 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2998117c-a0e1-39dc-8242-9014d954a3ab | -12.13245 | -54.65564 | 2025-06-11 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17657af7-6a7f-392e-8dee-b8df82235d1e | -12.20853 | -49.62411 | 2025-06-11 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 208d385e-541c-3b8e-8946-bcd686f66d17 | -10.65872 | -49.42598 | 2025-06-11 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6bd2e8d9-7529-33f8-9a64-7d7e68c34320 | -9.41249 | -48.43475 | 2025-06-11 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a5fe3df-c96e-3b42-a2a2-70b22580f76b | -10.30476 | -57.14256 | 2025-06-11 05:10:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bbef008-0331-3462-8ebc-963f8e6a13e0 | -12.26405 | -55.07693 | 2025-06-11 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ee74589-202b-3449-a0c6-3000b0d600a5 | -8.28387 | -47.44418 | 2025-06-11 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5923e549-420c-38d0-aedb-a5a360540ec1 | -10.07392 | -52.7489 | 2025-06-11 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7db17cca-d97a-36e1-8f9e-26b965aab5a1 | -11.13853 | -53.92241 | 2025-06-11 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0c76ee1-8309-3349-b572-0e18189fe8a0 | -12.78424 | -48.73203 | 2025-06-11 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca222156-2941-3b10-a7c5-fb186104b884 | -11.34486 | -45.21866 | 2025-06-11 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README11.md)
