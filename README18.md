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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0b1cd72-4314-32db-bc78-0805561f774c | -12.26903 | -50.69294 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1095eeb6-080a-325b-8bb0-e1dfee138b0a | -14.49767 | -48.32915 | 2026-09-27 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 383fbab3-0041-39f1-aacd-1ec9ab9b27a6 | -12.47307 | -47.48515 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fe3d9940-85b6-3421-b9a7-46a5893f4d02 | -13.66274 | -44.31461 | 2026-09-27 04:10:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59348875-3e72-3811-9f55-74e25f7ba584 | -16.7975 | -39.41646 | 2026-09-27 04:10:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5aa30a68-36f4-3170-9c6a-72653dffec64 | -13.33755 | -46.80438 | 2026-09-27 04:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9dd81717-7a6b-3036-acd9-2437cd53da2b | -12.29697 | -50.29777 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 23741494-69b6-3182-902f-c164970741e8 | -12.25111 | -50.70645 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9107efb7-4cec-3a77-9fb2-2a4f19364234 | -12.83371 | -48.18791 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 93dc5cf8-9f1b-3f4a-b770-d764bddd8f1a | -11.88761 | -50.51003 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4be905bf-f762-33e5-99a0-d002f01a5038 | -14.11835 | -46.34097 | 2026-09-27 04:10:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 014ea14c-98fa-3350-bff2-081a101a232a | -12.28133 | -50.37929 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d37687b3-b8e1-368f-a05f-a98328223a48 | -13.21305 | -42.22537 | 2026-09-27 04:10:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 7fac6338-f135-39d5-8df7-2dd745c9a812 | -15.47756 | -46.15187 | 2026-09-27 04:10:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cefb3566-6c26-300d-8ceb-08ce61b892fe | -14.79318 | -45.95599 | 2026-09-27 04:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9fdfb11f-475e-39fb-a4e4-9abe0f79b550 | -11.91962 | -50.51311 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de51430e-e0e4-3ef3-9a4a-853fe58d075e | -11.88634 | -50.51657 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 1758b30a-16b9-3eca-be44-794b7b06bf4f | -11.77128 | -51.01729 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5025e82-4933-3c08-8e31-0abaca5ee0fd | -13.33291 | -46.80711 | 2026-09-27 04:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f33d9f5f-db35-3bfb-b09f-779c9c15c398 | -13.00503 | -48.67386 | 2026-09-27 04:10:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 605b7889-dc32-392b-8dc2-ee2379a45004 | -12.07627 | -42.21468 | 2026-09-27 04:10:00 | NOAA-20 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ab3bef1c-789c-328a-81b2-4ebb637cd7b5 | -12.3009 | -50.30503 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f0feaf3c-6675-34a5-9b3f-606cdfbb3cd0 | -11.87918 | -50.52533 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f9ba0c9-cab1-3dfd-b347-cea8237f6ef1 | -12.02031 | -50.60985 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e4dbffc-cda2-36a3-876b-91078aaadaf2 | -11.97102 | -50.58272 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76f33852-9685-32bd-b338-465b80485c27 | -12.27981 | -50.304 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 814c8459-29ee-38ee-9354-f66b219e6f4e | -12.28768 | -50.37404 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cab30f88-a5b1-37e1-8ee8-2c6eaa681f18 | -11.03356 | -51.32858 | 2026-09-27 04:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80fccbbf-518e-3565-8901-c3228159d483 | -11.77459 | -51.02905 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fada5b3-8aef-33e8-a3cf-1b55c3ef8ff8 | -12.80904 | -41.92591 | 2026-09-27 04:10:00 | NOAA-20 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 46b35ffc-a1c2-3160-abe7-083ae68d10e7 | -12.13902 | -50.32571 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72ba0269-d984-30a4-977c-f24eb0ccb015 | -12.13904 | -50.33264 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03928a32-71d2-32f2-b30c-4f0a0000303b | -17.83043 | -46.56164 | 2026-09-27 04:10:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fe9525cb-d4ce-3b16-a723-ecf808ad5393 | -11.98602 | -50.56415 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3626c815-0f40-3994-a523-dc010bd9ce65 | -12.25828 | -50.69753 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 70cb72df-dd45-371e-b559-373858bff717 | -12.12714 | -50.30368 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c61003c6-e4ef-3a9b-b394-c067d889856c | -15.33549 | -42.90893 | 2026-09-27 04:10:00 | NOAA-20 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 00ccdb5e-adb4-3297-b99e-6a5bcb582e06 | -15.42607 | -41.52154 | 2026-09-27 04:10:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 74c7e878-ddec-329f-bee8-af68c9a4a512 | -13.09123 | -47.41043 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ad727a93-e12e-37ad-9906-057a4924a41f | -12.25765 | -50.70087 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b1274b7f-0788-370a-934e-195380842ba4 | -12.26775 | -50.31129 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| f0e7d15c-b431-3b57-beb9-7d2c48b484cd | -11.76908 | -51.0228 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 889e9de6-d19f-3553-8b09-020dc17a7893 | -12.04971 | -50.59871 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 785fb01d-cf39-3ce6-8c4c-80c1a4eb11c0 | -17.7904 | -47.16943 | 2026-09-27 04:10:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 80186149-9fdd-31ac-b403-aeb5318a19f9 | -12.29803 | -50.74035 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40a932dc-9ea6-36ac-8212-26d3a688fa6b | -12.12081 | -50.30892 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07fbc60b-a3c6-3e61-82f3-13db7b8591d9 | -12.27468 | -50.30296 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| b59b0e24-c94f-3cc4-8089-8176c3590836 | -13.43681 | -43.82449 | 2026-09-27 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1530fdab-7b9e-3ab2-9872-ee7d398748f0 | -12.03985 | -50.59327 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d266f7d-2b89-3416-b851-641ddc9f02c6 | -12.122 | -50.30264 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2f6d6b0-101b-3436-9c21-c585d98be7cd | -11.9307 | -50.512 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 341376e8-1aea-3f96-b6ad-7fd8b92c9217 | -14.7248 | -45.5803 | 2026-09-27 04:10:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9558adb-8cbe-3cab-850b-6333e67fb8c2 | -18.09974 | -45.5794 | 2026-09-27 04:10:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b85c00d-36ed-3f6a-ad29-3735ecc41164 | -12.71235 | -47.31845 | 2026-09-27 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| efb8f18a-6d37-3f27-80eb-e428e7264a4e | -11.77409 | -51.00314 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ca05cab5-127f-3b63-a50a-606ee7035b24 | -12.69415 | -47.32008 | 2026-09-27 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f49a6b02-b881-3c67-a4b5-ff7b3b823be3 | -13.08838 | -47.42641 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d377db9c-f8e8-30b6-9ec2-3508fdf30521 | -12.66978 | -47.31134 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b038652-ed77-3cf9-931f-1585a64bfb76 | -12.26417 | -50.69529 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 037248f2-0e69-304d-82cf-4c9517c80126 | -13.21248 | -42.22895 | 2026-09-27 04:10:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 25.3 |
| d7b4e9bb-fc5f-3ebd-8135-8c3ea6c3d30d | -11.77269 | -51.01021 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bebd02fb-6004-3e23-8639-75d83ad39d35 | -11.271 | -54.43462 | 2026-09-27 04:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79393548-0ece-344c-bdfa-53a3302c48ee | -12.13666 | -50.33834 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a700c09-a661-393f-ad4b-c12586757c76 | -11.24025 | -49.85185 | 2026-09-27 04:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c82db82f-d555-3b7e-9851-923316c001cf | -14.39929 | -43.7798 | 2026-09-27 04:10:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2dce1bdf-4687-349f-8279-b99ab5f0f03a | -11.85916 | -50.51937 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2f15d843-cc90-342e-8b0e-880fa2f5de1a | -13.09803 | -47.42079 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f35cf57f-802e-3190-848a-2105d46fef79 | -11.8801 | -50.52363 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b4d035c2-51f7-37f6-8c15-adb4750af350 | -11.8857 | -50.51984 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 212c4fe5-3080-3a74-817e-4fc4acef5a3d | -12.70745 | -47.3216 | 2026-09-27 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7ef0d203-6627-3fef-a678-ee9b1572d798 | -15.67151 | -41.03291 | 2026-09-27 04:10:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 662edc5c-adf6-330d-9f57-504016568cef | -12.13965 | -50.32949 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd5b3b02-b796-31c3-ab62-570eeb2b0a4d | -12.27287 | -50.31233 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| b21ce730-f573-39a6-9306-07f4d0f3c2b3 | -12.25175 | -50.70311 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b1c9427-68b5-303a-9acf-6e92f44e578a | -11.77198 | -51.01375 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a10be73f-9818-3bb2-8fe6-a4505b389ac5 | -11.91899 | -50.51639 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a84b4d77-c1fd-36f7-a577-81ac1511316f | -11.88133 | -50.51706 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ceb6de8a-3fa8-3591-ba10-b0bcae17a492 | -14.5004 | -48.33856 | 2026-09-27 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aab7d133-6402-3224-98ca-16bbfd73c940 | -12.29436 | -50.39508 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39e4879f-097c-33fd-b172-84c4b0819e7b | -13.85382 | -43.99754 | 2026-09-27 04:10:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d47e84bb-72d7-3e3e-a33f-a99a4ea07cb5 | -12.30662 | -50.30296 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fddf6ac2-aec2-313c-846f-94554e5d827e | -12.12655 | -50.30683 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9defb7a2-0959-3f3e-963c-e65ff9c3aa57 | -13.64858 | -43.33057 | 2026-09-27 04:10:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 72f89f65-b917-3298-8f6f-ee56e5245322 | -12.17447 | -47.38175 | 2026-09-27 04:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c84ac2d-77f7-35f1-ba61-7c7b9ddb37a8 | -11.88111 | -50.51551 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 9ed09629-e92c-3049-ba0e-509eb164f1bd | -12.28041 | -50.30089 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 08c02f7e-bb26-36e5-82db-06dff37678d3 | -12.27408 | -50.30608 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 96d9dea4-d14b-38e3-b39c-7f678e5cade6 | -12.71162 | -47.32241 | 2026-09-27 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dc13b176-dc57-3e86-bc14-d873e14252f6 | -12.27429 | -50.69402 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d7556c2-3607-3043-a6c0-95a5d439c1ae | -13.30717 | -42.40219 | 2026-09-27 04:10:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 57557436-30fd-3b38-87ee-6dfd7d3bfe55 | -14.72114 | -45.57967 | 2026-09-27 04:10:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cda491f4-9374-3fb9-afef-62802c9dd535 | -12.21024 | -50.3799 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87952c14-f5e3-3d5d-b8d7-8a96c1f46217 | -13.09406 | -47.39456 | 2026-09-27 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 474c0302-df2a-3217-bcae-c75b4ed5a060 | -12.27618 | -50.37824 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5eb70d3-b9af-365e-8f67-40f629d2062b | -13.08642 | -47.41315 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03dfc556-c6b4-3b19-90f8-0ddd6fe0220f | -12.13843 | -50.32887 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b8db5a3-562a-3305-8df5-9e8384313dd0 | -11.02123 | -54.0467 | 2026-09-27 04:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6cdea93f-1543-3d93-ba3a-4b54b0f964e9 | -12.27347 | -50.30921 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 41f9b1a9-859d-3084-bb6b-7fc691a65878 | -12.25701 | -50.7042 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2f92119f-4906-3a99-adcb-858ff6ebe9f9 | -12.67047 | -47.30745 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README19.md)
