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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ce4ce6a-4397-38f9-b4f2-e893d582dd1e | -13.23067 | -48.50365 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 342f2512-5f73-3945-bbaf-6515b683adb6 | -18.60569 | -50.69909 | 2025-10-02 04:32:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1a77aa1-f125-322e-8101-1b46b3aabe83 | -16.0393 | -50.86488 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1749ba10-9cc7-3579-a359-221e7a4ab1b3 | -13.40375 | -47.78085 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32b21e08-6240-39ea-9de4-cb8cd30db6dc | -15.25948 | -49.309 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a7c28c27-d599-3aac-803f-b07db607b1e8 | -15.98798 | -47.35436 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f8e58c8-a4d4-3f18-8d4f-db79a00cd541 | -15.18219 | -46.41422 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 774ae0a9-9011-3944-879b-e47dd4feb24c | -15.28017 | -49.30894 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2972daf-e877-33d3-b874-bb64469d1acc | -13.40539 | -47.79204 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3e597313-696e-3312-9c9c-d8e7141433a3 | -17.70548 | -46.88646 | 2025-10-02 04:32:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38427e8b-6350-3f5a-8823-bec4f5ebe93b | -13.06586 | -47.02086 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 930677c8-3b7a-3095-bafd-642f3c96bfdd | -15.21194 | -47.99918 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a3f71b5d-db3f-3548-a175-9919ccb3bece | -13.23401 | -48.5042 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d343bfed-ed29-315f-93f1-7c80b01cda9d | -15.83022 | -46.25789 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad61ddb7-57a5-34c4-be32-96f64858e972 | -14.34951 | -43.84464 | 2025-10-02 04:32:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| faa41a86-95e2-35bc-a7c0-023e9b4493e2 | -18.63526 | -50.68797 | 2025-10-02 04:32:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b57ac6e0-653e-3f64-8a57-ab01d110257d | -14.68815 | -48.10796 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 197b3b60-3225-3ae2-a545-cd33425d9d9b | -14.87646 | -48.13502 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 740731a5-2eb6-3155-94d8-dcadd79b26ec | -14.78869 | -46.99491 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 676ba055-0a74-3446-bfea-86b28e9e7fc6 | -17.95043 | -45.03537 | 2025-10-02 04:32:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15de9357-0d50-3efd-9e01-aceafa10d5d7 | -13.29087 | -47.2513 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 96655346-1df3-363b-8983-a600c717c800 | -13.34606 | -47.80051 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a36dcebc-843a-3e30-9166-77bc60328d0d | -13.42203 | -47.79477 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c4ace03c-01ec-3de2-bb3d-a2a8390ce2ff | -13.06529 | -47.00235 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3900871c-9e43-3928-b870-7baa0d2b3005 | -13.4762 | -47.2519 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5148ca7b-9525-33cc-aa2e-5def5377342f | -16.02648 | -50.91955 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 68fdf108-b7bb-3f38-88b8-0263a8ce8a85 | -15.26012 | -49.29442 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e42e7b76-1e1e-380c-a2ae-0566de1d2e4b | -13.24806 | -47.30641 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80a3cae9-3fda-32d8-8de6-9e98dd830771 | -13.15779 | -47.83862 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b135880-916a-3417-9c24-75400da23b09 | -15.41231 | -47.04366 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3332ea84-abe4-3ab2-bb3f-3b57979935b8 | -14.67509 | -48.22625 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 736ac62c-5459-3f26-a33d-5ee1baf19afa | -14.88823 | -48.31253 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ff9e80d-c68d-3b99-b7df-322f1476a3ce | -13.78596 | -48.05833 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| df0b49e7-ea2c-3e4b-90a1-9c1d6b21f430 | -15.26247 | -49.29072 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2fedc2e-b0f9-39e6-ab1e-b98e5fa10e29 | -17.95039 | -46.80682 | 2025-10-02 04:32:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccaeb9e0-2088-35b8-8b11-65d3641093af | -18.44673 | -44.4958 | 2025-10-02 04:32:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79f834a6-a7d3-30d4-93ed-7eb96a694f44 | -12.90045 | -46.91375 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41b4e07f-5b68-3162-9cfc-2eb1e50e94b2 | -14.8737 | -48.13089 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ad15989-0042-3124-aec9-03c1b3c9c303 | -14.21749 | -46.09345 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c01f77e-72c6-3c12-90a3-6e5a609dd36b | -14.36566 | -45.94543 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 907f82ae-1020-3b26-9682-2d25e2345cb9 | -15.25754 | -49.2677 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 125593bd-d7fb-319e-b260-0509a1d8f4f8 | -14.85499 | -48.29276 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab138f05-26da-3ac8-a819-06aea06d1576 | -12.257 | -47.80108 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9bc40fa-8b85-3631-b2d6-a3699f468739 | -14.21751 | -46.11682 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95b1de53-99a5-3494-b8cc-6bad9872e6ff | -14.91041 | -47.2206 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1381ce28-d7b1-387b-8f6a-773a5af35711 | -19.96001 | -43.65539 | 2025-10-02 04:32:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 5b49ff06-a535-3112-a44f-d34165c97b2b | -13.75223 | -47.99069 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d51ccf13-86f1-3ae8-947a-0b5025120eb4 | -14.59162 | -48.32991 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62b5fcbf-cb5e-3d95-a631-bee30f201dbc | -13.36934 | -47.80433 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed79f13c-8ef4-3959-be22-5c6e71860f01 | -16.03412 | -50.91686 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f66af535-81eb-3fa9-97d8-643a8ec3e96d | -13.68191 | -48.07347 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 054e36fc-bcc6-3e40-a5ca-18d9c1a8dc98 | -12.43131 | -45.16825 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8748ef14-ee3e-30e8-add9-cd37febb1d96 | -16.04361 | -50.88183 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 698fedab-adb7-33f3-86db-b4af28a5a971 | -16.04409 | -50.8577 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fa7d0e9c-0056-3a27-8540-1ec9af16cf65 | -13.14955 | -47.7827 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81979bfb-d666-3a1f-99e5-3a5338aa54a0 | -15.19996 | -48.16262 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3933be9e-77dd-3fc1-acf7-e25e9fbc85b7 | -18.60961 | -50.69506 | 2025-10-02 04:32:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a054974-c63e-3fe8-bbf4-9703cb107cf5 | -11.86922 | -48.07553 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac67e4ef-fcf4-3a6b-8962-6b9553f864fc | -13.45841 | -47.25616 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5bb7929d-e4c2-3827-906c-13db2fe6ea13 | -14.69148 | -48.10851 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 989b0a59-118d-31f9-be42-97aa945b3a7d | -18.8461 | -43.14538 | 2025-10-02 04:32:00 | NPP-375D | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| e4a9df84-4dc0-3bc7-a5d4-9cbfef5846d0 | -15.21548 | -47.16724 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13d07dd4-427b-3879-80d2-06fed8ee5f68 | -14.47675 | -48.43498 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 749c0365-041c-3b9a-8e71-b0bd87a5f224 | -12.68165 | -48.57111 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ffacc51b-c0a3-309c-a2bc-91549c6eb12d | -18.3419 | -44.50484 | 2025-10-02 04:32:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25394106-80ce-338e-a42c-1ad1c82ca43b | -15.93309 | -43.33859 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82a27e90-5f7c-3092-883f-483e1af6ba12 | -12.66534 | -46.85785 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1770fbdc-3a13-3151-b172-98777f61c2b5 | -14.22154 | -46.11352 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4918888a-ee8f-367d-84a9-c09785e18cbc | -13.22246 | -47.85317 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2b6c92f-dd6f-30cb-b3fa-3352a36e4f91 | -14.42764 | -46.10856 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 613dd085-3dfa-3b01-9a72-00ddbedf2cad | -15.12077 | -48.49097 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea2ac756-929c-312a-b857-af0654543d89 | -17.55935 | -44.80103 | 2025-10-02 04:32:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 132af504-7b3c-3bfe-b14f-6d7e18c7659b | -17.08818 | -48.56026 | 2025-10-02 04:32:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f425437-849c-3b57-9f11-98be5ba4637d | -18.50797 | -44.04146 | 2025-10-02 04:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 00a974a1-1f3c-390e-a34c-b3b6fa57f270 | -11.85317 | -48.0474 | 2025-10-02 04:32:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 409f3141-f2bf-323c-b7e3-cf119ed31895 | -15.23613 | -48.7271 | 2025-10-02 04:32:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c3d082d-a82a-399f-b900-3a05f51d9bc8 | -15.93668 | -43.34276 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0df9cc6-ed0b-30ac-993b-8234be262ce7 | -14.90313 | -47.17825 | 2025-10-02 04:32:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d81fabb1-fb5f-3bf0-bc9a-526953a3703b | -13.95363 | -48.12925 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 131bfff5-56c0-3a62-bc15-9e12242686a3 | -15.21138 | -48.00276 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a3427dc0-249a-3357-9d95-ec77d15d05f7 | -12.85918 | -46.93649 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23336aea-6842-3a50-9878-4975b5c9cb97 | -15.20329 | -48.16318 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc6d055d-0104-37a4-84d9-e36e86c8ceca | -14.65338 | -48.26329 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23948f6b-a36c-36db-8456-85d2ede7748d | -13.78107 | -48.00276 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 550dfd50-b941-3959-b5cc-b542724220fb | -14.50656 | -48.48397 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12c1d957-36a7-31c6-8e68-308444b9cd0e | -12.41267 | -54.3656 | 2025-10-02 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3368e26-f9f1-3564-b617-0a2ac62a8243 | -12.2146 | -47.79359 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b389e822-c015-3ff8-a6cf-8cc0f60eba39 | -15.34938 | -47.08713 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e8dabfe4-f40a-3b7d-a76b-fa24ce6f5244 | -13.69958 | -48.62188 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e66c022c-913a-35f0-9029-69de2162d6dc | -13.15891 | -47.83152 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8e787ed-5565-313c-b93b-c2eb805aa28d | -12.06283 | -47.9832 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 806cf600-e7d6-33b2-bdc8-b0a501539aea | -16.03128 | -50.9124 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2de31f40-3786-366e-bb5d-79d54b654ee9 | -13.38165 | -47.3173 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 106c45ce-c17d-30f1-81b3-83696e837a73 | -15.26068 | -49.30169 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 826275ad-9dbc-3b4c-9788-ffbfd7c6f326 | -13.32032 | -47.205 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b396349e-9540-3429-92aa-3c28a38b866d | -13.08315 | -46.99784 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04c211de-8276-3f28-9fad-8813868944ec | -13.86931 | -47.9549 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aff29245-2d0e-3112-b956-b09928aba111 | -13.38704 | -46.94997 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3515882b-1ca6-31c3-845d-9a54538e612d | -19.98041 | -44.25851 | 2025-10-02 04:32:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d38b60d4-363b-3bf7-a5f0-42a6aad261f5 | -14.21463 | -46.1125 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |


[Clique aqui para ver as próximas entradas](README80.md)
