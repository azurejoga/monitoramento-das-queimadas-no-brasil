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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d04bc1e4-df5a-33f5-9472-383c1da20f94 | -7.63369 | -46.54906 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8b797ea-5239-323c-8389-acc090975de3 | -8.08227 | -49.94285 | 2025-09-01 04:10:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06c6fee7-244d-35a7-b2eb-fb710c546304 | -7.88281 | -46.99395 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ceedfb50-cfda-3fda-8e65-94a1c084c01c | -11.36862 | -43.62365 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a8f9bb6-ff39-320f-b7cd-ae4c0bb1bc57 | -10.12128 | -45.76642 | 2025-09-01 04:10:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86d451aa-149d-30d0-9f8f-cb074379cafc | -6.28549 | -43.82377 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cd04d90-05b5-311a-a9aa-a2405133605f | -7.24294 | -44.06055 | 2025-09-01 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d4c3a48-7fb0-394b-ba5e-0a86c4ff2586 | -11.32323 | -43.46946 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26ceeba9-6ad4-369b-89fb-aed2d1d923bb | -5.80277 | -42.5444 | 2025-09-01 04:10:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5c3fea3f-3eec-31ad-b18f-44ce50e41f98 | -6.51186 | -43.56367 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e65fbcd2-7fdf-32b3-b693-abc773de5d2d | -8.83385 | -47.4968 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83f5d7ba-a601-3b68-94a5-261c7d8ddb5d | -6.14277 | -43.32084 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5fa5fbdb-ce29-3e09-9923-47e7c5d72a09 | -6.17203 | -44.12077 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cae18c08-7b15-37ba-a169-e7c3d2eb06d8 | -7.99943 | -44.05188 | 2025-09-01 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aede5037-392a-3b6f-b08e-0438f87e6c41 | -6.15937 | -43.32738 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a51f5f2d-6b1b-3b97-ab48-1f655a7f7227 | -11.91636 | -46.44556 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f1fee1f-f0d4-3ecb-a398-c0b825fc72ba | -5.8513 | -43.22209 | 2025-09-01 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c663e36-f22b-334c-af15-d88b3a93a554 | -10.04879 | -48.09903 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| aa79f44f-9ccf-3da6-bcbf-b2461613850e | -12.30721 | -45.67982 | 2025-09-01 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1019c54-a273-3404-a900-71a07437fd5e | -5.85281 | -42.53408 | 2025-09-01 04:10:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b3465588-0f4a-3bd3-bfef-64f9c06140e2 | -10.04237 | -48.11052 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0d16a27d-1752-3cc8-aa59-1f3136324aa6 | -7.08229 | -44.35583 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 1fd96a9d-c3e5-3dfd-a132-118ffbf68999 | -10.60665 | -44.33292 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| e0ab5a09-ef9c-3dfc-941e-2e4fc6e6cb9b | -9.64349 | -47.82114 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6992f4b3-da6c-3a2d-b5f6-80d6597663bf | -8.18943 | -42.30231 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 593679dd-f12f-3cc0-9e22-6ae1714c5d01 | -6.11721 | -43.28235 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f1e74156-6c57-3ab0-92cd-1ceb195673e1 | -5.82474 | -51.38173 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e86d741-9dc6-3a5a-82fd-b3db0022ddd9 | -10.05087 | -48.08734 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d0a6fb1c-022c-3a14-b4b0-7915cce37dd5 | -9.15612 | -45.22146 | 2025-09-01 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef637d1a-110b-3f67-82cf-512494c66799 | -6.45803 | -43.96208 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 65a17f08-a20d-36d7-8afa-da465062b520 | -11.33253 | -43.51876 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bd1622b-325d-3c5f-9793-8f52d27dd31b | -7.08623 | -44.34069 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| bc2dfc63-edf3-3f64-a673-763f5bccde98 | -7.62951 | -42.65282 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d4523a79-569f-3141-a29a-fcaac009f82a | -6.7943 | -52.81359 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 087c9109-ed78-38c0-9098-a5e39d988044 | -6.70934 | -42.2493 | 2025-09-01 04:10:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f3611d28-8559-3d7b-8bcc-097493a1114c | -13.65564 | -46.93188 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d4a0ce4-e6a7-3579-9290-f799e94e529d | -12.40531 | -46.46157 | 2025-09-01 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51694f80-3048-3f58-adb8-22601623c676 | -12.96103 | -48.11761 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0efca122-b356-342f-8f9b-396d8fa0d1bb | -12.7964 | -48.08336 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8597172f-705d-313a-8551-94feb3a3d9ba | -12.59717 | -48.21538 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 09693acb-5299-30f1-9053-ac7369f08f57 | -17.15396 | -46.08207 | 2025-09-01 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b8e2752-09da-3d85-9490-3db7c9aed6f7 | -15.69408 | -48.93863 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e62369a4-f0e8-3a91-83ff-b499bdc668ee | -14.78794 | -46.73673 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81e3a872-3e9d-3b05-99e9-1ba3a53afb49 | -13.58194 | -46.93425 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d03650db-884a-3d04-852d-cda3f326c2b2 | -16.07884 | -43.62502 | 2025-09-01 04:12:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b07e7b42-2906-3ec6-b5c3-99fd4cfd6533 | -12.9428 | -48.10276 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c49032e-bcc1-33ea-8606-040050de71ff | -13.18021 | -45.28078 | 2025-09-01 04:12:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92b51d97-c1df-3459-b9c8-d9f1f76d2f6c | -14.75186 | -46.77159 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1148eda8-cd7f-38b8-b2f0-97e04dbb767c | -13.71061 | -46.92986 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f040660-d12a-3a13-bc63-8c360e6d5f0d | -14.37246 | -53.30686 | 2025-09-01 04:12:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 964a9a6e-9f42-30ea-acac-6c19bf3dde28 | -12.59031 | -48.19056 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 091fdd20-6ae0-3db6-8148-606752ae216f | -14.80021 | -46.73095 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67dd4413-969b-344c-af44-1630160ea94c | -14.48757 | -52.98958 | 2025-09-01 04:12:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a0e0c62-3c87-3357-8ab0-431d86d90392 | -16.97027 | -49.30032 | 2025-09-01 04:12:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 215734c0-f48a-37b7-8e34-6a24b68dbf7c | -15.29849 | -52.78738 | 2025-09-01 04:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 875c9161-4ea5-3c17-a909-0f2160811649 | -14.78941 | -46.72808 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eb3398d9-c50e-3e75-8011-f196a2302999 | -12.84355 | -48.07651 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e26ceab3-fca4-31de-a0d6-fea663766bbb | -13.51421 | -46.99036 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c8da227d-a702-3197-82ab-34d7e20b3871 | -15.69455 | -48.91274 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8c2bdd05-69f0-36c6-ba3f-84e053aff65f | -15.16016 | -52.3475 | 2025-09-01 04:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 183c24bc-41f4-3852-b79b-0e6ed4952ab4 | -12.60262 | -48.20866 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 562804c3-4bf0-3d1a-86ea-316c6ed38bde | -15.23204 | -53.7975 | 2025-09-01 04:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ceec82fb-979f-3dd1-ab65-c7464032a3fa | -12.87391 | -48.09371 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23116f96-bc2d-3ec4-b90c-9f3340e77962 | -13.347 | -47.04147 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92d59c2a-de76-3190-996d-a479eab40116 | -18.07265 | -45.94305 | 2025-09-01 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b39d507-37fe-3ceb-9c52-1d6b3d794662 | -15.31989 | -46.11421 | 2025-09-01 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa25a555-bb4c-3045-abbe-531e90da3920 | -16.29072 | -52.94132 | 2025-09-01 04:12:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7e4cbb2b-61f6-358b-ae87-4a1b484bc87d | -13.32318 | -46.8644 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 36da5007-1e77-3b6e-93d2-6819a64ab0b3 | -10.88138 | -55.75547 | 2025-09-01 04:12:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc56a3ab-f2d1-363d-b129-c401353dab20 | -12.57366 | -44.80338 | 2025-09-01 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3129358c-3c81-3669-9109-ba147b5c364d | -12.8389 | -48.07941 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9439665d-4ec8-3067-a225-005f1aae17f0 | -13.69411 | -46.90941 | 2025-09-01 04:12:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6e6a620-df2b-34fd-8d66-dd55152319a9 | -14.7753 | -46.76663 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5d7a76d-e663-3d13-8ea0-1f7c59845bd2 | -15.70077 | -48.90161 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| da2f18cd-cdea-327c-b456-444e7ae03348 | -14.8464 | -47.0962 | 2025-09-01 04:12:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6739ab9c-32c7-384e-a229-dc4f48301ffd | -14.77453 | -46.77118 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4677d036-0fc1-3264-ad06-9e15803dbf64 | -12.80981 | -48.07847 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36b35077-f994-37c9-a202-4ae6eb536635 | -14.81256 | -46.72318 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| beb1accd-1bf7-3b92-825a-737b38f88403 | -12.60127 | -48.21611 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d4b4d93d-d958-3532-9680-0e1331288782 | -14.74256 | -46.73828 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59d7bfae-046f-39b3-a305-d20da7f1b129 | -12.96245 | -48.10977 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3828f381-4f87-3703-8aa3-7e5cfa76e852 | -13.29344 | -46.90214 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2de2158c-3c10-3f89-ac2c-c9e17189decf | -12.95839 | -48.10909 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b82bd1c-d4dc-3158-b247-8def09419ed7 | -12.78232 | -48.09193 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f7274c0-1cb9-33e9-b480-1dba3084fb82 | -12.59999 | -48.20773 | 2025-09-01 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1a23b117-52be-3cd6-9026-07c9765fa97d | -12.62288 | -45.54752 | 2025-09-01 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c5c0be4-b6e8-3647-a488-f4e9da194fdc | -14.83724 | -46.73244 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 797611c8-268b-3391-91c2-928cea5f38f7 | -12.61411 | -45.51277 | 2025-09-01 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a7ef1c7-c941-3498-97fd-cb875c24169e | -13.37725 | -46.95311 | 2025-09-01 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9bf2cf52-4e1b-31f1-a596-07b078549639 | -18.07542 | -45.94754 | 2025-09-01 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5267c340-ff99-3f70-9a18-8a91eb4a3776 | -14.78494 | -46.7104 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e80b8d3e-196f-3832-8dbe-abed89a72e83 | -14.04617 | -44.58406 | 2025-09-01 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c32d3ac7-99be-38b4-9591-2929b2819683 | -11.51516 | -54.4765 | 2025-09-01 04:12:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ff9de78f-3a25-3edd-841b-19a5b487cc36 | -18.07479 | -45.95138 | 2025-09-01 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa54b1e5-d008-3ab4-ac3d-a7c3d231ef5d | -12.57149 | -44.79518 | 2025-09-01 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6478bea5-fcf7-331e-98e2-02d8703f948e | -15.69592 | -48.90521 | 2025-09-01 04:12:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92a43992-49e2-3095-9e4a-b92777f3a9b9 | -14.41801 | -51.66285 | 2025-09-01 04:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 552a45f0-2925-3996-b263-df49050838f7 | -15.32946 | -46.05742 | 2025-09-01 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4c009c4-dcdf-326c-960d-10eb14da241f | -10.87309 | -55.76128 | 2025-09-01 04:12:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c325ed9d-7c43-3859-93f4-9fb6ecc487a7 | -14.78643 | -46.74554 | 2025-09-01 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README41.md)
