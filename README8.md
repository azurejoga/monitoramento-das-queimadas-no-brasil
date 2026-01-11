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
| 0c33b32f-5ace-3ebd-83dd-b7578305da41 | -0.13248 | -51.39009 | 2026-01-11 04:57:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 528eed19-4591-326a-b919-730dbce25ba7 | -7.59542 | -45.8912 | 2026-01-11 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eec5e720-0a4f-3d0f-aa1a-d5d10fe57cf9 | -2.06693 | -54.37096 | 2026-01-11 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf36c3d0-dd7e-37d4-abdf-add38b6fa15e | -1.39524 | -48.15146 | 2026-01-11 04:57:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 05dc1d25-64b0-3c25-81d6-9446e8e59fa4 | -7.59584 | -45.88815 | 2026-01-11 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05131186-b662-3ff0-ad9e-a6f5b9b7f831 | -2.97029 | -54.33078 | 2026-01-11 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f7b33d8-6004-3587-aa94-01de73b4e493 | -0.05691 | -51.6599 | 2026-01-11 04:57:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ea375b0c-c2da-33a4-a24b-56e5fae7b627 | -2.6161 | -43.10117 | 2026-01-11 04:57:00 | NOAA-20 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cb5be0b-3960-3c97-8d36-e1a61b36cd4a | -5.49839 | -42.15751 | 2026-01-11 04:57:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6360b350-b967-3636-8b0b-4fb145777a26 | 1.11815 | -60.51651 | 2026-01-11 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 75dee6eb-a740-3b9c-90a3-d7bfddf2e4ea | -1.02507 | -47.6893 | 2026-01-11 04:57:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1689fd61-0fd5-37b5-a51c-f5e6b58acb92 | -0.89943 | -52.86055 | 2026-01-11 04:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6150a25e-dbc0-3e77-acda-be25f0286960 | -5.4638 | -45.28704 | 2026-01-11 04:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85652267-6107-3d48-8336-3531da2efa9c | -7.41212 | -48.95048 | 2026-01-11 04:57:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d2f730e-b728-39cd-98a3-bb37348185a1 | -2.52037 | -43.26313 | 2026-01-11 04:57:00 | NOAA-20 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1d7507fa-c9f7-3fa6-a5cb-4a803178bd9f | -2.07027 | -54.37147 | 2026-01-11 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a67d7329-b395-39d1-9acc-57a2c4b98528 | -5.85404 | -44.94706 | 2026-01-11 04:57:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe745ef1-031d-3a25-b50d-dcdb111e88f0 | -5.45899 | -45.28314 | 2026-01-11 04:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63ff6514-fd6b-3644-8309-5ae917721187 | -2.18415 | -52.01007 | 2026-01-11 04:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1692884d-1bb7-3c88-8fda-84fdc24969fb | -4.64768 | -45.79098 | 2026-01-11 04:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94c62bba-d0d1-36b4-91b2-15bfc4344439 | -5.46412 | -45.28495 | 2026-01-11 04:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c8cbc0a-c81e-3c06-899a-fa0df444adf2 | -0.08631 | -51.27919 | 2026-01-11 04:57:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0e0afa4d-1cb0-3513-9270-95d8ca266b59 | -1.30326 | -52.88511 | 2026-01-11 04:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d3dc037-493c-3537-9e57-a259763bb358 | -3.55369 | -43.65616 | 2026-01-11 04:57:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2f675a48-c222-390b-a4f9-3ec1b17a03d3 | -2.05935 | -53.47554 | 2026-01-11 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9edbe48-a06e-35aa-bb7b-b45779e3367a | -2.19089 | -52.01111 | 2026-01-11 04:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34c55454-b756-3db2-8ef9-030566343701 | -0.06083 | -51.65688 | 2026-01-11 04:57:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9772cfaf-cf57-3b4f-8739-d4a8dc5c9a30 | -1.84194 | -54.3109 | 2026-01-11 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a237044b-7688-3fba-889d-f1dc59cc72b4 | -2.19033 | -52.01468 | 2026-01-11 04:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53e59124-674f-3e30-bb2f-a62e08494b01 | -7.49373 | -45.5825 | 2026-01-11 04:57:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b5fcb6f2-857f-3ac0-bf75-ffdb3744cbef | -5.45855 | -45.28638 | 2026-01-11 04:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef87155e-1e0b-37d5-9104-01f3d183e947 | -2.18697 | -52.01416 | 2026-01-11 04:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 697ac7d4-d4a5-357a-8c90-7b40a37600dc | -5.49207 | -42.16371 | 2026-01-11 04:57:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d9fa7f11-3865-3ba9-a381-cc9085968fc7 | -2.97084 | -54.32729 | 2026-01-11 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3067cc74-60ca-32dc-8b82-be64f6f69862 | -5.85357 | -44.95047 | 2026-01-11 04:57:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08c7b476-f484-313d-82cc-f57e1985c485 | -5.28594 | -45.82918 | 2026-01-11 04:57:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d80f208-a067-364f-956b-8d2f247e6b40 | -5.28674 | -45.8274 | 2026-01-11 04:57:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5f702e9-3c5d-3f2b-bd1f-f23944af7be3 | -11.83726 | -49.19402 | 2026-01-11 04:59:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b592a84-ca0f-3e8e-94eb-3115a32765c0 | -10.77119 | -45.0208 | 2026-01-11 04:59:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e84b149-d201-3e8f-be12-e9030ed53d31 | -12.90525 | -52.5293 | 2026-01-11 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2728e38-ac84-3f21-9823-5e254e71f870 | -12.90223 | -52.52448 | 2026-01-11 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57162561-8013-3c58-97e7-88bfe0b61c56 | -12.90888 | -52.52983 | 2026-01-11 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 99e570cf-7228-3c9a-8ac7-db11cc8162b5 | -11.83286 | -49.19337 | 2026-01-11 04:59:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3db7ab94-50b5-31be-be29-ac5c58b65ebf | -9.04532 | -46.99409 | 2026-01-11 04:59:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b0dbd6a-791d-316a-989a-ee17343c5a05 | -11.83667 | -49.19839 | 2026-01-11 04:59:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 503b2492-5b66-3b87-96db-6e54eff1fc46 | -12.90587 | -52.52502 | 2026-01-11 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 750c30bf-8764-3a41-97b9-6c11097583d3 | -13.4282 | -43.86147 | 2026-01-11 04:59:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c311fe5c-becf-392e-be27-dcd8dc51997f | -11.83228 | -49.1977 | 2026-01-11 04:59:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 030d0217-1fb3-3b9d-b52f-b732c376975b | -12.90951 | -52.52555 | 2026-01-11 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9651344f-7885-3afb-867b-39c5711efc0f | -12.91252 | -52.53037 | 2026-01-11 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2d44819a-67c3-34aa-a1d6-b16f4fc07cac | -10.77167 | -45.01688 | 2026-01-11 04:59:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 229fbfb3-3c3a-36ae-a99b-fdceba50b93c | -12.90161 | -52.52876 | 2026-01-11 04:59:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36590402-ef08-3839-932a-703601792c4a | -20.24285 | -46.48248 | 2026-01-11 05:01:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a674c316-879a-36c5-821d-cc7ce6e75b7c | -18.81862 | -51.61195 | 2026-01-11 05:01:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b60ea7ab-64fa-3bab-b7ab-3cefceb7e597 | -20.24201 | -46.49144 | 2026-01-11 05:01:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cc4d0ef1-d0e7-3824-89b0-b75eb777f12c | -16.10107 | -56.75415 | 2026-01-11 05:01:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 222b6916-61ae-3eb0-86eb-bdf08895d1d0 | -20.24243 | -46.48701 | 2026-01-11 05:01:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 26b62cd2-74a4-3290-ac23-a227295ce80e | -20.13781 | -46.84692 | 2026-01-11 05:01:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e1e8774-f4f4-3c22-a2a2-1bcc9a1473df | -18.81449 | -51.6113 | 2026-01-11 05:01:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4f2daef9-7b33-37d9-a758-16f26b11c78a | -14.62764 | -55.47605 | 2026-01-11 05:01:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c8dd63b0-bf73-3ac3-b352-bfb4030b87bb | -18.82589 | -51.62105 | 2026-01-11 05:01:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b0130d9d-cf1e-3811-ac90-f2c1676d5447 | -16.09719 | -56.75718 | 2026-01-11 05:01:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18e5208e-76c5-3da5-bd5e-ff6301f9d5cf | -20.24791 | -46.49184 | 2026-01-11 05:01:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b9299a23-e7a8-3259-904d-6093a62e26d1 | -18.82225 | -51.61652 | 2026-01-11 05:01:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4244a33d-86d1-3915-bfcf-533f9d1d41cf | -20.13171 | -46.84987 | 2026-01-11 05:01:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88e8b38a-7728-394d-83af-6d0886cda469 | -15.91043 | -56.75536 | 2026-01-11 05:01:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dec377de-0a88-3d3a-8356-2b1d0e42d4e9 | -13.99963 | -60.3406 | 2026-01-11 05:01:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 85318d8a-3bf8-31ae-ac3d-af343ffed724 | -20.23102 | -46.48188 | 2026-01-11 05:01:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8d3266e7-482e-36c1-8b49-4e2e2d98a2ec | -18.82176 | -51.62048 | 2026-01-11 05:01:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 979ea124-0c3d-399f-b40d-566f48a723a3 | -20.23692 | -46.48233 | 2026-01-11 05:01:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6dc2016e-0bdc-3ac5-9521-749e49553cae | -20.2471 | -46.50056 | 2026-01-11 05:01:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 21092145-209f-32bb-958a-00831daab02d | -17.75305 | -43.42707 | 2026-01-11 05:01:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| deace9c2-11ae-34b4-8f16-5a5bcb0539dc | -20.13213 | -46.84562 | 2026-01-11 05:01:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5b061e3-04b4-3893-8c9d-bf9a71bf06ca | -20.14392 | -46.84377 | 2026-01-11 05:01:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79899d50-56a3-30b8-b9b4-7f7f2311961d | -17.75268 | -43.42708 | 2026-01-11 05:01:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55934118-5040-31d5-b802-4959308e6ae7 | -20.13823 | -46.84261 | 2026-01-11 05:01:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 647f34c3-c339-3ad8-b113-2f2b9ea56a9a | -18.81498 | -51.60739 | 2026-01-11 05:01:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| de11f127-1dca-3c65-8e2b-3cf36cb4a3d0 | -20.25171 | -46.51462 | 2026-01-11 05:01:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b572071-b8bd-3066-bcae-bf42f3e73d90 | -20.24751 | -46.4962 | 2026-01-11 05:01:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 87b3839c-0857-3157-9507-5ef72f5e7c9d | -16.1005 | -56.75774 | 2026-01-11 05:01:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 01210216-41f8-3b3b-98a8-fa29408821cd | -20.23734 | -46.47786 | 2026-01-11 05:01:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| df824ec0-7334-3871-8fab-2cfee5da893d | -15.25675 | -56.72262 | 2026-01-11 05:01:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0055e9f0-a4a3-3871-9ebf-c93f1d8d0076 | -5.83967 | -35.63822 | 2026-01-11 05:10:00 | AQUA_M-M | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 8608b097-a061-37ee-acb2-65fe7fd68f62 | -5.83528 | -35.64466 | 2026-01-11 05:10:00 | AQUA_M-M | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 9.6 |
| f960efa7-ef12-3cd3-ba44-2ef5d33c0dea | -18.8119 | -51.6134 | 2026-01-11 05:30:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| ebc661e3-6fc1-3d6e-bd0c-a486d568573a | -18.8119 | -51.6134 | 2026-01-11 05:40:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| ef114223-40cb-32f0-8237-b4edb2f1bcaf | 2.04912 | -60.86605 | 2026-01-11 05:46:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 248f32a9-8e9e-34ce-95ab-0b424799702c | 2.05297 | -60.86557 | 2026-01-11 05:46:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d817dd4e-ea58-3faf-a488-5e77f6b1d17d | 0.68641 | -59.27714 | 2026-01-11 05:48:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81f6aa52-79e6-3173-b3b3-79cdf15c0414 | 0.86007 | -59.68646 | 2026-01-11 05:48:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 837e5f92-b18b-3d61-b209-7e7dbc9e588a | 1.35696 | -60.37728 | 2026-01-11 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93ad2958-f56c-358c-872e-58f205ebeae4 | 1.116 | -60.51098 | 2026-01-11 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10daae45-42eb-3cfe-87d8-db4abb43460e | 1.12051 | -60.51376 | 2026-01-11 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 21d7b380-a2f6-3d15-92ab-90f0a75897d3 | 0.63952 | -59.52585 | 2026-01-11 05:48:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 118493fd-efb9-3399-af39-e3ceaf9c101e | 1.11654 | -60.51439 | 2026-01-11 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3173b8b-5235-31d2-8925-5298e62f5317 | 0.35283 | -60.40932 | 2026-01-11 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d1439bd-71b5-37a2-9126-5b150d4d00a2 | 0.35227 | -60.40575 | 2026-01-11 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9788d988-c000-3993-9f22-7160862f0f8e | -12.89958 | -52.52303 | 2026-01-11 06:48:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c04a6581-5fce-30be-b7eb-a764aee60d41 | -6.08969 | -37.85646 | 2026-01-11 11:34:00 | TERRA_M-M | MARTINS | RIO GRANDE DO NORTE | Brasil | 2407401 | 24 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 04e652c0-7da2-34e3-8410-f03ef385eb64 | -6.75553 | -38.42567 | 2026-01-11 11:34:00 | TERRA_M-M | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 20.4 |


[Clique aqui para ver as próximas entradas](README9.md)
