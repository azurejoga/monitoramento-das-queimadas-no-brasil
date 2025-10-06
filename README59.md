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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e44611c4-ba4a-3958-85f8-628a5d818b65 | -18.25632 | -53.36105 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c5520cb-4824-34e0-bf62-7a14cbd9b816 | -18.14621 | -53.39027 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d9c14dfb-6087-30d6-bd97-62be7e947342 | -19.62891 | -45.92009 | 2025-10-06 04:29:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21ea7987-256b-30ad-8de9-4dec734fb668 | -18.39437 | -45.20554 | 2025-10-06 04:29:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c639b8a8-924b-344d-b083-df8aa4b91aba | -19.90365 | -46.79765 | 2025-10-06 04:29:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 625ba969-f0a5-37ad-91ae-9f4e36c60113 | -16.37083 | -51.49478 | 2025-10-06 04:29:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a32d5645-e725-39e5-827f-48f6b994d8d9 | -17.86501 | -57.59076 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 469b26de-abbb-33ee-b12e-8bef38c8e369 | -19.02101 | -45.02311 | 2025-10-06 04:29:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ed3bee90-3ea3-3fca-abf4-647c66a2fe28 | -18.39375 | -45.21015 | 2025-10-06 04:29:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58f5b559-8834-30e0-a7d4-da4c9c602a43 | -17.97462 | -57.58829 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4a2b291e-9ffc-38f1-bfd5-a3603531dad6 | -23.4361 | -45.48045 | 2025-10-06 04:29:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| abb35302-5d04-3fd3-bbbd-2ea9c83de783 | -18.2785 | -53.32517 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcb6fc84-1701-33b6-8786-0ea4235d6a1f | -17.9849 | -57.5923 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 68729b5a-e8ef-35af-b4c1-9068a352a348 | -17.85877 | -57.59607 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f46a5855-7697-37c0-bf69-ccd8236a9982 | -17.90549 | -57.64859 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2b4663ad-cd5a-38e7-a7b0-19675b4e890a | -22.37928 | -50.02105 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 63bd3e8f-7b7d-385d-9902-beda9d208824 | -18.13947 | -53.40181 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b6274229-a87f-3eed-aac8-637514a12478 | -18.44607 | -49.43553 | 2025-10-06 04:29:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45463f75-3d18-394d-b3bf-7056cc16de34 | -22.63129 | -47.71553 | 2025-10-06 04:29:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5c2813d4-5c94-359d-94c9-8dd76de105ca | -22.07455 | -54.13319 | 2025-10-06 04:29:00 | NOAA-21 | DEODÁPOLIS | MATO GROSSO DO SUL | Brasil | 5003454 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c3997af7-f89c-3a58-8e11-9943197d01fd | -18.14438 | -53.40066 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d0e13919-c03a-3676-801e-8846988f33dc | -18.51633 | -43.9214 | 2025-10-06 04:29:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8cd2ef55-bdcd-35bd-aad3-f1c1d506c107 | -20.11398 | -46.35303 | 2025-10-06 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dae847ae-9d37-3127-b078-4c25b605a831 | -18.26544 | -53.33256 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e206a070-bbc4-30df-aa2c-83e81673f404 | -18.26836 | -53.33797 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7935273a-91d1-3338-8828-df3ad043ea1c | -16.15005 | -57.56992 | 2025-10-06 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8784a714-a253-35c4-9de4-274021eef0a8 | -17.97703 | -57.57627 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 26be4bfe-4434-344a-8b1b-721e17011ac4 | -18.5895 | -49.98754 | 2025-10-06 04:29:00 | NOAA-21 | INACIOLÂNDIA | GOIÁS | Brasil | 5209937 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3fa45459-31dd-362b-ac65-8bbf62a92585 | -17.88073 | -57.64289 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6959fe1b-d02c-3f56-997b-9f2f349cc4ad | -19.63255 | -45.92065 | 2025-10-06 04:29:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 528470c0-30b7-3617-84ce-02ec7f7675ce | -16.92119 | -52.04018 | 2025-10-06 04:29:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e3b6d4d-d1e6-319b-bd45-47f84b0eb6aa | -17.96848 | -57.59315 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 075f5136-e2d0-3e26-b486-14d2206efa8d | -18.14884 | -53.39352 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9b9c518d-7a14-35b0-8ad8-6dfa6d6021bb | -22.57821 | -44.87261 | 2025-10-06 04:29:00 | NOAA-21 | LAVRINHAS | SÃO PAULO | Brasil | 3526605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 33ac9a2c-aade-3316-951a-8e525bb0cd6f | -17.2614 | -46.92364 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4abef3a6-c028-3c11-bd83-2993c06fa03e | -22.38681 | -49.97278 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ca1dc244-ac1b-3401-baca-3ba543e765c0 | -21.39528 | -45.07455 | 2025-10-06 04:29:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7790a1b1-6207-3517-a796-7ae7a06b08bd | -16.36099 | -51.48849 | 2025-10-06 04:29:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d9bc34c-a0b6-3865-8348-fbbed9f6be90 | -19.62466 | -45.92402 | 2025-10-06 04:29:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 36d7302d-1ef7-3997-bead-65c5ad774b57 | -22.97406 | -48.35023 | 2025-10-06 04:29:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 04ba0906-4d28-3a52-993a-6db165f171e6 | -18.23068 | -50.93624 | 2025-10-06 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d8aeb6b-1870-35da-b8ab-f526e0f1e9e0 | -17.87176 | -57.58282 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c86dcc20-3221-3fba-97da-749f00b02e84 | -18.54063 | -48.25652 | 2025-10-06 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 740aff88-61b4-3a4e-912a-a7d5e5d52d9e | -17.87581 | -57.64156 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| dd0b62ab-38f3-3876-af93-5d0312489111 | -20.34872 | -47.18348 | 2025-10-06 04:29:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc23d6de-bb31-3d20-9deb-876ed4f4df85 | -21.18981 | -45.15123 | 2025-10-06 04:29:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 62fed734-83b1-3680-bdf3-2a9001954eae | -18.14417 | -53.39762 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 8f291fff-aa3a-36f9-837b-d4326b4d4aca | -21.95069 | -46.45852 | 2025-10-06 04:29:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2a88687f-5f87-3fb0-a5e2-b5f72f9c7ea3 | -20.20352 | -46.14127 | 2025-10-06 04:29:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d576f19-8ae9-3e4d-b337-3732c3b2bba6 | -22.12615 | -45.00776 | 2025-10-06 04:29:00 | NOAA-21 | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 33c1e6f0-c02b-3573-8a62-74ed7029250c | -20.26825 | -43.63889 | 2025-10-06 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ee73e616-85c9-35c4-88fd-2e75918bdd3b | -22.38862 | -50.02655 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 225e5b86-b033-3d3e-9810-3c4e5dc67893 | -17.8804 | -57.6432 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| beb2b0e4-9778-31bb-9be1-a801668bfa7b | -18.27511 | -53.32207 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8b363e5e-0dbd-3a47-b907-ced4391fc2ea | -17.94544 | -57.60495 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 305286b6-2194-3866-82a2-65204a528e69 | -22.97522 | -48.34223 | 2025-10-06 04:29:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1bfe3a88-d608-3edf-89d1-6968f86fabf0 | -21.39488 | -45.0415 | 2025-10-06 04:29:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0e3f6cc4-efa8-3fc4-9b18-9a33e7036f75 | -17.59137 | -44.45224 | 2025-10-06 04:29:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc1cdb20-4e48-3f94-a3b0-60c123bdcc3f | -18.11508 | -53.41089 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b760abac-6874-3d77-817e-fec8f2e5505c | -17.9234 | -57.61168 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 77c3033e-ce9d-363c-bad8-08d840c4b959 | -22.03356 | -45.30083 | 2025-10-06 04:29:00 | NOAA-21 | JESUÂNIA | MINAS GERAIS | Brasil | 3135902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9e2aa359-d636-3afd-8060-6364adedec0d | -16.35882 | -51.47985 | 2025-10-06 04:29:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6f6bf23-fead-3de9-a37a-a38af1d568e1 | -16.95525 | -52.69236 | 2025-10-06 04:29:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 80aada04-eb7a-3361-af4b-fdb90430599a | -22.23599 | -49.02711 | 2025-10-06 04:29:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3bbecec5-519d-38db-94ea-ea2d46f9d18a | -19.50466 | -44.17503 | 2025-10-06 04:29:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f14fdfa-1afb-3a55-930f-38a66f022ab0 | -22.37267 | -50.01986 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0bd9205c-30c3-395d-b8a3-58d4097bf37d | -18.27596 | -53.31723 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 055d1bc8-3634-35b9-9aa8-2b0b647271aa | -21.39029 | -45.04624 | 2025-10-06 04:29:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8348f6f2-4470-366e-adb7-f151e5596137 | -15.87945 | -59.37881 | 2025-10-06 04:29:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c17f1c02-6c5a-3950-bf50-3b342bbdfeb3 | -19.01723 | -45.02254 | 2025-10-06 04:29:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 29345d34-eab3-3bc7-a050-d896872ab058 | -22.98948 | -46.14952 | 2025-10-06 04:29:00 | NOAA-21 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ab427f4f-0fd6-37cc-9b30-2bab0da8142a | -20.20291 | -46.14576 | 2025-10-06 04:29:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6d1dcd14-c23d-357b-91eb-2ff302c5f081 | -19.01929 | -45.03509 | 2025-10-06 04:29:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9d872d70-b9b9-3ba1-a240-11d48084473b | -17.67691 | -52.23854 | 2025-10-06 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e266f31a-be5f-3215-9c7c-c47ab83b9732 | -21.69744 | -50.05235 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 83533603-ba9b-3f72-a0de-4976e4809e62 | -18.99012 | -50.56039 | 2025-10-06 04:29:00 | NOAA-21 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5d5cd574-59e5-31d1-90e8-fda99f9db02b | -16.15065 | -57.56701 | 2025-10-06 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6376a314-56ad-3efb-bec9-813009cce9c5 | -18.14137 | -53.39145 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 53b46593-b5b4-3ad5-9f0f-65987d029791 | -18.14067 | -53.39945 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 76ccad50-d355-3449-aaf4-2acf606819a0 | -19.66626 | -45.92322 | 2025-10-06 04:29:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 05951174-d32b-31d1-9c3f-87bbe14b65c1 | -17.98076 | -57.58337 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 40d26b29-4b64-3f13-ac62-23cb2ade5dc8 | -17.59325 | -44.45099 | 2025-10-06 04:29:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f0ee4ff-ac5a-3e9a-b807-c9cef195d1c5 | -18.26963 | -53.33102 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e88a09ad-a0d5-36e3-a7b8-950f971be60c | -21.61147 | -45.29034 | 2025-10-06 04:29:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 074ddba2-4610-3036-9c47-a13480f75136 | -17.96144 | -57.60248 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a0827055-bef8-3d84-8faf-7750bd75b6bb | -17.89494 | -57.64943 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 306bcef3-2fab-3318-bfac-3fb367f02e0c | -21.40567 | -45.05474 | 2025-10-06 04:29:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 713ed06a-60ce-3c38-bd1f-5d32c7073dbd | -21.60827 | -45.28457 | 2025-10-06 04:29:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| acce4ec4-ac73-3517-8a7f-2de3329563f8 | -19.93659 | -44.63979 | 2025-10-06 04:29:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 0a195ebb-0de1-3cc1-a405-f2013f8ce243 | -22.98577 | -46.1488 | 2025-10-06 04:29:00 | NOAA-21 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| abca98d8-2931-3fac-a461-3e21d63be2c8 | -17.25014 | -46.7846 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44464dec-0532-3f48-aed3-6beffc0aa836 | -22.57121 | -43.64325 | 2025-10-06 04:29:00 | NOAA-21 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c66359a5-79a9-31fb-8dc6-154e6bb8e434 | -17.25823 | -46.80094 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc66dc4f-311b-3537-9f83-2aa02453e73e | -19.93648 | -44.64096 | 2025-10-06 04:29:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 4f8002f8-6864-315c-9279-4acd70ad265a | -18.28037 | -45.41512 | 2025-10-06 04:29:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a507bec-cbae-374d-94da-2007224568ab | -17.25743 | -46.92691 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 996b2db8-f08d-3a87-82c6-0cf7624d19dc | -17.99941 | -57.54729 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 291a73e4-eff3-3b67-beda-b76de15f65e0 | -17.87976 | -57.64642 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ed86937f-f274-30d6-a98f-be41da80e505 | -18.87434 | -48.6082 | 2025-10-06 04:29:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2b34cbd-8d3d-3920-83ac-8063cc7101f0 | -17.66379 | -44.43816 | 2025-10-06 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |


[Clique aqui para ver as próximas entradas](README60.md)
