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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1175c2f9-b13d-31e6-9b38-fbdeda7d06a7 | -14.59775 | -48.10119 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 782a95eb-ef31-35b7-ac07-114841da53c0 | -11.85589 | -47.67044 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 725bd475-8eb7-341d-8608-e134a5c2c563 | -12.29072 | -47.1255 | 2026-09-20 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f73bb14a-1a03-3e24-a074-7ff668246112 | -13.89054 | -48.59156 | 2026-09-20 04:21:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a090b607-bc0d-3116-8c07-950a606ecd8d | -15.46922 | -48.42007 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 40a7a5e7-497c-3c48-ba25-03122a2e7e9f | -13.8873 | -48.58619 | 2026-09-20 04:21:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a2fed14a-5e11-3293-84fa-8cef736076a0 | -11.86367 | -47.65003 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65de5912-4e9c-33c1-9216-8ae7884d5b43 | -11.2122 | -54.0755 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6793689c-4129-3df1-ad4d-bba1dec9ae4f | -14.11078 | -44.83607 | 2026-09-20 04:21:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbecf7e4-60f3-34bb-934e-f0f0ace95603 | -11.37996 | -51.38612 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d6c5e0d-7b97-3e1f-93f7-7d3a0e0a7109 | -18.68314 | -47.05573 | 2026-09-20 04:21:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f375069-64c5-3a25-ad56-9521e55e393b | -12.74723 | -46.18245 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3f54b688-b273-37a5-8c4c-f65579533f3c | -11.10203 | -54.02517 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| fcdc3ce5-9f68-3ee3-9b0b-424db20d25d5 | -14.59392 | -48.10003 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a221859e-92b0-36de-b5dd-9a41b5ac2796 | -13.89203 | -48.58339 | 2026-09-20 04:21:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 3800dfe5-9fc3-3f45-a761-89e9640cf8c6 | -14.69182 | -46.69871 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c2e26971-7af5-3d74-bf93-45b5942a4d1e | -12.75808 | -46.18442 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce2b3901-dfea-3ea1-9805-757a80d9a335 | -18.60766 | -48.20823 | 2026-09-20 04:21:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4ec552d-4b41-3a60-9de1-89d7d081c298 | -11.22959 | -54.08376 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 452bc134-3b79-3acd-b617-68606eba2f28 | -12.74146 | -46.19449 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2355b86e-cfcf-37c5-aaf5-4aedc0e37406 | -11.87392 | -49.00354 | 2026-09-20 04:21:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4103d01b-afb9-3942-8502-e935c6024954 | -14.68094 | -46.69673 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8939c5b2-e2b9-3d12-8116-068f99ae0d18 | -18.6761 | -47.05444 | 2026-09-20 04:21:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d32963b5-8559-3ced-aa50-05c7714c8476 | -19.32773 | -46.36493 | 2026-09-20 04:21:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d8cea06-7962-36c8-a40f-25b8ebe273b4 | -11.7888 | -49.8286 | 2026-09-20 04:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f77503b2-cc6b-3faa-8956-4d3d8f445fa8 | -11.86179 | -47.6535 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9042a3ca-ac44-323f-a965-8b0dc81fb788 | -19.08394 | -46.65188 | 2026-09-20 04:21:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0a132ad-3853-3b3a-b32a-855689c0d927 | -12.75871 | -46.13653 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 006e2dee-acc0-3639-a220-128a339ae1da | -13.28091 | -46.73184 | 2026-09-20 04:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a11d884-480f-30de-aecd-e143118d9e5f | -16.59105 | -45.33374 | 2026-09-20 04:21:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb8398f6-64a2-3929-b5c2-c674bc74ee97 | -11.3816 | -51.40585 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 003e281c-4a84-346d-bd20-44c781a42451 | -14.93383 | -49.9063 | 2026-09-20 04:21:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce8743af-948b-32ff-8c06-a04ec5bca44f | -14.10955 | -44.84353 | 2026-09-20 04:21:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 524073fd-ec0d-3a63-8abf-15624e98423c | -12.29183 | -47.10789 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 738d733d-e121-33a3-89f2-bb2c7f2ca522 | -11.81499 | -50.06908 | 2026-09-20 04:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 776f4eb8-eeac-3384-a14d-d18c52be0e99 | -14.59528 | -48.09874 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a0ba8ae9-0144-3d3e-98b8-e31ec118e263 | -16.5932 | -45.34183 | 2026-09-20 04:21:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cbf845f0-c591-391f-a132-5ada8821c0e4 | -13.02142 | -46.91221 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17e91e01-8d92-30a5-b77c-7c5cd21d896f | -11.22349 | -54.0825 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7c23e4ba-8633-3b35-b185-0a1bdd74c499 | -14.60989 | -48.10788 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 785a0e61-f9f3-3e6c-a649-e09b65245ff1 | -13.94958 | -47.84529 | 2026-09-20 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d5ddae04-ebab-3f47-a0e2-8534f3daffdf | -15.61929 | -47.84513 | 2026-09-20 04:21:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cd125520-c729-39c9-b094-768bafb2f4d1 | -13.96339 | -47.85832 | 2026-09-20 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aaedfb0c-76fb-3a3d-a864-39bd70b783d3 | -13.39721 | -49.45616 | 2026-09-20 04:21:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97c80f98-5361-3af7-bebe-cdffbef19e8b | -15.87104 | -49.91704 | 2026-09-20 04:21:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56d8adf4-5e1c-3c80-9ce9-4a7eac52ee6a | -12.288 | -47.1072 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f56de89-592c-3d90-8175-cb8ed31f09f0 | -11.85415 | -47.67398 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1cc4059b-96d3-39e4-b9f7-0c35d97a6031 | -11.84815 | -46.87136 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d732f650-420f-3bb2-8b2d-166f11505b9d | -17.94224 | -45.95136 | 2026-09-20 04:21:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cee25901-6ea3-39e8-89aa-cca448b64fa2 | -11.7409 | -54.55984 | 2026-09-20 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b32e44e-fd94-3d02-a47f-ae342122bdf9 | -11.10808 | -54.03028 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 559405b4-eb5d-313b-90dd-af7ad70a5c37 | -10.88203 | -54.08971 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf152f89-ed9c-3bc7-a4df-fe91eb845ea1 | -11.72229 | -54.55568 | 2026-09-20 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cac06832-9958-3bc5-8146-c58c0cf107c7 | -13.62383 | -48.29358 | 2026-09-20 04:21:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7bb5b6e-5896-3317-89d1-ec125b37c84a | -11.38956 | -51.42029 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ab86040-3567-3e2f-9dd7-629937eec28f | -10.88308 | -53.9864 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b691f5ed-4bfc-3762-a829-de9c6d0004cb | -11.21313 | -54.0709 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 51adf5bb-8f70-37e2-b84f-16e2c756ced1 | -11.86082 | -47.6659 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd9665a4-e061-3ece-993e-f629ddf19506 | -12.52645 | -50.03788 | 2026-09-20 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 52755086-42eb-3a3b-bc72-87d17c6fbe36 | -12.75155 | -46.1789 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2d4052a2-ce24-3e36-87d4-62a6929947a3 | -13.88803 | -48.58218 | 2026-09-20 04:21:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| d8019928-e7bc-31b9-a965-2565778aabd3 | -12.75308 | -46.21409 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 31ed7c51-8893-3776-a734-dea659dbc08f | -13.87983 | -48.58086 | 2026-09-20 04:21:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8c921483-d5fe-3355-8fc8-ddcc5016d3c4 | -15.6188 | -47.84198 | 2026-09-20 04:21:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fda5397c-c14a-326e-876c-b003664c4230 | -11.19667 | -55.03746 | 2026-09-20 04:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d861b024-e940-3fb9-b3c7-c2146def40ba | -15.47404 | -48.41591 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 42f38f54-4eed-3360-b766-cdd24312a3c4 | -11.09495 | -54.02877 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 73e1f0f1-1c2c-3a46-a417-9eb7064e15ac | -19.02448 | -46.91818 | 2026-09-20 04:21:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d97aaa8-9f92-3f2f-824c-8639aaa41082 | -11.87279 | -47.668 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e91f205-7978-3221-b79f-87beb46353af | -11.86173 | -46.88354 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 508d3733-c4e8-3d84-8691-9b959fbf550a | -13.94658 | -47.8395 | 2026-09-20 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f4deef72-dac0-3324-8b60-256a7d353d08 | -11.7596 | -47.45204 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7083c7b9-f6d6-3974-b5d1-57d7bacdd757 | -13.62791 | -48.29405 | 2026-09-20 04:21:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f56054a-744e-36ed-baad-c7abdff3016b | -10.90821 | -53.98338 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f92440c-ee04-3ccd-acb2-09aac9e0c758 | -11.11417 | -54.03154 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6a1a0a27-dcbb-38c7-9db6-fcb71fbd3561 | -10.91811 | -53.96924 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b79588a2-2d04-3746-ad1c-5b9358b4936e | -12.29157 | -47.1207 | 2026-09-20 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0143efb6-62a9-3fe8-8184-28e1c84293a3 | -14.67014 | -54.45907 | 2026-09-20 04:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3a5e77d-80cf-34dd-93a3-af9be5aca18e | -12.12134 | -47.03513 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe3823ea-f46e-3995-973c-b08416719728 | -11.99679 | -50.02133 | 2026-09-20 04:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b204aaba-3aaa-3713-9070-e48c3904d514 | -18.55407 | -47.23932 | 2026-09-20 04:21:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d4be2f71-f45f-335b-84a0-2526b8c15fe6 | -11.83456 | -46.85933 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6adbb42f-7149-30f1-baed-3b127bb7ceee | -11.12118 | -54.02808 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9468b00a-f496-3fce-95f3-3213aab7aed7 | -11.12829 | -54.0207 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9364f6c4-f6d5-3d19-b0a8-33544420bb72 | -11.77011 | -47.43831 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5d79eda-9023-301d-8d1f-2ae5d37be337 | -15.4654 | -48.44125 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8d40c99-26b5-3f2d-9b2b-ab15cfe68d2a | -11.12125 | -54.02417 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f503d866-87c6-382a-a199-9db2c53a841f | -12.74508 | -46.19514 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0ecd1c7-f395-3fbb-9fcb-0ff48bc5d387 | -14.05675 | -52.0912 | 2026-09-20 04:21:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87301f7a-fc82-3ba9-96b6-bb6243b99084 | -14.66868 | -46.68116 | 2026-09-20 04:21:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0cdbd8ac-7179-35a5-8f94-f6a63e3b7feb | -10.86497 | -56.18353 | 2026-09-20 04:21:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ad6f93be-d283-337a-9746-99444f2681c4 | -11.87749 | -49.00856 | 2026-09-20 04:21:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e3e3e076-3884-31d2-a485-52ef1266ef72 | -12.29755 | -47.17651 | 2026-09-20 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c44758f5-6bd9-32e3-95e3-1182d5de730d | -12.75879 | -46.18017 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0df6d41-b506-3cb3-91a8-362f9f256d8e | -12.75517 | -46.17956 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9178e395-2526-39b0-b4ee-338edbcbc54a | -13.02804 | -46.91867 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f5e5907-91be-3902-a9c0-fe937ec5f3b5 | -13.22178 | -46.94006 | 2026-09-20 04:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff3a8cfd-c60e-3b2a-9f91-90c35bc6bf8b | -12.15573 | -47.04132 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2dae1d70-d9b4-3143-9262-8648fb4d3a15 | -12.01022 | -51.47562 | 2026-09-20 04:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fae8a9ef-cf6b-3cd3-87b3-e500be2af454 | -12.41928 | -47.46449 | 2026-09-20 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README45.md)
