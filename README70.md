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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ad20ffa-8ffb-31f1-a84e-d90a9600da57 | -16.04183 | -54.39109 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fbe02603-e263-31a2-b2d3-56927ee13cd1 | -10.50579 | -59.61924 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8046f88-e7db-3cd8-908b-9c2aa70a7b6a | -15.5992 | -56.41419 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d1a4be0-9606-3b5e-ab8e-7c37e6354e15 | -15.63555 | -56.38152 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8fd5f9f-255d-3ace-ad95-8221e88b54e8 | -14.72737 | -53.57957 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e370a588-4441-3dd2-a516-37106fb1c0ec | -15.85246 | -47.69577 | 2026-09-01 05:18:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4848936d-5bf1-33f9-83de-93e263c45fb2 | -10.75582 | -54.00516 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65b5e39c-21b2-383b-b33c-04acac590a00 | -8.87646 | -66.89037 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5068aa13-e5d1-3956-a089-c5bcf528da23 | -14.46293 | -52.51564 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57695da2-3862-38de-9b81-6b85e5b5a0fb | -11.26393 | -50.56871 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0d01487b-9275-3a0b-a30e-cef9908ddf21 | -12.09389 | -45.03683 | 2026-09-01 05:18:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0e531d4-6ada-3ef4-9114-0f69726a6321 | -16.13845 | -52.3777 | 2026-09-01 05:18:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c4d14edd-7e72-30b2-8aad-7dfb5508d322 | -14.26565 | -52.86679 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 568a0e0f-fd6d-324f-a327-57713af9c094 | -10.41985 | -57.23142 | 2026-09-01 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46595bfd-6310-371b-b96b-1f51c6def929 | -14.50963 | -52.23914 | 2026-09-01 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8acbf5d0-b29f-3a0d-b18e-d8ae65d0bd4e | -11.91177 | -45.06855 | 2026-09-01 05:18:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c1579c4-5b7b-376d-b790-05cee400dc46 | -13.4735 | -57.02924 | 2026-09-01 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bba7af19-163c-3082-8315-e9fdffe3ac0e | -13.45717 | -51.87469 | 2026-09-01 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d23ab51-08a7-3742-81a0-b3803a683f5a | -14.66184 | -53.54467 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7e05a2f-d2fc-3420-addb-16d5d206f7a4 | -14.37804 | -52.52953 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0370077e-c366-3aaf-abe9-54f764374735 | -11.24561 | -54.01198 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| baf5d0b3-4a14-3b9b-a0e0-e75e3f75e331 | -15.22157 | -56.35134 | 2026-09-01 05:18:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49668f24-87fb-346f-b4f5-39850cdf066e | -15.86909 | -56.49458 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf6bfb4c-ba86-3211-b707-ec0691fa6a1e | -10.75027 | -54.06689 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7deaff72-216f-3980-ac19-5f9fd021fb85 | -10.10459 | -68.40466 | 2026-09-01 05:18:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad6f7ef8-47fb-3732-9be9-789278d6294d | -11.24623 | -54.00785 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a8078b3-cf66-3fc7-b027-3ecb9b7cc806 | -10.13385 | -68.58683 | 2026-09-01 05:18:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd6fad31-84f0-33fd-9623-1cbc8a374c3f | -11.30306 | -50.56873 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 720137f2-5f58-38d0-a3e8-1381092a5351 | -15.60042 | -46.57706 | 2026-09-01 05:18:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 282bc295-3094-3936-857a-de430c0ef5ec | -9.46115 | -67.4589 | 2026-09-01 05:18:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3806aaa3-a4d7-39c1-8a1b-9d5e2fc83f34 | -14.26532 | -52.89847 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad7841de-8168-3963-ac3b-9cba696d419d | -15.06194 | -47.99403 | 2026-09-01 05:18:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 372d2424-78de-3102-8f3d-cb9db224cc77 | -15.63896 | -56.38207 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 357f51e1-2a13-311f-9a5a-75a16a10c96b | -11.24384 | -50.58367 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55f7050e-1cfe-3113-8458-4babb129b652 | -12.95567 | -45.965 | 2026-09-01 05:18:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d751c4e6-61f7-39e9-bc5b-af9cd3827999 | -15.63337 | -50.1041 | 2026-09-01 05:18:00 | NPP-375D | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd2a41b0-580c-3289-9b26-cb2a5b2665e9 | -16.14267 | -52.37826 | 2026-09-01 05:18:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 61644f93-7504-3bcc-a825-b5e5b7f0f597 | -11.68406 | -47.15139 | 2026-09-01 05:18:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b27ff92-58c9-3212-8b0c-972930a0fe18 | -15.23461 | -56.35731 | 2026-09-01 05:18:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e675f77a-f12f-31a5-aed8-8cb2e6efcc68 | -12.78453 | -46.46428 | 2026-09-01 05:18:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7fea1efe-92db-383d-8650-366c9140fc72 | -14.40736 | -52.49667 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8df06f4b-a041-329e-92f5-f67269024063 | -10.41652 | -57.23087 | 2026-09-01 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04e507ae-6d4d-3e3a-a25e-64f9cd93bae1 | -8.77201 | -69.34307 | 2026-09-01 05:18:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a1aece5-f1e9-3c71-9fb7-d00b825e51d1 | -15.76879 | -56.09788 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 24abe6e7-e996-3ca0-9180-6fd8fc445854 | -8.87566 | -66.89455 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6e0873ec-9a84-312c-bc70-51bfbd92ff16 | -15.63953 | -56.37831 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f99f4251-6bc1-3962-9ae7-e6210cc7aebc | -16.37448 | -54.52032 | 2026-09-01 05:18:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e9abab7-ba19-3dd9-b378-95686b59e671 | -15.62982 | -56.41911 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f5b9070-5c6a-30ad-b364-3c1b0e931b99 | -15.75392 | -56.10316 | 2026-09-01 05:18:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 850d0221-68c9-3e8b-9b7e-a34af2dd2c10 | -15.01808 | -52.77127 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0eb09c05-5ce7-361a-a764-757a6bf4d0e5 | -11.10787 | -51.5379 | 2026-09-01 05:18:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 50dc2824-8faf-355c-a4c6-038bcc7ed54f | -13.27393 | -48.55092 | 2026-09-01 05:18:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4bf13aa4-34cb-373c-89fb-85298bba80cd | -14.43489 | -52.50804 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a52b6984-9679-3665-b502-3c2f1f58df7a | -10.06094 | -59.4031 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 068ef65d-f8f5-3834-9741-a03048e2ecf9 | -16.48157 | -47.95142 | 2026-09-01 05:18:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 95a9bb88-1575-3d98-895d-0c124179cc15 | -15.0312 | -52.76562 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57214547-b8a7-378b-b6c8-85b9bf26b182 | -15.67288 | -45.92035 | 2026-09-01 05:18:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 458d3962-1e03-335b-84c8-dd39cc71d4ef | -14.13212 | -52.79319 | 2026-09-01 05:18:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 277c57fd-0691-340a-8a4f-aeb2bf9b12a2 | -16.04853 | -54.38107 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 15366c8a-4e05-3198-8168-6da0b90a5847 | -13.47294 | -57.0328 | 2026-09-01 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59112aa1-ddd5-3b5c-a5f6-139696e5864b | -15.24273 | -53.8476 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acb52335-e875-3e56-92fb-d1606fc98675 | -14.58419 | -54.07765 | 2026-09-01 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e6a9843-92ef-3a03-81e3-5b999237c7d4 | -14.26097 | -52.87136 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ce48dd9-07ad-3711-bd06-d645e0ee602b | -15.84146 | -47.69033 | 2026-09-01 05:18:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 891a9f57-ce20-3df0-84b5-f1cf95edfafd | -14.47058 | -52.52036 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 66c6bf27-5233-330a-be73-caaf70d3c658 | -9.00542 | -67.80275 | 2026-09-01 05:18:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aff0a966-71d9-3f12-b158-04d55b6286b6 | -14.40586 | -52.50776 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bb4c6c3c-51a7-3ba9-b14a-58a3c5dfdcac | -10.51265 | -57.43105 | 2026-09-01 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aa16925-fc89-3842-9603-aedb1d6fd557 | -14.39525 | -52.52493 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6de60a9-3550-3f4d-847d-62e36bdd3267 | -14.26168 | -52.86618 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01c6f035-5d09-3c13-bde8-491f38f1b00b | -15.63838 | -56.38583 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce28f091-3fde-30e4-9b7c-96a5044fa054 | -8.60304 | -70.22162 | 2026-09-01 05:18:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91ff0601-cad1-31d1-9db5-ea1b1caf74fc | -14.1314 | -52.79846 | 2026-09-01 05:18:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5132f9e8-d339-3a8c-9290-b73b3e545705 | -14.45883 | -52.51522 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 882f96d6-f4ee-3871-9091-2698b95ec99c | -15.4013 | -52.71463 | 2026-09-01 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f125b438-32e8-310b-ba8e-8f56c0fc3452 | -14.39118 | -52.5243 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1be2202d-bbeb-38f6-ab14-cac04cc9122c | -8.59086 | -66.97738 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7eb49c64-b023-3379-8b5d-dd51ef1b79e3 | -10.44198 | -67.84468 | 2026-09-01 05:18:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c187c57-c19c-3041-b51a-7be2830e989a | -8.58504 | -66.97619 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 267b2aa0-5014-3e29-921c-7c3a58b5b185 | -15.24944 | -53.85056 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c50192ba-3333-3510-9059-a048c91d1a0b | -15.18493 | -46.24698 | 2026-09-01 05:18:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b48befea-415c-329e-b033-db012ae37252 | -14.39476 | -52.52857 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fc0e535-395d-3dcc-996b-5545f3d7207e | -16.37015 | -54.5242 | 2026-09-01 05:18:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b7e0f49-c125-354f-933b-b2cef9456c58 | -13.84052 | -54.08909 | 2026-09-01 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60311f14-88f3-3f74-b122-38233ed080ec | -16.5403 | -49.57056 | 2026-09-01 05:18:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e732f5aa-c127-34aa-9680-e59303314f91 | -8.86989 | -66.89342 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4e94e7b2-e6cc-30d4-b0e2-1f3562236f59 | -8.88222 | -66.8915 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e1a7ba1-a749-3eef-898f-b1a32a7e63df | -15.39608 | -53.76181 | 2026-09-01 05:18:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0957878a-609b-31b0-95c0-2dd8323f71f2 | -11.49669 | -60.58862 | 2026-09-01 05:18:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d4ee5aa-1fab-3dc2-a0c9-086d4f7915d2 | -14.00557 | -54.08495 | 2026-09-01 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d21767f-12de-3f62-a12e-aa4242d56e69 | -11.06478 | -51.5281 | 2026-09-01 05:18:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00a98205-b3d3-380f-865b-ad35c72497e3 | -9.32719 | -68.89202 | 2026-09-01 05:18:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20ac6eb5-9038-3ea1-a323-7c534c0434c4 | -13.33141 | -51.72543 | 2026-09-01 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56d0956d-ff31-3a2f-b124-f157d6f0a909 | -13.48234 | -57.05992 | 2026-09-01 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8d03e63-8ca1-3630-a563-453bb00ac7c9 | -11.06838 | -51.53244 | 2026-09-01 05:18:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 545f60b0-e945-371b-b2a5-c274f6853463 | -15.55373 | -56.27547 | 2026-09-01 05:18:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d685aad5-5bcd-37df-b273-36e11bf03d66 | -11.25388 | -50.5762 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e2c78b7f-e95a-3e6c-a8e3-d850826cbef0 | -13.32868 | -51.77759 | 2026-09-01 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95126ef0-9101-36d5-8264-9d694fae4a60 | -8.86245 | -66.77235 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fed74f71-9412-324d-9e49-1abf3713fc17 | -9.80181 | -59.43485 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README71.md)
