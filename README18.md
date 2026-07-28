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
| 42f1a046-7b86-35e6-9a8b-d4406601271a | -20.60371 | -57.23767 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94d2ced7-9f90-38dd-a0cb-7555d70902e4 | -13.29726 | -45.1054 | 2026-07-28 04:53:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 5c84a977-ca91-3270-b20a-f43bb8b140c5 | -13.97864 | -53.94831 | 2026-07-28 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dea54597-d96e-3f3a-896c-88957664bc18 | -10.9343 | -43.05059 | 2026-07-28 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 2e804af8-d792-3abe-85e6-d832b46fefa4 | -15.80133 | -56.6998 | 2026-07-28 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d5ed89a7-33b0-3d23-8476-32127a1a5784 | -12.45416 | -46.51 | 2026-07-28 04:53:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b4b388b6-5c08-3011-a841-68307d073c81 | -10.7508 | -42.08942 | 2026-07-28 04:53:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7b74f619-8e07-32b3-b184-693ccf8b8e86 | -9.60882 | -47.75603 | 2026-07-28 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf185b5f-eff7-3e2e-aead-c5369e83cbd6 | -13.98198 | -53.94888 | 2026-07-28 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dae22bb9-6401-373a-831d-7170b21123db | -13.9914 | -53.95416 | 2026-07-28 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 701443d0-6efc-3388-8a8b-47b479cc46bb | -12.8439 | -44.3856 | 2026-07-28 04:53:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 95d0f56c-a5e7-3a1d-9666-2477b8aa626d | -11.98436 | -45.5472 | 2026-07-28 04:53:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49c648f8-6195-3c29-9059-8ad83b2b0317 | -16.86414 | -49.58303 | 2026-07-28 04:53:00 | NOAA-20 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a38c84fb-2dbb-36e6-9cdf-b2fadaca9a1f | -12.84889 | -44.38629 | 2026-07-28 04:53:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fe6bd0e1-26d6-344f-b5e0-80ea10031081 | -13.72284 | -51.89366 | 2026-07-28 04:53:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c82b3c8-6cf7-3ad8-92e4-ff25450a6d0a | -10.94063 | -43.05643 | 2026-07-28 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 47a76556-1358-3737-9f75-40f7786aa2e0 | -12.45736 | -46.51873 | 2026-07-28 04:53:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2048b2cd-4588-3a67-b730-229e9d1677cd | -10.26793 | -49.72776 | 2026-07-28 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 979c86d1-59bd-36bd-92c2-325703375962 | -17.3128 | -42.67704 | 2026-07-28 04:53:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 873a07e9-88cd-347d-96f8-e06cbae9bc45 | -13.70115 | -51.90126 | 2026-07-28 04:53:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d33b79e-6df4-33f3-9402-6471b5018ac5 | -14.22906 | -58.98258 | 2026-07-28 04:53:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd8252c5-8199-3ba5-aaf2-e8c05e12966b | -20.6442 | -57.27785 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a153651d-753e-327c-bb44-e1afc3929787 | -12.84816 | -44.39206 | 2026-07-28 04:53:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2ca8ff2e-aefe-3be4-8cae-7e34c5bda25b | -8.64192 | -64.90842 | 2026-07-28 04:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7976c961-e4f4-3de3-bd4d-1f1f366a1bc0 | -10.38479 | -49.57734 | 2026-07-28 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 976c3f50-de24-3988-b95c-19ef823d0604 | -21.80854 | -53.08472 | 2026-07-28 04:53:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62b01de9-eccb-3eeb-859f-781186ec16b2 | -12.4575 | -50.5464 | 2026-07-28 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7617038-d59a-300f-9115-0a63004ddb76 | -17.31325 | -42.67274 | 2026-07-28 04:53:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 566c46a2-d427-3445-92bc-748e58223ba2 | -11.77975 | -47.081 | 2026-07-28 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 232aec1c-1666-340b-8786-371158fbb3ba | -20.29799 | -53.72617 | 2026-07-28 04:53:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 226ce45a-63b9-3095-b93d-d9c056c2ff96 | -10.75032 | -42.09331 | 2026-07-28 04:53:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 38df6edd-b2c0-3e6f-9a0b-ad7001303a37 | -21.88311 | -56.26389 | 2026-07-28 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ef2a5b6-ba60-3c76-abfe-a34023bece82 | -9.1092 | -56.85699 | 2026-07-28 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52ad5fbe-105b-3228-b11c-0af3ee3f231b | -15.40416 | -55.92207 | 2026-07-28 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1827de8e-2020-3d80-9241-4edbf72dc74f | -12.49327 | -43.77448 | 2026-07-28 04:53:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 00842da6-f3a0-3d7b-a5e9-b9819f800a66 | -11.9746 | -45.55077 | 2026-07-28 04:53:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a101bf8f-88a2-3589-ac64-6cf81ab00696 | -12.72958 | -52.06062 | 2026-07-28 04:53:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1872d37e-530f-3f99-b546-039241c02637 | -21.31401 | -52.83407 | 2026-07-28 04:53:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e10afa7-7fc7-3315-8927-04913cdaee40 | -10.93974 | -43.06314 | 2026-07-28 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f20d2c96-0b2d-3334-95ea-50e9b62c52bd | -16.86478 | -49.57833 | 2026-07-28 04:53:00 | NOAA-20 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4411726a-5611-3c0f-98f2-8c50937c1c01 | -14.22481 | -58.98188 | 2026-07-28 04:53:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90b45ac9-7227-38e0-873c-1992ed015a23 | -12.49367 | -43.77131 | 2026-07-28 04:53:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a0515f1b-a28b-3a5f-8fe7-cda75ecda5ce | -12.46379 | -50.55127 | 2026-07-28 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ecd20a88-0b77-373f-aa37-5634a23ef889 | -12.93604 | -56.63331 | 2026-07-28 04:53:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3d3fc8c-1626-370f-83d8-2027e60ca1c1 | -20.62672 | -57.27219 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2170218-2152-37f3-9c00-31b9b011bf98 | -19.72005 | -47.41228 | 2026-07-28 04:53:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f8a41f0-6dbf-3bad-bcf7-14e52a12b441 | -13.34831 | -54.28792 | 2026-07-28 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b79c4409-f859-335a-9a8c-eeb984c333b7 | -14.30529 | -58.97241 | 2026-07-28 04:53:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0f6689b8-bcdd-301a-a1d4-bade00eb2936 | -20.65543 | -57.27584 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7125c487-0dec-3fa5-bfd0-df46b04c564a | -12.6769 | -47.67457 | 2026-07-28 04:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3be78c4-ef8d-3b7b-b38a-20d3efb2fffb | -10.97224 | -49.44122 | 2026-07-28 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 091a023d-0018-3478-ab6c-d4d3068a7e92 | -20.61763 | -57.26186 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4be83e80-488f-3b49-8bf3-51931c0a61e7 | -15.40695 | -55.92696 | 2026-07-28 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3d94e5c7-8880-35fb-aec3-1d16b567e0e7 | -10.94453 | -43.05534 | 2026-07-28 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 300e8ba1-14d6-34e9-879b-a5d638d7b89e | -15.5599 | -56.09545 | 2026-07-28 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 189b828d-e9ea-3d8b-98fd-739f08b32023 | -13.35228 | -54.28482 | 2026-07-28 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f26d9048-ca02-319e-93ce-bca941b5e0a8 | -23.19192 | -49.77719 | 2026-07-28 04:53:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 39c0fdb0-f742-32c7-8a9d-4d0ed060bd36 | -14.41412 | -52.11776 | 2026-07-28 04:53:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5c5f7b24-64ab-3448-8296-923350dd2203 | -12.04043 | -47.80201 | 2026-07-28 04:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0adac985-71b3-3154-b7b4-f933895efa4c | -8.89021 | -65.02076 | 2026-07-28 04:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 70915e0b-6e4b-3909-a1e4-30625619fef6 | -20.62464 | -57.26324 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 723cf5ed-fe69-3b6e-83fe-09717089b9a0 | -15.76312 | -48.39105 | 2026-07-28 04:53:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca65b051-056a-31d8-96dd-20dc78b3660d | -11.97717 | -45.53178 | 2026-07-28 04:53:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 980a5a3c-b15b-31a3-bd9d-79830fd130e5 | -14.28396 | -58.99343 | 2026-07-28 04:53:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43a7d825-7b9e-3e73-81e5-0b3030c3d2b8 | -13.29864 | -45.09464 | 2026-07-28 04:53:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 6e3645bc-2bf9-3b96-877f-e0cdeeafc457 | -10.67567 | -49.66292 | 2026-07-28 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daa91d71-9d94-355b-9911-b292599131a6 | -12.32466 | -46.73565 | 2026-07-28 04:53:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e5a9981-a3e2-356d-b733-ee82c5326de6 | -21.2207 | -56.19371 | 2026-07-28 04:53:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4659daab-1d72-3ee8-8d14-3c62a5178af3 | -13.35565 | -54.28539 | 2026-07-28 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0969b30-1aa6-3cb8-8a9f-e2c16d41e0df | -15.44336 | -41.37057 | 2026-07-28 04:53:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6c3e409a-56da-3c58-bbd4-95060065217f | -17.3336 | -43.63394 | 2026-07-28 04:53:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 80a6ccae-d526-3336-9d24-603b9c9d4f8f | -10.83556 | -49.38848 | 2026-07-28 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 497cca68-f66f-34a7-9724-d5bf83a18b54 | -11.63936 | -60.44627 | 2026-07-28 04:53:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22d33fe5-33ae-3ad1-bb20-e52bbfab5d80 | -10.94495 | -43.05198 | 2026-07-28 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| bb9dc27b-91e3-3a0c-aea3-279d076b9657 | -10.94019 | -43.05978 | 2026-07-28 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 3bf35f6a-3a52-3e5b-832d-251afc81f173 | -20.62114 | -57.26255 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b49662b-871c-3006-8347-25e44f9f91ce | -10.9362 | -43.04904 | 2026-07-28 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| f5f092e5-a430-3889-a247-6711b9842eed | -20.64771 | -57.27852 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f3661460-0872-36ce-8a43-e7c9b81e790f | -9.10518 | -56.85629 | 2026-07-28 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffb64ca2-22c7-31fa-a7b6-8bb5f332920f | -9.11382 | -56.85415 | 2026-07-28 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3da8cae-2a1b-3a20-8faa-f8cafde0be9d | -20.65121 | -57.27921 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31c05c7b-dab6-35d5-9a33-62ee590657da | -12.45361 | -46.51411 | 2026-07-28 04:53:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a84af04-e595-3187-8abc-51ecc26da3f2 | -12.30437 | -50.35058 | 2026-07-28 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7df5898-36b2-3f70-97a2-7bc3542d97ea | -10.94369 | -43.06207 | 2026-07-28 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| be15b9cb-9867-3f06-a872-ed37696dbc3b | -10.55044 | -48.60839 | 2026-07-28 04:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21b5d471-599f-31fd-a547-ade65ca6a1fa | -15.40765 | -55.92278 | 2026-07-28 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 48c4d40c-3b29-3c81-a0a2-b6c4caae21db | -11.15328 | -54.12458 | 2026-07-28 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9545c30-239f-3fc9-a2d4-e770535fc106 | -9.60744 | -47.76541 | 2026-07-28 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e6c6113-d872-303d-936f-efd17aad75b1 | -12.46036 | -50.55074 | 2026-07-28 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 775e1ee8-00c9-3a32-9ac1-242cb2ec98ed | -12.45792 | -46.51463 | 2026-07-28 04:53:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae3aa262-60b4-3f8a-9776-4461fbf28dd7 | -11.97588 | -45.54128 | 2026-07-28 04:53:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2f767c9-b072-3137-a308-55606a35927d | -15.44389 | -41.36547 | 2026-07-28 04:53:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3631cb70-ac37-3ee9-bc36-46aa94a5a117 | -12.3084 | -50.34726 | 2026-07-28 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc961505-e6ef-38cb-863d-31369a5889de | -14.21523 | -58.98935 | 2026-07-28 04:53:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f726afaf-8ee0-3177-b892-e85f31d5203b | -14.29576 | -45.64017 | 2026-07-28 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bf3d8e8-4b61-3fdb-b5de-74dccd7ec852 | -10.38828 | -49.57788 | 2026-07-28 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c84b103-0384-3129-b051-e929373139a7 | -11.68518 | -50.21177 | 2026-07-28 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2c25b98b-beb8-3e1b-bc6f-673aa83a2a92 | -14.30044 | -45.64079 | 2026-07-28 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 935b91e5-0789-3a03-b3a6-9e5d6241bc1f | -20.59298 | -57.27861 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d931bcf-b3b2-3aa7-99f4-4908cf0cdbfc | -13.34891 | -54.28425 | 2026-07-28 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README19.md)
