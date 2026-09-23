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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5936ea3-8ebe-3d2c-834e-a9ac5132c253 | -10.27526 | -50.52646 | 2026-09-23 06:40:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 8267beb7-204b-34f0-be1c-bf256b130ae2 | -10.28374 | -50.54167 | 2026-09-23 06:40:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 9b4e97f1-409b-3987-b934-7207bca05470 | -10.23169 | -50.21792 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| db28708e-ace8-3aa0-93fd-2f25b50c9cb0 | -6.62624 | -43.72197 | 2026-09-23 06:40:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3ffcd20a-df2c-3104-ab20-d51450879a72 | -10.24672 | -50.23914 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 980b652c-3bd3-34e2-b785-be000c2d2535 | -3.2259 | -46.94616 | 2026-09-23 06:40:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 54caeaef-5402-31eb-ac08-9843d0958897 | -8.77329 | -45.62951 | 2026-09-23 06:40:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 40b3feac-f295-3eab-b3bf-d1c5e1607f98 | -10.23631 | -50.23742 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 75eeaf6e-02d9-3148-9fe9-5fdbc32b2fe8 | -8.91108 | -45.94188 | 2026-09-23 06:40:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e6c946b3-e95f-3b06-be54-b06e3d01dc79 | -10.24059 | -50.21186 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 639cbc90-180e-303b-90c3-1c3ae051f8c8 | -10.25399 | -50.52292 | 2026-09-23 06:40:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| fce353ea-e92b-39d9-a67e-f7c39ad1379c | -6.66628 | -42.57397 | 2026-09-23 06:40:00 | AQUA_M-M | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 504f4183-fded-364e-981a-ef55e6c6fdcd | -7.41853 | -49.83147 | 2026-09-23 06:40:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| c8cc5252-152c-3f1e-96da-e239131af0d0 | -6.72039 | -44.14449 | 2026-09-23 06:40:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a89fee09-375d-3f71-92c4-ecc843da3b01 | -10.26462 | -50.52469 | 2026-09-23 06:40:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| cfa332a1-73d9-3a7e-85a6-92ee3e4534fd | -10.23374 | -50.20513 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 84b46fa6-8e1d-37b5-a95d-e9f162f1b0ce | -6.66789 | -42.56296 | 2026-09-23 06:40:00 | AQUA_M-M | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 94fe2678-6c71-3929-b117-bf225dfcff17 | -7.02345 | -44.6504 | 2026-09-23 06:40:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8476ca16-90f6-377e-b262-23cff380c054 | -10.25925 | -50.22807 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.7 |
| ee18a68f-f6a8-33bf-86ff-cba7c5a4e979 | -8.46478 | -48.68446 | 2026-09-23 06:40:00 | AQUA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f70075b1-b87c-3495-9b00-d3fae461ea34 | -10.02445 | -50.2238 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 1efb61de-e5d9-393b-88b9-37ceae250e6a | -6.60481 | -43.74237 | 2026-09-23 06:40:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| f15b5c0a-b97b-345f-be33-8de891420140 | -10.25098 | -50.21359 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7d16fdd7-e2a7-3df2-98a0-779d658669cf | -7.0323 | -44.6517 | 2026-09-23 06:40:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 5547e799-2787-3670-8e76-7e2ddc9c0b15 | -6.62345 | -43.74107 | 2026-09-23 06:40:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0ddcd607-d8da-3378-b94c-d6bf53066a27 | -10.25617 | -50.50951 | 2026-09-23 06:40:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| bd24f74c-1b14-38b7-ab83-4c0da4de586f | -6.60623 | -43.73285 | 2026-09-23 06:40:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| c0704d9f-a96a-3b84-a08a-70a7f7022c15 | -7.42061 | -49.81834 | 2026-09-23 06:40:00 | AQUA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1e6f567e-a7ff-35e7-b447-3db5c7d852df | -10.28054 | -50.52036 | 2026-09-23 06:40:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 60c1a191-934c-389e-8f96-e2b445be42a7 | -7.43277 | -49.83893 | 2026-09-23 06:40:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 3ee3aa75-90e0-3d78-a7dc-51e9f3f7993a | -6.61677 | -43.72461 | 2026-09-23 06:40:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 8e4a5362-a5fa-3efa-914d-3172e17d6385 | -6.33656 | -43.36867 | 2026-09-23 06:40:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 29e82fdf-9efa-38d3-931e-fe02f95d9a3e | -10.54019 | -43.98381 | 2026-09-23 06:40:00 | AQUA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 80d374c5-1a2c-3e44-9854-cf23352628b5 | -6.47941 | -43.59042 | 2026-09-23 06:40:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 64c29d35-27ac-3eae-be2c-f5830a604cbc | -11.35424 | -44.20417 | 2026-09-23 06:40:00 | AQUA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d31b35a8-887a-3be3-aa2e-7c395830d53f | -6.78789 | -48.67659 | 2026-09-23 06:40:00 | AQUA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5f58359f-f38e-3277-8bc3-d69d6ebc7acf | -6.98186 | -42.59907 | 2026-09-23 06:40:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 76cbfe3d-c804-3836-aaa9-30193faca6eb | -10.28279 | -50.50701 | 2026-09-23 06:40:00 | AQUA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 32d01a62-8f4e-3169-aaa8-2676fb76ea11 | -6.32745 | -43.92994 | 2026-09-23 06:40:00 | AQUA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7b03bab1-b123-3f81-a72d-c1339cb51de4 | -7.42929 | -49.83217 | 2026-09-23 06:40:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 87ce6eec-9bcf-32ff-bd9d-6ae0ce96fee7 | -10.03697 | -50.21267 | 2026-09-23 06:40:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| d887d7ac-86b3-3e8e-a513-84af78fb430e | -8.30829 | -54.76521 | 2026-09-23 06:40:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 1efd86eb-b698-365b-8f25-25f9daf5162c | -10.3933 | -51.84454 | 2026-09-23 06:40:00 | AQUA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 289aae5e-edf7-3b81-aa14-4e0911602495 | -11.29677 | -51.34557 | 2026-09-23 06:42:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 42d2b780-763a-357e-a4e5-50b079fa75ba | -14.68086 | -45.58729 | 2026-09-23 06:42:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 786d8f5a-efe3-31cd-8a44-660e5d6af931 | -12.12563 | -45.63885 | 2026-09-23 06:42:00 | AQUA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 134b22c9-c424-3179-bbe7-9ff970dc7867 | -13.30209 | -47.88792 | 2026-09-23 06:42:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e7520989-e5ca-3ac6-a4d7-24663ef454a2 | -12.41541 | -46.96377 | 2026-09-23 06:42:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 0dd41ed2-04be-3226-8ed0-fc96e099e434 | -11.28062 | -51.37339 | 2026-09-23 06:42:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 1f4d5c5c-7fb6-3f83-a647-aca275b65c8d | -12.40664 | -46.96241 | 2026-09-23 06:42:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5903a25b-c096-3a4f-bc22-789b723e140e | -13.29026 | -47.89813 | 2026-09-23 06:42:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1eb98e83-5078-3922-9bb2-e0947cd240ea | -11.45514 | -47.39099 | 2026-09-23 06:42:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 331385d8-f23e-31b7-87ef-13fa8f6c1fb3 | -12.4127 | -46.98162 | 2026-09-23 06:42:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e920d292-1ed9-369a-9646-27c6a538df31 | -11.99153 | -52.44731 | 2026-09-23 06:42:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 07e7a64e-57a2-36eb-8d51-ede5e252066a | -12.50816 | -46.96553 | 2026-09-23 06:42:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3c783e69-a163-3472-a1c3-6f34cde39faf | -14.66268 | -45.58459 | 2026-09-23 06:42:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 993c43f3-76f2-3b21-a602-033be313691b | -11.11649 | -48.31047 | 2026-09-23 06:42:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| e27f07ea-4de8-3149-adde-34afe414f10f | -12.3186 | -50.21558 | 2026-09-23 06:42:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 992846fc-d040-336b-9945-7be924e9dfb6 | -12.40529 | -46.97134 | 2026-09-23 06:42:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4fb5c066-4211-3234-826a-bc59096fd26d | -11.98857 | -52.46484 | 2026-09-23 06:42:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| e4a309c4-b43b-3ede-ab63-6ada8e618b77 | -11.29177 | -51.37529 | 2026-09-23 06:42:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 0617f0f8-4299-3c3e-bf41-00aeb6d6998a | -11.72868 | -50.78209 | 2026-09-23 06:42:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8d473a4c-58b6-398b-b8c2-128b0a86a836 | -12.41406 | -46.97269 | 2026-09-23 06:42:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 4d5dcbbc-2b31-3f4b-8f63-7020ed0e382b | -11.118 | -48.30093 | 2026-09-23 06:42:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c458d1a8-7b67-31b9-b6c0-1d0e1ab70778 | -11.12759 | -51.051 | 2026-09-23 06:42:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fc1b88f7-90e3-34a8-b05c-4d516cd6c1a2 | -13.06052 | -47.40744 | 2026-09-23 06:42:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b3c534c2-2a21-3242-92f6-099de7dfd5f5 | -11.67072 | -50.97337 | 2026-09-23 06:42:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 10fa3273-8e6e-369b-bb6a-9a91cbb342a6 | -14.6613 | -45.59434 | 2026-09-23 06:42:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d226de95-8677-3832-8570-eaa52089ec3d | -13.06932 | -47.4087 | 2026-09-23 06:42:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7021006a-4539-386b-95cb-8340f53f9ad0 | -14.68994 | -45.58865 | 2026-09-23 06:42:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| d3128156-09ca-33e4-86c1-0ba4a771c86b | -14.6236 | -45.66217 | 2026-09-23 06:42:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 839a91ca-a63e-30a5-9bf1-a323353f825f | -11.63625 | -50.98161 | 2026-09-23 06:42:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 7b2dc964-0275-33ef-a515-3eef32a882c0 | -11.98343 | -52.45293 | 2026-09-23 06:42:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| b80df23c-e2bf-3ae9-8393-94922266610c | -15.62772 | -43.52579 | 2026-09-23 06:42:00 | AQUA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 2dcbfb9c-cdd2-3804-a880-3ca3262c9ab4 | -14.63265 | -45.66352 | 2026-09-23 06:42:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 27342a59-c644-3b86-b1c2-2c9bcca05193 | -14.73397 | -45.60517 | 2026-09-23 06:42:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 45f016c4-8908-3d92-a017-71d85465a172 | -11.66846 | -50.98711 | 2026-09-23 06:42:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b6685db6-7486-3103-b938-86f50177f7a6 | -11.09355 | -48.34058 | 2026-09-23 06:42:00 | AQUA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 58206bfd-4dbc-3987-9ff2-0279e47df618 | -11.12566 | -48.31168 | 2026-09-23 06:42:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 62e52be5-c327-3ed0-a568-d3e6da9717bc | -11.9954 | -52.45505 | 2026-09-23 06:42:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 42396809-46a7-3882-8130-13a4062faa13 | -11.63395 | -50.99538 | 2026-09-23 06:42:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c0c27c89-7776-39d5-a3eb-355f34f950e2 | -14.2956 | -43.1827 | 2026-09-23 06:42:00 | AQUA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 9b251d1a-9062-32e7-a596-722912d0fd3d | -13.2208 | -47.02532 | 2026-09-23 06:42:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad03e7e0-9ddc-3638-a7d5-c4e3ec46f197 | -11.64699 | -50.98344 | 2026-09-23 06:42:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 660d5089-611a-3f2b-9d42-b60882078a09 | -11.12442 | -51.05832 | 2026-09-23 06:42:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b3c7c3d4-3b23-356f-bd11-11c48a881a47 | -11.64083 | -50.95417 | 2026-09-23 06:42:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 6ff5b291-0b41-39f1-aa00-43a24659a47f | -11.70862 | -44.50725 | 2026-09-23 06:42:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3da0a869-9f41-3989-84c5-13bdc0b7084a | -11.42831 | -47.37162 | 2026-09-23 06:42:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f041bb1c-a135-3368-9926-290a5902829c | -14.60061 | -45.62917 | 2026-09-23 06:42:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 66831c7e-b87b-36c8-a61e-cd0766aa652c | -11.28314 | -51.35854 | 2026-09-23 06:42:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 35.6 |
| b19523a1-c1cc-39f8-8d27-50cfdceb2a74 | -13.29168 | -47.88895 | 2026-09-23 06:42:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 29a8be4f-aed2-392f-873a-5c0e72b62f50 | -15.62943 | -43.51284 | 2026-09-23 06:42:00 | AQUA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 94.1 |
| a0485fb7-cb4e-30fc-b4c9-92d97ff352ff | -12.41677 | -46.95485 | 2026-09-23 06:42:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ff13aee9-955b-37a7-bac7-c522871f0934 | -13.42568 | -46.2733 | 2026-09-23 06:42:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9fe9f529-fab7-3495-bbe0-a11e0074e704 | -11.29427 | -51.36042 | 2026-09-23 06:42:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 455a0815-3593-32bd-9ba0-b6be862ed743 | -8.62012 | -66.73264 | 2026-09-23 06:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b12f58b6-dd73-325c-80da-bdc82879e0d8 | -8.76808 | -72.77294 | 2026-09-23 06:46:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46673039-6b3b-3faf-8412-00eedfc7043a | -9.55929 | -65.98478 | 2026-09-23 06:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 721f703f-86c7-37bc-8b78-39d131b8709b | -9.55494 | -65.98988 | 2026-09-23 06:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8724d6e4-a508-35ec-9b46-43692f60b05c | -9.55563 | -65.98409 | 2026-09-23 06:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README128.md)
