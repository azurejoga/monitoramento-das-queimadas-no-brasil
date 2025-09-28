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
| 35689aeb-3111-31c5-bb81-d26eb8c63751 | -18.0249 | -51.1811 | 2025-09-28 00:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 5118f7bb-b923-33b1-b8b8-9d151d330847 | -7.0315 | -40.0237 | 2025-09-28 00:30:00 | GOES-19 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 80.4 |
| c3d24a68-6aa8-3ce5-8155-b48205401835 | -11.0083 | -57.0658 | 2025-09-28 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| d81dd888-4f2f-3923-9bae-7db34bfce41e | -18.0453 | -51.1556 | 2025-09-28 00:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 488.5 |
| 8ff9a386-0cfc-35db-9da5-317feae864e7 | -7.3659 | -47.0394 | 2025-09-28 00:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 91e3fe85-0e97-3f54-a433-3bff33a276e9 | -14.7856 | -45.6586 | 2025-09-28 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 203.3 |
| ba0dca79-3067-3667-a058-a04aad80e0a0 | -7.3847 | -47.0378 | 2025-09-28 00:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 976be9db-f133-382e-b0ff-0f2877a50f5b | -9.6512 | -62.8336 | 2025-09-28 00:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 82.4 |
| e7113456-b401-3acc-9109-570d01c21e82 | -18.1977 | -53.3208 | 2025-09-28 00:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 179.7 |
| b592bd2b-3e82-3670-9467-5af47b3afb2a | -14.7851 | -45.6818 | 2025-09-28 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| ed71f242-850b-3605-b954-cd4a9c1a03d9 | -12.9918 | -49.4448 | 2025-09-28 00:30:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| d2689479-ea73-3c0f-b44a-04177a1895a7 | -10.9894 | -57.0672 | 2025-09-28 00:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| e068f22c-7fd5-3893-8283-8488a79a9bf1 | -14.766 | -45.6621 | 2025-09-28 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 56ad64f8-9404-32aa-a78d-561d5b23b6ae | -11.9989 | -47.0371 | 2025-09-28 00:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| b51c20d7-8f02-3810-bcb0-33e98997634b | -6.4419 | -43.9317 | 2025-09-28 00:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 500761ab-298c-3a6f-b838-00121e9340fe | -16.9667 | -53.6975 | 2025-09-28 00:30:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 306c9993-69e3-3cbe-8b02-1e16e36007fb | -18.0653 | -51.1522 | 2025-09-28 00:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 0a05235a-082b-37ab-abe6-00774c5b8e5d | -5.8149 | -42.8167 | 2025-09-28 00:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| 8157868d-3384-3bba-9ab5-0a75cd11de22 | -7.0126 | -40.0257 | 2025-09-28 00:30:00 | GOES-19 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 10181137-691e-39f6-a69c-bbdc69b432d0 | -13.011 | -49.4423 | 2025-09-28 00:30:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| fe96a6fa-1b48-395a-83f7-3f181465cc8c | -14.7861 | -45.6353 | 2025-09-28 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 4e58657b-b381-3008-a148-242eab720d66 | -8.483 | -47.7983 | 2025-09-28 00:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 02fd7fb6-3876-3189-bebb-f2aafbdaaa5b | -7.0129 | -40.0009 | 2025-09-28 00:30:00 | GOES-19 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 41.0 |
| 142e5152-c91f-3784-bb1c-7db241a43ef7 | -9.6511 | -62.8526 | 2025-09-28 00:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 962bb0ee-0e48-3b0f-9d42-9ecc706a2c56 | -3.7381 | -49.4445 | 2025-09-28 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 9cd7326a-5a75-3c97-b1da-952355eb3ef0 | -7.8538 | -43.7995 | 2025-09-28 00:30:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 10b417fa-fb16-35d1-8597-e760863a5c59 | -13.0106 | -49.4641 | 2025-09-28 00:30:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| a0a9ea2a-f842-36af-ac34-e82ecaffb1f9 | -18.0254 | -51.1591 | 2025-09-28 00:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 123.6 |
| b000831a-c969-3f52-87fd-3635e434d64e | -14.766 | -45.6621 | 2025-09-28 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 0fb6afe2-06d6-3cb0-b679-832a1681196b | -9.6511 | -62.8526 | 2025-09-28 00:40:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 87.3 |
| a223f5a7-6a2d-3088-bc78-7cbb0ca1222a | -16.9667 | -53.6975 | 2025-09-28 00:40:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| d1c7e6bd-9b2b-35a8-970f-6859bf4cf461 | -18.0653 | -51.1522 | 2025-09-28 00:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 05ab1127-89a3-3a02-bb16-80bbb715bc33 | -18.1977 | -53.3208 | 2025-09-28 00:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 56f0e5a3-c06b-33ba-879e-0b20f158c555 | -18.0249 | -51.1811 | 2025-09-28 00:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 007810e7-d22b-370e-844b-7d7b694bcb03 | -7.7785 | -47.0258 | 2025-09-28 00:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 10ec209e-7302-3115-916e-56471e11b5b7 | -11.3889 | -46.9847 | 2025-09-28 00:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 14586c90-184a-357f-95e0-7b27f540eef2 | -7.0126 | -40.0257 | 2025-09-28 00:40:00 | GOES-19 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 37.4 |
| b4b6967b-66f9-36c2-9db9-628704b219a5 | -7.7972 | -47.0241 | 2025-09-28 00:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| cb8da9df-43fa-368f-8202-c674014ce7b0 | -15.537 | -47.9024 | 2025-09-28 00:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 6cc0e71b-e57d-32fc-9825-0fd81dd7172f | -12.6917 | -46.8708 | 2025-09-28 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 2e1789e0-30f5-3734-9b31-5d45fe57fbb6 | -9.6512 | -62.8336 | 2025-09-28 00:40:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 88.5 |
| c16eaf30-b31d-39a1-9520-df07642cbc95 | -18.0453 | -51.1556 | 2025-09-28 00:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 386.0 |
| 4eb86874-42c1-35d2-af73-0b193249983b | -12.9918 | -49.4448 | 2025-09-28 00:40:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| b8522064-920c-357f-859d-6806c393f77c | -7.7599 | -47.0053 | 2025-09-28 00:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 951813fc-cd09-3974-9a09-f43ae483f3a8 | -7.7975 | -47.0019 | 2025-09-28 00:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 54977139-4f44-3139-9aee-418bd12a5fdd | -11.9846 | -47.8865 | 2025-09-28 00:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 24ca8955-c29b-305f-bee0-8e34685ef1b2 | -14.7856 | -45.6586 | 2025-09-28 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 543324d5-270d-3c2c-ae81-c22f30e5ff80 | -18.0448 | -51.1777 | 2025-09-28 00:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 1c41ce76-38f0-32e2-98c5-d02225dd23c0 | -13.0106 | -49.4641 | 2025-09-28 00:40:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| e6fa756d-a008-36be-8d99-e88a3c8a5786 | -7.7412 | -47.007 | 2025-09-28 00:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 657ba2c1-b722-3749-963e-ca0b1bf277a9 | -7.3847 | -47.0378 | 2025-09-28 00:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| c6784d5c-2cbc-3f68-ba7a-23408e7d4e42 | -7.7977 | -46.9798 | 2025-09-28 00:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 34b2ce54-18be-3636-b402-5ab936dca9fc | -13.011 | -49.4423 | 2025-09-28 00:40:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| c9791fbe-95fa-375c-a662-95cce5e96806 | -14.7861 | -45.6353 | 2025-09-28 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 6c5ee70b-49e0-3680-b540-fec6fcfd87b2 | -14.7655 | -45.6854 | 2025-09-28 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 82255f55-a9fe-3b58-8a18-3827d6984613 | -5.8149 | -42.8167 | 2025-09-28 00:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| bcad1243-e57d-3250-9fb3-57fbb45680be | -6.4419 | -43.9317 | 2025-09-28 00:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 0d89af04-d08b-3964-b96a-6887b5cb0327 | -11.0083 | -57.0658 | 2025-09-28 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| f38b755c-0f8b-3818-8dbc-ed04e7eba34f | -14.7851 | -45.6818 | 2025-09-28 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| dee14638-b766-3911-a5ea-07a9fcb81960 | -7.7787 | -47.0036 | 2025-09-28 00:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| e573d7e3-ef00-3984-9ab7-890de06fc34c | -18.2176 | -53.3177 | 2025-09-28 00:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 77.6 |
| a847cbb7-cbb5-31ab-a061-353d71a9fac6 | -10.9894 | -57.0672 | 2025-09-28 00:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 08e2a252-d944-3f0c-9819-ac146e97e8cc | -18.0254 | -51.1591 | 2025-09-28 00:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 261.0 |
| d865393c-fa64-3747-ba0c-fce5a9711623 | -8.483 | -47.7983 | 2025-09-28 00:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| a67982fe-96bb-37a9-9975-b6deed7e4c46 | -25.15348 | -51.97207 | 2025-09-28 00:48:00 | TERRA_M-M | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 8c8c97cc-2b26-34ad-b196-fc8ccc9bb11f | -16.9667 | -53.6975 | 2025-09-28 00:50:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 54494376-3076-35f6-b59d-a28097ba6137 | -9.6512 | -62.8336 | 2025-09-28 00:50:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 104.9 |
| f475f045-6658-3fab-a062-5ae7307fff92 | -18.0254 | -51.1591 | 2025-09-28 00:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 7bbda200-5185-3f30-a4e8-6d29968e1062 | -9.0766 | -45.5519 | 2025-09-28 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 7071a205-7650-307a-95b3-10e60873ea25 | -13.011 | -49.4423 | 2025-09-28 00:50:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| b3c86d0b-62e2-322c-a5ba-3ef512c1015b | -14.7655 | -45.6854 | 2025-09-28 00:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| fd21556d-100b-3845-ac1e-c2e748567a2b | -7.7972 | -47.0241 | 2025-09-28 00:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 9327ac8a-43b6-3ccb-950f-4229baabab54 | -18.0458 | -51.1336 | 2025-09-28 00:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 0f6df952-b5da-3182-93b8-4af8b76189d6 | -11.9989 | -47.0371 | 2025-09-28 00:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| cf34a303-6e13-3943-b69d-54c57b58c1f4 | -7.3847 | -47.0378 | 2025-09-28 00:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 9db62cd1-8376-3e10-aca2-761ef6ff94ff | -18.0448 | -51.1777 | 2025-09-28 00:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 275.7 |
| 2185f7c1-fb81-3a09-b326-9a43fc50a66f | -5.8149 | -42.8167 | 2025-09-28 00:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| c6d234f7-988a-33c1-b703-868f1e9d3479 | -7.7412 | -47.007 | 2025-09-28 00:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 92ece046-aecc-3607-893f-830270367f2e | -11.9846 | -47.8865 | 2025-09-28 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| a6c4e92c-3408-3883-a1a7-aebaaa88d5b7 | -7.7785 | -47.0258 | 2025-09-28 00:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 9135d9bb-ed96-33f9-a17e-3492cf00ded8 | -12.9804 | -46.8504 | 2025-09-28 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| beb76c1d-4c1b-37a5-8cc3-a82b61c7bd12 | -13.0106 | -49.4641 | 2025-09-28 00:50:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| de2389a2-828a-3780-a23f-5514698ee2ba | -18.1977 | -53.3208 | 2025-09-28 00:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 9fd75343-098a-3b9f-aec5-f1220768485f | -18.0453 | -51.1556 | 2025-09-28 00:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 452.2 |
| 04db2b3d-06c4-3023-ad98-4d1bd282b520 | -14.7856 | -45.6586 | 2025-09-28 00:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 227.6 |
| b9136a3a-373b-3530-b6c6-240a1cf1a175 | -18.0249 | -51.1811 | 2025-09-28 00:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 22ceee8e-c66f-32f2-b19e-4ce1845a0741 | -9.077 | -45.5292 | 2025-09-28 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 282.3 |
| c8080b0c-fd98-3dc2-8b28-76a22f3420fb | -14.7665 | -45.6388 | 2025-09-28 00:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| b62cd9ba-d8d6-399f-8700-f32420397dcf | -7.7599 | -47.0053 | 2025-09-28 00:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| bc1b5759-74db-36dd-b181-e16c6b643cce | -2.5772 | -48.4146 | 2025-09-28 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| e912335d-e5fd-3514-b0bb-f3a6a9479d46 | -14.7851 | -45.6818 | 2025-09-28 00:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| bb6a7c0e-bd38-368d-af5b-cc30b6cafcd8 | -5.7396 | -42.8461 | 2025-09-28 00:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 645c6350-8515-3599-a439-9f845e9fa555 | -12.9918 | -49.4448 | 2025-09-28 00:50:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| d03d212b-3b4d-3374-a78d-d6232668a774 | -9.0773 | -45.5064 | 2025-09-28 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 7abadb13-844c-3b34-8dbf-8943ab5c1a99 | -14.766 | -45.6621 | 2025-09-28 00:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 196.7 |
| 045b3434-5bcd-324f-92e6-c8ae74e5aa77 | -9.6511 | -62.8526 | 2025-09-28 00:50:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 930d92b1-8a26-34fa-bb4b-37a065639acb | -10.9894 | -57.0672 | 2025-09-28 00:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 114f1f6d-3519-3e11-96fd-0946d54b14b9 | -14.7861 | -45.6353 | 2025-09-28 00:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 8107df94-6b94-399d-89ee-558da372d048 | -17.7338 | -46.7056 | 2025-09-28 00:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 788d7bf6-b6e2-34b2-be7e-8fd83e2b6e38 | -8.483 | -47.7983 | 2025-09-28 00:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |


[Clique aqui para ver as próximas entradas](README3.md)
