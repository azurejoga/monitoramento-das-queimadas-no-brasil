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
| 5f04e360-1d3b-3485-bf38-037e060d1762 | -9.4992 | -60.547 | 2025-08-15 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.4 |
| b7d77432-facc-3b99-90f0-9128de61218f | -9.518 | -60.5268 | 2025-08-15 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 51645265-00ec-3e23-8fa2-aa827805d11f | -11.3468 | -55.4124 | 2025-08-15 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 740bf0de-60e6-3a7a-925c-87804b444ddc | -11.3655 | -55.431 | 2025-08-15 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 132.7 |
| b69654cc-4b9d-36b7-b630-fb17a210ed71 | -6.9487 | -59.5297 | 2025-08-15 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e39aef45-c42a-3820-8384-9d3e4ad127fd | -11.3466 | -55.4326 | 2025-08-15 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 127.7 |
| c01a4072-0b24-32b3-8714-1a605e88d4c6 | -7.0797 | -59.2157 | 2025-08-15 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 68790045-562b-37e1-bc29-fa443453ce77 | -9.3876 | -60.5335 | 2025-08-15 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 75eced0c-db46-3dee-a199-03d168b953e1 | -5.455 | -60.1391 | 2025-08-15 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 151.4 |
| eced4a13-f826-31c9-bcfc-c9133f2854e5 | -11.9292 | -43.4526 | 2025-08-15 00:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| bf8d17cc-ad25-3085-a235-1f5d1aef0e40 | -7.0982 | -59.215 | 2025-08-15 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 50632454-1823-3296-b890-8d849ae36c88 | -8.3099 | -45.0196 | 2025-08-15 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 3e239f8d-54fb-3224-a488-67b8818aaff0 | -9.4995 | -60.5085 | 2025-08-15 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 336692f0-3353-3146-b3c1-c037aa9a3ff7 | -9.5179 | -60.5461 | 2025-08-15 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| eb66dfc4-8b71-36a0-ac0b-89d77a6c8a68 | -9.3875 | -60.5528 | 2025-08-15 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 39cde3df-3515-3bed-a86b-4d5b1602d7c8 | -7.5292 | -61.3254 | 2025-08-15 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| ccfbf218-ecdb-354a-a124-ddac824198cd | -11.9099 | -43.4556 | 2025-08-15 00:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| bce640a0-3b92-3c82-b281-8d0dcaace6f9 | -3.4254 | -49.0517 | 2025-08-15 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| e7c0397b-e033-32cd-b2c4-414a8a75fe66 | -7.9517 | -61.7464 | 2025-08-15 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 61739435-26fa-33dc-8ad8-659e047f559f | -7.3116 | -60.628 | 2025-08-15 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| af3b4a90-7361-318b-aeeb-331c4f326b99 | -5.762 | -46.6741 | 2025-08-15 00:20:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| da2d10fb-8a2d-3521-8e1f-30e9fa9f7c63 | -6.9303 | -59.5305 | 2025-08-15 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 4ddbb70f-6658-39d5-bb21-b2b0ca39c691 | -5.455 | -60.12 | 2025-08-15 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 9827ce6b-5c33-37c7-994b-09e9c2e34b1d | -11.3657 | -55.4107 | 2025-08-15 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 2d03a425-b610-3cab-b74a-672ad50d80d0 | -6.9302 | -59.5497 | 2025-08-15 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 573b93d7-70f4-3b25-8f5b-e982cd1bff61 | -2.4876 | -47.5737 | 2025-08-15 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 0b7e7e39-39a5-31b0-8d94-44bba81adeb6 | -9.4994 | -60.5278 | 2025-08-15 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 149.4 |
| b9421d4b-fdec-3f91-9401-a7addfcb00e8 | -7.52 | -63.1052 | 2025-08-15 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 58434280-c767-3ee3-9e85-49a2af5a186b | -11.9104 | -43.4319 | 2025-08-15 00:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 8f878224-31e2-3676-be4c-e04f0e99ad4a | -7.5385 | -63.1046 | 2025-08-15 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| a1975a24-b208-3190-9c97-857bf2c5c5b7 | -7.33 | -60.6273 | 2025-08-15 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 7f6e08f5-a1c1-3772-a6ca-21e78729b1a5 | -7.5201 | -63.0863 | 2025-08-15 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| b5b40ebb-0c86-3176-8dde-23a7aec9fd79 | -7.6103 | -63.516 | 2025-08-15 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| c8751e91-1453-3c2e-b55d-3a32e2d87b44 | -11.9296 | -43.4288 | 2025-08-15 00:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 99ed2455-2529-3f87-bc55-1e2f33d1abf8 | -6.49 | -62.9306 | 2025-08-15 00:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| ef0a0cc5-020e-356e-8fc5-f67ec34e8385 | -13.3203 | -45.2177 | 2025-08-15 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| e8aca75e-86d2-3751-b3b5-088f09f10fe6 | -9.0357 | -40.5219 | 2025-08-15 00:20:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 109.9 |
| 66a000ab-076d-3b4f-8a32-c151f0ca6508 | -8.1029 | -61.1878 | 2025-08-15 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| ab83ff5f-da5b-3389-8e94-12c8dff83309 | -14.2444 | -44.5897 | 2025-08-15 00:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| f777bb2f-a073-3804-8df5-c0502d85f436 | -7.5291 | -61.3444 | 2025-08-15 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| d1ccca0b-3043-3013-9456-c38dd576432a | -7.2919 | -64.7049 | 2025-08-15 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 3da5681a-6eab-3981-ab50-a2b8fd4acf7f | -7.0796 | -59.2351 | 2025-08-15 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| f865bf56-2985-3d12-a24e-bfa340a049ad | -7.0613 | -59.2165 | 2025-08-15 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a7f25457-7299-31c7-80d5-f20a7e112164 | -9.5351 | -63.5771 | 2025-08-15 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 313d377b-deb6-3530-b788-d430dc7f5201 | -7.4006 | -44.859798 | 2025-08-15 00:21:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a1ab6c69-cb85-34cf-9b4f-0e6c580e9313 | -8.6079 | -45.618401 | 2025-08-15 00:21:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c3764b66-a3a4-33a2-bfcb-6b36e292b47e | -3.423 | -49.039902 | 2025-08-15 00:21:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34824ee3-ef1a-3421-bd28-b43d8984cf3a | -6.9127 | -45.2089 | 2025-08-15 00:21:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8b5752e-4460-35a6-a720-8bda0dbce6b9 | -11.9098 | -43.435398 | 2025-08-15 00:21:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4be5b312-7ff3-3ce4-a6ed-faa26baf0495 | -11.9326 | -43.445499 | 2025-08-15 00:21:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 217aefa7-9868-3c85-b7ba-8ec547ac362b | -16.600201 | -47.043201 | 2025-08-15 00:21:00 | METOP-C | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ed75223d-d5f1-3e7a-84c8-1da1615fcf5c | -2.5354 | -47.702099 | 2025-08-15 00:21:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d93b4b75-150b-3220-bba8-819fcd61d53e | -8.5218 | -43.298302 | 2025-08-15 00:21:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 69223f6e-3850-39d2-9783-d05a28f47467 | -3.4206 | -49.029202 | 2025-08-15 00:21:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50cea655-8eb1-33d4-b538-2201ccd8662b | -6.3343 | -42.7953 | 2025-08-15 00:21:00 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 93f11859-2706-3757-b977-fba6a7ab8d36 | -12.3134 | -44.339298 | 2025-08-15 00:21:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e87f949e-df6c-3f90-acf2-2a2323de16a7 | -4.98 | -41.712399 | 2025-08-15 00:21:00 | METOP-C | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4f72dada-703f-3dd8-8539-75aa1323c0ba | -5.7687 | -46.6703 | 2025-08-15 00:21:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 470f9993-2636-380b-8e26-d2029c15a363 | -7.4482 | -49.236198 | 2025-08-15 00:21:00 | METOP-C | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d0fd680a-1341-30c7-93bb-ffbc636396f2 | -9.2711 | -50.2472 | 2025-08-15 00:21:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1394a9ce-945c-391a-9f36-fe77f6a64f16 | -2.4943 | -47.566502 | 2025-08-15 00:21:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 198595f8-11a5-31fd-8496-d1d1bee6c2d6 | -12.5929 | -46.9603 | 2025-08-15 00:21:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 946e8258-143b-3b87-87d6-e4f2c28da1af | -4.6068 | -43.314201 | 2025-08-15 00:21:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1928ceee-cd51-392c-b801-18655c040730 | -6.9617 | -42.877102 | 2025-08-15 00:21:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 340cb21e-ccc8-30c3-a6b3-e55f827cb4e9 | -2.3923 | -47.660999 | 2025-08-15 00:21:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ac49b82-7cbe-3f7f-95c9-bde1a768b804 | -3.8224 | -41.5709 | 2025-08-15 00:21:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 95cf8a35-433c-3822-ac84-5c660f64d61b | -5.5439 | -43.893902 | 2025-08-15 00:21:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79a21ae8-4561-3759-9160-7dd58d6cb617 | -11.1937 | -40.952801 | 2025-08-15 00:21:00 | METOP-C | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0fd07ab3-304b-399c-ad62-1d2f541458d0 | -5.6865 | -43.6604 | 2025-08-15 00:21:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3609a835-6fa8-34e7-8d00-bc24b84ca5f0 | -9.7204 | -48.0159 | 2025-08-15 00:21:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f232c43f-2244-3eb0-8918-68c774f32f1b | -3.4478 | -48.9674 | 2025-08-15 00:21:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be049a92-51f2-3991-b2f6-c187c88b7884 | -11.9114 | -43.4426 | 2025-08-15 00:21:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a0b90657-629e-31ac-96af-ca481dbe898d | -4.7882 | -45.330399 | 2025-08-15 00:21:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8e024d1-616d-3839-8536-ef3e688bfab8 | -8.2976 | -45.006302 | 2025-08-15 00:21:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b686a4f2-f86e-397e-9b9d-e946a00ec315 | -4.2248 | -47.213001 | 2025-08-15 00:21:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1d1e140-7d87-3206-8c96-e855d93d88da | -7.8655 | -48.231899 | 2025-08-15 00:21:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2430ee81-e3d5-3d18-9a6f-792fd6efcea2 | -3.4254 | -49.050701 | 2025-08-15 00:21:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa53eace-3d20-3e88-bf2b-eb41fc44f11c | -8.3091 | -45.0117 | 2025-08-15 00:21:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 613098d4-628f-3dc9-8649-5a03d7ae4393 | -8.3206 | -45.017101 | 2025-08-15 00:21:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7dfe9ed9-4724-36d0-8ee6-756b39034009 | -6.4936 | -42.860298 | 2025-08-15 00:21:00 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3b074022-a1ee-3ed3-8eac-7dc5ae4cd426 | -8.7222 | -44.004601 | 2025-08-15 00:21:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f4ab35cc-9b28-31a5-bf71-8dad6d8a2b4c | -12.5831 | -46.962299 | 2025-08-15 00:21:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be67bf14-23b9-33cf-9e69-1c41d75b65d4 | -15.6604 | -49.763699 | 2025-08-15 00:21:00 | METOP-C | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 83a8bc4e-79da-3aa4-891f-938c22891ce6 | -15.4031 | -46.593102 | 2025-08-15 00:21:00 | METOP-C | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a5436924-015e-342d-bbba-163980580471 | -5.7866 | -43.602001 | 2025-08-15 00:21:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 779203a0-ef90-37a0-be46-d89fd060a6d3 | -17.491699 | -47.838699 | 2025-08-15 00:21:00 | METOP-C | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aa931ad4-2828-337b-be83-88b92a7b9a7f | -3.8206 | -41.5634 | 2025-08-15 00:21:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1d85a029-528c-30cb-983b-de081412984f | -9.0347 | -40.504799 | 2025-08-15 00:21:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| eb073809-b34e-3fe7-8f8c-be517139d982 | -9.1821 | -45.333 | 2025-08-15 00:21:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e11e5a9f-74ad-3448-ae50-25fba6ae174c | -5.5455 | -43.900799 | 2025-08-15 00:21:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0118ae31-a03c-3729-ad64-26a76d1ea992 | -13.3327 | -45.2183 | 2025-08-15 00:21:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f31bc79f-a54a-3d2c-9e21-dae964215c13 | -11.1953 | -40.558201 | 2025-08-15 00:21:00 | METOP-C | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bf29b2b9-855a-39a8-be78-02f225008ce2 | -7.3826 | -44.871498 | 2025-08-15 00:21:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84f62acc-9525-3e95-bfe7-c865c726c884 | -9.0399 | -40.527302 | 2025-08-15 00:21:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 5119a1c8-e636-3985-abd1-bc06b967f882 | -8.3399 | -40.979099 | 2025-08-15 00:21:00 | METOP-C | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c13fa3dd-354e-362b-b8dd-0f50d76eaba0 | -13.8844 | -45.555099 | 2025-08-15 00:21:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce7737b1-8926-3558-9812-f8993664ae39 | -5.5489 | -45.369598 | 2025-08-15 00:21:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d5c1cfc-eca4-37c1-a281-b8f9a1e2c379 | -8.2 | -42.2486 | 2025-08-15 00:21:00 | METOP-C | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 55e6dc83-f8b5-333a-ad61-c0a14c57c534 | -11.1969 | -40.565498 | 2025-08-15 00:21:00 | METOP-C | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| aad01483-4861-31e8-9810-b4cb08d673e9 | -12.7592 | -44.406601 | 2025-08-15 00:21:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
