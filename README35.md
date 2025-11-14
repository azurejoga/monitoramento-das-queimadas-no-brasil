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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b36d87d-2a91-317d-8f9c-b1bf35ada39e | -14.69873 | -46.60832 | 2025-11-14 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c59129d7-8e87-3770-a8af-262a5b5e7618 | -12.27563 | -43.83624 | 2025-11-14 04:25:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8af8abf-d9d8-398e-b470-9143d6e57746 | -4.71087 | -46.44821 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8db86c67-2776-3487-896e-f4bcb3bdba0b | -13.73595 | -43.14293 | 2025-11-14 04:25:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 12e5525a-a6fb-32b9-b759-d8bd26d51f82 | -11.85226 | -49.21482 | 2025-11-14 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 52fd83d7-0607-3819-bfbf-3380190cb9cc | -12.82653 | -43.44572 | 2025-11-14 04:25:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9a0bc16-622c-3b4f-b0fc-23d251cf33e5 | -12.00852 | -46.76993 | 2025-11-14 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66ffcf01-8c85-3eb9-a87c-7f6ba953aae9 | -6.89707 | -42.08669 | 2025-11-14 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f559ebed-c50b-33db-af06-9f98fff43cb3 | -5.36172 | -46.28913 | 2025-11-14 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d380467d-7a12-3ea0-844d-6b9fd3afad72 | -5.3525 | -46.76292 | 2025-11-14 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9313b626-ab03-31a7-b992-1a47cf58185f | -6.14154 | -48.05092 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0a4cdd2-6b9a-3c77-b45f-6f5069d57adb | -5.71786 | -42.35397 | 2025-11-14 04:25:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6ac69c05-23f5-3572-b883-14e39c808c40 | -5.25365 | -46.18102 | 2025-11-14 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9826d321-ab02-36d7-bbfa-cc17d5e9ef48 | -5.02138 | -44.50739 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| badac8d0-1c5e-3b7d-92be-4d275a2deb2a | -5.42624 | -43.19756 | 2025-11-14 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72d3ee92-058a-3ece-8f1b-3f0441adeee2 | -14.69704 | -46.61902 | 2025-11-14 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0448a32c-d788-3d4c-a569-067ebcd66efc | -7.42167 | -39.10438 | 2025-11-14 04:25:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 814e30d8-4b67-3743-bb9e-5cc34af05c87 | -6.15911 | -48.05148 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 93046678-eade-3590-9c9a-36a8e601e159 | -12.08158 | -47.88525 | 2025-11-14 04:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 116e050a-578f-3973-801f-dddeb355e33e | -7.12153 | -42.72351 | 2025-11-14 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| de8d000f-75e2-3bd1-a99e-bc7056d679c5 | -11.85153 | -49.21909 | 2025-11-14 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| b5b0761d-4f30-3fa4-969e-5e61722b7cbc | -4.77435 | -46.45066 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 951ddec6-1919-3450-84ba-f586f508a19c | -11.94454 | -44.59517 | 2025-11-14 04:25:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 83127142-a61c-373c-b0e5-a987dea68aab | -12.71706 | -45.41848 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 971cbdc3-ebe6-3044-bf98-0c927044bb60 | -3.79638 | -52.0099 | 2025-11-14 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 98659ff6-5120-3b8d-8a2f-7c3439aa768f | -6.13348 | -48.05413 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d59cba76-497d-3daf-a4c6-65e646c67ded | -6.07655 | -41.54971 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c8e88e66-481f-30a3-8035-6444d04976fa | -14.34966 | -47.89286 | 2025-11-14 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 98982f44-5c13-3b4c-87fb-e3374b5a9424 | -6.97607 | -41.63512 | 2025-11-14 04:25:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5cbffa48-1559-3702-8a45-fbeaefdb6238 | -6.11151 | -41.59189 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a676954b-3c51-3a47-8355-e49ec286353c | -11.84863 | -49.21418 | 2025-11-14 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2f1906ef-6e06-32b1-a9ec-98f17724f078 | -5.06415 | -49.87564 | 2025-11-14 04:25:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfe7f305-bd6b-35ef-8a79-3f30a70337d2 | -6.98159 | -39.17112 | 2025-11-14 04:25:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 94fe1c79-4c05-30e8-9eb6-26012a5de63f | -16.54231 | -49.35648 | 2025-11-14 04:25:00 | NPP-375D | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8a0fa2d-8241-304e-9e26-cc79bfcc4ac8 | -6.8881 | -42.85889 | 2025-11-14 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 75e9a905-4e7a-3725-a6bb-2019419fd846 | -13.84976 | -46.90224 | 2025-11-14 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec3dbd69-3c22-32cc-8292-2ac2396115e2 | -6.08013 | -41.62936 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7d41dd65-c3bd-3b4e-b82d-53a08617d25d | -12.59346 | -48.33488 | 2025-11-14 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2fe4fd2-c816-3a79-8164-cfa53bcb24f1 | -14.98325 | -47.86735 | 2025-11-14 04:25:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b40d4c46-7ef3-35c1-b819-fa903079d20a | -14.31004 | -44.58257 | 2025-11-14 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3390c9c-d3b3-3326-bdf8-fe82e3017f1b | -12.59944 | -47.05094 | 2025-11-14 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80d1f0a3-1fe9-3044-9a67-2c4629300c9f | -7.00054 | -42.78314 | 2025-11-14 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7fc9b23d-6ddb-33a8-a2c2-f3ab3b12c06e | -14.70425 | -46.61656 | 2025-11-14 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca76a8b6-694f-3ce8-a50e-7350681db62b | -11.85444 | -49.22401 | 2025-11-14 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| c722aec7-eb57-3a23-8e10-f3e633df0f8a | -11.55947 | -44.94558 | 2025-11-14 04:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be0a559e-d2b1-3325-bb70-e911f52f8ab8 | -4.64379 | -47.94977 | 2025-11-14 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df0b7dc0-10c2-3f0b-aabb-7088d0b153c9 | -6.06915 | -41.57375 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7353ae5b-bdb0-37ce-aea3-2f5188746e76 | -7.14936 | -41.25107 | 2025-11-14 04:25:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b624fe8e-eb9f-3a23-b7af-0c873b61ce13 | -16.45148 | -45.01172 | 2025-11-14 04:25:00 | NPP-375D | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8645d0a7-5eb4-3a56-9ea8-713b9ef007cf | -5.90477 | -42.74607 | 2025-11-14 04:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eb34c1ed-951a-3988-b6d9-1aabac2349bb | -6.14321 | -41.6974 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c4ac79f3-4923-3d8a-ac3e-3365de7986a1 | -11.93004 | -44.71222 | 2025-11-14 04:25:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bed9240-08cd-3b3f-94e2-c759c0edca27 | -5.25005 | -44.7317 | 2025-11-14 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f70070e-db47-3d6f-b29b-0e1119dba854 | -13.68489 | -43.00512 | 2025-11-14 04:25:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fd614f2e-efb1-3073-af65-468bf24d472f | -6.28791 | -41.73272 | 2025-11-14 04:25:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 859c0e35-bb09-39a4-8826-d07b8ea2638f | -4.88223 | -49.38782 | 2025-11-14 04:25:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5337dcc8-b975-34ff-84e3-016b0da3f74e | -5.36915 | -46.28661 | 2025-11-14 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3704a3f8-e985-31a8-9a33-e949427f412c | -6.41366 | -39.75341 | 2025-11-14 04:25:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4f6fc0d2-0025-3ee5-92f2-8cfbfb5aa8e1 | -3.4164 | -52.7347 | 2025-11-14 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 443a8dad-f4bf-3105-8ff3-9225bfccbdd3 | -6.98143 | -39.17125 | 2025-11-14 04:25:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2c551e6c-b548-3112-b941-6e6f6aa11289 | -6.82746 | -43.16335 | 2025-11-14 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| afbbc6ff-5a33-3aa9-9d95-841366fd77dd | -12.43164 | -43.1789 | 2025-11-14 04:25:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11e2d0a8-29a6-3d27-a140-c8c72fa35671 | -3.86651 | -50.92226 | 2025-11-14 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb334326-a0c5-3dc3-affa-ef3ee61029df | -6.48196 | -39.34856 | 2025-11-14 04:25:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d4dda5d6-27d4-3865-9104-a3f2a4ad6939 | -6.0691 | -41.72727 | 2025-11-14 04:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6818f1b4-58dc-3da7-88c7-c6166cbd86e1 | -4.77647 | -46.45032 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50615752-e2c8-3e91-bcf6-6a8668a76250 | -5.75165 | -45.10641 | 2025-11-14 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5622e32a-b463-393d-8b21-e197b304d941 | -11.24335 | -47.49662 | 2025-11-14 04:25:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90ae91d8-9fab-3f1c-ba06-1f4ab7624320 | -12.04187 | -49.44102 | 2025-11-14 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8d2382e-44cb-3474-9f42-edc773d04e7f | -12.0091 | -46.76637 | 2025-11-14 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2fd3056c-72bc-3a1d-9263-37a36e2471d2 | -6.56681 | -42.12949 | 2025-11-14 04:25:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| eb9ce3f5-075d-3cc4-9920-7856f806557c | -5.75091 | -42.72305 | 2025-11-14 04:25:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d956e614-8cd5-36af-b2b3-98ab35dbf823 | -6.48252 | -39.34482 | 2025-11-14 04:25:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bd720258-4388-3ea2-9ea5-d1521ed102e0 | -5.74692 | -42.72622 | 2025-11-14 04:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 00107fde-eac9-3672-8932-ee67fa2d1ee0 | -6.88404 | -41.58033 | 2025-11-14 04:25:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6718fd78-e37b-378f-9ab5-d5c47aebf367 | -7.15349 | -41.27411 | 2025-11-14 04:25:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e8bd7ce9-f56f-3081-ae87-4fe10ac217b1 | -5.49818 | -41.91027 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 66a7e871-2c2f-3fc6-b411-c4f85b8ce5bf | -5.89734 | -42.7487 | 2025-11-14 04:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8145def7-196c-3266-92b6-1763f947930f | -5.78283 | -51.42602 | 2025-11-14 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf6a3318-78f2-38ef-b26e-9eb5bf5ace96 | -5.36795 | -46.29402 | 2025-11-14 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 839f2c21-0fdb-3678-aa42-d024298fa26e | -12.71205 | -45.42865 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 98d242df-d1ff-3ff7-8b8c-9feea8ee47e5 | -14.67661 | -46.89357 | 2025-11-14 04:25:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ec0ee2db-d1a1-3a74-aec7-71082d71e4ba | -5.52863 | -41.75688 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 95e9dc38-ee92-34fb-9b9c-4c705a6a62ae | -4.672 | -45.80228 | 2025-11-14 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33868217-f4de-3f4d-87ec-6b297ae9b098 | -5.89392 | -42.74816 | 2025-11-14 04:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 30df74f1-1ff6-310c-bfeb-315826b29268 | -11.5711 | -44.87036 | 2025-11-14 04:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64dcaef1-9082-3a3e-814d-e5ad2d736e96 | -6.08869 | -38.46351 | 2025-11-14 04:25:00 | NPP-375D | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c2a0b9a0-4005-33ab-a0fe-bc55f26f0bfd | -7.10971 | -44.071 | 2025-11-14 04:25:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 571ef81a-6061-3dfd-a7bf-0270341c3e78 | -4.41931 | -47.6008 | 2025-11-14 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 717e3e18-2441-3f38-9460-2b5286289bdb | -14.31234 | -44.5907 | 2025-11-14 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10212b58-63b7-3f51-88a4-12ce40b237fb | -4.9919 | -42.91426 | 2025-11-14 04:25:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d78dc25d-e93d-3233-a26f-b3c52a66dd93 | -14.92078 | -47.36118 | 2025-11-14 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c657f245-0a71-3d66-b2c6-a08c97d7739f | -11.7304 | -48.52116 | 2025-11-14 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f04609d2-54a2-3406-bd34-5f223dc2e460 | -5.5958 | -45.17495 | 2025-11-14 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f6e0202-34c9-3352-ac33-ae89637fc2b7 | -5.01636 | -47.69211 | 2025-11-14 04:25:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e671dcb1-a29f-39a3-81ae-e4c566981dbb | -5.61112 | -41.06464 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 91c746b0-aebd-3246-ba8c-2f1b8f62ccb1 | -14.9513 | -48.44336 | 2025-11-14 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46f4cf75-9413-36a1-87e0-b7b87344266c | -6.42821 | -47.30045 | 2025-11-14 04:25:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4c4cae99-1ffd-31ea-8d33-1434bc5312da | -13.97802 | -40.6029 | 2025-11-14 04:25:00 | NPP-375D | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d9705a75-9bb4-37c1-a5b8-b118da2575cc | -12.5955 | -48.3363 | 2025-11-14 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README36.md)
