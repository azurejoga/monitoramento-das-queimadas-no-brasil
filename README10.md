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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08da97f8-2d00-3b34-aae6-868b7822db6b | -2.72623 | -46.18235 | 2024-12-24 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78449421-a465-3cd3-bbfa-357f9e178522 | -2.81822 | -45.93429 | 2024-12-24 04:36:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ada94e4b-9939-3c90-a8f8-6dcf54b9f9fd | -1.70433 | -46.43002 | 2024-12-24 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0248a441-c54b-3184-a4a0-f54f53ff8cbe | -6.31317 | -43.46858 | 2024-12-24 04:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 595af0d1-af47-3372-969c-e829f522167f | -2.99157 | -40.38853 | 2024-12-24 04:36:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 45617078-e28e-3098-93be-fa414e50898b | -3.34909 | -53.21196 | 2024-12-24 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7d47b86-0860-35a9-a3e8-08cdc2b7c6a7 | -2.75485 | -45.71434 | 2024-12-24 04:36:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd5f1ae5-4aef-33c0-aa08-575eacdd99f4 | -2.19174 | -45.68196 | 2024-12-24 04:36:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 096314a8-90a0-3194-b9a2-c3e2763d269d | -4.30083 | -40.70201 | 2024-12-24 04:36:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d587a35f-9d76-3cee-9063-d23b98a980f6 | -2.81531 | -45.92981 | 2024-12-24 04:36:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e310adb-3159-3038-83b6-e6d0c41c4192 | -2.64068 | -46.1031 | 2024-12-24 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f24bce0-c316-377c-9fed-d6ac4de576b9 | -6.11823 | -43.01612 | 2024-12-24 04:36:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c5f5e31b-7f26-3d17-9b42-4f0fd03b7df4 | -2.1158 | -45.49586 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ba8163d-8565-305d-b0cb-98da96c1f589 | -2.57946 | -51.92258 | 2024-12-24 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e11fd2f-00e5-3100-a9fe-2381546b929f | -2.60527 | -45.90776 | 2024-12-24 04:36:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf7849e8-c01e-3827-a081-b816bf7f45ff | -2.51068 | -54.19051 | 2024-12-24 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3bb8199c-d130-378a-8a6c-dbb829d1edeb | -1.58734 | -53.34241 | 2024-12-24 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b03a553-8106-3060-b48f-4dff953a226c | -3.21939 | -45.4461 | 2024-12-24 04:36:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91e69bde-8ead-3adc-9520-a7142d75ffdd | -3.03173 | -53.89545 | 2024-12-24 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 045cdca3-2fb9-39fb-8917-1e3302538b40 | -6.97043 | -43.5489 | 2024-12-24 04:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2ee46fbd-6378-30e8-ab9a-900814a41a50 | -0.96154 | -46.78377 | 2024-12-24 04:36:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a65f084-e565-335b-ab18-631407dc67cd | -2.7941 | -51.77168 | 2024-12-24 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 338279fd-1393-37c0-afd0-d1dade63fb6d | -2.35648 | -54.61885 | 2024-12-24 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 141bf747-a6bd-326e-9e16-c69c5fb1e80e | -2.58346 | -54.24889 | 2024-12-24 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 735627cd-4d11-379d-9b9e-bb5998925737 | -2.34794 | -45.58651 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 79f13668-7daa-3600-8a96-bdabf85eb65c | -5.98698 | -45.39686 | 2024-12-24 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 067811fb-1310-31b8-bcea-b839e597acc3 | -4.52261 | -45.82685 | 2024-12-24 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2422b0ce-140b-3e03-8636-b8686f5d53c1 | -1.71 | -54.49203 | 2024-12-24 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 05c0988d-f2e3-31b0-b66d-36c8e1ecfbc3 | -3.18822 | -45.97502 | 2024-12-24 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fefa024f-6001-39c1-8a37-b0636013b275 | -6.94589 | -43.53696 | 2024-12-24 04:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f64e7f9-7780-3208-a4ec-71be4be6fd46 | -2.34438 | -45.58597 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f937704d-4cb3-3e7c-8400-38ad89636bcb | -3.58381 | -59.6152 | 2024-12-24 04:36:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd2c2a4f-dd2f-3f73-95cc-4956fb13ad01 | -2.09227 | -45.36321 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1c22e6b-447f-3e50-bd4c-3666bd1bd0ea | -5.99074 | -45.39744 | 2024-12-24 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4cbeccd-dce6-3738-9774-01fb71939cfb | -5.53542 | -42.85397 | 2024-12-24 04:36:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 801a80bd-3ab8-3dba-b574-364aab550590 | -3.18762 | -45.97899 | 2024-12-24 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76c135b1-9cba-34f9-84ee-153a9ee5b42e | -3.44966 | -52.86337 | 2024-12-24 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b358116-46a7-35d5-87d8-93bb0ad59a24 | -5.97946 | -45.39582 | 2024-12-24 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 896fc8c1-762f-3dfa-857a-f9918c972810 | -3.18726 | -45.98056 | 2024-12-24 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 089bc711-e564-3643-8f86-f0297abfe8dd | -6.95445 | -43.53831 | 2024-12-24 04:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bda77373-e566-3208-a4dc-69d0ad571d0c | -2.3515 | -45.58704 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 7ba1192f-d53b-3397-97d2-5dc2bfaadb5a | -1.58372 | -53.39273 | 2024-12-24 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e40f3d6-fdc6-3b7c-86d0-be1c65f287d6 | -1.71065 | -54.48786 | 2024-12-24 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| affe84c8-47cd-3e42-9571-f579832c244c | -2.64536 | -46.09595 | 2024-12-24 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b27d410b-f98c-36d0-aa84-30a7a167201c | -2.64476 | -46.09979 | 2024-12-24 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69263b25-45d7-3233-b19b-f705384e65ed | -2.89503 | -51.82036 | 2024-12-24 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93e0d945-e6c4-3c5f-b6b9-90eb438020b5 | -8.79516 | -49.79532 | 2024-12-24 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b763c118-493a-3ed8-9f85-4ea2f14500cc | -9.92473 | -59.90448 | 2024-12-24 04:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91cd19ec-f0cc-3c79-96b6-34c3378b8360 | -6.22774 | -55.62649 | 2024-12-24 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 1036307b-2bcf-3f4a-87ae-f2496c94d6f2 | -7.91344 | -61.54488 | 2024-12-24 04:38:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4a61e51d-4223-373c-a4b1-f406ea4f759d | -9.9302 | -59.90557 | 2024-12-24 04:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7144a1dc-bc15-3bf9-a827-0d510e0a9a05 | -12.55646 | -57.7571 | 2024-12-24 04:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa5b91fb-87c6-3efd-adad-bb3beb3a5d5d | -12.71342 | -40.21099 | 2024-12-24 04:38:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ec47cd94-cdcf-389c-baa4-8757a7b08fce | -12.78992 | -54.22331 | 2024-12-24 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44abee70-8c0b-338b-adf6-8e14317205a0 | -8.80346 | -49.80734 | 2024-12-24 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b203ee3-cbd8-3856-a2f0-67c87472a5bc | -12.78702 | -54.21835 | 2024-12-24 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08988786-0b28-303a-b557-dbe1b25425bd | -8.80622 | -49.81134 | 2024-12-24 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14682539-2a03-30d4-8d66-6f234bba7ccc | -6.22847 | -55.62219 | 2024-12-24 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 456ae92f-45f4-3b7b-ac00-d5bf59d86e92 | -9.15663 | -40.96728 | 2024-12-24 04:38:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5201353e-089c-3866-a500-0ec6789fbb87 | -8.79239 | -49.79132 | 2024-12-24 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 436fcebe-af0c-3473-bd88-25513cb3090d | -9.92952 | -59.90921 | 2024-12-24 04:38:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c7f5e32-6185-3573-9bdb-d3a178b693e0 | -10.59822 | -38.40934 | 2024-12-24 04:38:00 | NOAA-20 | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 946f9b34-a085-34e9-9ec3-b7bd3c955cc6 | -9.79898 | -47.97769 | 2024-12-24 04:38:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5141eee-ee9e-3bef-a8aa-1931ff0167a9 | -12.71293 | -40.2152 | 2024-12-24 04:38:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3e3604a1-b169-3725-8f40-c050cbffe9b6 | -8.80124 | -49.79985 | 2024-12-24 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf67aa4b-58b6-3814-aa2d-5a35f0078a99 | -12.55742 | -57.75464 | 2024-12-24 04:38:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75842aa6-d8fc-3e56-acd2-e272f96001ae | -8.79847 | -49.79585 | 2024-12-24 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86208ac2-228a-3ab5-86bc-db0b8db41c7e | -10.5976 | -38.41431 | 2024-12-24 04:38:00 | NOAA-20 | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 177ca6fe-385c-3e1d-aef3-d8dd60c6d242 | -12.71356 | -40.21155 | 2024-12-24 04:38:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b7ca5524-c626-3f7b-834d-30db060b6ff8 | -19.99846 | -54.74437 | 2024-12-24 04:40:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 44f47307-0404-3600-85ba-a4de5a5fdaea | -19.99914 | -54.7404 | 2024-12-24 04:40:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 741978b1-bb50-3d0e-8fe5-716ce614d6a7 | -21.4527 | -56.15588 | 2024-12-24 04:42:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6cb95a51-72c3-36fe-a0bb-54d03d498d1d | -23.98296 | -48.9171 | 2024-12-24 04:42:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fa3224f-afd4-33d7-b906-b1c04be0191a | -23.59351 | -47.44173 | 2024-12-24 04:42:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 09f35cb5-9ad1-364b-90cb-e605db172f2e | -23.59449 | -47.44091 | 2024-12-24 04:42:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b0124800-1113-34b5-833c-99328861b4be | -22.20942 | -54.37779 | 2024-12-24 04:42:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4bd545dd-24a7-33f0-8ade-1e78b66e49ff | -23.23711 | -51.28535 | 2024-12-24 04:42:00 | NOAA-20 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 44d47758-440e-3834-9cc3-4dfe60406d31 | -22.53984 | -48.81441 | 2024-12-24 04:42:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 077a1d45-18b0-3e15-8d1a-bdded1608f0c | -30.5567 | -52.8906 | 2024-12-24 04:44:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| e4e8a316-7d9c-3dd9-a59a-7100cfdf2b4a | -30.46144 | -56.39735 | 2024-12-24 04:44:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| b7271253-ceab-3661-aa59-40e43f0c0901 | -1.10341 | -54.17302 | 2024-12-24 05:29:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c8be61e-f419-3f3d-b1cc-4a0091a04898 | -1.58314 | -53.33438 | 2024-12-24 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 10c445f8-799b-3584-b366-1a11c1f4aa2e | -3.87235 | -55.98687 | 2024-12-24 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0dcacc5a-c55f-3524-9be1-cbf520510c78 | -3.58577 | -59.61628 | 2024-12-24 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 392ed624-6249-3874-b55b-798b6ed4958a | 1.00816 | -59.50211 | 2024-12-24 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d19d032b-92b1-37e2-b64f-eb99b681b9c5 | 0.5534 | -60.35835 | 2024-12-24 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35d939e2-a95c-3bda-95b3-1341311676e5 | -1.58722 | -53.3406 | 2024-12-24 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b65165f-94e1-39e8-a3e2-535ebdd00b9e | 0.5652 | -60.43383 | 2024-12-24 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cc900ed-8fae-3635-ac4a-2ee0c99f3771 | -3.58635 | -59.61255 | 2024-12-24 05:29:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dd1f13a2-261a-314d-a311-bbbf6683507b | 0.93057 | -59.57139 | 2024-12-24 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c375a199-3fdf-37fa-bada-0354d54513c0 | 0.56244 | -60.43777 | 2024-12-24 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2724edc-334c-340e-b310-1be922e274c4 | 0.36805 | -60.45733 | 2024-12-24 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fe3bf96-4948-3463-838b-c7ee15aea1b4 | 2.36642 | -60.15847 | 2024-12-24 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93ad2cdd-ee32-3997-9587-82bb7d0e024b | 0.55529 | -59.80524 | 2024-12-24 05:29:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d7a53ab-fde3-38e8-b03f-7f0a52da9e64 | -2.92526 | -51.58202 | 2024-12-24 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31b31e9c-60ff-38bd-821d-9820600ce23f | -3.15857 | -52.14299 | 2024-12-24 05:31:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02f83cd2-fa75-3b59-b8ed-fbae6ef32e0f | -2.37854 | -54.62074 | 2024-12-24 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2ad6795b-ad27-31c5-bfb4-2d721050175b | -2.76751 | -52.64886 | 2024-12-24 05:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f3dd223-3dbb-37c5-84f8-f8966e374e59 | -9.93284 | -59.90534 | 2024-12-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b89698ac-5b7b-3ffa-beb4-406cbbea5da0 | -1.51696 | -54.95505 | 2024-12-24 05:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README11.md)
