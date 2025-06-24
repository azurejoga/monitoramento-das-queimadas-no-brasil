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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5dcf5cd-2a46-34d9-abfe-0175c4b477cd | -9.39574 | -48.43984 | 2025-06-24 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4280dcc-cc67-304f-9618-25e38b9b3d92 | -8.57138 | -51.57684 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d91eb752-effa-3617-8705-65fb12f8a533 | -10.28574 | -47.61186 | 2025-06-24 04:04:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f277bc12-a22b-3f2f-bad0-9c6a9cfb24c2 | -14.92265 | -46.3909 | 2025-06-24 04:04:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 775603ce-973a-3b0c-b8f4-4a9362c6a695 | -15.645 | -41.25467 | 2025-06-24 04:04:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b119aaf1-16b2-3ba6-9fb0-335200a27fb3 | -14.16512 | -39.98653 | 2025-06-24 04:04:00 | NPP-375D | ITAGI | BAHIA | Brasil | 2915106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b857e8b4-01b8-34af-9a40-0675cbad5aa9 | -13.76829 | -44.09309 | 2025-06-24 04:04:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88d128e8-9eed-3040-804f-5cbcb527371d | -15.14721 | -42.24804 | 2025-06-24 04:04:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b59e5d25-c1c2-301b-a557-1676f130d53e | -10.06244 | -49.65991 | 2025-06-24 04:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40371fc2-33eb-3081-9a70-4075b595d80c | -14.31102 | -42.82481 | 2025-06-24 04:04:00 | NPP-375D | CANDIBA | BAHIA | Brasil | 2906600 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| e34936ac-c1ec-3899-995e-ae70c9661e2f | -8.36917 | -47.43068 | 2025-06-24 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6cf0032-3703-3f56-abff-6a5028e87be2 | -8.33736 | -48.53026 | 2025-06-24 04:04:00 | NPP-375D | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f5c029a-ff6a-3bb1-a90f-e4bfb15efef7 | -8.06545 | -43.11271 | 2025-06-24 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 53ccea82-5252-397a-9a66-d0fa09512b27 | -10.59732 | -49.64759 | 2025-06-24 04:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9b7b53d-81b7-374b-ae15-d2c294b4bbf4 | -9.40093 | -40.3149 | 2025-06-24 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 69db5eb7-a656-363c-8c49-7f04f04533ff | -14.44539 | -48.91539 | 2025-06-24 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7261de07-de6a-3978-af4a-1e754a10d108 | -10.5819 | -49.64461 | 2025-06-24 04:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb10fd80-921a-3b54-a6a3-acf39f369b6d | -13.50772 | -42.6755 | 2025-06-24 04:04:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7e686ee1-e7bd-332e-b48a-d6d95348aa9a | -14.44084 | -48.91435 | 2025-06-24 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| de9ebce8-8071-339f-be34-b4ef3eb2a2ed | -14.22359 | -42.76897 | 2025-06-24 04:04:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c70d8a6d-dbc2-3a1b-885e-8285c0567767 | -9.3104 | -40.58709 | 2025-06-24 04:04:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d214d6f3-82c7-34ff-96e8-65739167a740 | -14.1963 | -42.7793 | 2025-06-24 04:04:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 418244f3-9d03-3aba-9b2c-14dc610cbf96 | -11.24867 | -49.48915 | 2025-06-24 04:04:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de3c1f5d-b88b-3b7d-bb5e-e8bde446ed89 | -9.34108 | -40.30537 | 2025-06-24 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 19819105-b386-37c9-a83c-e6ba5c8b558b | -10.8813 | -49.55264 | 2025-06-24 04:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1eff5c0d-0094-3119-8bbe-484d3cfaa089 | -14.43626 | -48.91053 | 2025-06-24 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 702acd15-9402-3c84-9210-86cf22e9437b | -12.75254 | -44.40868 | 2025-06-24 04:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 95011027-c243-32f6-9797-4b63b2b6797f | -10.576 | -49.15144 | 2025-06-24 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cc4c835a-39ef-318b-9d5f-8ebbebab6471 | -11.56789 | -47.4316 | 2025-06-24 04:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9e667fc6-588e-3c74-8228-2ff3a7de47ff | -14.38379 | -46.14024 | 2025-06-24 04:04:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 783a2701-bce1-3faf-8f7a-e681a98641b4 | -8.55673 | -51.55553 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 688a8a60-66cb-32eb-a69f-3ef7ae0571f6 | -10.23443 | -44.63743 | 2025-06-24 04:04:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b3f5fca-40a0-3f6e-b476-16433eb8b84e | -8.58777 | -51.58919 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49df6f90-8f85-3511-ba0f-87b5d8049c3e | -13.54821 | -42.4893 | 2025-06-24 04:04:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 07c09ad7-6ce8-3a06-a54b-83540826c626 | -14.2297 | -42.77375 | 2025-06-24 04:04:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a2ad0fc6-c02f-3ee2-a779-00b807373ad9 | -10.58532 | -49.65488 | 2025-06-24 04:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f11e7d88-f3a0-349b-ae38-3f6806b783c9 | -8.97202 | -49.86948 | 2025-06-24 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44fef89c-92d9-3bd6-99e0-4b3f4fac12e6 | -11.93569 | -48.42377 | 2025-06-24 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51756c72-f509-34ba-8ca9-0eb157806c1e | -13.55272 | -42.48266 | 2025-06-24 04:04:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c4df6d6a-5464-357c-a091-5ad3854e3f12 | -9.31502 | -47.79305 | 2025-06-24 04:04:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f403ee79-a119-34cd-98ab-e8668b254b91 | -14.66636 | -41.90901 | 2025-06-24 04:04:00 | NPP-375D | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 12c9fd5f-8f05-3aeb-92f9-090777fa3002 | -10.05725 | -49.65891 | 2025-06-24 04:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48065686-6dc3-3a9c-a468-7cf86fa4fa95 | -8.33835 | -48.52464 | 2025-06-24 04:04:00 | NPP-375D | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be1703c4-6446-36e9-92e0-aa9a75c929a2 | -8.55975 | -51.56534 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 720f99b7-537e-3d42-95bc-bd321e6ac7c4 | -9.13105 | -47.58475 | 2025-06-24 04:04:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46192683-cc5d-389a-881d-157e26cb3a7d | -9.64385 | -48.56682 | 2025-06-24 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07329247-c344-3f9f-bff3-310faabc1145 | -12.7554 | -44.41346 | 2025-06-24 04:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78e12201-8c7b-3ec0-846f-25c27307f6bd | -9.12647 | -47.58385 | 2025-06-24 04:04:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c73e33f-a5e7-3292-b65c-c2283713d5a4 | -14.44081 | -48.91156 | 2025-06-24 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd26561d-aef3-3645-a917-5a510b6e2c5b | -8.06255 | -43.10809 | 2025-06-24 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| a9584233-ed9c-3f96-a6b0-ef6b8d084cb9 | -10.87623 | -49.55161 | 2025-06-24 04:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e81b6b11-a48b-3f4d-9d2b-2da1bce6b1db | -12.40396 | -43.80403 | 2025-06-24 04:04:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df69d471-6eec-3ebf-befc-2d456b4e0f06 | -11.56185 | -47.91684 | 2025-06-24 04:04:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acd90fa6-6fae-37d2-9449-78c209ad292c | -13.73852 | -47.74455 | 2025-06-24 04:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d4f473b-be8c-33f5-b93c-dcecbf413f85 | -8.87158 | -47.26956 | 2025-06-24 04:04:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f93f272-4247-3524-a599-a111e985d508 | -9.41412 | -48.42102 | 2025-06-24 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| abf0b5db-e7ff-376b-adf1-4dde280cf1c0 | -7.86796 | -47.87741 | 2025-06-24 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 338c919c-92ab-3a45-9ba0-d004f890391e | -7.4496 | -45.57775 | 2025-06-24 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 381e2af1-aeef-3e98-962b-bf9e625da1f9 | -10.084 | -52.74911 | 2025-06-24 04:04:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 66b7e44f-f6d7-35f7-8f22-85740aa9e77f | -12.24771 | -46.68505 | 2025-06-24 04:04:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c162321-5715-3220-9db5-7df55018f6cc | -8.06479 | -43.11674 | 2025-06-24 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 8bbb96e9-61d9-391c-9358-ce3c4425ac1e | -9.17387 | -40.5513 | 2025-06-24 04:04:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f4219df7-39b7-3c3b-8e87-eed25da2d556 | -13.76763 | -44.09703 | 2025-06-24 04:04:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 536812b5-1e13-3358-b626-bf7ae67f7eaa | -8.98338 | -49.8681 | 2025-06-24 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 108451f1-50e4-3029-99ed-a825cf7a0fc8 | -10.51622 | -46.93169 | 2025-06-24 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dafe2c2a-63d1-3525-9c62-3c23251d5238 | -15.30594 | -42.01772 | 2025-06-24 04:04:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 52bd32a9-dac1-34a8-93ed-0200c1890748 | -14.44443 | -48.91735 | 2025-06-24 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7fb8c1e0-5146-3add-8be9-bb5b567291fc | -15.30353 | -41.39962 | 2025-06-24 04:04:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7602a2e8-f8c6-324a-ad14-d7c3bc30d7a0 | -11.61058 | -47.61993 | 2025-06-24 04:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebba56fa-545e-3979-8ccc-7779bcf99a77 | -7.31275 | -45.77733 | 2025-06-24 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dec545a-5695-34e2-bd78-061bbd2ee361 | -10.06303 | -49.65672 | 2025-06-24 04:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f34aa9cf-1180-36a5-8b23-1b7ef91aa1d6 | -9.39116 | -40.46025 | 2025-06-24 04:04:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7c99724d-1812-3cdc-a435-421696264d39 | -12.28559 | -48.80245 | 2025-06-24 04:04:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2490f1eb-9f1f-3846-8651-3ea463a1e406 | -10.59161 | -49.64968 | 2025-06-24 04:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb443894-ce4a-32cb-a13b-ebe1a55ab2e6 | -10.0777 | -52.74782 | 2025-06-24 04:04:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 978fc217-7bd9-363a-b348-9e29c0fdf635 | -11.94032 | -48.42464 | 2025-06-24 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df7d0abd-f5ef-3d92-9737-0d3b4e0d0c25 | -8.55587 | -51.55999 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 092db38b-e193-38c0-ac6d-eff4658544c2 | -8.059 | -43.1075 | 2025-06-24 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ec8a1c14-d537-33bf-aaf9-6af07c7f0043 | -10.65216 | -44.49181 | 2025-06-24 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6826767f-cbed-3f89-a4a5-3d27c5429524 | -13.63666 | -41.85176 | 2025-06-24 04:04:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a58628ff-1727-39c3-ab8f-42029492f1eb | -14.14401 | -42.74055 | 2025-06-24 04:04:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 74451e2e-de47-3671-bf3b-59f002886ed9 | -9.11723 | -37.12349 | 2025-06-24 04:04:00 | NPP-375D | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fc75d462-9a0c-388e-8203-db5d9f07a60b | -14.20008 | -42.7986 | 2025-06-24 04:04:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0568b2fb-9c94-312e-95da-16719c38ab7a | -13.76766 | -47.75497 | 2025-06-24 04:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68d21012-04e9-34d0-ba67-a333fa42aecf | -7.85699 | -47.11418 | 2025-06-24 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d5ca0b5-4bce-3d8f-bc9f-d84753ff4092 | -13.07612 | -48.83477 | 2025-06-24 04:04:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d019ba87-12b2-3253-880b-ace504abea64 | -11.098 | -46.65048 | 2025-06-24 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d26469eb-a101-38e6-9e34-3a8beb0206d0 | -9.31964 | -47.79404 | 2025-06-24 04:04:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa06bb8e-017a-3938-a707-2c69b2a9c122 | -13.73356 | -47.7474 | 2025-06-24 04:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6567f127-0ce1-3b20-82be-283220474383 | -11.0931 | -46.65378 | 2025-06-24 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bc0aad50-ec17-3206-8385-e1f59542daba | -8.24233 | -44.95334 | 2025-06-24 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4556df9e-686a-3169-88ca-c9c7ab40cb70 | -10.23818 | -44.63804 | 2025-06-24 04:04:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 65ac1bd5-b797-3a0f-a11a-a9c86756f836 | -10.87174 | -49.54753 | 2025-06-24 04:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 461d6ad4-f0d0-3b65-81e5-81b56108670b | -8.58943 | -51.5804 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65947ea3-51c6-3547-901e-6e8d878eb094 | -10.07872 | -52.74262 | 2025-06-24 04:04:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a5457d62-d43e-3a60-b2c9-ed8fc768eb63 | -8.55538 | -51.55524 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5712ea3f-0e35-3ca9-a78b-c85237775d93 | -8.24317 | -44.94841 | 2025-06-24 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59e68a58-3556-341f-b5c5-267fffee6fe5 | -10.87681 | -49.54853 | 2025-06-24 04:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3334740-0df7-34e3-8276-c8d86bb7a3bc | -12.89353 | -43.79138 | 2025-06-24 04:04:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c280cf3-2c18-3a07-b616-71479eb406ad | -8.97738 | -49.87051 | 2025-06-24 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README10.md)
