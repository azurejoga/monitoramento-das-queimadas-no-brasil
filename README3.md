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
| 67b0b967-ea31-3766-a37d-15c1ec5b3ab5 | -9.57869 | -44.59697 | 2026-01-18 04:27:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 24c2e46d-25a9-3222-8238-749d8ef4277f | -8.07949 | -35.4192 | 2026-01-18 04:27:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4faf0ca6-cd98-3220-89df-cce53309488b | -11.20346 | -47.57018 | 2026-01-18 04:27:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c9786de-6c42-36c3-8501-5fabe094be11 | -6.02788 | -44.32972 | 2026-01-18 04:27:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5529d627-ad95-3a54-957d-f4f78857d90d | -8.56221 | -46.03177 | 2026-01-18 04:27:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c6554739-c634-3b1b-963f-a7880bffffdc | -12.082 | -48.19652 | 2026-01-18 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 733f1201-f882-335a-afd6-989f3363ceaa | -11.78495 | -45.3568 | 2026-01-18 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 614f546e-5a45-3da7-8039-68a4b22008be | -12.40607 | -46.89109 | 2026-01-18 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53a1ae52-aec2-3a86-bdd9-6ba395d8541d | -8.92974 | -42.95639 | 2026-01-18 04:27:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3fc28e84-1008-38a0-8a06-a0d93a05b6b5 | -9.57578 | -44.59249 | 2026-01-18 04:27:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b0f4c808-4ef8-3dbe-aaf9-0614891d0277 | -9.57959 | -44.59544 | 2026-01-18 04:27:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0c88c54d-8231-3cad-86d8-32238ba69c17 | -8.07996 | -35.42218 | 2026-01-18 04:27:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 33d5ac65-29e2-375d-9711-c37aa8d5c4fb | -8.0806 | -35.41747 | 2026-01-18 04:27:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dc3aa6b7-08dc-3157-9d44-18d56c040189 | -9.57609 | -44.59489 | 2026-01-18 04:27:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5418f39c-276a-3ab7-bab1-c509b61d8cb5 | -5.25206 | -44.74805 | 2026-01-18 04:27:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed8356c3-232a-3c41-8cdb-70bb45313367 | -6.98623 | -42.86967 | 2026-01-18 04:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ba22ca57-5f2e-3aa5-bffb-174d63c91020 | -12.07167 | -45.30285 | 2026-01-18 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 549cf496-3804-392d-84bd-b514604abe6c | -11.69226 | -48.846 | 2026-01-18 04:27:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d0bd011-3d7e-39d9-99ab-076350e0a9bf | -9.57929 | -44.59304 | 2026-01-18 04:27:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0ca2ef98-98f7-3c6d-a460-6304413a8a41 | -9.5831 | -44.59597 | 2026-01-18 04:27:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 931794c1-cf6a-3bf2-95a4-f42d9d1f34c9 | -11.53007 | -47.69468 | 2026-01-18 04:27:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db8a140c-f959-32ff-adb9-abfc07ac4989 | -13.54822 | -45.59099 | 2026-01-18 04:29:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4f3ca86-14b1-3e83-8b08-ec4845068d7e | -14.7443 | -45.90674 | 2026-01-18 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da6b2097-ddac-3474-8b64-5ce3865b2e6d | -14.77793 | -45.94439 | 2026-01-18 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d93882db-ae85-3bb9-8e5f-78ee41f1ec30 | -13.68883 | -52.58819 | 2026-01-18 04:29:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0575ff0c-8a56-39b1-94d6-a027ea0cec4f | -13.94055 | -48.51432 | 2026-01-18 04:29:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d655f6ea-41ed-347d-972a-277f726399a5 | -13.99103 | -45.80009 | 2026-01-18 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5043e76-f359-3bc6-9a0f-f1e4c6322f59 | -14.74779 | -45.90728 | 2026-01-18 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5199193a-c776-3a89-a13a-2682ef265120 | -12.35242 | -51.21903 | 2026-01-18 04:29:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30baaeee-b34d-370f-b312-edf636a0ef07 | -15.56257 | -59.65958 | 2026-01-18 04:29:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 013b8b0a-2b01-3de0-ad59-6337bfe13cf3 | -13.94387 | -48.51487 | 2026-01-18 04:29:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00eef5af-910f-3b36-9c7b-543360d9c457 | -13.99161 | -45.79613 | 2026-01-18 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2331de60-7b7c-3d5d-821e-4cafa1721247 | -15.9477 | -47.68194 | 2026-01-18 04:29:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa1a5fe3-b65c-3aa4-bc3c-616b6b79a5de | -16.91044 | -51.28513 | 2026-01-18 04:29:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6707df53-6124-38cb-a145-501f874f29d6 | -13.03883 | -46.79617 | 2026-01-18 04:29:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb7e6fae-1404-3f54-89e3-559cfc595c9b | -14.78489 | -45.94547 | 2026-01-18 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1402eec9-0ffa-3a4e-a2c0-dff2ead3e406 | -14.78141 | -45.94493 | 2026-01-18 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64b8187c-d4a7-3579-a31b-00bff75632cf | -12.65913 | -46.76892 | 2026-01-18 04:29:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8183bac6-0ccc-3cb5-a138-f5462d43b559 | -18.88083 | -40.24143 | 2026-01-18 04:29:00 | NOAA-20 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bbfe4033-f282-3b33-8349-8a6eff097b90 | -12.66248 | -46.76946 | 2026-01-18 04:29:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90c11a59-b5f3-3705-b7fa-2c23a87ab6fa | -13.74512 | -43.65854 | 2026-01-18 04:29:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72f072a2-9154-3ab9-b10e-eb10e54e7005 | -13.74444 | -43.66349 | 2026-01-18 04:29:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 73f3e77e-d654-3301-8a97-5c119cfa295a | -16.58576 | -57.80889 | 2026-01-18 04:29:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| bd3c6313-f0bc-3c2a-a674-426e5cde1605 | -12.34878 | -51.21838 | 2026-01-18 04:29:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0416aa83-d18f-366f-baab-99cd6e3aa66d | -14.79109 | -51.94468 | 2026-01-18 04:29:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85a11638-f3b9-3a5d-a7c5-e50a2d1fc3b7 | -12.65299 | -46.76425 | 2026-01-18 04:29:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00c14dae-32b3-35e7-ab71-7d5251ec5c87 | -14.74372 | -45.91072 | 2026-01-18 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6097c51-a630-38f7-9550-a48eee578eee | -13.69707 | -55.68568 | 2026-01-18 04:29:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0fcb7d74-1cc3-364d-b992-2413a885c0c0 | -13.42928 | -47.33982 | 2026-01-18 04:29:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82120d14-2086-3c71-97bd-1aef494b2337 | -12.70934 | -46.79908 | 2026-01-18 04:29:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7a1a8a49-05ad-31c2-b7e5-e15539e535cf | -13.42596 | -47.33926 | 2026-01-18 04:29:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78fa209b-a56c-390e-9d87-43cbf1eb4d0b | -18.52913 | -39.80343 | 2026-01-18 04:29:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fb87408d-fe59-33f5-aeb2-16b69c80cf27 | -14.76635 | -45.9264 | 2026-01-18 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da9c6ca4-75c8-3140-ac1d-2121e8f773b7 | -12.70655 | -46.79495 | 2026-01-18 04:29:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a9dce64-57e9-3984-9de2-61eb399aee57 | -16.66687 | -52.40623 | 2026-01-18 04:29:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d5cb203-162c-32d4-9d6b-b0589bf88932 | -13.69884 | -55.68318 | 2026-01-18 04:29:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1506e013-ef89-34b6-96da-c4ed390f8263 | -13.42707 | -47.33212 | 2026-01-18 04:29:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 487efe58-7d4f-3791-a854-c0d008b15b7f | -13.54942 | -45.59016 | 2026-01-18 04:29:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bc0c607-113e-3928-83f9-fb69eff617db | -13.42375 | -47.33155 | 2026-01-18 04:29:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0896b606-31bb-3269-9d6a-bce0f66f532b | -14.76345 | -45.92189 | 2026-01-18 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 029f4331-569d-34c4-9b8b-b1e2e89fb411 | -13.36712 | -44.26176 | 2026-01-18 04:29:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ab2e0e9-2819-3850-a33a-792da9340b5b | -14.74489 | -45.90276 | 2026-01-18 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 98e51525-b03d-3627-8f06-299526e3555b | -18.88049 | -40.24467 | 2026-01-18 04:29:00 | NOAA-20 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 35bd10c8-69da-3a66-8ec2-07a58333d675 | -12.34952 | -51.21404 | 2026-01-18 04:29:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0174f17a-fc0f-3fcb-afe2-f2bf9435425d | -14.77503 | -45.9399 | 2026-01-18 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bea14393-f87c-322f-a494-cda7e91b51a5 | -14.74082 | -45.90621 | 2026-01-18 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2be982ca-ad9e-3eac-b7ce-972a6f148e97 | -12.66303 | -46.76586 | 2026-01-18 04:29:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee9c1ce6-88ae-350e-add4-d21c43d99246 | -12.65244 | -46.76785 | 2026-01-18 04:29:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f452e9a9-e263-3d19-a311-3b4bdb539a2c | -13.04111 | -46.79591 | 2026-01-18 04:29:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd18604c-00fd-33f9-9976-4bcfc7ed75bd | -21.1252 | -40.8965 | 2026-01-18 04:31:00 | NOAA-20 | MARATAÍZES | ESPÍRITO SANTO | Brasil | 3203320 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b5005889-32cb-3a3d-a102-610be0228cc7 | -21.09277 | -50.64744 | 2026-01-18 04:31:00 | NOAA-20 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b10c5976-659e-3003-92c5-0ed378c55dd6 | -22.44563 | -42.08331 | 2026-01-18 04:31:00 | NOAA-20 | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fe9bf1e9-ca03-3e38-b923-e293be1228b1 | -18.81268 | -51.6047 | 2026-01-18 04:31:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 25c226c6-ebb8-3acb-aee9-a8bb0963d8fb | -19.21253 | -53.43679 | 2026-01-18 04:31:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dda2267-bae6-3f31-9953-fb1a16e17039 | -20.84156 | -51.74034 | 2026-01-18 04:31:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| aa19c99b-3c58-387d-9f63-afbb35778fde | -21.60409 | -50.89029 | 2026-01-18 04:31:00 | NOAA-20 | SALMOURÃO | SÃO PAULO | Brasil | 3545100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 67d89b7b-6144-341b-8ea1-04d189ff55eb | -19.47287 | -55.46495 | 2026-01-18 04:31:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 829bf08f-aae6-3b25-95e2-50d8b4770bf7 | -21.19992 | -56.9319 | 2026-01-18 04:31:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7fd09dc-3feb-37dd-86b7-c4d0839d59db | -21.12776 | -40.89576 | 2026-01-18 04:31:00 | NOAA-20 | MARATAÍZES | ESPÍRITO SANTO | Brasil | 3203320 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c5b2d6e5-dfaa-33c6-b333-d13bdfb148d8 | -19.21168 | -53.44161 | 2026-01-18 04:31:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae740718-fa49-316b-9534-23c3ce43117e | -18.81614 | -51.60533 | 2026-01-18 04:31:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f220f9a9-7aa6-3ed3-bab9-5535fb524c7d | -21.08944 | -50.64682 | 2026-01-18 04:31:00 | NOAA-20 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f1f3a22a-f241-33fe-a014-2b1cd2a03c78 | -26.8718 | -48.68985 | 2026-01-18 04:33:00 | NOAA-20 | ITAJAÍ | SANTA CATARINA | Brasil | 4208203 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 23d5b345-ae7e-3948-aa02-3902c0c42589 | -2.35802 | -51.89254 | 2026-01-18 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81b38a68-e359-3cc7-823f-8f9779b6f64d | -2.15908 | -53.65253 | 2026-01-18 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 35ef0eac-5899-32a4-8403-67839c67a452 | 3.48083 | -60.29302 | 2026-01-18 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a0ce625-6372-3061-a3f4-e51f45fe139f | -2.35427 | -51.8876 | 2026-01-18 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c66bce51-6371-3fa1-80df-3d657efb9f03 | 2.5492 | -60.5707 | 2026-01-18 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78235c09-6759-3be3-936c-a622f62ccf83 | 3.48018 | -60.28876 | 2026-01-18 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec8daf5e-e618-359f-b857-bac6d06b4682 | -2.16296 | -53.65316 | 2026-01-18 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d58c0f42-c7a2-326e-a2cd-abffa2583d84 | -2.1599 | -53.65423 | 2026-01-18 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 676f0936-0285-39ba-aad2-53e12f6bf4e3 | 2.5522 | -60.56584 | 2026-01-18 05:16:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b757f7a2-1ede-3954-bccb-0aa52fc47d69 | -2.16063 | -53.64932 | 2026-01-18 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4782a918-a7c7-3b5b-a631-1f05bf53a6db | -16.5909 | -57.80653 | 2026-01-18 05:20:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 87cecae8-6598-37a8-b85a-17a768427ead | -10.5443 | -56.33738 | 2026-01-18 05:20:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 402fde44-7df4-3c89-98e8-5a7d02240c6b | -15.25827 | -56.72365 | 2026-01-18 05:20:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f795967a-d0cd-3d04-a7fa-7bda3229741f | -16.58721 | -57.80601 | 2026-01-18 05:20:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9b2e23eb-c21e-38a2-b571-ace054a7afa3 | -21.19938 | -56.93091 | 2026-01-18 05:22:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5946e9d2-7165-3f21-8d0b-b8178ce406dc | -19.47251 | -55.46445 | 2026-01-18 05:22:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 08588444-2cf0-3bfa-9d3f-cb1fc39e1bbf | -20.84665 | -51.74028 | 2026-01-18 05:22:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README4.md)
