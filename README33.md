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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c4cd52b-a143-3923-8d7e-ba2cca9f1418 | -7.33185 | -55.61551 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8aa82f9-fc8e-3b49-9625-6e7eef3e5c2c | -9.45162 | -45.40062 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4d5dc63e-cfc3-39b2-a262-9d5baab96504 | -7.31459 | -46.76839 | 2026-09-21 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10d7428b-c6cc-34bf-afe2-1e876967db79 | -9.46609 | -45.41788 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17c9ccfd-dd31-3ae7-aecc-dc0a8393c44c | -9.47519 | -45.40445 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3c1d0ff-e7b8-34bc-98c9-34ee1d88072e | -6.7244 | -55.09487 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8f055753-44a4-35c6-a7e8-d61e79cb5186 | -4.21318 | -44.66776 | 2026-09-21 04:19:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c97b02c-f287-368e-b6d6-71564ec7014b | -8.44835 | -46.40007 | 2026-09-21 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 887fc089-62f7-3ff6-ba67-5107c8b3f872 | -9.54265 | -45.39341 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b01fcca5-7c0a-377a-8c51-fef6c4dafc28 | -7.57458 | -57.69498 | 2026-09-21 04:19:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a5e4fb4f-233c-314e-8299-82a4ae87e0a9 | -7.58313 | -57.68914 | 2026-09-21 04:19:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9f0916ac-afbd-3e78-8003-23d546e32c2d | -8.75922 | -44.28097 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 482e5114-3054-30c6-a90a-1136a59c27b7 | -4.5899 | -45.16449 | 2026-09-21 04:19:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3af45cc8-22e2-33cd-bc34-c7b63fee15fb | -6.20324 | -53.56605 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c03ca4f6-06e3-3dee-9d02-e49399e198b3 | -7.43684 | -44.77294 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3eca4a9a-e265-3fa2-ac72-6dcd65dfe078 | -6.47451 | -48.44653 | 2026-09-21 04:19:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be4eae04-2eeb-3a14-973b-9546790f756b | -5.00757 | -56.10011 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d161392e-7d55-323f-8cff-56cef606f72b | -5.8158 | -53.525 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d065ef7c-c6fb-305a-b1df-d1f1e0aaff47 | -5.81075 | -53.52002 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3a65af0-158b-35cf-9bb6-e8ebc34d5ff3 | -6.20581 | -45.35752 | 2026-09-21 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 747827cf-2d95-3dd3-82cb-e90206d8f37b | -8.78801 | -48.73547 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 92e40a2a-df3c-3610-a9df-2ab220b7347a | -4.67779 | -40.14215 | 2026-09-21 04:19:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5502cee4-1a04-3901-9442-4a34585ea0a9 | -7.23936 | -55.60684 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b2fa11cd-685c-332a-8921-4bb4fb4e6c8e | -4.35985 | -47.78435 | 2026-09-21 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60ed5bfe-96b8-342e-991d-85be54a63bc5 | -9.00369 | -44.34589 | 2026-09-21 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5eacde69-e6ff-3c78-ad71-c3b433538267 | -8.3786 | -45.63039 | 2026-09-21 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 587130e3-88da-326a-ac0e-8374318af541 | -5.80594 | -52.09103 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6af1002-d008-35bd-9c48-3e256fe5bc0b | -5.97553 | -52.2009 | 2026-09-21 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b80c3591-310d-3c09-a856-3c6b10f2bf45 | -8.46693 | -45.08591 | 2026-09-21 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9f50f13-b679-3e95-8d16-5a003dcf62ff | -4.34838 | -55.66256 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a614d67f-a7c0-3b0b-bfd6-e0ecdd3693fc | -3.34369 | -42.7646 | 2026-09-21 04:19:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 40095333-da7e-3265-afab-42fc7b3bd059 | -9.44746 | -45.42602 | 2026-09-21 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 006b02b0-7a8f-3c1f-8cd7-938d66b44675 | -3.44208 | -50.60466 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a849f2a-f02d-315c-a26b-64a2e550688f | -7.32546 | -55.61435 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42311f14-59c0-39d9-a432-bd4d0b17baf0 | -6.29607 | -41.76611 | 2026-09-21 04:19:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 58c93c08-10e7-318f-90bd-3c19716466f0 | -7.24336 | -55.58573 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 860f329e-be4d-35dc-a497-da7c4ca78917 | -7.24585 | -55.60757 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 22287d00-1940-3281-93e4-39b077ffc223 | -6.56519 | -45.5458 | 2026-09-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 87deade5-9d96-3c04-b52a-56047854988d | -9.45221 | -45.39698 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 634d3f38-8f16-3af4-97a9-6d18269b1d59 | -6.97996 | -45.82422 | 2026-09-21 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5064c89d-d290-325b-8b87-dbb8b1008f2c | -2.45662 | -49.22682 | 2026-09-21 04:19:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5068581-6835-3fa8-9c39-ef8852254193 | -7.42678 | -44.77131 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 510b3d24-4e70-3960-9f3f-c722dd450924 | -8.73421 | -36.82829 | 2026-09-21 04:19:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3c97ba00-979d-3549-ba1a-2ed22ab4227c | -3.57796 | -49.81098 | 2026-09-21 04:19:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e90d1df4-36d9-3d03-a0b7-f5748362d35b | -9.46053 | -45.40953 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11462aab-3283-3096-a2f2-45ba923abfd8 | -7.29515 | -46.77324 | 2026-09-21 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7207cea2-e76e-3386-be11-0fe19c7e9a62 | -9.27263 | -46.19256 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5c9d788-0917-3475-af52-0c496b5085a8 | -7.71197 | -49.38406 | 2026-09-21 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1d4b5f5-1734-3b99-8043-dd1db69cefc4 | -5.21354 | -56.10646 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 48588bfe-39cd-3ede-8ebf-e3093153501b | -9.02719 | -44.92018 | 2026-09-21 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86b98db8-09c2-3f02-858e-95f3108e4149 | -6.97823 | -39.88887 | 2026-09-21 04:19:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 231cccf1-d008-377f-8b24-98a6b8df96b3 | -2.6101 | -51.72902 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 765ba6b2-042b-3799-b2ed-dbbdf287a812 | -6.14344 | -55.71088 | 2026-09-21 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 77992b3a-e0b9-313e-842b-40b4fb855724 | -1.67637 | -54.9402 | 2026-09-21 04:19:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d8515068-c33e-33d9-aaf2-74e1e9075ff7 | -2.82413 | -46.70679 | 2026-09-21 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 527abf32-e20b-3f2a-b923-3f2793fe578f | -8.57152 | -44.54176 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 578d5778-2d9e-3ccd-9b64-672bf3d077f4 | -7.33923 | -44.46969 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff13cbe0-9b42-386e-802c-43e062e0a92f | -6.76489 | -55.63611 | 2026-09-21 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01275cde-a1c5-3d88-868f-18fe5293aecf | -7.34314 | -44.4667 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba31a4c0-8209-382c-bed1-5f0feb4ff361 | -7.86947 | -49.3019 | 2026-09-21 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 798cb4a5-a3d0-3245-9125-480ada535440 | -9.45459 | -45.38246 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 38df888a-05b7-3743-a9be-4c4f3d060f3a | -3.4461 | -50.61098 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 468bec52-24db-3aaf-9c14-cf4ad410699b | -7.78014 | -44.8171 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3061af1c-9091-30b2-a589-109de3562209 | -8.76901 | -48.73929 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7809d94e-8527-3f99-afec-ba5384b59f1b | -8.76142 | -44.28849 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19179668-c276-3c38-9f16-5a0a5b4df43b | -5.83516 | -53.51624 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9490733c-5f1e-3e9b-98dd-be95ff8b63fa | -4.0951 | -52.12003 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4f0ff879-e02f-3e3a-a48e-93fc062c9cd8 | -9.57631 | -46.54773 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15139e89-d8cd-3535-8e29-f350718fa3a1 | -7.34371 | -44.46316 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee963cea-8a6e-3a17-b76e-2cccc3404af2 | -7.41786 | -44.76258 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6bd7d229-4dce-3b47-aa33-783f64195dcd | -5.81866 | -53.50899 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1518ff4b-a408-31bc-aa0e-6431af505dee | -7.41613 | -44.77328 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b5699443-8810-391c-8d13-e385b9e558a2 | -6.99877 | -43.30157 | 2026-09-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7d58c921-f5bd-3881-a62d-703aff06df5a | -2.61493 | -51.73336 | 2026-09-21 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| befa08de-0746-3989-af5a-f66eee79fb8c | -8.77966 | -44.28069 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bfa45cde-448a-3d7a-a4a9-0061677216c6 | -9.44309 | -45.41041 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2834700f-c125-3ac6-a0a8-be7539b33731 | -6.54986 | -45.57478 | 2026-09-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dba1972f-1eef-3945-a209-61ae1b8a69c5 | -8.0084 | -44.81396 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2eab7b33-fd8a-368b-9907-b4d6fb281890 | -6.91196 | -43.74203 | 2026-09-21 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddadae4f-f5d3-37af-9346-8749b8c52caa | -4.59197 | -45.16444 | 2026-09-21 04:19:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 16ca4d61-b5ea-31e4-8d9b-d90fb288a378 | -5.6328 | -40.87044 | 2026-09-21 04:19:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 24dd4c6d-ac36-364f-aa71-a0386fcf926a | -9.24558 | -46.18417 | 2026-09-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 069f82a4-536b-3151-b366-d65b3d732526 | -6.83284 | -45.55643 | 2026-09-21 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa469b9e-afd8-3f46-a27f-69a2246d1c4a | -7.59303 | -57.67619 | 2026-09-21 04:19:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 525616bd-7b7b-3e6b-b927-bc8535b57047 | -6.89862 | -41.70111 | 2026-09-21 04:19:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2158376d-f20c-306b-86bf-46c1ac0c6e6e | -6.56214 | -44.84624 | 2026-09-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa51c6c3-25e7-39fc-9b57-92e9d022713a | -3.17103 | -48.61388 | 2026-09-21 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cd786da-8302-383c-aaa3-7406728da474 | -3.41172 | -39.28248 | 2026-09-21 04:19:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 37e08b60-b70d-34e0-baf7-13b656934680 | -8.33783 | -50.83713 | 2026-09-21 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 31bb4d5f-69b1-3eac-817b-125bccecc650 | -9.01508 | -48.15543 | 2026-09-21 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92280705-d6c5-311e-a528-5d09ff69b972 | -7.38656 | -51.77567 | 2026-09-21 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0762c35-193b-39d0-81cc-2bc784259f0a | -8.66467 | -45.33656 | 2026-09-21 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9fae878-8271-3878-acc4-b240b46005ba | -9.45042 | -45.4079 | 2026-09-21 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6c1efa7-5c7c-38b2-91a8-883b84cdcd91 | -7.1357 | -42.08635 | 2026-09-21 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d9a95bd2-6d62-34c6-ad43-af2c5af3b3ec | -7.43406 | -44.76884 | 2026-09-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f610491a-44fa-3afb-8b12-70574159b427 | -7.05935 | -49.91122 | 2026-09-21 04:19:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50b3b364-a5ac-3869-8a3b-764bca4a41f0 | -8.78089 | -48.74171 | 2026-09-21 04:19:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35552bc8-cea3-3af8-a89b-0136b1a76602 | -6.44902 | -48.44941 | 2026-09-21 04:19:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f061c0b-32fa-30b8-8c7b-6d10aac69306 | -5.8795 | -53.63656 | 2026-09-21 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57a9878d-77dd-3064-8be6-2229058da397 | -8.7769 | -44.27667 | 2026-09-21 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README34.md)
