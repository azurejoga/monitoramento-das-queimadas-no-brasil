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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6710021b-1d31-38d9-8a51-7b4a882ee8bf | -17.13138 | -39.66261 | 2026-01-03 03:19:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 240afb3c-b40f-3fba-a92f-00bd02dd57df | -13.43198 | -43.85697 | 2026-01-03 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cf7c05ec-ea3f-3e93-a6b2-95a4691d7455 | -11.40623 | -40.30171 | 2026-01-03 03:19:00 | NOAA-21 | SERROLÂNDIA | BAHIA | Brasil | 2930600 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9b77b430-55e6-3d4b-9b54-f4349b3110b8 | -5.42877 | -36.70695 | 2026-01-03 03:19:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8ec5b2b0-f2f7-3c04-b2d1-97af5491ca9a | -4.68649 | -38.16211 | 2026-01-03 03:19:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f7bf3601-969d-32e2-ab89-9cea576f2b07 | -13.46631 | -38.94219 | 2026-01-03 03:19:00 | NOAA-21 | CAIRU | BAHIA | Brasil | 2905404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3e4b3251-ebb9-36dc-b1ff-6c609688ea81 | -6.75243 | -35.04647 | 2026-01-03 03:19:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dabc0831-fe39-3523-a06a-5c1115c2e861 | -16.92326 | -40.12702 | 2026-01-03 03:19:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5953f5ce-13f1-361e-b1e6-7900187a2a5e | -12.95268 | -41.18299 | 2026-01-03 03:19:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f957f96a-13dc-348f-97ee-3d01bce47697 | -13.46111 | -38.9383 | 2026-01-03 03:19:00 | NOAA-21 | CAIRU | BAHIA | Brasil | 2905404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2a4ff8d9-b940-3b4b-ae27-b4e49d62b877 | -13.46248 | -38.93549 | 2026-01-03 03:19:00 | NOAA-21 | CAIRU | BAHIA | Brasil | 2905404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e5cd9b19-d3ea-3742-98bb-c1a471b857a6 | -6.74817 | -35.04559 | 2026-01-03 03:19:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b4026493-06f5-3067-b112-9bcdcd46e349 | -12.95351 | -41.17889 | 2026-01-03 03:19:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 183ae54c-95c3-3d78-abf3-65a180169ca2 | -17.129 | -39.6604 | 2026-01-03 03:19:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 652e1eae-85de-378f-bdf8-714b5ce41bf1 | -13.46742 | -38.93649 | 2026-01-03 03:19:00 | NOAA-21 | CAIRU | BAHIA | Brasil | 2905404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| da9ed13f-7be4-36ef-9250-d18b91889b2d | -5.7674 | -35.66978 | 2026-01-03 03:46:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO NORTE | Brasil | 2409332 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b3bb2fb3-9df1-3179-a991-3e4e8c728236 | -4.73714 | -38.72768 | 2026-01-03 03:46:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2d32d64f-b594-3693-a9d9-57c75549f78d | -5.4281 | -36.70486 | 2026-01-03 03:46:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 27c960f6-be3f-3a90-aa15-bf2a7c9212af | -5.02418 | -40.26176 | 2026-01-03 03:46:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9cd20afd-2ced-39b3-a419-69cc7b661b04 | -5.36939 | -36.80868 | 2026-01-03 03:46:00 | NPP-375D | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 68936e2c-f9d9-39af-adc0-7f402481521a | -4.42214 | -43.10645 | 2026-01-03 03:46:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffd74d67-8632-3036-be30-1e26f5af9500 | -4.68973 | -38.1633 | 2026-01-03 03:46:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50e53e75-639a-3abb-a44d-7da701c4f573 | -4.4422 | -38.05653 | 2026-01-03 03:46:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 54105bfb-d3a2-3dfd-bc9c-d7a9b584077b | -4.68609 | -38.1627 | 2026-01-03 03:46:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 31e06d2c-acc6-3081-8db8-f76ff9693ddb | -5.02007 | -40.26107 | 2026-01-03 03:46:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d352d0aa-2399-3f2e-b21e-442fbdb651bc | -4.42166 | -43.10933 | 2026-01-03 03:46:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3cbba14-2503-3124-b27e-ec3a4e71166d | -2.42553 | -44.04862 | 2026-01-03 03:46:00 | NPP-375D | RAPOSA | MARANHÃO | Brasil | 2109452 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 199d0f80-3a72-3bf7-83e0-fec9937de6f3 | -5.46206 | -40.69997 | 2026-01-03 03:46:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 995132fe-4a42-3daf-830b-aa1b15c8c5d3 | -3.01413 | -41.12705 | 2026-01-03 03:46:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 18f21da1-94c4-3acb-bc3e-b4f8fd9f23de | -3.30422 | -42.75452 | 2026-01-03 03:46:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a96af239-d539-3da0-ae2c-9d73c1d810f8 | -2.42493 | -44.05227 | 2026-01-03 03:46:00 | NPP-375D | RAPOSA | MARANHÃO | Brasil | 2109452 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66a0e5cc-5b03-3846-a610-7a31521db4bc | -2.94738 | -39.92589 | 2026-01-03 03:46:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c110c101-f264-399a-a905-e1b7e605cf16 | -5.49398 | -40.73985 | 2026-01-03 03:46:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a2eb8eb6-d4a5-3efa-8679-c3fb43f4f63e | -6.68324 | -35.27055 | 2026-01-03 03:49:00 | NPP-375D | PEDRO RÉGIS | PARAÍBA | Brasil | 2512721 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 198c4fbf-394e-3afc-83bf-8274685b9e10 | -6.68269 | -35.27402 | 2026-01-03 03:49:00 | NPP-375D | PEDRO RÉGIS | PARAÍBA | Brasil | 2512721 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 34229024-4cee-32e0-968a-b6f4e3c86b14 | -5.89095 | -39.66041 | 2026-01-03 03:49:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2cd1694d-8213-38a7-a0e3-615ec693d0ca | -9.21186 | -35.5603 | 2026-01-03 03:49:00 | NPP-375D | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 65fbf7bd-a9da-300a-bcb4-1f0d217c19d6 | -7.46053 | -35.10431 | 2026-01-03 03:49:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| cd7fdf7f-7f9a-3174-8c97-5da9e05b7799 | -9.20853 | -35.55977 | 2026-01-03 03:49:00 | NPP-375D | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| e3d0057b-f666-3c35-b47c-8695f575e31c | -7.4572 | -35.10378 | 2026-01-03 03:49:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f3d9e7fd-8bc6-3f64-9b6c-63a6d882f06c | -9.79635 | -35.92707 | 2026-01-03 03:49:00 | NPP-375D | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0ebca60a-a9b4-356d-aa58-89ca29054221 | -6.2805 | -39.53545 | 2026-01-03 03:49:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 511006c8-f3ee-35c0-bc04-bff78806114f | -7.45666 | -35.10727 | 2026-01-03 03:49:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6051f846-f740-38ab-bc3f-b25b1816a5ba | -5.32205 | -43.56407 | 2026-01-03 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7aad9a28-ed0c-3abc-ac3f-69bffa11204b | -5.95706 | -39.99144 | 2026-01-03 03:49:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2127c38d-5c8c-3e76-ba18-3d6ca484b7c6 | -8.75672 | -38.83826 | 2026-01-03 03:49:00 | NPP-375D | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 8de1fe22-eb72-3e08-8e45-a1e9faed36fd | -5.89031 | -39.66214 | 2026-01-03 03:49:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2fe14d1a-4367-3fcf-9d35-937d8df35db5 | -5.89116 | -39.65715 | 2026-01-03 03:49:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d7ca3665-9340-3cc4-a5bf-6b6b2f59998c | -6.67937 | -35.27349 | 2026-01-03 03:49:00 | NPP-375D | PEDRO RÉGIS | PARAÍBA | Brasil | 2512721 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 39d31949-ccc0-3288-846e-2d671131c467 | -9.79967 | -35.9276 | 2026-01-03 03:49:00 | NPP-375D | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 389af2be-8a9d-38b3-8558-143f568feae8 | -5.32767 | -43.56205 | 2026-01-03 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 27013536-dc3e-3e91-b4b2-8d7e53369c41 | -9.48243 | -36.03419 | 2026-01-03 03:49:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cdbb1ded-2063-3a1a-9968-8d96c9dd9d95 | -5.32257 | -43.56103 | 2026-01-03 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ccc034fc-2e9c-39c9-8f44-07c4c87b6f40 | -9.2052 | -35.55923 | 2026-01-03 03:49:00 | NPP-375D | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 547d3445-dfd2-39d0-9db5-124b59d14d13 | -7.71594 | -35.39155 | 2026-01-03 03:49:00 | NPP-375D | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f0ab6fe4-7493-3d59-ad6b-328ffbdc36a8 | -5.32664 | -43.56809 | 2026-01-03 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33b39a7c-7cb2-3c29-a1b4-2357b96a5656 | -5.32153 | -43.56718 | 2026-01-03 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 73184eae-3da0-3101-8405-662410689c03 | -9.85576 | -36.17335 | 2026-01-03 03:49:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3979b50a-a1ba-3d01-95d5-ab95ef26201b | -8.08547 | -35.70734 | 2026-01-03 03:49:00 | NPP-375D | CUMARU | PERNAMBUCO | Brasil | 2604908 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 68e3f4ce-fcc5-3c32-be1d-97224ae0dba7 | -6.66221 | -38.97763 | 2026-01-03 03:49:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e4a1dc49-bbab-3b12-af32-610ca4ce66b8 | -7.02048 | -39.68429 | 2026-01-03 03:49:00 | NPP-375D | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 191679db-3732-3c4f-b4ee-b78b02bb3a34 | -5.85738 | -40.3467 | 2026-01-03 03:49:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8b46027b-97f3-3310-9ed3-f3241193dd6e | -5.32716 | -43.56505 | 2026-01-03 03:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5c31ab4-938d-3d27-8404-22c06c2f9d76 | -9.48299 | -36.03069 | 2026-01-03 03:49:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b785c5c4-0d12-3fc5-80ed-5025822127f4 | -7.58316 | -40.1026 | 2026-01-03 03:49:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d4d85d64-ee67-3f46-8213-54b44fdbbfc0 | -9.92203 | -37.17611 | 2026-01-03 03:49:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 56b219cf-25ab-3077-a243-22731211a080 | -6.66304 | -38.98019 | 2026-01-03 03:49:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 73713bb0-e41c-3992-acea-17d5c538f3bf | -7.45998 | -35.1078 | 2026-01-03 03:49:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 9dd65a08-58e8-384c-b378-7eb528757a8d | -5.71151 | -39.84771 | 2026-01-03 03:49:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c10bb4cb-5994-333e-a96e-cfa6f07604d3 | -15.37452 | -43.60524 | 2026-01-03 03:51:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ac941242-3e7e-3602-8cee-8e3588852e56 | -12.9528 | -41.17926 | 2026-01-03 03:51:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 273ccda0-e9cd-35a2-b3b0-0ae0c8f9c25f | -15.42692 | -39.53912 | 2026-01-03 03:51:00 | NPP-375D | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 32ceed66-d31b-3afb-b9af-ac21f574d720 | -13.47789 | -44.01524 | 2026-01-03 03:51:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| abcec86b-d0c4-3583-abbb-519fa0be8377 | -13.76667 | -39.01134 | 2026-01-03 03:51:00 | NPP-375D | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dee5eae0-3130-3f27-a103-d73e305cfe38 | -17.49831 | -41.5868 | 2026-01-03 03:51:00 | NPP-375D | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c7fef3e3-54cc-3369-a155-b376cffccd3c | -15.52525 | -43.55343 | 2026-01-03 03:51:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b911f5d-3ba4-305c-a637-306f4eb9010f | -16.24773 | -42.23357 | 2026-01-03 03:51:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 113efab6-8ea9-3714-a049-4dec8e589214 | -18.48404 | -39.8647 | 2026-01-03 03:51:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 05db74fc-e1ce-3b8a-b772-d9458d8b821c | -17.87749 | -39.76979 | 2026-01-03 03:51:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0df06714-f9e1-3fa1-b2cb-e7927b312b40 | -13.42833 | -43.85244 | 2026-01-03 03:51:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42dd26f1-89b7-30db-acf8-c2237b928b41 | -11.9581 | -41.29339 | 2026-01-03 03:51:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0f9c0945-1875-335f-974f-590b23b305b3 | -13.46693 | -38.94139 | 2026-01-03 03:51:00 | NPP-375D | CAIRU | BAHIA | Brasil | 2905404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 10d858c4-01ae-35a8-91e1-9cbe677ccf77 | -13.46411 | -38.93697 | 2026-01-03 03:51:00 | NPP-375D | CAIRU | BAHIA | Brasil | 2905404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4e5a73dd-9613-3ea4-8bad-c0bbe104f85d | -13.42745 | -43.85714 | 2026-01-03 03:51:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 674cd287-d725-3b89-a319-338c213932b3 | -15.52093 | -43.55283 | 2026-01-03 03:51:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f08c151-74b5-361c-9f98-24cd34f8898a | -13.43199 | -43.858 | 2026-01-03 03:51:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 094fc4ba-bb08-36ed-9454-8f9b800d222a | -17.12992 | -39.66207 | 2026-01-03 03:51:00 | NPP-375D | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 94b4d7f6-9007-3dfe-a992-c35339040a88 | -17.13056 | -39.65823 | 2026-01-03 03:51:00 | NPP-375D | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| df978191-86e4-3d26-84bb-bb3c17d24eec | -13.43286 | -43.85331 | 2026-01-03 03:51:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35cffc23-4bdd-3ec8-ad73-5da0fcda31d7 | -13.76322 | -39.01074 | 2026-01-03 03:51:00 | NPP-375D | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 07a9a738-e60d-33b1-b87a-706440c9a4ba | -15.78691 | -41.33438 | 2026-01-03 03:51:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4fcb2a30-3837-3381-b417-5448f0879ee1 | -13.47879 | -44.0105 | 2026-01-03 03:51:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0397e151-e71b-3e9f-8452-28b90c8e5301 | -15.42757 | -39.53526 | 2026-01-03 03:51:00 | NPP-375D | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c0bcb35f-6443-3823-ada6-7041d2cac998 | -15.03398 | -43.83432 | 2026-01-03 03:51:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e3f03a00-8d2b-304b-9848-20a42263174c | -17.50116 | -41.59222 | 2026-01-03 03:51:00 | NPP-375D | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d8231e37-9e37-3a5b-9a6c-1f18a7a806ec | -13.46475 | -38.93314 | 2026-01-03 03:51:00 | NPP-375D | CAIRU | BAHIA | Brasil | 2905404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cb17523b-d519-3c80-93e4-086850b283fd | -15.37588 | -43.60357 | 2026-01-03 03:51:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5d69ba3a-64e1-3086-b8f8-c1d7a3f26be2 | -17.19085 | -40.22587 | 2026-01-03 03:51:00 | NPP-375D | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b62ec231-402a-3b82-94a6-398b3064618c | -16.92146 | -40.1282 | 2026-01-03 03:51:00 | NPP-375D | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 746480cc-e873-3828-88f1-094f20d96b68 | -15.37529 | -43.60103 | 2026-01-03 03:51:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.9 |


[Clique aqui para ver as próximas entradas](README3.md)
