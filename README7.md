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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 018b27ff-f8c8-3338-91e4-08cd4f447ddd | -8.55727 | -45.99168 | 2026-05-22 05:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d8a76ccc-04e9-31e0-ac3c-671d073100f6 | -9.07911 | -49.6781 | 2026-05-22 05:25:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4dc0e22c-8b04-3575-934d-122df645a5a8 | -11.0654 | -46.70776 | 2026-05-22 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f40336a-264b-319f-a441-6c579a2054d4 | -9.07342 | -49.67725 | 2026-05-22 05:25:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 306f17dd-1603-300c-8e21-f30b8d26671d | -11.06775 | -46.70249 | 2026-05-22 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3612d9cf-4998-3b7a-af52-3a2c73c0063c | -10.91293 | -54.11086 | 2026-05-22 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d9d9434-ff01-3ae8-a352-656def27d2a1 | -11.61324 | -55.33271 | 2026-05-22 05:27:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5987d81-26a6-3c4e-b375-78893189d5c8 | -17.95478 | -54.46183 | 2026-05-22 05:27:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe016453-9d65-3de7-b26c-b1b60c42844c | -11.31411 | -47.57719 | 2026-05-22 05:27:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d1d130c-2cb5-3da3-abe6-869d1fd51f63 | -11.6092 | -55.33213 | 2026-05-22 05:27:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d46625e2-ef75-302b-8c95-01291a03a9c7 | -11.60251 | -54.19148 | 2026-05-22 05:27:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2463f333-3c47-347b-b1f6-ae2e42551bb4 | -11.6087 | -55.33568 | 2026-05-22 05:27:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53bbce4b-4385-3143-834e-71b0a268a2ae | -10.91669 | -54.11562 | 2026-05-22 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5630cef-e1a7-384d-a143-c9b16cb0ca6e | -10.88892 | -53.73946 | 2026-05-22 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd6e8e29-56a7-30ac-be1f-8d6fbe957272 | -11.61274 | -55.33626 | 2026-05-22 05:27:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 266b6eb5-6927-35bb-9b70-01dfe28124f7 | -10.89275 | -53.74444 | 2026-05-22 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64c76808-2464-32d6-8ec1-f0c94d22e08f | -10.03417 | -59.35692 | 2026-05-22 05:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 81aa25aa-a20d-3393-be48-78338c1c32ac | -10.91235 | -54.115 | 2026-05-22 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d66aad5-025a-34c8-9d88-f2fd5e2490f4 | -10.03083 | -59.35638 | 2026-05-22 05:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d417146-136b-364d-a18d-431172681ee1 | -11.30741 | -47.57647 | 2026-05-22 05:27:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d1454cb-7775-3bbb-8deb-02955d6dd66f | -10.8883 | -53.74389 | 2026-05-22 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e6d8740-65eb-3a40-9aac-f378a5d692b4 | -11.60311 | -54.194 | 2026-05-22 05:27:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ca71b01-3dcf-3488-82f2-827c267c6ebb | -10.91726 | -54.11147 | 2026-05-22 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18f75138-a7ba-3e98-8631-b70055104a9f | -10.88447 | -53.73886 | 2026-05-22 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f63180c0-1957-3f47-961a-01cd9ed5baf4 | -10.89337 | -53.74002 | 2026-05-22 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 291888d9-4a5b-3e88-9ef9-ed1e7837d689 | -11.43993 | -52.9299 | 2026-05-22 05:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24010e3f-1983-351a-b2d8-f698b0858dd2 | -10.031 | -59.35807 | 2026-05-22 05:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5f78277-80b9-35ae-8c00-afd8f39f1a00 | -9.94487 | -52.47266 | 2026-05-22 05:46:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1039889-9dae-3a83-aba7-71414694a247 | -10.0341 | -59.35619 | 2026-05-22 05:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83b7c172-99b0-3231-a5fb-b8a809494b6a | -9.94564 | -52.46593 | 2026-05-22 05:46:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbd1e65e-e657-3d0c-b4c8-78cebdb20e06 | -11.44765 | -52.92409 | 2026-05-22 05:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ad0aee2-c8dc-37e2-9c87-cc056fd04304 | -11.44069 | -52.92326 | 2026-05-22 05:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d517ef56-4eb0-3dd6-a415-4244aa8f7999 | -10.4871 | -49.359 | 2026-05-22 06:42:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7e3efc57-17bd-3097-809a-2841f5a24f74 | -9.94293 | -52.46792 | 2026-05-22 06:42:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f39d8b8e-6bde-38a8-8206-f5598b334941 | -9.29632 | -45.48847 | 2026-05-22 06:42:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 7a4ab4ef-25e1-3182-a104-1276ab15f99d | -8.55053 | -45.98548 | 2026-05-22 06:42:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| bb14717c-0da2-3f6b-9925-6f866881e2cf | -19.7676 | -54.06797 | 2026-05-22 06:44:00 | AQUA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6e555d83-6ddf-32de-bb76-a313a1087de5 | -5.7752 | -45.128 | 2026-05-22 10:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 160b9cd4-a50b-3996-b27d-b6900f04aba5 | -5.7752 | -45.128 | 2026-05-22 11:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 1e44f715-fa59-3acb-9b86-6855eef08e05 | -5.7752 | -45.128 | 2026-05-22 11:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| ddf72b3e-7ce5-37cf-9bd5-0a7407d8dd8a | -5.7752 | -45.128 | 2026-05-22 11:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 9643c4f0-fd76-3c85-a654-dbfcd4c84542 | -5.7752 | -45.128 | 2026-05-22 11:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 6af9c446-6296-3d26-bfba-998f4b7e9387 | -5.77247 | -45.12999 | 2026-05-22 11:55:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 067d95b3-df83-31ef-9ac2-b5dc3abd3384 | -6.22457 | -46.89248 | 2026-05-22 11:55:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 5acece9c-d5a7-336a-a632-a9fe5a5dcf16 | -5.78162 | -45.13131 | 2026-05-22 11:55:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 9a3669cc-b16a-300e-add2-c85db05b35ca | -6.56718 | -47.90397 | 2026-05-22 11:55:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8c11f9c9-4319-3bd7-8634-11e226d3e190 | -5.7803 | -45.14074 | 2026-05-22 11:55:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 80526e22-fca2-3470-8b87-85e60c52ac3e | -6.22583 | -46.88367 | 2026-05-22 11:55:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 6d5a56c2-17cd-368a-8d46-62c33c5dcefc | -11.94522 | -43.396 | 2026-05-22 11:57:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 1758d8ce-01e1-323d-805f-7008853f1cf5 | -11.95634 | -43.39762 | 2026-05-22 11:57:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1e06a291-29fd-31c5-b71c-ff799bc53bc5 | -8.55617 | -45.97911 | 2026-05-22 11:57:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0e14901b-47c5-30f1-a20b-469f9202c447 | -9.06382 | -44.77533 | 2026-05-22 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 148bdeff-4f86-32c4-9c1d-60bc4392e30c | -10.66542 | -49.72006 | 2026-05-22 11:57:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| feda800a-06c5-399a-b4d7-027b7569995e | -8.92251 | -46.91653 | 2026-05-22 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 163eff1f-9783-3773-a549-4bb59f50fc13 | -11.44475 | -52.92867 | 2026-05-22 11:57:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 69c7b3e3-e2c7-3ce5-800e-8dc1c4c59f91 | -8.93137 | -46.91776 | 2026-05-22 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| a1433b9f-75df-3844-881d-0c13dadf60be | -9.05414 | -44.77409 | 2026-05-22 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 85b9a2b7-99fc-3201-bc75-666ca6cbd644 | -15.16961 | -43.78428 | 2026-05-22 11:57:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0552f5e0-7ee9-364f-9a69-868e50e91fd3 | -7.64588 | -45.29936 | 2026-05-22 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2bc2df0a-c93e-3c59-b7d4-6a8790e2deee | -11.34357 | -51.41636 | 2026-05-22 11:57:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 46bbe054-61fa-30ca-912e-6cc6f12415b1 | -10.35717 | -45.2686 | 2026-05-22 11:57:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6fd028cf-39e1-3bb3-be3e-b34d4de38e03 | -8.93264 | -46.90881 | 2026-05-22 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 8469e4e4-7b0c-3709-a90b-da8e7a47e23c | -8.92377 | -46.90758 | 2026-05-22 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| be7a24f8-3bf6-3c18-b709-67d8c7181e9e | -14.17718 | -45.33942 | 2026-05-22 11:57:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 9ed5c009-3fd7-332d-a903-c3128710f800 | -8.55487 | -45.98853 | 2026-05-22 11:57:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a135bdf3-2bc3-3e11-91e1-4c639baa1ed3 | -9.15355 | -44.42123 | 2026-05-22 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d0130f90-51ad-3ffe-bd2e-06c81fd71968 | -9.06529 | -44.76457 | 2026-05-22 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 421ee022-3339-398d-8e14-bbdd2ab26b27 | -8.7204 | -48.32448 | 2026-05-22 11:57:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 50484cda-878b-33c9-824c-cc76e81e6078 | -7.64455 | -45.30911 | 2026-05-22 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9dfebd1b-4f16-3ef0-ad37-4422a13c7fba | -10.66687 | -49.71028 | 2026-05-22 11:57:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 1cc85a97-101f-3e95-a667-9ad8194b9bb4 | -11.94703 | -43.38136 | 2026-05-22 11:57:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 3380477b-9a05-34c1-8ad4-0e3086c64854 | -11.6651 | -44.9627 | 2026-05-22 11:57:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 16ec2656-3cf4-3382-9836-4b899ebba7ec | -5.7752 | -45.128 | 2026-05-22 12:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 720d224e-72e6-3ef1-90ad-b2fe7c2cad3f | -27.36105 | -51.67316 | 2026-05-22 12:02:00 | TERRA_M-T | CAPINZAL | SANTA CATARINA | Brasil | 4203907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| ae5d1fef-8f32-304d-9c1b-113e512bbcaf | -27.36989 | -51.67471 | 2026-05-22 12:02:00 | TERRA_M-T | CAPINZAL | SANTA CATARINA | Brasil | 4203907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| fd202d96-030b-39df-b46e-7e239c404f43 | -5.775 | -45.1507 | 2026-05-22 12:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 5ed4661e-1bf9-3b01-a863-c6c6e32350c4 | -5.7939 | -45.1267 | 2026-05-22 12:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| f25ec38e-c72f-3a7e-ba51-64d8e31e975c | -5.7752 | -45.128 | 2026-05-22 12:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 210.4 |
| 6f7d4f2f-ffd7-3b01-9c4f-36100f988376 | -5.7939 | -45.1267 | 2026-05-22 12:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| df4073dc-377a-34cc-b995-0eeb90ea461f | -5.775 | -45.1507 | 2026-05-22 12:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 41a717b6-82b3-39ad-ab1d-421cbe19e015 | -5.7752 | -45.128 | 2026-05-22 12:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 311.6 |
| c44d8362-d9ae-357f-b838-84d46017f080 | -5.7939 | -45.1267 | 2026-05-22 12:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 372e7333-fed8-33c1-bb8c-571f57e70c97 | -5.775 | -45.1507 | 2026-05-22 12:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 62547fc9-0e4b-3d54-b89c-96d23d3386f9 | -5.7752 | -45.128 | 2026-05-22 12:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 256.9 |
| 135c45f8-5ef6-3f5b-8e80-2c84e8817e2e | -5.7939 | -45.1267 | 2026-05-22 12:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 51ed03c8-7f0f-3fb4-abf7-8578ec2d0953 | -5.7752 | -45.128 | 2026-05-22 12:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 205.5 |
| 5ba482c3-32fd-395f-95b9-127a54f30c30 | -5.775 | -45.1507 | 2026-05-22 12:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 48f884b0-46c7-3eb3-838f-2bf672c9bd80 | -5.7752 | -45.128 | 2026-05-22 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 21f663fe-ece4-3a6a-9403-d5b3789b79e3 | -5.7939 | -45.1267 | 2026-05-22 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| c6c15542-eeff-3f84-8143-5a30c09c7bc3 | -5.7939 | -45.1267 | 2026-05-22 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| eafc5588-7a24-3b12-a567-29a3cfdf2a7c | -5.7752 | -45.128 | 2026-05-22 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 237.1 |
| 5850cbb8-7cf8-34ae-88fd-267e75a32911 | -6.17 | -44.917 | 2026-05-22 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 4249dbd1-d6c5-3b07-83b1-40813b5f87ef | -5.775 | -45.1507 | 2026-05-22 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| e1432a15-4803-3b83-b59c-68a915f959cc | -5.7939 | -45.1267 | 2026-05-22 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 92802984-8919-3f1e-80b9-3dc1b3dd749a | -5.7752 | -45.128 | 2026-05-22 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 290.0 |
| aac26051-9ca9-310c-9ae9-0c85be21d992 | -6.17 | -44.917 | 2026-05-22 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| a905d726-17e0-3d33-8fcd-9dbd54a441bf | -5.7939 | -45.1267 | 2026-05-22 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| ccc6134c-5441-34ec-ae3b-ccf9f0bbba87 | -5.775 | -45.1507 | 2026-05-22 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 7119a666-56d2-3b0d-899f-7ea40c52bb6f | -5.7752 | -45.128 | 2026-05-22 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 299.4 |
| 62e621a2-b250-31a1-8b7d-c10dd1a8948a | -5.7752 | -45.128 | 2026-05-22 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 317.2 |


[Clique aqui para ver as próximas entradas](README8.md)
