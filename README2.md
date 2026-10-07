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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba041d93-d0f8-38b6-8ae0-7c77b4a7c03a | -3.1114 | -53.7839 | 2026-10-07 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 707d7ede-925b-3893-a8e9-2614c3bc49e7 | -3.1299 | -53.7633 | 2026-10-07 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 25f02015-6d75-3ac5-bd68-1ffbd0315e57 | -8.6847 | -45.2081 | 2026-10-07 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| f58c83bc-c8c5-3028-8949-c4f374b8fabb | -8.4433 | -46.407 | 2026-10-07 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 9c71a3cd-e1dd-33a2-94d7-231f4008b611 | -12.1746 | -44.7051 | 2026-10-07 00:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 15429a4b-d351-34f9-8e2c-4513c24197c2 | -2.9264 | -54.1505 | 2026-10-07 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 91fe5b82-5865-3b85-a737-e71fba28de16 | -7.8234 | -72.7142 | 2026-10-07 00:10:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 1901cc72-51fd-3f9f-bddf-142572765dc5 | -5.9835 | -40.9367 | 2026-10-07 00:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| f472787a-0ca1-3d42-895c-8e730069fa05 | -2.7613 | -54.0941 | 2026-10-07 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 278.6 |
| 6e0f05d9-01c2-3585-bde5-baf5d4a8dbc2 | -3.4762 | -50.0883 | 2026-10-07 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 193.5 |
| 3f939014-9f54-3ed1-ada7-e22792742e65 | -2.7612 | -54.1142 | 2026-10-07 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 4fd3b5cc-7537-3da3-9e5d-6954fd0bab05 | -3.6762 | -60.6409 | 2026-10-07 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| d4f9dd3f-33c6-33e0-bb09-70a8395c30c7 | -2.7797 | -54.0736 | 2026-10-07 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 5a2648f2-28b4-3d42-834d-5dce1f1366f2 | -3.055 | -54.1474 | 2026-10-07 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 3d09d867-983a-3369-adf3-238f681e592c | -3.0 | -54.1287 | 2026-10-07 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| aa61b9c1-bf53-3e2c-a1fd-63501884b6f5 | -3.4578 | -50.0679 | 2026-10-07 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 930ac1a8-a291-3e99-b335-5c58a5c67a6c | -3.4577 | -50.089 | 2026-10-07 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 475df91f-79ba-3a35-893b-7ba1898086d6 | -8.7225 | -45.204 | 2026-10-07 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 9861c8c8-2ec1-3f9d-b875-640423fc7a98 | -8.2868 | -50.2519 | 2026-10-07 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 99f4859c-ba77-35ae-b6e1-9fc92b808670 | -8.2865 | -50.2731 | 2026-10-07 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 234.8 |
| ff03ab3c-9a75-3a3d-ba3c-5fbea97a2b5c | -3.6762 | -60.6219 | 2026-10-07 00:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 13ad4f88-ce88-38ee-9165-b845b569fcae | -2.7796 | -54.0937 | 2026-10-07 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 260.3 |
| 83fcee12-eec6-3972-b0cf-5bd92ff7d14f | -3.8814 | -59.3202 | 2026-10-07 00:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 8c5bc852-b0cc-344c-965f-494c75fc1573 | -1.8193 | -57.1159 | 2026-10-07 00:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| ae64e888-578e-38e8-8071-5d4318f4b7b6 | -3.8567 | -55.9769 | 2026-10-07 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 5dd3d659-dbe7-37a3-9e4b-34b018720aaf | -4.0025 | -56.2487 | 2026-10-07 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| f7b89c25-9aae-3ecb-9c5f-8172337bb897 | -5.7376 | -45.1533 | 2026-10-07 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| c6ac2dd6-6d38-3e66-87aa-0defceea7656 | -8.5051 | -54.6202 | 2026-10-07 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 94bb9303-7b00-360c-8a7b-ad4d468cc19a | -1.8011 | -57.0967 | 2026-10-07 00:10:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 456f6479-e77c-3446-abd4-a7a2041749a0 | -10.2569 | -36.3362 | 2026-10-07 00:10:00 | GOES-19 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 78.2 |
| 7a96aba9-a34b-375b-aaef-f4cfb622fd73 | -2.7874 | -51.6719 | 2026-10-07 00:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| bac4cef4-f83e-3f5a-9c98-5d95e08fcf32 | -5.7187 | -45.1773 | 2026-10-07 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 41878c1c-67fc-34b7-8787-d70002d4b3bc | -13.5117 | -44.368 | 2026-10-07 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 86ddbcc6-4197-333c-a4f6-7eb3a8b08f2c | -11.0133 | -45.473 | 2026-10-07 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 6859259e-d0b3-3cb5-af45-0c4579beb150 | -4.7589 | -55.6516 | 2026-10-07 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 4bc0a35a-4665-3e28-894e-d45afc02d0f2 | -3.1787 | -50.5597 | 2026-10-07 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 228.0 |
| 9deeaae2-b5e6-3edf-98d8-7aacfd617cfa | -9.4621 | -67.0817 | 2026-10-07 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e8637a76-fd74-3de8-8997-e2ec9acbd316 | -3.4947 | -50.0877 | 2026-10-07 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| cabf2b91-3c9f-3bf3-94f0-0062e98f1a75 | -3.4763 | -50.0673 | 2026-10-07 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 4bf23af0-c427-33ac-bc16-aa27a1f0e0d0 | -2.7796 | -54.1138 | 2026-10-07 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 0e4d2916-d171-3697-84cd-ccce4f1e1e34 | -3.1972 | -50.5592 | 2026-10-07 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 1ce76d63-e55a-3583-9386-c45128d20a5c | -2.9816 | -54.1291 | 2026-10-07 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 899cbba7-e3d7-35c1-af95-4552c79e324c | -8.7036 | -45.2061 | 2026-10-07 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 282.8 |
| 245f11bd-aade-31e2-a870-acad77a365b6 | -3.0548 | -54.2076 | 2026-10-07 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ce27c85a-3e40-35ac-85a8-c76d62b05d0e | -5.9838 | -40.9123 | 2026-10-07 00:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 56.4 |
| 4c53bea4-36a7-3378-9b20-9139f679c474 | -3.1101 | -54.1661 | 2026-10-07 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 0304cc66-e311-386b-96d3-97e991751041 | -3.6206 | -55.2708 | 2026-10-07 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 78f1745c-d3fe-3807-a894-e944b4c4d3c9 | -11.7335 | -43.649 | 2026-10-07 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| d0121a48-7051-31db-a797-b05d56e0525c | -5.7374 | -45.176 | 2026-10-07 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 6ee18294-bf14-315e-9686-a10f7627929a | -6.766 | -56.2402 | 2026-10-07 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 40134d94-a3fb-33de-b4e9-f0c395b3be7c | -6.2947 | -43.6427 | 2026-10-07 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 2e6f3162-e8e6-33ce-8a72-e3260ec30236 | -3.0184 | -54.1282 | 2026-10-07 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 437f3df2-7d0e-3648-ae6b-df8d2c492717 | -12.1939 | -44.7021 | 2026-10-07 00:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 38d0ab8d-28c1-394b-bb02-f85d0bd96322 | -8.7033 | -45.2289 | 2026-10-07 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 137.2 |
| b4075b5a-878c-30de-bb40-d9d764f187b5 | -3.8997 | -59.339 | 2026-10-07 00:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 853fe09b-4291-3891-988c-387b5c6de14e | -11.0137 | -45.4501 | 2026-10-07 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 4962129e-ab3f-3068-acd7-e1898553f723 | -8.7039 | -45.1832 | 2026-10-07 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 4f273833-1015-3eb7-8b4a-402f89a3fc2a | -3.5515 | -59.4807 | 2026-10-07 00:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| a40f967c-19d8-313f-85c1-de862ef04502 | -3.5061 | -51.6924 | 2026-10-07 00:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| cc64413a-e547-3c28-8218-188b8f27d298 | -3.6205 | -55.2907 | 2026-10-07 00:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 999d2602-5779-3d61-b37e-e936a5632b12 | -3.8997 | -59.3198 | 2026-10-07 00:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 2d775659-14c3-31fe-9b77-d7376bcce197 | -3.1115 | -53.7637 | 2026-10-07 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| b731a5a0-9d89-346d-b411-90bb638d9185 | -8.7228 | -45.1812 | 2026-10-07 00:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 88b4b385-1728-3428-8208-dc8bbaa77335 | -2.7613 | -54.074 | 2026-10-07 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 1371db85-92ac-3fd6-94fc-716586076d30 | -2.9447 | -54.1702 | 2026-10-07 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 68f95036-ee28-3923-a336-9c91ed576ba8 | -3.1787 | -50.5807 | 2026-10-07 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 3cde81f0-58d7-3846-8cf7-d6c9ee6692d1 | -3.32 | -54.02 | 2026-10-07 00:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eab46364-0d9e-3ce0-80f9-493aa0f9a1c7 | -3.29 | -54.07 | 2026-10-07 00:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa1d9257-54b0-3021-b204-1e7532df1946 | -3.29 | -54.01 | 2026-10-07 00:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bc16af7-8671-3798-93e8-89cf8806f8c6 | -8.7 | -45.24 | 2026-10-07 00:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 382fef7b-5826-36e8-b310-0cfcc9c068f5 | -3.0557 | -53.9464 | 2026-10-07 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| d8436672-97c2-311c-bdc5-936a010c6212 | -3.1299 | -53.7633 | 2026-10-07 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| e50babec-0584-3406-aeb0-6ca42a09eec9 | -12.1935 | -44.7254 | 2026-10-07 00:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| a3c1a27d-8ec5-370d-9b49-d70046de6faf | -3.5061 | -51.6924 | 2026-10-07 00:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 0439821c-fb22-3b93-9cd0-6a6b43d7f763 | -4.7589 | -55.6516 | 2026-10-07 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 5a51510d-b2ec-306f-8389-fa5eae395263 | -4.0025 | -56.2487 | 2026-10-07 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 685dbd97-4cbb-3c83-9b4b-27eddfed8531 | -3.8567 | -55.9769 | 2026-10-07 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 610a1743-0590-3f70-9be7-34a032d06191 | -2.7796 | -54.0937 | 2026-10-07 00:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 259.6 |
| 3844b559-3324-3a3e-9ba3-bb1030eff1c5 | -3.0375 | -53.9066 | 2026-10-07 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 6fa357cc-0229-30f3-89bc-ae46620e0b76 | -5.9649 | -40.914 | 2026-10-07 00:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 48.8 |
| ad6df824-6e7c-3311-a657-76006eb9d83f | -4.8659 | -44.369 | 2026-10-07 00:20:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| dd4a2ee9-df58-32f8-8fd9-c6844878578f | -2.7613 | -54.074 | 2026-10-07 00:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 16b20daa-038d-3e32-9a32-7d9eb3976840 | -3.0548 | -54.2076 | 2026-10-07 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 43b281e8-d024-38ca-8378-e06c91acaa82 | -1.8011 | -57.0967 | 2026-10-07 00:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| e43fa0ce-e15f-3e2e-bbcb-1d1bc3093f9f | -3.1787 | -50.5597 | 2026-10-07 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 199.5 |
| f8a3b327-a216-3a5e-880e-0f3dbbbab49c | -9.4621 | -67.0817 | 2026-10-07 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 99e18a4f-5709-31a8-aa62-bf0a86e65b70 | -3.1972 | -50.5592 | 2026-10-07 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 5aea8607-e670-33fe-b110-7ed351463518 | -3.1971 | -50.5801 | 2026-10-07 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 168514cb-132c-3d9a-93f3-124460d2ee5c | -6.2159 | -52.8285 | 2026-10-07 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 9f7bbdeb-ed06-3db1-ad6a-5c701b3629c8 | -3.8566 | -55.9967 | 2026-10-07 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 926a6ac4-fea6-3632-aa5e-51e1d20574da | -7.8234 | -72.7142 | 2026-10-07 00:20:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 2be4e33d-c8c9-3464-a15d-a46d7ad1da3e | -3.0558 | -53.9263 | 2026-10-07 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| af569932-b565-3c48-8a96-aca59c0dc222 | -8.7033 | -45.2289 | 2026-10-07 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 138.6 |
| a4eaa703-1329-31d4-981b-8b659206d469 | -8.7039 | -45.1832 | 2026-10-07 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.0 |
| acc38cd6-bbe8-3fb1-afb2-1bcb79735ca6 | -4.0024 | -56.2684 | 2026-10-07 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| afe8fce4-eea2-32e7-9cb3-15de62ec33f3 | -2.7797 | -54.0736 | 2026-10-07 00:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 83c0ead8-4f88-350b-8f73-0029cc4cd115 | -2.9448 | -54.1501 | 2026-10-07 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| b7956483-0fd3-3bf4-9031-cc26647c5a02 | -3.658 | -60.6222 | 2026-10-07 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| cc827c46-5b9b-3823-a66c-2568e4319589 | -13.4922 | -44.3713 | 2026-10-07 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 524a28ac-07ab-38a2-8461-0937868bc9b2 | -8.7228 | -45.1812 | 2026-10-07 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |


[Clique aqui para ver as próximas entradas](README3.md)
