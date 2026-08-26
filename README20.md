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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ef13fbb-34a3-328a-aaa7-d91ff4ab996e | -8.08271 | -45.91072 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d158595e-14b7-3482-853d-806f44fd48f7 | -9.59251 | -45.99509 | 2026-08-26 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80407f37-255a-3308-892a-85b75768f69a | -6.83635 | -52.50484 | 2026-08-26 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b74d6f8a-5bbb-349b-b427-681292adfec1 | -7.76202 | -44.75425 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f29011f8-06e1-3867-b464-34778aa1f717 | -11.29069 | -47.07439 | 2026-08-26 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5915cbcf-b2d9-3960-8921-59856b67f278 | -13.36876 | -48.2191 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 366b9251-8f82-3434-97be-a1ba200246af | -12.66301 | -48.42024 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dae79192-9914-3a41-baef-671dcd77440a | -8.63561 | -54.7571 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37f109c0-c3ea-3c87-b1b6-a76642c668ce | -8.01076 | -51.80814 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 019f8a4d-5c87-3daa-9756-45fb8166849b | -8.02815 | -51.81594 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c1931fa-7250-365c-91b4-f8945bd7efe7 | -11.96753 | -47.75814 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3016787c-5851-3a09-8d9c-06b51f2d1d69 | -10.91186 | -44.73828 | 2026-08-26 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c70b1afb-2e98-3a15-ab78-2119a3e1c9bb | -7.29148 | -43.02592 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f728a05a-82ee-3251-ab0e-41108d936855 | -7.31638 | -42.985 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 64310730-5394-386f-85d2-6e888eae0088 | -12.6851 | -48.40987 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5c5759d5-8429-341d-b775-86e745e5be54 | -9.03517 | -50.79573 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 37e3c3e4-9fe7-310c-b15a-adac4b49e428 | -6.27009 | -53.38821 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f46ac889-dab4-34f6-af13-b5f25a699b67 | -12.76785 | -44.26154 | 2026-08-26 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9c7741a7-11dd-3fe8-a155-0c0b9a8c6293 | -6.25193 | -53.37147 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 17371d24-5e78-39e9-a214-6f8ada9b8c98 | -7.13599 | -42.80403 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7dfb549b-c244-3c0b-84d2-b781983dc2e3 | -12.02157 | -46.0078 | 2026-08-26 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 3a490138-327c-3626-b0f8-fb7d4114992b | -6.26802 | -53.3614 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bc8db8ec-11b7-329a-896b-e74e82f2f0e6 | -8.00995 | -51.80914 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4d24889-fc6e-33a1-910c-ed81b9599e8d | -9.66328 | -55.09136 | 2026-08-26 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e131b7db-565a-3706-b29d-611f39235045 | -8.31175 | -45.71755 | 2026-08-26 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6f67af8-2bf3-386f-a6a4-ec76ed5a81a9 | -7.08823 | -42.17593 | 2026-08-26 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6e8802aa-d008-38d5-a0fe-35efe943df1d | -9.03089 | -50.78757 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a52222cf-60b9-34c9-a144-7fb1fbb3c4f9 | -7.28782 | -43.02642 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a8fbf891-27fb-3573-8ac8-41b0b8ab5aa7 | -9.03025 | -50.79103 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3c8623e0-23e2-35f9-a479-febfa0bf3f31 | -6.25647 | -53.38371 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7ff8ae48-00cb-339e-a0ba-ccaa460abc64 | -12.0336 | -46.0306 | 2026-08-26 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c568b25f-507e-3893-bf31-35297e016f90 | -8.81612 | -49.61148 | 2026-08-26 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ce69952-99ab-399a-b23c-d31280de0270 | -8.07617 | -47.51287 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9199ab84-7403-3c66-b1c7-4214ce8d2ced | -7.09165 | -42.17649 | 2026-08-26 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3575cdfc-775d-3461-aa3f-a870b9918ff2 | -6.28048 | -53.37063 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e79914f-a121-3d69-b078-06e1d7f05706 | -12.76151 | -44.25629 | 2026-08-26 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d551b509-e3e8-3555-b4fc-05f442cf507e | -11.79939 | -47.24312 | 2026-08-26 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1e1d766-7eab-32f4-996e-88806ffee264 | -7.30451 | -42.96783 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ef71a441-2689-3126-b913-d0b4f0bfa66b | -7.13415 | -42.7717 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 88768334-58fa-3110-a8bf-ace806fe321c | -9.9677 | -53.94881 | 2026-08-26 04:08:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f137b635-88f6-3fdf-8cfb-e8bb9569b7a2 | -12.70183 | -48.39491 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 275224b7-a64f-3120-b9bb-ca42d15babd0 | -13.35277 | -48.23362 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ed1ab3f3-c8c7-30f9-80cc-6443e97936eb | -8.01516 | -51.81799 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 438841f3-76f1-36f2-98fd-365b155518a3 | -9.01533 | -50.77777 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ad41a6e-2a6e-329d-b5a4-1a489efc984a | -12.66394 | -48.41508 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| aad0beaf-d269-3f5e-aa8d-6c1376be787e | -12.97765 | -39.79549 | 2026-08-26 04:08:00 | NOAA-20 | MILAGRES | BAHIA | Brasil | 2921302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2950188f-bb0a-3eb1-a53a-29d50530b36e | -10.76068 | -54.03138 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 7152c9dc-951e-3832-856e-05a207c140a0 | -12.69304 | -48.41717 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6b34e1f6-21de-3832-972a-1eebaa17ee7d | -11.48975 | -45.11269 | 2026-08-26 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 55e6bb45-ee2f-3326-bb26-00d322ee848b | -12.73988 | -46.48225 | 2026-08-26 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e20c24c-ce3c-39aa-b086-df431cee3b48 | -10.46876 | -40.55468 | 2026-08-26 04:08:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8e9ee6b0-b3a2-3997-94b5-605767585be7 | -11.81825 | -47.65465 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8863709-68b6-3fac-b032-a6d6a224d656 | -7.25446 | -49.85722 | 2026-08-26 04:08:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f23e004e-4418-34f5-abcc-f190d8a4c39f | -7.12744 | -42.79056 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3dd78602-5566-3000-8759-26c92c87ed27 | -7.13527 | -43.18404 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b4f4b0de-3563-3acd-a767-f9b70a176c95 | -7.15219 | -42.81475 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 282c0b6e-1750-3c35-aab5-3302580e3657 | -13.34521 | -48.20017 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b75c2b6-254f-3389-a5ce-b7db7ca19855 | -13.33941 | -48.20711 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e5b4b986-d0db-38b7-8943-867d84f77684 | -7.13892 | -42.76453 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 091cefff-2a7c-33c3-84ff-9172c6ac71cf | -6.2508 | -53.37587 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4042cb60-f137-3864-8790-8258a6a12041 | -12.65762 | -48.42432 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ba97ae13-9a78-33de-9c5b-d2fa7fb4e534 | -7.39994 | -44.68753 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2bf0d589-969e-362f-92bb-3439ff60a6df | -12.75555 | -46.46292 | 2026-08-26 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ede5f77b-c4ff-3b0f-90bb-98546db7e1b8 | -7.14113 | -42.77288 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a0ab44c9-86d7-3981-b287-ff83aef19a1d | -12.28488 | -43.14209 | 2026-08-26 04:08:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 153713ef-3adf-3427-be62-01cea3000687 | -8.09146 | -51.68055 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f09aaa2b-0eff-325a-806c-adf82319483a | -7.14081 | -43.17243 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4954a942-bea5-3193-a23b-7f444e741f0f | -7.29145 | -44.08175 | 2026-08-26 04:08:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d1a3facc-611b-39b3-9aea-ec4ada89db05 | -12.73357 | -48.37377 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7edb572f-9e9e-39c8-9d61-015e5e4e22c6 | -12.72383 | -48.37629 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2413aa6c-9b80-3405-a474-e2d462bce3c9 | -8.02663 | -51.82102 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 55a3cdc5-d9bd-3e62-878b-121d24d268db | -12.7632 | -46.44261 | 2026-08-26 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09a71979-387f-38bc-acf5-93184c75dd97 | -8.75422 | -49.94968 | 2026-08-26 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ee55f2c-8419-3b44-8a69-7f7dc8f40452 | -7.28297 | -45.35751 | 2026-08-26 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 768a76b9-7755-3e0a-959d-64f4d6f0167a | -11.42034 | -44.54757 | 2026-08-26 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5b5e2045-fa86-3bc6-b748-a8fecd3df1f4 | -11.49283 | -45.09454 | 2026-08-26 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df203c0b-6585-3670-9c18-bf83c6e1a513 | -7.13948 | -42.80463 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 51c1366b-772e-348b-8616-77edba485398 | -14.03505 | -43.84864 | 2026-08-26 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 371e3be7-725a-3dea-85f8-4f29f5d82cd1 | -12.66428 | -48.4217 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| da58f14b-6de3-3dec-aca4-263cb6086482 | -7.13764 | -42.77229 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| abecaf41-26aa-3ad0-9821-e677f2fca51e | -7.25504 | -49.85403 | 2026-08-26 04:08:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67324d49-e8e4-3d86-9796-9d3d6667222d | -14.22672 | -42.11252 | 2026-08-26 04:08:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 226d8643-03ff-35fb-ac16-ca2f7f50b12a | -6.50026 | -53.26212 | 2026-08-26 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 243ed1f4-624e-350b-8078-5630b11626a0 | -11.49426 | -45.1087 | 2026-08-26 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db3ab70b-1910-31eb-b5f4-f80949a17b41 | -11.42829 | -44.52274 | 2026-08-26 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ed00242-909c-3d20-8d4a-e0261b656e2c | -8.1037 | -47.46385 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 04b90638-e495-398c-989e-82da8e7462d8 | -12.69655 | -48.39835 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80fe2a01-d210-39d1-89d5-bbb5cff1bf5d | -12.68863 | -48.41589 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 47cbf960-fc95-3011-98f0-a80c0610fb9d | -11.76246 | -54.53099 | 2026-08-26 04:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a3e26f56-0f4f-3315-8e55-e7c8d2a9e22b | -7.75593 | -44.74332 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f2e929c8-bfee-3b7a-8c54-a1aa026c318a | -9.0407 | -50.79723 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3f8a8a7-9780-3184-b8a6-c77da67355de | -6.28172 | -53.36402 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f78873d4-c436-3eae-9186-e08c0750f3c9 | -13.78263 | -46.89973 | 2026-08-26 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9882841-ac62-3b47-b1fc-fb21be2414a2 | -7.30017 | -49.54219 | 2026-08-26 04:08:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de77730a-78c4-343d-86d5-691f8d9067b7 | -11.77784 | -47.26893 | 2026-08-26 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b927a44d-329f-3654-895e-c20485ccaf43 | -12.02546 | -46.00851 | 2026-08-26 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b143be5b-55e1-31a1-9ef4-a5af29257556 | -7.73873 | -46.1464 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3b3e3fd-2dee-3438-b872-52cff9a35ff3 | -12.1723 | -50.61034 | 2026-08-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff43188a-27dc-31b5-8ee0-0180ad1dbbeb | -7.47565 | -46.08678 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb191ce8-ddb7-321e-bbf5-6d0325b12cc6 | -12.02882 | -46.0349 | 2026-08-26 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README21.md)
