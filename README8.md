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
| f09e8993-0fb9-34dd-a867-11d793bd1161 | -7.79507 | -43.00917 | 2024-12-14 04:23:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7d03f1a7-82ab-3c8f-b370-bb32937feaf8 | -1.71529 | -52.56643 | 2024-12-14 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 823807c8-6ffd-3fe5-a601-451b266bfaf4 | -1.69829 | -52.61143 | 2024-12-14 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0d27ac8-68ed-36ad-a85e-293a5266a18f | -3.56135 | -43.65932 | 2024-12-14 04:23:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 729f158d-3daf-31d4-925a-76e4d467086b | -7.88775 | -42.44445 | 2024-12-14 04:23:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 61d4b993-a82d-3b98-9b95-ed9d039eabc4 | -4.17141 | -42.43158 | 2024-12-14 04:23:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b1080746-9838-369f-9d11-589cbbf23600 | -1.71611 | -52.56127 | 2024-12-14 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bde32bde-75d2-3a74-afc5-7d69e2c79200 | -8.93521 | -44.24247 | 2024-12-14 04:23:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb5807de-93e9-3401-81d0-dfb8db065dd6 | -4.77234 | -37.81421 | 2024-12-14 04:23:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ba032ddc-5d7e-3f12-a71d-ea8e234b874a | -2.96295 | -39.96286 | 2024-12-14 04:23:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| aff89328-1c3a-31f7-87d2-04e266011537 | -3.45944 | -40.81782 | 2024-12-14 04:23:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 717d531d-079e-3b7f-9bc0-8e742a654f21 | -9.28203 | -40.17364 | 2024-12-14 04:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| eeb92d0a-42c8-37a2-98bd-85ad55729990 | -3.56193 | -43.65564 | 2024-12-14 04:23:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06a3f07e-7aaf-3f00-a966-7da9b7224e17 | -1.74178 | -45.19235 | 2024-12-14 04:23:00 | NOAA-20 | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e7d9748-3e83-3091-9ca4-5c4c0c00351a | -3.6244 | -46.71592 | 2024-12-14 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57a7bc06-44cd-3e02-9e9a-8b6dea747fd7 | -7.99828 | -39.42806 | 2024-12-14 04:23:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a8f9565f-4d65-37a1-a371-c292eb8e66ff | -3.294 | -42.51734 | 2024-12-14 04:23:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc7fb73f-04d7-399c-b568-1a2870460e43 | -3.62496 | -46.71236 | 2024-12-14 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05fccca7-c5ca-38fe-ab50-6f2b8b1182c1 | -4.01846 | -44.55513 | 2024-12-14 04:23:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 13b4087e-4f55-3580-8681-3e8fa7e868bc | -10.24798 | -39.37325 | 2024-12-14 04:23:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 46f6752e-8e35-306a-a69a-ebb70dd52c17 | -9.27695 | -40.1773 | 2024-12-14 04:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e26b3b9b-7134-3a07-8674-3eaf6ee7a0fe | -3.90382 | -44.1604 | 2024-12-14 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7cc3144c-a70d-3266-800e-99ad7691d966 | -3.38559 | -44.15409 | 2024-12-14 04:23:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a11c6d4-c19a-3947-85b9-876140c2d9dc | -1.93861 | -45.19138 | 2024-12-14 04:23:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38d7d5c2-163f-3c42-a088-efa01d25672d | -7.6672 | -40.84931 | 2024-12-14 04:23:00 | NOAA-20 | CARIDADE DO PIAUÍ | PIAUÍ | Brasil | 2202554 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 62add730-8599-3ca7-8955-4f44b08d2218 | -3.56078 | -43.66301 | 2024-12-14 04:23:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b420e94a-a177-3fe2-9a5d-6a64bb84b280 | -3.79164 | -46.83696 | 2024-12-14 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f36810a8-7c65-34c8-b705-51e56f3e05f1 | -8.93812 | -44.2469 | 2024-12-14 04:23:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 045cbaf4-e6a5-394b-9418-02ed316f477f | -8.35135 | -43.81981 | 2024-12-14 04:23:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c8154fd4-12df-3a5f-99ad-fff5f9aa0dc7 | -3.28919 | -42.52488 | 2024-12-14 04:23:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3db7a63-ae2f-301f-9fab-edcc0fffe3f0 | -8.93463 | -44.24636 | 2024-12-14 04:23:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d2d5167-c1f0-3947-9118-bab920a07055 | -4.96328 | -38.73681 | 2024-12-14 04:23:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8403c7e3-0808-3d94-bf85-d2e4d0461630 | -3.25157 | -46.85923 | 2024-12-14 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c546d70f-8141-392b-81c2-6935fc9b504e | -4.16779 | -42.43102 | 2024-12-14 04:23:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 33125931-d3d2-3cad-8307-29be91c39785 | -3.251 | -46.86282 | 2024-12-14 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 76a67334-2ed4-32f2-aeda-684260822802 | -2.75336 | -45.71415 | 2024-12-14 04:23:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f386d60-6312-3810-ac95-8bbb0334f917 | -2.95882 | -39.96224 | 2024-12-14 04:23:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 31674698-b423-3069-a774-75aa4645c8fa | -3.28981 | -42.52085 | 2024-12-14 04:23:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e0891f2-2fe2-3e0b-a1e5-28d38d43393b | -4.16652 | -42.43935 | 2024-12-14 04:23:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2c0eb40f-f37a-3b2c-8263-0bb08cca0889 | -4.40359 | -45.82524 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e637a27-f2f0-342b-bc00-34eea543131d | -3.68328 | -51.6664 | 2024-12-14 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94367864-dc91-3032-8dca-1eed39819f10 | -6.02583 | -45.81239 | 2024-12-14 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3eea8269-7f32-373e-b39d-419222d48aae | -7.8349 | -35.18437 | 2024-12-14 04:25:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 7c09e3b5-c460-3084-87f3-c59245ea1f89 | -5.89534 | -45.53984 | 2024-12-14 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f46e0f43-cc94-30e4-8921-cd8e67b00c4c | -4.01523 | -46.64721 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7da5940d-e17b-3ecf-a5ca-c84a31836201 | -12.55971 | -57.76176 | 2024-12-14 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2b23e1d9-ab22-3edd-b0f7-384fb98dea46 | -4.71558 | -43.19561 | 2024-12-14 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5f95c23-6e70-3c53-971d-5a5a742b9e59 | -16.83553 | -46.12946 | 2024-12-14 04:25:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6db67510-d561-3e24-a0b1-0f4a8edc9179 | -12.54557 | -57.71506 | 2024-12-14 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7d6ea8d7-6a34-3c1c-80eb-8d2b25ee0d01 | -15.56833 | -47.85752 | 2024-12-14 04:25:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd31c886-13e5-34a8-8c4a-689262abb65f | -4.02844 | -46.82316 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2a54eba-aa3a-3beb-83c8-d10f4843e071 | -11.82171 | -57.82706 | 2024-12-14 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a9829a7-ca2b-3171-9568-071a5f962dc2 | -4.41683 | -45.82732 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f93b1c2-f1e5-3b2e-8049-406333a9b190 | -6.08894 | -37.62253 | 2024-12-14 04:25:00 | NOAA-20 | PATU | RIO GRANDE DO NORTE | Brasil | 2409308 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| db29db95-c839-3d26-820d-2e984d484fbd | -6.01591 | -45.81084 | 2024-12-14 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77925db9-7af3-37c3-94b8-dd00fc056c7c | -4.41189 | -45.83713 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ec6bf11-3827-3045-b81d-22c3fec5e68b | -6.93384 | -42.84834 | 2024-12-14 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a20273b6-6dba-36ef-815b-41cb993e3853 | -4.41851 | -45.83817 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00f1212b-c918-36d4-9f8f-3ad7d040efee | -4.04131 | -46.80704 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c510397e-86e9-34e7-a35b-c42ea749e251 | -10.66288 | -44.71636 | 2024-12-14 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe0826f7-6d24-3ee4-87e8-cb9a075ba364 | -5.96552 | -40.44179 | 2024-12-14 04:25:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 64dc07db-769f-3780-ba0e-e4f58382884a | -4.03795 | -46.80653 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4adf8560-92ba-3794-ba73-cc869d3980e5 | -4.07539 | -46.72173 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b28bedd-1ba1-351b-974f-6d0e2d8389f8 | -13.66005 | -55.25179 | 2024-12-14 04:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 076abaf7-115b-35a5-8b5b-7944981a31c4 | -5.93197 | -46.06265 | 2024-12-14 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc9f2ddd-ca0a-3a10-b8c5-91c38637bbb0 | -11.9678 | -49.11874 | 2024-12-14 04:25:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d72cc301-59d3-37c5-a92c-84833a22d07b | -5.53357 | -42.86175 | 2024-12-14 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b4cb00fb-0630-3a0b-b62f-577a4747108a | -5.94365 | -43.76896 | 2024-12-14 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f2f93fc-ddad-375a-b197-b9f125257420 | -4.4069 | -45.82576 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2ee8871-31e1-3597-a6bc-733d108028e1 | -4.40858 | -45.83662 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff541663-1a2b-32bd-a0cc-eaf5cdd13a56 | -4.08095 | -46.66481 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbe4e8c7-56ba-3fc3-8e1a-7aecdf84f7c1 | -14.68814 | -52.63003 | 2024-12-14 04:25:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9aedaaa-285b-339b-8307-506e6ec58e37 | -3.9897 | -46.89364 | 2024-12-14 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b5f94d6-bf2b-30e2-8b23-41aaea18aad8 | -6.23872 | -46.42286 | 2024-12-14 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7bc2612d-97fe-3a7d-b32c-2e99383286e7 | -4.02565 | -46.8191 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 416417ab-972c-30e5-98d0-c2214e2f0541 | -6.92109 | -35.72099 | 2024-12-14 04:25:00 | NOAA-20 | AREIA | PARAÍBA | Brasil | 2501104 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ac09294c-63a5-37be-93c6-a2ad8a27cfca | -4.02229 | -46.81859 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 026f145b-b925-3910-bd0a-df0a6510a76a | -4.40251 | -45.83214 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10d6bb6e-3f6a-3113-92b0-638c13527e64 | -4.41466 | -45.84109 | 2024-12-14 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bd8b889-fd26-36b9-9132-e689009961ff | -11.82031 | -57.82837 | 2024-12-14 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8646eaad-3c3d-3ddd-aa2e-83c676274800 | -14.69115 | -52.6357 | 2024-12-14 04:25:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aec8d85c-8ba0-3c8e-96a7-b9f9d35fc4a5 | -12.55678 | -57.71721 | 2024-12-14 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1190a50-6da4-30a2-af82-227e22b10cfc | -6.77913 | -38.32811 | 2024-12-14 04:25:00 | NOAA-20 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| face05b5-c96e-3646-9e1a-d743bcdba245 | -11.96839 | -49.11871 | 2024-12-14 04:25:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4815350-4143-32b4-a541-9a903222daf6 | -4.07427 | -46.72886 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0f89e85-5b5c-3a04-a813-7ee7a6535783 | -6.92653 | -42.84723 | 2024-12-14 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 47800b42-64e9-3f37-a22e-c12ce8ea6663 | -5.05588 | -42.61692 | 2024-12-14 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 004ec508-be96-3b62-88f4-88ab03e75722 | -12.90928 | -55.04679 | 2024-12-14 04:25:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59de015d-036e-30de-82c6-2c264e9e8654 | -4.0347 | -46.69719 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a62c1045-4349-3789-93e9-cb60d8d1939d | -14.83937 | -53.67632 | 2024-12-14 04:25:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ff29fee-14bc-3551-b125-f14209480052 | -4.65394 | -43.81905 | 2024-12-14 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 261feefa-4553-3138-829a-1ff3d7909567 | -4.41406 | -45.82335 | 2024-12-14 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 175d026b-dcf5-341d-854f-4f433f676216 | -4.09931 | -46.61356 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 553a12b8-4929-3c51-9d8d-6bb793dc70fc | -4.03617 | -46.90472 | 2024-12-14 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f91545a-3c69-31c4-a397-f2ffcff5ab77 | -4.03674 | -46.90113 | 2024-12-14 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d3c821a-5983-31f1-9022-3e961138a45f | -4.02285 | -46.81507 | 2024-12-14 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0b54aec-dbbf-36d9-9c20-214291ed61b5 | -13.17779 | -53.28674 | 2024-12-14 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e844c96-d61b-30c3-9685-1518d096776a | -4.24913 | -47.57479 | 2024-12-14 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7de2dfce-9594-3a27-bc27-eeb9a637d089 | -5.095 | -46.03005 | 2024-12-14 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 970c96a4-76f1-3c5d-bf61-40cd821a101f | -14.84349 | -53.67715 | 2024-12-14 04:25:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README9.md)
