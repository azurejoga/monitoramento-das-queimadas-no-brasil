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
| c4dd0145-dc82-3e9f-95a2-29cc702f51d3 | -21.51801 | -42.26448 | 2025-11-22 04:50:00 | NOAA-21 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 5415d240-e590-37ce-a384-4cc03b6a40cf | -20.88806 | -52.34016 | 2025-11-22 04:50:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8cfabef9-69d8-39d1-a185-810509f351f5 | -29.95223 | -51.61604 | 2025-11-22 04:53:00 | NOAA-21 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 75f21c63-820e-3aa9-9554-f8c6ae0e06fe | 2.54404 | -60.57433 | 2025-11-22 05:12:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 022f1162-287e-392d-a5b3-063e79f5368a | -1.6044 | -47.01931 | 2025-11-22 05:12:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e5ef3d1-8019-3555-a92b-616a5335b719 | -1.85434 | -47.48006 | 2025-11-22 05:12:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7230aa56-398c-3001-b06f-4a27d3a14904 | 3.26645 | -51.19767 | 2025-11-22 05:12:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95eed9f5-eba3-3f3e-8f31-ed35341ac800 | -0.96938 | -47.56358 | 2025-11-22 05:12:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db15ae0a-d6cf-39ca-b3f1-c5ba32873e41 | 2.54348 | -60.57065 | 2025-11-22 05:12:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cae4b789-c167-3475-a854-1e9d542b443f | 3.98736 | -59.6161 | 2025-11-22 05:12:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d47457c-5195-3bac-b8b6-dd3458541720 | -0.96986 | -47.56045 | 2025-11-22 05:12:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be66cc9c-e133-3488-a5bc-4a591e9586cf | -2.93361 | -48.23312 | 2025-11-22 05:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f591a82d-d3cc-3682-8816-9d972d32f997 | -2.63946 | -47.38405 | 2025-11-22 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75f12103-8d3a-343f-a462-b9d90bbf6b08 | -2.93317 | -48.23603 | 2025-11-22 05:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 85eaa844-5fc0-3305-bd5a-ce172dcecee4 | -2.91882 | -48.22766 | 2025-11-22 05:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5edac243-fc12-3f22-8877-5e70e8f136b6 | -2.91837 | -48.23064 | 2025-11-22 05:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb9deb59-a960-31e6-aaab-7fbd1e8c3359 | -2.69394 | -45.10701 | 2025-11-22 05:14:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84cb7efd-8f22-365d-aa8a-f640ef58bfc2 | -3.2185 | -52.45773 | 2025-11-22 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f136e721-886c-30e3-aa54-9da000168abc | -2.92853 | -48.23232 | 2025-11-22 05:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 6f477117-8220-37cc-8be9-8a9acd4fca1b | -5.67085 | -55.7543 | 2025-11-22 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2712e99e-8148-31a0-b2be-58309f3bd6cd | -2.923 | -48.23443 | 2025-11-22 05:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| a2137e97-0e99-39d8-80c2-973df63120a6 | -2.63996 | -47.38072 | 2025-11-22 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 590ce602-c71c-3651-94bc-69c80559f1d2 | -2.92389 | -48.22851 | 2025-11-22 05:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 11029bdc-2250-3c58-bb3c-ade83039bdb3 | -3.34381 | -53.27676 | 2025-11-22 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb114d73-7c1b-332e-b214-3e1209a44029 | -2.92897 | -48.22939 | 2025-11-22 05:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 72a513c0-2b98-3939-8b4a-d5a09c503b22 | -5.04732 | -56.4973 | 2025-11-22 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7d41ee7e-134e-3498-926d-f97a111ba4fa | -2.69464 | -45.10221 | 2025-11-22 05:14:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 521f867d-b1d1-32d9-b401-46c0a4fa8745 | -3.46427 | -52.23268 | 2025-11-22 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 098f9041-0239-30ac-bfa1-99eee6794ed5 | -2.92434 | -48.22552 | 2025-11-22 05:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 48ca00ef-d36d-3168-81be-2dd6637d637a | -2.46962 | -47.83012 | 2025-11-22 05:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db32946b-5803-33fd-aa2c-ed9361d25f64 | -3.79947 | -51.14436 | 2025-11-22 05:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 992791b4-1d8a-3089-93ba-4dc3b033a315 | -2.91792 | -48.23362 | 2025-11-22 05:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55aaf7ce-708b-387b-a545-132d51121ef0 | -2.92345 | -48.23147 | 2025-11-22 05:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 01b140ed-c3d2-3617-ae3e-bfde9140893e | -2.93405 | -48.23019 | 2025-11-22 05:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 03f0af2a-47eb-39ae-a11c-1c711014ccb7 | -3.45766 | -47.62835 | 2025-11-22 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cdd6ed0-8457-32dd-8e64-7b6667e2245d | -2.91927 | -48.22465 | 2025-11-22 05:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5da07a31-be5b-3d71-9d08-10270c116064 | -2.92764 | -48.23818 | 2025-11-22 05:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5271ddb6-d270-31d6-a7bb-cf275799f6dc | -3.02028 | -53.96899 | 2025-11-22 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2afdbcc5-0773-3312-8c97-9ad2b98c7b66 | -3.74791 | -52.07651 | 2025-11-22 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82d64453-0666-3a37-8178-f091aae9d707 | -6.22299 | -55.63697 | 2025-11-22 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0ee4488-56e4-3b6e-a0f6-51863f2a8807 | -3.74868 | -52.07148 | 2025-11-22 05:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5421f29b-6b07-30d7-be6d-9ea31e177aa1 | -2.92808 | -48.23525 | 2025-11-22 05:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| fff16013-6385-3f0a-9468-aa8437b2077d | -1.65757 | -52.10583 | 2025-11-22 05:14:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44d821be-3c27-3099-9198-152a985b93ab | -3.34315 | -53.28104 | 2025-11-22 05:14:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3882c1da-04b1-38d2-b385-6cad84adede7 | -4.36968 | -55.77029 | 2025-11-22 05:14:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa5dec9e-cde0-3087-8640-c3d9643f9a5f | -3.01675 | -53.96844 | 2025-11-22 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02d8ec01-8709-3184-99e2-7313ffde27cd | -3.45718 | -47.63153 | 2025-11-22 05:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0716013d-d842-32b6-a402-89de3552dda6 | -2.92941 | -48.22643 | 2025-11-22 05:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 1705dffe-f724-3f99-8390-d2a7c967a798 | -9.77543 | -67.04942 | 2025-11-22 05:16:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86832b1f-4137-3121-8dba-59259d67d634 | -17.0705 | -46.59628 | 2025-11-22 05:16:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39fabdd9-545c-3633-be1b-da92099f74c0 | -9.78063 | -67.05043 | 2025-11-22 05:16:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 747639c9-eef1-394d-816f-6d0e61450512 | -9.78065 | -67.05082 | 2025-11-22 05:16:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 29a494c6-f41d-3b03-b8bf-6128bef270d3 | -17.07247 | -46.59562 | 2025-11-22 05:16:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f7ddca8-f6ff-3a6d-8396-dea19cb538b7 | -10.06921 | -63.06285 | 2025-11-22 05:16:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbec5f95-6548-321f-b143-69e0662cddb0 | -9.25192 | -60.33366 | 2025-11-22 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44eefa65-0903-3db3-8a11-9f06d8828867 | -10.64535 | -61.38673 | 2025-11-22 05:16:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7291d0a7-3762-38ec-b2f4-3528a57bcae6 | -9.77544 | -67.04983 | 2025-11-22 05:16:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c422655b-3222-3a60-94e5-37b3229febe7 | -17.06989 | -46.60252 | 2025-11-22 05:16:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de6eb158-d5a4-3907-b4d0-b2fbf86c4607 | -10.07318 | -63.06358 | 2025-11-22 05:16:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac234d13-f81a-3840-b699-a7eb186b4cb0 | -17.0719 | -46.60186 | 2025-11-22 05:16:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3e363b1b-7241-30f7-b546-595138e32ea9 | -10.79914 | -49.29708 | 2025-11-22 05:16:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ba79cae0-1d98-3ba9-845e-16c757da978b | -20.88654 | -52.34418 | 2025-11-22 05:18:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e408dbc5-919b-397a-942a-586292d7f7e2 | -18.09609 | -54.52049 | 2025-11-22 05:18:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bda3244-60bc-3a35-8232-45cc1059b72e | -20.88306 | -52.33824 | 2025-11-22 05:18:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ead5bc1-8807-38ea-8dd8-1eea2dcdeaff | -20.88157 | -52.34369 | 2025-11-22 05:18:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 63d2de18-55d3-3c5e-9b7e-de78a4ec23e1 | -18.09658 | -54.51664 | 2025-11-22 05:18:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f2f6d23-debc-378c-a06c-6a954956a949 | -20.88245 | -52.34407 | 2025-11-22 05:18:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c8527717-bab3-37f7-87dc-917a28fdb52c | -18.51075 | -54.92355 | 2025-11-22 05:18:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39fabb74-3306-32cb-974b-0566636ae6f4 | -20.24433 | -56.62217 | 2025-11-22 05:18:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c08a68db-63b4-37a6-8f68-eb0478ac6745 | -20.24924 | -49.33973 | 2025-11-22 05:18:00 | NPP-375D | ORINDIÚVA | SÃO PAULO | Brasil | 3534203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c65ab802-605c-308d-84e1-4861eef02458 | -17.8651 | -54.50235 | 2025-11-22 05:18:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 69a5ed87-54fe-39b8-88c1-584fdd8b5d0e | -18.11264 | -54.52299 | 2025-11-22 05:18:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af76860c-e3bc-369a-876a-8072b8596585 | -20.88804 | -52.33873 | 2025-11-22 05:18:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 510cab8b-65f8-38ac-83ac-346344f5cdd1 | -17.86737 | -54.50174 | 2025-11-22 05:18:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b8ba5f5-77e7-3355-ab6b-40352220d48a | -20.25138 | -49.34079 | 2025-11-22 05:18:00 | NPP-375D | ORINDIÚVA | SÃO PAULO | Brasil | 3534203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d5fd4ef0-6b62-3de6-b4c5-d7ae70282417 | -21.96033 | -56.46727 | 2025-11-22 05:18:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9872214f-778c-3df3-9b08-2b8ce89ac624 | -20.25178 | -49.33642 | 2025-11-22 05:18:00 | NPP-375D | ORINDIÚVA | SÃO PAULO | Brasil | 3534203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1bbe4db5-0a06-343b-ba7f-79657a5c4e6a | -20.88743 | -52.34457 | 2025-11-22 05:18:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9500be5b-3aad-3ba9-b178-2708cd2cac45 | -18.1085 | -54.52239 | 2025-11-22 05:18:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a95e35fa-1981-314c-9688-bbc065675b35 | -21.97211 | -56.77948 | 2025-11-22 05:18:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cab57a73-fe2d-3a07-b59f-77cb6e3e1fb0 | -20.88221 | -52.33786 | 2025-11-22 05:18:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eb1c38a0-c67f-3cb5-b322-27cd5a94e894 | -20.88719 | -52.33835 | 2025-11-22 05:18:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7b5ecc5b-fe7f-3fa3-804d-56668f666430 | -23.23788 | -51.28254 | 2025-11-22 05:20:00 | NPP-375D | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8bebf5c0-006a-3458-bb50-165dac4837d8 | -23.23752 | -51.28643 | 2025-11-22 05:20:00 | NPP-375D | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 61a81179-df47-3b43-9775-c7346b42a0e1 | 2.54685 | -60.57339 | 2025-11-22 05:33:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c9370e2-6b94-3183-8c52-78029244052a | 0.64065 | -59.92764 | 2025-11-22 05:33:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 307f9fba-489b-3af2-b9e6-ee9e0ba4625a | 3.11159 | -60.76834 | 2025-11-22 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0b28ca58-48a0-3c7a-ad8b-126d5d369a2d | 3.11491 | -60.76783 | 2025-11-22 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e9f55ec7-bf08-32b6-8302-72b472d290fb | 2.54351 | -60.57391 | 2025-11-22 05:33:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7115e155-e247-3f0d-944b-9f58eba3b718 | 3.98977 | -59.61713 | 2025-11-22 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c8bcc9d-59cb-3dc7-9b5e-704e675246ad | -9.41886 | -63.72364 | 2025-11-22 05:35:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e352d826-87bf-33ce-b6f6-4b88ff4376dd | -9.24849 | -60.33195 | 2025-11-22 05:35:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| def8d789-de39-3079-ac1f-1727e0433623 | -9.42218 | -63.72416 | 2025-11-22 05:35:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fcbc739-6537-38e9-9bc7-15b66a57c1c2 | -9.88136 | -66.85606 | 2025-11-22 05:37:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d0aca7f3-8a0e-3c5a-84bf-4489a5f710bb | -9.23086 | -65.74429 | 2025-11-22 05:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70d43674-537c-34f1-87d6-cc28c489738a | -9.82185 | -63.24739 | 2025-11-22 05:37:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b66ef0b4-b73a-3ece-b320-302a29c3fb9a | -10.07078 | -63.06318 | 2025-11-22 05:37:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a7d0b8d-6c6b-35ae-8f4e-f722785b75cb | -9.22692 | -65.74734 | 2025-11-22 05:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b24b0677-7305-3a25-935e-700272a19f74 | -9.79217 | -64.63481 | 2025-11-22 05:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 5cdda326-dc72-37ad-84cd-c232f78e47b2 | -9.51877 | -67.42631 | 2025-11-22 05:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README9.md)
