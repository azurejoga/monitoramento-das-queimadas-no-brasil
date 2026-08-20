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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82463922-fd94-3b95-9615-0f6e4cc61664 | -18.0487 | -44.6066 | 2026-08-20 00:00:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 491bf001-b010-3fa1-830b-8bb8e8908a17 | -5.8087 | -55.7293 | 2026-08-20 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| c3f1fa1a-1bec-3c14-938a-3d4ad1987b94 | -8.6727 | -54.6492 | 2026-08-20 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 279.6 |
| 7d9fa306-36a6-3da4-a0af-d88551746025 | -6.9129 | -59.3385 | 2026-08-20 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| e330016a-408f-3053-b0ff-4345d3fbb30c | -6.583 | -58.9658 | 2026-08-20 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| bc97cf16-af98-3f3b-99ac-dc75d0f65722 | -7.3413 | -45.8377 | 2026-08-20 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 272.6 |
| bfc7d3fa-a84b-32bd-8a8b-548b6e805b8a | -6.4389 | -52.7548 | 2026-08-20 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| cf06b04a-aef2-3ccc-a412-537c3a4a44af | -5.8088 | -55.7095 | 2026-08-20 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 420156c2-9532-30b1-9a63-0f2ee99f5d7e | -9.139 | -51.1307 | 2026-08-20 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 22e88078-5603-3dda-b6cf-35f0b717b77e | -8.6729 | -54.629 | 2026-08-20 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 0a9f7cb9-1d45-3979-bc9d-b575cfed96ce | -6.6015 | -58.9651 | 2026-08-20 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 1882a815-80fa-3467-87df-9d6ea8ac54f5 | -8.654 | -54.6505 | 2026-08-20 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| b9ee977d-6c3a-355d-b1ad-81b8ea71b0e6 | -6.6929 | -59.0966 | 2026-08-20 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 23340f6c-132c-3abc-a546-3c248168549f | -8.6915 | -54.6277 | 2026-08-20 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 3e26b04e-d032-3448-8d8b-22852d875be5 | -6.7114 | -59.0958 | 2026-08-20 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 20acf7c9-8a25-3878-a8bc-24599f932356 | -6.8778 | -59.031 | 2026-08-20 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.7 |
| f7124da7-6c95-38d4-af69-dc11d273e624 | -7.9751 | -44.6648 | 2026-08-20 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| b4d0211f-49e9-3c87-b5c4-d8fd6f02d18b | -8.6725 | -54.6695 | 2026-08-20 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| e3022953-54e5-3e46-818a-aac6e225bc0a | -6.9128 | -59.3578 | 2026-08-20 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 8bbb5c5e-bd8d-31b4-a436-cb35f8b3b162 | -7.3788 | -45.8344 | 2026-08-20 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 0f5b882e-9c5a-38b0-bd48-4e6bd8c1ae74 | -9.1388 | -51.1517 | 2026-08-20 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| a2b0bd1f-9748-3a08-aaee-fbd325b73d71 | -1.8425 | -54.4917 | 2026-08-20 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 7846059f-ed6f-3207-bc01-eacd60523646 | -12.4726 | -54.7382 | 2026-08-20 00:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 4a87c983-bd66-3560-a37c-74cb321517e2 | -11.1936 | -54.0199 | 2026-08-20 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 352c7952-a7ab-3bef-91f6-7c328358a604 | -18.0285 | -44.6113 | 2026-08-20 00:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 778c6121-acea-335d-85e0-0d5a428f561a | -6.5829 | -58.9851 | 2026-08-20 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 1765b2fa-6c6e-3dea-a315-3f241f7cc94a | -9.2256 | -59.7894 | 2026-08-20 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| eabc9509-0006-3032-99e5-d79602c2b5b1 | -11.2191 | -55.0382 | 2026-08-20 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 065c30e1-1a39-3884-8e28-cd5df3c5b7c7 | -9.207 | -59.7903 | 2026-08-20 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 36e8893d-5e0d-3acb-b9e0-8dc69e79ee53 | -17.3372 | -43.6139 | 2026-08-20 00:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 218.1 |
| f2ad996b-caa2-3bd9-990c-d6ca3145f0d8 | -9.2258 | -59.77 | 2026-08-20 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 1216004f-9adc-391b-8f61-709b947e9554 | -7.3603 | -45.8136 | 2026-08-20 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 193.6 |
| 8281527b-0272-3302-a72a-56e28c548e8a | -8.5401 | -54.8802 | 2026-08-20 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| e1cae03b-c391-346e-94cf-5cf7436758e2 | -5.7903 | -55.7301 | 2026-08-20 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 380b3634-c00b-3b0e-a0b7-4dd4d09e4473 | -12.4916 | -54.7364 | 2026-08-20 00:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 226.2 |
| 681b7884-531a-376b-be5a-6f8b78d7641d | -8.5214 | -54.8814 | 2026-08-20 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 65ca928e-e790-3718-98b0-3e6aceeb0882 | -14.4554 | -45.6251 | 2026-08-20 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 16d23e87-8591-31ac-98b3-892f8dcd0d48 | -11.2189 | -55.0585 | 2026-08-20 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 50046de1-28a5-33ea-972a-682f1722459a | -1.8242 | -54.492 | 2026-08-20 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 8343657d-b4a0-3fdd-a12f-d462c2a6c805 | -7.7551 | -49.2067 | 2026-08-20 00:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c31d9021-16ce-3b27-b4a5-1863aac32567 | -2.5629 | -47.2445 | 2026-08-20 00:00:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 67738d47-c0b0-3394-b1c5-0892d5751832 | -6.9313 | -59.357 | 2026-08-20 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 57d8b38a-2a59-35b6-946c-b830b9ea6806 | -9.2071 | -59.771 | 2026-08-20 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 44204bfe-04b2-3a25-bd35-345e81bcae1c | -12.4919 | -54.7158 | 2026-08-20 00:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 6780a243-6762-3a2c-8da2-c15341d2e0b0 | -12.4729 | -54.7177 | 2026-08-20 00:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 5a06d301-233d-3092-8521-3e0ff4bfada0 | -6.4391 | -52.7343 | 2026-08-20 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| ea33904f-aa6b-3bcb-b1fb-796b06f5407b | -5.7904 | -55.7103 | 2026-08-20 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| ca46d7b5-53d6-3f53-9e72-3da439e95c6b | -12.4914 | -54.7569 | 2026-08-20 00:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| ba62534a-a79d-3799-a8ce-fad9ddaba028 | -7.3415 | -45.8152 | 2026-08-20 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 265c7d0f-ebc4-3dec-b7e1-a4b5aa5fe2f2 | -6.7124 | -58.9219 | 2026-08-20 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 99dcd06d-7ca9-3dd3-bb9a-b7a4b6c596b9 | -6.7122 | -58.9606 | 2026-08-20 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| e30e786a-3b28-3257-aec0-96c37b6b4dc1 | -6.4392 | -52.7138 | 2026-08-20 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 51192ffc-2c3e-31dc-baaa-d15035b192df | -6.8593 | -59.0318 | 2026-08-20 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 40ccbdc3-66f0-3270-a0ea-a011b2671a7f | -17.3365 | -43.6383 | 2026-08-20 00:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 95.3 |
| ab5baa70-4ea8-369b-b0db-14e957e5ce7d | -7.9563 | -44.6667 | 2026-08-20 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 555f786d-3fe3-30a4-97b0-f184d7b1e892 | -7.36 | -45.8361 | 2026-08-20 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 341.8 |
| a681103f-2215-30cf-916e-9bab6c82fc72 | -10.4513 | -54.6565 | 2026-08-20 00:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 45f7abc3-c0af-3d4b-a1a4-f7454a3b46cf | -6.6939 | -58.9226 | 2026-08-20 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 87834feb-9941-3866-9cc7-dfae539870cf | -6.3863 | -54.9451 | 2026-08-20 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| d8efb2b3-7918-3557-a27f-41a207f41f28 | -8.6913 | -54.648 | 2026-08-20 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| c1b53454-e5fa-323a-b1da-e9f85e88d938 | -14.4559 | -45.6019 | 2026-08-20 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| c658d912-0a8c-316e-ad80-2bb9658a3774 | -11.1939 | -53.9993 | 2026-08-20 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| c1bec27b-3069-375b-b4e2-cffd89135af9 | -9.12 | -51.1534 | 2026-08-20 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| e9c8ae14-bbc5-3dcc-9603-59a4a2f41487 | -6.7123 | -58.9412 | 2026-08-20 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1fd85542-7003-3dad-8ec1-c6645fc26763 | -9.1203 | -51.1323 | 2026-08-20 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 2328e268-e8e9-3a69-bec7-4613a140b8c8 | -6.6014 | -58.9844 | 2026-08-20 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| ef79fa72-56e2-389f-a483-3ff05a3d9a92 | -6.6938 | -58.942 | 2026-08-20 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 424d4548-1fa7-3377-b133-2b2481e5bac7 | -6.6937 | -58.9613 | 2026-08-20 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 043e309d-8ae3-39cf-9b8a-747adfc9401a | -14.4559 | -45.6019 | 2026-08-20 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 4d1ae6fa-cf31-350a-9c39-202a75a719ce | -11.8083 | -44.8072 | 2026-08-20 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 0fcfc1d2-38b8-3382-b1f0-4d09087a2617 | -8.6725 | -54.6695 | 2026-08-20 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 8c4606a5-1bcb-3fff-830b-f5073a1c4d62 | -6.6937 | -58.9613 | 2026-08-20 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 4709b56d-046c-3911-94d1-1e6fbdfa6a72 | -6.3863 | -54.9451 | 2026-08-20 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 733684e6-cf96-3d18-aa73-38c32c02cec4 | -6.7124 | -58.9219 | 2026-08-20 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 8213f0b0-4d0c-36d4-88ae-419edd1c5424 | -17.3372 | -43.6139 | 2026-08-20 00:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 203.1 |
| cb60b3d6-38e5-3daa-b892-d67d85519325 | -8.5214 | -54.8814 | 2026-08-20 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 8ff92e97-eb60-3e74-9b71-66b6037b73b4 | -11.2189 | -55.0585 | 2026-08-20 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| d7e1423c-6d9f-3059-8007-835ac4140bc2 | -6.7123 | -58.9412 | 2026-08-20 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 76fe61d6-c33d-30bd-9f0d-5a20cb1f6c72 | -2.5629 | -47.2445 | 2026-08-20 00:10:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 45594f50-ed4a-3033-a7cf-84334a348e31 | -6.6939 | -58.9226 | 2026-08-20 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 90f5f893-026f-3cd6-a420-8fba4c7e04ab | -5.7903 | -55.7301 | 2026-08-20 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ed2ededf-198b-3f8b-ac57-432dbca26afa | -6.6015 | -58.9651 | 2026-08-20 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 29e9f2b1-04af-38dd-8452-121fd83407a8 | -7.3415 | -45.8152 | 2026-08-20 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 2c9fd2a1-b565-36fa-8a2c-b0a0f5566edd | -5.8088 | -55.7095 | 2026-08-20 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| facad526-1836-362a-94ee-7289a1616ec9 | -14.4554 | -45.6251 | 2026-08-20 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 13c89b7e-9f4b-3d01-a1a6-70c4c1e17302 | -2.5814 | -47.2439 | 2026-08-20 00:10:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b4bef285-95b4-3521-bdd9-9c8298e92408 | -6.5829 | -58.9851 | 2026-08-20 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 3a456a7f-078e-3529-a11e-c8657689d638 | -9.207 | -59.7903 | 2026-08-20 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| baa02566-5a00-33b6-90d5-f46c6ea060a0 | -6.9129 | -59.3385 | 2026-08-20 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 060ae82f-fd68-3384-bfcf-2433f7cf1185 | -1.8242 | -54.492 | 2026-08-20 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| b7b13b48-fe92-3e26-a11d-36cfd5e1abd4 | -5.7904 | -55.7103 | 2026-08-20 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 62d46e6b-01f1-3682-9339-4e3c7370fccb | -8.654 | -54.6505 | 2026-08-20 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| d9d0434d-f383-3737-935f-b11ee58be1d9 | -11.1936 | -54.0199 | 2026-08-20 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 005ba75d-809b-350d-b160-747da3318d42 | -5.8087 | -55.7293 | 2026-08-20 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b14abe32-3824-38e3-b9a9-d82ec751dba8 | -6.4391 | -52.7343 | 2026-08-20 00:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| e7cfab99-66e0-372f-9f75-2625f86d1540 | -8.6729 | -54.629 | 2026-08-20 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| f44710f7-eb62-33b5-84fe-7e7b4a78d567 | -7.9751 | -44.6648 | 2026-08-20 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 0cb15895-2831-3c96-b103-42ae2d046546 | -6.6938 | -58.942 | 2026-08-20 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 7d805a8e-5f38-3cb4-aaa6-d9285c35322d | -7.3603 | -45.8136 | 2026-08-20 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 232.3 |
| 48a8bbe9-a0b2-3d66-841e-e61a5df474b6 | -12.4916 | -54.7364 | 2026-08-20 00:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |


[Clique aqui para ver as próximas entradas](README2.md)
