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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7da73d2-bbce-3975-9083-206d4c5eacc2 | -2.38006 | -57.15791 | 2024-10-30 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d985b91-e67a-37af-af4c-8e3593da232a | -2.37951 | -57.16138 | 2024-10-30 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99e7e502-891d-3c87-8302-5cea33763807 | -2.34353 | -57.1528 | 2024-10-30 05:08:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76b6a6a6-c85b-3459-86ea-494b7281d009 | -3.84953 | -56.97622 | 2024-10-30 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bfd78aa-0642-38e5-abfe-79eee83de373 | -3.78325 | -57.09621 | 2024-10-30 05:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 95a58710-bc5e-312f-8594-f4d93d541f80 | -3.71578 | -57.13459 | 2024-10-30 05:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc3cc917-c7a0-3193-becc-9520a7ef7b1c | -3.69644 | -57.10689 | 2024-10-30 05:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ab3d0f3-fac1-3fcd-9611-4475e2ebabfb | -0.63265 | -58.00497 | 2024-10-30 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ce6adb6-c9d5-3d59-8878-7d71c97fc786 | -3.61746 | -58.55462 | 2024-10-30 05:08:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25663832-1089-3f8d-bbe2-72a00d02d225 | -3.61406 | -58.55408 | 2024-10-30 05:08:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa5eb4b5-e246-3791-8a9f-3706b9bae805 | -3.55208 | -58.68006 | 2024-10-30 05:08:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7500b35-a613-3abe-b7d5-1c8e0ae38660 | -3.54925 | -58.67582 | 2024-10-30 05:08:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d81a9076-4f04-31cf-bf72-eca98400af05 | -3.54866 | -58.67952 | 2024-10-30 05:08:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1b1d3e6-6f55-3909-acd8-56050c19972c | -3.49393 | -59.28944 | 2024-10-30 05:08:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5849407d-f567-35d8-a656-9d9f2dd67085 | -3.49331 | -59.29333 | 2024-10-30 05:08:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 117f7f67-bdb4-3882-9654-eef7a53ffe3d | -3.438 | -59.57268 | 2024-10-30 05:08:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc6e3530-fa57-3db0-a364-5138eec7b6f9 | -3.43741 | -59.62211 | 2024-10-30 05:08:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27c5cfcd-8828-3ea7-bf25-7b326e4751ac | -3.43677 | -59.62614 | 2024-10-30 05:08:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a81beefd-e740-392a-87d0-80c7b4f385f5 | -3.40114 | -59.66613 | 2024-10-30 05:08:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ed53a42-4133-36f8-86e9-ea7d9ade6361 | -3.18558 | -58.95373 | 2024-10-30 05:08:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f378e32-cea8-3a17-9e82-ce77d2a0f2f9 | -3.14959 | -59.08937 | 2024-10-30 05:08:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a4058e7-90b8-378d-ab51-ea550ec05f6c | -3.0713 | -59.21373 | 2024-10-30 05:08:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ade23ca-86c0-368c-97ab-1404e105d87b | -3.07068 | -59.21763 | 2024-10-30 05:08:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c96f3663-061c-3da3-8daf-a8a216b47ec1 | -4.22592 | -59.94328 | 2024-10-30 05:08:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff339109-7a39-3043-9975-8f2e1cbe6ca4 | -4.2255 | -59.85525 | 2024-10-30 05:08:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 216d3c86-0226-3a03-97bc-1644863eaeb2 | -4.02548 | -59.83841 | 2024-10-30 05:08:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68d90188-c07d-3789-aa95-fc1e8f1b2bc9 | -3.98536 | -59.14639 | 2024-10-30 05:08:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18aa5228-cde8-3c7e-bde5-f6bc69972a93 | -3.98329 | -59.14677 | 2024-10-30 05:08:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 693da395-d7dd-37db-a890-b76f2d59d1ac | -3.78965 | -59.66229 | 2024-10-30 05:08:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d363264-01fb-38c1-b711-6df73119b710 | -3.7637 | -59.3936 | 2024-10-30 05:08:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e7a725c-9089-3b2f-be28-e769ebb1ee44 | -3.70786 | -58.93297 | 2024-10-30 05:08:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1da5677e-88f5-3bc5-8aa8-177486f513fd | -5.24486 | -59.98443 | 2024-10-30 05:08:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 483066f8-6be2-3a74-bd84-7d53462fc31d | 1.12894 | -59.44568 | 2024-10-30 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1587d6f9-df2c-36ae-b46e-fc65b62546eb | 1.12824 | -59.4412 | 2024-10-30 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9ac9ad3-a3b5-36ed-b9cb-18651f2b9fa4 | 1.12522 | -59.44625 | 2024-10-30 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81292b7f-6957-3395-8931-aec224a63fb3 | 1.12452 | -59.44178 | 2024-10-30 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3665f893-623a-3eeb-8cde-cc45eb20aca6 | 0.99605 | -59.45969 | 2024-10-30 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4d2aed5-93e3-351d-bf0f-6d227873a552 | 0.92611 | -59.56057 | 2024-10-30 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f741b80-8005-3345-93b9-ac01ab5f2d21 | 0.92541 | -59.55608 | 2024-10-30 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b42a280-890e-37ba-880d-0d2449ccd373 | 0.8657 | -59.61604 | 2024-10-30 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61402589-9465-3a2a-970e-8bf5dcb7e87c | 0.64081 | -59.62141 | 2024-10-30 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b3ef1b5-daee-3c27-92bb-746569471d95 | 0.63708 | -59.62199 | 2024-10-30 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0139401d-afa5-35af-9929-078925eac128 | -2.08491 | -59.93196 | 2024-10-30 05:08:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf5d7093-3bf2-39c7-b42a-4f24973b3be0 | -2.05258 | -59.85176 | 2024-10-30 05:08:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 947a7528-635e-389b-8059-c16169c8d5c0 | -1.85836 | -60.28774 | 2024-10-30 05:08:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9147eb9f-2321-34cb-afc2-4a0d2aec4042 | -1.42761 | -60.28918 | 2024-10-30 05:08:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55348052-bf2f-3ee4-9183-60d1bec75a05 | -1.42383 | -60.28856 | 2024-10-30 05:08:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a01b577d-c808-3eb7-b709-6f49152f9836 | -1.42079 | -60.28339 | 2024-10-30 05:08:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7bc8a3a-61fb-3d74-b36c-f02f4bf74c01 | -1.42053 | -60.28571 | 2024-10-30 05:08:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 493e07fd-6399-3199-8073-2ed1f244784b | -1.42005 | -60.28795 | 2024-10-30 05:08:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a2d665b-64fa-360a-9c7e-c82ec6c601d8 | -1.29794 | -60.22667 | 2024-10-30 05:08:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f217516f-fb6a-35fe-bac5-c9cd09e1e3ac | -2.63703 | -60.01549 | 2024-10-30 05:08:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe99e371-9266-3ae7-8654-9fbb9dee6292 | -2.21274 | -60.15932 | 2024-10-30 05:08:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4721d99-1182-3b40-9ef7-b6de71fb0680 | -3.76373 | -61.19916 | 2024-10-30 05:08:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0a7ef8c-c485-315c-bef5-4ed8db2fc5b6 | -3.76163 | -61.19645 | 2024-10-30 05:08:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcdd157b-0341-37c7-96a7-36337e92144e | -3.65673 | -61.09079 | 2024-10-30 05:08:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05f17d2e-d86f-3917-904f-9a5f76016bdc | 2.03095 | -61.23066 | 2024-10-30 05:08:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32f75e6b-d777-3a80-9d7b-414496aefd6f | 2.02673 | -61.23132 | 2024-10-30 05:08:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d13f236-b4d3-31ae-9842-4650f94237d7 | 1.89161 | -60.48121 | 2024-10-30 05:08:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6039bfdd-0e7a-3d1f-9565-f7aa070b532d | 1.8876 | -60.48181 | 2024-10-30 05:08:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41d52f88-57e8-3a36-9d96-3519c1840392 | -0.15353 | -60.8671 | 2024-10-30 05:08:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9edb0a9-3113-3e57-90f5-8fc3b873ee0a | -0.15408 | -60.86367 | 2024-10-30 05:08:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2eb5e93-8e98-3482-9b57-de50f550a057 | -0.14499 | -60.86931 | 2024-10-30 05:08:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa5181af-d927-3981-aa06-42b893a6ce43 | -3.09613 | -61.70601 | 2024-10-30 05:08:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea5a1f56-959e-301b-9ac5-b131e5a5bf24 | -3.09556 | -61.70951 | 2024-10-30 05:08:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efc1d845-ec05-3bca-baac-011fc0a59112 | -3.09152 | -61.70888 | 2024-10-30 05:08:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b50a9540-86e9-3905-b40c-49d0a72a8053 | -3.08691 | -61.71177 | 2024-10-30 05:08:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a158f543-a2fb-3e11-88b3-1a70170b2853 | -2.98408 | -61.44902 | 2024-10-30 05:08:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60d09db6-f432-3841-a596-83bf984a8d34 | -0.76796 | -62.87645 | 2024-10-30 05:08:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7e25c73-ccdb-3a06-9de5-e9c1195cd581 | -0.76725 | -62.88102 | 2024-10-30 05:08:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bede302-ebe2-3910-9560-89ff14ec3135 | -0.7651 | -62.89479 | 2024-10-30 05:08:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d85ef97e-493c-3a63-b54c-e2c4cf11e895 | -0.76439 | -62.89938 | 2024-10-30 05:08:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8ed8038-839f-35a0-b5a0-67d5f846a5cc | -0.762 | -62.88488 | 2024-10-30 05:08:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f78a2b6f-89e3-3419-a3f2-b34200e4ffb9 | -0.75985 | -62.89865 | 2024-10-30 05:08:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c699861d-fbab-37d6-8214-ec402e9e8a3e | -0.75603 | -62.89333 | 2024-10-30 05:08:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 565aa674-8313-3b13-b0a5-70a33d20dc87 | -0.75531 | -62.89793 | 2024-10-30 05:08:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8dd7603d-f7db-3a21-9291-c1476dc69603 | -1.00542 | -62.79807 | 2024-10-30 05:08:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bfb493b4-0729-3251-aff0-e54528b9dff6 | -0.77489 | -62.89167 | 2024-10-30 05:08:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff2c12b2-0e71-3717-a5dd-a298c1d709fd | -6.09128 | -43.55324 | 2024-10-30 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3244191-facc-3f7d-8d41-c4c94651797a | -6.08411 | -43.55257 | 2024-10-30 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 590e3432-9eb3-336f-a431-e7b2b61e6075 | -5.83485 | -43.6536 | 2024-10-30 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 558eeb7b-ac48-391b-aebf-d7c13fb41537 | -5.82778 | -43.65256 | 2024-10-30 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f81c2fd9-a9a4-3083-98d2-f6fe2ea8f1c7 | -4.26875 | -43.44266 | 2024-10-30 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 8983adbd-9d1b-3b4f-b52b-6af4194eccae | -4.34933 | -43.77789 | 2024-10-30 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 936246e8-3aac-3200-a89f-e6d4c464a01f | -4.34885 | -43.78078 | 2024-10-30 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21b58f96-e676-30ab-959c-1afb66f336cd | -4.34847 | -43.78407 | 2024-10-30 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a356c71-58fa-36c5-b3b6-ea19dcb6387f | -4.34796 | -43.78693 | 2024-10-30 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b797ed2e-15a5-319c-9be0-829ba90fe60d | -4.34159 | -43.78305 | 2024-10-30 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1bff03e-8827-38cb-957d-9074c836c304 | -4.34105 | -43.78615 | 2024-10-30 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d9402eb-b163-3356-bd79-c2a820719e73 | -4.2706 | -43.44133 | 2024-10-30 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 65d95018-7763-3f75-8875-f7a0e5452fdb | -4.26967 | -43.44781 | 2024-10-30 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 234e2776-0830-3286-8fa8-c58ff6240819 | -4.26878 | -43.454 | 2024-10-30 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 44b01dc7-e127-3df0-9789-404c943d6550 | -4.26788 | -43.44904 | 2024-10-30 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 6b32db35-2f81-3f7f-a574-9c4ca9e20788 | -4.26358 | -43.44034 | 2024-10-30 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 72314b09-e1b5-350e-9858-ebb255b50b92 | -4.26266 | -43.44678 | 2024-10-30 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 36797aae-19b5-343a-8f34-9e344b815302 | -4.26175 | -43.4531 | 2024-10-30 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8c3dcb6a-5ee3-3612-8cea-f8bf7cee7120 | -4.25564 | -43.44579 | 2024-10-30 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 390c9f2b-951f-3921-a1c5-fe54fb3a4a71 | -4.25471 | -43.45235 | 2024-10-30 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 315493f0-665f-3155-b2d9-c5238c88f46a | -6.66839 | -44.70084 | 2024-10-30 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0dda76ce-dc80-30fd-bda6-8ccacec04f36 | -6.66465 | -44.70444 | 2024-10-30 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README84.md)
