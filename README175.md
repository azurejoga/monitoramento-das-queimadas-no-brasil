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

## Dados Diários - Página 175

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c47defd-9a0f-35e5-b979-1743b0ecc9d0 | -9.92 | -44.84 | 2026-10-07 16:15:00 | MSG-03 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a058fab9-33e1-388a-a3a1-40433247e984 | -12.22 | -44.7 | 2026-10-07 16:15:00 | MSG-03 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9933d8f8-0700-3d9b-89f6-0e716cf22c4d | -6.95 | -45.31 | 2026-10-07 16:15:00 | MSG-03 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1dd64d83-e559-3051-a955-df68167ffe47 | -12.22 | -44.79 | 2026-10-07 16:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a5d3d462-4d3f-385c-8e87-6aec13107e6d | -3.43 | -56.96 | 2026-10-07 16:15:00 | MSG-03 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 10312b09-fe28-3fa2-92a2-09b345ed9667 | -1.9 | -45.42 | 2026-10-07 16:15:00 | MSG-03 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d2a98f05-17e0-3052-90c0-ab3122182b12 | -6.95 | -45.26 | 2026-10-07 16:15:00 | MSG-03 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af9c9727-8a8e-3c05-b7df-9e22dbcdb18f | -3.29 | -54.01 | 2026-10-07 16:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e034247e-bfc1-3bb8-a570-b731a3cb15b9 | -9.92 | -44.79 | 2026-10-07 16:15:00 | MSG-03 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e0f84e91-f56f-3e4f-8be4-752d0895488b | -1.87 | -45.42 | 2026-10-07 16:15:00 | MSG-03 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e3c22951-04bc-30e3-b82c-5d7f285a1c26 | -9.95 | -43.56 | 2026-10-07 16:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a8802c6-d5f5-3388-a067-6d0cf2cb1b54 | -5.73 | -45.18 | 2026-10-07 16:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4081f4c-41ba-395c-acee-2b3cab4b6f14 | -3.29 | -54.07 | 2026-10-07 16:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28d7a14b-38fc-3d4e-8b91-3a48cf55ab1e | -6.69 | -45.36 | 2026-10-07 16:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81b72042-5337-36df-b49e-492e4966ff51 | -12.22 | -44.74 | 2026-10-07 16:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6b08eae5-e272-38ec-bc63-6562a97c7523 | -2.79 | -54.15 | 2026-10-07 16:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c51db223-8ff7-374a-bcf0-e4686c8e2547 | -2.76 | -54.08 | 2026-10-07 16:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 218766dc-3d94-3f68-b3e2-847ee26e093a | -2.79 | -54.03 | 2026-10-07 16:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1998dd9c-0b3c-3d4b-9666-49587b3a6456 | -3.43 | -56.89 | 2026-10-07 16:15:00 | MSG-03 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b13d791-b35e-3910-9798-b399732dc20c | -5.73 | -45.14 | 2026-10-07 16:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9223ee6-5d8e-3476-b332-7dbaca94f050 | -12.16 | -44.82 | 2026-10-07 16:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9101c19b-838c-3ed4-abf6-286eb3002225 | -12.19 | -44.83 | 2026-10-07 16:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5b21c8ed-3416-3b25-b6e6-227c05667a75 | -3.26 | -54.07 | 2026-10-07 16:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdfccc64-6578-3a4b-9005-43c8987d8d5d | -5.72 | -41.7 | 2026-10-07 16:15:00 | MSG-03 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4f4f2626-8f50-38e7-bf9b-7ea9800f018a | -5.95 | -46.35 | 2026-10-07 16:15:00 | MSG-03 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb399fcb-7a29-3839-940a-00c42d7e68fb | -6.22 | -52.82 | 2026-10-07 16:15:00 | MSG-03 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a91f26cd-c6df-3d6d-8c41-7758bab12e8f | -6.92 | -45.31 | 2026-10-07 16:15:00 | MSG-03 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec279bad-ce3c-30b1-b7c0-04fe59a201bc | -2.79 | -54.09 | 2026-10-07 16:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a30268a0-9339-387c-a495-e745c6ef3a92 | -14.34 | -41.27 | 2026-10-07 16:15:00 | MSG-03 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 27318dda-86d0-3dce-966c-8ce694f1dd87 | -9.806 | -65.0167 | 2026-10-07 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 5b84f66e-82e7-32cd-8e72-bce1cbf25715 | -1.3927 | -49.2727 | 2026-10-07 16:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 14a1e20f-9a99-36c9-a323-6be7f148dd13 | -0.4136 | -52.0357 | 2026-10-07 16:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 71.0 |
| a0ffad64-0d19-3ad2-b8bb-57fca8e88928 | -1.1713 | -49.2969 | 2026-10-07 16:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 7534f5c6-0096-3b8e-9e7c-0895b0a6c0e5 | -9.7499 | -65.075 | 2026-10-07 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| a9df81f4-53c4-35e7-a43d-5faeef6ecd8f | 1.7121 | -55.6261 | 2026-10-07 16:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| fa98ecb7-55d5-3ce5-ac7f-ae3f67fec43c | 1.7671 | -55.5859 | 2026-10-07 16:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 692ebcbe-13ac-3fef-b46f-55fd0bde9d3c | 1.9864 | -55.8789 | 2026-10-07 16:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 3d8ecdb5-da19-3dfe-8bb3-f9daa239f2fc | -9.8061 | -64.9979 | 2026-10-07 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 0e81bf7f-b9ba-3b72-8e53-0cc0249b619e | 1.8767 | -55.7424 | 2026-10-07 16:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 38c82667-a753-3da8-8711-50f1b75cabb4 | -7.8789 | -72.3492 | 2026-10-07 16:20:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 134.9 |
| a066e48d-94f1-3568-9770-4e50a591a14b | 1.6385 | -55.8047 | 2026-10-07 16:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 630e6278-b54a-32ca-9517-ed1e777b92c1 | -10.9762 | -45.4094 | 2026-10-07 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 4041f4fc-cb2c-32b6-abe5-9bc6cafef8f2 | -8.0851 | -70.1169 | 2026-10-07 16:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 74.2 |
| e9267248-3f66-39fa-8a89-a54d7370b563 | -0.3952 | -52.0152 | 2026-10-07 16:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 86d6f833-829a-33cf-be4a-5203188611f7 | -10.9949 | -45.4298 | 2026-10-07 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| f2d029a0-f99b-3a3f-a527-e096e0be0fd7 | 1.6937 | -55.6263 | 2026-10-07 16:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 13edd0e6-e9a6-325f-8100-bbaf9642849a | -7.6582 | -72.4237 | 2026-10-07 16:20:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 8cfaa607-c572-39ff-acaa-0a717e8ae9bc | 1.8768 | -55.7227 | 2026-10-07 16:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 4470db9a-3909-3bf3-bf2c-74a7e7d7ca09 | -8.0851 | -70.1352 | 2026-10-07 16:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 10729f9e-0e4a-35a3-8bfa-1c2fceb470b6 | 3.36 | -51.3454 | 2026-10-07 16:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 67.6 |
| e4b69fa1-1af6-39b0-a0c1-cc1b02bf3b94 | 3.5263 | -51.2778 | 2026-10-07 16:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 105.1 |
| c85337d8-823e-3ac3-94d0-dd67241a2645 | -7.9008 | -70.1928 | 2026-10-07 16:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 415fd53c-47ee-3e16-a75b-3194154cdb18 | -8.3234 | -70.7364 | 2026-10-07 16:20:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 07e3edaa-6ecc-3800-9bac-ef65cf6b245c | -9.4317 | -45.8519 | 2026-10-07 16:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 78d5fa3b-f157-3ca7-80ee-3c1aca2f924f | 1.7671 | -55.6056 | 2026-10-07 16:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 984e60f2-8e77-3d75-a864-d236e21c37dc | -0.3768 | -52.0358 | 2026-10-07 16:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 77.8 |
| b3a29e44-57f3-319a-bd2b-e0867e9f9803 | -12.1746 | -44.7051 | 2026-10-07 16:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 352.7 |
| 7aa210cb-1ac1-360c-afe4-749d871b60ca | -9.75 | -65.0562 | 2026-10-07 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 309742a6-2205-3fba-b13d-decb11c3d693 | 1.5283 | -56.0227 | 2026-10-07 16:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 44132932-93ea-365a-b035-1a799be415b3 | -9.6757 | -65.0401 | 2026-10-07 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 88.9 |
| ffd99efc-0f10-3c3a-96f8-edd3dbec135e | 1.7487 | -55.6059 | 2026-10-07 16:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 13f6230f-c2a7-3439-98fd-053ee46f02bf | -11.1556 | -46.0916 | 2026-10-07 16:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 961bb9e1-1807-3405-93eb-744fca3852e8 | 1.5283 | -56.003 | 2026-10-07 16:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 120c015c-70b9-3738-a60f-ae38c489fb63 | -8.2495 | -70.8289 | 2026-10-07 16:20:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 101.1 |
| d09af439-6d30-35ad-99ad-5262412a7662 | -10.9762 | -45.4094 | 2026-10-07 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 01e964b5-b64c-3835-b54a-1b82e9fc221c | -0.4136 | -52.0357 | 2026-10-07 16:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 1d03d437-d6e9-3f98-83e2-a7f1bc7c796e | 1.7854 | -55.5856 | 2026-10-07 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 8f4e2355-b4e1-317b-9f8e-94a438429adf | -9.806 | -65.0167 | 2026-10-07 16:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 130.5 |
| ced91aa1-6948-3995-917f-748a6c2ee086 | 1.7671 | -55.5859 | 2026-10-07 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| aad16f37-a79e-3a4a-963d-25abbca40eb2 | -9.432 | -45.8293 | 2026-10-07 16:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 6ff53cdd-dc9e-3183-b9e6-35af68fef21e | -10.9949 | -45.4298 | 2026-10-07 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 2c4cd88d-c97c-3ed3-8601-6e1e968ecb40 | -8.339 | -72.6194 | 2026-10-07 16:30:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 945745c9-b5c3-3bbd-bb2f-b16152899cad | -8.3391 | -72.6012 | 2026-10-07 16:30:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 106.3 |
| dd546e57-0574-3903-874b-5be705f6404e | 1.6937 | -55.6263 | 2026-10-07 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| c0da2633-406c-3253-9d69-21e2bd7e32a7 | 1.7304 | -55.6061 | 2026-10-07 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 9e8dc499-2ea2-3470-aa8f-92924ab1ad23 | 1.7121 | -55.6063 | 2026-10-07 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 0a73a1f4-28b2-379b-8c31-99345fbc662b | -11.1556 | -46.0916 | 2026-10-07 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| b8082b4a-7546-3d84-af91-785e8551398d | -1.3927 | -49.2727 | 2026-10-07 16:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| fc770702-d23f-35e9-a8c1-cdd37bba69cd | 1.7671 | -55.6056 | 2026-10-07 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 30ee3282-b11f-307a-b048-479fe61526ab | 1.7671 | -55.5661 | 2026-10-07 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 7f35666c-9fe2-3326-a87f-b60183356f2d | -9.6572 | -65.022 | 2026-10-07 16:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 66dac81d-ab5a-3aa2-a0b6-c39561a57d78 | 1.7121 | -55.6261 | 2026-10-07 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 3165c8a7-ff7a-3157-9b0f-e860c3002639 | 1.6385 | -55.8047 | 2026-10-07 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| b4c4b87f-e203-38b2-ba34-198fd182185f | -9.6757 | -65.0401 | 2026-10-07 16:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 103.8 |
| fafe82e0-f32a-329e-bdc7-fb3bf48b3f28 | -30.4444 | -52.69246 | 2026-10-07 16:33:00 | NPP-375 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 83.4 |
| 6a237e9b-e276-3930-a0f6-8b837cf7720f | -30.44343 | -52.69393 | 2026-10-07 16:33:00 | NPP-375 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 47.3 |
| e0b8e5a0-c51f-3266-8a31-517bd9894dc6 | -28.55503 | -49.40459 | 2026-10-07 16:33:00 | NPP-375 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a83e5c3d-6795-3e30-a855-1e80ed6bc84d | -30.44279 | -52.68083 | 2026-10-07 16:33:00 | NPP-375 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 92.7 |
| 5d61841c-edc5-34b3-8269-c20fb2044814 | -29.87622 | -51.52853 | 2026-10-07 16:33:00 | NPP-375 | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 5.5 |
| c50ec0ef-2360-34c1-8f33-8e29ceefc924 | -28.35363 | -49.67523 | 2026-10-07 16:33:00 | NPP-375 | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 91b41d83-c467-31d9-978f-2d8226886171 | -30.44412 | -52.686 | 2026-10-07 16:33:00 | NPP-375 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 83.4 |
| db623ff4-d42a-3997-ac64-7c9a8f56d66a | -28.55103 | -49.40629 | 2026-10-07 16:33:00 | NPP-375 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 1c13fd70-d60b-3e28-86b9-8ceb45a83dbb | -28.3564 | -49.67442 | 2026-10-07 16:33:00 | NPP-375 | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 491edd30-b9f8-30ab-8eb5-008561db917d | -30.44312 | -52.6875 | 2026-10-07 16:33:00 | NPP-375 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 92.7 |
| 298ae8d9-f24b-3900-b01d-f62a4b2ddf9f | -11.23212 | -44.87002 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ec3d7724-8d10-3399-8c07-857b4a534286 | -18.47078 | -40.86178 | 2026-10-07 16:35:00 | NPP-375 | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 46c5f12f-934c-353a-b57d-34939b31c255 | -11.85276 | -43.55449 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 4f5fb57a-2d66-307c-b6e8-165942ab120f | -11.2349 | -44.02193 | 2026-10-07 16:35:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 0627dc11-9169-338f-b275-e6cc763dbb9a | -12.199 | -48.42378 | 2026-10-07 16:35:00 | NPP-375 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 166.0 |
| b794bb05-6afe-3c12-8b2c-ae42c0bc2774 | -13.07062 | -43.611 | 2026-10-07 16:35:00 | NPP-375 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README176.md)
