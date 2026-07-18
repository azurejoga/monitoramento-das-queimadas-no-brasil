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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07254ee1-ad31-3902-b78f-c48c1527959d | -13.3023 | -45.1511 | 2026-07-18 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| d6355548-736b-3795-b962-148a09c86047 | -13.3217 | -45.1479 | 2026-07-18 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 07fad5da-f8a3-31d2-a37e-97e5ce9da286 | -13.3023 | -45.1511 | 2026-07-18 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| b68ebae0-24e8-3e3e-b7d7-58ae265e1e28 | -18.7364 | -54.1988 | 2026-07-18 02:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 97173abd-9083-3384-9344-bc0fa1319479 | -13.3023 | -45.1511 | 2026-07-18 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 6ee473c2-25a3-3ce9-92e2-b48deaae18f9 | -13.3217 | -45.1479 | 2026-07-18 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 189.2 |
| b09b5a19-3271-341b-92db-5d9c180a0fcb | -18.7364 | -54.1988 | 2026-07-18 02:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 475540ff-e7a9-36e4-ac42-9536b4d440d5 | -18.7364 | -54.1988 | 2026-07-18 02:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 90.1 |
| ea251db2-7276-38aa-8ff9-efc22c2af31e | -13.3221 | -45.1246 | 2026-07-18 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| a85972a1-55a1-3a97-b0af-15787ce8f063 | -13.3217 | -45.1479 | 2026-07-18 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| ed90eb1c-4de1-3414-ab23-4407e5f66e81 | -13.3023 | -45.1511 | 2026-07-18 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| cc7121aa-db64-3cbd-b16c-a8b3243f31bb | -13.3023 | -45.1511 | 2026-07-18 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 039eff17-a84a-3c93-8b81-8697e3650e1b | -13.3217 | -45.1479 | 2026-07-18 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 5258416e-9d9f-3700-935d-9c7f54626511 | -13.3221 | -45.1246 | 2026-07-18 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 80c8f1f7-6e13-3ca5-a971-6bd8cffbb3d0 | -18.7364 | -54.1988 | 2026-07-18 03:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 34bf7913-193b-30a0-9b08-541cb9ffc272 | -13.3023 | -45.1511 | 2026-07-18 03:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| b6fd2ad4-3ae8-31c1-aa88-c7bca394284a | -18.7364 | -54.1988 | 2026-07-18 03:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 29b0739b-3dd5-353e-a8b3-cb428817fef3 | -13.3221 | -45.1246 | 2026-07-18 03:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| eeca02a3-5306-37ec-9c18-f589a7177137 | -13.3217 | -45.1479 | 2026-07-18 03:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 168.7 |
| d3840502-084e-3ec6-9bc5-7dc6574ab377 | -13.3221 | -45.1246 | 2026-07-18 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 79adfe21-80ce-32f0-992e-fff9e099119a | -18.7364 | -54.1988 | 2026-07-18 03:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 74.7 |
| f8c9d030-7db5-3197-b18d-d24af36c4805 | -13.3217 | -45.1479 | 2026-07-18 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 202.9 |
| d7e04f28-5664-33f5-8565-a51b8fc8f144 | -13.3023 | -45.1511 | 2026-07-18 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| ff6c58bf-4a3b-3335-ae0b-ca6cf4447e36 | -13.3217 | -45.1479 | 2026-07-18 03:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 8412da79-aded-36f1-88c0-3599d92d487d | -18.7364 | -54.1988 | 2026-07-18 03:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 989ad1d2-4176-3e9b-9403-a39cbad7fa15 | -13.3023 | -45.1511 | 2026-07-18 03:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 1caa62c0-a1b3-32e9-89d5-883810d1a30f | -13.3221 | -45.1246 | 2026-07-18 03:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| f08c0bb9-99ae-34d4-baa4-98925bed98ac | -18.7364 | -54.1988 | 2026-07-18 03:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 638d6218-4da0-314d-b8aa-8c00337071cc | -13.3217 | -45.1479 | 2026-07-18 03:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| aa4d411f-6ae5-35f0-b57b-0160133e8fe2 | -13.3023 | -45.1511 | 2026-07-18 03:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| e3263e46-dbad-3274-b8ec-ec75719a6359 | -5.92772 | -43.64174 | 2026-07-18 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d959ee98-5aed-37b3-98ac-ade11a9a5c6f | -5.12248 | -43.23207 | 2026-07-18 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8543d21c-1af1-3d05-aebc-b737d61b29c4 | -6.06084 | -39.65418 | 2026-07-18 03:42:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 001a83cc-1fac-36a4-90ae-624f26114afe | -4.83033 | -44.0647 | 2026-07-18 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 56566bbc-5653-3828-bbe2-1362698bb787 | -5.12197 | -43.23506 | 2026-07-18 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4dc2e7db-0593-3815-a760-42f9a4df668b | -5.53053 | -45.27169 | 2026-07-18 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 228d5ead-1ddc-3b41-80fe-0f069b784989 | -4.8309 | -44.06129 | 2026-07-18 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8148bc4f-c433-35e2-b33a-94b3efce6b83 | -5.92666 | -43.64791 | 2026-07-18 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1a7eb3c-780f-3e61-9e13-5b6e4c2a8fa8 | -5.92718 | -43.64488 | 2026-07-18 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e58b2234-4089-3cea-b348-73d99959dc48 | -5.89575 | -46.21247 | 2026-07-18 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b28ce778-2278-3a61-a6d9-2a5fe194b137 | -5.89653 | -46.20815 | 2026-07-18 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7015e2d2-8f81-34d4-b8b9-688e0bc6ce0d | -3.02057 | -40.31837 | 2026-07-18 03:42:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 84af6ed9-ae76-33f9-984e-83f01f955730 | -5.12146 | -43.23805 | 2026-07-18 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c1ffbc7-ea3d-3221-b797-146ee3acad85 | -4.8331 | -44.06551 | 2026-07-18 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04729901-8e60-3728-9a2f-13d536babef2 | -5.59674 | -45.33954 | 2026-07-18 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50fc6dd5-aa10-3afb-8d04-93e79c1acc98 | -4.82833 | -44.0612 | 2026-07-18 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 155edffa-6cc2-3328-9bac-847b77ec3318 | -5.71322 | -45.6628 | 2026-07-18 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be2b1aaf-21ac-363e-a529-b2ad6375b440 | -4.83369 | -44.06211 | 2026-07-18 03:42:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8b88274-c2f5-3235-8b49-a0f912dae50d | -5.52476 | -45.27094 | 2026-07-18 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a630138b-6363-30a3-9de1-58f7de15af57 | -13.55426 | -47.78387 | 2026-07-18 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1309d985-6560-3145-a771-1c89886133c1 | -11.79422 | -45.9338 | 2026-07-18 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1346f56-5ef7-30f2-a3f0-d9ee30dfeaa8 | -8.93987 | -47.61466 | 2026-07-18 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddecd5e1-0e17-35da-9c4a-00c8ae6e5280 | -10.4783 | -42.47831 | 2026-07-18 03:45:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 657a9049-6877-38ef-b36f-1b3f38b94a2c | -11.54911 | -48.25992 | 2026-07-18 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 50447459-9ffe-3f43-8a80-e1a9d274d1ea | -10.53072 | -48.15836 | 2026-07-18 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bc92b01d-b861-3a27-b704-834e65678c2d | -10.53387 | -48.15613 | 2026-07-18 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5ae2c30b-9233-395a-9531-36aa8673fcfd | -13.31852 | -45.14927 | 2026-07-18 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f469c36b-f00d-300e-8aba-5a026386cc37 | -9.48763 | -46.6588 | 2026-07-18 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4af61d8d-426f-34a0-a526-65e427616cfb | -10.53283 | -48.16131 | 2026-07-18 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c36ce7d0-148a-329d-be0d-0f299c93729a | -8.94328 | -47.61517 | 2026-07-18 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b016f3d2-18fb-32d3-a181-f6daac7bb6e5 | -10.64718 | -47.23625 | 2026-07-18 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03d9a2eb-8ffd-3921-91d2-860ab42ebc79 | -12.50831 | -48.25731 | 2026-07-18 03:45:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a78c4cb8-afe2-3e30-b3f5-5b4667094016 | -10.52755 | -48.15498 | 2026-07-18 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41891df0-0202-306d-a054-c9a169256d46 | -10.64808 | -47.23165 | 2026-07-18 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10d60093-892c-347c-8baa-710df2b4e089 | -8.94613 | -47.61592 | 2026-07-18 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f41b1d4-6dcb-331a-86cc-06e8a085304a | -7.91763 | -48.25991 | 2026-07-18 03:45:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a2dec15-5cc5-3e7c-aa90-d3150b9d68d2 | -8.12693 | -47.87565 | 2026-07-18 03:45:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c253f9f6-83d6-3a89-aefc-e787c5a71c55 | -13.31686 | -45.15789 | 2026-07-18 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0c2d7361-ac90-3f12-a69d-6ad6eb4343b2 | -8.12801 | -47.87005 | 2026-07-18 03:45:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a274f881-5b13-33ac-9bca-65f38c5a4ce8 | -10.47754 | -42.48264 | 2026-07-18 03:45:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bd7086dd-abaa-3c28-a74d-6ef090b30fb8 | -13.31245 | -45.154 | 2026-07-18 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| be1b806f-005f-313b-a8ec-115b45594806 | -7.48172 | -46.67263 | 2026-07-18 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4ca8417-7489-38e4-965d-b340ea309b25 | -13.31741 | -45.15499 | 2026-07-18 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e0889b0f-b807-37a5-9e72-5a53c54e18db | -12.6894 | -48.21131 | 2026-07-18 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 780fa154-7bae-368d-9f1b-cf44cd8cd0e7 | -7.48364 | -46.668 | 2026-07-18 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d64774ac-688f-30ab-9ee2-fe866b065e5c | -8.95053 | -47.61127 | 2026-07-18 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c1834d2-234a-38de-8dcf-b07b98b1004c | -9.69983 | -47.70141 | 2026-07-18 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1f60daca-f25b-306e-9968-c194f382194e | -11.07877 | -40.21389 | 2026-07-18 03:45:00 | NOAA-21 | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aa4bb62d-184b-37e2-a7d9-f342510aff1b | -9.48682 | -46.66308 | 2026-07-18 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b970d944-31ad-3aed-ac12-f3f3b46c2f09 | -13.31797 | -45.15212 | 2026-07-18 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c423a19c-e04e-3369-a6d1-93bbdab89b13 | -9.48843 | -46.65454 | 2026-07-18 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abeb5962-d9b5-3af5-88a0-dbe9457c3070 | -7.29198 | -46.25982 | 2026-07-18 03:45:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bea3238-2f58-318e-b01c-dd5b0041ee28 | -7.91388 | -48.25764 | 2026-07-18 03:45:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 60cf5f4e-aa75-3f50-9933-99ad20a73706 | -9.53216 | -47.12304 | 2026-07-18 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c83c2f0f-ae95-39a6-91b3-04bf002997df | -8.12677 | -47.87399 | 2026-07-18 03:45:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fdd2697c-4533-3b39-ad7b-088f4563f1d4 | -7.28608 | -46.25856 | 2026-07-18 03:45:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 385081df-795a-39d3-bba8-d5596a3475dd | -7.28689 | -46.25417 | 2026-07-18 03:45:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07558afc-3038-39f3-9654-0d5b68421beb | -13.31412 | -45.14536 | 2026-07-18 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 6bc17d53-91ad-3537-8a15-8fc2f554ac03 | -8.94081 | -47.6096 | 2026-07-18 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dbb851a7-f6e2-3e91-99e2-e8f925d34669 | -7.85261 | -48.39864 | 2026-07-18 03:45:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3cfce16-456a-3d13-87da-23dfc660905b | -7.48258 | -46.6679 | 2026-07-18 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 790ff1dc-7a7a-351b-ba2a-63998d0a8eb9 | -12.38836 | -43.896 | 2026-07-18 03:45:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fc58c03-27aa-3f1d-8561-7d16af136825 | -9.99772 | -43.43305 | 2026-07-18 03:45:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9542749-4ead-3165-b311-c7775c86907b | -8.94426 | -47.61009 | 2026-07-18 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4339ec53-9650-3529-b1f9-8c850c678d0b | -11.5481 | -48.26496 | 2026-07-18 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f89b076c-3564-3bfa-a2eb-42f140cd776c | -12.50216 | -48.25611 | 2026-07-18 03:45:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e883bff-bc25-344d-aadf-1770a8f3d4de | -9.52613 | -47.12185 | 2026-07-18 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 89952e13-001b-325e-b124-014b7191554c | -12.68329 | -48.21009 | 2026-07-18 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c280db02-e5dc-34b1-be46-9e1b9a35b79f | -13.55999 | -47.78565 | 2026-07-18 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9810884a-14d4-38c6-9557-8c57cfa29895 | -13.55071 | -47.77824 | 2026-07-18 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README5.md)
