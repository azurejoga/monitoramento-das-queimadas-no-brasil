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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d2408db-e759-3673-a8f6-713c0b828759 | -11.47058 | -47.59963 | 2026-07-11 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc553dce-bfb7-3956-8ac4-8c833396e304 | -14.73756 | -48.19664 | 2026-07-11 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bdcc148-a9f4-3446-9e10-9c4b5b62f370 | -11.12283 | -38.62863 | 2026-07-11 04:17:00 | NOAA-21 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2810954e-a93a-3c77-a624-e30ed15c6748 | -13.36847 | -54.34222 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26c987b9-383d-3a70-a074-edf31887eb3d | -13.25056 | -45.11065 | 2026-07-11 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb1b2d53-2996-3566-9b7e-af4be921eef5 | -13.38178 | -54.36018 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3f11c43-4b6e-35ee-905f-2206cd82cccb | -13.37996 | -54.3409 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa5b1351-0f00-377a-b114-848ac5d879fa | -13.38719 | -54.36129 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a4892be-7636-39b5-81b5-f5acb11798a5 | -13.34941 | -54.35337 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d860cb0e-ecae-3681-b425-248c2753f543 | -11.47354 | -47.60435 | 2026-07-11 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42c9da4b-487a-3895-94ba-ae075e9aadf2 | -11.88554 | -47.65739 | 2026-07-11 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a82f7e81-f95a-3dd4-9d9a-8c488b0f7f90 | -13.76114 | -46.26016 | 2026-07-11 04:17:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 661d6c90-212f-3f64-8a5f-69f93404682d | -13.76449 | -46.26081 | 2026-07-11 04:17:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c119e5b3-83d8-361a-bbdf-42d11fceb4ea | -13.84991 | -44.97763 | 2026-07-11 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d141e3b-4bd2-3a9b-b497-3fc4325ac971 | -13.37925 | -54.34453 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56ab831f-5704-392b-b41d-315cec96769f | -15.22902 | -52.68369 | 2026-07-11 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 850f0761-196c-343e-bf12-1a7ea401364b | -10.65106 | -46.58086 | 2026-07-11 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b384e3d8-0b29-3b21-8991-01922c7653ed | -12.68743 | -46.50846 | 2026-07-11 04:17:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79914672-a9bc-3201-960a-7fdeaaf37394 | -13.32224 | -54.33999 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15d932a6-d0b8-36c5-a0f8-503d9700214b | -22.58214 | -44.08459 | 2026-07-11 04:17:00 | NOAA-21 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ffca52bd-a2af-3dc6-89c8-620d5779910a | -21.23962 | -44.00638 | 2026-07-11 04:17:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 27a85667-5d40-317d-857f-b6929bdd32b7 | -13.37244 | -54.35057 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab9ff5a9-b2a3-3e8c-a8ca-efa91de4a297 | -9.59781 | -48.54733 | 2026-07-11 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb468d48-f6d1-3278-bfe2-347ca410a47e | -21.97378 | -55.94247 | 2026-07-11 04:17:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25929ee9-8f7b-39a2-80c9-ff65cd1780d5 | -12.46075 | -49.58323 | 2026-07-11 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 01c12c85-2044-32c1-9821-2dd86dcfb186 | -16.33362 | -48.06794 | 2026-07-11 04:17:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edc64d6c-288c-323d-9d03-f75ac359464c | -22.9164 | -49.20644 | 2026-07-11 04:17:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8decd3d5-8738-30e7-8505-ed8f3341bd7e | -10.84915 | -45.03653 | 2026-07-11 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac6ef6ac-95b0-35cc-8c2a-5c3b94dec57e | -12.45612 | -49.58601 | 2026-07-11 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4feb4a1e-5a36-3e6c-8cd4-f17f8038f6cb | -15.59062 | -46.81479 | 2026-07-11 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc4806a8-65ab-3859-bb32-fa42bf506f27 | -13.21535 | -54.31215 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0117f350-e2e0-362b-95db-ce4cbd7d6059 | -11.47284 | -47.6085 | 2026-07-11 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2f2529d-da91-37ac-9d66-f418a3591935 | -9.59695 | -48.55248 | 2026-07-11 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 425b35ad-cd83-38e0-9da8-a7ca1d65de71 | -13.37315 | -54.34696 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e27f63e-f14f-3835-8a04-b4ffa007343c | -13.37568 | -54.36266 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 437b05f3-7eb7-3ddb-9444-f29eff6e818b | -22.98287 | -48.92058 | 2026-07-11 04:17:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 35c6c1a3-03a6-30b1-bb27-8a231afaccb8 | -12.4521 | -49.58527 | 2026-07-11 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cb3542e2-3b91-3efe-b55e-b0204bbf3f57 | -11.90318 | -49.16195 | 2026-07-11 04:17:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e5283f8-b04d-3483-bcf9-97725fea0526 | -20.04885 | -47.79878 | 2026-07-11 04:17:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5251d8f2-872c-3256-95b1-bee65b750845 | -17.83313 | -41.95916 | 2026-07-11 04:17:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9dbdab7e-5242-34f9-9174-8c1c4024d7a9 | -13.43707 | -43.84396 | 2026-07-11 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e93de35e-4671-37d0-b123-aeedc61155ad | -13.37173 | -54.35419 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a606e3ee-0a17-3533-aa89-eb5dcac638de | -13.97611 | -53.93227 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7ba49bf-d526-35b6-a846-ed4e4b169744 | -15.58847 | -46.80677 | 2026-07-11 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5024ecf8-2e5e-35fa-b703-b028db53cb30 | -21.28306 | -41.80955 | 2026-07-11 04:17:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 98e29110-bca4-3ad0-ac07-26103bb23a13 | -13.44039 | -43.84451 | 2026-07-11 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 14afd8cb-c49d-3adf-8773-e3f8a2ed29bb | -21.42773 | -47.06302 | 2026-07-11 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09a1fe15-ad17-3849-9170-a66412f1400d | -13.38607 | -54.33838 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7c20e2f-c400-361d-80ff-e78fd170848c | -10.73692 | -47.26924 | 2026-07-11 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4577195-b703-31dd-b1bd-d94dacb9b61b | -9.57106 | -49.10532 | 2026-07-11 04:17:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c749828-3a4a-309d-9fa2-1ba4e4363b47 | -10.82965 | -49.37969 | 2026-07-11 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45a24916-c768-36dc-8de7-c93b425b1154 | -21.14173 | -43.95753 | 2026-07-11 04:17:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c44a8062-4373-3ac8-b7c8-dfcd27e0a527 | -12.83031 | -44.34101 | 2026-07-11 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c631580-8736-32c2-ad9d-7a066b4f866b | -22.92398 | -49.20369 | 2026-07-11 04:17:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2e88219-c63f-3aa2-b726-20cb5971ad81 | -13.39611 | -54.34439 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 389d0943-06d1-366c-8bfa-87fdff222f00 | -12.94311 | -43.0226 | 2026-07-11 04:17:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3628a586-bfca-3ab9-8f84-27e03680fc60 | -13.37426 | -54.36989 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d540d18c-5699-388c-9c95-d7cbf2d5b9da | -10.38039 | -49.5841 | 2026-07-11 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0c531da7-9601-3153-8e7a-5e96022a8533 | -10.38105 | -49.58026 | 2026-07-11 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8e52fe37-ae5a-3a91-ac51-10264c510d71 | -20.15511 | -54.40363 | 2026-07-11 04:17:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 604d93f8-6e36-3dac-bd19-0a6857de9b45 | -10.68765 | -49.62075 | 2026-07-11 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77d9fe1f-6b72-332c-a1db-a64b4e83208f | -11.70986 | -47.80747 | 2026-07-11 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6451fdb8-60c8-3f5e-9230-680adeafee94 | -13.38931 | -54.35049 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4928520-4617-3e5a-bd1d-25dfab55765a | -13.85321 | -44.97818 | 2026-07-11 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ce7d47c-f524-37bc-a548-1593c48c5ba6 | -10.53928 | -54.86895 | 2026-07-11 04:17:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db0e3b69-b48b-3493-9f64-9681ad67bf3f | -13.84716 | -44.97356 | 2026-07-11 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 913f46fd-9049-302c-9d61-aa10f230c488 | -10.10018 | -47.97981 | 2026-07-11 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 97bb8af8-6e71-3aeb-afb9-8939a1acb85e | -10.12507 | -50.17491 | 2026-07-11 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a3f19cae-d14e-3e75-ba30-0f99512569d4 | -15.58508 | -46.80619 | 2026-07-11 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b2e14ba7-01e3-393e-ad22-b63e92d1cf37 | -9.59678 | -48.54939 | 2026-07-11 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd93433c-90a5-399f-a9b6-550044d9f8b5 | -12.19358 | -44.49662 | 2026-07-11 04:17:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5004ae4c-9c6f-3f7a-a4f6-49bf9e046abb | -13.37497 | -54.36627 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8e663a9-7563-314a-bc8d-d10fdfaf0361 | -10.38455 | -49.58481 | 2026-07-11 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8467e311-5ab6-30f2-90bf-8b9834023a95 | -11.85013 | -48.23891 | 2026-07-11 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17266c9e-1078-3e19-ba6e-cfd7579c5bde | -13.55217 | -39.92213 | 2026-07-11 04:17:00 | NOAA-21 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 84a00d49-ee10-3ec7-ae97-ecbf96d4b6bf | -13.3954 | -54.34803 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef7edaf9-7b6b-3e93-b9de-22d486483097 | -13.97677 | -53.92893 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99427288-e4c4-3ac7-9712-c5b41467080d | -21.76425 | -56.30321 | 2026-07-11 04:17:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fee3948c-46d2-38ca-8893-bef3e482031f | -13.25718 | -45.11173 | 2026-07-11 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ccf80d6-605e-3c6c-8757-94c8b81b716d | -13.36271 | -54.37136 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5be8965b-83a5-3933-9129-5648f5acf79c | -11.9392 | -46.74201 | 2026-07-11 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4bfe24b-824d-3105-ad85-042905ed1d2c | -13.35013 | -54.34975 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1dbfaef-a404-31c6-842e-93677fe8edd5 | -12.82755 | -44.33697 | 2026-07-11 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e5a6225-455d-3a42-b20f-ccecf76e4d01 | -13.38392 | -54.34931 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37716ecd-ad41-37f0-96a8-ca2d0a508098 | -21.59068 | -48.78433 | 2026-07-11 04:17:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44444ef8-4746-3dc9-bb3d-d81cefd7d6e9 | -13.34402 | -54.35222 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bce24995-43f5-3261-8b2b-a7e8989b785a | -13.3825 | -54.35657 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfffa413-b994-3b1c-a033-ee04238d108a | -14.74334 | -48.20624 | 2026-07-11 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5234432-e984-3567-807d-77d13daea77a | -13.25387 | -45.11119 | 2026-07-11 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9b73870-cd6c-3cbc-8dd4-29b075266c73 | -22.3814 | -49.78948 | 2026-07-11 04:17:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 65e702ac-1bda-3722-acf1-64953c066067 | -10.41096 | -46.202 | 2026-07-11 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f12dee2-fe0f-3e7d-838f-e86679ff9409 | -11.83514 | -48.23642 | 2026-07-11 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c187ffd-fcc2-32e8-adc0-c83c9350b6ea | -17.83251 | -41.96374 | 2026-07-11 04:17:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c4b80ff1-7d9a-3e86-a419-bdf60cf76743 | -10.4144 | -46.20257 | 2026-07-11 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8185ee58-12ce-37b6-965f-40812108b77c | -15.59124 | -46.81106 | 2026-07-11 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 341722a5-2869-3e41-a270-40d52b210e8f | -17.4952 | -42.46029 | 2026-07-11 04:17:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9febbb97-d2fc-315a-8bb4-a34f4c0fe09e | -10.09941 | -47.98439 | 2026-07-11 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5680ae8-a44e-3dd6-ac92-99e40bb81435 | -13.38321 | -54.35295 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a70abcf7-ea54-3c0a-8f6e-c65217f9e517 | -10.40869 | -49.44389 | 2026-07-11 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6d551e2-2481-39ec-a6d2-de4407fcdc42 | -21.42383 | -47.06613 | 2026-07-11 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README6.md)
