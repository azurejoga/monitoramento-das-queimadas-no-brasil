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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f33fa81-edec-38da-b731-b2ddd4376041 | -12.7815 | -47.29531 | 2026-10-01 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b00bf45e-785b-351a-90c0-da02a22bfafb | -10.84906 | -48.69979 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db5ad688-50d8-383e-ab6e-4bf491c630d9 | -8.35101 | -45.49545 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae41cc90-62ee-36b6-8d8e-c06a1da111e6 | -9.54458 | -56.16512 | 2026-10-01 04:34:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 819f610b-e4e1-3dbf-b9cf-f66ce4f052cb | -9.53995 | -56.16095 | 2026-10-01 04:34:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8508dd6-837d-3c74-b304-ffefc42d203d | -9.20185 | -45.82203 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c3d0ec4-e38d-3dbf-80af-f95bc46eb50c | -9.79593 | -44.81264 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f6643ba-a6bc-3a7a-ab04-473d199cf44d | -13.51987 | -46.88713 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd20a2eb-eef7-3b8c-af1c-8d76dc28f1a7 | -8.6352 | -45.29281 | 2026-10-01 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f23cfed7-a457-32e9-a010-dadbd4733e8c | -8.15875 | -54.83574 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2d4e67f-e6aa-36c2-9a5a-e08764c281d0 | -8.22496 | -54.74616 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5039254f-3c08-3569-86ce-f1ee050c89dc | -7.019 | -47.54086 | 2026-10-01 04:34:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 017a20e8-7c22-3451-ae24-0c99cb1c2596 | -7.53725 | -47.12561 | 2026-10-01 04:34:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 653f238f-087c-3a6a-a7d5-8a1090fca69f | -11.45299 | -43.44435 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1d5595f4-cbfd-3b83-81f1-c53b456d4d95 | -11.43352 | -43.4172 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a78802bc-d4e3-32c6-956a-0f7839085d63 | -11.26425 | -43.51954 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b24ef4a3-f3e0-3677-b367-78c5509af7ef | -9.16293 | -45.59431 | 2026-10-01 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8318094-0eb3-3be8-a496-4f9091597cc4 | -10.85692 | -48.69382 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aecb1937-9db6-30d9-8aa2-9362a9bf79b6 | -12.35426 | -46.37748 | 2026-10-01 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af4cc243-1428-39ec-b985-c5907d3049f1 | -6.68569 | -58.86988 | 2026-10-01 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 40eb3268-dcb1-35db-8fe2-06feec04c85e | -9.39373 | -56.97279 | 2026-10-01 04:34:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f8fbe24-6564-3018-99f1-4445387b255d | -11.51699 | -47.17594 | 2026-10-01 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 936b15c5-ede7-3cb9-94d6-1e566eda4109 | -8.24765 | -45.43893 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| edb7dc67-8da5-3aaf-a94e-a2e47cbb0c00 | -10.2509 | -49.67223 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ee87f05-53b5-3b1b-ad53-5a66ccec331c | -9.27159 | -46.44689 | 2026-10-01 04:34:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0312bd7-2881-3ead-9bb6-5b0dfd413754 | -13.38138 | -46.83527 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9af8e011-489d-3d95-9e92-2ba0dd47789d | -11.71363 | -43.43402 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 397995a4-7c1c-333e-be26-4c11224ce966 | -12.90445 | -44.82144 | 2026-10-01 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cce13c7b-7dbe-3600-9ad3-548f12e1459a | -11.44184 | -43.41356 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b5f9561b-c9a2-3c84-ae60-34d22df6c375 | -6.26916 | -51.82125 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e41fcb14-68bb-3e73-9385-4ad7226ca41d | -10.8412 | -48.70576 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7272e9bd-23e3-3404-a477-2b90f01b6b77 | -6.43621 | -55.80866 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d60ea4e0-dbdc-3b18-926e-b9e9a2a90c26 | -6.34695 | -55.32724 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ff9c085-938e-3a9b-bc67-4809ead5963a | -13.38474 | -46.83575 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 942f63ff-99d1-38bd-92cf-d2c41a76e906 | -10.2533 | -44.57918 | 2026-10-01 04:34:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b5e62c3e-3b1a-31a3-9475-31515d42aeab | -8.26449 | -54.73866 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ceb1e647-9036-3594-b5ae-cf95f8c23d45 | -11.40878 | -43.48146 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5dd2ee1d-4991-33b6-b0c7-032524938116 | -11.3877 | -43.36386 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 14e63c40-d4c9-34b2-a8c8-653e55552569 | -13.0976 | -47.44472 | 2026-10-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e511c1f-6e2c-37ae-93e6-bed0ba437cdf | -8.38026 | -50.72825 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab3f3aac-7cac-38e5-9b34-3ea20f8caf4c | -7.17278 | -52.62944 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06f1e2cd-9f27-382e-b286-43b09c04ae87 | -14.14786 | -42.09159 | 2026-10-01 04:34:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 070551d3-a348-3f8e-ae51-53c47ab55129 | -7.851 | -45.82701 | 2026-10-01 04:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9668fde8-c549-39da-a928-2fe02544a7bd | -12.70452 | -46.95811 | 2026-10-01 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97c0e49b-1307-36e6-b705-f9ae441c72ee | -6.69846 | -55.05307 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ec9fdf7-f245-3bdd-a5d1-2ce444797555 | -12.85608 | -44.33966 | 2026-10-01 04:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2df9621b-9bca-3cfd-8f3a-33540f30ade9 | -6.75476 | -55.09136 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fe18bc8-b630-3bfe-acad-77a2e480b9d2 | -8.75971 | -47.19407 | 2026-10-01 04:34:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d8ae591-bafa-3261-afed-e67661fe6b3f | -7.7316 | -54.80353 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e126f364-d473-32ee-8d5a-564ef6a45f33 | -9.775 | -44.80941 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 844eb492-2ec1-3da9-ab84-f01f63a212b8 | -9.65174 | -45.12151 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eeb004bb-29e1-3684-96dc-4000324919b8 | -9.37283 | -50.66296 | 2026-10-01 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d12daf4e-5a59-37d8-bb0b-e87217df586f | -8.05688 | -55.34354 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eff1ac57-f20f-33ab-9a03-414b60337cdf | -10.93706 | -47.98499 | 2026-10-01 04:34:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5eb24f7b-5952-348c-bfed-fdf0fabb64ed | -9.10511 | -49.60375 | 2026-10-01 04:34:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3752c839-f432-325f-8173-06e723118066 | -7.55141 | -55.03355 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb0186e2-5b55-3439-967a-6e651c489a3e | -13.32465 | -43.4765 | 2026-10-01 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76f2e7e3-2ac6-384f-8307-20143e9859b0 | -12.17712 | -47.38361 | 2026-10-01 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4fc0e4ff-1f5f-3da2-9cd2-a6e8e2aa033b | -10.84805 | -48.68479 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fafec9d7-30ae-3915-b404-281c00ea0fab | -8.01188 | -47.45229 | 2026-10-01 04:34:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27d612f6-087c-3639-b351-38e200b591a9 | -6.69899 | -55.05007 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8e633b6-402d-3307-83d0-34b5f0132bdc | -12.31397 | -50.28614 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d22e373-1dc9-3c86-a875-8fa97f2f1ad0 | -11.38591 | -43.40265 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 989cfaaf-8455-338c-9d67-093282ca9b1d | -12.19368 | -48.43405 | 2026-10-01 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60d45c23-5224-30b8-85e1-870311f2e44b | -13.3205 | -43.82312 | 2026-10-01 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14596861-f58a-318e-bb0c-ec3b3899b130 | -11.14592 | -49.05046 | 2026-10-01 04:34:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c208bc3-1d94-3e66-88ad-421a8144469f | -13.53711 | -49.18698 | 2026-10-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2c6d3d4-ebea-342c-a3fe-caf6c109ab54 | -9.80232 | -44.81762 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91b74554-00c1-3c24-a91d-f2dc75b6f1bb | -12.39163 | -54.10569 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b00e0454-7cfb-3f2c-977b-184d7f0d4f0a | -11.79403 | -50.5094 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28783ea2-9854-31cf-94e8-5a31745a31b4 | -12.18983 | -47.38927 | 2026-10-01 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63b91df9-9e93-304a-9e84-e3b56d4e699e | -8.79649 | -48.0055 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 173b8a19-9ae3-380b-ae45-f533d9348fe8 | -13.54438 | -49.18449 | 2026-10-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 266c7061-e5f1-3916-9b84-b30be4913e35 | -8.63464 | -45.29647 | 2026-10-01 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68c92202-b097-3646-ba35-b6abce1cd353 | -11.45924 | -43.45495 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a606585c-a014-3390-8650-e479412abff6 | -6.34527 | -55.33672 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e197c3c-76e4-310c-9bc2-55befc404f1c | -10.72564 | -50.53865 | 2026-10-01 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b0b713a-7792-36eb-b0e4-787b72db58c0 | -9.06631 | -44.99223 | 2026-10-01 04:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 035b5af5-4485-3dfe-aa91-6aea07fea1d6 | -12.63284 | -42.14795 | 2026-10-01 04:34:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4cd7a1d9-3f5c-3717-ad02-19eed9d29c3f | -7.82376 | -45.8263 | 2026-10-01 04:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 92fff066-d075-37b3-9c9d-514e82770d50 | -7.49222 | -45.79622 | 2026-10-01 04:34:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfb0710a-bb47-32bd-93e9-8f1b79ffadaf | -14.27013 | -44.50674 | 2026-10-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba4ef537-e031-3026-98da-44c58907ff33 | -6.05874 | -53.28329 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00774f66-461f-3022-9e5f-4e235568c03a | -11.7383 | -50.4081 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23ef013a-83d1-3646-a5ea-b83b4702133e | -12.44879 | -44.19112 | 2026-10-01 04:34:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82be04fd-5a35-3df9-a439-b93b0f82f33d | -6.34174 | -55.32625 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1a70104-210d-34cb-86db-bcbf5c3dec91 | -10.84631 | -48.69553 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32795f41-8d0c-30df-bdf7-c2744c86f731 | -11.45123 | -43.42955 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2b087e44-4ad4-3b91-963d-792f51095bd4 | -8.49662 | -50.78101 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a714b5df-0065-3fa2-8161-f15a09178834 | -13.37727 | -43.99387 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1e9f891-144e-338f-87d6-06e13a723441 | -11.73057 | -50.4109 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f0cc0c4-26f2-37a1-bbc2-069ed20e913d | -9.96223 | -59.2611 | 2026-10-01 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3bef590a-b5af-3476-ac83-955da66f8f71 | -10.24177 | -59.0287 | 2026-10-01 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0846770f-be6a-3e46-b326-312495ef7212 | -10.84297 | -48.69489 | 2026-10-01 04:34:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9d3f6a1-3982-3042-86ef-50b6195a64f2 | -11.17556 | -54.11716 | 2026-10-01 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3f5d05b-2b6b-39f3-9ab0-50ea17a846dc | -12.41376 | -40.92146 | 2026-10-01 04:34:00 | NOAA-20 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 907ed7bc-cad8-3ab5-8726-301e3c013092 | -11.4068 | -43.41325 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acecef67-2d27-3af2-8f8a-33a745aa81eb | -8.32944 | -46.75843 | 2026-10-01 04:34:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a906503-2a93-357c-aba6-956da7be6802 | -13.73732 | -48.97617 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c7fa76c-23c4-329b-9aa2-9be1f98edcf2 | -13.32572 | -43.473 | 2026-10-01 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README59.md)
