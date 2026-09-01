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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb243f05-6dfd-3a64-b324-aacb40390a35 | -10.95019 | -61.65427 | 2026-09-01 05:18:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 59e22191-f6c1-3412-b8d5-302848083f67 | -11.29863 | -50.5681 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 08eca67d-057e-3c61-a8c2-4be70bb8013b | -10.06028 | -59.40712 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6371f1c3-5fca-3e4a-aa3e-9335922366b0 | -15.03069 | -52.76942 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73c45fa3-ce47-307e-af1d-12dcea0a0b00 | -15.25324 | -53.85106 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 072f85c8-ee03-3df2-b2cf-821690c6cdd5 | -13.56929 | -55.14634 | 2026-09-01 05:18:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a071411d-1a28-3c26-aa1b-3c260b7c21c8 | -11.29814 | -50.58246 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 73965ce2-3961-3fd2-ac8e-e3220aec8a62 | -11.24766 | -50.58866 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 390c65d9-60f1-3979-8fb0-16eeae123a3f | -15.64725 | -50.11163 | 2026-09-01 05:18:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b38d7d0d-5498-35db-81d5-6e0ae2bb8427 | -11.26716 | -50.57807 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 79102fb3-e922-3666-813f-78d366ea2522 | -15.66465 | -48.71115 | 2026-09-01 05:18:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23707317-139e-3b79-9f72-ee5aefe2576a | -15.7484 | -56.41825 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54e5e626-b7db-3e83-b028-9c4413cc4ace | -14.7166 | -53.57283 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9769a3c2-fc2d-3250-8170-4af730efb4f1 | -10.7467 | -54.06636 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90104c60-ca8e-3bf4-8f43-4b4dbf7f1c36 | -16.04289 | -54.39441 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 52741ffe-b2b4-374d-b04a-bd20ea7fde92 | -15.25101 | -53.8439 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ff2985e-5651-32cb-a449-f8b99fb33d43 | -11.91112 | -45.07384 | 2026-09-01 05:18:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ddec6e59-63a4-3add-b132-cd51678dcfc0 | -11.10682 | -51.54542 | 2026-09-01 05:18:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| ac7e9e43-7d22-3b6b-ac69-e9915d220911 | -9.0322 | -65.42921 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b7bd9ea-07e8-3078-bb49-4e653a29a0d0 | -9.45524 | -67.45768 | 2026-09-01 05:18:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f2949857-8506-359e-9426-7aca571b21e4 | -15.62419 | -56.38738 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57258918-2c26-3293-8cf0-e79ef2f855c4 | -8.77872 | -69.3444 | 2026-09-01 05:18:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00bc8765-60e2-3a36-befa-c5d3681aa428 | -11.91265 | -45.07105 | 2026-09-01 05:18:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b6d5c7e-db80-3c13-97b0-95e859928f79 | -14.415 | -52.50161 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d059d29-f215-39e7-9784-25ba1c77066c | -13.3819 | -51.76501 | 2026-09-01 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a153008d-d337-3ce9-ab14-25045c1cd8a8 | -12.95685 | -45.96439 | 2026-09-01 05:18:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 88c9e323-dce2-3048-9828-6d513c35af34 | -8.72064 | -67.11188 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7be2995b-f927-3ca5-9459-1157a960efd3 | -9.05933 | -65.48787 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94fb829c-6d60-3db3-a84f-4ddac75f3ca0 | -14.66119 | -53.54948 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca28c439-a20e-3930-a205-5499c223fb43 | -16.47539 | -47.95534 | 2026-09-01 05:18:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 4e5788ad-0302-3dbc-b577-af30f31a36f4 | -15.63754 | -50.11019 | 2026-09-01 05:18:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82120d09-34f5-3b42-946a-e5bc37d45223 | -10.75739 | -54.06794 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 837b71ed-fe37-3c5b-b256-1f671ebfc2d5 | -11.62884 | -54.56958 | 2026-09-01 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 272d58ce-9e22-30d9-ac9d-d0dc478debe4 | -13.38414 | -51.74884 | 2026-09-01 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43a5a657-41d4-310b-80c7-18b8e44f1f82 | -15.05644 | -47.99282 | 2026-09-01 05:18:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35ea8af5-dd40-3667-b0cc-fa09e3b6b418 | -11.2748 | -50.58805 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| edd6bed4-1182-3e98-9a7a-d5f8738761ce | -9.88956 | -60.27722 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a033b175-7d32-3722-bd59-45bb938639fb | -14.38566 | -52.53453 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36ac8394-9166-374c-b526-d766e11bcfd8 | -14.4517 | -52.50662 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e67cf76-37e7-3803-8772-07fe6afb6eee | -11.48489 | -58.51595 | 2026-09-01 05:18:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38d5a5f0-b119-3517-a7d4-8bdb063245c8 | -11.93509 | -45.10252 | 2026-09-01 05:18:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5450540-e6a4-33e3-86dc-8904ddec0883 | -15.21276 | -46.22268 | 2026-09-01 05:18:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1190819b-2339-3ece-8f3f-abde876c8df3 | -14.38469 | -52.54177 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6191a61-8281-3860-be35-21c06ae6f523 | -15.25009 | -53.84579 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab33d321-718b-363d-84f1-a031c25f4b51 | -10.74209 | -54.02391 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54b3c74f-d576-35dc-9cd3-b36ac27617c8 | -10.84405 | -54.03873 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 850d2146-8602-3615-a954-d16c099c1334 | -14.73434 | -53.58556 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6537a9a-9074-3ea1-ba84-844b8e866a22 | -9.00621 | -67.79842 | 2026-09-01 05:18:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6f91cf5-d0c1-3e99-9ed4-785a637e5c91 | -15.25628 | -53.8882 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff3540ec-b6b9-3e2d-87e3-dba19e2f2630 | -8.60442 | -70.21484 | 2026-09-01 05:18:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcbc78ed-e3c9-36b2-a156-fc1342f1609b | -15.63612 | -56.37775 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d6d8d74-1cd6-3e2b-bded-d491235d9585 | -14.39378 | -52.53582 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5832bd2f-06c0-3b25-8c50-1d092387e1c6 | -11.66626 | -47.60759 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35745feb-36a2-33fc-89b3-63d3dbf7fc0c | -14.41549 | -52.49795 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f218a749-b074-3aef-a650-df6a20375f61 | -14.257 | -52.87076 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9de3abb-30eb-35bb-bfd4-d934ec904590 | -13.38357 | -51.75296 | 2026-09-01 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0cbc1ee3-5e68-3327-861c-db64dc0c4504 | -13.38133 | -51.76911 | 2026-09-01 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58817692-cf3f-358b-ab81-ae874670b973 | -8.71478 | -67.11072 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e24885b7-b7e4-3185-bdcb-9abfcbab5fc5 | -15.21761 | -56.35453 | 2026-09-01 05:18:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3906bb7e-6da1-3552-a523-0968f16d6e68 | -10.73852 | -54.02335 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14e81573-6e1d-384f-b0ce-61c04707968f | -15.84758 | -47.68743 | 2026-09-01 05:18:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48438561-e280-386f-a02b-6a253390443a | -15.49108 | -56.01614 | 2026-09-01 05:18:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92bedcee-3be9-3edb-81d0-76d5ffd2c941 | -10.84048 | -54.03818 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f24585a1-aff9-3f44-bf83-fff80e88142b | -15.06155 | -47.99756 | 2026-09-01 05:18:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74fa7489-fa6c-3b13-b954-842c6da0456a | -10.06449 | -59.40368 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 503eedab-e9fe-3012-8a3a-b5e05406abde | -15.25454 | -53.84157 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f91d57b-5020-3433-8933-16c0a99b6a6c | -14.46649 | -52.51987 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7c2a87b6-cac2-33fa-b2de-094c0894f97a | -10.748 | -54.03316 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e738a18-2a13-34ac-9fd0-6dd82ed5e037 | -16.18787 | -49.32254 | 2026-09-01 05:18:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 825ce488-845e-3ee2-8bb1-083c5599e469 | -8.86818 | -66.77344 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de29ff9c-02f2-3378-94bb-a3bdad909004 | -13.32718 | -51.72489 | 2026-09-01 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92d0e2d1-c34a-3441-a5ae-ed3b2a8d1186 | -13.81594 | -54.01082 | 2026-09-01 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4572e11-78c6-3f10-bd18-abaf7c61f621 | -11.66808 | -47.59333 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b2543c8-be12-3eee-a178-0f5ceebe0221 | -14.72424 | -53.57408 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a90c2b5-ae98-38ad-a4d6-f4a7236a0be8 | -9.08404 | -65.38277 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85810952-1de2-3d58-9c19-b8c4cc3350ea | -14.13611 | -52.79375 | 2026-09-01 05:18:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f595e14-5e8b-31a2-b297-e184e8ebab2e | -11.17158 | -55.08982 | 2026-09-01 05:18:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3c543e5b-6927-3c72-971c-4ebc2348032f | -14.40686 | -52.50035 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b8b28579-af6b-3618-81d4-0fc1f9e53e23 | -11.30132 | -50.58187 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 52a702dd-acf7-35f5-8b52-4757ead60ea3 | -9.92721 | -60.49421 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e92a8077-8a3f-3505-8a80-9c4506d891de | -11.30441 | -50.56999 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| a0426cf6-4019-3895-b95e-44c085b7a353 | -10.51208 | -57.43457 | 2026-09-01 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c12a659-14ef-372a-b510-453a7d6933b5 | -15.66333 | -45.95163 | 2026-09-01 05:18:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66c2b6aa-074a-32e5-a99a-7bc23181026c | -14.97243 | -48.14843 | 2026-09-01 05:18:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 93dcfda6-b26d-3d50-a0d5-5889274f9240 | -14.39217 | -52.51697 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 117b3a3b-d82d-3a4a-9c97-36503b02ce33 | -10.09838 | -68.40341 | 2026-09-01 05:18:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1d77807-0c35-3388-aad5-cfa2bb7af73d | -15.61 | -56.38892 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 592254c7-88ea-3882-96b6-f9d70f306418 | -11.06424 | -51.53185 | 2026-09-01 05:18:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc77539a-9379-3116-aec9-18f6ee48c447 | -10.75323 | -54.07146 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c8ce8d2-35d2-3fa3-a3cc-621443dbe730 | -12.94949 | -45.96441 | 2026-09-01 05:18:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 932175b7-d6fb-3e2c-b694-8b0a87859f2f | -12.95627 | -45.9693 | 2026-09-01 05:18:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 346d61e4-ac5f-323b-a497-4d07ef437545 | -15.18672 | -46.23026 | 2026-09-01 05:18:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 515b9a46-4472-32a9-9306-c8f4dd155510 | -13.82839 | -54.01487 | 2026-09-01 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0fbbfe83-0236-350f-871d-3932def549de | -13.38436 | -51.81227 | 2026-09-01 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 588610fc-2444-36bf-84eb-ae0eb7fcb924 | -10.50156 | -59.62266 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b7b987c-b23c-3ccd-ba90-ec12450987fb | -9.06518 | -65.48561 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7732e87-8260-3f13-bbc7-c8744d1267a6 | -16.04226 | -54.39901 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b37940d0-2b59-3792-8549-72969bc0ba45 | -11.2963 | -50.5581 | 2026-09-01 05:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 40eb5985-397f-31e8-ab37-85ba18e762c2 | -11.315 | -50.5774 | 2026-09-01 05:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 9ac8aa1f-9b86-381a-8744-51d68a192ad6 | -6.9552 | -55.635 | 2026-09-01 05:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |


[Clique aqui para ver as próximas entradas](README72.md)
