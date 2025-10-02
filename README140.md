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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9dcdf856-ef7e-36e2-8dba-c930bd5c9d97 | -15.25298 | -47.9081 | 2025-10-02 05:57:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| dfe1b6ce-e110-3c30-964f-f78c02f43d1c | -13.378 | -47.29227 | 2025-10-02 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1cb54940-d002-310b-bee8-b89653086d55 | -12.94578 | -48.43144 | 2025-10-02 05:57:00 | AQUA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9fb0de44-59a0-319a-a666-93ca1c50eeb9 | -16.21119 | -48.11005 | 2025-10-02 05:57:00 | AQUA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 17ca3ccb-ad7d-3dce-85f2-17466a35672f | -13.21012 | -48.51152 | 2025-10-02 05:57:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 471b2be1-4980-386e-bde2-3f441aca2d65 | -12.67526 | -48.56793 | 2025-10-02 05:57:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| bd783622-70f1-39f5-8081-82f58931d528 | -14.39793 | -46.07447 | 2025-10-02 05:57:00 | AQUA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5fa5a846-6430-3317-8427-81627002a28b | -12.81927 | -47.02244 | 2025-10-02 05:57:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 28d978c9-f812-32d0-a414-4d37db41d055 | -12.49561 | -50.25178 | 2025-10-02 05:57:00 | AQUA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4bd25987-4eba-34a5-ba1b-b2d59335dddd | -15.19034 | -46.39513 | 2025-10-02 05:57:00 | AQUA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c37f559c-e699-3278-ab70-4f1a6b93f9d5 | -13.37201 | -46.33343 | 2025-10-02 05:57:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 715d70ef-2677-373c-a7be-ff4893e4ed1f | -12.86728 | -47.00228 | 2025-10-02 05:57:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 64a6f5c7-ffb1-34d0-a32d-20b360423bc6 | -15.27789 | -49.30627 | 2025-10-02 05:57:00 | AQUA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1f00d057-4a73-3513-b75f-b24e8b9033a8 | -12.26613 | -47.80568 | 2025-10-02 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d30ecc7c-89a1-3c21-b607-227d17e6a8db | -13.29193 | -47.25404 | 2025-10-02 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ba1660ed-102c-3d7a-90f9-b7d7813f4c9e | -13.80389 | -47.53578 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 36.3 |
| d62f1b3f-5629-3d36-837b-129090551b05 | -11.83709 | -44.95235 | 2025-10-02 05:57:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 66034bae-15be-3e12-bbc4-804a40e22604 | -13.95358 | -48.13326 | 2025-10-02 05:57:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ef46eb76-0464-3b36-a42b-ab77b44a8171 | -14.36771 | -45.96199 | 2025-10-02 05:57:00 | AQUA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 05766dcf-8593-33b8-b119-e6d1dfc2ef0d | -11.57123 | -47.0192 | 2025-10-02 05:57:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a89fd9af-197f-37a5-8114-ced21f0f3866 | -14.64444 | -48.1461 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4a838ac8-f830-3c55-9cd0-bb428cc971fc | -11.27281 | -47.82489 | 2025-10-02 05:57:00 | AQUA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 71ec99c7-bd6b-38c6-b7d8-161789c75154 | -12.66484 | -48.57012 | 2025-10-02 05:57:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9b1726be-dc10-3bec-b7e4-3d5a7071d6c0 | -13.80525 | -47.52679 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6e797a9e-7a2c-3707-a847-f47b283933c8 | -17.17575 | -47.02273 | 2025-10-02 05:57:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 54edd702-a5ab-357f-9873-fbe40d39b0c1 | -12.6828 | -48.57871 | 2025-10-02 05:57:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| afc6db39-f905-394e-b0a0-0cbffef4ba85 | -13.29327 | -47.24509 | 2025-10-02 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c2edd5a1-81cb-3a36-9d97-7be8c8521fce | -12.86594 | -47.01125 | 2025-10-02 05:57:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 88bfa7a4-5fa4-34e5-9ade-f3805c699110 | -13.21124 | -48.44505 | 2025-10-02 05:57:00 | AQUA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 178a984d-d515-3564-904e-8ac6c09c250b | -14.98546 | -46.92133 | 2025-10-02 05:57:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d07d436f-9d83-31e8-97f8-8aa93fe9c141 | -14.59005 | -48.324 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 59bbf776-ed06-331a-bc01-5c761eaf3f15 | -16.13636 | -46.68317 | 2025-10-02 05:57:00 | AQUA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 987f4985-9b1c-3af3-9bd1-44981b565eef | -12.27695 | -45.36753 | 2025-10-02 05:57:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 2ff8e513-d7e5-322d-9536-1914b0c5e504 | -13.32368 | -47.22224 | 2025-10-02 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 580a7c40-170b-3d3d-a7a1-34b4d23286e8 | -14.2171 | -46.11319 | 2025-10-02 05:57:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 44d2b006-69df-3705-988b-1a91969196ec | -13.30382 | -47.84185 | 2025-10-02 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e48475af-e36b-369a-b94d-ad1290f182ab | -11.85066 | -48.04251 | 2025-10-02 05:57:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c9635f2d-c6a0-34b4-b6d0-f8b35afbf1ee | -15.99654 | -50.89885 | 2025-10-02 05:57:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 89012ad8-9997-3132-aaa2-6b332286e521 | -13.32078 | -47.00106 | 2025-10-02 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8b89962e-e423-3016-9292-4792bcfa3ea7 | -14.47892 | -48.44137 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 467a4b1c-c598-38d3-957a-1d8878a23dbb | -13.95501 | -48.124 | 2025-10-02 05:57:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9f85b10a-f557-3ce3-b138-ae6e54fb8508 | -11.57477 | -50.1587 | 2025-10-02 05:57:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4342afd9-d92b-3204-89ed-1962b7cadf66 | -13.81269 | -47.53715 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4480a8c5-1b17-3b3e-ad86-08ee0b330b9d | -13.42988 | -47.80264 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8c57c841-9790-3fb4-9fed-fe3ec379ceef | -16.0009 | -50.89396 | 2025-10-02 05:57:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 192a7308-55cf-3902-ad67-57f1f1c7727b | -15.25234 | -49.2919 | 2025-10-02 05:57:00 | AQUA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9b3fe5ff-df43-30ad-b46b-3cbebe3f7667 | -14.4297 | -46.10544 | 2025-10-02 05:57:00 | AQUA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 73ace6b9-221f-309a-a77a-72d8f9fe2477 | -14.60406 | -48.23281 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6789565a-bbe5-3feb-be3f-e48bb90b3875 | -15.21592 | -47.17195 | 2025-10-02 05:57:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c26c97fb-9fab-31d7-9c2a-ca2d0e2ea44d | -13.14609 | -47.84163 | 2025-10-02 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| bb5cc25a-6536-3168-973a-3ee97ad2236c | -11.27421 | -47.81573 | 2025-10-02 05:57:00 | AQUA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 8b30dac2-7e88-3880-9cc0-721d745c18cf | -13.91607 | -48.07411 | 2025-10-02 05:57:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 055c4b53-5724-3b7f-954e-302f3e3a0505 | -13.69221 | -48.6259 | 2025-10-02 05:57:00 | AQUA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f3390828-48bd-33bd-b026-c4fdaa0f3c1c | -13.79646 | -47.52542 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 65e3447d-0ec4-3f43-ab12-eb59c0feb1d9 | -15.22931 | -48.72516 | 2025-10-02 05:57:00 | AQUA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8504660f-c168-3bac-85a1-3ae38a8f00c1 | -14.86391 | -48.28352 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c99ae045-ef1e-3c2c-b876-3be0e99a691e | -12.70981 | -48.5829 | 2025-10-02 05:57:00 | AQUA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 85aede2a-f069-34d4-a1a0-6dd54524c9b7 | -14.30853 | -45.98686 | 2025-10-02 05:57:00 | AQUA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 21.6 |
| a70759fa-f29d-3f23-854c-629d8468e54a | -16.02643 | -50.92046 | 2025-10-02 05:57:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a996c069-0768-37cf-91b2-e0eb69aa9050 | -14.97659 | -46.91998 | 2025-10-02 05:57:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bdda4825-82da-30b9-8d13-7af34ff15b12 | -14.76093 | -50.53033 | 2025-10-02 05:57:00 | AQUA_M-M | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 100207cf-00aa-3c5f-8b0f-dd341b60d836 | -13.39602 | -47.78809 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 3179fc90-db3b-3eda-b8f8-b23677f4c6e0 | -15.26732 | -49.31446 | 2025-10-02 05:57:00 | AQUA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4c317bbf-67d9-3d16-8658-d40da39ab4cb | -13.65353 | -47.30703 | 2025-10-02 05:57:00 | AQUA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0d50efb3-4e83-3512-935e-b9e3b12f0f75 | -11.91156 | -47.88357 | 2025-10-02 05:57:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7ca57672-df78-3226-98b9-5c3a744dac68 | -11.81666 | -45.03009 | 2025-10-02 05:57:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 39157949-eee7-30a5-a88b-81637cf15fae | -13.00856 | -45.21196 | 2025-10-02 05:57:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c7b6a9c4-267e-3124-9a20-59f8d0d02124 | -13.34488 | -47.33307 | 2025-10-02 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 76cb8379-709e-3511-9c00-93ac219037fa | -13.78052 | -48.05621 | 2025-10-02 05:57:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 64b6c524-2e84-3e88-8fdc-4e5ebc9ab9aa | -11.86856 | -44.99698 | 2025-10-02 05:57:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| bca886b0-a544-3880-a492-8654fc4ce592 | -11.87352 | -45.02818 | 2025-10-02 05:57:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 26236f10-3ee2-390d-9286-2256e62acc47 | -12.94344 | -46.36634 | 2025-10-02 05:57:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 91edb471-853c-33bd-bb12-031679112f9b | -14.48035 | -48.43211 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 295fe0a2-a63a-3b68-bd42-ec65b0f3f8fb | -11.90862 | -46.74187 | 2025-10-02 05:57:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 64b5f566-c0f5-306f-a72b-51b960661988 | -11.85925 | -44.99598 | 2025-10-02 05:57:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7dc3c075-864b-38c1-a066-f9889a6a0be7 | -13.7447 | -48.7015 | 2025-10-02 05:57:00 | AQUA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2469d11d-4f6e-3268-beb8-3d37a3d79c67 | -14.86611 | -48.38699 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 647470c5-be24-3ac9-b792-debbf31fc724 | -13.30134 | -47.19128 | 2025-10-02 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dcd5af15-e557-3bad-89bb-f06ae0668d29 | -16.04345 | -50.87769 | 2025-10-02 05:57:00 | AQUA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 1974ab95-6ccc-377c-9e98-1fe88710fd17 | -13.40483 | -47.78947 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 7240961d-09bf-3ead-8527-c61dcdb26a85 | -13.31197 | -46.99975 | 2025-10-02 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 34793f19-5566-30d0-a742-f736d137b943 | -14.43796 | -46.36779 | 2025-10-02 05:57:00 | AQUA_M-M | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8711e88b-12e1-3847-9f5c-776b525b0849 | -13.30693 | -47.58437 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b42b9e5e-a0f9-368e-a704-2aec64fe9ce2 | -12.8646 | -47.0202 | 2025-10-02 05:57:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| afaaacfe-d0f3-38c9-9280-7baa1159046a | -14.69295 | -49.61407 | 2025-10-02 05:57:00 | AQUA_M-M | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 137bf84c-7508-3795-9602-067daa250af3 | -14.70216 | -49.61558 | 2025-10-02 05:57:00 | AQUA_M-M | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 15ad90fe-70c7-325c-a892-9053018675fc | -14.36908 | -45.95235 | 2025-10-02 05:57:00 | AQUA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f73a0824-c0a8-3e63-b995-8616d376034b | -11.26532 | -47.81441 | 2025-10-02 05:57:00 | AQUA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 89d5fd85-063b-3402-bc7b-c0fb9eb8a4d8 | -14.5898 | -46.7167 | 2025-10-02 05:57:00 | AQUA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| fc954a77-540f-394d-9072-52d1863dd9eb | -13.80254 | -47.54477 | 2025-10-02 05:57:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ec2e643c-7c11-38d6-8045-14d16132dfde | -13.30988 | -47.86136 | 2025-10-02 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 07b802de-8c11-3f8a-a62a-d7eebe299a41 | -11.82589 | -45.03156 | 2025-10-02 05:57:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 321bdff7-c276-3a76-9b34-63d83c07dc1c | -12.49383 | -50.25631 | 2025-10-02 05:57:00 | AQUA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f6043438-fa43-3654-9236-1acc82ab058b | -11.97746 | -47.01486 | 2025-10-02 05:57:00 | AQUA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7aae70dc-730e-325e-896e-1afa6558668d | -11.8607 | -44.98583 | 2025-10-02 05:57:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c6d1ad28-08b7-3a3a-9ade-45319f2ffb5d | -14.64544 | -48.25792 | 2025-10-02 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7db7a9d5-e3a5-334d-9d57-861259007405 | -15.29352 | -46.387 | 2025-10-02 05:57:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 139d8fa7-4de0-3b1d-91bf-b10907afd467 | -13.69073 | -48.6353 | 2025-10-02 05:57:00 | AQUA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a4401d0d-d313-3232-9046-94c6a3cf8a01 | -14.41673 | -46.13591 | 2025-10-02 05:57:00 | AQUA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 307288c7-39c4-383c-a793-18ddb87bc5c3 | -16.00883 | -50.90623 | 2025-10-02 05:57:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |


[Clique aqui para ver as próximas entradas](README141.md)
