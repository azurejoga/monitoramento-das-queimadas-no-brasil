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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51770973-c3ef-3574-be6a-6fffde59cac5 | -7.8571 | -46.7082 | 2025-07-29 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| d2e59430-9b88-3d40-ac18-46b61eb89cbf | -18.449 | -54.6462 | 2025-07-29 00:00:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 87.7 |
| d96d3229-1bda-305a-9e30-5777c146a8d5 | -7.9445 | -44.0918 | 2025-07-29 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 9826139c-e951-3fec-91ac-c2fbcddf1a20 | -7.9259 | -44.0706 | 2025-07-29 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| bbcff4b0-2d8e-35d6-8789-ed41584a38b0 | -7.8756 | -46.7287 | 2025-07-29 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 5ebb0e40-2e9a-3309-9376-3010eae52570 | -11.4393 | -45.1154 | 2025-07-29 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| d2c71f17-dd61-33a9-b0a9-d1cbf9973970 | -2.8921 | -48.2977 | 2025-07-29 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 273e84c7-9803-30dd-a469-4bd508754eaf | -7.4541 | -49.4018 | 2025-07-29 00:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 84fad726-a8dd-3cce-a666-3fc37e181565 | -18.4287 | -54.6704 | 2025-07-29 00:00:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 59.4 |
| cf23f0f7-8e27-34b9-b222-870143ab3e71 | -7.8568 | -46.7304 | 2025-07-29 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 151.4 |
| c65ebaa6-3e5c-3ed8-a572-c592be7fd24b | -11.7317 | -48.1849 | 2025-07-29 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 797e639f-6cb4-3265-a387-6157ec27f361 | -2.9106 | -48.2971 | 2025-07-29 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 5e8dbc9d-ea4a-32de-a23f-daf6d6085d85 | -6.0343 | -47.5579 | 2025-07-29 00:00:00 | GOES-19 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| f79f256e-c114-3fa7-a74a-e81cacc88375 | -11.4201 | -45.1181 | 2025-07-29 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b5a675a3-e74e-3b8b-9e49-30a50d5492b6 | -7.9256 | -44.0937 | 2025-07-29 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 6101e8ee-fc8c-3671-b318-f6aa41133e5a | -6.0341 | -47.5797 | 2025-07-29 00:00:00 | GOES-19 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| bc0c5316-f7c0-36ca-a648-40a681d65e49 | -5.858 | -44.2319 | 2025-07-29 00:00:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 38b6330e-a40b-3f39-92ab-dae7d887390d | -18.4486 | -54.6674 | 2025-07-29 00:00:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 203.4 |
| 0eaa792f-260a-3ce1-9b80-5892338c423b | -11.7508 | -48.1825 | 2025-07-29 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 4a1e7098-c1c9-3933-918b-068dd5bc9348 | -15.8221 | -41.89831 | 2025-07-29 00:05:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 0738967e-b45a-318c-9fc4-cc5a94b9dbc4 | -15.12262 | -45.32804 | 2025-07-29 00:05:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 5e40b5d2-d585-3ab7-8e41-dc40de281fc4 | -15.72785 | -43.24057 | 2025-07-29 00:05:00 | TERRA_M-M | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 26.8 |
| df4b8198-739d-34b1-8602-fa94216955ba | -15.82072 | -41.88764 | 2025-07-29 00:05:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 25.0 |
| f06d5fe4-3860-3fad-acfa-55b3c77208ed | -15.73476 | -43.23382 | 2025-07-29 00:05:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 11.7 |
| fddbae09-6dda-35cf-b87f-a5d2c02adfbb | -15.12463 | -45.34544 | 2025-07-29 00:05:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 163c6dca-741e-3093-acdf-befca52f026c | -15.72945 | -43.25338 | 2025-07-29 00:05:00 | TERRA_M-M | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 8.5 |
| f52050b3-783f-33b9-be1f-c056e7868ccb | -16.54824 | -40.50404 | 2025-07-29 00:05:00 | TERRA_M-M | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 89b89980-bbf3-3b01-93a8-4da85429caea | -15.73628 | -43.24663 | 2025-07-29 00:05:00 | TERRA_M-M | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 29.4 |
| 3f009a4c-8a3f-3222-aed6-1810b15dd697 | -8.88293 | -47.33746 | 2025-07-29 00:07:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d734ba82-1694-361b-901d-869322007cb9 | -14.34884 | -47.09402 | 2025-07-29 00:07:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 6edf4351-3f7c-3464-9c91-a43bd140bcfb | -7.80492 | -46.57532 | 2025-07-29 00:07:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 7bd64eaf-b92c-3069-bb8b-add8b9fb4004 | -7.61383 | -44.8254 | 2025-07-29 00:07:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 95bbcd5f-8732-3836-a018-c2ef7528bc6a | -7.24563 | -43.07003 | 2025-07-29 00:07:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 45.8 |
| 8c4552b8-21ae-3964-85df-c335f37ea3a6 | -11.42028 | -45.12851 | 2025-07-29 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7dfc6309-3a75-3528-b1b5-1af6a0f3fefb | -10.00373 | -48.13271 | 2025-07-29 00:07:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 649a5750-975a-3938-9ae9-0526d58bc6b5 | -7.85611 | -46.73191 | 2025-07-29 00:07:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 271.5 |
| d1b2888e-406b-309d-9fdb-367d2ea72114 | -8.5088 | -43.31393 | 2025-07-29 00:07:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.9 |
| efa8db3d-ad4b-38f5-9e37-e44c471fb064 | -10.22418 | -46.46465 | 2025-07-29 00:07:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 57b3a9dc-f89a-3bc3-a672-67ee4ac49805 | -7.92501 | -44.08818 | 2025-07-29 00:07:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 40027a29-b208-3d6c-b1f8-4cc17b0002f6 | -7.44983 | -49.38334 | 2025-07-29 00:07:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| bf0a79d8-4853-343c-a3d1-3e40c4f3ba81 | -11.73384 | -48.16694 | 2025-07-29 00:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 79803449-10b6-36f2-872c-4abfa0b478e0 | -14.50561 | -46.54113 | 2025-07-29 00:07:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 2e953599-3e52-3c45-82d4-5110ad3729a4 | -7.81178 | -50.21542 | 2025-07-29 00:07:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 6526e6d9-3059-32f6-bddb-43079d710a17 | -14.49493 | -46.54818 | 2025-07-29 00:07:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 27.5 |
| a7dd3999-dae2-324f-a564-64e061b2967f | -11.75093 | -48.19072 | 2025-07-29 00:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 295e59b3-4b28-36e9-bfbe-591809308659 | -7.81482 | -44.96134 | 2025-07-29 00:07:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 71d9afdf-dfdb-35bf-8264-b6de4e76d26a | -10.52217 | -42.5504 | 2025-07-29 00:07:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| d5653553-56f7-39b3-b0c6-ac579f9a7527 | -8.95081 | -46.75317 | 2025-07-29 00:07:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| f83a8db3-4de6-3053-8283-9fd6e4b26e32 | -14.49255 | -46.543 | 2025-07-29 00:07:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 7a2502f6-c1cc-38d2-a4fb-38ce4b9fa1c9 | -8.82271 | -43.92918 | 2025-07-29 00:07:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 4dd74882-2054-370c-8bb4-15cadc2475ef | -8.94248 | -46.74782 | 2025-07-29 00:07:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| c964fc6a-0010-37e8-9bc6-5baa70438fd7 | -8.51957 | -43.3228 | 2025-07-29 00:07:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e2255cde-b8c3-3461-99c4-e4044da8bd1f | -8.51014 | -43.3241 | 2025-07-29 00:07:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 3388a09e-46c4-30a2-8426-bfb1964e88f6 | -7.09676 | -44.38053 | 2025-07-29 00:07:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 9b7eb216-61dc-33f5-bff3-ca2bfdc06dbd | -11.97799 | -46.9547 | 2025-07-29 00:07:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 3f9d50f1-af74-3f61-b41d-2cc1b7c77386 | -11.74483 | -48.17089 | 2025-07-29 00:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 164.9 |
| a7b03b5b-c728-3527-bb81-0027e465f71b | -13.0025 | -44.88346 | 2025-07-29 00:07:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 4e7bdd7d-15fd-35fd-886a-87fadd9c5835 | -9.23284 | -43.15583 | 2025-07-29 00:07:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 33.3 |
| 5a71b8fb-101f-3ace-b2fc-83c55a6a5f84 | -11.27047 | -44.65704 | 2025-07-29 00:07:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 85076a7b-fcd3-3fb7-abd8-824157d083f6 | -14.35833 | -47.11057 | 2025-07-29 00:07:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 8d327d27-1532-3867-98cc-132bc0cc0d44 | -12.99313 | -44.89962 | 2025-07-29 00:07:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 9f4e93e1-6283-38f1-8ce0-a3c6e8831d1d | -11.26878 | -44.64351 | 2025-07-29 00:07:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 30417b94-19d0-3355-b958-5dc6e1eb4e35 | -9.99795 | -48.14011 | 2025-07-29 00:07:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 9f58e182-89b7-3328-be20-37d290d7335a | -10.28047 | -46.92727 | 2025-07-29 00:07:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 593452ba-bd24-3c4c-ae0a-165bf67e2db0 | -8.95686 | -46.76424 | 2025-07-29 00:07:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| dad3c96a-624a-3768-a3af-56ba9ef737fb | -11.43138 | -45.12686 | 2025-07-29 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 199.6 |
| fcae248a-1319-3e19-add0-d62f7c4e25d7 | -9.3948 | -45.50109 | 2025-07-29 00:07:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d7c8e49a-fd26-3453-a2b2-fa0626b84114 | -7.9446 | -44.08549 | 2025-07-29 00:07:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 99942f3b-c158-39a0-af06-bb1ed194f2c1 | -10.90152 | -45.8318 | 2025-07-29 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 082e8eb6-0190-3db1-9884-3d949989c449 | -11.74811 | -48.16507 | 2025-07-29 00:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 41633a5a-b5eb-35f4-9ecd-64772ea8115c | -7.93627 | -44.09777 | 2025-07-29 00:07:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 38.3 |
| d7d4065c-a9b6-3b97-bf94-a297c3001470 | -14.31929 | -48.63807 | 2025-07-29 00:07:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 4c833ea5-2fd9-350e-b3cc-779fa48321b4 | -8.51823 | -43.31263 | 2025-07-29 00:07:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2e23164d-ebe4-33e3-a7bd-f73e5db68336 | -11.74781 | -48.19636 | 2025-07-29 00:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 253abb08-f50a-303a-88f3-42d4c9ad181d | -13.00436 | -44.89838 | 2025-07-29 00:07:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 408a8cff-3f52-3ec3-b65a-bc854132231c | -7.46827 | -49.40187 | 2025-07-29 00:07:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| a2f5d8bc-163a-3235-8242-b5418d33a112 | -7.85401 | -46.71503 | 2025-07-29 00:07:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b9507944-a7eb-3fa8-8845-388d4a255ced | -9.39295 | -45.48664 | 2025-07-29 00:07:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d64d0cc9-3003-3321-af27-8e456de2f06e | -11.43322 | -45.14175 | 2025-07-29 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 033f79cd-0d53-3f6d-be02-a821c21667f8 | -14.01175 | -44.62248 | 2025-07-29 00:07:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| cb225e15-d173-347e-ae9d-b2f754fbc17c | -14.49247 | -46.52714 | 2025-07-29 00:07:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 31d6c6d7-8c9d-3275-8f97-f2cf75918d6b | -9.36853 | -45.74482 | 2025-07-29 00:07:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fc9a4237-66fb-384c-807d-5c9234738532 | -11.7366 | -48.19239 | 2025-07-29 00:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| f79d716c-cab2-3cc1-866d-1469b5bdd940 | -9.18907 | -43.15762 | 2025-07-29 00:07:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| b9bcc438-f02d-318c-add7-1d59429107d3 | -14.3514 | -47.11667 | 2025-07-29 00:07:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 3484c48c-63eb-3f94-8631-51ceb3581d68 | -7.93481 | -44.08686 | 2025-07-29 00:07:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| d509f1c5-f196-3b16-a4cc-31ff61e50dcb | -7.46802 | -49.40847 | 2025-07-29 00:07:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| a22ad825-a3d9-3651-93ca-bf511d42f74e | -7.25483 | -43.06878 | 2025-07-29 00:07:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 0fc8c33e-0483-3735-88cd-192df233de68 | -7.24432 | -43.06045 | 2025-07-29 00:07:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 32.0 |
| f3dce6f1-ef27-3631-8d2c-873ddc1f2f20 | -7.45329 | -49.41045 | 2025-07-29 00:07:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 201e0019-f10f-3f38-89b5-28e225846f2c | -13.00403 | -44.89273 | 2025-07-29 00:07:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 397dc913-212b-3b7b-b241-416e3613d1fe | -9.99507 | -48.11623 | 2025-07-29 00:07:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 32.7 |
| da8667eb-cfb8-31ca-81f8-41cc187bd63b | -7.85823 | -46.7489 | 2025-07-29 00:07:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| e18431db-d68c-3912-a544-000a8f56598b | -7.45354 | -49.40387 | 2025-07-29 00:07:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 98e50801-9d4a-35d0-9e39-0f5a1789597b | -14.3559 | -47.08772 | 2025-07-29 00:07:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 34.0 |
| cd9c71ef-42c5-3d22-b3ca-37c9ad542e87 | -11.98671 | -46.70228 | 2025-07-29 00:07:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b9053614-f55d-3d7a-b859-0070a3f1b8d2 | -8.9547 | -46.74652 | 2025-07-29 00:07:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| d6a6c785-ed2b-39aa-be3f-c36533d17697 | -7.92646 | -44.09911 | 2025-07-29 00:07:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 80bf9eff-d366-37e3-92fe-fe3ca30d7082 | -7.92356 | -44.07731 | 2025-07-29 00:07:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 0f155245-4d96-3198-bde2-3a02363c2fc8 | -14.32262 | -48.64288 | 2025-07-29 00:07:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 31.4 |


[Clique aqui para ver as próximas entradas](README2.md)
