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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a46a5ee5-77b3-3512-a249-778960dd0263 | -9.16371 | -68.24551 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d881f130-f00d-3f9d-888e-7b5b9b5f28bc | -6.07944 | -57.89111 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b851fd76-f62b-36f1-afd0-8f72fb6881ff | -6.31211 | -55.15156 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8cbb386-2817-3b23-ac2c-292259867e0d | -12.43831 | -49.59138 | 2026-09-12 05:29:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b58ffe62-ad9b-31a2-8348-91ec68bec1fb | -6.12021 | -55.64287 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71e69194-6349-362f-a66f-2b8416d40dde | -6.88873 | -55.64901 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab51f312-feeb-33b2-a490-2f8de2d751f2 | -6.22996 | -51.70607 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06e179f6-a3ef-39e5-9060-824ea753d48a | -9.18013 | -68.20535 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dae63c4a-c91a-3036-b119-c024ae54dfb3 | -6.06171 | -53.49091 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a600e21-4277-3186-8dbc-bc877ddfbb20 | -9.1629 | -68.25012 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0630b97f-e44a-3154-ab37-30e6d5032437 | -9.73769 | -64.95586 | 2026-09-12 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08465a29-943a-31c5-b1de-a8357dcafca0 | -9.63548 | -49.67888 | 2026-09-12 05:29:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89f4723a-4054-34a9-b305-340739c1f12e | -5.97851 | -57.77013 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fdc4726-a8f0-3dbe-bede-293dafb0ff4b | -6.12073 | -55.63943 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3e800e2-eb8d-3e22-828f-436c921bfb76 | -6.56587 | -58.98108 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f60ef7f-a3d2-38fd-a0bf-39e340eaf598 | -6.51363 | -58.29176 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de085827-1833-31e4-a4a9-9e0503879c05 | -6.60539 | -58.83933 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68a027cc-394e-36b2-a7dd-ca6a2044ef40 | -6.19556 | -57.72116 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 88af270e-2e16-370a-9cf1-c81f15d17e35 | -6.11564 | -55.64581 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b80a096-6c88-3512-a336-db48825ea640 | -6.29014 | -56.02452 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e5e8d5e8-996c-31b9-8b24-05605b4a4235 | -9.18019 | -59.69287 | 2026-09-12 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e7c0c86-bbc8-39ff-bf30-7eb886ea91ca | -6.12126 | -55.63592 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d09c9c2-6305-32ab-8eba-a4752121d6c6 | -9.31483 | -68.7791 | 2026-09-12 05:29:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0cfea79-1500-3c2f-b601-143a86bc804e | -9.16358 | -58.30904 | 2026-09-12 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c982af7f-dde2-3a26-bbc9-efeaa9bd5407 | -6.81903 | -58.99688 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce602328-cbdb-389b-9b00-8634cc70a787 | -6.61878 | -51.14535 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b7d236c-2398-3c15-9d5b-66f7a7c43cc8 | -6.39474 | -55.19931 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e881011-5964-3668-ba1f-e5e332c67ec7 | -6.60708 | -58.85102 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a59370c9-1fa7-3f21-b306-40ddc8b560d6 | -6.61393 | -58.85207 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 01e2cc8d-6215-3d04-8a54-5096f050dc19 | -10.48547 | -51.36258 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a8ba649e-d1b5-3aac-b3ba-f924ed780e4c | -10.51347 | -57.44686 | 2026-09-12 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e3525d22-a03d-3b7c-8e49-88de371c03aa | -10.90912 | -47.84172 | 2026-09-12 05:29:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25a17704-3d03-3124-abc8-5faa7fb91cc8 | -6.10888 | -59.90733 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e9f8d82-0f45-304c-b304-2170663bfeb8 | -9.44641 | -67.02936 | 2026-09-12 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca309bc8-8a05-3f30-977d-dca04a43ed5e | -6.0637 | -57.73165 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a59a279e-6ac5-316d-b588-9d081f2a3c88 | -6.23089 | -51.69954 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 126b007f-7f39-33bb-9794-cf45fd54a026 | -5.97726 | -57.77832 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b31dc1e8-0ec7-30bb-ba2b-dbfdb59b2ee2 | -9.19207 | -68.21696 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 763cb9e5-b5e4-30a4-8102-c236fc8df553 | -6.19136 | -57.72472 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 139540ab-cd59-35e4-9c43-1dc3246dab76 | -8.70267 | -70.68597 | 2026-09-12 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a37837d-0664-3d4a-910a-e37706ca33b7 | -6.85071 | -55.24713 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9563453-3ba3-363e-9212-ef57077aae13 | -12.13704 | -48.95702 | 2026-09-12 05:29:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 517a1043-87b5-3bd0-9142-3e38efdaa2dc | -6.80226 | -58.78856 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f51616bd-0ed3-3e0f-bd66-e81064a01398 | -9.50105 | -68.49567 | 2026-09-12 05:29:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ef20ba2-0078-3417-b6bf-742f536e644d | -8.5067 | -50.14946 | 2026-09-12 05:29:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d055fd33-6378-3fe6-90eb-74d879349b1a | -6.09892 | -55.64726 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2604886-2ed8-3c87-ab5f-0fdd87c85994 | -6.11386 | -59.89737 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6483f23-14f0-3aea-a316-2851436f2829 | -6.07505 | -53.49757 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9254dc7f-344a-3c92-9b10-0abc238994e2 | -6.11441 | -59.89387 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f221122-fc9e-353a-a878-a5fe8bebe0b0 | -8.53604 | -54.71964 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d4ccbe2-6d62-3b62-a794-84d3950aea90 | -12.13558 | -48.96969 | 2026-09-12 05:29:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c6155947-698a-3efe-97a1-bf0630f9c2eb | -9.30357 | -68.3056 | 2026-09-12 05:29:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 288d29ed-d507-33be-88d6-52294972a483 | -6.11209 | -55.64194 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eabaa04d-0343-31a5-bc82-c6da2fa13a2c | -6.18483 | -57.71952 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1be9b5df-4b41-344e-b6d0-b6405b6c5daf | -6.6105 | -58.85155 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ca2e8b36-cbad-37be-825f-db3049d9f670 | -9.49648 | -68.49478 | 2026-09-12 05:29:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5407bfd1-a0d9-3aa0-b8ce-b1b977f5a8a6 | -11.24916 | -54.13152 | 2026-09-12 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5707c07c-da5e-3ede-af64-fc663d6447aa | -8.8497 | -71.36923 | 2026-09-12 05:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0365340e-238a-322a-b2aa-ea2bc8e480b5 | -9.96061 | -67.82924 | 2026-09-12 05:29:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d6903fa-0cb7-3a36-a2d6-fce43d701b23 | -6.10752 | -55.64491 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d60a4930-6b33-33fb-ab61-7a769162e847 | -7.03237 | -55.39624 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1d38d23-7672-3d62-b52b-cd1bfc8b0dfd | -6.17766 | -57.71849 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce3fcb22-b36c-3cba-805c-059d9162019e | -9.46479 | -67.09611 | 2026-09-12 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0260cd72-8e44-34a7-a9d4-f29c15b6d2e0 | -6.13981 | -57.68885 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd6a2361-bd2d-340a-bad3-3b676786ce27 | -9.71312 | -54.34684 | 2026-09-12 05:29:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64f09b99-a593-3830-878c-d969ef37f83c | -6.20394 | -55.27222 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e6838d8-18c1-349e-a154-4c2ac9036393 | -8.95275 | -67.38985 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1f35bc1-edeb-3720-bdac-de98baf63959 | -6.12884 | -57.7124 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a66e069-92be-329a-82b0-d7324874e3c2 | -6.337 | -55.30228 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5546a4ad-46a5-3fe8-abee-1863b569d541 | -8.5372 | -54.7218 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f03ca7c3-213a-308e-869d-4cf6aad642e3 | -6.18716 | -57.72825 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc7b12e1-22d3-3134-a1f2-df89c8fe2433 | -10.89087 | -47.8369 | 2026-09-12 05:29:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb54e865-60c3-3920-84ac-b3dc340f9084 | -6.136 | -57.71345 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d4cfdea-db60-3ae3-ab55-9524982a17f2 | -6.20808 | -55.27281 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f551214e-48cf-3f5f-a417-9e923522157f | -6.28166 | -59.9304 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cfef5ce6-176b-3968-9e4f-4264dd9e4731 | -6.84774 | -55.81126 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68639685-0b46-3687-b648-3146bed764cc | -6.42987 | -56.1102 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bba6f484-20f5-3471-a604-6f9179627d0d | -8.11396 | -54.78978 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 206dd382-fc38-3147-8a14-44b1d2f971ee | -6.21223 | -55.27339 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78549041-79e7-3311-bfb2-c7edc86db076 | -6.17828 | -57.71437 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07da7e97-7997-37f8-a0ad-ffc6d4b038a1 | -8.06985 | -54.84735 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67516651-4d92-3084-a6f1-55f0c21a8f39 | -6.13958 | -57.71398 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bd5e5c4-0bbf-3492-841c-b82bced54fcc | -6.79824 | -58.79178 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12dad3cb-8386-332c-99cd-e911c03e8add | -6.10054 | -55.63646 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50949d5d-9706-3ba0-a843-a444c931f697 | -6.10913 | -55.63425 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74b1682c-9ca2-3fc6-96ab-cef23f485d18 | -6.61927 | -51.14186 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dda5ea2d-ad76-3856-bcc5-d1e36b988dea | -9.73696 | -64.9602 | 2026-09-12 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f008e2ce-f286-31e3-8725-506d384aa702 | -6.21249 | -57.77794 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e80c28f8-e00c-3c95-9d6a-4c4c69ad9a34 | -5.97078 | -57.77307 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dc6ed66-0139-35d3-a4e0-8b88308cfb1d | -6.28709 | -56.02261 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48a2c73c-a51b-3bf8-a438-683b37ef15c0 | -9.53078 | -67.1675 | 2026-09-12 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93031a27-6db8-32e6-86bf-96c6ec1a0ebe | -9.46653 | -50.31588 | 2026-09-12 05:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0618c760-ad7c-3394-a2e8-4ad37e1dbbe0 | -9.46829 | -67.10071 | 2026-09-12 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67bcc94e-115d-31f8-bbd0-fd1b6a5e8041 | -9.41637 | -68.90691 | 2026-09-12 05:29:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39e58733-959d-3cc6-a83f-3ad064a8919b | -9.15999 | -58.30848 | 2026-09-12 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e900dc0-0151-3986-a52b-76c884c853c7 | -10.47927 | -51.36538 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16b4b2b0-10ae-39da-b215-20dbacef9ecd | -11.24294 | -54.1414 | 2026-09-12 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fd0589c-7738-3606-8fb1-7aa3d097cf25 | -8.53339 | -54.71673 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1898580a-46d0-3bc6-8b52-19b8604d83a7 | -6.61166 | -58.84411 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ab617ef-9e4f-3fec-ac6d-aa8fab08a68f | -6.6202 | -58.85684 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README49.md)
