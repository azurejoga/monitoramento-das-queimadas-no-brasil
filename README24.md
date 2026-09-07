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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5b06a90-841d-3ffc-9354-1ec40eaac425 | -8.51859 | -63.87283 | 2026-09-07 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0869b3bc-dc77-34e8-bcbf-de0def5e67c1 | -5.36494 | -56.02851 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d30004a-9538-3e49-b3aa-812aa4ba0670 | -13.30279 | -45.23703 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| af4e687b-dbe6-31a3-932d-cfda3d5acb03 | -11.04148 | -44.34394 | 2026-09-07 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef34ca88-93c5-3c7e-b0f8-6dd15fb3bcf8 | -5.29189 | -60.1251 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f362f0f2-b152-3ae4-8c96-3328f6579301 | -5.36574 | -56.04666 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b0e91e5-eb1c-3643-9d2b-b52df6efa0e0 | -9.72685 | -43.39887 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 76025cc5-f11a-3090-acda-a197afda5001 | -5.83007 | -49.1943 | 2026-09-07 05:04:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc982a30-1404-3288-9819-1803dbcd821c | -9.57455 | -40.35664 | 2026-09-07 05:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2c99b352-3c64-3f8f-b035-c8bf4ca1c21d | -3.77162 | -61.75998 | 2026-09-07 05:04:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 67023b30-107e-3dae-b672-a7fb98c871e1 | -6.13556 | -57.68611 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d28904e5-6fe5-3717-86df-bb7913c65816 | -4.29389 | -59.95845 | 2026-09-07 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21b4c2da-a5e3-317f-914e-2298292bdd69 | -9.57455 | -40.35836 | 2026-09-07 05:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 23d53938-2298-3e3a-8d18-974994473002 | -8.76045 | -62.42721 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ae00bfd-2836-383e-8d6b-c7b8d53277f7 | -5.83005 | -60.25386 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 95558fb4-1933-3bea-b1e2-b1f28b7f6fd1 | -8.75636 | -62.43291 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9482f691-7071-3dc8-8818-73d0fbece550 | -4.09845 | -60.66286 | 2026-09-07 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c619fb5b-b909-38ae-a548-553a1c36ac72 | -5.99959 | -57.70282 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35fa0336-d23c-3c2d-9386-6687b87d4000 | -11.50954 | -49.61284 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7797e0c9-6401-32e7-93a9-f3c15ceee2c9 | -5.34793 | -56.03917 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b5af834-f161-3304-b1a9-4b7d25d15bbf | -5.30065 | -60.13208 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8fddb7c7-e971-3791-99d3-166943122e7e | -6.05471 | -57.79442 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90da12cd-a440-3c68-a92e-9e1d55feb096 | -9.73679 | -43.41143 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f163f00e-6a19-3ae8-a2a7-c1a6948f1c6b | -11.52598 | -49.61704 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d25508a6-29b4-330a-969f-7231c61cdc5d | -7.10064 | -56.52042 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f641497-763c-3043-9e1f-583f5399cddb | -5.99672 | -57.69498 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1caef4c5-f4c8-3e7a-a7eb-7aedae752006 | -5.29394 | -60.14186 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6b2a88d-8e4f-3c81-b263-59dd4c1d0d7d | -6.86921 | -55.60191 | 2026-09-07 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 898f8699-5a8d-3f17-a131-dd195cae6100 | -5.99731 | -57.69146 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed68ace0-f1f3-3665-94af-88706e9efd0c | -5.99494 | -57.70567 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 97ef1ff6-1d61-3579-bf8b-26e6b70362c8 | -13.30729 | -45.24414 | 2026-09-07 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1722d2b7-f8c8-3721-965b-c463fb787f37 | -4.28718 | -59.96839 | 2026-09-07 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d64b88e8-3c8e-3993-ae99-4e0471ae9cb3 | -11.33706 | -45.09988 | 2026-09-07 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ae258545-d4af-39cb-9ec7-d0b74aeac7c1 | -4.5572 | -55.04025 | 2026-09-07 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e50fc05-6d6c-3f25-b4f1-3e228dbad6ee | -5.36719 | -56.03788 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0fc66cc-9158-3eaf-a98c-ba1d1809c767 | -5.14842 | -55.96035 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e4de693-b9e3-33dd-80ed-d0e0cdc2e559 | -6.14736 | -59.94154 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3700b162-ccde-3fba-9742-a27895eea722 | -5.35237 | -56.03542 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 837efd9b-2d4b-3184-83ad-1bb11018ef35 | -11.33787 | -45.09362 | 2026-09-07 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 95002754-ff62-3564-8568-1c418ff75f57 | -3.77099 | -61.76363 | 2026-09-07 05:04:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f710aa4c-6bcd-3fa5-b3fc-9d0289c07447 | -5.30848 | -60.14439 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c28a7512-76cf-3aa3-870c-3b97b6a9bc6e | -5.28953 | -60.12337 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3083c17c-9183-30ad-bc35-15fd5bb02c4b | -4.42871 | -55.09488 | 2026-09-07 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fea3888-75be-31ab-9c01-ec7644319e05 | -5.14769 | -55.96473 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a565ad8-e58d-330a-bac0-5de1bddd6f27 | -3.77796 | -58.85121 | 2026-09-07 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c0fc24c6-d0d3-39f7-b37b-7bd2bd779dbf | -5.14101 | -55.95916 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7116d845-cd69-35b6-8bb5-0d161e3151e6 | -10.37401 | -45.01711 | 2026-09-07 05:04:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db1c1e8d-7cf9-3a4d-9c5e-510be69bf7a1 | -5.98743 | -57.70058 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c854681-c7b0-32b0-a129-990e6e8a525c | -11.32557 | -45.06599 | 2026-09-07 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f7d0aa2-bddf-3a7c-875b-1e086e1dbce0 | -5.2958 | -60.13126 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f9f40a30-813b-38a1-b3da-556c5f034f5d | -8.53619 | -63.87629 | 2026-09-07 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abc2cbdd-afc9-36d1-9998-12ab8487bd42 | -3.38839 | -61.32916 | 2026-09-07 05:04:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 511be1ab-c8b0-314b-a363-d620af61f425 | -11.33238 | -45.09525 | 2026-09-07 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc76f51f-2e75-3482-b596-be7a1662eec7 | -6.06168 | -57.80288 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60ff6df7-cf9e-3eec-a3a6-0714cfa5c1c5 | -4.67922 | -55.63951 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53fc98c7-4069-3e05-ad22-2014bbe2ce93 | -8.54127 | -63.88166 | 2026-09-07 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7a45553-9fbf-3262-8320-95a85250b91a | -6.00019 | -57.69924 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25773ac6-d851-3885-a361-0f0b8d638d1a | -5.8264 | -49.19374 | 2026-09-07 05:04:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7da9e2b-f809-3b8d-a98c-eb4cb8f32d48 | -5.29936 | -55.86349 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7923fc55-ff44-3800-9702-a8dd5ba8b6bd | -4.34949 | -56.27953 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4cbed4b-1547-34f5-a010-54c62e54f1a7 | -5.30007 | -55.8592 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da875ef8-ab78-3a22-8ef5-c6ce979bf59a | -8.52872 | -63.8836 | 2026-09-07 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2527e5f0-5208-370b-9569-d250843d75fa | -8.75924 | -62.43388 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46311670-a541-35a1-9f92-e15a2acdf785 | -8.76697 | -62.42162 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7fe3058-fa75-3d22-a35f-758d2e8ac955 | -5.29655 | -60.14104 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 854c2c92-b4e8-3f4f-8029-ec8f7376ae58 | -5.36349 | -56.03727 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d7bc96d-3e0f-3cad-b65d-fada7d5d4e16 | -3.39008 | -61.3128 | 2026-09-07 05:04:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fa0baf5-c49c-37e6-af07-a6cdb42f7a72 | -6.17653 | -57.7368 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7543f5c0-81c1-3f36-ad97-7707711070f3 | -7.78894 | -56.33935 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cab1bff9-7088-39ec-a276-50870c31580c | -8.76757 | -62.41828 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0336b761-d39f-3dc8-975e-724f070b8323 | -4.97407 | -56.29025 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf62bc6b-534a-3376-91dc-57f001696a64 | -11.5148 | -49.60374 | 2026-09-07 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16d155d7-48b6-30a4-beab-be2bfa2a9507 | -5.99266 | -57.69424 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04e9aa0d-39d9-3a6d-b159-79e6ae6a82e5 | -5.32 | -55.87579 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3ef603c-3c95-3be2-83fa-406ef699dba8 | -5.16622 | -55.96767 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a275be32-c0e6-3d16-a7b8-a531de6f8e28 | -9.74451 | -43.39626 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 3bf28138-5bbe-3557-9d6a-a5ada7b53459 | -9.24799 | -46.6863 | 2026-09-07 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6065acc-be2f-389b-9aba-102d3d1f9ec4 | -3.83452 | -60.76473 | 2026-09-07 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17828473-6f51-3ee8-93aa-357c0ae75dad | -7.78822 | -56.34363 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 048e8b7b-798e-376e-88f1-e3da639b9c88 | -3.64015 | -59.54299 | 2026-09-07 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a9b941d-6fdf-35f8-9573-dbd7fca862b1 | -3.89728 | -60.9306 | 2026-09-07 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f42187a6-4ca4-3874-be8b-acf34926e9af | -5.83292 | -60.2558 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d1bc66a-9f3b-355d-8024-07ec9759ee25 | -8.5036 | -54.648 | 2026-09-07 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9b17df9-9df1-3251-910a-b26dd5bf7b5b | -6.13715 | -59.88831 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e38647c-c95b-3328-a2c7-6588b93b3026 | -11.33199 | -45.09831 | 2026-09-07 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ae00203-142d-343a-8408-0a8530f27d16 | -5.28424 | -60.14021 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ac474ca-5f7e-3975-9c87-ff5be2df2f6b | -4.67332 | -55.6297 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb01aa34-5987-335c-9c9b-4662e1195f53 | -3.82935 | -60.76378 | 2026-09-07 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7b4100e-a7be-3e8e-a465-b5e56cf2c82c | -5.36792 | -56.0335 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27974cbe-1614-370d-a563-1a959847b444 | -5.28705 | -60.12426 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 162f5da2-a60e-34dc-91a6-11f7291d773f | -5.3709 | -56.03851 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bf1786c6-fcc4-3cb7-ae3e-8ee7b413534e | -5.29961 | -60.15256 | 2026-09-07 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa278008-35b3-3e1a-aba9-74a0e607b95f | -4.54502 | -55.98256 | 2026-09-07 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91120d30-aff7-3666-93a4-793a0876a11f | -8.75949 | -62.41626 | 2026-09-07 05:04:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 976f08cf-cae5-3e3d-bb1e-5b846af1ca0a | -5.35971 | -56.01415 | 2026-09-07 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9f190e2-bb60-313f-8b0f-a7782cabe1a1 | -4.43228 | -55.09547 | 2026-09-07 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3b2950c-f48d-3a53-b8cd-2715bc3d79d2 | -6.05942 | -57.79139 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d6bc2fd-144f-3f69-bd77-1f0a0a1588e8 | -7.94933 | -45.24161 | 2026-09-07 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63673ff6-74c5-31c3-84ed-95071a4aa094 | -5.9892 | -57.68998 | 2026-09-07 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7402dfdd-331f-3125-bc09-0d0901ab1512 | -9.744 | -43.4002 | 2026-09-07 05:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |


[Clique aqui para ver as próximas entradas](README25.md)
