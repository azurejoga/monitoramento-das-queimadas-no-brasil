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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bc8af26-aaed-3436-ae34-bbd1462841d5 | -15.26633 | -46.35569 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d95ce5c3-ee7c-33b4-9c23-fada94ef9470 | -10.91715 | -47.06487 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 32c16423-3944-3b3e-ab38-24f29abe0b16 | -8.18308 | -50.30217 | 2025-10-07 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9c67a28c-0590-364b-9119-2b42bf93118d | -9.18541 | -47.84315 | 2025-10-07 04:57:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e900df93-3d79-3603-89fb-6aca9273376f | -12.16585 | -51.43778 | 2025-10-07 04:57:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d12349f2-3291-3996-8dad-2abd16ef36bc | -10.42398 | -50.31273 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a2cac9eb-5b40-3737-a259-f0e9905edda8 | -13.36427 | -47.25404 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f062ea5e-0e0d-3a2f-9eb6-576caffe1b6c | -13.27872 | -47.16431 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f79968f-6d3d-343b-85db-b6680a5dee3d | -11.02857 | -50.91893 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c37520d9-b9f2-3df6-af98-927533367de8 | -14.65702 | -48.37837 | 2025-10-07 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df3cf4c7-3d35-34b6-96d8-aadce11fb17c | -11.81235 | -45.12465 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 183c7fcb-49e9-378e-9b8e-37e415abc1b8 | -8.10955 | -55.08054 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f056a57-6b69-3d88-a115-891af890b291 | -13.36969 | -47.25149 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a152fbbb-85ac-3f9c-a8d8-8f69ea273f1c | -15.55549 | -46.83006 | 2025-10-07 04:57:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c6490c60-affe-3570-8911-511905e94a28 | -11.15327 | -54.88644 | 2025-10-07 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2a4cabc-471d-3df9-835a-a4f0918a6fb8 | -13.25219 | -47.17789 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50b716b6-27bb-3940-98c1-d70d6e90f8ef | -9.67804 | -48.39148 | 2025-10-07 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f54f2ff-6132-3063-b340-c066d6c9c146 | -10.80756 | -48.81336 | 2025-10-07 04:57:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d794aee-699d-37ee-80f0-817ff86e972d | -11.15922 | -47.95932 | 2025-10-07 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d911bd7-119e-3940-a0dd-c307601d8d3b | -14.91519 | -51.44516 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| d30fe76c-54b9-30ad-8ca4-71baf97f9d2b | -10.64071 | -57.09544 | 2025-10-07 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbd125e2-5857-3742-91d4-ca6339232fbb | -12.25945 | -55.10777 | 2025-10-07 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b00c8bd-4c68-3967-b600-5c91bd8435b9 | -12.3096 | -55.11216 | 2025-10-07 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbb89135-22f5-3508-adc7-3d9f2f8c643d | -14.75337 | -46.05189 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9e2e1be4-1076-3faa-92f8-93d88bd8b55a | -9.51561 | -51.35968 | 2025-10-07 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 649328db-ba08-3946-91de-02b2ec7211ba | -14.61259 | -52.48889 | 2025-10-07 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5db2291e-0890-3e52-aeb0-094acb4336af | -13.28529 | -48.06023 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 598cd4c7-c332-3d01-b122-167e5dd2a5d2 | -9.33615 | -54.52054 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8726a4a1-2d62-3426-ac3c-934bf6662187 | -15.17429 | -52.76075 | 2025-10-07 04:57:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d6dacfa-5989-3444-8e94-1b74842395b2 | -10.4043 | -45.37672 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6f4a43a-0c52-3fbb-80a7-1e4c1bdd923f | -11.65287 | -46.40431 | 2025-10-07 04:57:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea2b4545-1c49-3748-97d5-7cd271911300 | -8.46651 | -49.22098 | 2025-10-07 04:57:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb14ef89-071b-369b-a1d9-7b1cd585ce6b | -10.09378 | -50.52181 | 2025-10-07 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7e97670-60b6-3ac1-8429-3a72d201d0d0 | -8.62095 | -54.96228 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67c33444-dc98-3dac-8d71-6f139570fd3d | -11.49782 | -44.97515 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5d5fa76-e21e-3a93-902a-bb94bc6cb100 | -9.00748 | -49.21418 | 2025-10-07 04:57:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea8224d3-cc24-3e70-a431-0e7c8ab9f348 | -10.37748 | -50.30403 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| ec067041-c8c9-386d-9feb-c0e8ca4805db | -14.76314 | -46.06463 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f60d7dc1-7ff1-3f22-9716-cbc5065e076b | -13.22108 | -48.46637 | 2025-10-07 04:57:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3639d11-533e-3751-a83f-c03e2020d18b | -11.20902 | -54.98518 | 2025-10-07 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 694568c2-218b-3cc4-a005-ba60e8e1df8c | -11.15437 | -54.87944 | 2025-10-07 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f9d5c1e-8cba-34da-9a68-c73ac3fbfc91 | -9.7833 | -48.28179 | 2025-10-07 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 69f298fd-8687-379b-b30b-a58153cf59d9 | -12.89513 | -54.75236 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dd2ee664-4809-32a9-b457-c439a41808f0 | -10.63944 | -57.09845 | 2025-10-07 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87eed14d-0e7a-3d50-bfe4-4c6fc39b4646 | -10.74841 | -50.4786 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c645152b-884d-3e50-b29f-c654f3a9d4a7 | -11.78548 | -45.13351 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e04f9cd1-ff08-3669-9107-7ed465ef8bd0 | -10.45336 | -50.41437 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 2b9cdde2-ddbe-3cde-81c2-7a6b0ff20d9b | -10.80866 | -56.23746 | 2025-10-07 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5f7fc2a-db81-3705-a5c1-8f83333719fe | -11.94839 | -51.47873 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 060a26f2-e4dd-3a22-a2fd-b08618a9fb4c | -11.93299 | -46.42247 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99e2a147-8f56-3898-9318-2a2405212244 | -12.32229 | -55.11783 | 2025-10-07 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6e6ec5a-9529-32a4-a527-779eebb458ec | -14.80828 | -44.89835 | 2025-10-07 04:57:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4eee15a8-c671-3b12-a6f2-23f3ceb6da05 | -14.76619 | -46.03846 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 93320057-344e-3abd-b048-23d6e2781f9d | -14.62357 | -52.4904 | 2025-10-07 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 217ac356-6a81-397e-b5b8-186cbb95ce2c | -13.7414 | -48.6579 | 2025-10-07 04:57:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a9af265-a2cf-340c-8eb9-96256d25b9d0 | -10.59295 | -54.36557 | 2025-10-07 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 446989fb-02c0-340f-a549-c1b59878af9c | -11.94703 | -46.43712 | 2025-10-07 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 696650b8-2950-3499-80ca-c630efb3b64e | -12.92783 | -54.71734 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fe85db6-8199-3394-b9bd-18e3d6e633a1 | -14.92853 | -51.40594 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af86d9ea-cb54-375e-a1f6-85c8fc071b5f | -14.77333 | -46.07372 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5fcc1bf7-ef00-3316-b250-b1b1c29b23cb | -10.87765 | -56.06512 | 2025-10-07 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3fe2e3c-f082-38a3-9a9c-4a0f91b17272 | -8.06324 | -54.92281 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c55052c-21b7-33ff-8f8f-e21e6203a3fc | -13.37046 | -47.25079 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02001245-349e-330e-97f3-2ff8335c98d6 | -12.24244 | -43.77594 | 2025-10-07 04:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d07133f-6d53-3d9c-8bd9-001c496554c5 | -7.9393 | -63.71478 | 2025-10-07 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33c54e17-8a68-36f8-bacc-1b02c1219da2 | -14.92714 | -51.41605 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f902159e-29a8-3507-a1a0-9dc5c0b93319 | -14.92228 | -51.45133 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c0d54193-44d4-35c8-a4c5-421aaa3f7505 | -8.91126 | -50.60383 | 2025-10-07 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bd31208-9394-3ed1-be3f-572f6efd0c72 | -15.59025 | -47.26735 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fec1e0b7-cab8-3e5e-bf5c-718519ac4b70 | -12.39829 | -51.13907 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccfa496a-f4aa-3072-a928-1940572dbdcf | -10.26141 | -44.38037 | 2025-10-07 04:57:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e34461f0-bea6-31db-923d-3a953914e694 | -14.90746 | -46.86694 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5bb6a88-f55c-369e-a6cb-b11909d94a42 | -13.37525 | -47.53675 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c73799ab-6c5b-3305-b1ef-f3f090f1195a | -13.70682 | -48.07499 | 2025-10-07 04:57:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2b7dcd8f-a100-35a8-8f12-34ee94899315 | -15.50035 | -47.92732 | 2025-10-07 04:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6caa629e-d0cd-3e38-8b2d-dedf373f8b2b | -11.9453 | -51.47355 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b89c9977-7099-38ba-b82a-06f0332b303c | -13.27959 | -47.16436 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2263d42-a747-3b44-a5b1-656c29451192 | -11.7393 | -54.72063 | 2025-10-07 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80ffa5b7-7958-3f58-93a9-d39499893c50 | -15.49606 | -47.92124 | 2025-10-07 04:57:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34f16ba2-c1fe-3c49-be14-3c60619ac585 | -12.18128 | -50.9244 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0a1b9a03-0777-386f-bd59-9b415c593b5a | -12.61491 | -44.76215 | 2025-10-07 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b9f36e4-21c9-356c-8b03-bb08823cc97c | -11.22495 | -54.86195 | 2025-10-07 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bb0bb0b-ae87-3923-a9c7-7b81b7242af0 | -13.71093 | -48.08104 | 2025-10-07 04:57:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 64603c2f-cf54-3c62-86e5-7aba2c0b1bf4 | -13.22557 | -48.45969 | 2025-10-07 04:57:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc1adbfe-6b25-3e2a-ba9e-19136e162986 | -10.21791 | -57.68744 | 2025-10-07 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c9ff6c8-b309-3df8-b50c-e0d0bf0ad3f6 | -15.60234 | -47.2979 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| faac9df1-ba14-3dd7-9b5b-9c6a7c97ca78 | -15.26614 | -48.05342 | 2025-10-07 04:57:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02d499a4-c52e-326f-b987-ab85a78bf4c2 | -15.604 | -47.29927 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 89d09ef0-d7ce-34f2-9f40-aa789118bb80 | -10.99983 | -51.2547 | 2025-10-07 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e734d1fa-acba-3031-b4a3-5abfb7e2abfb | -9.96658 | -43.78434 | 2025-10-07 04:57:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d5aab7b9-c0f0-3e59-85b9-99b119db7484 | -9.78274 | -48.28574 | 2025-10-07 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0866c337-f268-3971-8ea1-d6904eaa12c6 | -8.61483 | -48.79651 | 2025-10-07 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b45f4ed9-b381-3c7c-9a2e-65996e18f844 | -11.1602 | -47.7564 | 2025-10-07 04:57:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b14924a-72fc-3736-8e93-dee7fbcb5033 | -11.77451 | -45.129 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35e2234d-828f-3a13-b364-8b94018e7e29 | -11.25756 | -50.2798 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef87167f-b1fb-3bb1-9935-570f16eadaee | -11.12894 | -47.21613 | 2025-10-07 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c1eb94af-1112-32be-a22b-62383eccbdd9 | -12.35053 | -47.05894 | 2025-10-07 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 3a27ad4c-6902-3b8b-8759-9e343b9708b5 | -12.38599 | -51.08788 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6811d08f-2c0f-3891-9d77-9d3d7acb0992 | -7.61709 | -61.35343 | 2025-10-07 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ed0b22de-a5e4-3cec-b714-daa97652f9db | -13.30095 | -48.05114 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README89.md)
