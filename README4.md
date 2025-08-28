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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94d98d21-0f2d-3918-9c52-48f1e26a5111 | -6.17245 | -44.06992 | 2025-08-28 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| b6fc2c8e-ed8c-38ea-b457-dd9a29bd931f | -4.15595 | -43.88366 | 2025-08-28 00:11:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 8fea2cbe-bba9-3c35-9739-1b32c322d7a4 | -7.38447 | -47.03829 | 2025-08-28 00:11:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 797aff3a-ee34-3f3c-9bf3-e3ed1847a40c | -7.06872 | -44.36308 | 2025-08-28 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 006c2ee8-ac38-3fa6-a63b-fba082fd7626 | -4.80525 | -47.26025 | 2025-08-28 00:11:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 7794d64d-d28e-3f0f-8526-8f2a6340970e | -2.97945 | -48.60399 | 2025-08-28 00:11:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 907ca56a-ca42-3235-9715-1762c92ac3eb | -5.53519 | -42.66018 | 2025-08-28 00:11:00 | TERRA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 60f4104c-9891-3c11-95cc-424286c859fd | -6.15978 | -44.04395 | 2025-08-28 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a387afc0-1f18-35e5-acad-2fd90568efb7 | -7.42537 | -42.06454 | 2025-08-28 00:11:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| b0e50a18-0361-3da0-97d5-6ae8daeef1bb | -7.38624 | -47.05198 | 2025-08-28 00:11:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c929c6ad-4b1c-3cfa-bd7b-ecb44331fa26 | -7.22192 | -45.31621 | 2025-08-28 00:11:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 66705a8d-1503-3205-8667-972bb83dc40f | -5.2126 | -44.32686 | 2025-08-28 00:11:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 69000007-0184-3fd5-8e78-b992927699ac | -5.20238 | -44.31897 | 2025-08-28 00:11:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 2b6f5f48-30ee-318c-9541-c2c06f2932ce | -2.12851 | -48.00788 | 2025-08-28 00:11:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f1b30ccf-a8bd-3093-baed-96cd2bb2a3fd | -7.78346 | -43.18679 | 2025-08-28 00:11:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| be5d7990-e674-31e5-9e91-278fd05436e8 | -2.9814 | -48.60941 | 2025-08-28 00:11:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b7ce3e1b-5085-347d-9066-147c77fb42b4 | -5.20363 | -44.32812 | 2025-08-28 00:11:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f5a87d39-4c11-369d-ba2d-8a29bd7b29ba | -6.08062 | -44.00565 | 2025-08-28 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 160e369f-5951-3a6b-9700-15577c6af04d | -6.4336 | -37.1331 | 2025-08-28 00:11:00 | TERRA_M-M | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 0b4e871e-6d19-3268-a515-2ba831686734 | -6.88364 | -43.61771 | 2025-08-28 00:11:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 35ed8261-416c-3d45-8eee-82886ec146d8 | -5.195 | -46.07523 | 2025-08-28 00:11:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 65a52681-85d9-3860-882d-b78fb507783e | -4.08646 | -48.05011 | 2025-08-28 00:11:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 0e91e6de-3ef4-3649-bae3-e13f7f614f60 | -5.68684 | -40.97969 | 2025-08-28 00:11:00 | TERRA_M-M | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| fe152952-44cf-3789-bb27-1f3f3dc2d6ae | -6.16102 | -44.05302 | 2025-08-28 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d6607c20-e9ff-351c-b446-b551a97eccf2 | -7.2869 | -49.25483 | 2025-08-28 00:11:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 244c63f0-788a-361c-9e6c-a8557d38d63b | -3.73436 | -40.26729 | 2025-08-28 00:11:00 | TERRA_M-M | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 52.3 |
| 3801313d-6213-33db-b1ad-a9fd722d762b | -6.87352 | -43.60999 | 2025-08-28 00:11:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 33.0 |
| ce0f0354-b4f9-3c4f-bf4c-94cf7a9aee8c | -7.05961 | -44.36431 | 2025-08-28 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 844cb035-08fb-324b-856d-d17b9d796e9e | -6.0794 | -43.99673 | 2025-08-28 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 993cc803-a873-3cf7-af8d-c527e687c432 | -3.98461 | -47.87647 | 2025-08-28 00:11:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 5d57659e-5009-3fb7-a38a-3d6390882d39 | -6.81047 | -44.35904 | 2025-08-28 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1cbb9291-983d-33d5-bd43-43e934bdbe1e | -7.94902 | -43.93139 | 2025-08-28 00:11:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 21cc1dff-fa09-3474-af64-e716f45d8ab5 | -6.33218 | -43.75882 | 2025-08-28 00:11:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 31c98bb2-ecef-3553-9106-0db9eeba6631 | -7.42741 | -40.09245 | 2025-08-28 00:11:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 2c0389a0-b4d1-327b-bbe6-758884b9bdbf | -7.63067 | -42.68079 | 2025-08-28 00:11:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 093da5d9-94de-382d-95be-a7dad9c58909 | -6.43759 | -37.12595 | 2025-08-28 00:11:00 | TERRA_M-M | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 36.1 |
| 68254a3d-9a3a-3c7c-b95c-6ec13c58f0ee | -3.19146 | -43.90023 | 2025-08-28 00:11:00 | TERRA_M-M | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 03e6c3bc-3b3e-3acd-8da0-f238a2063a0d | -5.67035 | -39.07079 | 2025-08-28 00:11:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 54ee1b38-682a-3564-9e05-a4e6205e8931 | -6.16176 | -44.39688 | 2025-08-28 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 12136650-c0c5-303e-ad92-94562615f31d | -4.08709 | -48.04354 | 2025-08-28 00:11:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| e652b7b7-45a1-3c24-8ff7-a2f0b13810ce | -5.55005 | -45.37767 | 2025-08-28 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2b1136c4-3649-30d8-bd7d-6d9fce37da90 | -6.33094 | -43.7498 | 2025-08-28 00:11:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 839fdf76-2698-3481-ab5f-39ae11000cdd | -7.42586 | -40.08192 | 2025-08-28 00:11:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 162.6 |
| 5b3550c4-f256-3f37-9734-383d88688f09 | -6.18493 | -44.16135 | 2025-08-28 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5870854c-841a-388a-9ab0-da23765c29f3 | -3.75999 | -49.0557 | 2025-08-28 00:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 05370bae-2c45-36b3-b29c-a4aff48999bb | -7.18277 | -44.87402 | 2025-08-28 00:11:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8a42669b-eb03-317d-8320-9650e47b6b68 | -3.59946 | -49.45264 | 2025-08-28 00:11:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 76e57dd5-16e7-3d5e-bac5-4896a3ad1486 | -3.98649 | -47.89075 | 2025-08-28 00:11:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 3b52235f-24ab-30c7-9707-c8d9991e3293 | -5.23291 | -39.37564 | 2025-08-28 00:11:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| e77e3732-80db-3d95-ad8a-3c37e3dc4e2f | -6.16225 | -44.06207 | 2025-08-28 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d2abde32-7ca3-37d2-83cf-e8c261cb00fc | -7.78224 | -43.17787 | 2025-08-28 00:11:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 84a2bef7-e208-3137-aa37-e2f38ac4ec21 | -7.41627 | -40.08337 | 2025-08-28 00:11:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 24.3 |
| ba5fbbb2-91e3-3a3d-882e-fec28f833d42 | -6.44433 | -44.57846 | 2025-08-28 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 8a13a664-eae8-3411-9970-460603fc9812 | -6.22277 | -43.35666 | 2025-08-28 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 9c9e97db-077e-3f26-8141-6ee679d7fb41 | -6.15144 | -44.38892 | 2025-08-28 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8c5a5332-d49c-31ef-a416-121ff59b5016 | -6.49702 | -53.3954 | 2025-08-28 00:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| db1fc58b-e662-344d-851e-7aceb4c7b47d | -7.7911 | -43.17664 | 2025-08-28 00:11:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| abecdc9b-6333-3d1e-b141-dc3218d69625 | -7.63434 | -42.70733 | 2025-08-28 00:11:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 2b07bdb2-ff22-37b8-aba7-fe253607e0c6 | -3.23908 | -43.4492 | 2025-08-28 00:11:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1d978689-1bf8-3003-950f-508f1e90d54a | -3.75458 | -49.06183 | 2025-08-28 00:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 13ecca3b-e333-3279-89a6-8a5e9c6a0ee0 | -6.57961 | -47.38888 | 2025-08-28 00:11:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 47005006-63e9-30a5-af3d-94a4c303381c | -5.16118 | -47.8478 | 2025-08-28 00:11:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| aeae7d64-329c-3e3b-8486-5758f3f52f5f | -2.44232 | -47.32905 | 2025-08-28 00:11:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2ca3908c-f51a-305c-aec0-5586e9f6e48c | -3.22783 | -43.43288 | 2025-08-28 00:11:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| de98b511-61b9-3c20-87ce-5b8d42f2273e | -6.56848 | -47.36959 | 2025-08-28 00:11:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 75e2b197-19a8-3e36-b2ff-0ce54ce41485 | -3.72742 | -48.36163 | 2025-08-28 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fb6b4fd3-c658-3288-a7b2-4a4b89627c07 | -5.77396 | -44.92576 | 2025-08-28 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b6307298-1244-3a9e-a5ad-e8131393dfed | -7.21709 | -45.31242 | 2025-08-28 00:11:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 316719c0-351b-38be-b45c-b3b8463c11cc | -7.23709 | -45.43222 | 2025-08-28 00:11:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 08b4826d-1d0d-3939-a7c6-25a172602266 | -3.23027 | -43.45044 | 2025-08-28 00:11:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5021ac50-84b7-31ff-bbf3-f8c8b81c84f5 | -3.73849 | -48.94421 | 2025-08-28 00:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 9f8772af-8f1a-3d05-b9dc-c000dc2d0712 | -6.88488 | -43.62672 | 2025-08-28 00:11:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 0cfa1867-cae9-39d0-84eb-8d80160d51a2 | -4.793 | -47.24917 | 2025-08-28 00:11:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9bc60146-382a-343a-8260-d12bdbfd3531 | -4.48395 | -47.67935 | 2025-08-28 00:11:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 45c6f209-4f18-3133-b499-419f65aa5442 | -0.75421 | -47.76431 | 2025-08-28 00:11:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2b26d90a-623b-3113-972b-ad8259625aa5 | -6.87599 | -43.62798 | 2025-08-28 00:11:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| aa3bcd0d-0046-3fea-9701-a4a6981b869f | -7.07917 | -44.30397 | 2025-08-28 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 15ed355d-6cee-3f10-9f39-7eb7f9958a97 | -6.85697 | -43.62151 | 2025-08-28 00:11:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9f5ba6d5-2409-3024-bc51-fec7e43eabd1 | -6.87105 | -43.59206 | 2025-08-28 00:11:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 90591854-6e62-31f2-9607-ca6533c3e09d | -6.57027 | -47.38372 | 2025-08-28 00:11:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| bb6a522b-73f5-3ceb-97ab-31c64889eec5 | -3.98264 | -47.8825 | 2025-08-28 00:11:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 5e736a41-afd9-3884-a05d-d1183424c323 | -6.28351 | -44.48198 | 2025-08-28 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 47dcee08-cc27-3129-835c-e66d21927044 | -6.44304 | -44.569 | 2025-08-28 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 463f94c3-cee1-3bb4-8a44-0e16d1ce67f3 | -6.8671 | -43.62924 | 2025-08-28 00:11:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 6516731a-3a2a-33a9-92a2-885793c17fb1 | -6.28225 | -44.47262 | 2025-08-28 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5991a846-84cf-3846-a7fa-24eed8b14e39 | -7.25759 | -45.36477 | 2025-08-28 00:11:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 4d287ada-92ef-31e9-a0b0-b3f4878b2d4a | -4.88381 | -44.95673 | 2025-08-28 00:11:00 | TERRA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 21dd32b1-0a9b-3df7-8c84-a1f2ec111b38 | -6.56863 | -47.39032 | 2025-08-28 00:11:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 075da327-152c-3f8f-8504-dad424edf3bb | -5.74669 | -40.44548 | 2025-08-28 00:11:00 | TERRA_M-M | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 190a60c3-5b3e-3737-a08f-e7860c4ee00c | -5.91346 | -46.16764 | 2025-08-28 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 764718a3-fcb6-347f-9dbe-f86ff47ef62b | -6.4966 | -53.40032 | 2025-08-28 00:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| d4645a0f-3a1b-39bc-a236-67f298ab4694 | -6.17121 | -44.06086 | 2025-08-28 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4a622928-8b9f-32e1-9aca-56b8c764406f | -6.17719 | -44.17175 | 2025-08-28 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3106aaff-4b55-3cf6-ad6d-fb8fc3b7a006 | -6.2252 | -43.37436 | 2025-08-28 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e2d0f232-b8db-3fcc-aa4a-1006c0a54ca4 | -4.79474 | -47.26197 | 2025-08-28 00:11:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 176.7 |
| 068a5671-be84-3c34-855f-fb5983386407 | -5.21135 | -44.31775 | 2025-08-28 00:11:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 367a9ab6-e626-3a90-84d2-7b58e78117e2 | -6.24409 | -43.38073 | 2025-08-28 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0d3ac26f-aa15-3ae1-999e-38b320918288 | -6.16049 | -44.38762 | 2025-08-28 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fc42f5a4-a4cc-3a5a-bb24-c13cc3ceffe9 | -0.75255 | -47.75213 | 2025-08-28 00:11:00 | TERRA_M-M | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 8977147a-06f9-34ce-92a5-1f4ac6fc756c | -7.43298 | -42.05429 | 2025-08-28 00:11:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |


[Clique aqui para ver as próximas entradas](README5.md)
