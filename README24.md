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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8f98d4e-a96f-36e3-9f92-f463676b0c8a | -11.73544 | -46.61362 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 416a14aa-419f-31f7-9691-dc00a8edaf46 | -14.18675 | -46.26781 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| ffc62899-82ab-3843-8135-ced5c11a7d4b | -14.22478 | -46.28862 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 40.9 |
| d1bb3f5e-f61f-3a61-af32-a5df99185fca | -17.33516 | -46.66871 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c746efd8-605b-38c4-9322-76394c4b661f | -12.1244 | -44.83117 | 2025-09-13 03:47:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c7eb6a2a-c31a-3744-b049-1b2733037afe | -14.2173 | -46.25243 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 37271c06-45c8-3ba1-8504-3881b00387b6 | -20.16855 | -44.9247 | 2025-09-13 03:47:00 | NPP-375D | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81e0c57a-d423-3b75-91c7-7a18639783e4 | -12.09645 | -44.90117 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95dcb4ec-ab70-34d3-b983-5606ab38a6d1 | -9.00524 | -45.77108 | 2025-09-13 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 508f6c9d-d56e-3650-951c-0cb6cf24631a | -15.62465 | -39.25101 | 2025-09-13 03:47:00 | NPP-375D | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 35a15656-9826-3aff-839e-4e6d698d81fa | -18.04283 | -45.42701 | 2025-09-13 03:47:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54a7cc29-bb3b-344e-900f-2af5b3b6589e | -20.26327 | -44.19064 | 2025-09-13 03:47:00 | NPP-375D | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| eeb48659-ee77-39c0-bc3a-16eb302431eb | -12.08581 | -44.90227 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3934aa91-51f0-3076-9ede-cbbd4fded457 | -13.58031 | -44.88648 | 2025-09-13 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6185744-0d99-3dc5-9f68-b74df1db5537 | -17.28621 | -47.2557 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72af4900-3f8c-3a01-ad7f-929fd59e1b29 | -14.74859 | -45.26373 | 2025-09-13 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31f710e1-85f9-3395-a888-ed860fc6fbdb | -20.02313 | -47.63918 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f40a30d-c430-3a9f-a03d-85a0d87b9858 | -11.71953 | -46.60486 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c685ff0f-5c8d-385c-a22f-ef676ac503aa | -8.24212 | -44.35896 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63fc967e-9a31-36ab-85d1-1bf398de22c8 | -10.76688 | -41.33825 | 2025-09-13 03:47:00 | NPP-375D | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 01cdce9b-bb75-3552-9324-295d90954c00 | -18.89228 | -47.05427 | 2025-09-13 03:47:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a99d4aae-8a5f-3399-b19f-4fff1562646f | -12.10036 | -47.58215 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 32f37dcf-5fc2-3cf9-a883-79baf90e6622 | -10.24093 | -48.63947 | 2025-09-13 03:47:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 286891c5-c085-3a75-a4a2-c85a6f56129c | -11.71096 | -46.55912 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04d0fa95-aed9-3138-a358-f47ed23c697a | -20.34135 | -46.66563 | 2025-09-13 03:47:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7448cd8-782d-3095-ad77-400643d0618a | -11.85362 | -50.56631 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 73480c1b-680a-394d-8a9b-9e271fdf0034 | -13.26573 | -43.74001 | 2025-09-13 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63382890-ca3b-384b-9659-f5252b8c4304 | -13.00193 | -46.7449 | 2025-09-13 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cccfd9b7-52a0-32a5-a251-05eea3680180 | -13.88189 | -48.27913 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60574380-86bf-3e32-b612-8c9b6ec91afa | -12.84475 | -47.93751 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| be509872-b8a5-3013-b244-ddafbd70cdb9 | -12.85167 | -47.93435 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3b02f519-be5e-3a43-a206-13f84298e630 | -12.10368 | -47.59668 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b3ac46fd-147e-336f-931a-fdbf9438b4a0 | -10.75286 | -50.52155 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a3fe51e-325a-388a-8e28-1a03590475c5 | -13.77298 | -46.28833 | 2025-09-13 03:47:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 740fd853-d75d-34cd-9d45-b12c0a9bb47a | -18.59242 | -47.19393 | 2025-09-13 03:47:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0938f140-4e5e-3763-830b-c4b1913efb96 | -11.72438 | -46.58022 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 040b411e-6004-3b95-a2b5-c43bde068d98 | -12.10539 | -47.58806 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a269e751-6217-353c-87ea-3027ac5359b4 | -13.08108 | -48.26222 | 2025-09-13 03:47:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 52ff827d-f328-338c-bd02-ec60136ff099 | -14.18013 | -46.2457 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4fb1bf59-c501-367a-9635-c78e5bf26f6b | -11.86339 | -46.75298 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9cfe33cd-34fa-3db3-9691-f1b45d1bf3e7 | -7.56299 | -42.65994 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3c63d24a-2aec-3ed3-b507-57ea651add02 | -14.12993 | -45.37389 | 2025-09-13 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dce4d97e-eb56-3b6a-bcd6-2fdc8fd54978 | -14.21811 | -46.27636 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| e61d9c12-b5f6-3ef4-9372-c2765005244e | -12.94405 | -48.00686 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f61ff73f-4b6f-33cc-b838-5996282ac9db | -17.30672 | -48.73717 | 2025-09-13 03:47:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01c5ec44-5f2d-3788-8ed1-4d9ded28b54f | -14.21874 | -46.30135 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 8118bef4-19dd-392c-8a9c-95adbfb97462 | -18.06654 | -45.45485 | 2025-09-13 03:47:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5f74fe77-2365-3700-9960-604dcf4cb3f6 | -17.30572 | -48.74176 | 2025-09-13 03:47:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2445f97-1d84-39e7-98cf-69681d1dc2e8 | -14.2268 | -46.27866 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| fa7ed6a5-9f19-3f67-8e5e-a40dd6b5f3e4 | -11.48679 | -43.62796 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ee850375-b97e-39cb-ab00-078d713d13ea | -14.17556 | -46.24101 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2e68c2cf-29e5-3b07-b482-d422065063e0 | -16.25772 | -50.07696 | 2025-09-13 03:47:00 | NPP-375D | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0aafa325-1d27-3f54-99ad-baffd6bc86c3 | -14.70377 | -42.50813 | 2025-09-13 03:47:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5c7ddcb8-c6a0-3d2d-8ac7-120eeabab09c | -18.3305 | -50.97185 | 2025-09-13 03:47:00 | NPP-375D | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 553e611b-44a9-3cf5-a2d0-ad264075c52f | -11.84295 | -50.55982 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 58639d75-fe2e-319e-8794-f9dc1edebb7c | -12.11587 | -44.84838 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f0f22573-f866-3139-bad9-797699fd313b | -12.90995 | -47.95906 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f31f571f-f580-345a-ba1d-be917f05ea0f | -19.2045 | -44.62149 | 2025-09-13 03:47:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b09e4ed4-5e64-391c-b6e1-85b7168d84bb | -14.18549 | -46.24637 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0eb4f42d-8007-33a2-8f36-cbe9f1e895f0 | -9.41214 | -43.40762 | 2025-09-13 03:47:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d6848b96-e82d-386a-ac97-1684a400a37f | -11.43332 | -43.55096 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c7632cd-39e0-3479-b93f-6585e4479e29 | -14.18013 | -46.27343 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 123021d6-c744-368e-ac7c-d13dfa470abe | -21.19176 | -44.02831 | 2025-09-13 03:47:00 | NPP-375D | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 11c07290-d0b3-39b3-ae37-bfae6662fa15 | -11.74435 | -46.62822 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1bf2bb06-4b19-3159-ab8a-19167a7e3750 | -14.22277 | -43.50966 | 2025-09-13 03:47:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39148a7f-6627-3c01-a46b-9058f5e812c4 | -17.28562 | -46.10831 | 2025-09-13 03:47:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 016bbf7b-d861-3f8a-b016-43937ff48416 | -10.37017 | -50.50053 | 2025-09-13 03:47:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5411a87e-e43b-333b-a56e-c0bbd74e8715 | -11.85065 | -50.58057 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| e1f84820-aa19-3044-97c7-fb6e67437929 | -11.79687 | -50.55331 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1b628bc7-1448-379f-a45e-b7dce06a4f82 | -18.97421 | -48.60068 | 2025-09-13 03:47:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d29508bf-a51a-3222-8395-65215963cf73 | -10.36225 | -50.49928 | 2025-09-13 03:47:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8f40a072-515e-3d66-b7f9-409ee647df48 | -14.2821 | -46.05947 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd1f2dc5-8d0b-3b54-9568-f73dfcbfd97e | -12.0002 | -47.76536 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9c9886a2-ee1d-3597-8e63-b34d5e260586 | -17.41746 | -49.24712 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c56a6af-02a6-36d1-bff5-7966a3f6fcab | -12.10764 | -44.89708 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 849b90f7-0766-3f32-aaad-040ca243ce36 | -8.18136 | -42.4142 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d22c17e7-b7c5-37c9-b7a2-31904a0c0c15 | -11.45298 | -43.57501 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1cb34c0b-2e6f-3294-920c-fb208f46ce08 | -11.47463 | -43.61508 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2112fdd-951d-31d9-be7c-7743f4f61502 | -12.82068 | -47.96282 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4c5db2cd-7ce2-3847-adc6-1eefc2c3088d | -13.58414 | -44.89303 | 2025-09-13 03:47:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c068c457-7d60-31fd-b27d-6a2434e84816 | -8.08602 | -42.55941 | 2025-09-13 03:47:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 11d7800c-d275-3770-bd6b-18b0d7eb217e | -20.01985 | -47.65224 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e48358d0-49d1-3d17-b3ec-2b0a65edd3f0 | -11.72363 | -46.58401 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd813666-b1da-3290-9c1c-eb3254b0ca2f | -10.77712 | -50.55018 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 84ebeb9d-af39-370c-a9e0-8c6d97ad17ae | -20.09503 | -46.91236 | 2025-09-13 03:47:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9ac7611-9bc8-378b-9014-bae6df1339d3 | -9.00601 | -45.76691 | 2025-09-13 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 45fa000c-727c-3667-a940-ec26f19e8205 | -18.32917 | -50.97757 | 2025-09-13 03:47:00 | NPP-375D | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8fe81394-49f9-3ffb-afb4-3c529e768b44 | -11.59305 | -50.61459 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ddbb8f64-17f0-38ac-bb9f-f69c8486cdcd | -13.88289 | -48.27427 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8145dcf2-e193-3f0e-9f44-45b4a93c4703 | -10.36796 | -50.50839 | 2025-09-13 03:47:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 41dff2cb-d285-37ee-8d18-6824c692cd2d | -17.40857 | -49.25888 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9b9402e5-6bda-3c83-b7e3-1831c21cc66b | -11.84093 | -50.55593 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 613efd70-0d40-33ee-b846-9ed49884ff78 | -16.36183 | -51.5404 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 295c1d44-8c23-30f0-a1f5-62e79d231287 | -10.59376 | -43.02943 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d074c84a-ef6f-3895-9012-e042e675f152 | -7.94197 | -46.90955 | 2025-09-13 03:47:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55362f1d-a4f8-3881-8fad-78d8cd26a3ac | -13.94523 | -48.18446 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bbee85fb-feab-327a-8449-c4944e214252 | -10.7622 | -50.55442 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0c454277-7f16-3ff4-896a-7b8ecca2a085 | -17.4443 | -49.23931 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 844ca6ac-8df6-3182-9d2f-5026d14582cd | -11.35791 | -43.50492 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eaded592-9832-3afa-9d33-691b9b9121cd | -12.99629 | -46.7441 | 2025-09-13 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README25.md)
