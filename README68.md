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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8457a953-3fee-3572-b335-a93283d52b27 | -9.75893 | -65.05647 | 2026-09-22 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a307158b-b0af-34e2-a4aa-1cf32ec09a0b | -15.26822 | -47.6051 | 2026-09-22 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c44ba39-b04b-3a9f-ae21-d6289636d641 | -15.74955 | -43.30754 | 2026-09-22 04:49:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fc56a22-c1c9-357b-a266-bef059899a79 | -13.20359 | -51.71932 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfe3ad0b-b4dd-3753-9b53-969332a00d96 | -12.30082 | -50.70229 | 2026-09-22 04:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcb18695-5c0b-3fd6-8a3c-4946c76dcbdd | -10.90003 | -53.97356 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a5df419-7b45-323c-a615-b3ef11142ffd | -10.91838 | -53.94618 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8e8827e9-4014-386e-a4d6-5979d8c7ea8d | -11.99155 | -52.46181 | 2026-09-22 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92667e39-8d48-3e0a-b62d-d865fdfd7fc6 | -10.59709 | -53.97733 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63643332-47e9-392a-bb28-62306826ffa7 | -12.19588 | -47.0312 | 2026-09-22 04:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e0dcdeec-04e8-316f-92fc-a6888951062e | -12.76671 | -52.83238 | 2026-09-22 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6072b2be-3bd5-33fc-9766-a48dfe55112f | -10.59989 | -53.9816 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8d3447bc-e442-3eda-9448-be78303725a1 | -15.60243 | -48.32794 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b7c34871-8ee9-3572-9343-491c1391e19a | -12.15502 | -47.3865 | 2026-09-22 04:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40047272-0430-3d48-9f96-7c4c5a1bd416 | -13.28226 | -51.78288 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2a936f3-3773-36f3-83a6-e3937d34f8bc | -10.5856 | -57.48537 | 2026-09-22 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf08c9d2-e545-349a-b16a-e25934817059 | -9.93735 | -57.51034 | 2026-09-22 04:49:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f6580d2-362f-38e3-84f3-039d08669007 | -15.4493 | -48.48127 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b545eee7-a375-361a-8c4c-0517ad4a9a7b | -10.91998 | -53.95784 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ccb4244-2ab1-3357-ae65-4ca2bb17d0c7 | -13.52311 | -51.52067 | 2026-09-22 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1895e6a1-451b-340b-9bdf-f0483effddd0 | -11.8381 | -46.8143 | 2026-09-22 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc18a261-5808-3c5c-a4de-5ea2b9fba047 | -10.88011 | -54.09615 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdfe3548-b378-3b4a-8263-b398b15b43b8 | -11.04683 | -54.15023 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5b0d5ae-75ba-3830-8543-6fa25d51845c | -15.26588 | -47.60455 | 2026-09-22 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56c36d7e-119c-31ce-9e38-f473fc766121 | -13.71597 | -48.78843 | 2026-09-22 04:49:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 506042fa-95fd-3a88-bb5b-83e0e362d2ed | -13.20638 | -51.72346 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7a8e3d1-ed46-37ad-ae2d-ebaff3fe2531 | -13.07052 | -50.61507 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84e8004e-a3c9-35df-97b5-54b05db2cafc | -11.05058 | -54.15121 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc96b2fe-82a7-379f-9fd8-128a7e5b767b | -11.05119 | -54.14748 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1ad0b83-ef83-3842-8c33-7727b70b209b | -12.36417 | -50.20345 | 2026-09-22 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1a37ba1-a7e4-3e03-8434-fb0659971a60 | -11.95152 | -46.51566 | 2026-09-22 04:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94bc0d5a-4b09-3268-8a38-909b8635b72a | -16.81842 | -50.56747 | 2026-09-22 04:49:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dacc3489-da6c-37bb-93a2-fadd462fbc25 | -11.32183 | -54.03855 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6e226ef7-95ce-35e4-9e62-40e3ea57e012 | -11.04743 | -54.1465 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b863e0de-e62c-32b4-a401-7798e535abff | -10.91898 | -53.94249 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 255270f9-41fc-377b-87f1-e8984b143542 | -12.15452 | -47.39009 | 2026-09-22 04:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a306bfc3-efb7-331d-9a30-f93e6c8c85f4 | -10.61569 | -53.99186 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 69fc9942-231b-316e-b747-563d8e57c0ee | -13.28498 | -51.76486 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fce4ca0a-30d6-3a57-8878-fadd6204a1d8 | -11.32531 | -51.35861 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a866c8be-30f7-399c-ba20-b3c109e9cfc6 | -10.87191 | -53.95374 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ed8ca68-5667-3179-bbff-4370e62973f6 | -11.47231 | -47.74134 | 2026-09-22 04:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9415a235-619b-38bc-aadb-a66332c0b7ed | -11.83392 | -46.81372 | 2026-09-22 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79430ba4-3e3e-31c6-b95a-59dfe6e31534 | -13.52366 | -51.51702 | 2026-09-22 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 6b5804b2-31e2-314e-9867-d149b5085561 | -10.60269 | -53.98589 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c80a20be-f312-3e97-bdd9-be288cb15f7f | -11.32341 | -54.05022 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51d81f2b-a438-3727-a65e-9b40e5eb4077 | -11.95419 | -50.08761 | 2026-09-22 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d973c99-5b91-3b72-b01e-445a4d3c2479 | -12.84746 | -44.34533 | 2026-09-22 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8cdc9276-5148-3570-aaed-8859ae7b1f1a | -11.4726 | -47.74256 | 2026-09-22 04:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4d6382e2-6815-353e-a5cc-7c72597fe0a6 | -11.75132 | -54.57172 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36181123-8e88-3659-8f76-c0ca687e6f44 | -10.90742 | -53.97094 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ee243f8-cc66-3adc-a867-6c71bd830e4e | -12.56668 | -45.97432 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| a03ba038-5aa4-3148-bf23-53a78b98e766 | -10.61289 | -53.98758 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| b0d629eb-ad44-3ad7-8cf9-2aac7435843a | -10.86566 | -57.16592 | 2026-09-22 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ed087602-8934-3ed2-ac6d-23b6f6501479 | -10.22028 | -59.40242 | 2026-09-22 04:49:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e2186d7c-3a41-30c7-86ec-920b76095b6a | -13.18136 | -43.40614 | 2026-09-22 04:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8f85a34-52d1-35ec-aa73-dfe68d60dcc2 | -11.95527 | -46.51996 | 2026-09-22 04:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ecddec77-ba54-3377-b960-a384929dd080 | -10.59929 | -53.98532 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d50bec3c-7f3d-3871-a931-8e755678f9f0 | -14.34802 | -49.05164 | 2026-09-22 04:49:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96ddc71b-86a9-3d2f-bae2-7c5cf6f173b4 | -11.88662 | -49.00997 | 2026-09-22 04:49:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f05c98a-a923-30e3-a8e7-6bd78ba48db7 | -13.40384 | -49.48144 | 2026-09-22 04:49:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9c6a37e-d7e7-3d08-b99d-a0dc07748c95 | -13.86353 | -48.58335 | 2026-09-22 04:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09b114a4-cd81-3805-98a8-d14e67a3fbeb | -14.75245 | -48.42831 | 2026-09-22 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c45ed388-94bb-36ab-a1aa-2cfd972d4e7c | -14.75887 | -48.44003 | 2026-09-22 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 326c9a88-8add-3fa8-8877-ef14a6be1cf5 | -10.93498 | -58.33429 | 2026-09-22 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae553102-f62e-3896-9d40-7aa23c3ac860 | -14.76145 | -48.45055 | 2026-09-22 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6be87aa0-f2e2-3d55-8733-021cf40604d3 | -12.89438 | -52.07621 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 973dd052-4e31-3741-81c7-dd7b230aa51a | -12.92956 | -51.01887 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b3ecd9b-b367-39b2-a84e-f23d0661688c | -16.67583 | -41.84851 | 2026-09-22 04:49:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 30c2e8a0-8b8d-3798-b9ec-f90f39829e06 | -11.88138 | -46.84014 | 2026-09-22 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd6c2d1e-d53d-3d96-ba9b-c6fe0bbb0329 | -11.01518 | -54.12959 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 246a2abf-39d0-3ff6-a988-500b4b7bcaf5 | -9.28592 | -60.61597 | 2026-09-22 04:49:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e726d197-edc0-3522-9217-fbb7729e90fd | -15.44351 | -48.46465 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 25af642a-fd47-35bd-81e1-fba284c2c365 | -13.27279 | -51.32813 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b360377e-5464-38b9-96d2-b60449cfac4f | -12.56839 | -45.96075 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| d2bb6585-4415-30e5-9fc4-ee7da040d19f | -10.60329 | -53.98217 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bcc7ccca-02cd-3922-ad6f-060836bc5156 | -12.30876 | -50.69584 | 2026-09-22 04:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3439f478-4c31-393b-80b1-833942bcceb8 | -11.50643 | -51.5076 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38063dbe-fc09-3b67-9d36-cf1622a7d1c0 | -11.08905 | -49.75049 | 2026-09-22 04:49:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 866511af-cd1c-3a2a-8401-d50eb25fa0fd | -14.67158 | -45.67046 | 2026-09-22 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6a86ab08-fa0c-3f10-a22d-41cde23c0f2f | -11.32582 | -54.0354 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc44ca3a-a62b-3c70-a671-ad45f3167e2c | -14.63605 | -45.66949 | 2026-09-22 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cce0f41d-62b2-3181-820e-0aa155239252 | -11.50087 | -51.49944 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc4b275b-eb7a-3d7f-a108-cc8915745fd6 | -13.27224 | -51.33181 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a786031-6a89-3ef4-8366-ef86d37211c1 | -14.04514 | -52.06231 | 2026-09-22 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc52b632-5295-33f2-bb79-46659732ede1 | -12.40909 | -47.08133 | 2026-09-22 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3ca77d19-c528-3163-810f-5621061fd13f | -12.14732 | -45.12996 | 2026-09-22 04:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae80245b-2a9c-3ae8-93b7-642fdc1ebf98 | -13.62727 | -42.47925 | 2026-09-22 04:49:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b6634c25-950b-3e8c-a5d5-137a959d8ea9 | -12.56955 | -45.96281 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 55673b08-9906-3e5e-9626-d2af2ebc10fe | -14.92089 | -49.89638 | 2026-09-22 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| beb83dd4-98c0-3a47-8fb7-16d06632edd0 | -14.76598 | -48.44655 | 2026-09-22 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c79bc51-e331-3723-83b5-979ed41ee39f | -11.16515 | -51.11738 | 2026-09-22 04:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 59449094-3cc5-38ae-9679-12aabfe87086 | -15.46454 | -48.39837 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa68e133-6b61-3890-aeed-a9795a24a09a | -15.26636 | -47.6007 | 2026-09-22 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5068349-3602-3feb-8e91-b7bce0d60c15 | -13.21833 | -46.93975 | 2026-09-22 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 246995da-f883-37a4-86b5-30cb3968c390 | -10.6898 | -54.48578 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad91156f-bf4e-320a-892a-a118c64aa2b7 | -10.91659 | -53.95729 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8e12773-fd8c-3ea0-9ab0-40c077723e42 | -13.92449 | -48.56705 | 2026-09-22 04:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bfb37b36-acec-32a2-a1c3-b7dc61ddbade | -15.42036 | -47.20364 | 2026-09-22 04:49:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33796fb0-82bb-3e8b-b85d-2196ace3940a | -12.92884 | -50.931 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a11cba7a-48ad-3c4e-a4fe-9754bb70d24e | -10.90522 | -53.96301 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README69.md)
