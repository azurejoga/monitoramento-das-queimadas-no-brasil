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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 383e20e0-2a05-3dc4-ad37-e4a76ede04d5 | -7.48982 | -63.82489 | 2025-07-19 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37d54b37-62bf-3b3a-8fb8-b049f4b75d35 | -8.97372 | -61.51505 | 2025-07-19 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f5d1007-84f4-3169-a0f0-343a8e25d9ec | -10.02279 | -66.83029 | 2025-07-19 05:50:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 10ff56f6-438c-3a33-a0d7-5ba63825aa6b | -8.97429 | -61.51097 | 2025-07-19 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08569243-f0c0-3ac9-9b2d-198b9ce396cc | -10.29603 | -60.54772 | 2025-07-19 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6751b9e4-ac0f-3edc-a0fc-5e5f19a9b1f1 | -10.98712 | -68.52348 | 2025-07-19 05:50:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c13149b8-ec96-3ba0-b9fd-b85dedf94779 | -7.4906 | -63.8184 | 2025-07-19 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d068174a-e52e-3286-aec0-351040ed2be6 | -8.31164 | -55.11119 | 2025-07-19 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e5423f10-f5cc-3c0b-bada-ff9b1f2ce7fb | -10.29672 | -60.54263 | 2025-07-19 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39886b30-5851-3506-b79f-1050d5a7d4b6 | -21.046 | -55.98608 | 2025-07-19 05:53:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1c636ac-1de3-3b64-8cef-7809a5b9b503 | -21.03888 | -55.98533 | 2025-07-19 05:53:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01f80f5b-a3b1-3639-ad61-ad073961df4a | -2.9109 | -48.2325 | 2025-07-19 06:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| e38ecf70-a569-3e3e-99f9-db07240337f1 | -11.7317 | -48.1849 | 2025-07-19 06:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 84d35278-9040-37e6-b16b-305722ffa657 | -2.9108 | -48.254 | 2025-07-19 06:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 74ee8bee-0d3d-3b5a-84d9-acab5d45ae89 | -11.7317 | -48.1849 | 2025-07-19 06:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| e451e5d7-8f81-3068-aada-d41e8426a735 | -2.9108 | -48.254 | 2025-07-19 06:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 5b9c3b98-1e1f-35a2-8d82-00387284594e | -8.97114 | -61.51091 | 2025-07-19 06:16:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b21784f-16af-3d57-b564-5c12efb3b59b | -9.02295 | -59.77012 | 2025-07-19 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a58f91c-19f8-337c-9911-e31489dd74a8 | -10.98462 | -68.52383 | 2025-07-19 06:16:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0b3c7bb4-5ab0-3edc-b4b4-cd4314996f7a | -8.97571 | -61.51475 | 2025-07-19 06:16:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 096d46ba-b93c-39a9-a684-8c7d4f5c5ec2 | -10.04085 | -67.82577 | 2025-07-19 06:16:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 901e8cb0-89c7-3e5c-9e56-6ae8d0d51254 | -7.49149 | -63.82131 | 2025-07-19 06:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e58c9feb-836c-3e3a-b601-301edc053c04 | -7.49112 | -63.82052 | 2025-07-19 06:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d2c32830-c441-3ec5-a8ef-835da91a1047 | -9.01573 | -59.76898 | 2025-07-19 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b876e3cb-7db1-3f4a-a629-7ef332394f1e | -8.96983 | -61.50856 | 2025-07-19 06:16:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 269454cc-9669-3da5-8d54-ec023bb914bf | -8.97638 | -61.50938 | 2025-07-19 06:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3233f7f3-e349-3289-8658-a77ca01297b8 | -7.49063 | -63.82417 | 2025-07-19 06:16:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0de6b4c-3f03-3fdb-a581-90f676c92526 | -11.7317 | -48.1849 | 2025-07-19 06:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 27651c05-d53a-3e07-84c4-375493b6d8b1 | -2.9109 | -48.2325 | 2025-07-19 06:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| f603d971-5fe1-39e9-be9a-d00324871ec4 | -2.9108 | -48.254 | 2025-07-19 06:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 8a8e18ac-21e0-3103-9840-4979dd793ffb | -11.7317 | -48.1849 | 2025-07-19 06:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| cfe545df-cc0f-3bd8-847d-ac00ac89d7dd | -2.9108 | -48.254 | 2025-07-19 06:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 849e9a43-0cde-30e4-9784-2773f0da77a6 | -2.90473 | -48.2158 | 2025-07-19 06:35:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| b9a9a4a0-6fef-30eb-bde5-1ae40a4d238a | -2.89984 | -48.25049 | 2025-07-19 06:35:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 6d86db86-ce36-3db0-bd2e-61ff96d92626 | -8.96996 | -61.50525 | 2025-07-19 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9d6c149f-f12f-3b58-91c1-fa1d317926cf | -9.01867 | -59.76139 | 2025-07-19 06:37:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e9573f24-f1bd-3af2-88db-1fc982c94af0 | -10.29581 | -60.54216 | 2025-07-19 06:37:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 52b17695-8ead-321f-a0c6-77984488db47 | -2.9108 | -48.254 | 2025-07-19 06:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 8250bdd6-1ded-309e-9304-e410bfffb660 | -2.9109 | -48.2325 | 2025-07-19 06:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| d2c445c1-4663-377e-8cec-670c771c1a4b | -14.17013 | -58.20237 | 2025-07-19 06:40:00 | AQUA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| def41336-9145-3f9f-a4e7-525356695d4f | -14.17153 | -58.19239 | 2025-07-19 06:40:00 | AQUA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 00423351-cd3c-3262-bb3a-5a8c4a5c0905 | -10.98568 | -68.52756 | 2025-07-19 06:40:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4099b90-e29f-3d92-8066-7d30202159de | -10.98632 | -68.52209 | 2025-07-19 06:40:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0d49707-fc21-3b1f-b2d0-d0c3c1562946 | -10.98554 | -68.52634 | 2025-07-19 06:40:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4deaa78e-13d5-3875-a063-fe4296cc0ee7 | -11.7317 | -48.1849 | 2025-07-19 06:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| b94fc457-0b08-3e31-ac1e-7984b301f7a2 | -2.9108 | -48.254 | 2025-07-19 06:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 8287b5b1-89ec-3cbc-b9c4-a8768cd720b9 | -22.1161 | -52.5776 | 2025-07-19 07:00:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 44.6 |
| d7d202bb-faad-3b03-bbef-556ccbdedb4d | -2.9108 | -48.254 | 2025-07-19 07:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| ad3e4d60-bb4e-3bbb-9839-e08142e88039 | -22.1155 | -52.6 | 2025-07-19 07:00:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 45.0 |
| 6618725d-a540-3ff2-b66e-4c69b43bee98 | -11.7317 | -48.1849 | 2025-07-19 07:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 7d8e457b-7d43-3a29-a35a-5c44a90f7dad | -22.1161 | -52.5776 | 2025-07-19 07:10:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 100.3 |
| 74201298-c6cb-3514-ba93-a1f6e659a284 | -22.0948 | -52.6041 | 2025-07-19 07:10:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 73.0 |
| adf7f60a-b8ae-382a-9c1f-0bbc21f9a99f | -2.9108 | -48.254 | 2025-07-19 07:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 378f4f30-60ce-3efd-b921-bfa3ebb07932 | -22.1155 | -52.6 | 2025-07-19 07:10:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 117.9 |
| 5f682adb-f1f2-3114-bc5b-76e0cac7060d | -22.0953 | -52.5818 | 2025-07-19 07:10:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 62.1 |
| c2fb9d66-d44a-3dd6-86bd-1d97b894f79d | -11.7317 | -48.1849 | 2025-07-19 07:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| abd3e3da-2a20-3295-9b9a-e36ed0886bb5 | -2.9108 | -48.254 | 2025-07-19 07:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 061fba8f-3689-350d-a2f6-b0c0c0308f6c | -2.9109 | -48.2325 | 2025-07-19 07:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 02d42249-98dc-3736-aad0-1b1c81b2cac3 | -2.9108 | -48.254 | 2025-07-19 07:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 0200de07-dca8-3c12-a891-773518d374c0 | -10.7261 | -46.7782 | 2025-07-19 11:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 1b1e4cf9-2d97-3fe4-89d9-f6996216c252 | -10.7261 | -46.7782 | 2025-07-19 11:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 98f6cd69-66ce-3556-abd7-3ba5544aea4b | -10.7261 | -46.7782 | 2025-07-19 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| fdf72f5f-efd2-34db-a08d-ee9d01e01c8a | -10.7257 | -46.8006 | 2025-07-19 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 2d56a9e0-8a5b-3c5b-880a-9b96dad3c96d | -14.7011 | -45.0685 | 2025-07-19 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 3a224d7f-8934-3b2b-a99d-7eb6d249b4ad | -10.7257 | -46.8006 | 2025-07-19 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| c7555993-f8a1-3468-aca4-7f7f93c4056c | -10.7257 | -46.8006 | 2025-07-19 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 1c06add9-a80d-32ed-9436-e6d383c73362 | -14.7011 | -45.0685 | 2025-07-19 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| c5cbe728-938e-30a4-a149-a3ba5cad4e30 | -10.0311 | -46.3012 | 2025-07-19 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| f8f4504e-61fa-3801-96c1-a7d3d6413b1b | -10.7257 | -46.8006 | 2025-07-19 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 4e1e4ac8-9891-308a-a2ac-3f7df3d1f9e0 | -7.33816 | -45.32995 | 2025-07-19 12:29:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cc094aa5-31ee-3756-b1de-31159e0ec024 | -6.36048 | -45.3757 | 2025-07-19 12:29:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f834f8f8-88d8-3b21-b3b6-02cc98c0a27b | -7.4861 | -47.49413 | 2025-07-19 12:29:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6e52afc5-e1b0-3905-80b3-8341311acf03 | -7.62981 | -44.30008 | 2025-07-19 12:29:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 073b1c52-2d3f-3226-901e-b7c12325e98c | -8.26985 | -46.07642 | 2025-07-19 12:29:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0d2618d6-757c-33a5-a0d0-ca399ecc1f68 | -6.3589 | -45.38727 | 2025-07-19 12:29:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 61018d40-a6d7-3dbf-8d80-22f9c5fdc565 | -6.17029 | -48.05869 | 2025-07-19 12:29:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6c87dddb-1179-3657-aee1-fd4a57da405c | -7.58075 | -49.91865 | 2025-07-19 12:29:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 0c9b1764-5833-3adf-83ee-2852ef152270 | -8.46562 | -48.39024 | 2025-07-19 12:29:00 | TERRA_M-T | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e550321e-eb6b-3725-93dd-7cf16a716d60 | -7.06357 | -44.06532 | 2025-07-19 12:29:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a03a5a53-2f0b-34e5-b3f8-2981f62def6e | -10.03668 | -46.30587 | 2025-07-19 12:29:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 306bccac-a32e-33cd-af11-4f337afb3184 | -2.24488 | -48.067 | 2025-07-19 12:29:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 9a407139-47e7-3890-af91-3e962dea7c79 | -7.83896 | -44.19318 | 2025-07-19 12:29:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 6f9abd99-0b8d-316e-80eb-bd43014c2b77 | -9.81188 | -47.73799 | 2025-07-19 12:29:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b1ca77f9-ab87-38a0-ade2-df7ed7c46f7d | -9.84949 | -44.69763 | 2025-07-19 12:29:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 2a580beb-ebb9-37f8-904e-4630944304b3 | -8.01337 | -43.65944 | 2025-07-19 12:29:00 | TERRA_M-T | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a99eb9f2-1469-395b-b687-11cb1e0a1f0f | -3.04671 | -49.42147 | 2025-07-19 12:29:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 6e2764ab-23c8-33d8-8e4d-3b844f53c71b | -4.30885 | -48.105 | 2025-07-19 12:29:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 4416fe2f-7717-37ec-8497-ea90b432be22 | -2.91269 | -48.24586 | 2025-07-19 12:29:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 8f363dda-7223-3969-885f-fda878969de8 | -7.87339 | -44.70186 | 2025-07-19 12:29:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9c5334c6-7278-39cd-a28d-aeb41315dbf5 | -9.80689 | -48.56171 | 2025-07-19 12:29:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5de190a5-1236-3bbf-9a4c-d8d97e251938 | -3.68394 | -47.43958 | 2025-07-19 12:29:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| c8d7635b-39c5-3071-92bb-0a84cca7ddc0 | -4.81784 | -47.31726 | 2025-07-19 12:29:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 77e51478-385b-37ff-91bb-d09e61880031 | -3.67774 | -43.05023 | 2025-07-19 12:29:00 | TERRA_M-T | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 32c49c6d-6c36-3bbe-a801-ffef2dcc2c7e | -3.11749 | -47.00978 | 2025-07-19 12:29:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 322cf1cf-eea5-3d6e-8a07-e89ee05bdf31 | -8.07003 | -50.11029 | 2025-07-19 12:29:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4f4d2d47-585d-328e-8ad9-e8e6c461cce6 | -4.25438 | -48.54459 | 2025-07-19 12:29:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f3832597-2cb6-3c0d-9272-db92560c7b20 | -7.17567 | -44.09314 | 2025-07-19 12:29:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e766efa4-a8d1-3e5d-8f5c-23f15419bff9 | -6.9673 | -45.49989 | 2025-07-19 12:29:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 65fc25b9-bfc9-3036-b892-b4f76004dee3 | -2.91396 | -48.23708 | 2025-07-19 12:29:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 3b73e864-d81d-3f65-a1b8-c3432325cec2 | -3.68268 | -47.4484 | 2025-07-19 12:29:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README31.md)
