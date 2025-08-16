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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f82ea75-e2df-3f63-8ed2-7a87b99cd2da | -6.88236 | -59.15012 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bedd638-8a85-3b98-bf62-eed9feb65636 | -9.18893 | -59.68238 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63180bc0-4c71-31bd-aa8d-c3c683cd490c | -7.5031 | -61.38005 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 198d207a-e203-32c2-9c2c-2132fae6e5b2 | -7.52628 | -61.38369 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db7f3372-2649-3236-89ed-f1b50b99a6ee | -6.94198 | -59.54064 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0cae996-3025-3388-b860-f03a6d3b80ea | -7.28209 | -64.69685 | 2025-08-16 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0390c2ce-6d73-3d8e-8658-a2138f831d1e | -7.67828 | -63.31059 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df9ff697-0950-3813-a1f6-6222712ac9ef | -7.87756 | -61.80851 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db5bf893-3c59-34e2-9146-d1c90e336fa9 | -7.24083 | -60.6428 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6e6beee-1250-398d-b4fc-b55c28c3ffc4 | -6.95425 | -59.52789 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0dcf075-4302-3eee-a0ca-d879f7dc0f84 | -9.50296 | -60.5224 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3a92b8d-b692-3502-bcee-a3d9164c5561 | -9.1665 | -59.64116 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ae1aee5-6864-3062-ac5f-f896565b6c21 | -6.9291 | -59.53495 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0a2cb1d-3436-37fa-9ad2-dc92dd7abd93 | -9.18656 | -59.65194 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d115efb-1593-3f41-bc08-41a1dbe923b1 | -6.939 | -59.64963 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5cebe04b-c208-36d5-ad09-861de1b9809d | -7.52677 | -61.3375 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2873c629-d378-3397-905d-252d2e5def02 | -7.59676 | -63.50396 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a41b282-55b1-3c23-a5d5-147c4a57e48d | -10.04338 | -59.12074 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d52ddb69-fad6-3c9c-a8a1-ecd144c9577c | -8.56156 | -63.92705 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18784f31-7b2d-3428-95af-83e66efd01d1 | -10.43325 | -60.28252 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf60fc6a-b778-3c2c-b495-0a67c06ba1e0 | -8.99006 | -60.49987 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 48f411dd-6072-33d4-bb7b-621671ab1982 | -7.87534 | -61.82251 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9f0075a-1620-302c-b87e-9c97b98d87ef | -8.11388 | -61.1932 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbe43eb0-8c2c-3a2b-9522-35fe81afcc93 | -8.97242 | -61.68327 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 3f5ad8f6-45e7-3c9a-a49d-92f5c41ab6ba | -8.98525 | -60.55316 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d9684b6-01a5-3d50-b58b-d865e0f668b2 | -9.0001 | -60.5231 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79ef0a8c-35f3-3559-a979-16973dd931c2 | -6.93636 | -59.53243 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77be1a85-5ec8-398f-bda2-1ac76cf41b81 | -8.1128 | -61.20013 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00912997-e827-3a08-8c33-845390da0b49 | -6.48144 | -62.93875 | 2025-08-16 05:23:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5aa24492-d816-3ac1-b2d1-ab6d7360b4f2 | -7.41159 | -60.02319 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a564bb0-8140-3680-8987-26c3e7603c47 | -7.95396 | -61.75599 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d9fe31a-ff38-3f67-82de-64e709590e95 | -9.16196 | -59.62537 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3787b35b-a3fc-3442-a03f-ea73ef6ddb21 | -8.99896 | -60.50848 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ee87b2d-dbe8-3ecf-b9fe-a516f3456061 | -10.23773 | -48.3069 | 2025-08-16 05:23:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 87cdff47-19d4-37d8-982e-b518aefb0794 | -9.03486 | -67.43177 | 2025-08-16 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32b5ca86-ec8f-3aab-9d6f-0206c57c6b42 | -6.62534 | -60.00858 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25f1206f-df36-31ca-9279-0acaa6ca0c1f | -9.36418 | -47.98146 | 2025-08-16 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb31edab-1276-3873-8d5f-672740ed4f43 | -7.56332 | -61.42864 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5960eb00-442e-3c38-96fe-6acd5c7a380f | -9.60597 | -63.46599 | 2025-08-16 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72c5b019-3b28-3f0b-bdc9-fb481bf03dab | -8.98627 | -60.52452 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9fc49cf3-da71-3bd0-bfa7-866a1666734b | -3.8289 | -47.74407 | 2025-08-16 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e3ec5f7c-71af-3f5b-82ea-a182b8850c4c | -9.18601 | -59.65562 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d0f35eb-98d8-3592-840a-56ab987eed5d | -8.98301 | -60.54561 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b695ce3f-be92-346c-be62-2dab34390370 | -6.94424 | -59.54831 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b7d7d2f-68f6-3e82-856c-a021048153e1 | -8.98287 | -60.50235 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 4d9c80e8-df5a-3377-b29e-767cbc1d4468 | -6.94925 | -59.53808 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bdde904-132c-3c8c-a048-9260e4ceaf64 | -7.52619 | -61.31963 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fab8a9a3-dcef-3151-a79c-41a7388184a0 | -8.11225 | -61.2036 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25524bc1-75a2-3b35-ace3-8f6a1cddc0ad | -9.50134 | -60.53301 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2b0a83e-09dc-30e7-8c8b-08968078a2f8 | -9.00228 | -60.509 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa86cb32-b0a0-31dd-8b1b-b3218f2629da | -9.01537 | -61.23394 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b94ec535-6415-3721-be0c-a677843bed9e | -6.95144 | -59.52379 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97166f42-6dbf-3b61-b862-8ab609055a0a | -6.94643 | -59.534 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 58ac10da-a3b2-3672-b49e-8fc0a496a484 | -9.06085 | -58.94244 | 2025-08-16 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 63002fb3-6286-3467-a0d5-3d33e65cee0f | -10.42934 | -60.28565 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21df6231-8564-33d8-9578-5add4e2f5ee8 | -8.89502 | -60.74012 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 38cc4ce5-9b16-37b2-83ea-262db61cd848 | -7.91463 | -70.22296 | 2025-08-16 05:23:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e40c57a-4c33-365e-8f0f-faf859f1bd08 | -7.56718 | -61.42569 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 694f95c5-863c-398b-b571-a702161a927a | -6.87513 | -59.84282 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e156cee1-c197-3b45-a113-7aeb557a773a | -7.62944 | -63.32637 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90bf6faf-9ab7-362a-beb4-f2a7bfa15939 | -6.9537 | -59.53145 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0036d655-85fd-3e6d-bcaf-77928eec0647 | -7.43437 | -60.03034 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecc51eb1-0d04-39c9-8a30-989029b61676 | -9.16593 | -59.64485 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d75710f9-1eeb-3bb2-a640-8d1e2b5970e1 | -8.99617 | -60.50443 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a93cc5f-3c17-3905-9411-446bada247f6 | -6.94126 | -59.65725 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78fbb973-6fe5-33fe-baba-2aa563ce2a23 | -7.68174 | -63.31116 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 229ceb5e-06e8-3469-ab87-0158b12e614b | -7.52673 | -61.31617 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4503be80-1367-33c4-be3b-25b0cf516522 | -9.85027 | -62.21981 | 2025-08-16 05:23:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7336de76-e95a-3f82-a01a-70a82b3a2afe | -7.4578 | -60.40697 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbd1a9fb-4ed9-35af-a012-3065e1dc325e | -6.48115 | -62.93436 | 2025-08-16 05:23:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 701fdafc-b860-3428-86b6-39f2c09d2fa3 | -7.67703 | -63.31827 | 2025-08-16 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a0876f1-cbcd-319a-871c-dda257af43de | -7.49311 | -63.82563 | 2025-08-16 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e812897-5dbb-3921-a341-f0f40be87c68 | -10.96526 | -49.57118 | 2025-08-16 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 06dc8d5f-063d-3833-986d-988f09bf8d91 | -9.50079 | -60.53655 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95c36a71-f20c-3bae-a665-f1898019b870 | -7.52343 | -61.31565 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b706b47f-d243-316c-9187-2a960bcae175 | -9.0018 | -60.53416 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 26656bab-d924-3423-8d88-d59de670d16b | -10.01399 | -59.22346 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3595c2f9-a636-3e70-9fa5-7ec645623603 | -10.92985 | -56.84778 | 2025-08-16 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fffcd269-77e2-3ef5-b9fa-17e9031ea32a | -9.20576 | -59.63978 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bf2ed76-819f-35df-b30d-d4607259d390 | -8.10174 | -61.18418 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d0f7dc9-78eb-3cd0-8a7b-d7f04fbe1769 | -7.53615 | -61.34254 | 2025-08-16 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 557c1839-0fa0-35aa-bdaa-aa147d5496b8 | -9.3525 | -50.25505 | 2025-08-16 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7aec9f8d-806f-3130-981b-55802308e2b9 | -6.93565 | -59.6491 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 830f005e-bb0a-32aa-9232-d8138abc7146 | -6.63144 | -60.01313 | 2025-08-16 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2413036e-fbd8-3c70-a003-59501ac81803 | -7.43878 | -60.02384 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 834cf8e6-d0e7-3e21-b21c-4abe08238755 | -6.95151 | -59.54573 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 747d9993-38b3-3c43-b040-7d0d9a72e0c4 | -8.97851 | -61.70924 | 2025-08-16 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 30.1 |
| ad5431d4-bf29-3761-a94d-42923d0eed1f | -8.98247 | -60.54912 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1a894c39-4769-3975-8957-b2083cb85320 | -10.01457 | -58.42601 | 2025-08-16 05:23:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3200b7a-4001-355f-bc48-99090435074c | -4.22881 | -47.2145 | 2025-08-16 05:23:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f27ef492-5fef-3f65-9706-05b039493229 | -8.99461 | -60.53663 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0bb91c1f-76f1-30fd-85a6-70cc17eedfa2 | -8.99793 | -60.53716 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| babcde20-3224-38f1-8f4c-ec905989139c | -6.9548 | -59.52431 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a1d05e8-d503-398f-b9bd-0ad68884a067 | -8.81245 | -52.04399 | 2025-08-16 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66a63cd6-deae-3165-bd5b-6270331762b8 | -10.00256 | -59.95918 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 053c1565-68f9-3650-8955-1f3ed50a1306 | -9.17701 | -59.66924 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c683e6c0-0a45-3ad5-ae15-908b9d9e31f7 | -7.4432 | -60.0173 | 2025-08-16 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc77be1e-d652-3da0-8ce6-5add7c15af30 | -8.98843 | -60.51044 | 2025-08-16 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cb9414b9-596f-31c0-a4bd-55b0fae192ac | -9.30091 | -64.54929 | 2025-08-16 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8abc2ebc-9860-3829-95b1-42d4ddd3edc3 | -10.04395 | -59.11684 | 2025-08-16 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README56.md)
