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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d89481b-281b-3448-9f91-1315cf9882e5 | -10.83558 | -46.48259 | 2026-07-18 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75906826-7e42-30ae-a421-bea8745d9e48 | -9.5234 | -47.11805 | 2026-07-18 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 175e9994-697a-3694-abb1-f5e04295fd5d | -12.5036 | -48.25534 | 2026-07-18 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b4dffef-4a37-31ec-b693-38c295f99ab7 | -2.79267 | -48.57669 | 2026-07-18 04:19:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88252ba3-d360-3c3d-82bc-1c591eb9c534 | -12.45158 | -49.58738 | 2026-07-18 04:19:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f61c6db-7981-35dc-8838-c84e4c656556 | -9.08402 | -50.62005 | 2026-07-18 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b8e4f16-7a30-38f5-9847-02f644b1bab6 | -2.77262 | -49.47061 | 2026-07-18 04:19:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e2b035b5-309f-3d16-a654-e74e05cd3152 | -13.5788 | -47.80047 | 2026-07-18 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 989270ba-63b9-3539-bb1b-16c7cc263e82 | -9.67459 | -47.89757 | 2026-07-18 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50f6781c-5742-37be-8844-f78dc5d39c5d | -12.11499 | -49.93631 | 2026-07-18 04:19:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45984828-76ad-3e1a-b1f7-03a4e2d81549 | -12.94726 | -44.72923 | 2026-07-18 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5dd45f4c-e456-373a-a02f-029677519836 | -12.76368 | -52.16076 | 2026-07-18 04:19:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8e54d85-1980-3e86-a208-46175f4b60b8 | -13.32132 | -45.15244 | 2026-07-18 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7974782d-648e-3039-aef2-56f563e72f2c | -15.39113 | -47.50776 | 2026-07-18 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9acce960-221f-35bd-a756-8de78a969f42 | -9.0731 | -50.59415 | 2026-07-18 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0568bc9e-6acd-3695-ab3e-f7f0da9b9b76 | -9.48967 | -46.65833 | 2026-07-18 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b1d54a6f-343e-358c-b29a-c8d01d225344 | -10.8363 | -46.4784 | 2026-07-18 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 909ea8b5-6473-37a7-b877-c66fcad9f23b | -12.45078 | -49.59177 | 2026-07-18 04:19:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65e837ca-2fbb-3675-8d55-f0a1edc90f28 | -13.4391 | -43.85044 | 2026-07-18 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 801dbbfb-78da-3517-b79a-706dd138d042 | -13.31387 | -45.15501 | 2026-07-18 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e33d1075-64ea-370b-a702-7fc0c850efab | -13.3217 | -45.1479 | 2026-07-18 04:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| b6f8116f-75e8-3616-bf58-08f8c39be0a9 | -18.7364 | -54.1988 | 2026-07-18 04:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 75.5 |
| df58f07a-171b-3862-a51f-7c8b6da243f4 | -13.3023 | -45.1511 | 2026-07-18 04:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| f3597381-be66-397a-8bcb-107b3211b80d | -19.71698 | -50.21167 | 2026-07-18 04:21:00 | NPP-375D | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1fd8903b-6329-31bc-8026-ff049818fdbf | -21.77721 | -46.93048 | 2026-07-18 04:21:00 | NPP-375D | ITOBI | SÃO PAULO | Brasil | 3523800 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8416ed54-1300-37a1-8f90-2d05f8b0f201 | -22.72004 | -43.59168 | 2026-07-18 04:21:00 | NPP-375D | QUEIMADOS | RIO DE JANEIRO | Brasil | 3304144 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7a9f6b2b-724e-3e63-a92d-e6b82fd29036 | -19.8456 | -51.54551 | 2026-07-18 04:21:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cfb9723c-db2a-34a4-b499-dbf063955ded | -22.92347 | -48.73083 | 2026-07-18 04:21:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6af35ac-b7bc-313e-ae24-a7bc84ed4ff9 | -16.62214 | -49.40031 | 2026-07-18 04:21:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24294e9c-b6fa-3a4a-85fc-5e6645d3b51d | -22.46758 | -43.08781 | 2026-07-18 04:21:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2ff91504-bcbe-3c95-9308-fb1174647c50 | -22.79429 | -49.34363 | 2026-07-18 04:21:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b580561e-79e1-332c-9190-16236d6aeb85 | -22.92408 | -49.20651 | 2026-07-18 04:21:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65024587-8e36-3703-8120-99980365c578 | -22.44953 | -45.24177 | 2026-07-18 04:21:00 | NPP-375D | DELFIM MOREIRA | MINAS GERAIS | Brasil | 3121100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 69a1b17c-dcf8-3dec-bbd9-40da878c84f6 | -19.8207 | -57.99676 | 2026-07-18 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3ce1149f-5b19-380f-98f2-628ac866d872 | -20.32186 | -41.51513 | 2026-07-18 04:21:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1f38d107-39e8-3747-8261-5d5a2ee364a9 | -19.8197 | -57.9976 | 2026-07-18 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e7d25aa0-d7c0-3d60-9771-abe620e02fdd | -22.46703 | -43.09914 | 2026-07-18 04:21:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7e34d447-0e2a-39fc-a602-985f37285e2c | -19.13784 | -44.25293 | 2026-07-18 04:21:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c657146f-e3c2-3447-b685-a4dfade4d365 | -18.73379 | -54.20667 | 2026-07-18 04:21:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 8014cc28-29a5-34ac-b5cb-fb8302db642d | -22.24998 | -52.8737 | 2026-07-18 04:21:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 175a3588-b1c4-359a-9557-0f3d4064a24a | -23.16228 | -46.57551 | 2026-07-18 04:21:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f250a97e-f3b2-3836-a54f-acd77020dbf2 | -22.46469 | -43.09047 | 2026-07-18 04:21:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 93606fd0-df9c-3c8d-a7e6-97be61e4fc57 | -21.76517 | -56.3069 | 2026-07-18 04:21:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d259a12-3bf3-3d63-972c-cadebf610e22 | -20.32247 | -41.51081 | 2026-07-18 04:21:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e35e2d56-2a7c-3b18-9685-830a1eeb16e3 | -19.86987 | -57.96157 | 2026-07-18 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 917f2e4f-9e69-3d50-af97-9e2c01677414 | -18.73569 | -54.20707 | 2026-07-18 04:21:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 20.2 |
| c2cf985b-6978-3285-9f1d-0318366c74de | -21.76813 | -56.3017 | 2026-07-18 04:21:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f08d5948-68af-3c5f-b902-f2bc731b00a4 | -23.5983 | -48.25436 | 2026-07-18 04:21:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 391b8b27-7635-3794-bc98-7d3ee0ffcc20 | -22.92044 | -49.20574 | 2026-07-18 04:21:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 056c4082-88e8-35ec-91e2-a17dae25e94f | -18.73642 | -54.20357 | 2026-07-18 04:21:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 98651933-5cae-3d07-a00f-52ed8f4e346f | -22.46589 | -43.09959 | 2026-07-18 04:21:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d9b6ab60-d6a0-3580-b757-a2b0b3dbeb75 | -22.25449 | -52.87484 | 2026-07-18 04:21:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3b82299e-b5e7-37cc-8773-cddab43f980f | -22.45285 | -45.24238 | 2026-07-18 04:21:00 | NPP-375D | DELFIM MOREIRA | MINAS GERAIS | Brasil | 3121100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c5941c09-fe67-3cc0-b791-ac29d380a2c5 | -23.40072 | -46.50665 | 2026-07-18 04:21:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 2042c49e-0550-3c6b-be57-a5cbd1084765 | -22.79795 | -49.34443 | 2026-07-18 04:21:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9f6f1292-91a7-38cb-91d4-42d6a9590ba3 | -19.82205 | -57.99103 | 2026-07-18 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| bbf2b4da-0cc4-30ae-a7a3-33afb38d7327 | -22.5543 | -43.68155 | 2026-07-18 04:21:00 | NPP-375D | ENGENHEIRO PAULO DE FRONTIN | RIO DE JANEIRO | Brasil | 3301801 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 523a31ed-4c4f-3cf8-84f6-a7cc8f23a59f | -22.3938 | -47.59211 | 2026-07-18 04:21:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| af434080-78a9-3920-b895-4bfd48ec33f7 | -22.24898 | -52.8786 | 2026-07-18 04:21:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 01d0389a-ed13-3d4c-9ee5-eaccf72c7daf | -19.93325 | -44.07239 | 2026-07-18 04:21:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 792c1ab8-e0f4-31c9-80f7-4e511c1816eb | -19.81056 | -57.9818 | 2026-07-18 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 370583f5-c009-3fbf-98b5-93d0b56fca11 | -21.77173 | -56.30422 | 2026-07-18 04:21:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c1be366-9868-3c73-94eb-d5b1ca83c152 | -21.76613 | -56.30262 | 2026-07-18 04:21:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3176f2f8-b01b-3963-a3d7-76c21619602f | -19.89462 | -46.17717 | 2026-07-18 04:21:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7fcd1d4d-cb31-3420-aeec-dfcbde32170e | -22.47217 | -43.08812 | 2026-07-18 04:21:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b6ca9adb-2951-36ae-b2b8-c69dd079efdf | -19.71769 | -50.20795 | 2026-07-18 04:21:00 | NPP-375D | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 4daf95a6-4120-3d7e-b9fe-8be56b5d2e36 | -17.91681 | -45.27964 | 2026-07-18 04:21:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f91a925f-3be9-33bc-9c0f-f75bf94d50a0 | -21.85721 | -48.76355 | 2026-07-18 04:21:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8339d098-a8a8-3d25-96a4-4daaa3bf4475 | -18.73989 | -54.20406 | 2026-07-18 04:21:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 55320e73-c42a-31fc-b230-2a935d26732e | -22.19845 | -47.23504 | 2026-07-18 04:21:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f853ff30-4395-3fba-b7d8-dbd259181ca3 | -19.87053 | -57.95671 | 2026-07-18 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9255121a-50ff-38dc-96f9-d1b5bee6a997 | -19.78122 | -48.26186 | 2026-07-18 04:21:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6adb1325-d7b1-37b1-8ae7-783803ff703f | -19.81491 | -57.93444 | 2026-07-18 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a91e87ba-0166-3724-8eb2-a85ef7025be9 | -18.73105 | -54.20281 | 2026-07-18 04:21:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c771ab95-8d4b-3bb0-8cb3-20923c4fc970 | -19.35247 | -45.15723 | 2026-07-18 04:21:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23e0a004-5a2a-3861-bd0b-8c977deaa9aa | -20.32221 | -41.50947 | 2026-07-18 04:21:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a06c4eb5-3868-3d9b-b83b-f55435066569 | -19.82108 | -57.99188 | 2026-07-18 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cb142da7-78bc-374b-89ab-776c1814545f | -21.16229 | -48.56352 | 2026-07-18 04:21:00 | NPP-375D | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 5698f1e4-ed08-30c3-a68b-daf217957e2f | -21.85439 | -48.7583 | 2026-07-18 04:21:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| baf92285-dc2f-3e3f-b4d2-13425f9fd3c6 | -18.72576 | -54.20164 | 2026-07-18 04:21:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 11e186be-4911-335c-ac5e-9c65161efb94 | -22.92269 | -48.7352 | 2026-07-18 04:21:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fd65903-2d1a-3378-982e-780c65280070 | -18.73454 | -54.20317 | 2026-07-18 04:21:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7b074ebe-292d-32f6-b6ac-58ac5b204348 | -18.78184 | -44.45097 | 2026-07-18 04:21:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5075e86-5cfe-39b0-885f-a1c1145200bf | -19.78199 | -48.25745 | 2026-07-18 04:21:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc5bfdc3-2a00-3484-99b7-96e210ceb6c1 | -19.87119 | -57.95587 | 2026-07-18 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9cbd68fc-9fd0-38d7-9126-b667c29c1208 | -23.82898 | -47.51072 | 2026-07-18 04:21:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 16c22346-3259-38a2-a577-affd1e305d4b | -21.26208 | -49.11712 | 2026-07-18 04:21:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7e9924a3-1050-33b7-845c-5cc0fd0b2c55 | -21.27157 | -49.15584 | 2026-07-18 04:21:00 | NPP-375D | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 802f57a3-4c08-3529-93ee-40eeef421431 | -19.86917 | -57.96239 | 2026-07-18 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6142f005-c96d-343a-986a-d980c78e0512 | -19.66562 | -46.83308 | 2026-07-18 04:21:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d19f7d01-486b-35f0-903e-da4269d3da7a | -20.32527 | -41.51438 | 2026-07-18 04:21:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4ebfd350-0351-3e3d-a8a4-5c3a0d3cefcc | -20.07309 | -43.7093 | 2026-07-18 04:21:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2e33324d-c1ec-338b-88fc-ef326edc8fbb | -23.59712 | -48.25549 | 2026-07-18 04:21:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b0e135f-40cf-325f-a115-cb55a1152cff | -22.79344 | -49.3483 | 2026-07-18 04:21:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 087f9ed1-4586-309c-8cb5-8e9e8811cefa | -22.79709 | -49.34912 | 2026-07-18 04:21:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6591a4b2-84af-32a6-bb1f-b525b59380c2 | -22.57091 | -47.30842 | 2026-07-18 04:21:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4ff857cb-262b-32e9-921c-96b72002aa59 | -21.8588 | -48.75457 | 2026-07-18 04:21:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ac6e554-e916-355d-af6e-e7572a8cd96e | -19.82612 | -57.99932 | 2026-07-18 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 878a9d12-0fb8-3c23-af96-35d60fa5626d | -20.07421 | -43.70193 | 2026-07-18 04:21:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 97207947-750a-3530-92cc-38348577ba32 | -16.51664 | -47.73389 | 2026-07-18 04:21:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README9.md)
