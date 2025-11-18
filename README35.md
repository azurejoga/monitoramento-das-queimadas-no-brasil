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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae8678cc-e2cc-3ebe-89cd-536f4a6c0eb6 | -5.75238 | -45.10486 | 2025-11-18 04:48:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2a4801f0-46c5-3313-8ddb-1a1bc9479fdc | -3.47611 | -46.06688 | 2025-11-18 04:48:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 794a356e-80df-34fa-938b-c868f902a5f7 | -1.67586 | -53.20784 | 2025-11-18 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40f0c515-f18e-3ad1-a7d7-fee71a79c5b0 | -6.40309 | -42.32186 | 2025-11-18 04:48:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ddf43581-c257-366d-9ef6-3c9c0665652d | -4.97073 | -41.84739 | 2025-11-18 04:48:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ee2c2fe9-8f71-3192-84a2-a283e909ea48 | -3.14711 | -52.17311 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f4ab316-f2b2-3f14-8aa7-a8344b3e1039 | -3.04872 | -47.01649 | 2025-11-18 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 447a2372-e18c-3598-a98a-57fb5c8b6da2 | -2.4978 | -49.34612 | 2025-11-18 04:48:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac348b51-0eff-3415-903c-d1ea0050f8d5 | -3.87036 | -51.27918 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5cfd284-20f5-3c6c-b145-814a7ba800cf | -2.53353 | -58.02687 | 2025-11-18 04:48:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bb3c16a-f815-34cc-8091-4132dcc8c725 | -4.9389 | -49.82647 | 2025-11-18 04:48:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0cb805f-6a11-3f7d-a395-04ec48f02389 | -3.4942 | -50.3428 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90289926-587a-3439-9f2d-854e7c143c64 | -1.43046 | -48.92241 | 2025-11-18 04:48:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11cc6bba-4f3a-39b2-8640-4974ee2cafb4 | -2.78746 | -50.31961 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e85e7ca-9407-3ea5-9ccc-e5a5103e9f77 | -3.40882 | -46.90502 | 2025-11-18 04:48:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14dd9106-15b5-3073-8233-691ba091334f | -4.67623 | -45.79847 | 2025-11-18 04:48:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9119315a-7053-3756-89ee-7cf1cad91065 | -4.18482 | -44.2364 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c855018-c1a6-390a-a9c7-7d45ee624085 | -1.41125 | -55.74654 | 2025-11-18 04:48:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc4e02f1-bf64-37b0-a121-a0c60107a2eb | -2.33732 | -56.07616 | 2025-11-18 04:48:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b83231d-66c8-33e2-aaa5-4e97fab2c8bf | -3.5065 | -51.60857 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e587ff5d-a1af-315e-9069-11ee275c1066 | -2.56407 | -48.53074 | 2025-11-18 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df12a08a-916e-3f0a-ab86-486e325e7afc | -3.75861 | -51.80569 | 2025-11-18 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b81b37b-a5c4-3e02-a029-13b9aae8b078 | -3.17341 | -48.60873 | 2025-11-18 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb249e78-054b-38ff-807e-c885fc64fa47 | -4.40662 | -45.83139 | 2025-11-18 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e94757b-d6fe-3fbb-946f-84f47c8eb045 | -3.23236 | -50.49915 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d798a1c8-6a11-3b59-a954-4f1eeaa9a770 | -3.22318 | -50.96593 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c38d7907-2545-31c9-9194-7be6013e599f | -2.39795 | -55.70458 | 2025-11-18 04:48:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3eb0b573-a6e2-3e38-86b4-4e232a16f02b | -4.17602 | -44.235 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2357942e-ea2c-3d5b-b4cc-5e6a0b2f2c44 | -3.79912 | -50.12593 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e689a59-099f-3f5c-b84e-701c1b5593f4 | -3.78356 | -45.59417 | 2025-11-18 04:48:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7d03723-7e76-3a35-ac88-02116567fe2b | -6.08914 | -49.8964 | 2025-11-18 04:48:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6909bf20-bf10-37d8-8530-48a0df2d9042 | -3.14134 | -49.89827 | 2025-11-18 04:48:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb83e790-a87f-3f1e-b4e1-cf8ef83aa5bf | -6.93525 | -39.62906 | 2025-11-18 04:48:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f31f2761-7373-3a5a-8d33-cdddb4684fd6 | -1.31064 | -54.18634 | 2025-11-18 04:48:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5cf5d4f-d485-3bd0-aba7-9a5f41775050 | -3.60585 | -43.60619 | 2025-11-18 04:48:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d2f7c92-6385-3006-8edd-e35cb6cad6c0 | -4.02278 | -45.54604 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25ea7a02-efa4-3762-9aba-6a2393d93108 | -3.29976 | -50.67307 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8a5d1fd-98cb-3009-909d-4f58a168a176 | -4.19933 | -44.22973 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 71e95252-c1bf-3053-86a4-5b6f41945751 | -3.06584 | -51.52473 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0314783d-16c2-3d70-8517-1a0ce743dc71 | -5.47437 | -44.69007 | 2025-11-18 04:48:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df641f80-36e4-30ea-93b1-a26b7ddacc71 | -3.38297 | -51.0235 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94110381-b7a2-3b79-892f-7b08c831cf6a | -2.72751 | -48.71504 | 2025-11-18 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 844bb577-4e81-3ee1-96cb-785ee7ee55e5 | -5.09445 | -56.16493 | 2025-11-18 04:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 211140db-89a1-3634-9ebd-94f209e60596 | -3.87335 | -47.17821 | 2025-11-18 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5858fada-8b61-3563-8dab-532d9a5388ef | -3.40381 | -50.18747 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4db66d44-632d-3eab-926a-33ab6f201dad | -4.6505 | -46.53746 | 2025-11-18 04:48:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e9e50d8-064f-3e1c-99ad-8213f1fceb8d | -2.48889 | -49.33759 | 2025-11-18 04:48:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b236749-371a-3e6b-b685-38581d2091b0 | -2.45592 | -53.80316 | 2025-11-18 04:48:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32310bc5-9bf6-3cad-af93-fd89a033d17d | -3.24966 | -51.03129 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9aec629-1881-3789-8e42-178cb9d05c65 | -4.01556 | -47.41905 | 2025-11-18 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77a9f92d-f6a7-3ead-b84b-40bde92aab58 | -2.44085 | -49.22988 | 2025-11-18 04:48:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b2dfe90-d30f-3c8d-b37a-34e30e8ba757 | -5.63488 | -43.92902 | 2025-11-18 04:48:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 719a8db5-cde7-3fd4-a9d6-b846620a097f | -1.92354 | -48.80355 | 2025-11-18 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 0bc64a63-52a0-3ac1-b683-33235d029276 | -3.39995 | -50.1904 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 091d45f2-0bde-3071-8395-c43675883780 | -3.01104 | -44.38332 | 2025-11-18 04:48:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ea78a4f-3473-3f94-a934-97d43c69d086 | -5.20541 | -50.62971 | 2025-11-18 04:48:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8c14bf2-275e-3ff0-be98-df5f3bea7682 | -3.48797 | -52.35977 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eebeceb6-cf70-3a32-9a86-21a8f0111947 | -3.07576 | -50.22735 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae9f3a0e-f5a8-3276-bead-91085fed6113 | -3.42232 | -51.65409 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f09309e9-7d5c-3cf8-859c-53d7ba876c09 | -6.5578 | -42.70477 | 2025-11-18 04:48:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f89972c2-3c9b-3033-a236-b6b7f56b6b94 | -3.81019 | -51.34159 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 05ddf90b-b8ee-36ea-b510-f91022723d56 | -3.56193 | -47.30944 | 2025-11-18 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45d673f5-a1bb-3234-aa62-050c6d414156 | -6.21219 | -46.88324 | 2025-11-18 04:48:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb2033ba-b38b-319f-ac55-90e5356badb0 | -2.85833 | -49.61266 | 2025-11-18 04:48:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fcfc8610-4722-3b94-83b1-61eaeda4d4e2 | -1.41983 | -48.90277 | 2025-11-18 04:48:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4dc77e6-57f0-3b96-be9d-d16bd464d234 | -3.64229 | -50.84006 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9bf7dfe-657b-3881-aa4b-172a07439282 | -4.97985 | -41.85873 | 2025-11-18 04:48:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7fa19f2a-0d63-3299-bd32-b5ff31deb0c1 | -6.67788 | -42.03628 | 2025-11-18 04:48:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f9b2d30e-96ad-3357-a5d4-252304787c46 | -3.25319 | -50.68996 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a47e7863-2bcb-3104-aab1-f2e0314af0c1 | -3.30216 | -50.07908 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 410900b1-44d8-3489-955f-f1d36ab57713 | -3.17841 | -46.60598 | 2025-11-18 04:48:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4928d5cd-29d1-3d59-a9f8-e092411b4522 | -5.15114 | -47.24873 | 2025-11-18 04:48:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fab3e9f6-5ca2-3b62-9318-94ad4b82368d | -3.5246 | -50.34403 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7094291c-9bbc-3edf-a152-4ec54cf4d537 | -3.19169 | -50.64843 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 145a7c9d-7951-355c-87ed-3a373dfa9849 | -3.17637 | -48.02541 | 2025-11-18 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 07a13f47-6987-34c2-80bc-e7188c6adb66 | -3.12755 | -50.15777 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2467e805-3892-32ea-9b88-e4cec958752a | -6.36463 | -46.15516 | 2025-11-18 04:48:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f71b0553-f07f-3f11-8913-e8f54a2aac08 | -3.17469 | -46.60542 | 2025-11-18 04:48:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68b28802-4728-307e-954e-00d19dfc14e1 | -6.41081 | -47.20221 | 2025-11-18 04:48:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1a5d68b-f7de-3155-91db-fabf76111e8e | -4.14174 | -46.76283 | 2025-11-18 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d295a764-deb6-3443-89a3-d87bc8773d94 | -4.64514 | -45.65239 | 2025-11-18 04:48:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36e32eb7-5f4c-3e99-bc47-7047935db21a | -2.91971 | -47.84324 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48c9939d-e9b3-3a4a-a8c5-de583ac77753 | -5.73918 | -46.28908 | 2025-11-18 04:48:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19a328c6-af3c-3c50-9fa4-f7ae1ff771cf | -2.98146 | -51.0817 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01444ef6-d315-38d6-828e-d61188a4df31 | -6.71962 | -40.80302 | 2025-11-18 04:48:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| d15b4de3-8c48-3d2c-a1d9-364a41d827f5 | -3.8364 | -52.29887 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90698109-b547-3ff0-acc0-04ab8290aef0 | -4.18922 | -44.23709 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a94a870c-3234-3dea-8d41-0abbd502a095 | -3.9356 | -52.18211 | 2025-11-18 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f97cadd-89dd-3d31-8602-918aaeb10fe7 | -3.14881 | -51.49083 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e2e19e8-1858-32d0-a7b8-db7b09e09983 | -4.13799 | -46.76227 | 2025-11-18 04:48:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af831b4b-0ad1-3562-866c-eafc1ebe05cc | -6.54862 | -46.9032 | 2025-11-18 04:48:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adaa4968-85bc-3ec7-afef-98f13570c019 | -5.57644 | -47.08937 | 2025-11-18 04:48:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0047b3c1-fcd0-3fb0-a113-7c8708e03cf6 | -3.83298 | -52.29831 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00b72c1b-aa39-30ce-bc4e-27b5d27560df | -3.08045 | -50.34814 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33b9c5a3-10c6-3786-994a-558207a38110 | -6.11426 | -46.18553 | 2025-11-18 04:48:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59b8c5f1-4b96-3fd3-8490-88bbabe89b12 | -2.85998 | -53.01146 | 2025-11-18 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4601347e-ac88-3b3a-a699-39bb4159a93d | -2.49446 | -49.3456 | 2025-11-18 04:48:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a99c6311-114b-3bd6-849d-1201143ca4c0 | -4.19491 | -44.22913 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c216fafc-e23c-33fa-a855-3249a2bbbc74 | -6.21982 | -46.88445 | 2025-11-18 04:48:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 113c39d0-1aa8-3140-b388-7f9b0ebe16bc | -4.35177 | -44.34921 | 2025-11-18 04:48:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README36.md)
