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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f162fa3-8e54-33bf-8b19-65b266dc2182 | -10.30385 | -63.39148 | 2026-10-05 17:34:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 05fa45b8-8ffe-3d56-b6e0-73f06da07034 | -3.86377 | -55.8256 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76b33d30-6a13-31c1-b4c4-977926688a21 | -3.68224 | -59.62694 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 977fbad1-9407-346f-8c53-eb4ddb7ceb5b | -2.78847 | -56.97558 | 2026-10-05 17:34:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 25a2b30c-369c-3d81-bd3c-93aa985bfbf6 | -4.11644 | -54.42739 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 10e95e4a-0769-37b8-97a0-dac164535aad | -7.78814 | -70.01258 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 94faca09-acb2-3471-ba29-b2130cb55212 | -11.30626 | -47.78056 | 2026-10-05 17:34:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 48a6ff78-8360-35df-a035-db24a742f2ac | -3.54687 | -60.51581 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 252230f3-00ba-3f74-ac30-a0ab160a2f48 | -5.78711 | -59.87365 | 2026-10-05 17:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5186b4a6-1447-3759-b121-6d737e0ddf94 | -3.11301 | -57.65641 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6df9ae2e-cba5-3317-a462-1f3bf152f12e | -13.50234 | -61.13591 | 2026-10-05 17:34:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 4df94c09-a46b-34d1-af0f-ef9ba875a8c6 | -3.3312 | -53.38776 | 2026-10-05 17:34:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 640f0548-dfc4-3176-9486-2ce1db0186a3 | -3.32862 | -59.07972 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a6e3fc90-05e5-3054-879f-e95fb720a8e6 | -4.0211 | -58.75616 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c6456f1a-f56b-3e16-9eb0-2a023a408deb | -6.78331 | -66.6571 | 2026-10-05 17:34:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35200309-a299-3d66-858b-b9bf91a3afc1 | -3.12647 | -56.98072 | 2026-10-05 17:34:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 6f0abd50-1eaa-3605-87d5-f4444208f070 | -2.62825 | -49.30548 | 2026-10-05 17:34:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2fee75c9-aa07-3e69-930e-fe3b99a34d2e | -3.6764 | -60.62969 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 71c96e53-b4a1-3a73-8d85-98498c148911 | -3.41183 | -58.01331 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dbdb42ac-c45f-3966-a508-e31ce2c595f5 | -3.4324 | -59.57126 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ab6cbc28-3ca8-37bd-8feb-4bfaf3f23855 | -3.42349 | -56.9479 | 2026-10-05 17:34:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 82403c1c-0528-3dea-b5d0-e63848372b46 | -7.95311 | -69.92968 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 93072be8-12b8-300c-a995-1c8e25a29d48 | -5.98292 | -55.38337 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5e3b83a4-ba81-3e41-83ee-dcfc9ef684ed | -7.36707 | -73.1452 | 2026-10-05 17:34:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 15.2 |
| dc2dc983-898e-351d-929b-c3bca8bfa095 | -3.63936 | -58.93686 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| b98ee414-6f3a-3a4b-968b-cb466e5f9ffe | -8.3627 | -71.06035 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 41c754c0-58ce-3e78-b50b-126a7681eeb4 | -7.36055 | -72.60313 | 2026-10-05 17:34:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| ca913b9b-d37c-31cd-90b6-8e3e43577907 | -3.40889 | -58.01788 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 65d2a485-89b6-3a36-bdb4-05ad4f04641b | -3.74813 | -59.41547 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ee10d521-308b-352f-b8e5-7a3141fbacd8 | -15.76439 | -56.47652 | 2026-10-05 17:34:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f4fbd1a4-eb3a-383c-a0c6-fabda7531ed6 | -2.96371 | -54.10809 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 36ce6353-0947-35ce-ba7b-69a5a955ebd2 | -3.07564 | -54.15908 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 07c1964a-7a75-3b2e-b029-8bf076865819 | -4.9097 | -56.26212 | 2026-10-05 17:34:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bfdfa624-c1a5-3e40-ba31-4ee6c41d158c | -3.38617 | -59.42812 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3f39c623-dd75-3b8f-aa12-2c7815788f34 | -2.95609 | -54.14729 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 0fd17320-a502-3caa-923c-f00112858476 | -2.97874 | -57.902 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a8c23891-89ee-3cbb-ab85-a6f83217883c | -6.18987 | -55.34713 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 321893ec-b9d8-3723-9f7e-a6981f203f2b | -3.77134 | -61.18587 | 2026-10-05 17:34:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 584d4be8-a58d-36af-86fe-cabd87e69525 | -3.5826 | -55.40134 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f4a65faa-48e3-306d-8c84-025c83f463b6 | -3.45559 | -60.56215 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d5304414-738c-3259-b188-68539561b63a | -3.63195 | -58.93421 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3e2dc20e-41fd-3906-9076-e689bbd1cc4b | -7.80272 | -66.78444 | 2026-10-05 17:34:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| abe8bf24-232b-3559-99c2-b8bb5348995d | -2.94699 | -54.14884 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 5f747f3a-5d76-32fa-84bd-b682af8f6986 | -13.77788 | -58.24903 | 2026-10-05 17:34:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9828cce9-d103-3ce0-afbb-18253f142caf | -3.75314 | -59.4257 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e718c0b6-94f3-37d1-9f41-c4c114596749 | -3.66812 | -59.66897 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 43bcf6a2-6573-36cb-82a0-b09ed898aa42 | -2.93912 | -54.10124 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 19cef4e8-0f53-3b0b-834e-f821011c4fc6 | -3.59043 | -61.71475 | 2026-10-05 17:34:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 41ac0daf-1263-34b4-8e90-fca320e1a78a | -3.58087 | -60.53887 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3f31ac2b-1744-3b42-b1be-925adc918527 | -3.71794 | -54.22866 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4fcdbb58-aa9e-3a46-9c69-baed1569bea3 | -3.46286 | -54.59552 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 746e870d-86f8-340c-973d-63229629bba5 | -2.94391 | -54.13026 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| e6e23a75-9f2f-3fea-aa64-a1075b682712 | -3.70634 | -60.16132 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ca54bec7-979f-3518-9950-0cc963e0618b | -3.03393 | -57.41842 | 2026-10-05 17:34:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce570358-c79e-3711-a9c8-2d8cf8092da1 | -3.86371 | -57.50304 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| eb0d35f6-1eb4-343b-9fb8-c4d313ab7bb7 | -3.73751 | -59.0271 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f8818dcd-e377-3bde-a0e6-b0954f70e3ce | -2.99432 | -54.03612 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 360138db-43bf-333a-8e46-f820f9e33837 | -3.67369 | -54.53286 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 151e6c7f-3d7c-31df-adf1-e1cd21f2b42b | -2.95231 | -54.15271 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| a011e950-5597-3fd2-b5ed-8e65cee30964 | -6.21034 | -55.27201 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fdb52606-7e59-3767-976c-15f113a888f1 | -3.46219 | -54.59128 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 95244f4f-dca3-39bd-b8f6-b45126bc53e4 | -6.77912 | -70.17796 | 2026-10-05 17:34:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 81631415-b08a-389f-9a35-050a50d1f193 | -7.36722 | -72.60239 | 2026-10-05 17:34:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 23c97f0d-250d-31e7-bea2-b796cc125a15 | -3.08094 | -54.16291 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| a31e84a5-ebaa-3841-87ba-5e0dc04cc223 | -3.64342 | -58.62188 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 3ffa0ac1-bfa7-3eaf-a3ea-e7171b01997f | -2.95557 | -54.14623 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 66ee3256-5266-3277-9540-a5d18289d1a1 | -6.17129 | -55.36985 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d3f2e7cb-be0d-33f3-b4e7-37f109f3f07a | -11.01912 | -68.5145 | 2026-10-05 17:34:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 47ec46a1-18af-395f-8955-a1d427d35e8f | -2.96904 | -54.112 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0d3fcc63-fca6-33d1-b492-14a4ad69d3f5 | -4.90733 | -56.26033 | 2026-10-05 17:34:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48f56fec-e8c0-332e-8cb9-3ebfe45b3563 | -3.62842 | -60.20586 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6c86c51f-dd9b-3ede-b534-6712a3c294f5 | -3.51451 | -59.55488 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 21.0 |
| d35ff155-6393-3875-adca-a5592762d57b | -3.2497 | -57.90463 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0914fcf1-5f9b-3c38-8c66-4d0d5853e9e3 | -2.98657 | -57.90503 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6482550b-2d1d-3611-8a6e-ac9988e50fcf | -3.72033 | -58.20319 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 30bee810-142e-3575-b312-61db0ade45f8 | -3.44288 | -59.61702 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c8a8ba31-2e2b-377d-ae39-dabf31728163 | -2.97274 | -57.83932 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a12e1352-b66f-3c91-8a75-3b45c2187472 | -3.12291 | -53.70304 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 8bca87c7-215e-333a-8af8-6db7a63eae4e | -12.11163 | -60.67239 | 2026-10-05 17:34:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 27.9 |
| e6c3f8ff-729b-3065-84c1-4d9a38a4266f | -3.71776 | -59.68585 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4cf0662e-f6d9-3f46-9594-e0f217fd8472 | -3.74084 | -59.41291 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 647b835b-a872-38b5-9fa5-13be5214c820 | -2.99499 | -54.09853 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d2e325fd-8e89-3817-b18d-fc7b374c219d | -3.19694 | -57.08633 | 2026-10-05 17:34:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0b16bb9a-3e53-34a7-b85d-a9510ebbef0a | -3.47182 | -59.64897 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccc9c7d8-f42c-37ea-8e3d-9347c2809201 | -6.23562 | -55.64695 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0fd85e94-84d9-3f25-ad2e-d775db8a47ce | -3.5833 | -57.57824 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| c0b6fa26-5f48-3183-9d89-1677b7c21f39 | -5.98804 | -55.36465 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7c95215-aea6-310d-8abe-0daa05be1410 | -2.88186 | -56.60432 | 2026-10-05 17:34:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4aa13743-9d86-3ad3-a60f-30032fc0eeb6 | -7.77451 | -69.92956 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f726bc5e-2574-3fa7-977f-21082d8bdd38 | -7.80303 | -66.92206 | 2026-10-05 17:34:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e44d35e3-1053-3c2c-955e-1323c9cc3401 | -14.71005 | -58.66661 | 2026-10-05 17:34:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ff4f2b5a-cfe0-3d22-806f-7c42d5bf27f7 | -6.2356 | -55.6457 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 38751776-4f86-36d3-a325-c9639e96c778 | -2.95385 | -54.162 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 0970a097-a9d2-3398-bb87-55d4cb57a7fc | -3.37757 | -58.23505 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7642f4e1-f193-3303-bbc5-5f6dcee8eee9 | -3.11501 | -57.66908 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 97b132e3-dd90-3f5a-af85-cdf970eaf10a | -3.47018 | -59.50339 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c1d5be5-1634-3cf4-9e22-f876289af0cd | -6.04584 | -59.94502 | 2026-10-05 17:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0f6fe3b7-034c-3542-9578-3b05e38e502f | -3.46654 | -54.58988 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d8ad9a76-54b8-3e05-ae1d-4345256e87a9 | -9.79675 | -47.77892 | 2026-10-05 17:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 99c1b30e-7467-3bda-b4ec-3913f85f1ab8 | -2.95612 | -57.61028 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README138.md)
