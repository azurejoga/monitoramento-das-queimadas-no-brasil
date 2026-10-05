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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ffc1432-1154-3ac2-a2e2-740cea89062a | -11.2242 | -44.2888 | 2026-10-05 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 717c5e73-6ff0-3a65-9757-495e7411a47f | -9.7687 | -44.8082 | 2026-10-05 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 76bb9925-8b44-326d-a7a4-d2f2237890dc | -11.1962 | -44.8037 | 2026-10-05 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 389f72c8-cea1-3274-8ced-aa78502de441 | 1.978 | -60.6099 | 2026-10-05 14:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 487.2 |
| 65d48fe9-e531-3a4e-8392-09a3c3a79416 | -10.9762 | -45.4094 | 2026-10-05 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 4a049877-098c-3dd0-9708-fc017f609027 | -12.8509 | -39.9352 | 2026-10-05 14:20:00 | GOES-19 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 120.3 |
| cb0f2891-1d14-3cea-a997-c84501340cd4 | -7.4889 | -42.8059 | 2026-10-05 14:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 2464a628-eaf1-3136-8373-c6860a43d9f9 | -10.7493 | -45.3024 | 2026-10-05 14:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 3fa5cfc4-5b20-34f6-92a3-497c5d16629a | 0.4465 | -60.5442 | 2026-10-05 14:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 562ff5d7-a7a0-34e5-b2ed-564856d0d48a | -9.1334 | -65.9 | 2026-10-05 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 623d105f-71ea-37a1-82ce-865f27862025 | -10.9575 | -45.389 | 2026-10-05 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c67aeaca-32cd-3ba5-9777-a526f2488a5c | -9.1613 | -68.2568 | 2026-10-05 14:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 7b646195-6681-3425-b115-1edad94870b0 | -7.8358 | -45.2948 | 2026-10-05 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 33161f94-79bf-3ac6-9799-b384190b82ff | -8.7526 | -64.1909 | 2026-10-05 14:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 1a8e5631-ad4f-3799-9f73-5626e40f2cee | 1.978 | -60.6099 | 2026-10-05 14:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 462.7 |
| bcd744ca-2cb6-39fa-bf1a-0668d3cf17b5 | -9.8246 | -65.016 | 2026-10-05 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| b133ed56-761d-387d-a80f-fef6b4c406bb | -9.1612 | -68.2752 | 2026-10-05 14:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 29e68fa0-f42d-3ec1-9d89-5d0630d070fc | -7.8356 | -45.3175 | 2026-10-05 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 937371b8-4d9f-3a5e-84e4-d4c852a1b124 | -10.9567 | -45.4349 | 2026-10-05 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 203.0 |
| 2661df57-f5fe-3b3c-ac10-9f75da7d5929 | -11.8315 | -43.5391 | 2026-10-05 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| ae9768d6-a778-3340-9889-f689810cd2f3 | -10.9762 | -45.4094 | 2026-10-05 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 454d6c5e-c390-3e81-93fb-12335a6d956f | -7.7208 | -45.4872 | 2026-10-05 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 83f8985a-bca6-322d-8947-74b1ee847bf0 | -11.4503 | -43.4091 | 2026-10-05 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 2c514ee6-62a2-3cad-be9c-f414b9268186 | 0.4465 | -60.5442 | 2026-10-05 14:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 150.3 |
| d38006ec-ebfa-3dfd-bd2c-f23c20e99757 | 3.8214 | -60.9982 | 2026-10-05 14:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| e13abca2-e7a8-3d3f-bed1-64b78d45765c | -10.303 | -44.648 | 2026-10-05 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| dd1a5ea1-7548-335b-b27b-98e44bb015dc | -10.9571 | -45.412 | 2026-10-05 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| ed973d6c-7eff-3bdb-8595-404231e1d10b | -9.1334 | -65.9 | 2026-10-05 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 862b998e-2a78-3b35-9829-5a82700c5b50 | -11.6951 | -43.655 | 2026-10-05 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| ee3c7288-44fb-3e9a-b572-cdf938dc8c4b | -6.9143 | -43.6583 | 2026-10-05 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 08db9e3c-f4ea-3017-8a77-74f6a6932414 | -11.7174 | -43.4861 | 2026-10-05 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| d0163f99-2063-3cf5-bf02-c57888f5b5e0 | 0.4465 | -60.5252 | 2026-10-05 14:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 158.8 |
| 62da9c85-a39e-39ed-8135-184f076eb939 | -11.8123 | -43.5422 | 2026-10-05 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 5966e994-6707-34fb-8acd-e73913aa447c | -9.393 | -65.8918 | 2026-10-05 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 597d5903-b32d-32fc-a3e9-98cc3af3f4b6 | -3.7925 | -42.9489 | 2026-10-05 14:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| c67e4af6-133e-3ea9-921d-1c2194f7a370 | -9.393 | -65.8918 | 2026-10-05 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 29613274-5f03-3d67-84db-1abf519f59b3 | -11.4503 | -43.4091 | 2026-10-05 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| c01efe58-d499-3829-a9a9-f9ac5d9acfa6 | -10.9575 | -45.389 | 2026-10-05 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| b8a6c1b3-e51d-3b66-b042-f3203affbb6e | 0.4465 | -60.5252 | 2026-10-05 14:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 189.9 |
| 2a4dba5e-a963-3016-90ca-a67208e127ef | -9.1334 | -65.9 | 2026-10-05 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 904324ae-606f-31c7-9e58-4d5654d78b7e | -9.1613 | -68.2568 | 2026-10-05 14:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 29e63f76-d7e1-355d-9b8e-96064653413c | -9.8246 | -65.016 | 2026-10-05 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| f82033fe-430c-3983-9b4f-3c0de9d5ca85 | 1.978 | -60.6099 | 2026-10-05 14:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 724.1 |
| ccf4f6ec-ce45-39f3-a4b8-02c4930c0ce2 | -6.9328 | -43.6799 | 2026-10-05 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 53124067-79be-384d-b4d1-4c961b3941ec | -13.5007 | -61.1333 | 2026-10-05 14:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 25fc27cb-45e4-356e-84bb-3ab56e17acc1 | -9.4116 | -65.8912 | 2026-10-05 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| b7c68d4f-f969-3266-9711-23ef9bc57d33 | -9.9175 | -65.0313 | 2026-10-05 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| d8a26e1c-653a-3679-bb0a-1f082a4998c2 | -9.8071 | -44.7804 | 2026-10-05 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 9118a846-efa5-3d66-9a33-c289a357b573 | -7.8356 | -45.3175 | 2026-10-05 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 513d0d63-f6c3-3728-8af1-2b2723c84750 | -11.8123 | -43.5422 | 2026-10-05 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 625ec67b-0d15-3750-879b-df80dd7e6454 | -8.3397 | -44.1658 | 2026-10-05 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| e3d25802-8c48-3437-9645-7819c4d6cea3 | -8.7526 | -64.1909 | 2026-10-05 14:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 143ee3f2-00fd-3b92-b400-979ace1e5036 | -4.3837 | -43.9154 | 2026-10-05 14:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| d924cfd4-a2fd-3dc8-9565-be8e5173aa22 | -1.4487 | -48.9313 | 2026-10-05 14:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 78d4a26f-2eb6-37d6-98fc-de97b32801ed | -7.8358 | -45.2948 | 2026-10-05 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 7a16d45c-233f-3348-a8b8-4458d668a4e2 | -11.8315 | -43.5391 | 2026-10-05 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 9a4a5c5c-4d5c-360f-9bed-895f29864ee8 | -13.5197 | -61.1319 | 2026-10-05 14:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 81dc0986-5dfe-331d-a136-c14b6c018e89 | -13.5199 | -61.1124 | 2026-10-05 14:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 1c19283e-c59a-394f-aae6-d0257171802f | -9.0059 | -65.4186 | 2026-10-05 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 16bef705-cfd8-3535-ac11-1440c7c19f17 | -9.4751 | -64.3336 | 2026-10-05 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 244b7dd1-e071-3409-b285-8f32e05a876b | -9.1334 | -65.9 | 2026-10-05 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 6b67daa8-2d04-30e6-82fa-c9001d55f25c | -9.9175 | -65.0313 | 2026-10-05 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 5712e09a-3f30-3163-88bd-d70fc1d213a4 | -9.8246 | -65.016 | 2026-10-05 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| d4ef34a4-97b9-3f17-908a-29d9456407e5 | -13.5197 | -61.1319 | 2026-10-05 14:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 3572e4c2-3740-31d5-a0d8-aea771e11c3f | 0.4465 | -60.5252 | 2026-10-05 14:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 153.1 |
| a09a90c5-3c9d-3154-bb8a-dd0013f2a96e | -9.4565 | -64.3344 | 2026-10-05 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 4323d7c1-6cfe-3660-a3e5-1f0e757b80e4 | -13.5007 | -61.1333 | 2026-10-05 14:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 7a91aa9e-7966-375d-ade5-6cfb1729cd6a | -9.1222 | -64.3843 | 2026-10-05 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 2334a22e-93e0-34d5-bf08-901728d3b03a | -9.1335 | -65.8813 | 2026-10-05 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| b5459ce5-570c-37a7-b3bb-75def755b0a9 | -9.393 | -65.8918 | 2026-10-05 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 5dc29700-e155-3687-b57e-5c1971a9483d | -13.5008 | -61.1137 | 2026-10-05 14:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 0ef6c5df-d04b-39a2-abb2-deca197dc7e7 | -9.0244 | -65.4181 | 2026-10-05 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| d843e2c3-24d7-3892-b154-9b7b752fb238 | -9.0987 | -65.3783 | 2026-10-05 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| b0876f52-6fee-36a2-89f8-db7688424687 | -9.0988 | -65.3596 | 2026-10-05 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| cc672e1e-7536-339b-a200-6aec842b275c | -9.4116 | -65.8912 | 2026-10-05 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 1b9c3f76-e0b1-35a7-bf2b-e714f1f360b7 | -9.0046 | -65.6988 | 2026-10-05 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 011865d1-beb4-37ba-9102-beb1993d0856 | -9.1174 | -65.359 | 2026-10-05 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 8f9bc771-034c-38c0-9387-83eb1ca70d40 | -8.7526 | -64.1909 | 2026-10-05 14:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 89fff5fc-e4c8-3a17-ae11-5bab2eba89f3 | -9.043 | -65.4175 | 2026-10-05 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 3a63c5d9-8daf-3d32-b3e7-b63f18d8189d | -8.593 | -66.8081 | 2026-10-05 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 894fbbfa-ac37-35bb-94eb-0840ab040623 | -9.1445 | -67.7577 | 2026-10-05 15:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| db027f95-900e-338d-9fcf-e201070da245 | -9.4565 | -64.3344 | 2026-10-05 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 7ff1861c-3184-30f7-b8cd-d32620bb15c6 | -9.4751 | -64.3336 | 2026-10-05 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 4fd9b492-ef90-39e0-905c-7713a7f1a7c1 | -9.043 | -65.4175 | 2026-10-05 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 99a6a94f-5e47-3444-97a5-5240583915ca | -1.3927 | -49.2727 | 2026-10-05 15:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 383fa1b2-1986-3ad0-a8f3-d90f35144dc5 | -9.1222 | -64.3843 | 2026-10-05 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.2 |
| f064a037-dfc0-3f97-8fd3-3166028f9def | -9.9175 | -65.0313 | 2026-10-05 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| ec70d880-4651-38ad-936c-19c97836ab88 | -9.0244 | -65.4181 | 2026-10-05 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 31e0aa6e-fe9c-3b54-ad42-889be0c5e1b1 | -1.6396 | -55.1319 | 2026-10-05 15:00:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 4d7f2ebd-de6b-3b9a-9f82-881a7caa2dec | -9.0046 | -65.6988 | 2026-10-05 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| e469832d-8684-370e-ad27-0a9838484514 | -13.5199 | -61.1124 | 2026-10-05 15:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 7b300cbf-3d25-3f47-901d-39141aaeaa0d | -9.393 | -65.8918 | 2026-10-05 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 1686d3b1-ca65-348f-ad04-1f9dc92ed8c1 | -9.1174 | -65.359 | 2026-10-05 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 483a6281-c29c-3d76-9d0f-9e589227e4e4 | -9.1259 | -67.7581 | 2026-10-05 15:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| d1d9cc1f-684c-3df6-8173-123785c8e9dc | -9.1535 | -65.5634 | 2026-10-05 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| cac4fdab-c208-302f-ad24-e70ed1e8a857 | -9.0059 | -65.4186 | 2026-10-05 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| f4879c3d-5330-3e04-9413-651d7a0ff23a | -9.8246 | -65.016 | 2026-10-05 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 40715d64-15c5-386c-b403-0a1b203c9b9e | -7.1778 | -42.0055 | 2026-10-05 15:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| 08eb03f1-3423-341d-95ab-18087cff6fbd | -9.1335 | -65.8813 | 2026-10-05 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| e13edd76-fac6-3dc2-983a-3a46f73e31d1 | -1.1094 | -54.1401 | 2026-10-05 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |


[Clique aqui para ver as próximas entradas](README66.md)
