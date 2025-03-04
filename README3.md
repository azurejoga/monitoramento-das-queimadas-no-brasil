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
| 00409452-a6e9-3052-b439-f6eacbf54a44 | -10.53257 | -44.66661 | 2025-03-04 04:01:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e98b03d-1eab-3dc8-83aa-5d13f6616133 | -11.46586 | -48.0044 | 2025-03-04 04:01:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbc1ac6d-dd08-3d79-b162-7a0d7586f4cd | -7.83611 | -36.86262 | 2025-03-04 04:01:00 | NPP-375D | CAMALAÚ | PARAÍBA | Brasil | 2503902 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ab3db123-3562-3ee5-aea6-303f681fc1d0 | -8.43862 | -36.34595 | 2025-03-04 04:01:00 | NPP-375D | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 71064a11-7372-3440-8a19-2312fa1d0b35 | -8.10495 | -43.14234 | 2025-03-04 04:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 18328033-1392-3198-8dfc-0fe65860e801 | -8.10561 | -43.13831 | 2025-03-04 04:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fecff324-8f5e-3940-af5b-d137a351e8a5 | -11.46501 | -48.00906 | 2025-03-04 04:01:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d236eaa0-5fb9-358d-850d-04640c17876b | -7.83244 | -36.86206 | 2025-03-04 04:01:00 | NPP-375D | CAMALAÚ | PARAÍBA | Brasil | 2503902 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e3072b92-03cb-3a4c-8f2b-f5e4daed5147 | -14.0183 | -45.62678 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0eebcbb8-9277-3e4f-a75f-696bfa61682e | -14.02416 | -45.63737 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e56d2c46-7504-32b7-a46a-c74d4132d558 | -14.01585 | -45.64061 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7b924db-8b24-33ad-b230-0c1a469c5e7b | -14.01081 | -45.62541 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 87828468-40c0-3b52-b06d-0a003bb7001a | -13.98967 | -45.59079 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cd2b760-93a4-32ff-9ffa-25f1c45a8a23 | -14.02041 | -45.63668 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fdde7103-78d9-363d-acb9-2bc1a7e71d07 | -14.03246 | -45.63413 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 145da709-63c7-3b4e-8afb-4fc1a2889d52 | -14.03459 | -45.64404 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ea8ffbf-9216-30a9-9e92-703299565c43 | -14.02709 | -45.64267 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b10728f-5b90-3371-9045-74e44a1d2899 | -13.99714 | -45.59216 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 09828ceb-0d16-3572-9074-6d00620230be | -14.02953 | -45.62884 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a98c93bd-81b4-3494-ae98-502b95e3d2aa | -19.4541 | -45.30582 | 2025-03-04 04:04:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a89a8c9-c6bc-3166-8348-edff55995a98 | -13.99046 | -45.58619 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e64e371e-6898-3f83-bc45-c9f49dba8bfd | -19.2334 | -46.08597 | 2025-03-04 04:04:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d687d5fe-60e0-3d93-bb5f-0b1072387563 | -13.99419 | -45.58688 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| aca3362b-39ba-308f-968c-3086d21573a8 | -13.98887 | -45.59539 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4d23c4c-d4cc-3a4e-87d4-a60fa1c50457 | -16.07575 | -46.61566 | 2025-03-04 04:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcfc8209-700d-3ffb-a215-cf3a682a0534 | -17.38711 | -46.56331 | 2025-03-04 04:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ede34cd-2013-365a-8d86-2d6541617fe2 | -19.24131 | -46.08303 | 2025-03-04 04:04:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c38dc3f-5762-3a77-903f-73762edc102a | -13.99793 | -45.58756 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 60cd077b-92c2-3f4e-b212-aa2ea8c79725 | -13.99182 | -45.6007 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 66ff2f42-115c-373d-9cbf-48ac04bde128 | -13.9934 | -45.59148 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 057538dd-1d65-3265-85c9-c2bfa65b263d | -14.01537 | -45.62148 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c568f31d-46c1-32a1-a7cb-5b17be517e00 | -14.01292 | -45.63531 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5680797f-bd0f-328d-ace4-6cd166c02a18 | -14.00706 | -45.62473 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dd0d60d-3b2c-3f16-a828-f280c40c79bf | -14.02204 | -45.62746 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cefc9c30-bbea-3252-b6d8-f0e7608c7b15 | -14.02659 | -45.62355 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53750a1b-19a7-3218-a2bb-cda6a4405926 | -14.01162 | -45.6208 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6f4671af-7039-399e-917d-67465008fa52 | -14.02497 | -45.63276 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4f88d59f-4d5a-3026-a9cb-f90c1243ccbe | -14.01455 | -45.62609 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf3ae2ab-fc35-305b-be15-105529d515a6 | -12.95708 | -41.04276 | 2025-03-04 04:04:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5cada37c-8f96-3e30-b5b2-cc92011d5156 | -14.00999 | -45.63002 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 800db569-239e-3cb6-bb3a-7eccd3321f99 | -14.01565 | -45.61933 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8de910d-6612-3854-b778-085e3af51f6f | -13.99577 | -45.57769 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 066eb78d-0dc7-37a5-af32-4d524e08bd1e | -14.10335 | -44.12886 | 2025-03-04 04:04:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d4015d7e-b684-3551-a0df-8b1464a52522 | -13.99261 | -45.59608 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 808b1bb2-bf94-3f82-a066-f24fadca6211 | -16.0731 | -46.12595 | 2025-03-04 04:04:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41c8dd7c-2b1f-3d97-93de-3c22145d27e2 | -13.99282 | -45.57241 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3ef2d80-619b-32f7-918a-ba944f874efe | -13.99125 | -45.5816 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a69f95a-e7f6-356e-8dec-4145e3050a61 | -17.981 | -47.22436 | 2025-03-04 04:04:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 470aa7d3-f24f-33d1-a0e9-e0c1d076aaa5 | -20.33099 | -42.29768 | 2025-03-04 04:04:00 | NPP-375D | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 431d674f-6dcd-3e1c-8ff7-2fbf9ad51a9e | -14.01033 | -45.62787 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 426027af-72de-3f7a-aa82-b9965a8bf317 | -13.99498 | -45.58228 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fcedb1ac-f474-3fcc-b55e-278e69d0b999 | -14.03084 | -45.64336 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e7de176-5bb9-3096-8bc9-752ccc128a05 | -13.99635 | -45.59676 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1562517d-fd5f-3f73-b1c1-7c2c98358977 | -13.99872 | -45.58297 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| da217cf8-2bf7-3986-a36e-efe699f6be02 | -14.01374 | -45.6307 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 195fb1cf-f8a9-31c9-a711-3bc0966284a4 | -13.48189 | -44.04054 | 2025-03-04 04:04:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bed8b8d2-dea8-380c-bbfc-99626ccb55af | -14.01329 | -45.63317 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11919ecd-28a0-3f66-ab61-bcd44554e285 | -13.99951 | -45.57839 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a364075-539e-34e9-a3be-3d9a4c8d1d75 | -14.02123 | -45.63207 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1590654c-6fc3-3f08-9ccd-99f6231219b8 | -14.01748 | -45.63139 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e3d4b00e-f4f2-3e34-92bc-1367bc03cc0c | -18.03892 | -39.92395 | 2025-03-04 04:04:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7f29140d-3f58-38fb-9b0a-0ab6ebfad0b9 | -14.02366 | -45.61826 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2389d4f1-9d2c-3ea7-b0b7-379c17c4cc8c | -13.99556 | -45.60138 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3343da9-7830-39f4-8804-6d1efc030df3 | -12.18905 | -46.69823 | 2025-03-04 04:04:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 090974d1-ff81-3ca8-88b0-bf5dc32b8f25 | -14.01879 | -45.64592 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 567d69cd-f23c-3bb3-ae79-89a17823f4ef | -18.15532 | -48.01873 | 2025-03-04 04:04:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76790a47-460f-3d20-9581-4b56b2b2a146 | -12.18841 | -46.70196 | 2025-03-04 04:04:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80a71067-c67d-3806-918b-7c655bc299af | -13.99203 | -45.577 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28af4561-525c-3501-8370-b4daf8d74e56 | -13.9993 | -45.60206 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7774dcfa-5b3b-3ed2-8064-1f8e5d2f9dda | -14.00738 | -45.62257 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60bd923c-b57f-3d06-aa4e-dd7b9b602d62 | -17.01256 | -46.42371 | 2025-03-04 04:04:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01b7a2cb-fb82-36bc-b587-84e322a17f81 | -13.98751 | -45.58091 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a700a27-acb6-318a-8e04-8d05916de1fd | -14.0196 | -45.6413 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60babe64-c24b-3496-979d-58a8586fc1f5 | -14.01992 | -45.61757 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f6f1f37-f606-3721-9d56-c0949bcc52e6 | -14.01911 | -45.62217 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b7c32634-0803-35d4-a1b6-e7b283da95b7 | -13.98672 | -45.5855 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4eb8b2ac-4fe1-347a-add5-a97c966fbd68 | -14.02791 | -45.63806 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a6fa615b-867f-30bb-9778-a8b15b2b75e8 | -14.01486 | -45.62394 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a8576c43-9a14-3b96-b680-472dd0add64d | -14.01667 | -45.636 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0c5408ac-f341-33fd-9d99-ad657406b0e4 | -14.02335 | -45.64198 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0da90847-d718-32f8-a3fb-42c69e02a52b | -13.9883 | -45.57631 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e970889e-4c23-3e2a-a660-fa2b225eb922 | -14.00009 | -45.59745 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e2965c18-d77d-38b4-8778-cbc0d435c5b5 | -14.01408 | -45.62856 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7ae4c40d-9ba3-37df-a6ae-41980ad0f326 | -14.02254 | -45.6466 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4319d263-51cd-3087-bb1b-78652c8d0501 | -14.02628 | -45.64729 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 985d7e26-f51d-3af2-9fac-749dc1562560 | -14.03165 | -45.63874 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d25c12e-1bcd-356f-8e58-a02586c7f86a | -14.01112 | -45.62325 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2748bd0-dac7-3093-9602-f80a6f3518c6 | -14.00088 | -45.59285 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1195f94c-f79f-349e-957b-ec830e201e28 | -14.01251 | -45.6378 | 2025-03-04 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfc54a9e-8534-3b08-955f-cadfb6c6f810 | -17.97715 | -47.22356 | 2025-03-04 04:04:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad6c7238-02a1-34b7-a2c6-ac51f6770d24 | -21.63073 | -48.67997 | 2025-03-04 04:06:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a9a9d397-8945-363f-9f3e-af42b9489295 | -20.0991 | -43.99053 | 2025-03-04 04:06:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e1959de9-ef0e-30dc-bc67-92d64f7a1e38 | -21.6347 | -48.68074 | 2025-03-04 04:06:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f8dba8c-af7a-3a9d-9741-52d494feae44 | -20.09971 | -43.98677 | 2025-03-04 04:06:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b2e6374f-4f1d-3591-a22c-c7133d6af3b3 | -20.09515 | -43.99371 | 2025-03-04 04:06:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d9ecf175-9ee5-3e58-a0ad-f623ce589ac4 | -23.98474 | -48.91517 | 2025-03-04 04:06:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0e3b39f-dc23-35cf-913a-722c9413729b | -24.49753 | -47.99923 | 2025-03-04 04:06:00 | NPP-375D | SETE BARRAS | SÃO PAULO | Brasil | 3551801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 467a0be4-90d4-31e2-873f-ffe51c4a2b54 | -21.63867 | -48.68154 | 2025-03-04 04:06:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc3af74e-e28c-3fe5-8208-dab7f0629040 | -21.18048 | -43.98098 | 2025-03-04 04:06:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 51362df7-d7a8-3a0d-8621-36d409af742a | -21.62418 | -43.46546 | 2025-03-04 04:06:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |


[Clique aqui para ver as próximas entradas](README4.md)
