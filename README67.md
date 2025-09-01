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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d15676a-c7c8-3ebe-a982-d661a03f35aa | -15.70001 | -48.88448 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b73f7da1-dd3d-34fb-9947-eb3487e26e4c | -14.21789 | -48.38082 | 2025-09-01 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c19bcf8-9d46-3f68-9f30-b44ee74c6682 | -12.91864 | -56.99421 | 2025-09-01 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe40742c-d7e9-31e1-b344-327cdac4e089 | -17.1558 | -46.08461 | 2025-09-01 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0095426-1f76-3812-8f82-bd75fa4136fc | -12.88409 | -48.88717 | 2025-09-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e571b566-cfcc-3e91-a6f0-3c4357006697 | -13.69053 | -46.92124 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4763f647-9a2e-3bce-a068-3bac609ba9d5 | -14.00091 | -46.31496 | 2025-09-01 04:34:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f803c9d-6f40-3157-a4b6-017ef39e453a | -16.6836 | -49.46065 | 2025-09-01 04:34:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9cb420da-fa49-326c-9160-8ee48a1a7c4d | -11.88885 | -46.75111 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1410dd8c-5c0f-340d-9fb6-e8e741074d09 | -12.56621 | -48.22218 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 351ed7de-4adb-37dd-9d40-6dfcace72307 | -14.82467 | -46.73539 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d8f117e-08a0-3f38-88a6-d47dfb2a12b5 | -13.55105 | -46.95899 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5acc15c9-c74c-315b-894c-9d1b61958575 | -14.81871 | -46.72572 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76680a0b-335d-37ab-a3be-e0811a6fc5ca | -15.61864 | -47.85898 | 2025-09-01 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e549c947-fa1c-397c-a37c-ee6c2afbdf9d | -8.67628 | -62.40609 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69266391-79a3-38ac-9699-63e92c07ff63 | -12.14118 | -47.19364 | 2025-09-01 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16218af0-0be1-3127-a321-a1ad6c93e8cd | -11.08595 | -52.0398 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 166696a6-c45d-3c70-bf10-814be3222072 | -8.62442 | -62.58854 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bd15041-1ccc-301e-8137-13bf8143581b | -12.57847 | -48.20935 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 79f3b577-6100-3ef3-af7b-bd7146fda11b | -15.16183 | -52.34662 | 2025-09-01 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 140eafa0-764f-37f7-babd-e6cbcd617e87 | -13.17402 | -45.27717 | 2025-09-01 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 804f0b00-fcd3-3162-9a12-4a44584776d3 | -14.15986 | -43.67345 | 2025-09-01 04:34:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 06ea0138-7971-3770-b2e6-c4e3441f9876 | -11.05283 | -46.92089 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 301bc45b-51c7-38b6-8e1d-26293a3791dc | -14.80374 | -46.75357 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5be4de7a-79c9-3c24-9ab7-d5fab4e296f8 | -13.70443 | -46.8999 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e12ce8a-6104-37a3-86d4-168fb97d269e | -14.22815 | -51.65351 | 2025-09-01 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd897421-ea3d-39d3-a6b9-1c62016abc0b | -12.96807 | -48.1178 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d32ef03-cd5a-387b-841f-ae53a096926c | -12.87607 | -48.16714 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 18838a1e-d677-3a34-b4ac-7fada5781570 | -13.33767 | -46.96073 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 144eca08-86e9-309d-8b7c-014bf90fa0b5 | -12.31007 | -45.67712 | 2025-09-01 04:34:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| abfa4b2b-3325-350a-8e77-efb83c249ed8 | -8.75617 | -61.42702 | 2025-09-01 04:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b4c85d12-d9dd-3314-b6b2-141fd1a93451 | -13.54279 | -46.96629 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b66b702-6e80-3163-8abd-c6bd7d69cc34 | -15.58773 | -48.35118 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| fcd37130-caef-352b-80b1-f5dc78fe911a | -10.77299 | -48.84039 | 2025-09-01 04:34:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f65f0cc-a42e-35da-b4b3-90707d50028f | -11.96297 | -51.36578 | 2025-09-01 04:34:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb7d99bc-c38d-3656-85d5-0da03636537a | -15.59057 | -48.35542 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea582f3e-e747-337d-a89f-1d537078e81a | -14.42178 | -51.67077 | 2025-09-01 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8d7846aa-63f6-3fc1-89b3-98b4f4f43211 | -11.78683 | -46.43792 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccae68d3-3dfb-3f4b-b614-16efb2a0342d | -11.88537 | -46.75059 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5658a2d0-1924-3641-9262-e04fc1cc1112 | -12.59911 | -48.20897 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8cd72892-c302-37a8-a4b7-e1bc4d86ffa8 | -12.95943 | -48.1171 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba5a4e62-549c-3582-9723-cbfc5273ca73 | -15.58713 | -48.33198 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91d30a0c-d81a-3244-9fd1-f7c4e60e2675 | -11.37269 | -43.6232 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27ec40d0-a8eb-3ad8-92db-ef746cc6601e | -11.04479 | -46.99697 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04f6a47a-a42e-3b4e-bc26-c2e58dd6c31f | -15.10029 | -48.14863 | 2025-09-01 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf56b507-2a24-31eb-af7e-6e40cd191f36 | -13.34527 | -47.03814 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 213b0bdb-f55c-32ec-b310-1c902129cbb4 | -14.01957 | -44.60956 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5896b8af-8b5a-3f10-b2d2-6f30f6e3f47f | -14.79273 | -46.74147 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fec25c04-8235-3d30-8183-9d8c4a784f5f | -15.72793 | -48.99383 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9c464cda-5a26-3353-9a7c-03d36bb21e24 | -17.83173 | -44.32491 | 2025-09-01 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b88d61bb-81d3-35bc-a28e-2bced37b7dfd | -16.50742 | -55.03505 | 2025-09-01 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d94b14e9-f6de-34f8-8456-23cb96b29ce6 | -14.48478 | -52.99625 | 2025-09-01 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15e37d15-57ee-322a-8760-0c5f50f9f62f | -13.47795 | -46.99275 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ca12160-bd20-39cc-a820-4cd3349a650f | -13.33879 | -46.9772 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d8a40eb-572d-39c3-9a8c-858f0524ea9f | -14.78911 | -46.74116 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a1c9ce0-82fb-3f71-b522-82a7c8427ea2 | -12.86404 | -48.06513 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2312f8b6-2951-3c7f-b675-b34e1ac0457b | -15.79677 | -48.21635 | 2025-09-01 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7e693b9-50f5-3935-92c6-e7da0ffb43d7 | -9.44836 | -60.58068 | 2025-09-01 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 76b6ac91-eced-3d40-9fa7-2dc81ba29c38 | -11.89 | -46.74333 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1faf4045-8cbe-3e19-9122-1218bbc3ae4f | -11.37321 | -43.61944 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e5d31de-e061-3259-a097-90f654d09c26 | -11.95497 | -45.83457 | 2025-09-01 04:34:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05c76067-0990-303b-ad28-93462d919903 | -14.79958 | -46.73118 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d18f94b-1a10-30ba-a40f-4de19239ced6 | -13.3219 | -46.84916 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 955713f4-4ed7-3143-89d3-1d7b044f21aa | -15.59792 | -48.35276 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b88934c0-3161-3e87-a2af-1fa8777e503b | -13.40814 | -47.0236 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24f7b516-3ed7-331e-b3c4-d937dd6801cc | -11.04708 | -46.9819 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29614c32-cf0e-30ed-8f04-c7ed6c5a510c | -11.90623 | -46.68183 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95727f3e-fdc0-3509-a55f-70b6524fb76b | -13.48961 | -46.98653 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5872e2f-1a21-3da6-b0b5-175a20656fc2 | -14.77412 | -46.76848 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 823280ae-45cc-3eaa-b688-f163cb957359 | -14.42025 | -51.65874 | 2025-09-01 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff1351ec-8ceb-32d2-896e-22bd8e834bf5 | -14.78692 | -46.74298 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 40c03c2f-a0c8-3828-a138-73f4ff9666fe | -13.49423 | -46.97946 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 795b4124-330b-3753-8d17-c303cc012625 | -15.08328 | -48.12268 | 2025-09-01 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c4dc7b8-9acc-322c-b070-1c910c690970 | -13.16955 | -45.28136 | 2025-09-01 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| b7b73c4e-3f25-39c2-9fc9-11849748cf10 | -14.58486 | -54.53586 | 2025-09-01 04:34:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e35c610-1a68-353c-b2f2-1ef33393da2b | -12.63847 | -48.16697 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ff4d9f8-ddf0-3ab6-9c3b-b57c04570c0f | -12.09105 | -44.72348 | 2025-09-01 04:34:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 32aac792-80b2-3c46-b85a-f5059fb199ce | -14.99205 | -48.14786 | 2025-09-01 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d505f007-e8f9-39f8-b499-cd86f295c731 | -11.03451 | -47.04148 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f126237-a702-35fb-bf9a-205e9db49c0f | -15.69835 | -48.91803 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| defef93b-85a1-305b-b4c9-ef44ac274e9b | -16.15433 | -49.63757 | 2025-09-01 04:34:00 | NOAA-20 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90e42212-c2a3-381c-b15f-a068348a2eba | -13.34229 | -46.97773 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fc38f4c-8450-3d14-801a-fb0509178d77 | -14.20721 | -48.38303 | 2025-09-01 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54f2c302-3bdc-3e46-8692-a9597fc09da3 | -14.59506 | -54.5698 | 2025-09-01 04:34:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52a360d4-6a1f-3a9f-b13b-063054101eae | -11.33222 | -43.68229 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7139a98-562a-35df-b863-b0efda0c1181 | -16.20627 | -55.9485 | 2025-09-01 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 73432bce-ee02-392d-8fcd-bc673ce27720 | -11.80756 | -46.4194 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 46516b79-84a2-3c07-a4d1-d0d72ec4724d | -12.84001 | -48.07645 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 03031142-ea5a-3717-9a73-e81d7db4c087 | -13.53809 | -46.97376 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5195c146-fbb8-38ab-b621-32421ae058b7 | -11.07031 | -52.06709 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb025534-8b4a-3ae9-aea4-363d574f765b | -15.5894 | -48.34003 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 631a968f-dc3f-3ab5-b80d-9491ad7617c9 | -15.31086 | -46.08148 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38499097-52a9-3a05-99bc-2dad53eb4989 | -11.33119 | -43.68155 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1387a4c5-4844-313f-a3d2-1b237b07cdf1 | -12.60302 | -48.20589 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89b411f2-b4bd-3d1a-ae9d-5dc59d98cb5b | -13.33188 | -46.85465 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db707544-b594-35e9-9115-0beba71d8e19 | -15.99878 | -43.42232 | 2025-09-01 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ea38150-bf4a-3e41-b0c7-8013dcb11a16 | -11.37375 | -43.64605 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50720d88-9adc-3777-b2bd-9a1fb669242c | -12.58849 | -48.18879 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5783c281-32ee-347f-8a32-cd4a057833df | -12.86013 | -48.06818 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| db93bec9-5745-3359-bf03-31aa5691533b | -13.31839 | -46.84855 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README68.md)
