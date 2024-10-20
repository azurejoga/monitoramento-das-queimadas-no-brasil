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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a91bb570-b928-34be-b6fc-5a5d53f96e7d | -10.69666 | -37.04906 | 2024-10-20 04:08:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0f2c1a5c-efbd-39ac-8abd-a489753f6252 | -6.14625 | -37.81184 | 2024-10-20 04:08:00 | NOAA-21 | FRUTUOSO GOMES | RIO GRANDE DO NORTE | Brasil | 2404002 | 24 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 0f921c94-fd11-3c2a-87bc-50c5106fd09c | -6.14256 | -37.81125 | 2024-10-20 04:08:00 | NOAA-21 | FRUTUOSO GOMES | RIO GRANDE DO NORTE | Brasil | 2404002 | 24 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 5fc0114c-808a-35d9-9aa2-f1c0a5185843 | -6.4183 | -39.75817 | 2024-10-20 04:08:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c39afb03-7501-3d28-bd41-c9511075fc6c | -7.90727 | -39.26622 | 2024-10-20 04:08:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 15bf2ebe-294f-3777-96a6-6f8a229de5dd | -7.51107 | -39.58705 | 2024-10-20 04:08:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7cccdba8-4773-3aa2-b322-8c4890666c52 | -8.75714 | -40.81769 | 2024-10-20 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dfc8e4c4-3606-3cc3-b28f-0781a8f7b010 | -8.75659 | -40.82127 | 2024-10-20 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 075100f9-a0de-3dce-aa78-eb4b3ec10661 | -8.6617 | -40.64168 | 2024-10-20 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 19ef9d4b-22ca-3634-a96f-e87cae451a8a | -8.21389 | -40.27324 | 2024-10-20 04:08:00 | NOAA-21 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6aaf3f81-4914-3fbf-82dd-7365111dc11e | -8.21258 | -40.27283 | 2024-10-20 04:08:00 | NOAA-21 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 79c377dd-9887-30b0-8128-7d8f33f2292d | -4.01168 | -40.38251 | 2024-10-20 04:08:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e32f4cac-9baa-30d4-90b2-a88bee746911 | -6.40734 | -41.68597 | 2024-10-20 04:08:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dac5274c-bcd8-3a8e-953f-7597e00ecbba | -9.01643 | -42.01451 | 2024-10-20 04:08:00 | NOAA-21 | DOM INOCÊNCIO | PIAUÍ | Brasil | 2203453 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c28e6b51-24c8-333d-8f22-39c595f865fb | -3.70575 | -42.41221 | 2024-10-20 04:08:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4a38bb04-8103-3172-bbaa-427e299bbcf6 | -4.46007 | -42.90696 | 2024-10-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ba0d66f-13ee-3bb2-9e83-02ce1c073549 | -4.45666 | -42.90644 | 2024-10-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cb9ee6c-8094-3a34-8f93-2d012d423859 | -5.61809 | -42.78004 | 2024-10-20 04:08:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 39cce753-3adc-38d4-9c36-654b21005d58 | -5.59401 | -42.93164 | 2024-10-20 04:08:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 9a617ffa-0c53-362e-86ce-a05acd0de39d | -5.59063 | -42.93112 | 2024-10-20 04:08:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 53107122-c637-39b6-8cf2-b42aebd7537d | -5.59005 | -42.93477 | 2024-10-20 04:08:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e99744b4-2bb0-390f-afe8-7bbf9757fde3 | -5.48327 | -43.3404 | 2024-10-20 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| db6ff264-fd6e-3840-811f-19c49cda1fc2 | -5.95017 | -43.38654 | 2024-10-20 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e8dc8e51-6118-3d52-acc6-79f24a1d634b | -5.94957 | -43.39028 | 2024-10-20 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 18f78739-b442-3406-bfa3-939ab89bbe71 | -5.94273 | -43.3892 | 2024-10-20 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7d833f89-f40c-391b-a7b7-ed4f38fdd473 | -5.93262 | -43.36474 | 2024-10-20 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8055d2d5-66e3-33dd-bc32-e451d5b0c777 | -5.93203 | -43.36846 | 2024-10-20 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a1be345e-f495-32c2-9ed8-6309f38f3f27 | -5.92341 | -42.95795 | 2024-10-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| a21b5ee3-cd3f-3e15-ab59-56efce03840f | -5.92004 | -42.95741 | 2024-10-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 9b4ebe09-a616-3d35-8b11-a769dda9d8b1 | -5.91666 | -42.95687 | 2024-10-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 6c113d64-4770-377d-af5f-19a9fd729833 | -5.91609 | -42.96048 | 2024-10-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8d1c3be0-352d-3307-a920-3240cb59a1f0 | -6.53947 | -43.04096 | 2024-10-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 966eddbe-269a-36e9-a492-0675807fbd14 | -6.46421 | -43.20756 | 2024-10-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91aedfc8-253c-3039-8c27-6848061ef99b | -3.30287 | -43.5116 | 2024-10-20 04:08:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e003ce5-0cb5-35f6-8972-720f355ac2dc | -3.51877 | -43.61363 | 2024-10-20 04:08:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 010a26f2-2385-3976-9a54-a6809df06026 | -3.51814 | -43.61763 | 2024-10-20 04:08:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e8686304-0888-3317-9a25-de65d9e4e632 | -5.03925 | -43.79316 | 2024-10-20 04:08:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09b104dc-425b-3079-a852-4ce6e67ba508 | -4.86233 | -43.24716 | 2024-10-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04d6f06e-9255-336b-86c6-a1493a6bd12e | -4.86173 | -43.2509 | 2024-10-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fd6dd27-32b0-33e9-bbe4-993a74155f75 | -4.8583 | -43.25037 | 2024-10-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23abc768-a69b-33fe-9504-6ae721418f65 | -4.58333 | -43.98798 | 2024-10-20 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c46cc89-37da-3768-a6e5-0fa73f9dcb6a | -4.58027 | -43.98775 | 2024-10-20 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2801d3a4-cea8-3830-a90e-8f581d15e0d5 | -4.57978 | -43.98742 | 2024-10-20 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5917923d-6733-3458-ad03-641305b2e2a0 | -4.52559 | -43.48716 | 2024-10-20 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e917872b-5d23-399f-b162-3eb99e14ae67 | -4.81878 | -44.35526 | 2024-10-20 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de0df0c2-e9a2-3101-b8c5-0d13dc9b0cf2 | -4.40198 | -43.85338 | 2024-10-20 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59cf81de-eef3-314f-8ac2-c3c8adb152f8 | -4.16299 | -43.35607 | 2024-10-20 04:08:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 35f781ac-f9ed-39df-939f-74b36ebe9616 | -4.16237 | -43.35991 | 2024-10-20 04:08:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 75ac4f69-f555-3370-a35f-03268a3c95f9 | -4.15951 | -43.35554 | 2024-10-20 04:08:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6eef0ed1-29d1-31f0-a5a8-b580ac4638c3 | -4.07415 | -43.38605 | 2024-10-20 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27ac59fb-b267-336f-876f-83b03b06a4ad | -4.4884 | -44.58891 | 2024-10-20 04:08:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 493ebb73-82bb-3929-8605-c89898eba049 | -4.31301 | -44.25488 | 2024-10-20 04:08:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfb92f24-a9dd-31db-8e35-4f0f29eb4113 | -4.30939 | -44.25432 | 2024-10-20 04:08:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b217022-b445-3d0e-a301-91d1d9d24250 | -4.28951 | -44.51974 | 2024-10-20 04:08:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 57810347-1767-37aa-9e08-a5d7ebd73878 | -4.2888 | -44.52404 | 2024-10-20 04:08:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 185a5e5f-2854-3ac8-ba2c-98b88f7b79da | -5.54086 | -43.90221 | 2024-10-20 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a8409cc5-4295-36a7-8a8c-ccdc59500f0b | -4.09622 | -44.22673 | 2024-10-20 04:08:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 735a1d43-a89f-3b4f-957a-3d59602b51a5 | -4.09555 | -44.23092 | 2024-10-20 04:08:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b443f2d7-3e48-34ef-b257-7c0a62785b59 | -4.05674 | -44.31112 | 2024-10-20 04:08:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1847e73b-2a5c-3d3b-adb9-336e95821254 | -3.95649 | -43.17587 | 2024-10-20 04:08:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ea6a0a3-b534-3884-9a0a-123433823bf7 | -3.67571 | -43.69859 | 2024-10-20 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fab0e93c-0d70-3b44-a0ab-3f958fe320a7 | -3.67506 | -43.70259 | 2024-10-20 04:08:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 01925601-6dfc-3136-89fd-bb451ec49141 | -3.77411 | -44.43539 | 2024-10-20 04:08:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 217c4009-63d2-33e9-80b3-d36df175e739 | -6.18969 | -43.70963 | 2024-10-20 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 984e1c15-20ec-3b4f-bd0c-e0cb86e79960 | -6.15488 | -43.6231 | 2024-10-20 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bd29e05-faa4-35a5-bd03-c05da4919df3 | -6.07288 | -43.86887 | 2024-10-20 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d79b800-3521-3e44-983a-7e1b936fbc02 | -5.93179 | -43.84646 | 2024-10-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cae38e68-9080-3b13-aebd-06a2e772a7f8 | -5.85731 | -43.74422 | 2024-10-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f732bf15-8844-32ea-acbe-2e65770fb4ca | -5.85446 | -43.73985 | 2024-10-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7fcc5282-9b09-39b1-b909-556a58d30d61 | -5.85384 | -43.74367 | 2024-10-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8ac81581-be0e-30fe-9811-ac0660053dc1 | -6.15958 | -44.42986 | 2024-10-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3302eed7-8b4e-3ab7-a6d9-98fd31fd61eb | -6.156 | -44.42934 | 2024-10-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0fb7aed4-3f55-3382-a6ff-eb213b7f8bee | -5.91015 | -44.06764 | 2024-10-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d45b98b-c48a-3d10-96b1-231bd338e5b3 | -5.82981 | -44.04736 | 2024-10-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0cfe13d4-83a1-3c6a-9eb7-8240892c5219 | -5.82917 | -44.05131 | 2024-10-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90676bf9-62ff-3ab0-8753-208d1e1d5613 | -5.46444 | -44.86581 | 2024-10-20 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05a134d8-2253-33e0-9fa9-076d8ca14e06 | -5.4318 | -44.81189 | 2024-10-20 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a76fdf31-1057-360e-8f5b-fadb0a32055f | -5.33974 | -44.70958 | 2024-10-20 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d7a664ef-4503-3116-b95c-41fae002ffac | -5.29949 | -44.72643 | 2024-10-20 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e969aca5-6477-3db3-8371-e7687043f431 | -5.72965 | -43.81543 | 2024-10-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 251a0bdc-d69e-3941-9fa0-0148b015aa49 | -5.72617 | -43.81488 | 2024-10-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 544d7543-1720-3572-a34b-6fb3ab13e45b | -5.72201 | -43.77453 | 2024-10-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a8785b27-44dd-3dd1-841d-b6b1cad67649 | -5.71917 | -43.77009 | 2024-10-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7068f67f-3293-3538-9c6e-7e920dc9b37d | -5.71853 | -43.77398 | 2024-10-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03fc492f-d87f-3c9d-99ed-7dcfadba4783 | -5.54437 | -43.90277 | 2024-10-20 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1fcda752-bc81-3087-a772-1e1bf10f81b6 | -5.54374 | -43.90668 | 2024-10-20 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1ae11891-eef7-3e3e-92bf-082d50700246 | -5.54311 | -43.91059 | 2024-10-20 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 52b36b55-6779-30a8-bbf0-1eb7249d2cf3 | -5.54023 | -43.90613 | 2024-10-20 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 39735f52-71eb-3038-a597-fb18b8f14128 | -5.5396 | -43.91005 | 2024-10-20 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7dc716c9-b998-30c3-8e78-cfd30099a9ef | -5.52854 | -43.95657 | 2024-10-20 04:08:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ab9e5e5-0df2-34b1-a60f-42be34dfdb03 | -5.50582 | -43.46338 | 2024-10-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e7e4bda-e273-3257-8882-7d0154102c11 | -5.37969 | -43.61551 | 2024-10-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89a657a4-01b9-3722-82bb-bb5a241777c4 | -5.37561 | -43.61876 | 2024-10-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20b8d980-11f0-3780-a297-1a7b9f3c782b | -5.36563 | -43.57011 | 2024-10-20 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 19b2d882-1efc-3d60-9888-164264bacebe | -5.36501 | -43.57395 | 2024-10-20 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cd754a62-2134-3a4e-bef8-b7c90c0a2669 | -5.36217 | -43.56955 | 2024-10-20 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 472414b2-389c-345f-bbae-c413888f6f37 | -5.36155 | -43.57339 | 2024-10-20 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 07fc5a17-5459-3cdd-a6d3-48bc00d0cee9 | -5.35871 | -43.569 | 2024-10-20 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f26e63c4-9d3f-3f5e-a1f0-ef889d0dae70 | -5.35809 | -43.57284 | 2024-10-20 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47dbd334-fc9f-3442-8270-dc44ad2fd6ee | -5.26572 | -43.98936 | 2024-10-20 04:08:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README17.md)
