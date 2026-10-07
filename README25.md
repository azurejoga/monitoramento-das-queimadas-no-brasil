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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5558af18-3aa6-3a73-832c-dfb41ace3cf5 | -3.4763 | -50.0673 | 2026-10-07 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| d6e7964e-ea1e-3aa9-901d-e07d8df6a64e | -3.1787 | -50.5807 | 2026-10-07 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| dbfd64db-456b-38fb-b0c7-bfa5b768d668 | -11.0137 | -45.4501 | 2026-10-07 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 61286cd8-8596-3ea5-b8ac-d9468de91a14 | -3.6762 | -60.6219 | 2026-10-07 01:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 810e75ce-11cd-3384-9ad1-88a2395c3e6c | -3.055 | -54.1474 | 2026-10-07 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 80925529-e90d-3189-be71-1bbfe41f1e8c | -8.7222 | -45.2268 | 2026-10-07 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 46.7 |
| cf24a039-e482-39ab-9b93-15a1e300a2c7 | -8.2865 | -50.2731 | 2026-10-07 01:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 157.6 |
| 20c68eed-f8b0-3368-9a59-ade91df97634 | -9.1076 | -67.7215 | 2026-10-07 01:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 8a111512-bb9a-3cde-b0a9-69a78231814b | -11.7966 | -46.57 | 2026-10-07 01:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 757fb982-78a0-375e-91d6-42c48a9b5ae1 | -3.0 | -54.1287 | 2026-10-07 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 5e5d2cd5-43b0-3560-acdc-535541d0dea0 | -13.5117 | -44.368 | 2026-10-07 01:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 241b6904-7896-3568-9e13-11ad80bf8e4a | -10.8798 | -46.6691 | 2026-10-07 01:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| afc7711f-8d4c-3244-8e4c-d86d47aa5853 | -2.9264 | -54.1505 | 2026-10-07 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 839a52cc-691a-3d05-9269-29df1843b440 | -3.0375 | -53.9066 | 2026-10-07 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 83719db4-8390-301b-8918-a25f586a8663 | -3.1787 | -50.5597 | 2026-10-07 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 132.9 |
| ecfe4b61-59b4-374f-ad95-c19b193876f6 | -3.0374 | -53.9268 | 2026-10-07 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 24dab6df-5335-3b7e-8179-c85308b17f1d | -3.4762 | -50.0883 | 2026-10-07 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| ad50e59f-3300-31d2-bc44-4bbcf4264036 | -3.0373 | -53.9469 | 2026-10-07 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| fbada385-430d-369c-b0e2-777f9aff5f29 | -10.9946 | -45.4527 | 2026-10-07 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 33cd616a-e3b2-33a1-beaa-8370e20e275f | -3.6579 | -60.6412 | 2026-10-07 01:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 3edccbf6-ffc1-3936-84c1-9ad175673f12 | -10.9949 | -45.4298 | 2026-10-07 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 1c3fd0a3-3319-3b56-be79-507e0fcb12bc | -2.7796 | -54.0937 | 2026-10-07 01:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 200.6 |
| 2d9eca3e-5c7e-36e2-beb6-b7fd30768399 | -8.7225 | -45.204 | 2026-10-07 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 1622d53c-6e23-3c95-b66a-ba135c488893 | -14.2531 | -41.6256 | 2026-10-07 01:30:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 171.5 |
| 4de9aa69-263b-3959-8fe2-1224ececb4ea | -3.8566 | -55.9967 | 2026-10-07 01:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| df9fcb73-1592-3098-8610-2edab84186b4 | -3.4577 | -50.089 | 2026-10-07 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a5835757-40fe-30c0-ae36-25b6937fbb48 | -11.2333 | -44.8678 | 2026-10-07 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| e17707a1-95b8-3b76-b4c8-af0d4b020ff4 | -1.8011 | -57.0967 | 2026-10-07 01:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| d0f7515b-db58-3f19-8ad3-8b1b6505c6be | -1.801 | -57.1161 | 2026-10-07 01:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 625112d5-8dec-30b0-843d-cf23fb4e1d70 | -9.1517 | -65.9554 | 2026-10-07 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 69f8a4d2-b70c-3b8c-99b2-236b7cb7af79 | -11.014 | -45.4272 | 2026-10-07 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 941ca139-d3f9-3640-b1e3-b659851b4c64 | -3.0184 | -54.1282 | 2026-10-07 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| bde408cb-58e7-385b-84a0-6f41ae5b1c82 | -11.7962 | -46.5926 | 2026-10-07 01:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 8d3f435a-e6d6-3463-9e52-483614a48096 | -8.7039 | -45.1832 | 2026-10-07 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 8dd336e5-82a9-3e97-a35c-4a7fa94f6cc3 | -2.7797 | -54.0736 | 2026-10-07 01:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| d9c682e9-05db-3651-a403-2114a35d4c36 | -8.2868 | -50.2519 | 2026-10-07 01:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| ed744dfe-e1b8-3b95-b647-21704b289db6 | -11.1051 | -45.689 | 2026-10-07 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 475a4cc0-6697-33e3-b996-7806f5c5601d | -11.7335 | -43.649 | 2026-10-07 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 9c09e07c-b526-318a-9dc9-11a064091f60 | -3.4577 | -50.089 | 2026-10-07 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| e506b8c2-8b2e-3b5a-ac28-3f06f08eb8b2 | -2.7613 | -54.0941 | 2026-10-07 01:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 234.1 |
| c080576a-558c-3fb4-a0df-abf6aa1a2b54 | -3.0191 | -53.9071 | 2026-10-07 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 928f3c21-59bc-3b37-a6c2-592d0a6793c4 | -8.7039 | -45.1832 | 2026-10-07 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 399789c0-ba27-3363-8132-7991971928fe | -3.1972 | -50.5592 | 2026-10-07 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a63de11e-c1f2-3db7-92b5-f6e5f4036025 | -2.7797 | -54.0736 | 2026-10-07 01:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 2191d573-eafb-3900-a7b3-0ceadf45a363 | -5.9647 | -40.9383 | 2026-10-07 01:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| b9403db0-084d-36cb-b5b4-39fd7af9e4df | -8.7228 | -45.1812 | 2026-10-07 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 228.7 |
| a8f9144b-da37-3ede-baf1-8c9674e2b432 | -10.9949 | -45.4298 | 2026-10-07 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| d50ee1c4-8426-3455-8679-0690524d94ca | -8.7036 | -45.2061 | 2026-10-07 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 235.2 |
| f6e04cff-2806-300f-9e13-a7ac0534fbcb | -14.2727 | -41.6215 | 2026-10-07 01:40:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 67.8 |
| 9eacbfee-3f24-3a5e-87af-68d620ad9a56 | -8.2865 | -50.2731 | 2026-10-07 01:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 147.4 |
| 4fc11722-f3e6-302f-81c3-67662e94bf7f | -3.0001 | -54.1086 | 2026-10-07 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 027237b8-1a30-305f-b14e-2825baad8be5 | -2.7874 | -51.6719 | 2026-10-07 01:40:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 8ed4f036-b06d-30e0-a263-9ee3bb22ab35 | -3.0374 | -53.9268 | 2026-10-07 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 217.9 |
| 87438b99-3d7b-369d-9232-c1d276e9a88c | -3.2727 | -50.1583 | 2026-10-07 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 6fac7990-c5a1-32ac-96ee-943181d379ad | -3.8567 | -55.9769 | 2026-10-07 01:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 4f52d766-d574-34e3-9465-a30adde6d4a6 | -7.1265 | -60.7307 | 2026-10-07 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 3af50ea7-e32f-353c-8151-f032bbc44147 | -2.7796 | -54.0937 | 2026-10-07 01:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 196.0 |
| 618260fc-68c4-3ebe-9984-276e21bf6ffa | -3.4963 | -59.5775 | 2026-10-07 01:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| d30ac4cb-619a-39cd-9567-d6dc9a86c35c | -5.7189 | -45.1547 | 2026-10-07 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 8ca2e692-6c19-3477-98d7-13577e85b95e | -3.4762 | -50.0883 | 2026-10-07 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| de751390-3cf5-39d2-8a9e-3fb26c0c0525 | -11.1047 | -45.7119 | 2026-10-07 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| dd312eb0-e71c-3f64-9d72-649639894d7b | -2.7613 | -54.074 | 2026-10-07 01:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| c90ed947-9d42-37e7-a72f-018ac9d379bf | -2.7612 | -54.1142 | 2026-10-07 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 822e6a81-414a-31ed-b252-1fdb11133645 | -1.801 | -57.1161 | 2026-10-07 01:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 10f7146d-c1b9-3099-8095-4c3d95e8c47d | -3.658 | -60.6222 | 2026-10-07 01:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 7a6e954c-7933-399b-a88e-9d1e6ae99f59 | -3.8566 | -55.9967 | 2026-10-07 01:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 493db849-d7ac-33ad-befe-db30a5fba7d4 | -10.8798 | -46.6691 | 2026-10-07 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| acf80d00-f2a6-3d9f-8ed9-cb8865c0b42b | -8.7225 | -45.204 | 2026-10-07 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 251.4 |
| ac66c44b-fc77-32b6-8fb4-ca185002d887 | -5.7374 | -45.176 | 2026-10-07 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 4ec538ca-f235-3e09-8914-af4a71116c03 | -5.7187 | -45.1773 | 2026-10-07 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 076e6178-e4d4-3cd6-af66-c938c50fc68c | -3.1115 | -53.7637 | 2026-10-07 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 3f230d65-1c13-3883-a413-717148fe4cbf | -3.0558 | -53.9263 | 2026-10-07 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 19173399-e174-37b4-90d9-2a8a08dd7ecc | -3.0373 | -53.9469 | 2026-10-07 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 63f7429a-d2bf-372b-ad80-5b3d8c014e7f | -2.9448 | -54.1501 | 2026-10-07 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 44f29a20-f17f-3911-a53e-de998b1a1155 | -14.2537 | -41.6007 | 2026-10-07 01:40:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 123.3 |
| 14f5baff-642e-3f50-a15c-809611b4af06 | -3.1787 | -50.5807 | 2026-10-07 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 60367ff5-d259-35d9-a09c-c88e3b3f1b6b | -11.7966 | -46.57 | 2026-10-07 01:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| ddea2858-26d7-339b-b3c2-c4966cfcdf13 | -3.2913 | -50.1366 | 2026-10-07 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 083f1921-af27-38a2-89cf-17efa546d176 | -3.4763 | -50.0673 | 2026-10-07 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 756c09ca-f683-3a74-aa49-2b4d499c001a | -3.6205 | -55.2907 | 2026-10-07 01:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 26554c15-37a6-3297-b9f7-e152972166b7 | -3.0 | -54.1287 | 2026-10-07 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 8729d050-bbd8-3c5f-a6cd-2c4fd13d6f6b | -14.2531 | -41.6256 | 2026-10-07 01:40:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 311.0 |
| b0901789-cf9a-358f-bb6e-e929075dbd24 | -3.5515 | -59.4807 | 2026-10-07 01:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a55c38e5-0bea-3702-a825-b6697d6b6a64 | -3.6579 | -60.6412 | 2026-10-07 01:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 113.9 |
| bb292b74-f2e5-3e38-ba62-28d93bfe40e5 | -10.9946 | -45.4527 | 2026-10-07 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ea4d098b-9724-3993-8423-2c5d8b77e19e | -3.0375 | -53.9066 | 2026-10-07 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 275e0bc5-e312-33d8-a4ea-9fcadd4c4b05 | -11.014 | -45.4272 | 2026-10-07 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 287a9dd8-f49d-337a-9735-a75b6d8dbef2 | -3.0184 | -54.1282 | 2026-10-07 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 760063c8-6ba6-3526-ad52-467592e7cfc4 | -11.2333 | -44.8678 | 2026-10-07 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 1c74e62c-78cd-3663-8b14-aef8f806b0d6 | -11.0137 | -45.4501 | 2026-10-07 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| bba5bf9e-32ce-368c-90d0-26dfefb42d96 | -3.6762 | -60.6219 | 2026-10-07 01:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 4e4f0d8e-ec6d-3d63-a751-bd7ddcf1018b | -3.2728 | -50.1372 | 2026-10-07 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 165.7 |
| 5c2a27c5-43cb-391b-8e53-cf6cce99316a | -8.7033 | -45.2289 | 2026-10-07 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 6e5b9cc4-c39d-3c1d-abd3-78f6e9cd5806 | -3.4963 | -59.5967 | 2026-10-07 01:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| efebff64-691f-3ec1-be41-eae286b4b6db | -3.019 | -53.9272 | 2026-10-07 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| e79a52a2-96fe-3287-972e-9b043d0fe641 | -3.1114 | -53.7839 | 2026-10-07 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 287d6da4-24a9-32c1-891b-a27a0f187ffd | -2.9264 | -54.1505 | 2026-10-07 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 83e05830-3648-3826-bbec-2c3292c8f421 | -3.1787 | -50.5597 | 2026-10-07 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| d9e4b8b2-3af0-3084-91b8-c5cbb60aae19 | -2.7796 | -54.1138 | 2026-10-07 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 2a366181-caf2-3a73-849c-16c567bb6db9 | -3.1101 | -54.1661 | 2026-10-07 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |


[Clique aqui para ver as próximas entradas](README26.md)
