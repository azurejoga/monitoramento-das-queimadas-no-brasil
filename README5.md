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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6bb6809-e2fb-3f61-9c93-b04fee9357ca | -18.41556 | -45.22047 | 2025-10-08 00:50:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 2fd87830-9f31-32ff-9cae-6e955910f71d | -21.01941 | -50.69024 | 2025-10-08 00:50:00 | TERRA_M-M | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| c733d0c3-9277-34f8-9d54-e6c96fed6849 | -15.39841 | -48.00342 | 2025-10-08 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f5346282-98b1-3f5e-9669-eb87839eb83b | -15.9533 | -42.61588 | 2025-10-08 00:50:00 | TERRA_M-M | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.7 |
| d1ca9391-5711-3511-a5f6-68aa5d02946b | -17.29415 | -42.65719 | 2025-10-08 00:50:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 862.2 |
| 2c26a735-f3ac-3d2e-942c-a5816be57340 | -18.05423 | -57.52213 | 2025-10-08 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| bb755e3f-2223-39f4-8b19-85a7535b6bbc | -13.03122 | -47.91896 | 2025-10-08 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3bc1e399-9b24-3e06-a523-8245ad1f0c4d | -11.17987 | -54.8947 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 165.5 |
| f63e324c-a445-33b2-8841-676c612b0ab0 | -13.23455 | -47.17842 | 2025-10-08 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| b6343d5f-38d1-3ba8-89ad-fede6667db56 | -12.02805 | -45.20688 | 2025-10-08 00:52:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 5285f11c-a4d2-3a19-91d0-d69c6b8c9203 | -10.64602 | -47.46713 | 2025-10-08 00:52:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 323ba8f7-0148-3be0-b863-8fc444fe8857 | -11.45289 | -50.19995 | 2025-10-08 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 39.8 |
| e8001543-cf8e-3391-ac02-4a469fda32b4 | -11.67107 | -50.97029 | 2025-10-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| daf52d46-561c-3181-af50-ac126ed8821a | -10.90702 | -51.02833 | 2025-10-08 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 8a9bda1c-7686-3825-af98-1cb0d02f6b02 | -13.05882 | -47.94633 | 2025-10-08 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c544c06b-df88-3e09-8d5f-a59a6d24ddb1 | -10.43741 | -55.05682 | 2025-10-08 00:52:00 | TERRA_M-M | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7b29aff9-c9c6-3698-bb73-5c8de001197a | -13.29416 | -47.16834 | 2025-10-08 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 89ddafc7-f4c5-313c-96ff-811a9530064d | -10.44176 | -51.63816 | 2025-10-08 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d9439270-a118-31aa-8aef-e15a700db71c | -7.79846 | -46.0051 | 2025-10-08 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 45ee75aa-607a-3815-9313-0f438e7beb0b | -7.35347 | -43.86411 | 2025-10-08 00:52:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 0e691d0e-56a5-3534-8fca-dbad474a3fd8 | -11.16692 | -54.86735 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 20209c44-129e-3d08-9d0f-290351449d92 | -12.38995 | -51.14506 | 2025-10-08 00:52:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e4b97b56-5fe8-355d-b589-b514b41b6cfd | -14.70274 | -46.02327 | 2025-10-08 00:52:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 26678e46-61ba-33f6-99cb-a85fa6479efb | -11.33438 | -56.20359 | 2025-10-08 00:52:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 1ccb3b3e-07bc-3d9a-adb8-37a7a9d2004a | -10.86841 | -53.74754 | 2025-10-08 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| c8d28fc7-c84f-3350-919c-8df5cce45132 | -11.4271 | -56.2876 | 2025-10-08 00:52:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 371113a7-59ce-3468-b956-cbefb2c8734a | -11.1513 | -54.88896 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| ea314bd1-6380-3977-94ba-1120197337f6 | -10.85682 | -51.01496 | 2025-10-08 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 35e1bb9c-e396-3790-9160-fe9bd05a4607 | -15.63643 | -53.81258 | 2025-10-08 00:52:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e7eb3a9b-b86a-304e-b051-03ac97b0cb93 | -14.93729 | -46.79794 | 2025-10-08 00:52:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| dc241ddc-2977-3591-aee4-ad5137fd5603 | -13.08155 | -48.01597 | 2025-10-08 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9bacff14-99b0-3397-8f8f-1a5e148eed82 | -12.39917 | -51.14362 | 2025-10-08 00:52:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4d74106b-84a9-310d-92ec-d95aeb3e20f6 | -10.96801 | -54.14636 | 2025-10-08 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a6c8e27d-e0a0-3739-a91d-8ae89d0981b1 | -13.30254 | -48.02913 | 2025-10-08 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 3e361df4-010e-3611-a3b3-6723588cb4bf | -11.69379 | -46.37883 | 2025-10-08 00:52:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 7c715c16-3f4b-33ee-ab1b-3017738834bb | -11.36503 | -55.18238 | 2025-10-08 00:52:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 59f69f65-a695-357e-b3cc-9b5cc5f539f5 | -11.70682 | -46.37628 | 2025-10-08 00:52:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 73c62b5d-2f55-37ce-98dd-faf9de1e1fb5 | -9.63942 | -55.07878 | 2025-10-08 00:52:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 79b3dbf7-f0bd-321c-bda7-ffb210733a6f | -12.01381 | -45.2095 | 2025-10-08 00:52:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 9b18b6b9-fab1-39c1-b75a-3d0a9c72226c | -9.18563 | -47.78706 | 2025-10-08 00:52:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| a6bdd1fa-1687-3d99-9ebc-cc931783f2b6 | -13.88297 | -51.9099 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c63664e7-fb7f-37cb-ad60-9c2f1d087b03 | -10.85835 | -51.02528 | 2025-10-08 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e5e18ef2-f903-3991-a93e-eb5dcbc5a8a7 | -10.46895 | -49.38456 | 2025-10-08 00:52:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| ecc58084-83d0-34dc-a27a-4121401c6a60 | -7.47416 | -46.85098 | 2025-10-08 00:52:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 19e9caa5-9376-357b-adb0-5dfcf1d9a4cf | -10.92588 | -51.02541 | 2025-10-08 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 135.3 |
| adb27b0d-4861-371d-995f-274a41adcd34 | -11.23947 | -47.38165 | 2025-10-08 00:52:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| d0ecc7ba-2797-3f49-9d27-2f0a21d3e362 | -8.98006 | -47.48679 | 2025-10-08 00:52:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 72dc8630-3328-3b1f-a2f9-01f99e7e3aef | -11.3813 | -54.34264 | 2025-10-08 00:52:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| a1a8ff73-9a5a-37c3-9bec-4b6057b9be06 | -9.38468 | -59.41479 | 2025-10-08 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 03b40efc-3a5c-344a-b08a-30e9816d5fba | -9.79371 | -47.74356 | 2025-10-08 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 748d58a7-88b0-30fb-abc7-50ae0e2fe951 | -11.16039 | -54.88766 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| ee3e94bb-109e-3ad8-aa14-52427a3e4332 | -15.18645 | -48.10786 | 2025-10-08 00:52:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b4203d49-5314-3154-87ae-898dbb4580bd | -9.09102 | -47.96137 | 2025-10-08 00:52:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| a97577fa-95a0-3529-91ce-00a22ccee502 | -9.97325 | -48.77492 | 2025-10-08 00:52:00 | TERRA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f906ce21-53ae-3f77-9225-cb4e6e6fca91 | -10.24146 | -52.69724 | 2025-10-08 00:52:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fde6051b-b8aa-31e8-9863-e8429c03e8a2 | -12.00107 | -47.195 | 2025-10-08 00:52:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b57b9e53-c156-39fe-a64a-8671941e3635 | -10.89609 | -51.01946 | 2025-10-08 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1282184a-ecb9-3d88-bc65-0075e2f403be | -14.8714 | -56.59392 | 2025-10-08 00:52:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d14cdbea-c1cb-32c1-8e7f-9f4eb383ba65 | -10.68231 | -54.68807 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f16baf67-a3f2-35d4-8d66-730c623ba5f3 | -11.01842 | -52.32168 | 2025-10-08 00:52:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5df805a4-7683-33b6-bf9a-abacfefee14a | -12.32383 | -50.26841 | 2025-10-08 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c3985b4d-0a76-3a36-9a8d-affe50cc8ae0 | -11.35579 | -55.1836 | 2025-10-08 00:52:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e10843c7-ffde-3d09-b1b7-1e6b57413d17 | -13.41125 | -48.86407 | 2025-10-08 00:52:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 7c00f90d-7803-36ed-80e1-45141d5cf367 | -10.09063 | -51.18741 | 2025-10-08 00:52:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8023e65d-d784-3f31-b266-945bbe2ca792 | -14.69209 | -48.41089 | 2025-10-08 00:52:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 43231f01-3ced-317b-8830-f7abd9d9ca51 | -14.61743 | -52.48184 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 735b4e50-a027-3cf2-8064-f042ec2dd9da | -14.67548 | -51.90287 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| acb964a3-c477-318a-8e39-37ab256dc2f8 | -14.61617 | -52.47277 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b09c0f14-4afb-3b8a-96df-928b1cf80dd7 | -13.22241 | -47.17913 | 2025-10-08 00:52:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 32d99607-fa5e-3ad3-8b80-2a2de21783e7 | -14.68435 | -51.90151 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bc9be9ad-276e-3d1f-9d14-86c75a322f9f | -11.14221 | -54.89024 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 10365eea-2cb1-39ab-bccc-a058b46e17b8 | -11.12529 | -54.90231 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 904cf321-a0f1-381f-b8fe-7f84b529e157 | -13.80987 | -45.79574 | 2025-10-08 00:52:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 244d014f-a6f5-3e7c-a497-dc8dafa0a90e | -13.33582 | -48.01857 | 2025-10-08 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| eeb8f65a-ebfd-3d95-9928-f430ea9c7beb | -11.21973 | -47.83385 | 2025-10-08 00:52:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 520de6dd-e4d0-3b66-afb6-c3a1f8bffdf2 | -11.44238 | -50.20752 | 2025-10-08 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| d47933fe-7a76-35b0-9c34-123c453658e4 | -12.7433 | -44.71865 | 2025-10-08 00:52:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 15cefcb5-249a-3203-a6f9-10fb192e14c4 | -10.67458 | -54.69869 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ca834031-6a41-36d1-bc32-ed2bf28ed546 | -12.18221 | -50.98517 | 2025-10-08 00:52:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5788e843-15f6-36ba-9b3c-e16d0c3f120e | -11.1682 | -54.87684 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 60575283-67f9-3292-8984-31756e603025 | -11.01364 | -50.89349 | 2025-10-08 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 65bc8b8d-d7cb-3260-af8e-3d5aa44460e5 | -8.61679 | -45.10827 | 2025-10-08 00:52:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 2693622d-95f1-3eba-a94e-901e3ef31792 | -10.3819 | -48.13683 | 2025-10-08 00:52:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 885c8b08-8252-3fe5-a705-4245a3616706 | -12.23884 | -47.86589 | 2025-10-08 00:52:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ed2378f1-77ae-3d64-a432-07fa0bd4ac21 | -11.176 | -54.86606 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| cf8bdc3b-9f0e-3dfd-bae9-8ee548e66d2c | -11.15784 | -54.86865 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 5c993432-bed7-30d7-96d7-506af599883a | -11.75771 | -51.49493 | 2025-10-08 00:52:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 82a16607-e6e5-3674-b2a4-763247053919 | -7.58274 | -47.21382 | 2025-10-08 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f3c7e43d-267d-3763-a96c-b6403ca3273d | -10.64917 | -47.46104 | 2025-10-08 00:52:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| f4699f7a-1d79-3cdf-8972-7cdbcfbc87d2 | -10.58376 | -51.47445 | 2025-10-08 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8807c633-316b-3452-aa17-2da0738487db | -10.89909 | -51.04009 | 2025-10-08 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 74ac96fa-4bbc-3a28-aec4-c2d1c5806e78 | -7.80127 | -46.73092 | 2025-10-08 00:52:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 751db6e4-80c5-3518-a015-898ddd7534ca | -14.71271 | -46.08212 | 2025-10-08 00:52:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 18aa84d7-0525-355c-947e-5a452cce9611 | -11.12403 | -54.8928 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e61fd427-6fac-33bb-9592-0167dce77fd3 | -12.42236 | -45.62017 | 2025-10-08 00:52:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 35.8 |
| f5239f42-4d48-3625-9184-ba03f4f745cc | -11.15003 | -54.87943 | 2025-10-08 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| b2b98efa-f219-30a0-aad4-1df3c52b2c89 | -14.38885 | -46.03509 | 2025-10-08 00:52:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 78bb3852-7fad-33fc-b2b4-d757e17240a7 | -9.17905 | -47.82491 | 2025-10-08 00:52:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| e5c307ff-36a3-3c57-be8b-cc5be1cc3ee3 | -13.00052 | -51.09788 | 2025-10-08 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4ed995ad-acd2-374d-bfff-d2e72b0c6dbd | -14.70939 | -46.06254 | 2025-10-08 00:52:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |


[Clique aqui para ver as próximas entradas](README6.md)
