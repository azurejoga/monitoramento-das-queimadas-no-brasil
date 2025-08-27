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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdbc1e70-f1f3-3bbd-8be5-dfaf1638b488 | -8.34237 | -62.93675 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27cede63-0a82-3048-a6bb-0e675135234e | -10.26943 | -64.50328 | 2025-08-27 06:08:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3cddd6af-1546-3aab-be36-b4114728ba08 | -8.85123 | -62.44384 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8c5362f-da02-31cd-b73f-6d401619e845 | -8.07678 | -61.53822 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3e4130e-9185-39f1-97a6-1cf02775befe | -9.18031 | -59.51328 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d466d5ed-7c7c-31e0-876f-bf3d9365a5ea | -8.91501 | -65.9203 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f6bd714-b24b-36f4-b70d-cfd21e45ee0a | -9.0222 | -65.7286 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ec90bf5-cbf2-3f41-99aa-4a8e404c5d46 | -8.07093 | -61.53742 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85f89a42-097e-306b-8613-64718989b7dc | -9.16309 | -59.54127 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ecdcac3-2bea-3e34-89a6-7677bfe62f2f | -9.40116 | -60.53762 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0032e137-6beb-30c4-8d3a-be9c7f20653f | -8.96167 | -65.97074 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| cff86aac-16bf-3954-b037-aa3dbae350f5 | -9.02607 | -65.73357 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 826ed9f4-8d92-32b5-9b15-5443ff0f3d04 | -10.04002 | -67.53251 | 2025-08-27 06:08:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a10c72f1-d6a0-3b1b-ba77-10c508636491 | -8.34282 | -62.93336 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faa0c592-7f59-3c98-acd5-0c64c51c9675 | -9.19374 | -60.80734 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aee85e36-9141-3861-888b-8f9584110bc2 | -8.93202 | -65.9271 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d7fcd523-9bf7-33ee-9999-d6e5789e92bd | -7.54651 | -63.84066 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7386e2f-19c5-3233-bf06-77a36d6d6f5a | -8.95666 | -65.97441 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 17037f75-220f-32e9-9b37-00aaefc3b06e | -8.10959 | -71.25026 | 2025-08-27 06:08:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e908d67-3627-3eb1-a405-ec20b0f1c814 | -8.5043 | -69.79884 | 2025-08-27 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1967d8cf-dbbc-375a-9d8c-dac20c11ee4f | -7.66346 | -62.54632 | 2025-08-27 06:08:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c16b8fdd-928e-38f7-a67c-4e24b3a18a4b | -9.39864 | -60.50581 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b24cbe0a-0142-3a06-a7e4-6d91e5f12de1 | -8.50082 | -69.79831 | 2025-08-27 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb24821a-b8bd-38d5-8e82-2913dfc76365 | -9.40499 | -60.50669 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3f8dd742-2168-36f3-8d8e-a8c6c8fded96 | -8.06933 | -61.54982 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e338c601-9d85-3711-b85f-bcf79bce81ef | -8.89121 | -62.47505 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 620c7f26-ceff-3b7c-af4a-e70ddd80de23 | -9.41006 | -60.51785 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| db831f60-f0ca-34ab-9f38-c59929d4e091 | -7.37872 | -64.36079 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d98732a6-451a-30ee-8b05-921dce31bc9f | -10.0877 | -62.90252 | 2025-08-27 06:08:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b76c7f55-a80a-3c73-9526-2dfc1271a1f8 | -9.69627 | -65.71873 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3625b55-cecf-3ed2-9edc-ad272a90ab78 | -9.62009 | -62.26435 | 2025-08-27 06:08:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fa1f5c2-2c88-3ca2-a136-eef174b9d964 | -9.18751 | -60.80656 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7a26458e-ddf0-3f3b-b351-d79c791312bc | -8.96066 | -65.94756 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 97402c50-6c0a-3225-a527-2123254990d2 | -9.15265 | -60.78188 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b097f40-be00-3bfc-a53c-2a9a61ef6408 | -8.96229 | -65.96641 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ad1350d3-f7f3-3d17-b219-3a3bb5f8b451 | -10.09411 | -62.89632 | 2025-08-27 06:08:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fde65b2c-8add-395d-879b-51c22a0ebda1 | -9.22957 | -60.9201 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6acefe64-3c7b-3d5f-9c29-30da27064e61 | -9.64479 | -64.98921 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24d4a806-3033-3d95-a58c-12eee4b34c77 | -9.61959 | -62.2682 | 2025-08-27 06:08:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42df0ec7-e78e-3dce-8b63-006453f1e451 | -9.1568 | -59.56371 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5dfc0afc-32bc-3323-a995-60b26abfbc33 | -8.88789 | -60.76339 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d4eac3b5-a366-34fb-a37e-b5034a54e5a9 | -7.40007 | -64.34788 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3f73914-de62-3b81-9dd3-26687081078d | -8.61044 | -62.65145 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35bc9114-7fb8-3953-8fd9-35e5740f16b6 | -9.06545 | -66.06544 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 81288cb6-3bea-3c14-bbfc-cbb80ed92bc1 | -8.85632 | -62.44831 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54659d3c-cb92-3ac3-9902-6fbbf1ab9c55 | -9.16256 | -59.51551 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63cc9778-5733-365b-919c-7207a811d763 | -9.4088 | -60.52805 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5edad84a-d7a4-38d9-a7cc-1756d3bc3352 | -9.18728 | -59.53719 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4ba4fe6a-770d-31d7-803c-4c573e05ce3b | -8.85025 | -62.45129 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7efb46e-3be3-3513-8c4b-77eb556705f1 | -8.93716 | -65.9541 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9039ea18-eed5-3116-ba5e-71597062a9d0 | -8.89969 | -60.76989 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f81dd4b-82ed-35bc-967b-7bbd5a2fe92e | -8.91441 | -65.92456 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1f6b7c0-397c-3fe1-a129-b365b4bf69c1 | -9.15203 | -60.7868 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c64a1568-433e-3f53-9cfa-2eb913316c5b | -9.41955 | -60.54524 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67aea423-7bd1-39f9-a22c-d44f29a20360 | -9.79518 | -64.26961 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6029360-20fa-332c-816f-42be26ad6b62 | -9.8286 | -64.2858 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f174497-bc3a-3f14-ba3e-14aa4bbd7268 | -8.95728 | -65.97011 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 91308abc-fa94-3552-a98b-ef00dc8c99e6 | -8.94155 | -65.95475 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 8c3b3cc3-5e5c-3e2d-aa04-c6a78d8a1f10 | -9.16669 | -59.5667 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 49e146d9-5cfe-3559-a85c-0574654ac69b | -7.46846 | -61.40077 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99e78df0-4463-300f-a514-92968ce64d0a | -9.16233 | -59.54728 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a82e0dac-5ec8-3298-9871-671f1e68165e | -8.91942 | -65.92093 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7642728-b103-39a4-9a2d-988f6d611550 | -8.9948 | -65.4145 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57fcbe19-795b-3b52-9134-77992b9c3608 | -12.22311 | -64.23163 | 2025-08-27 06:08:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40017fe0-9b75-3cf9-b69e-918ca3f9f4fd | -8.92262 | -65.93008 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5ea7a8e4-8295-3830-b141-b38a809fb30f | -7.47936 | -61.36353 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6cc2662-1369-3ddb-a078-4972cbea63f4 | -9.16613 | -59.51727 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c325a5a-fb16-3599-8790-b47fe75432ff | -8.92382 | -65.92156 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a4a19fbf-1797-3388-b163-6d46ea5cd273 | -8.93581 | -65.93204 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 450faace-1aa6-3558-8400-406da7d87767 | -8.08386 | -69.90957 | 2025-08-27 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a728e58-6746-31a6-9a53-6ddaee92a2ac | -8.95657 | -65.94379 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2ef8fd6b-e905-3494-8212-8615012b71af | -9.66918 | -67.50779 | 2025-08-27 06:08:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ace7a390-6ede-3939-88d3-adf36b28fb7a | -8.95473 | -65.95663 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| f4bf6e76-e443-3268-a54c-ced9490443b2 | -7.53991 | -63.85754 | 2025-08-27 06:08:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 537f57f8-f70a-358f-911a-82eab0af32e8 | -9.41706 | -60.51353 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5fbc4573-cb9f-36d4-b323-953b01ded992 | -9.02668 | -65.72916 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| affed46d-37fe-3e3e-98ba-27e4b3cdf6fd | -9.40816 | -60.5332 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 81869cdc-a0c0-3cd7-8c66-da7ed52e8ff4 | -9.02325 | -65.68768 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89deed05-f4ba-32ec-b36f-d07c887998ab | -9.07476 | -66.06252 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f333f3db-3499-3fdc-bc2a-d1d71228f32f | -8.3538 | -70.84097 | 2025-08-27 06:08:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ce3d9fa-6cf2-3408-8ac4-8ad6fd05bc9f | -8.35044 | -70.84045 | 2025-08-27 06:08:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ad1317c-d6e5-3932-912d-ab70d1cae6a8 | -9.63757 | -59.63737 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0945030-440f-381a-9042-8379b92413fb | -8.8573 | -62.44085 | 2025-08-27 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e9cda63-936f-36b6-bd6b-4a045608369a | -8.89284 | -60.76094 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a6d4336-9aeb-3604-954a-c1b0b7a97d9d | -7.74121 | -61.08252 | 2025-08-27 06:08:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62146faa-185b-39f5-9ade-49c53c0f592d | -12.22351 | -64.22843 | 2025-08-27 06:08:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7a443e4-64d5-313a-a179-3ba6345ba244 | -9.67017 | -67.50082 | 2025-08-27 06:08:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d86257b-6f24-3d6f-8f52-0658abedba52 | -9.64953 | -64.98988 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e320e720-8664-3d82-ba33-4488d313e59a | -9.16699 | -60.7686 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d59d0d15-fcbc-3edc-8802-5d9d4e1b4453 | -9.16904 | -59.54822 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7c219e7-52ba-377c-9a3c-3a539ce5e2ac | -8.33567 | -62.94614 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b2c4c52-0341-3bca-aff9-e7b6166e96ef | -9.6068 | -64.44956 | 2025-08-27 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b89e95c-d32c-3cb4-a74e-b75f24f1cbee | -8.9296 | -65.94421 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| a28e4522-40b7-376e-85d4-77b61806d309 | -8.07571 | -61.54654 | 2025-08-27 06:08:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f88147f-8295-3dbc-b264-4f68cc7c0cab | -9.41319 | -60.54453 | 2025-08-27 06:08:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b2b0bf46-d42f-348e-813a-95b8e9534d8c | -10.27933 | -64.50466 | 2025-08-27 06:08:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e8902a50-0907-3e66-83c5-e8ba68471d5e | -8.8941 | -60.76423 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce1a8490-7cd3-35d9-a3d6-c044ec08fdd0 | -8.89727 | -60.77631 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a4fdbb9-1c17-34c7-86e3-97e42a8f12e4 | -9.01752 | -65.69614 | 2025-08-27 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6927448d-823e-3e1b-a31e-2ff588062899 | -9.18327 | -59.45696 | 2025-08-27 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README85.md)
