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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96ab2218-d2dd-373a-beae-a7ae137549be | -12.70151 | -43.98479 | 2026-07-25 03:47:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b72e4b4-81e2-3990-af69-e3868b925dc5 | -8.73542 | -44.33636 | 2026-07-25 03:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdee7113-e5fc-388a-a4bc-08392911abc3 | -13.61166 | -44.36175 | 2026-07-25 03:49:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5421ead0-f073-3a0d-bda4-3841dae3f980 | -8.38238 | -48.21479 | 2026-07-25 03:49:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76c5f5ec-0928-3c52-9252-33bb06915c45 | -15.57503 | -46.81392 | 2026-07-25 03:49:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc840724-ea36-3d8a-91c3-fdff9c907988 | -12.66621 | -48.20795 | 2026-07-25 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee8795db-4a64-3204-83cc-3bf4fdf20a7b | -15.57411 | -46.81832 | 2026-07-25 03:49:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bafaf3d-fc25-3c19-a186-4c2251247c05 | -17.55469 | -46.5456 | 2026-07-25 03:49:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3bc69d28-dd00-310e-8b77-6aaf94425899 | -8.7347 | -44.34022 | 2026-07-25 03:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ff6c079-b65b-3af8-b66a-fcffb08a7ae7 | -14.06083 | -43.81907 | 2026-07-25 03:49:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5554f900-3274-3660-a81e-7d5917c3ec82 | -13.61316 | -44.35974 | 2026-07-25 03:49:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aebe0095-2110-34cf-aded-4504825e214e | -15.58669 | -46.8162 | 2026-07-25 03:49:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c793b44e-830d-3d25-bb6b-a14af527319d | -8.38099 | -48.22201 | 2026-07-25 03:49:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fab87446-141e-3bd7-98d4-9a3f9eacbb50 | -17.87739 | -40.01696 | 2026-07-25 03:49:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cf6917c1-29f1-352c-ab21-cb354fbac5dc | -13.61226 | -44.3586 | 2026-07-25 03:49:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02124675-362e-363c-b1d7-eb2076774c0b | -8.74107 | -44.3372 | 2026-07-25 03:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd7ffbe0-fb1c-3ca8-9698-cca3fa55c713 | -17.68004 | -40.2823 | 2026-07-25 03:49:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a107f474-e6c0-30bd-b9a4-25f32314e993 | -15.7684 | -42.16694 | 2026-07-25 03:49:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 26f083b5-ad9e-3efc-9257-73536dccb545 | -15.58086 | -46.81507 | 2026-07-25 03:49:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 930f1aef-71de-3563-97ff-d7947eeecad9 | -15.57993 | -46.81953 | 2026-07-25 03:49:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0277db30-028b-3e0f-b20e-b3b5c61473dd | -18.83871 | -46.59839 | 2026-07-25 03:49:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 567a48fd-8ccd-3731-8e34-37abaafaaa5f | -13.48207 | -44.03669 | 2026-07-25 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d7ba6ace-cc9c-39c8-bec7-18dadb6aacb6 | -13.77798 | -47.13228 | 2026-07-25 03:49:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ac9c296-dbff-33ad-8bf8-6b972e556b88 | -12.66754 | -48.20164 | 2026-07-25 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a4711eb-3174-346c-b11d-04f937f8ebe4 | -13.47701 | -44.03569 | 2026-07-25 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 73cc36a1-1291-3068-a03d-12ecde3522f1 | -9.43657 | -40.36565 | 2026-07-25 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 52cb8fec-bdd1-3370-8d07-aef690f82b9c | -11.807 | -47.0858 | 2026-07-25 03:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 1dbc2331-9d5a-38ac-a213-0d58b5be7008 | -4.08624 | -39.26143 | 2026-07-25 04:04:00 | NOAA-20 | PARAMOTI | CEARÁ | Brasil | 2310407 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2084f1a2-e4cd-38cb-aa8d-a0d487cf2730 | -2.47986 | -47.08643 | 2026-07-25 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b55d4dfd-c163-317d-8b5d-ce1609fb298e | -2.48177 | -47.08804 | 2026-07-25 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b58d7405-553b-3ad0-be7d-1f3d8b34f7f6 | -8.38355 | -48.21392 | 2026-07-25 04:06:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1199891-8df5-3647-8d39-656cc2521989 | -7.89487 | -48.27246 | 2026-07-25 04:06:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6626ea4b-4d40-3274-b39a-25968c7c5440 | -4.434 | -40.92339 | 2026-07-25 04:06:00 | NOAA-20 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c840542c-7ecb-3d97-9ebc-4ba238ee8686 | -4.05878 | -43.24551 | 2026-07-25 04:06:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d6e4834-7325-34dd-aa1f-03c3adffc148 | -3.80109 | -51.18618 | 2026-07-25 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 92e5c4ed-37c5-308a-9c17-c4fc0e847e43 | -8.8337 | -47.07931 | 2026-07-25 04:06:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b02870f9-202b-368a-8a03-e83f9a9e3677 | -8.77624 | -46.58257 | 2026-07-25 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c9d39acd-833b-3a4e-aaa6-704177f39a7b | -8.73498 | -44.33777 | 2026-07-25 04:06:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0c21e85-5170-3d84-8914-d6f2664d3e72 | -4.37155 | -47.76912 | 2026-07-25 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a45558a5-5773-349a-ad0c-0f62cbfae23c | -8.28334 | -49.60833 | 2026-07-25 04:06:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3dc995f4-5855-3c8e-a9a6-240fba3356c4 | -3.7939 | -51.19042 | 2026-07-25 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41dc1d18-37cf-31bb-a91e-3e8e0adef8ad | -7.89607 | -48.27681 | 2026-07-25 04:06:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19210b45-53bc-3b15-a585-369c001e7267 | -4.18017 | -48.58488 | 2026-07-25 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30dbbd3f-2fef-34e2-b5be-885e47fbee5a | -9.43571 | -40.36786 | 2026-07-25 04:06:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d316b978-de1a-30d7-ab01-f806f8195a21 | -8.83294 | -47.08368 | 2026-07-25 04:06:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b2004be-3639-34bb-ad17-45cca3558c87 | -3.80018 | -51.19147 | 2026-07-25 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 042593fc-4b9c-3a4d-8439-4b7edffbbbca | -7.89216 | -48.2705 | 2026-07-25 04:06:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9bc3da66-9d6f-3293-b4c9-1d477986535e | -3.72546 | -49.27207 | 2026-07-25 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfe921ce-2d12-32e1-8639-0e320a072247 | -8.37874 | -48.21318 | 2026-07-25 04:06:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8105dbd-2540-367d-af69-3d5b884b6feb | -4.36755 | -47.76252 | 2026-07-25 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 94c6b41f-5165-3407-8a24-3f9abbb93051 | -8.3826 | -48.21926 | 2026-07-25 04:06:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a7ce0bc-5087-389e-96f8-8b21c97bfdd7 | -8.73429 | -44.31925 | 2026-07-25 04:06:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5467c3ad-7759-3078-b5af-97d9656cd44c | -4.36657 | -47.76831 | 2026-07-25 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 630399d3-60fe-3470-a3c4-b9f8d2c82924 | -6.43128 | -46.20752 | 2026-07-25 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9203069-be58-3bd0-893a-50a7cf0b9da4 | -7.87843 | -46.90752 | 2026-07-25 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 578edf9c-f55d-30ce-b3a3-0c6633f631a7 | -3.7948 | -51.18514 | 2026-07-25 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0ea3e06-a022-3285-9fdc-e03fd90b8ef6 | -5.0874 | -47.945 | 2026-07-25 04:06:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a07c5112-b77a-3a93-8ef7-4ea8b9792041 | -4.18399 | -48.58881 | 2026-07-25 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 647f5146-ef40-381b-9cec-70f4c1b5b1c7 | -4.1807 | -48.58172 | 2026-07-25 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b3591a0-d6c2-393e-9ece-190efb4431df | -8.73945 | -44.33387 | 2026-07-25 04:06:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d451442c-3dfc-3c0b-acc9-408b6f1b2976 | -3.79814 | -41.61382 | 2026-07-25 04:06:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 66497266-f83d-39c8-a5f1-00db1ea39bc8 | -4.17926 | -48.58482 | 2026-07-25 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c36ac498-84fe-3b0b-b5f4-da18889711bb | -3.73101 | -49.27313 | 2026-07-25 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c110d0e6-5d68-31f5-b8b4-f3207c88f67b | -3.99658 | -43.27628 | 2026-07-25 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00278d22-2610-389c-87f5-adcbacf36139 | -4.17981 | -48.58165 | 2026-07-25 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76498bd3-1baf-3f24-8fa8-454066d1f366 | -4.06249 | -43.24614 | 2026-07-25 04:06:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0817c31a-7772-30ad-8845-72ce4a7d72c3 | -3.99585 | -43.28072 | 2026-07-25 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f448463-0b0a-3426-bb22-c214c262834e | -3.99512 | -43.28516 | 2026-07-25 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e9eccfe-7605-322c-84e4-52fe64b90f45 | -9.43626 | -40.36437 | 2026-07-25 04:06:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 881930e1-23cc-30b6-9e20-39d42bcf78a0 | -7.89702 | -48.27135 | 2026-07-25 04:06:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0bf33012-b53d-3960-8b8d-54d4192e81ac | -3.96444 | -43.11033 | 2026-07-25 04:06:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cac925cf-409d-3c90-8fde-1b99f7af47e3 | -17.67818 | -40.27869 | 2026-07-25 04:08:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 63129b2d-c8f4-39b8-888c-086128f50492 | -10.63891 | -45.22521 | 2026-07-25 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52b600f1-f8d3-32a0-b325-422bb7d59e13 | -12.01888 | -50.48872 | 2026-07-25 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe3bb019-80e6-3756-9d1a-01a8104f10f4 | -13.77612 | -47.13242 | 2026-07-25 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec144599-f496-3aa5-b939-4983af0774e2 | -11.79888 | -47.08694 | 2026-07-25 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 24e4bbde-94af-3545-ab6b-99a8c1c6e156 | -10.6812 | -46.34992 | 2026-07-25 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7686bd12-b1a2-3323-b542-c7b4f078a7d6 | -12.01366 | -50.48765 | 2026-07-25 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18331b8f-8614-346f-8b75-a469ac9379f6 | -10.68055 | -46.35363 | 2026-07-25 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 53fe88d5-8436-3140-a691-92efcbdabb2d | -11.60098 | -50.15301 | 2026-07-25 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eaf9399c-b2e1-3cfe-bff6-7a6503f2fea7 | -14.72973 | -47.14264 | 2026-07-25 04:08:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 80e0cb22-ba49-3b5b-8898-fdb0fa24be61 | -12.84603 | -44.39347 | 2026-07-25 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1acb3d14-2eba-3105-b1dd-64606e7a0ddb | -10.26544 | -46.73832 | 2026-07-25 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a4c84b91-29e6-337c-9a80-4b59a4dc09d4 | -11.77939 | -47.0994 | 2026-07-25 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6b9e339-5f82-355a-a3fc-956412e25ea1 | -10.68463 | -46.35432 | 2026-07-25 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 84da60ba-c86a-365b-b395-f705092e16ae | -16.77409 | -42.78932 | 2026-07-25 04:08:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2386cbce-a0e7-342b-8cb5-04637c0c28fb | -10.27033 | -46.73519 | 2026-07-25 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 410915bc-2fa8-3938-93f9-906d28eee7ec | -13.61018 | -44.35995 | 2026-07-25 04:08:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d401b713-c6a0-32cc-b489-1b37d14f1aab | -11.00244 | -47.4782 | 2026-07-25 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38d8542d-6264-3f56-b6b8-99d7b566382c | -14.17646 | -51.90836 | 2026-07-25 04:08:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74980d2d-2369-3914-be39-8cc9d82aa865 | -10.67713 | -46.34924 | 2026-07-25 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77101001-b3e6-3f9e-be8a-712ac3100b86 | -13.79176 | -47.13884 | 2026-07-25 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d9d911d-b57a-3bda-bc97-d19eb8e8f126 | -11.79412 | -47.092 | 2026-07-25 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 38a20af6-c462-355f-b377-7d32c013de7a | -11.80319 | -47.08973 | 2026-07-25 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bbbb499a-9b32-3230-b3ea-601027c4026e | -15.61722 | -48.27266 | 2026-07-25 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c516c034-6ffd-33a9-81e4-a919956d17fd | -15.58083 | -46.81456 | 2026-07-25 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5f54c7b7-12fc-3b61-bcf8-3d1029b3adeb | -13.78024 | -47.13284 | 2026-07-25 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78d9cb42-eeba-399e-9806-2a5fa8fe46ca | -11.79901 | -47.08892 | 2026-07-25 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| cdf7d723-9332-3c33-880d-b35e2e527953 | -14.05979 | -43.81854 | 2026-07-25 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c114b6a8-9f6b-3daa-a3d6-9af93ef11bbd | -17.87908 | -40.01589 | 2026-07-25 04:08:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |


[Clique aqui para ver as próximas entradas](README4.md)
