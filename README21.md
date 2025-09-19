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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a62205f3-85b5-3386-9a49-f2d0343772b0 | -3.74688 | -51.38052 | 2025-09-19 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e6b2651-f66a-3cab-9c1d-99a414663f8f | -3.69062 | -49.01849 | 2025-09-19 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6d409a2-05a8-3ea9-8f4c-d9e048002487 | -2.30741 | -48.34399 | 2025-09-19 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 819d6dd9-f506-3e60-9198-835f5ef37a0f | -4.22434 | -50.15777 | 2025-09-19 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4370aceb-52f3-3873-9cfc-60af059524cb | -5.34713 | -46.144 | 2025-09-19 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 10666164-3a7f-34ca-9bdc-4bf6a4c6c770 | -2.26185 | -47.88554 | 2025-09-19 04:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 120aeeee-f61f-375f-b5c3-5273ab0f7cf8 | -1.54854 | -47.80349 | 2025-09-19 04:44:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b36c92d8-fd08-37f9-9e7f-a96624cdabdb | -5.54316 | -42.16439 | 2025-09-19 04:44:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f1bc7475-8d2a-34ae-952f-78a6202f2c3e | -5.64402 | -43.88628 | 2025-09-19 04:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b434e3f2-8566-33fd-a85b-29a6e03c71d4 | -2.93848 | -49.45684 | 2025-09-19 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22314219-8dde-3d3f-9773-6ba7d6b7d4e5 | -3.37271 | -52.79359 | 2025-09-19 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2150c8f-f83b-391c-889b-9117f443e075 | -2.85326 | -54.89352 | 2025-09-19 04:44:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a29f7fd-f393-36bc-a268-a7ef145e32d3 | -3.69917 | -49.57475 | 2025-09-19 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ee0bb760-4590-3631-bba5-8fd7ddfedf33 | -3.79832 | -51.18243 | 2025-09-19 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0bb11d25-2fa0-3a57-9238-9d3d7049da93 | -5.50574 | -44.2341 | 2025-09-19 04:44:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b748ffd-ebe2-37cb-af32-0180c4a532f9 | -2.96018 | -48.59269 | 2025-09-19 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32f7d5cd-5f0a-36f7-ab95-b75a2bd5bd4e | -4.98093 | -48.36775 | 2025-09-19 04:44:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e334224-e0a1-3201-aef5-6a62449bc26e | -3.7845 | -52.32598 | 2025-09-19 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1304f613-a1fb-379c-a3f6-bc7cf3e59ec7 | -4.62532 | -47.01706 | 2025-09-19 04:44:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afe87e8f-da38-34e7-a725-c9b65f594da6 | -5.21518 | -42.31538 | 2025-09-19 04:44:00 | NOAA-21 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fc2a3279-f040-3ea5-9f85-57b27459c5ef | -3.08015 | -49.46441 | 2025-09-19 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e99d43c-7080-3ef9-b334-a9edef0435a1 | -2.94642 | -49.34001 | 2025-09-19 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b73e6257-6acc-3413-920a-278ed74567b5 | -5.63803 | -43.89498 | 2025-09-19 04:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f8c0e883-0ba0-3481-8445-4bf047adc3e6 | -2.38306 | -47.63157 | 2025-09-19 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0229cedf-c231-3176-968c-df216c9cb33c | -5.08507 | -47.51709 | 2025-09-19 04:44:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 04562244-85dc-3686-9180-aa7019a02191 | -3.1564 | -43.26029 | 2025-09-19 04:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27cbe70c-603c-3855-9aaf-53621ea15ee5 | -3.80903 | -51.07087 | 2025-09-19 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3193345-e1a9-3670-89ed-869a01e3decb | -2.93516 | -49.45633 | 2025-09-19 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7652d029-2776-3133-b569-d7fab80f7894 | -3.15223 | -49.48249 | 2025-09-19 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a22cb342-3311-3987-b24e-600f4bf19c24 | -2.26132 | -47.8424 | 2025-09-19 04:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3a872bfa-cfbc-3764-8a5f-c725da6eae73 | -4.86559 | -42.96984 | 2025-09-19 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8c53d758-c05b-3617-9370-28945e013d0e | -3.59579 | -55.3033 | 2025-09-19 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0a873ab2-fc5a-3cf1-88b8-08016cbebf39 | -3.69972 | -49.57125 | 2025-09-19 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c1b245ec-3ca2-3580-af83-31a3287447ce | -3.7016 | -47.68363 | 2025-09-19 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed520fd4-90b3-325a-9f6e-0f907266f185 | -2.94588 | -49.34351 | 2025-09-19 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d7814ecc-fe9b-30f6-a7cd-7241e268c50e | -4.69742 | -41.95998 | 2025-09-19 04:44:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ca8daee2-ac53-38db-96d3-369cc85163ff | -3.73633 | -53.73579 | 2025-09-19 04:44:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c218d82-2871-3b47-9381-480ae632d27d | -3.28185 | -49.14958 | 2025-09-19 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 116192d6-ca37-3ccd-9de1-523a287bda28 | -3.79649 | -48.63231 | 2025-09-19 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b59c4a5e-0fef-3378-9a13-c3dba8a1e33c | 1.95197 | -50.967 | 2025-09-19 04:44:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41f05d4a-7656-3b88-9810-c5da748b1e79 | -4.70262 | -41.96085 | 2025-09-19 04:44:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bed8a36e-b9a4-3b6a-aac9-a173e4c28d8c | -2.89614 | -52.8712 | 2025-09-19 04:44:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 180c4770-88b0-3855-bca6-1cb3e5c6b431 | -5.11458 | -42.90854 | 2025-09-19 04:44:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0936e43d-020e-33ab-9e91-239080e673ad | -3.42347 | -46.96627 | 2025-09-19 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 124a7f40-619e-319b-a5c7-8962ad85a4e2 | -3.5972 | -55.30131 | 2025-09-19 04:44:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ed351e6d-cf80-3a28-aa9c-f0359b5107dd | -4.71833 | -46.13288 | 2025-09-19 04:44:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ef0682e-d1bf-3a80-8cd6-9453d7c1079c | -1.75903 | -48.05353 | 2025-09-19 04:44:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf36b703-a656-3bda-a899-4982163f3b7f | -5.34625 | -46.14516 | 2025-09-19 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4c2648c3-ccad-393f-9500-a2c921faeeb6 | -2.91586 | -51.97168 | 2025-09-19 04:44:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6252e818-65e0-3691-b25b-ca626bff7c6e | -5.47284 | -44.69038 | 2025-09-19 04:44:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63e7e2e6-38a0-3cdc-a9ab-e20d1be99bf2 | -2.42779 | -49.32743 | 2025-09-19 04:44:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b327361-de8c-37c4-b71c-99951504bf2c | -5.53796 | -42.16359 | 2025-09-19 04:44:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| db2da719-651c-3418-8fc7-60463d9dbcef | -3.32395 | -54.92464 | 2025-09-19 04:44:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14587518-d528-3407-9e1e-ed2632a4c7a3 | -3.69006 | -49.02208 | 2025-09-19 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a279651b-7ea9-347a-8fa2-99e5679d229c | -3.45365 | -53.8319 | 2025-09-19 04:44:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89523721-49dd-313b-bab7-1c743ea8c51e | -4.25992 | -49.31416 | 2025-09-19 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48b47eeb-8af4-33b3-9972-627683c55260 | -5.64008 | -43.88083 | 2025-09-19 04:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 272a9fa6-0ef6-3dd3-9a6a-0afd56051745 | -2.37955 | -47.63104 | 2025-09-19 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e21fbbb6-1cd2-39ae-93c3-79a6a4105173 | -5.00267 | -43.17809 | 2025-09-19 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92f7e3c0-3fcd-3153-b55e-34894c16fedd | -4.99784 | -43.17744 | 2025-09-19 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e1988a3-9696-38bc-8272-4666a4e90014 | -2.91643 | -51.96808 | 2025-09-19 04:44:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b914219-67f4-30dd-8610-57b1232cb41b | -3.95665 | -49.29681 | 2025-09-19 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 966fdcd4-1cd1-32ea-a1eb-5334f67d7ee1 | -3.73904 | -49.05193 | 2025-09-19 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f48b1dd-e4e7-3d18-a07d-7857b6575708 | -3.92492 | -50.68068 | 2025-09-19 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa84ac2e-4729-3f8e-8c7b-00a0d86a5392 | -2.63821 | -48.04293 | 2025-09-19 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65919035-d430-344a-989c-3b84b4e897a6 | -1.77516 | -55.50135 | 2025-09-19 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34bbbf21-a24e-33c0-a17e-dd42e6857653 | -5.21258 | -45.17602 | 2025-09-19 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60479f45-d5b3-3836-a518-90f1d7616b1f | -4.66873 | -49.32953 | 2025-09-19 04:44:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d45274f-d382-3496-964d-255dad8e3379 | -4.20783 | -50.43708 | 2025-09-19 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff7f35eb-3301-3631-9637-5f30d65521e1 | -5.53842 | -42.16034 | 2025-09-19 04:44:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c0dd5528-3dec-3f45-96db-49b6c00c51b7 | -4.10592 | -48.74295 | 2025-09-19 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fc80b60-ef95-34eb-9c08-0ab11fe06a5f | -3.13515 | -48.8015 | 2025-09-19 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fd9e218-c019-300e-973f-7e279782151d | -2.64107 | -48.04724 | 2025-09-19 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63f61747-9d95-342d-99ca-72c7f164f8a8 | -4.01388 | -48.06022 | 2025-09-19 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5305391-17be-3c39-a183-cbce17a0bce6 | -3.73849 | -49.05552 | 2025-09-19 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d57af1fb-d704-32d3-81b0-a0d82e762634 | -5.09234 | -47.51822 | 2025-09-19 04:44:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f288cdcb-c6fc-37b2-a3ed-803626e1a8d9 | -2.7358 | -49.40373 | 2025-09-19 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f566332e-498a-3ad7-b41b-482ab81c0fd8 | -3.25277 | -48.76725 | 2025-09-19 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 082b1a6b-634d-3486-a9d0-55ed7a829f6c | -2.90158 | -49.80243 | 2025-09-19 04:44:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea263806-c115-353b-8fba-c56ca6fba51e | -3.96 | -49.29733 | 2025-09-19 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a49517ec-f158-372c-bcad-1ae1df352796 | -2.94975 | -49.34052 | 2025-09-19 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 847b30c1-b4e2-314a-b5dd-87654b758c08 | -3.32007 | -54.924 | 2025-09-19 04:44:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ba445fb-897d-3c2e-b827-0af316396004 | -4.62094 | -47.02093 | 2025-09-19 04:44:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e13e3725-03e6-3e3a-aa8a-50b3e463309b | -2.26531 | -47.88607 | 2025-09-19 04:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92784aa5-e5c6-3004-8dcd-b7f418d2acdf | -2.26479 | -47.84293 | 2025-09-19 04:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5e887c02-0d9d-351c-82c5-e4b47deddbb0 | -2.63595 | -48.99275 | 2025-09-19 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 538bbb6f-e4d4-3320-a86f-aa14dc9dec74 | -4.66482 | -49.3326 | 2025-09-19 04:44:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94edd2f6-1a34-33b8-a452-1b317fc2cdcc | -3.2824 | -49.14603 | 2025-09-19 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75fef4ac-932e-3d44-8272-a084ad123ab4 | -5.34318 | -46.14343 | 2025-09-19 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a4f09f8a-fb13-3802-9e00-a639a4b7fb09 | -3.32304 | -54.92221 | 2025-09-19 04:44:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec67d11e-476b-3f42-bca8-86bb2fe6fde7 | -5.34229 | -46.14459 | 2025-09-19 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3e15b1d9-e036-3692-a087-d0ba07276bfb | -5.0887 | -47.51765 | 2025-09-19 04:44:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 17ed723a-6782-374b-b11d-4666b4c4aad7 | -3.32152 | -54.9319 | 2025-09-19 04:44:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dda5e155-4064-3049-95f0-d2efa08f4217 | -2.94921 | -49.34402 | 2025-09-19 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99e9d9ec-9e53-3d85-8b61-3e0af8ece670 | -3.27905 | -49.14552 | 2025-09-19 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a462921-a327-3c90-8c1b-2e62f09f888f | -2.57285 | -54.65724 | 2025-09-19 04:44:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 77d3dde9-d0f3-316a-9978-a9d3bb496e63 | -5.6327 | -43.89914 | 2025-09-19 04:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75de6d4c-9b72-347c-ba9f-e2bc93a6190a | -4.48547 | -50.47026 | 2025-09-19 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fa39319-5050-31f0-b4ff-48bdba91add2 | -1.76304 | -48.05034 | 2025-09-19 04:44:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f38d966e-f9be-3859-8bfa-afb8ac0d68dc | -2.94867 | -49.34753 | 2025-09-19 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README22.md)
