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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 607fc0a6-5ccf-3932-9c3c-8eed528d96f9 | -11.483 | -49.4831 | 2024-10-09 00:56:11 | GOES-16 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| aa988fe0-ac5a-37d8-b704-9b16be1feec9 | -11.5233 | -65.137 | 2024-10-09 00:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 713fc747-9014-3b50-b5d0-8e627bd305a6 | -11.5726 | -58.9619 | 2024-10-09 00:56:12 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| aeea5799-5c39-33f7-a53a-878fd222c3bb | -11.5728 | -58.9423 | 2024-10-09 00:56:12 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| d8d1f283-c0b7-35a5-a1a0-9840aac68bb4 | -11.6806 | -64.0312 | 2024-10-09 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| c7298624-94c9-3008-a21d-7ce6b8435131 | -11.6808 | -64.0121 | 2024-10-09 00:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 51db6087-7ae8-3155-aa2e-ca415c66dd04 | -12.0107 | -51.0744 | 2024-10-09 00:56:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| db5cccb7-4df7-3912-84b5-16c87eb3c524 | -12.011 | -51.0531 | 2024-10-09 00:56:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 5d0f58ed-1d00-362a-a54d-58ae3972a923 | -12.7673 | -44.8904 | 2024-10-09 00:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| ed303800-da27-32df-b310-e978de5cdefa | -12.7678 | -44.8671 | 2024-10-09 00:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| a81fffa4-e6a5-3aa0-ac07-8cca15df306c | -12.6676 | -63.0819 | 2024-10-09 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 91.1 |
| ed63bebd-d47a-39fa-94a0-aa8fd880e41c | -12.7501 | -62.269 | 2024-10-09 00:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 059556a4-a1d6-34a2-a43b-d08d8c2fad2f | -12.769 | -62.2678 | 2024-10-09 00:56:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| b364cc0e-3c9e-30f2-b57e-95027a819183 | -12.8589 | -62.8211 | 2024-10-09 00:56:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 93b79b1a-ca38-3a32-abea-5e6e92191b5e | -12.8591 | -62.8018 | 2024-10-09 00:56:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 143.8 |
| d59c68e6-7afc-3bff-bd43-237d883349fe | -12.8593 | -62.7826 | 2024-10-09 00:56:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 469e1b9f-89f5-32dc-ad51-557ec3029e21 | -12.8779 | -62.82 | 2024-10-09 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 148.9 |
| 57ebd823-5917-3be9-b2a9-96ad114875ea | -12.878 | -62.8007 | 2024-10-09 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 335.3 |
| bad8654a-5f0b-3f81-b219-98a1ca48bfaf | -12.8782 | -62.7815 | 2024-10-09 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 19feb226-ac47-315a-834b-c133dbdcad87 | -12.9166 | -62.7214 | 2024-10-09 00:56:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 9e387f51-4f47-3dac-bf54-7eeaa15186f3 | -12.9377 | -62.4697 | 2024-10-09 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| ef50751e-196f-3298-bc6f-7cd2ba369b18 | -12.9378 | -62.4504 | 2024-10-09 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 88e31acd-b3ac-37cc-a32f-6187a5bdbaf1 | -12.9566 | -62.4685 | 2024-10-09 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 1a655b06-8426-34cb-9348-434ae2b5596f | -12.9568 | -62.4492 | 2024-10-09 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| f74267c4-01aa-3d2d-95f4-f20a5b6f4908 | -12.9756 | -62.4673 | 2024-10-09 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |
| e18caf4c-bd8b-3824-b5bf-f6fa3dde3f74 | -12.9757 | -62.448 | 2024-10-09 00:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| f8b8c2ef-4ac2-3904-9c55-834a0b90d24b | -13.3788 | -61.9388 | 2024-10-09 00:56:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 484931bd-9a04-301b-94d5-fe24b802d287 | -13.379 | -61.9194 | 2024-10-09 00:56:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 70.7 |
| f1663175-d980-3749-9044-a9b41c5c8a24 | -13.3978 | -61.9376 | 2024-10-09 00:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 116.8 |
| dc0be4e5-4b4c-30cc-8515-1cd3e2263472 | -13.398 | -61.9182 | 2024-10-09 00:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 2231eea9-6121-3910-96b8-747e9eee7d8e | -13.417 | -61.9169 | 2024-10-09 00:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 38bb6f13-896e-347e-83fc-d55050ec705a | -14.1192 | -44.9872 | 2024-10-09 00:56:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 170.7 |
| f94f2aab-bd0c-397b-bb34-3990373f3b6c | -14.1197 | -44.9637 | 2024-10-09 00:56:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 208.1 |
| 9664ffa2-bda3-35c1-aaae-f4397ecf3fbe | -14.0297 | -50.5625 | 2024-10-09 00:56:25 | GOES-16 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 0b796053-c478-3812-9a6f-9a72041c12ea | -14.1392 | -44.9603 | 2024-10-09 00:56:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 48084525-c310-37fd-8b14-45ec81ba94dc | -15.5996 | -57.3699 | 2024-10-09 00:56:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 70b22033-d002-33b7-b29f-f7ee276c60f0 | -16.54 | -45.2948 | 2024-10-09 00:56:38 | GOES-16 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 80.7 |
| b1dbb434-61c0-32b8-8460-6a2052fc49b6 | -16.5406 | -45.2711 | 2024-10-09 00:56:38 | GOES-16 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 7108bf52-f7f0-3f5c-a492-f1f0ea950ebb | -16.3988 | -55.9479 | 2024-10-09 00:56:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.5 |
| dde1712c-b721-390c-bb4f-19a127791d1a | -16.4184 | -55.9455 | 2024-10-09 00:56:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 108.3 |
| 25048811-9266-347d-a8c2-f46470fb11ff | -16.4187 | -55.9248 | 2024-10-09 00:56:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 11b119cb-db6c-3af6-8427-adbd8a1c6d80 | -16.4379 | -55.9431 | 2024-10-09 00:56:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 843a0d8d-c146-38c8-8588-09745e21e767 | -16.4383 | -55.9224 | 2024-10-09 00:56:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 6a7d442e-83b0-3b17-b7da-0166c6eec5eb | -16.7575 | -56.7081 | 2024-10-09 00:56:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 6633157b-cd27-32c7-ad72-b04bbd20a601 | -16.777 | -56.7057 | 2024-10-09 00:56:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| f3cf51a7-0da6-31c2-84e4-d2733db2413e | -16.8547 | -56.7375 | 2024-10-09 00:56:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.9 |
| 58effd7c-90ae-300f-9c8a-57296959305f | -16.8743 | -56.7352 | 2024-10-09 00:56:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.9 |
| 332f9a01-f988-302f-b3d0-e438f5839e3f | -16.8747 | -56.7146 | 2024-10-09 00:56:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 7dc3ecbb-6206-3f52-862c-064619e65aa1 | -16.9518 | -56.7875 | 2024-10-09 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 030b8039-91c2-3f13-b4a8-bff034286f41 | -17.0878 | -56.8534 | 2024-10-09 00:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 7c6f27ba-e7db-3094-8749-b0c8578602e6 | -17.1271 | -56.8486 | 2024-10-09 00:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 38139e52-64be-38c0-9c0c-3e59f1ea0667 | -17.1467 | -56.8463 | 2024-10-09 00:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 5330a42a-46b8-3af5-8784-b58284a16e99 | -17.1588 | -56.1222 | 2024-10-09 00:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 105.4 |
| 128b5252-1bab-3b64-a7c6-56cf8392779d | -17.1591 | -56.1014 | 2024-10-09 00:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 9a236552-bd85-3f57-8df6-69d85c912031 | -17.3353 | -55.0156 | 2024-10-09 00:56:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 731ec4a3-ef6a-302a-ba6b-e5b477e6c9f5 | -17.3357 | -54.9946 | 2024-10-09 00:56:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| d06ad13f-20b2-3fe6-9f8a-c6091db49366 | -18.5993 | -57.2629 | 2024-10-09 00:56:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.6 |
| ef1abe1a-6f89-3b1b-a8de-3cafb45ad079 | -18.5996 | -57.2422 | 2024-10-09 00:56:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.1 |
| f1d8d2d9-1346-3f29-ab8a-1f8253ca2b8d | -19.9924 | -42.4346 | 2024-10-09 00:56:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 119.4 |
| 9bd3aff8-0ed5-3d91-b7ad-991560a99c6d | -19.9998 | -42.2054 | 2024-10-09 00:56:56 | GOES-16 | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.8 |
| 08d10ef8-e35a-3cb5-a790-74200134f518 | -20.0006 | -42.1799 | 2024-10-09 00:56:56 | GOES-16 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 290.7 |
| a6d405da-debe-3bbe-bc28-c8085fba3aec | -20.0122 | -42.4541 | 2024-10-09 00:56:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 128.1 |
| 20e6dc2f-ff68-39bf-8c9b-2dd84f8dc310 | -20.013 | -42.4287 | 2024-10-09 00:56:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 199.1 |
| eaa636f2-823e-3ab5-86bb-1291a825267b | -20.1087 | -48.8261 | 2024-10-09 00:56:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 387c6865-3f8c-3bba-989f-b4f8e8d64840 | -20.2915 | -43.9444 | 2024-10-09 00:56:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 148.5 |
| e303bf49-8df3-3b9a-b679-fd30f49012a6 | -20.3346 | -48.7307 | 2024-10-09 00:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 278.6 |
| 435a003f-dc6d-3ecd-995a-56dee30cdc11 | -20.3352 | -48.7076 | 2024-10-09 00:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 267.9 |
| 9e702d3b-4bbc-3f94-af77-77220fed74d0 | -20.3551 | -48.7262 | 2024-10-09 00:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 469.4 |
| 2793427a-811f-3845-90d7-072751f1b48c | -20.3557 | -48.7031 | 2024-10-09 00:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 391.2 |
| 09cff9df-dfa1-31b4-8aca-609166f9ac10 | -20.3755 | -48.7217 | 2024-10-09 00:56:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 7517cfd6-4f49-3dcb-98d2-2270852787c6 | -20.3761 | -48.6986 | 2024-10-09 00:56:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 131.7 |
| a31bc779-79bf-3da1-bd38-b756821afc7c | -20.4133 | -48.8282 | 2024-10-09 00:56:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 6e181087-8651-39b4-90bf-b521b15b339d | -20.7477 | -48.5229 | 2024-10-09 00:57:01 | GOES-16 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 70.9 |
| ddeef21b-f7f4-3670-9fb9-b9a00c7abca1 | -20.7839 | -47.2559 | 2024-10-09 00:57:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 301.0 |
| 8cf22bc9-1e00-3d39-b885-caa19597085c | -20.7846 | -47.2323 | 2024-10-09 00:57:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 248.8 |
| e2f703e7-ee9b-3e6b-a6da-3c8374631b83 | -20.8045 | -47.251 | 2024-10-09 00:57:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 81be1113-d1d3-35ee-8225-b8d9ef1e3605 | -20.8052 | -47.2273 | 2024-10-09 00:57:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 268a0a27-2302-3888-b8e9-10f351bf4770 | -21.552 | -46.9712 | 2024-10-09 00:57:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 90.4 |
| b23d4519-5b79-38c2-b177-b3b02b719165 | -21.6259 | -44.6329 | 2024-10-09 00:57:05 | GOES-16 | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.6 |
| f9370112-4d86-3fad-9f82-f15f59a51dc8 | -21.572 | -46.9898 | 2024-10-09 00:57:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 6934dcd5-fcfd-3058-940f-a304a8a4e44f | -21.5727 | -46.9659 | 2024-10-09 00:57:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 6777a444-2ece-3a45-8a31-697a9547a550 | -21.6468 | -44.627 | 2024-10-09 00:57:05 | GOES-16 | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.6 |
| 52e22089-6a08-39fe-bc63-e39c3eb60081 | -21.5656 | -47.8878 | 2024-10-09 00:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 89.3 |
| c469a998-7b08-37d0-a505-6330f1306452 | -21.5857 | -47.9063 | 2024-10-09 00:57:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 84.7 |
| c8c3ed6e-2e6b-3869-8dd6-c47ed76a119d | -21.5864 | -47.8827 | 2024-10-09 00:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 110.4 |
| eeef22bc-6fd6-3311-bdd9-2c2a657d9868 | -21.8373 | -49.1726 | 2024-10-09 00:57:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.4 |
| 3a37031e-e932-37a6-9099-c1c57aec0ebe | -21.838 | -49.1493 | 2024-10-09 00:57:06 | GOES-16 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.1 |
| 58ce204d-8d49-314b-8344-ef169fad137b | -22.5806 | -48.5514 | 2024-10-09 00:57:10 | GOES-16 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.8 |
| 9b68bdac-e28b-30d8-bf09-f6aaa922e66a | -22.813 | -48.4462 | 2024-10-09 00:57:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 0cd7a870-5664-33ca-8f49-c4a17c0cf9dd | -22.8137 | -48.4225 | 2024-10-09 00:57:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 038b15f8-c14d-3754-b853-0c327d3f600f | -21.62 | -47.75 | 2024-10-09 01:03:22 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1572487a-ae67-3af2-9b5d-99ea5b2b3188 | -21.62 | -47.7 | 2024-10-09 01:03:22 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2efa7275-e9e3-3ed7-a316-7bb8c52c6b53 | -20.77 | -47.25 | 2024-10-09 01:03:24 | MSG-03 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| be005ac0-e5db-3c43-94a8-883dd236d2c2 | -20.8 | -47.26 | 2024-10-09 01:03:24 | MSG-03 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cf51a6aa-a037-3a3e-89a0-c226321461f4 | -20.33 | -48.73 | 2024-10-09 01:03:27 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bacb6e08-8d97-3d63-9904-13f235258390 | -20.37 | -48.74 | 2024-10-09 01:03:27 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b9f7d636-ebaf-357c-b83b-ee5b7e5d71c5 | -13.88 | -44.56 | 2024-10-09 01:04:04 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5794c415-d050-3b45-8c88-cd31f1ffc0ea | -13.88 | -44.52 | 2024-10-09 01:04:04 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa20744e-5ff0-3765-824a-b863dc2e8dbd | -13.91 | -44.57 | 2024-10-09 01:04:04 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 40ac4540-deb2-39ea-9de5-cadcc95819c5 | -13.91 | -44.52 | 2024-10-09 01:04:04 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README23.md)
