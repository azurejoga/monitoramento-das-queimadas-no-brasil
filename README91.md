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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d945c2a0-9530-3a19-a1a1-aac70f122079 | -3.6019 | -43.6099 | 2025-10-28 14:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| c134079c-604d-3bf4-b38a-c9854f1a15b0 | -4.3239 | -41.7839 | 2025-10-28 14:00:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 9d64fdf2-0059-3cc4-912b-2da621e0018c | -7.2758 | -44.9606 | 2025-10-28 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 26c51c17-e457-37cd-81f6-9b1102d2d43b | -12.3484 | -50.1779 | 2025-10-28 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| e815da95-dce7-3f71-83b2-d66d8b3b2e6b | -3.5645 | -43.6348 | 2025-10-28 14:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| ad9c38cb-8f41-3b63-ae5d-b9d5d5c96837 | -6.783 | -45.4347 | 2025-10-28 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 0832d8d3-b75e-3570-a5e7-f73ff8d975f6 | -6.0974 | -44.6718 | 2025-10-28 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 205.9 |
| 6a13e46b-e1f2-308b-bc2b-6cf0abb4aac6 | -6.0786 | -44.6733 | 2025-10-28 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 171.0 |
| a11488a0-2cbb-3eec-bb09-2c390b3db1b9 | -7.1227 | -47.0154 | 2025-10-28 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| dd664a9b-52fa-331a-ac9f-2c71c401de1e | -7.3613 | -42.4399 | 2025-10-28 14:00:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 63.8 |
| 05dde010-a674-3b4c-9c97-b62f409603ac | -14.542 | -48.0012 | 2025-10-28 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 52280ee5-8ba0-3ba1-ad6a-320296de80f9 | -13.9143 | -48.4335 | 2025-10-28 14:00:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 290e0b9d-f2aa-315a-a04a-7bd3c37d84c8 | -3.0759 | -44.4369 | 2025-10-28 14:00:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 77.1 |
| d6725034-7f16-3b54-b33f-019be624928a | -7.7783 | -45.3911 | 2025-10-28 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| a84ff57d-9a77-3b63-898e-1e9c5e71c027 | -13.5655 | -49.5845 | 2025-10-28 14:00:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| af188760-aadc-399a-b640-581b00490845 | -12.8299 | -47.7254 | 2025-10-28 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 01f0327d-33e9-3250-a1e9-e5b25c60eb9b | -4.7346 | -44.4457 | 2025-10-28 14:00:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| d0b78b14-28fd-3687-9395-961ccc49c323 | -3.5833 | -43.6108 | 2025-10-28 14:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 188.0 |
| f86ebd96-2fe5-3d1f-b229-cae76ebc6518 | -13.4786 | -48.0096 | 2025-10-28 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 2fd647da-6d3a-3f5d-a427-c2828807281e | -12.8303 | -47.7031 | 2025-10-28 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| b6a98521-97a8-3207-8bc9-bcd13e2b94ee | -7.218 | -46.8527 | 2025-10-28 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| b04da490-8f2a-313f-8fc1-0b9d300a52aa | -13.6435 | -46.4519 | 2025-10-28 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| cf3242ca-924d-3340-badc-4a63328a4e30 | -13.9337 | -48.4305 | 2025-10-28 14:00:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 8bf9750c-3a46-3b40-a08f-62b0ac7a01e9 | -7.4888 | -46.0716 | 2025-10-28 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 684ad09d-3b16-3dcc-9a24-bf04293637c4 | -7.0881 | -44.9547 | 2025-10-28 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 62751a66-07b5-3395-a19a-66d68338a2d4 | -15.1964 | -47.3964 | 2025-10-28 14:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 060e7774-3165-3ee1-8ea9-2b4f847aa77c | -13.9465 | -47.7595 | 2025-10-28 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 151.3 |
| c3385eec-aba8-3f48-afe7-76f277d4a521 | -13.6241 | -46.455 | 2025-10-28 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 5b941a51-9e8f-3643-885b-046feb1986bb | -13.9275 | -47.7401 | 2025-10-28 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| d66bf002-cdb5-3ed4-8148-2a7739a46c2a | -3.5646 | -43.6117 | 2025-10-28 14:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| dddaefa4-d373-3664-a3d9-5b61544c1081 | -4.8933 | -43.2349 | 2025-10-28 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 4a16c421-0b8f-3391-bdec-78944481af08 | -6.6224 | -44.6296 | 2025-10-28 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 71938e37-9c62-3918-a2e6-aefe36048d3e | -7.7489 | -44.6873 | 2025-10-28 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| a16e28cb-1e0d-3f21-a70b-0198a765e0a1 | -13.2262 | -47.084 | 2025-10-28 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 140.8 |
| f7fc45b3-68e5-3ee8-be2c-60710bcd2a9d | -6.3697 | -38.3819 | 2025-10-28 14:00:00 | GOES-19 | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 105.3 |
| 21e3dcf1-a45a-38fb-9bc9-68b887d6e755 | -13.6237 | -46.4779 | 2025-10-28 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 324.2 |
| e4d53947-6b33-3607-8fc6-206bff1df23b | -14.2491 | -48.1148 | 2025-10-28 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 3038b525-66cc-3f80-b79f-7a4ab6ebd9d0 | -12.5489 | -49.5901 | 2025-10-28 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| e92278b3-ef2f-324f-8eeb-d3a107c33f22 | -13.2691 | -47.8846 | 2025-10-28 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 7f512fb9-6591-372e-a53a-547b4c6e54c1 | -13.6431 | -46.4748 | 2025-10-28 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 148.3 |
| f6551879-7a5f-3b1c-b3c2-46f0c16aae37 | -14.9045 | -52.4354 | 2025-10-28 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 34c2d21e-2b7d-3d76-93cc-ff5e8a910d20 | -3.2611 | -44.6345 | 2025-10-28 14:00:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 1cf96ab7-f189-3490-84e6-e1762310f234 | -3.7075 | -41.556 | 2025-10-28 14:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 164.8 |
| 26679264-c7d1-3454-ac9f-b65790aa354e | -5.6055 | -41.1145 | 2025-10-28 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| 5e564f86-f6f4-322a-9375-f638435bca0e | -13.9469 | -47.7371 | 2025-10-28 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 596f28cf-95cf-39a3-8483-957b8bc77b67 | -5.6617 | -41.1341 | 2025-10-28 14:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 91.6 |
| b5d176dc-1d79-380f-abdd-90abff223f58 | -7.5928 | -43.5699 | 2025-10-28 14:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 0c5dbc12-9be5-3a9f-bd62-9cd2061e82ff | -14.2975 | -52.9366 | 2025-10-28 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| d6d0ede3-b1fb-3104-9817-1c3952fb3819 | -3.2795 | -44.6793 | 2025-10-28 14:00:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 7190745f-d63d-3897-a4f4-e0ab6c1fcdbe | -13.2258 | -47.1066 | 2025-10-28 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 87.2 |
| ba4a7a4b-afc2-348f-9d67-a454d2e49253 | -6.8822 | -44.9043 | 2025-10-28 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 80169429-63ea-3ccc-b8ee-b8d7e64996f5 | -7.9655 | -45.4637 | 2025-10-28 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 4c1f1402-9cf7-3150-980a-e74e313a7747 | -7.9693 | -46.7423 | 2025-10-28 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 8bf904c2-9344-3c6e-be3a-e0092aa5af18 | -3.7075 | -41.556 | 2025-10-28 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 158.2 |
| 70ad1e3d-4678-3c0c-9755-10d842d16b1e | -8.185 | -44.4593 | 2025-10-28 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 43dc79e8-a6ef-3a07-a038-2f216075a368 | -12.5298 | -49.5926 | 2025-10-28 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| e5ef31af-e28e-3848-9ee1-c89c7539eb12 | -15.1964 | -47.3964 | 2025-10-28 14:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a42affc7-a721-31ee-a242-edbba08af0ab | -13.9465 | -47.7595 | 2025-10-28 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 127.1 |
| f81f9070-5da0-3325-acfb-4fa27fe1eb74 | -7.7489 | -44.6873 | 2025-10-28 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 7fd44a79-50e8-3971-aeab-5bca652a3290 | -3.0148 | -41.6851 | 2025-10-28 14:10:00 | GOES-19 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| 9fe19057-9763-3e75-98be-689f422d7db1 | -4.7252 | -43.1991 | 2025-10-28 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 16171299-b18a-39e6-a295-13026ae8a50f | -7.4583 | -47.1641 | 2025-10-28 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 120.3 |
| fc6c7842-36ae-3f40-9682-519c92870bee | -4.3423 | -41.8306 | 2025-10-28 14:10:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 90314a42-864e-3519-b160-cdcedeac1a1f | -7.2755 | -44.9834 | 2025-10-28 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 9feccaa2-128f-3789-ba47-7d2d2ea13732 | -7.9467 | -45.4655 | 2025-10-28 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 5b4bf8a5-5719-396b-9b8d-c68fb6ac9e32 | -8.6065 | -45.4212 | 2025-10-28 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 90dd6ee3-ea24-33aa-bcdf-6b723e71f537 | -8.646 | -45.2806 | 2025-10-28 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 6b4cf5d1-0cbb-373d-973d-0c7a2ae5525f | -6.8822 | -44.9043 | 2025-10-28 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 3e8e1833-578a-3da6-92ae-b8ccf2f57c00 | -7.4888 | -46.0716 | 2025-10-28 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 7ffc2b29-db95-3860-a78f-5a28e2ed31cc | -6.0786 | -44.6733 | 2025-10-28 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 05c5d579-be34-3dc0-a1ea-cb13bf2fd1f6 | -3.7147 | -40.4172 | 2025-10-28 14:10:00 | GOES-19 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 82.1 |
| 9e6b29bf-2d03-36b0-86cc-f9fe5739ed30 | -12.8299 | -47.7254 | 2025-10-28 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 5cb4fcb1-58c4-35cb-aba7-792136232d6f | -4.5659 | -47.317 | 2025-10-28 14:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 105.1 |
| e4d263bd-ad92-3585-a6c8-ab6c2117ab01 | -3.234 | -42.6473 | 2025-10-28 14:10:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 8ff353c3-0ade-3c44-9a1e-e5dc4c97549f | -8.1853 | -44.4363 | 2025-10-28 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 7b95b854-fe6e-3d92-ab94-f110d4ec3d88 | -3.2232 | -48.7594 | 2025-10-28 14:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| c2f57ded-ac34-3eb0-bcfe-6c05c8090fa9 | -14.3934 | -51.8226 | 2025-10-28 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 5f816733-5097-3e31-85f4-70ed220f7384 | -7.3613 | -42.4399 | 2025-10-28 14:10:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 6c5a7a1d-d613-3203-ad6f-70186bb6c59e | -3.5831 | -43.634 | 2025-10-28 14:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 125.2 |
| cd8d43bb-46e5-3395-afa8-80d55e4ccaa3 | -7.218 | -46.8527 | 2025-10-28 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| d5f0955e-208f-3a3d-9886-7b186c1fde55 | -8.6334 | -44.8021 | 2025-10-28 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 2443dddb-518e-3501-9b56-bc345a346a88 | -4.3239 | -41.7839 | 2025-10-28 14:10:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 4955ca94-5288-3e21-85ed-dc56a3c3a980 | -5.6055 | -41.1145 | 2025-10-28 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 8b57cd44-5047-33a8-811d-5d419a7ca491 | -12.5489 | -49.5901 | 2025-10-28 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 25ec0f62-848f-3bea-8bdc-861290e92004 | -13.9337 | -48.4305 | 2025-10-28 14:10:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 244be956-037f-39f1-a4dc-682cfa311387 | -6.6707 | -45.4214 | 2025-10-28 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 92bbe255-70f9-357e-a6b6-7c44f0ff7976 | -5.6617 | -41.1341 | 2025-10-28 14:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| d84662ba-a6ee-3084-aed0-43a128b5fb76 | -7.2758 | -44.9606 | 2025-10-28 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| c77b7e3a-7308-346f-a2c3-84daaa574ed5 | -6.2755 | -41.8282 | 2025-10-28 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 3672926a-5a17-35d7-87c7-c1764566065e | -7.7783 | -45.3911 | 2025-10-28 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| c1bc7fb5-c653-3496-9425-e7d1a51a99ab | -8.0447 | -45.1378 | 2025-10-28 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 2598d5a6-74a8-3d2a-ab62-a629f0165191 | -6.0974 | -44.6718 | 2025-10-28 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 224.2 |
| 086d1d7b-f762-3984-8959-02f3289a510b | -14.8851 | -52.438 | 2025-10-28 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| b5733c06-a776-3a3a-8318-d7bf3796194d | -3.7261 | -41.579 | 2025-10-28 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| ffbb524f-cb3c-3ff8-94d7-82f9106437d4 | -8.4689 | -45.8655 | 2025-10-28 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 5941eead-85e1-33b7-9caf-fcffb3beb97e | -7.1227 | -47.0154 | 2025-10-28 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 241ae3ca-3b4d-3f43-b7f5-5cef9e43a743 | -7.9696 | -46.7201 | 2025-10-28 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 2a95a579-5d07-3383-a0dc-ba3cdc403f77 | -8.0444 | -45.1606 | 2025-10-28 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 20c40dd5-98e9-34ed-b4cf-420a98601128 | -3.7101 | -47.6403 | 2025-10-28 14:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 130.9 |
| b0d03453-a9e5-3685-8baf-a20c27e6705b | -13.9143 | -48.4335 | 2025-10-28 14:10:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 115.0 |


[Clique aqui para ver as próximas entradas](README92.md)
