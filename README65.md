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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3d2c73e-1f8e-3da6-aaa3-14bf4b4972d5 | -21.41465 | -47.79262 | 2024-09-28 04:23:00 | NOAA-21 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fb5d970-530f-329f-b9d8-2775bfe2b500 | -21.4142 | -47.77356 | 2024-09-28 04:23:00 | NOAA-21 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d368c65-7bf7-341c-b051-788a92c6ab83 | -21.41146 | -47.76928 | 2024-09-28 04:23:00 | NOAA-21 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9e039cd3-fe98-3111-8602-82c1a949f1be | -21.12629 | -47.02972 | 2024-09-28 04:23:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac542d95-178e-3fdc-ae76-6339c6770850 | -21.12355 | -47.03007 | 2024-09-28 04:23:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 869232f1-b9e2-3d01-90dd-6d5d56126539 | -22.22189 | -47.40293 | 2024-09-28 04:23:00 | NOAA-21 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e1f26632-220e-3c16-bd43-80f9f267973c | -22.59122 | -47.3879 | 2024-09-28 04:23:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f8b91da2-b66f-3d32-a99b-9d61b75c487a | -22.4603 | -48.45961 | 2024-09-28 04:23:00 | NOAA-21 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24a2b70b-e320-3b3e-b841-1d9fd5bbc47b | -22.45971 | -48.46333 | 2024-09-28 04:23:00 | NOAA-21 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24935134-69e6-37ca-b6f3-862971c819d7 | -22.45913 | -48.46705 | 2024-09-28 04:23:00 | NOAA-21 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b885b604-2342-38cc-b378-204125a486fb | -22.45641 | -48.46273 | 2024-09-28 04:23:00 | NOAA-21 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea53133c-1f53-3b32-880a-50fc845b95af | -22.45582 | -48.46645 | 2024-09-28 04:23:00 | NOAA-21 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c49ebc1f-f362-3257-9443-9e1e0e7b820f | -22.32977 | -48.59686 | 2024-09-28 04:23:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e5734abc-ad52-309f-b92c-366a3b119c57 | -16.67914 | -49.32276 | 2024-09-28 04:23:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dea2a75-fee6-3686-aeb9-5fe7cf166f75 | -17.14393 | -47.62826 | 2024-09-28 04:23:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a2f4adb-200a-3f30-89ae-cfb946c612e4 | -17.14336 | -47.63186 | 2024-09-28 04:23:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3cf3dd26-47b3-3c7c-a46d-02f3b85ef894 | -17.14063 | -47.62769 | 2024-09-28 04:23:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e7f85117-bb6f-3682-b3db-d2767c057aba | -17.14005 | -47.63129 | 2024-09-28 04:23:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 65c11b0a-ffe2-32ea-824b-fcc279bbfda6 | -17.13947 | -47.6349 | 2024-09-28 04:23:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b9118650-2259-3172-b136-f66c64518d45 | -17.92944 | -48.66275 | 2024-09-28 04:23:00 | NOAA-21 | MARZAGÃO | GOIÁS | Brasil | 5212907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1bceb7b-2234-3431-9250-71b5b046a7c6 | -17.92883 | -48.66645 | 2024-09-28 04:23:00 | NOAA-21 | MARZAGÃO | GOIÁS | Brasil | 5212907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36e31e08-805d-3f0b-a880-8cad8579fc9b | -17.92688 | -48.66577 | 2024-09-28 04:23:00 | NOAA-21 | MARZAGÃO | GOIÁS | Brasil | 5212907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7fdda7c-56bc-3b8c-83dd-70f29cf89b90 | -19.04508 | -47.91541 | 2024-09-28 04:23:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd0ca5c3-0820-3315-89bb-825303c38aac | -18.16574 | -47.98637 | 2024-09-28 04:23:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 010568ae-136b-3f70-8591-86d57d4624f4 | -20.29943 | -49.19325 | 2024-09-28 04:23:00 | NOAA-21 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86ca7faf-9bb6-3613-937b-a34c3e98bf2f | -20.87067 | -49.57039 | 2024-09-28 04:23:00 | NOAA-21 | JACI | SÃO PAULO | Brasil | 3524501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 42d0f791-ccab-33f5-8708-116ebc6614ab | -22.17385 | -49.06222 | 2024-09-28 04:23:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a69d781d-77f1-3da3-8d5b-7581ecdf62ca | -22.35814 | -49.31234 | 2024-09-28 04:23:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a502acd0-c2cc-3776-86df-3f52b0c6567a | -22.35753 | -49.3161 | 2024-09-28 04:23:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6ac62e3d-39e8-3d49-83a7-994f94970c6a | -22.35692 | -49.31987 | 2024-09-28 04:23:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a515e506-cfc9-32a9-bd46-460ff570c6e2 | -22.35543 | -49.30795 | 2024-09-28 04:23:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 05b0c737-9817-3b19-9415-dddd3d291810 | -22.35359 | -49.31927 | 2024-09-28 04:23:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7957d2cd-6950-3ffe-bc3b-4da90aadba53 | -22.35238 | -49.32677 | 2024-09-28 04:23:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e0ee6fc5-e62d-3ac7-9a40-cfbee5fce5ac | -22.35088 | -49.31488 | 2024-09-28 04:23:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| dfe9dc89-b9b9-3960-9d1d-d59c5a255136 | -22.35027 | -49.31865 | 2024-09-28 04:23:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e7a6af2b-2d45-30a2-b9fa-33133281d0bf | -22.34966 | -49.32241 | 2024-09-28 04:23:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| d5bf824c-c395-31fe-9867-1641070e3be8 | -22.34905 | -49.32617 | 2024-09-28 04:23:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| e05e5608-c6f4-3020-9c02-dc8e79941768 | -22.34756 | -49.31426 | 2024-09-28 04:23:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 327eafcf-da79-36b3-a589-add416adac47 | -21.63432 | -49.84146 | 2024-09-28 04:23:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d7b7b6ce-3d64-3e51-a18e-3bffb0477d66 | -21.50765 | -49.84232 | 2024-09-28 04:23:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 60106f49-baa6-3b24-a54b-3fe614ff2ea7 | -21.50428 | -49.84167 | 2024-09-28 04:23:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0afdea31-eb30-3333-846a-2d6851386d3e | -21.26485 | -49.45831 | 2024-09-28 04:23:00 | NOAA-21 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9a715361-befc-3ca3-8c10-bc6b2f58b8d9 | -21.09601 | -49.1361 | 2024-09-28 04:23:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c96211a2-8e33-3f9e-9387-d12c4f15cd17 | -21.09268 | -49.13547 | 2024-09-28 04:23:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 98d3fdc5-6e67-3b8d-90e2-481d61962e0b | -21.09207 | -49.13923 | 2024-09-28 04:23:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 345365ed-24ab-3abd-80f6-828f4ee30922 | -21.09146 | -49.143 | 2024-09-28 04:23:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 905e5b4d-0e2a-309e-af78-b8dfa3533eb5 | -21.08874 | -49.1386 | 2024-09-28 04:23:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 121425a9-7d76-3320-a42a-77c0993ad8bc | -20.87992 | -49.55645 | 2024-09-28 04:23:00 | NOAA-21 | JACI | SÃO PAULO | Brasil | 3524501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 13dc98b1-78f8-3e4e-9da4-6868df6fb3e1 | -21.92298 | -48.5655 | 2024-09-28 04:23:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da00e069-0c76-3b91-8f48-db62b29a36d2 | -21.0443 | -48.46235 | 2024-09-28 04:23:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 90e6076c-006a-34c1-9b85-ae9c2fdf7fd5 | -21.04099 | -48.46175 | 2024-09-28 04:23:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0f086c4b-3441-30dc-b74b-78946179ce30 | -22.60075 | -49.2024 | 2024-09-28 04:23:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bc2501f-5bf9-3e80-930f-044b4aa2eed7 | -22.59804 | -49.19804 | 2024-09-28 04:23:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56e521d2-1772-377f-b1fb-78ab108925a4 | -22.59743 | -49.20179 | 2024-09-28 04:23:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2851daed-3453-35cd-bdb7-c264890da00d | -22.54032 | -48.81414 | 2024-09-28 04:23:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb08f54e-74ad-3493-9772-12a4e2d2a745 | -17.00941 | -49.77954 | 2024-09-28 04:23:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 131f4ca8-f658-3ee0-bfa9-067982b6ca7e | -20.64391 | -49.93542 | 2024-09-28 04:23:00 | NOAA-21 | SEBASTIANÓPOLIS DO SUL | SÃO PAULO | Brasil | 3551306 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70950bab-895a-3b91-a171-40ded231a6de | -16.66793 | -50.59776 | 2024-09-28 04:23:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ed1864d3-f18d-34f1-a54e-c75a5027e5e6 | -19.77373 | -51.47417 | 2024-09-28 04:23:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 315a95c4-b65c-3153-b030-508a1301c7b1 | -20.998 | -51.79325 | 2024-09-28 04:23:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f181eeae-dd3a-3c17-8389-e8943c863601 | -20.99794 | -51.79111 | 2024-09-28 04:23:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a89376c2-94a8-3fc2-85f1-b98446bbeca1 | -17.86472 | -53.65817 | 2024-09-28 04:23:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63dcda30-d359-378d-bb9e-0cc0e42252fd | -20.80622 | -53.1053 | 2024-09-28 04:23:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f15e218c-d802-364d-b1d4-e3bcdf2a2117 | -19.61647 | -53.52561 | 2024-09-28 04:23:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2990a55-04bf-35da-b431-e304edcf83b5 | -15.68177 | -53.91395 | 2024-09-28 04:23:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0dd6eb0a-7f0e-3aa5-b293-2a213ca9bdde | -15.68088 | -53.91854 | 2024-09-28 04:23:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c104fbc-7635-3984-a007-5d790fd66d44 | -15.68079 | -53.91479 | 2024-09-28 04:23:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76a91953-7a33-3bb2-ae3d-67a8f8e38765 | -15.67993 | -53.9194 | 2024-09-28 04:23:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11c53a30-cdad-3fcd-aaa0-b735360c0e26 | -15.67816 | -53.90837 | 2024-09-28 04:23:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7f8a33c-b18f-3a15-99b7-c859dce3a067 | -15.67725 | -53.91304 | 2024-09-28 04:23:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 643651eb-0e29-31ad-bef1-29de3127d317 | -15.67714 | -53.90922 | 2024-09-28 04:23:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| edf62ca6-25ec-320c-9cba-b868214ceb40 | -15.67635 | -53.91764 | 2024-09-28 04:23:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d27e121-5b9d-3c60-8257-b035c98c5276 | -15.6754 | -53.9185 | 2024-09-28 04:23:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98e944e0-e9fe-356b-a145-a7adf05ad460 | -18.83818 | -54.5046 | 2024-09-28 04:23:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6a6f940-66a1-3a47-8894-45d81b9014ca | -18.83626 | -54.49969 | 2024-09-28 04:23:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae6e7a79-81f0-33ef-b701-3e8fd539c4c5 | -18.8353 | -54.5047 | 2024-09-28 04:23:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6daa229-b6c7-38d6-acb5-e7356a69d98a | -18.83436 | -54.5096 | 2024-09-28 04:23:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32dc3ede-fe6f-3119-a244-c40a6780c5aa | -18.82993 | -54.50858 | 2024-09-28 04:23:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47fab63a-0427-316d-be3a-c1d0e6f0f480 | -16.59132 | -55.97228 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b03ff127-94b9-31e6-a7bf-b8a43523d646 | -16.59069 | -55.97543 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 452e2f03-5e55-334d-9c83-bc96661ddf18 | -16.58957 | -55.96814 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f13fda3d-16a9-3b80-834a-39734fdcd287 | -16.58892 | -55.97127 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9f9731a9-1d9a-358a-92b1-45a142f1bd41 | -16.58747 | -55.96492 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fc73bfec-c5d3-34ca-ab62-b08d59c99771 | -16.58685 | -55.96806 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ab7d656b-79a6-3102-b866-0f7b27810d62 | -16.58512 | -55.96395 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 23eed756-88a9-3261-812c-df21efcac39f | -16.58448 | -55.96707 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 34bf052b-e0d8-377c-843b-7438cee23cf6 | -16.54046 | -56.04049 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| df0d8890-0d06-3f15-8ea7-bc53ba45f699 | -16.53983 | -56.04366 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0c4e2723-5786-3d22-9995-777d38a68990 | -16.13337 | -55.42803 | 2024-09-28 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30ba1524-204b-3115-9945-8b38289f48ee | -16.13276 | -55.43115 | 2024-09-28 04:23:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dd6b311-6305-3b95-a405-1de84c512caf | -17.11888 | -56.20092 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 093ac117-614a-3f03-829d-9150ea1c4b2e | -17.11822 | -56.20409 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| d720ec54-9fb1-3079-a8d5-4b301961cae2 | -17.11757 | -56.20726 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 6c781033-e2cf-3c59-a4f3-54e9ae097e19 | -17.11692 | -56.21043 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 45422325-0eed-3a30-842b-e1ef616d9e5b | -17.11442 | -56.19662 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 06c6b600-421d-3759-8188-a4f5387913d3 | -17.11377 | -56.1998 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b62690cd-ed6b-331d-86f1-d7e3d6406342 | -17.11311 | -56.20298 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| bdd32b54-16a3-394b-8bf9-08c6a49913b1 | -17.11246 | -56.20615 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 86b93ced-e952-30a5-95a6-50361316faf6 | -17.11181 | -56.20932 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 8698681f-6266-3b51-9354-e2285fd8953b | -17.11115 | -56.21251 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |


[Clique aqui para ver as próximas entradas](README66.md)
