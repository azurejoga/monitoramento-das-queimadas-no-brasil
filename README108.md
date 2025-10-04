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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 231f73e3-97be-337a-92bf-d9899c862eaf | -12.87457 | -44.62402 | 2025-10-04 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4897c829-dd2f-39b1-b074-098109ac5337 | -14.64387 | -48.30059 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| eaf9420f-d9e5-3243-9256-569768c02707 | -10.99867 | -46.68882 | 2025-10-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5028bb7b-6da8-3e97-9d0a-05ed25b20279 | -12.81664 | -46.86683 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 83e83f36-bb7b-3e1c-8f7f-6528e4d34d91 | -13.30861 | -48.13625 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38e921ce-c6e3-3f37-81a8-4849eeac5695 | -10.64194 | -49.13734 | 2025-10-04 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f2be76e8-2c9b-3cdf-9442-3b36426d6c99 | -14.94092 | -46.85759 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 27.4 |
| affeff40-1186-3e57-8a5d-4f4d679c00a6 | -13.73819 | -47.93322 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b047c7b3-890f-36f2-ac1b-2fa3be5c0505 | -15.74739 | -46.26465 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b50f237-35d6-3250-9b7c-d47d696f108b | -13.12225 | -47.93557 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eec69e5e-5916-3a9a-8370-4478c53a3011 | -11.92061 | -46.39747 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 7d0f7060-f239-3fe6-90dc-7089f04cbc9f | -10.33788 | -50.32608 | 2025-10-04 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 898346ea-26d0-31f1-b2eb-4a522d86d3b9 | -13.14083 | -47.80619 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 73b07e16-70ba-31ca-bb80-b38d8ccc1a2c | -9.88521 | -58.03897 | 2025-10-04 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40d9860b-5c39-30e9-9405-7afe8d09f19c | -14.38295 | -48.47746 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08ae73cc-1663-3b7e-afd7-1a93e4f0634e | -12.29832 | -55.13131 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60e58021-e21b-32d3-8296-a01b29e767a0 | -13.32128 | -47.61684 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 498bfbff-1196-34f6-93bf-5c5395f121ea | -12.89272 | -47.16762 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d49a1b2c-18c7-3fbb-9cb6-1c40cebb5aab | -12.71131 | -48.5553 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 534967c4-b43f-3026-bed1-1b45bbaddb6c | -13.88446 | -46.51098 | 2025-10-04 05:06:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| dc491f29-8e95-34b4-8e68-2ab61e816ca1 | -13.32422 | -48.09742 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ef6e52eb-4062-30e7-ac15-a2d79005900d | -15.72698 | -46.28783 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f39f17aa-9026-3cf3-8fe7-ab54b16b8a9f | -11.13061 | -47.8542 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa88fe78-8b8d-301b-8389-eeaf2c536916 | -11.87787 | -44.98206 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c9f381da-21d4-3e5c-9324-f3b83452f162 | -13.29716 | -47.82244 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ec76f73-47b6-375f-ae93-60835efb2406 | -11.91234 | -46.37345 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb6acbcc-e217-3228-b2c6-dd2b1ceaca2f | -16.02682 | -50.94071 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0203520b-3265-3ab9-868c-70696a666525 | -14.65613 | -48.24199 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4fb0cbe0-6e66-3c5f-834b-cb652004fdb7 | -13.11645 | -47.93847 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d1387a7a-d0bb-3c5b-9899-030b2967e5ef | -14.89783 | -48.27961 | 2025-10-04 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da61723a-d435-350a-9ca7-a545913889c6 | -13.13039 | -47.8163 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 804a1587-585b-37d9-8fa4-7ae791b1ea15 | -13.29538 | -47.59874 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 31.3 |
| cd9caa1b-b66e-3712-86cb-af2a84db4fd6 | -13.33139 | -47.57853 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9cc0f14c-f961-3c28-85af-e34d3bf62c44 | -14.86719 | -48.3548 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb6319ee-e533-3bee-8370-f3b4425b332c | -11.92628 | -46.35686 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f8c4693a-9356-3143-a5aa-d0c41c38a2cf | -13.99874 | -48.20403 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a6c12641-adf7-31e7-933b-0b066c26ffa5 | -13.12951 | -47.8085 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 76f7e936-fc1e-3ee5-aa72-ed641c8fe1be | -10.58795 | -48.72292 | 2025-10-04 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6c4d8709-503e-3ff9-8393-04e1bf94eb70 | -11.08925 | -47.88473 | 2025-10-04 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7fecca7c-52b6-37d7-af75-39907eb334bb | -11.2793 | -54.86747 | 2025-10-04 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e7f9d0b-d551-3827-bf8c-36f876f94a6f | -10.32789 | -50.33348 | 2025-10-04 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 39b0e29d-680e-3408-9194-20c95a06a64d | -14.66069 | -48.2497 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 477e727e-b938-3cce-806d-faeb98421e97 | -14.23565 | -46.09202 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5479354c-57c3-3c34-8fe6-0f76015d9a0e | -9.97701 | -62.19072 | 2025-10-04 05:06:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 554fc9e2-2db8-3c20-a89e-2f430ae2b192 | -14.74887 | -54.63936 | 2025-10-04 05:06:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af723f07-4c18-33ac-a134-7acae274d9d4 | -15.72081 | -46.28705 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c970274-bbb0-31ac-8394-d5b4c21bf802 | -14.2839 | -45.87711 | 2025-10-04 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c850c84e-c5b3-3b7d-b96d-1fd45d4cc0b5 | -15.74152 | -46.26869 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db5a4a97-f6f2-3195-9c18-eb78dc7a283a | -12.83336 | -43.80793 | 2025-10-04 05:06:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6bde460b-11f5-3abb-92a0-2312507f05ef | -12.47382 | -54.42439 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a41a01dd-8c3c-305f-8fd8-f7357d2596ff | -15.23069 | -56.84795 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69ef800c-9443-3aef-bce2-13e08029fef0 | -12.07515 | -47.99427 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a6d522a-7c49-33f3-9686-04c824f91c83 | -10.22463 | -59.15393 | 2025-10-04 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8612264-33dc-3e7a-b648-648f2c08f9c5 | -13.17659 | -50.88404 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7351620e-1f63-31af-9e27-2823310662fe | -13.73903 | -47.92616 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8b30200-e670-31d9-9c18-e67a085387f9 | -13.13341 | -47.93369 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dac4c450-4c5c-3a7d-95d0-0dd5d261bd94 | -12.30461 | -55.13619 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 060e8348-8112-3a4a-923a-a95d1d9d4666 | -10.12428 | -52.34793 | 2025-10-04 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 018d44ab-7239-38dd-b70a-37a3d34d3a60 | -13.1114 | -47.91241 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ece61380-b424-30c9-bb66-d72486e5029a | -11.99181 | -61.02608 | 2025-10-04 05:06:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ecc60c9-b98a-342c-bef8-b03ef1fc26c4 | -13.31433 | -48.13377 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5db1a40e-49be-3db7-a172-1728f69930c4 | -11.11454 | -47.89775 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 940ef3ab-4e22-3c1d-a105-5abd1b47c00c | -14.66352 | -48.3187 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6ff47c4f-bd4f-33a5-a63c-00ed3acf5c48 | -11.5046 | -45.01913 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d759f61c-48a6-3255-8cea-6f52c1c692eb | -14.66387 | -48.31569 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| af6b0b64-ea52-39f8-b075-94bcb993dd64 | -14.20641 | -46.07704 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a1e403b4-1e5a-30e2-bf50-097f9e170f95 | -11.13737 | -58.4038 | 2025-10-04 05:06:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fa878b6-8131-34c4-b7fd-1d51f5321ddc | -11.2439 | -47.80146 | 2025-10-04 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e5d24fb1-a8f3-3341-9209-297458665a6e | -13.21282 | -47.8189 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1e9dbc8-ac23-38b1-bd51-9d9a7473f5e6 | -11.11061 | -47.75401 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a36ac09-508f-3bf3-a150-4049c0de3249 | -13.17571 | -50.92422 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 26cdb88c-3819-3f5d-9ba0-088235442395 | -15.22565 | -56.81373 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b6ca5c8-4452-3fd9-b543-2301d1e75149 | -12.08125 | -47.98828 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62681dce-b39c-3085-a5bd-aade7bc7d86b | -13.74681 | -48.06672 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ade6ae0c-b22d-3891-8286-91a07edbf6aa | -9.19377 | -59.54925 | 2025-10-04 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbd11d30-65af-3821-a5c6-1f4168283280 | -12.70148 | -48.55035 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5c5fa771-6252-3ab0-9a31-4df56bf8dd44 | -14.6823 | -48.27836 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a9a1754-23c3-3946-8ebf-218792cb9899 | -14.89068 | -48.29394 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f9722766-d9b6-3590-9f81-415166285841 | -9.71358 | -67.466 | 2025-10-04 05:06:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4bbc6794-2f8d-3480-8560-fc5a9bd45c66 | -15.21181 | -56.83747 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e267e24a-86a9-32b6-9eb4-88bb5b759c58 | -15.23402 | -56.8485 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75629575-8b7b-3fe6-9798-3e456f1c14a7 | -13.77919 | -47.82154 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f27b23d-0026-3e46-bee7-4549ed0709c7 | -11.11533 | -47.89134 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2ac4f64e-a1fb-3402-93f2-31a94a0078a3 | -14.87166 | -48.36315 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 301396f0-a91d-33e3-bc74-9c51daa7ef95 | -11.68626 | -47.49457 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3d61ee55-9f26-343c-9f71-6ca4cec6729b | -13.32658 | -48.12225 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4e989ae5-4013-3a3c-92ec-49226917d96d | -13.98373 | -48.19296 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c74b1f8b-3c64-3975-bee7-997daf22055a | -11.54703 | -47.67612 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 61c2d923-c812-34e9-8a76-fbd2c4d87148 | -15.30254 | -46.30186 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 199e5040-0025-326a-895a-839060096279 | -15.34643 | -46.29918 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 84854ea2-41f7-3bc3-b0d7-b56242e88f7c | -15.32693 | -46.30649 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90504648-0c4a-3eb5-ad5c-df7a3627c717 | -14.69741 | -48.09171 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7eb2f437-066f-3c56-aeec-0be4691fe323 | -14.2361 | -46.08785 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d513b565-e929-3268-8b03-416b9067e975 | -14.88524 | -48.29377 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 09ec6209-83e1-340c-8ba9-883f21ff24be | -13.29817 | -47.57437 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8aa8d413-2521-3f17-8c14-05228e7d7c06 | -15.03576 | -46.97491 | 2025-10-04 05:06:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| efadc651-18f1-3f5e-aa1e-15cf28f49c9a | -13.18988 | -50.88326 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7fdb6d42-2882-3081-8547-ce84a7a31a5b | -14.89553 | -48.39097 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8f8735c-1eb1-34ce-9451-4dd0c6568e6e | -10.82966 | -57.19741 | 2025-10-04 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b603e13-7274-3603-a2fe-61ce8d35e8d5 | -14.75425 | -54.62709 | 2025-10-04 05:06:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README109.md)
