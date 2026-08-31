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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 347c8366-0cd8-352f-8be0-7bfe1eb1edee | -7.63559 | -46.72287 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8361324e-9af8-3a5b-bad7-ffd3d430b550 | -8.83315 | -47.95138 | 2026-08-31 16:50:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1f86b37d-deb0-32fe-9e54-2488bcf2204f | -10.8535 | -45.33047 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 8e9a9c3b-2807-3b94-ac70-4366bfe3991d | -7.99994 | -62.02702 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 466d2691-0e2e-310a-a488-9b0e1a259abb | -12.10284 | -47.14552 | 2026-08-31 16:50:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 47604642-4710-3893-98e3-6381a3ce5f16 | -6.95932 | -56.43964 | 2026-08-31 16:50:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| bbdf4a8c-be93-3742-9b52-a63bee351b29 | -12.09802 | -45.00726 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 257.0 |
| 71a8292b-a137-3532-84ad-c913392d39e0 | -10.12724 | -45.8381 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6c055780-0c2b-380a-af02-2b6edc557ecb | -10.85986 | -45.37114 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0dbd9c7e-8f98-3fd7-b524-1a44e5a4c327 | -9.79753 | -60.17601 | 2026-08-31 16:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b3aaf0a8-97f9-3159-9661-d6ce36dcfad7 | -10.06083 | -48.38906 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 52cc09bc-f6f2-3e50-b26e-acf7b00284ac | -11.20425 | -45.05922 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d4364b75-0a37-3ceb-affe-61b9533b9b22 | -10.5472 | -43.92373 | 2026-08-31 16:50:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0421b72b-d8d5-3f55-bb3a-9be4ce0c2c0b | -12.96218 | -45.93922 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| fce8290e-0a4c-35cc-97be-a9e7399d8e8a | -10.10265 | -50.29137 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| dfad66ae-4c60-3eef-8f54-39a94875d15a | -7.98102 | -46.53203 | 2026-08-31 16:50:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d0ac4a15-8582-32d0-9b6d-4dfab3d2856f | -10.68929 | -46.26161 | 2026-08-31 16:50:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6a064109-8567-3886-9a66-b6179098fe65 | -7.09392 | -45.79931 | 2026-08-31 16:50:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| ccfc8664-b726-3412-bc9a-65cb99e786bc | -10.84738 | -45.31491 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| fdf02710-bff2-33fb-886a-11a6129625f5 | -10.11804 | -45.84771 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 264b2cc0-896e-3900-8820-e19437a729e2 | -7.56415 | -60.48061 | 2026-08-31 16:50:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d2dc090f-7d05-33f0-8050-e191f9e57d77 | -11.32413 | -45.19585 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| aa3d1af1-202d-38d1-9485-f8953091093e | -9.20934 | -51.56209 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1c783610-4b35-36e3-8735-28f50805b2de | -13.41531 | -51.38813 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 87810bb7-f0ee-3022-8219-c15b2dbf08d7 | -11.22011 | -45.11182 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 443aba7e-572a-361e-8ce3-3edbf8dfcb91 | -7.41864 | -44.24736 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 10549999-d1b8-3c5f-bf7c-0603ef64fda8 | -7.5579 | -60.48151 | 2026-08-31 16:50:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 112c28b7-01e2-38a8-b3e0-bd91484014d4 | -10.11678 | -50.31626 | 2026-08-31 16:50:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 9bc0a08e-e193-3916-9d3c-7b753b667d59 | -11.15803 | -45.04572 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| bbaf7316-1a97-39bd-835d-c8f6cd8236c8 | -8.64325 | -47.31685 | 2026-08-31 16:50:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 5fdba023-220d-3df9-8617-637585b410af | -11.68773 | -54.54832 | 2026-08-31 16:50:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| bbe7d89e-02f6-3017-8d3c-62c40d8c5a10 | -9.22205 | -59.58305 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 27c85e8d-5330-32b6-948b-7cde72501f59 | -11.92984 | -45.08886 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0da0d05d-5bea-3376-8f72-1371362174e6 | -9.96853 | -46.78165 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1bdf15a9-5ce1-3cb1-b6c0-ef1d5e09f755 | -8.41219 | -44.97967 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 68f890d8-20df-35f8-bb54-35bf6fd8d6fa | -10.70255 | -48.21415 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1aff502-b79e-3300-8b68-d4f7a9885338 | -8.50324 | -55.31107 | 2026-08-31 16:50:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 22c9d258-6c12-3b6b-af63-79564620df79 | -10.40368 | -40.15362 | 2026-08-31 16:50:00 | NOAA-20 | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| bf345fea-3393-3ab6-98e1-44516af17dab | -6.92071 | -39.56505 | 2026-08-31 16:50:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 17077933-7db6-3640-aad6-620027831b89 | -13.57049 | -55.14867 | 2026-08-31 16:50:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 4f2024be-4f30-3f06-a189-9ee0690f8e44 | -11.25146 | -45.10222 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 375af3de-9fd3-3fe7-a594-0e8a16b439f9 | -7.22729 | -42.75813 | 2026-08-31 16:50:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f07d689a-3aa5-3c90-b692-57a43c8adcf3 | -6.41175 | -45.42646 | 2026-08-31 16:50:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 03a6ec45-d9f4-3b61-a2b7-b7d819562ebe | -9.67653 | -50.84407 | 2026-08-31 16:50:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| ae641b73-6a24-385a-8fa4-70430a1639ac | -9.20763 | -59.41611 | 2026-08-31 16:50:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5e8a2f20-fedf-3848-83af-9fba0fbf72be | -7.95147 | -44.26092 | 2026-08-31 16:50:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 71e58f6e-73cd-3e59-b430-916d9be30ccc | -12.91724 | -45.8546 | 2026-08-31 16:50:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| bdc2d8e8-16b4-32b6-830f-40a00c5092c3 | -8.38983 | -46.45936 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b73cf2c4-46f7-34c3-ab01-50b344c066d7 | -9.68793 | -48.12437 | 2026-08-31 16:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| bfa8d87d-9f27-3d5d-bec9-da0680a2f074 | -6.67997 | -52.87064 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0d88b3ce-a980-3215-ad7f-1aa655eb7fc9 | -10.08136 | -46.63176 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| be09e62d-1bed-3f91-ba14-40a4a94a667e | -11.68715 | -54.54385 | 2026-08-31 16:50:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2072f6b4-8cb1-34af-85f0-163c82692b9a | -10.08421 | -46.24865 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| f7bf6dac-a009-3969-a912-45bd2735f4f2 | -12.11181 | -45.02514 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| efd1c900-b283-3a8b-83e3-48427a90464b | -10.02365 | -46.15701 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 55823fe6-6a22-3192-a8d0-da9e9a8291ce | -7.49613 | -44.44809 | 2026-08-31 16:50:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 26f711fb-f44e-32a6-a482-0b3aecde4122 | -11.33299 | -45.16077 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 8e578689-ed93-3417-a12f-4603a9a905a0 | -8.95209 | -62.36804 | 2026-08-31 16:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 0eab0c3c-9853-3516-8682-c516347a5e9d | -8.75278 | -46.47083 | 2026-08-31 16:50:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3867a508-9c0c-30e4-89cb-e3df204dcdad | -8.08126 | -45.46192 | 2026-08-31 16:50:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5115d9a-2058-3bea-891e-5f016a8c36ff | -11.22368 | -45.11128 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5e06e71d-0c1e-3d56-ada9-1564c049752e | -9.16276 | -41.18788 | 2026-08-31 16:50:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a48dd962-d525-3348-b8c6-c472e6283273 | -7.64998 | -46.72448 | 2026-08-31 16:50:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d9344838-cbed-3a63-bc8d-78955e4a8157 | -8.88154 | -46.02227 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c4f7a152-b430-31e0-b314-819fe85b2110 | -11.25568 | -45.10577 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7fb5a803-18d5-3706-a2b8-aa69796bd1c7 | -10.98105 | -48.41724 | 2026-08-31 16:50:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b26bfdad-7944-3c1c-afb5-46639470faa8 | -6.4029 | -45.43112 | 2026-08-31 16:50:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| b6d42f46-c8b8-3845-8060-bb75255047d9 | -10.86116 | -45.37903 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2ce1602a-4e7e-3f9e-91fa-ccaf9aa3b130 | -11.04857 | -49.68394 | 2026-08-31 16:50:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3e850b9c-544c-3cf7-a24a-001b2bab101d | -11.36594 | -45.18455 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3bbddbc7-5ac5-30a2-8333-f8a8207583d7 | -9.19246 | -51.55944 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 33a347f2-dd1c-3c5c-82d4-c2ccd8d95b50 | -10.00204 | -46.41609 | 2026-08-31 16:50:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 23f1191c-89c9-347e-86b8-ff0618b6934c | -10.0836 | -46.62384 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 692e6a80-c426-3a38-b02b-5a00419b3704 | -8.36331 | -57.67318 | 2026-08-31 16:50:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d4dfc34-cafe-33cd-a769-1fa62a1386f4 | -7.93317 | -61.34301 | 2026-08-31 16:50:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| fea90738-34e4-3e5e-b1a5-82a8a36872b7 | -13.95872 | -54.39843 | 2026-08-31 16:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5e5a983d-b69e-3ec0-b031-f7d8a31e578a | -6.41047 | -49.93319 | 2026-08-31 16:50:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| ea982bdc-9a7e-3ea1-a554-c1ada78164e4 | -11.22221 | -46.10863 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 4d0984eb-10f3-369a-8868-1d1fb3880e09 | -9.47534 | -57.02205 | 2026-08-31 16:50:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5920be51-a96b-3d79-9c60-900c30746b56 | -6.83689 | -52.42848 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 28c453e2-06d1-3674-bc77-9b52eb3be787 | -8.05285 | -47.27876 | 2026-08-31 16:50:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 93081b38-32cf-3483-b9bf-1fa8d9b4ebcf | -7.52598 | -60.48098 | 2026-08-31 16:50:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c9d7504a-bb22-3563-9291-a54089f386db | -8.72356 | -45.37979 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d1582087-92c8-3565-bddf-8e0962991b41 | -6.69311 | -52.88255 | 2026-08-31 16:50:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 40a7a1ce-fe8f-346f-b557-ca6f609ec766 | -9.44967 | -45.67883 | 2026-08-31 16:50:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 1b7f3535-1311-3b5c-b26d-b7f73c2c026d | -11.82062 | -46.77129 | 2026-08-31 16:50:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b92e7449-3500-3a67-b7eb-26920acbf8cd | -5.66136 | -43.55948 | 2026-08-31 16:50:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| db60e12a-37a3-3051-8804-de6ce9deae53 | -11.48146 | -58.51812 | 2026-08-31 16:50:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 1a6c6ee7-6f1d-3a8b-8109-4f6aaf12e521 | -11.7152 | -47.64715 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 90b73a6a-73cc-3686-bef3-3441a355ac1e | -11.92627 | -45.08926 | 2026-08-31 16:50:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e40626b9-a533-304f-b9f7-9f9731c48b87 | -6.86914 | -42.88863 | 2026-08-31 16:50:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 089342bf-bfdd-3e28-9c95-39994a28b611 | -11.22522 | -45.09821 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 526a7df2-21fc-3e3d-8503-2b2568247295 | -11.16943 | -45.0481 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 9152cfa9-8239-3750-b4c8-cdd16965d0fc | -9.39401 | -60.56998 | 2026-08-31 16:50:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 32a8fb46-b085-3e52-9857-0aaf790cea02 | -11.67508 | -47.60675 | 2026-08-31 16:50:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a6dca02f-98da-336e-ac6e-204d0740a43a | -8.93056 | -45.04003 | 2026-08-31 16:50:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 028f701c-cb71-35ed-b735-be814e436ce3 | -9.30838 | -56.80155 | 2026-08-31 16:50:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbe643d1-68b1-32f4-8ecb-2f51136341fb | -5.6035 | -44.00202 | 2026-08-31 16:50:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| dc8007a3-9952-39e9-8459-dfbaf5742d17 | -11.25094 | -45.14442 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4eb28393-4fd5-347a-845f-0c42f7b70a40 | -11.21587 | -45.10821 | 2026-08-31 16:50:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |


[Clique aqui para ver as próximas entradas](README158.md)
