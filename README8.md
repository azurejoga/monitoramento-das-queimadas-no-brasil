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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 199cfafd-18bf-3e82-b574-b459d37fedef | -13.0122 | -42.3321 | 2025-08-17 02:40:00 | GOES-19 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 6bc2c0c2-8b00-3aea-a591-df9ec19b022a | -6.545 | -43.0373 | 2025-08-17 02:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| c13c79c7-9d92-3e4f-9857-6d5029872deb | -10.844 | -45.3356 | 2025-08-17 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 6cc9528f-0752-392f-9a73-36c6c9e1c806 | -9.518 | -60.5268 | 2025-08-17 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| e7125c45-1638-36ff-afe7-2920d7318aa8 | -7.9252 | -63.2608 | 2025-08-17 02:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 6795a61a-424f-3efc-89b0-7884a76865f3 | -8.9788 | -60.4964 | 2025-08-17 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| c834e471-ea28-32b2-a893-b93536e62e43 | -9.5179 | -60.5461 | 2025-08-17 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| a3ab3a42-9313-35b5-8818-e6c2e8ae8e29 | -10.8249 | -45.3382 | 2025-08-17 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| e6f9dc02-82b7-3ba7-b64f-9bb817d6d167 | -10.8249 | -45.3382 | 2025-08-17 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 8f5fbef1-543a-36d9-8e0d-5d81fd2e30f6 | -8.9788 | -60.4964 | 2025-08-17 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 99b7de57-6e2e-3c93-9ba6-58508a1f07ec | -9.4992 | -60.547 | 2025-08-17 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| caf8de65-aa03-3132-9882-d994b13bcc13 | -10.8436 | -45.3586 | 2025-08-17 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 251ba3d1-f508-3ec9-badf-0dc35e1233b0 | -10.844 | -45.3356 | 2025-08-17 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 181.4 |
| f472195b-1100-3505-8f3e-0cebeb2b8f4e | -14.9251 | -54.6774 | 2025-08-17 02:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 640b4fbd-a61a-3d15-b52d-43362c1732f5 | -10.8246 | -45.3611 | 2025-08-17 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 1cee2808-76dc-30bc-a986-b37cc5ed9613 | -9.518 | -60.5268 | 2025-08-17 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| fc8d78f8-5184-32ce-9fc5-e35c14c3f5d4 | -9.5179 | -60.5461 | 2025-08-17 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 299984ed-2ef1-3dde-b577-a016009c7fe2 | -9.4994 | -60.5278 | 2025-08-17 02:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| aef16341-4ab9-36b1-a7d7-9e1c0b45c5c6 | -4.9118 | -43.257 | 2025-08-17 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 481151f7-2de6-3c16-bda2-f2c271786ab3 | -7.9252 | -63.2608 | 2025-08-17 03:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 107f9a2b-ee94-349f-ad2a-865cacb886d8 | -9.518 | -60.5268 | 2025-08-17 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| b7260ebc-315a-33d7-ab58-b5a48f1dee77 | -7.9436 | -63.279 | 2025-08-17 03:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b4fe832e-a98a-3e24-a2f6-472748930c15 | -8.9709 | -61.6842 | 2025-08-17 03:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 285e04a1-63c9-34eb-9222-327f17322204 | -7.9437 | -63.2602 | 2025-08-17 03:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| c9cb8408-6c3f-35d1-8fc2-7acce32eba2a | -10.8249 | -45.3382 | 2025-08-17 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 1e916328-d519-3209-8e98-ed8a201c9798 | -7.9251 | -63.2796 | 2025-08-17 03:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 5e09fc65-f1f1-3ebf-bd20-45d13cfc6c3c | -12.898 | -46.1135 | 2025-08-17 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 6daa9c6e-ad1b-37c4-94be-763f0e2dd36e | -8.9893 | -61.7024 | 2025-08-17 03:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 9c5c76fb-2ca8-3224-8692-1e854df0b942 | -10.844 | -45.3356 | 2025-08-17 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 2e78eb91-4715-3b19-b62d-a4a0d83efc52 | -9.5179 | -60.5461 | 2025-08-17 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| b68533a9-f6d5-3798-ab28-c5a91fece5e5 | -8.9974 | -60.4955 | 2025-08-17 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 85c9b37d-31d5-37d6-a2e5-ae95f9a31797 | -8.9788 | -60.4964 | 2025-08-17 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| f36896e3-cfdd-347d-b44c-92378de71397 | -4.9118 | -43.257 | 2025-08-17 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| c0e5ae8a-ce9b-38e4-afe2-ab083c107bc8 | -8.9788 | -60.4964 | 2025-08-17 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| cb79bd2c-2d27-3ced-9640-b0e2921b4758 | -10.8246 | -45.3611 | 2025-08-17 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 3c996492-c35b-3793-88e7-c74b4b7dfe71 | -10.8631 | -45.333 | 2025-08-17 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| e014e986-da53-38ef-8449-f1556a722600 | -9.518 | -60.5268 | 2025-08-17 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| f23e3496-28b5-3273-b52d-f1b482f22339 | -10.8436 | -45.3586 | 2025-08-17 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 7828a4ab-5d03-38fd-aa9e-4d9c90dab22a | -10.844 | -45.3356 | 2025-08-17 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| ae00b7c0-6aa9-3519-afdd-0f71caa6197b | -10.8249 | -45.3382 | 2025-08-17 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| f02f01df-bfe0-358b-9354-f409aed6741a | -9.5179 | -60.5461 | 2025-08-17 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 15a30b86-c21e-3ff7-8171-68f94051f1a4 | -9.5179 | -60.5461 | 2025-08-17 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 154e0539-aaf9-3f1f-9bee-b7410e1c57e2 | -10.8436 | -45.3586 | 2025-08-17 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 6da2e27a-63e7-3448-9890-e65062de1ae4 | -4.9118 | -43.257 | 2025-08-17 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 4e9d5642-7623-3572-921c-1930fdf2df51 | -10.844 | -45.3356 | 2025-08-17 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 3ad2fe6f-e8fa-3ce6-9e42-ea700c2f10cc | -8.9788 | -60.4964 | 2025-08-17 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| e36f90f7-4eb0-3621-a2f3-7f86357cd79d | -9.518 | -60.5268 | 2025-08-17 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 5de58945-1130-31ed-96c2-e62d58be85ee | -10.8631 | -45.333 | 2025-08-17 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| fea604c2-141e-342d-9876-4e682ce34b31 | -3.97041 | -42.52975 | 2025-08-17 03:21:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| c0956290-44f8-3fc0-8688-c349cdfbf522 | -3.94514 | -41.83229 | 2025-08-17 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 1488ceaa-c282-3c7a-a341-835abc6d1add | -3.97798 | -42.52517 | 2025-08-17 03:21:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 6249b844-509b-3929-916b-19b801f54f6d | -3.977 | -42.53084 | 2025-08-17 03:21:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 6c622531-00ab-3457-a0d9-e2cfec222502 | -4.92122 | -43.24686 | 2025-08-17 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8614357f-b9d4-3395-86c0-6dab9a09445c | -8.53723 | -37.72147 | 2025-08-17 03:23:00 | NOAA-21 | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2e1c9821-bb5f-3ba7-9dec-678f1c563f88 | -7.24976 | -39.33334 | 2025-08-17 03:23:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 88a31572-d997-3c9a-80aa-dd8ee7ed8864 | -4.59923 | -43.32484 | 2025-08-17 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d3cde44a-5ee5-31d0-a7ff-f776364a0d3f | -7.53674 | -36.73053 | 2025-08-17 03:23:00 | NOAA-21 | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f7c1234b-c634-34d1-81ea-8d929fb08c0c | -8.75009 | -44.04131 | 2025-08-17 03:23:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 2ac13648-1535-3613-83b2-dc2c72c25881 | -4.60607 | -43.32598 | 2025-08-17 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c07c665a-c3a9-3ac5-abc3-f721e2a09d0b | -4.91699 | -43.25825 | 2025-08-17 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| e165d2ef-7482-3678-9b67-eb4ef0788578 | -4.92575 | -43.26019 | 2025-08-17 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 31ae182a-a23e-309c-9b2b-36628dcf2a93 | -8.50209 | -44.73619 | 2025-08-17 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 06b6fcdd-0d00-3751-80b8-f3457877bc37 | -8.50774 | -44.7443 | 2025-08-17 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d79c1ffd-fe2e-3cfd-9035-57d4ae9a31b3 | -4.92687 | -43.25411 | 2025-08-17 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 726cca72-fb77-394b-bc82-e86589e0d041 | -6.61983 | -43.88158 | 2025-08-17 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 8ece7c09-2faf-38a1-8160-72bc06f60a41 | -8.50088 | -44.73553 | 2025-08-17 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 60d2f4c1-bec3-3381-85c9-3d620bda7f54 | -8.7476 | -44.0362 | 2025-08-17 03:23:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 19694dc4-df64-3885-91fd-2e5a3a98f137 | -7.53249 | -36.72982 | 2025-08-17 03:23:00 | NOAA-21 | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7c9f5a79-cc9b-3b24-addf-32276f31779d | -8.74343 | -44.04002 | 2025-08-17 03:23:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eccd9118-abc2-3990-a4ff-a57ceab4bdbe | -8.50649 | -44.74359 | 2025-08-17 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0a97636b-4bd1-33fb-9050-006fc0f8455d | -8.50785 | -44.7368 | 2025-08-17 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1fe70772-8d7c-370c-89df-52eee72e158f | -6.61815 | -43.88651 | 2025-08-17 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5e06e6bf-5a81-3564-9b86-5f7d9781e870 | -8.50921 | -44.72999 | 2025-08-17 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| aa4e766e-d75d-3f59-9956-872d89e4b94b | -4.92012 | -43.25282 | 2025-08-17 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 0649fc35-ae77-306a-b7c9-e0085b451fe8 | -8.7464 | -44.04224 | 2025-08-17 03:23:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 1f0706ef-cfa7-3b1b-91cb-f6b8148dc1b1 | -9.61191 | -40.34715 | 2025-08-17 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 279cd53f-dfff-3e46-bed8-ff338b108ab1 | -8.50341 | -44.72936 | 2025-08-17 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 07434672-154b-3dad-89c5-843b0437450a | -7.14594 | -44.64453 | 2025-08-17 03:23:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac660310-377c-35c5-b25c-457098c562f8 | -4.92482 | -43.25346 | 2025-08-17 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| fe2c4915-ad16-382c-8a0e-f594229fb7f2 | -4.92374 | -43.25953 | 2025-08-17 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 48271f44-6566-30ec-9140-2af324a930c8 | -4.91807 | -43.25217 | 2025-08-17 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| e9906f2c-8073-3128-ac5e-873a99a31e8c | -4.60131 | -43.31912 | 2025-08-17 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d523c0c5-1f54-37ba-823b-c0a232f3f166 | -4.91901 | -43.25888 | 2025-08-17 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 18bb6d88-5f0a-332e-8e8d-d1380cc17550 | -4.59331 | -43.32436 | 2025-08-17 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf0b47c2-7778-335c-a49e-cc1e54feb161 | -4.607 | -43.32651 | 2025-08-17 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4608261e-755f-35e4-b514-b56140ab7bc8 | -7.14261 | -44.64468 | 2025-08-17 03:23:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3c52aaa9-f511-324a-a1b5-0d122de07b3f | -8.50906 | -44.73748 | 2025-08-17 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bbc9ab44-e7b2-3fe2-ae1a-abc9cb006559 | -8.51038 | -44.73065 | 2025-08-17 03:23:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9dcfbd0f-288d-3627-bee7-029e29cfa7ee | -7.13879 | -44.64357 | 2025-08-17 03:23:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c631dd2-d90d-3c77-946c-592d7104a62d | -4.60252 | -43.30616 | 2025-08-17 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 00f8ec5b-59ec-3b54-8744-d604ae381f56 | -4.60034 | -43.31857 | 2025-08-17 03:23:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 25896462-7ee2-3ffe-af65-edcca7446d5a | -6.61936 | -43.88002 | 2025-08-17 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8a411c52-f1a6-3bd5-80b5-7eff66bd3c61 | -10.83758 | -45.34022 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 02696454-2e0c-3573-a784-6bf732d432a1 | -15.24198 | -43.85504 | 2025-08-17 03:25:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 933bd8d2-4abf-3736-997f-3e1b299859f4 | -10.83695 | -45.33743 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f197ec7-acff-38b1-b57c-4be193d27bc7 | -10.83477 | -45.31861 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a321373-cf62-3965-8765-088c2196d067 | -10.83063 | -45.33892 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb9411b1-42c8-3b2c-aa5c-8be967723408 | -13.01219 | -42.32858 | 2025-08-17 03:25:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| bf0a988d-83d6-3eb6-b958-aeefcd6685d3 | -10.83612 | -45.31202 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8b1a5b4-8f7b-312c-a860-c1c4713de027 | -14.18291 | -45.32075 | 2025-08-17 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README9.md)
