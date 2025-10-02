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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6488af7a-8c13-3cdd-8d19-ead16fdcee59 | -19.88647 | -42.62695 | 2025-10-02 04:32:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| b98a2018-9231-3f76-9b5a-1ceedd0311c0 | -16.02581 | -50.92352 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0f38f388-8c99-3ddd-b4d0-73da1d126cee | -12.70946 | -48.5905 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef9ce1de-cc7d-367b-8720-0efca14c8493 | -15.23458 | -50.11329 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 84391d5b-dd22-341a-aba8-14a075af71d0 | -15.25953 | -49.29809 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d015ed50-b502-3198-9206-140d71297b00 | -12.42872 | -50.16549 | 2025-10-02 04:32:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b39a393-ce25-3619-96a2-3fbcfa1176ee | -11.45978 | -51.50733 | 2025-10-02 04:32:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3012305-fdfc-370d-9077-66501bc37e93 | -15.83953 | -46.24316 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3e46ade-4b7e-3c39-8796-db95127b6428 | -19.04848 | -48.13399 | 2025-10-02 04:32:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04876750-ce80-37fc-9bf5-6e133ec3869e | -15.46479 | -45.88288 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c445eed-944c-364c-bc9f-c4dc60da7933 | -12.24617 | -47.83138 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b46c2760-7aa9-392e-8c34-d0a3ed73e418 | -17.66874 | -48.15215 | 2025-10-02 04:32:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 458fcf9e-c58b-3f31-ae91-e7a4a6f48d2f | -13.64456 | -47.19376 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76c587d9-41b2-3d8f-a0c8-2302c57b44f1 | -15.40161 | -47.04566 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2865f69b-b6a1-348b-b886-ed0dd7f358ca | -15.92971 | -43.30095 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e93d360b-119c-31a9-9c2b-cdce8d54b224 | -14.31303 | -45.98879 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 843bd79f-f639-3be6-a8d3-35ec3ca440a2 | -15.40893 | -47.0431 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ea5c883-5b28-3f3f-90c3-ca4ab575d8a4 | -12.8496 | -46.86489 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e79a37b7-a1b4-3108-8e2c-a1e9fda425a8 | -18.72606 | -47.54384 | 2025-10-02 04:32:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ec678cd-7e5a-385f-a89f-b72f41555439 | -14.57837 | -48.30574 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3645705f-7137-3001-8ed4-dc3127b64c3e | -15.27012 | -49.30717 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30ad4eba-8a6f-3966-aa1a-24f7324acf77 | -15.22389 | -47.18008 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f744513-288f-3c9b-82da-f8f528176a86 | -13.16725 | -47.82197 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1d75cc9-3270-3980-8107-228b95b744f2 | -17.17294 | -47.03131 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a6d29da8-391e-3553-9a0d-ccbb4969f542 | -14.32341 | -45.96669 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2b8de11-36cb-3f38-bf43-eaee59b0aaf0 | -14.21173 | -46.10831 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8f419b4-54fd-3321-a78c-49fe7418908c | -15.75997 | -43.66899 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a9556e6-e906-35ae-aca3-82239c84699f | -13.19554 | -47.83754 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22521ab9-f105-377f-a0cb-48ed4331a5d5 | -14.65428 | -48.12793 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 678a7f8c-f626-3a61-b99c-f69e9dabab11 | -14.64617 | -48.26575 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e2d814c-57ec-324a-a764-301b6e6a5a3a | -12.67495 | -48.57001 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b84c4131-5307-3eab-bd55-4b898cf17d69 | -18.60558 | -50.69823 | 2025-10-02 04:32:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08aa3600-321e-3980-b87e-d7415b1e85f3 | -12.813 | -47.01327 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 308e9ded-170f-3ae0-a189-500c0008667a | -15.25165 | -49.30426 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ae8e01fb-7d08-3df2-8d6a-e61af1c509f0 | -14.30724 | -45.97999 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32fa52dd-2006-36af-a75d-be426ef94315 | -12.84079 | -46.94436 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e88a2072-366d-3311-90a9-9faba3470b05 | -16.28374 | -42.54502 | 2025-10-02 04:32:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18536478-bea5-3461-ab8c-25078c960982 | -14.36911 | -45.96976 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a3ffb86-043d-32cb-86a0-6e365b3f7d6d | -13.96035 | -48.10844 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 254e8613-daf1-319a-b219-1dd7ce714fee | -14.89418 | -48.36119 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ff11483-9981-30ff-9d77-69fe88c19cbf | -13.64984 | -47.65654 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 68368fe0-bacf-31f8-89fb-51c990de3343 | -13.51182 | -48.20627 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98e4b1bf-3139-3e68-af26-51f0e17d1888 | -19.69378 | -43.98959 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbdc6002-c64c-3af4-8ee9-c0aa9b6d6209 | -12.15248 | -46.67751 | 2025-10-02 04:32:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd361a9f-6121-31ac-bd27-2bd49738b78e | -15.15605 | -48.3977 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c876bfcf-a1ae-3e45-9756-856be68b3d94 | -18.19409 | -53.30627 | 2025-10-02 04:32:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d73ec888-35df-3a46-b463-409e5ad87b1c | -14.43206 | -46.35546 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e4c4e6b-c030-3f90-a2f4-53a3cf1123ab | -15.14305 | -48.02451 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddfa9570-d6b8-3860-9d17-7fa85792f67b | -13.8126 | -47.54033 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 90b91cc6-dd60-3f4b-a8b5-1a135b0d8434 | -13.54867 | -47.28144 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 515d3301-ce06-35d9-845d-262c211aa304 | -14.42244 | -46.11969 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8a6b36c-5385-30e2-9ef6-3ef1df2faf85 | -12.6351 | -44.85727 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2efb625f-b2c6-35d0-a385-d19d2252e5b4 | -15.019 | -42.22353 | 2025-10-02 04:32:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 18aa07cf-e56d-3a0f-9471-44b60c39c5f4 | -12.9443 | -48.43419 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8505e9d-0386-38d6-a348-d671be583995 | -12.69053 | -48.57994 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 84c8c9f9-9edd-30f3-80cb-fdb76f35a97f | -13.16392 | -47.82142 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 105ae030-71fe-3fd4-affd-132237fc5df0 | -12.77289 | -46.88233 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1d1c4c0-dc24-34ed-9d79-e910c407c238 | -18.50327 | -44.04599 | 2025-10-02 04:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 15694c88-bd05-3548-aacd-82d76c066e18 | -15.39492 | -49.18312 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b78ea96-61f2-3e76-a8f3-ef3c6c629960 | -13.77653 | -48.05312 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e32471be-a57b-323b-9635-62c1dbf22b9d | -15.34699 | -46.26968 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d24535f7-f4ef-346c-8fe0-fd1b16bdefe9 | -16.05085 | -51.03157 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5fc772b-671b-37df-ab3f-3489b8a2b678 | -13.75889 | -47.99179 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fa50bb13-dfcc-336a-a4dd-4cf48a7d7677 | -15.79354 | -43.73468 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f16211b5-b329-3c01-8633-405794fe697d | -15.24355 | -46.9828 | 2025-10-02 04:32:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7b8fb49-d31c-3ea1-bfb5-1984c4dc5968 | -15.3959 | -49.19825 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50b01ac4-223c-3562-8260-40c97a171329 | -14.21241 | -44.92464 | 2025-10-02 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d61dcb33-a633-33dd-9e77-ac0d4c880980 | -13.16554 | -47.85445 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0442dfb7-d7e4-36c9-8740-af41d5c2d65a | -13.29875 | -50.68067 | 2025-10-02 04:32:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 071654d0-08c0-328e-a8b7-cb940f89ac6f | -14.31014 | -45.98439 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31d4e624-0b50-32b0-ab55-8ff5883a0f0e | -14.8755 | -48.29251 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 637a93cc-f6f0-3ade-82df-8a096b726c53 | -14.64707 | -48.1304 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09e35907-94e9-35cd-9bca-d65f51df9c04 | -16.97695 | -49.17618 | 2025-10-02 04:32:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d72acb12-9f9d-3fa0-9875-d368a0b1b10f | -13.30592 | -46.99963 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0ae9da85-9a41-300d-a49e-d404f7dc89de | -14.36217 | -45.96866 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68a4f2d1-4c81-3cb0-9c05-88c270b5f0ad | -14.31477 | -46.00095 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 45cca58b-e651-3aaa-9861-7e6a937cabb0 | -15.29766 | -46.38811 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bb0056c-f0ed-3a79-afd3-e840056a2ab2 | -19.01067 | -45.00016 | 2025-10-02 04:32:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6925e9a-9ba4-3a6d-a506-0138bbda514e | -19.62916 | -44.90006 | 2025-10-02 04:32:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e4160eba-4e52-3959-bbe3-57369445a8ad | -14.21519 | -46.10877 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c985458-f18d-3936-a51c-38685d3a4d28 | -13.97073 | -44.87121 | 2025-10-02 04:32:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce2c807f-f307-3c17-83e5-fe6362909680 | -15.23288 | -48.08357 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb5e3119-2da9-3a02-8a3b-f7c70fc79109 | -15.23411 | -50.12144 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d4aced0a-fea3-388a-8ef2-84cadf39261a | -13.80422 | -47.51297 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e39cda1c-18df-3378-9ae8-c6629259b479 | -15.23258 | -50.10933 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6edda2d0-8d0f-380b-9a3d-920191ebe32f | -13.94872 | -48.09558 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4f208eb-7ed4-3bfd-84a5-1a411845f88b | -12.58801 | -49.90618 | 2025-10-02 04:32:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3ccb11a-c844-379b-9830-394912711ef9 | -13.17226 | -47.81187 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0321977-b777-3e96-8cc3-527ade85cf4b | -14.27711 | -45.94379 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d525f5c-788a-3a3e-8175-1bfcb09aabf9 | -13.53306 | -47.2494 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61adb8e2-9aac-392f-a1fd-b83eb20d0cdb | -14.44064 | -46.36847 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7de06a8-c54e-3509-a41c-55b56bfb4d28 | -14.71563 | -48.20736 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfa324cd-4c9c-3600-9562-efd03207bd86 | -18.3418 | -44.50649 | 2025-10-02 04:32:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5287ca4-e695-3bd9-8c9a-3fb385c79586 | -14.40748 | -46.07782 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dca37f44-9737-3137-8e7c-2121ac0f2286 | -16.96539 | -49.7286 | 2025-10-02 04:32:00 | NPP-375D | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9a175bb-a0c4-37a3-b58d-770b67ddbae7 | -12.88709 | -46.93356 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fa66e374-ce1e-3882-8901-f8be14fa43ed | -12.70291 | -48.56718 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 347dc82f-ec43-3a71-bf53-f46cac395db0 | -16.02882 | -50.8632 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26f6a7ae-f1fa-398d-bafb-3841264d1942 | -17.39301 | -47.16762 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fea18a0a-1b2c-304b-bd6c-244df4825b0f | -12.57957 | -49.89274 | 2025-10-02 04:32:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README82.md)
