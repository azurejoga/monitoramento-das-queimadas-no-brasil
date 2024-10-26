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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9feb07b2-643a-3aa3-9e42-8780133ace92 | -4.5614 | -48.0141 | 2024-10-26 01:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 9db9287e-00cf-35d5-8936-2608e6f322a7 | -4.5799 | -48.0349 | 2024-10-26 01:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 232.0 |
| b5a0ddbe-f277-3ef2-a39f-f0eb07f3bcda | -4.58 | -48.0132 | 2024-10-26 01:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 192.8 |
| e636438a-a2b6-398a-b58f-bfc51d58f3e0 | -7.6474 | -63.4584 | 2024-10-26 01:35:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 38f9d668-fa8e-3565-94b2-8d42108391e8 | -7.6475 | -63.4396 | 2024-10-26 01:35:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 952d70f4-65c0-3a03-b981-b0dc82692733 | -7.6659 | -63.4578 | 2024-10-26 01:35:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 45cd0f94-7035-3357-99e6-837e8d7f27bc | -9.4996 | -47.8068 | 2024-10-26 01:35:59 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| c100a318-ceec-3821-ab04-67e51e20650e | -16.9204 | -57.5291 | 2024-10-26 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.2 |
| d89f7ffe-8290-3e57-bdbd-f88e94f7956d | -16.9207 | -57.5086 | 2024-10-26 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.1 |
| 2f98eb66-1f81-34c7-a616-5c1d51f1cc2d | -17.0499 | -53.452 | 2024-10-26 01:36:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| f47c37db-b712-3507-8961-3a7f2183c003 | -17.1987 | -57.2714 | 2024-10-26 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.2 |
| 6bfa3b3d-b511-344e-b7c2-fd42a979f228 | -17.219 | -57.228 | 2024-10-26 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.9 |
| 904d22cd-f484-3992-abb8-4cedc25004c9 | -17.239 | -57.2051 | 2024-10-26 01:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 33c3bfce-7a73-3902-aea2-0b8005bb1c7a | -17.8226 | -57.5866 | 2024-10-26 01:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.8 |
| 46a0a8f7-6a5a-3679-9b84-0e57e9f04a62 | -17.6667 | -57.4822 | 2024-10-26 01:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 54223517-494f-3cc9-b3dc-c910e5ee101a | -17.6861 | -57.5004 | 2024-10-26 01:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.1 |
| e435f618-7f77-3cbd-ab13-38be463436fa | -17.6865 | -57.4798 | 2024-10-26 01:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.9 |
| a6e61dbc-1a99-33c0-a860-8b58853038e0 | -17.744 | -57.5756 | 2024-10-26 01:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.1 |
| 2fe2245a-3a51-3c23-a62c-e182ce48dc35 | -17.7443 | -57.555 | 2024-10-26 01:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.8 |
| f0e0d311-3039-3121-9d35-85cb15a43eaf | -17.7446 | -57.5344 | 2024-10-26 01:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 46148079-294b-3569-9c73-5102617c1234 | -17.745 | -57.5138 | 2024-10-26 01:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.0 |
| 2a59b40c-fb51-39ba-910d-caef6d263b73 | -17.7647 | -57.5115 | 2024-10-26 01:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 40075453-20b8-3324-94c7-0bc31f492e20 | -17.7831 | -57.5914 | 2024-10-26 01:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 3a93b299-ccd1-3286-bd86-cc8be03049a0 | -17.7868 | -57.3649 | 2024-10-26 01:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.1 |
| 923d69ce-9042-3fa5-9c9f-6b46bbad7815 | -17.842 | -57.6048 | 2024-10-26 01:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.5 |
| a300aa25-9093-3c61-bf4f-5e96bf662077 | -18.0827 | -57.3696 | 2024-10-26 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 462da2c0-dc26-3659-9094-1782512059ec | -18.245 | -56.0002 | 2024-10-26 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.0 |
| f1417d1f-a2b1-3447-9ab1-f05f2c6bb745 | -18.2645 | -56.0184 | 2024-10-26 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.8 |
| 1df46aa7-37e5-3e53-a3fd-d1c772e02f36 | -18.2649 | -55.9975 | 2024-10-26 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 09b358c2-2c23-35bb-9f1a-ae03b2fffb46 | -19.4866 | -56.6857 | 2024-10-26 01:36:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 71eba77f-67ed-3597-86cf-547268c2ca53 | -19.5067 | -56.6829 | 2024-10-26 01:36:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.7 |
| cb57d916-95f4-3fc5-bdb9-3ad906114111 | -19.526 | -56.7221 | 2024-10-26 01:36:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.1 |
| 84ac627f-14ca-3328-a370-b099b99db315 | -19.5264 | -56.7011 | 2024-10-26 01:36:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.9 |
| 796ec7e8-ede5-33cb-a27a-d3d93c8939b8 | -19.5461 | -56.7192 | 2024-10-26 01:36:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.9 |
| 7706b36b-097c-350b-99ad-da8b49c02ceb | -19.5465 | -56.6983 | 2024-10-26 01:36:54 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 95.6 |
| de88ea99-7514-3a9e-8b72-f866ec3030dc | -19.5866 | -56.6926 | 2024-10-26 01:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| 21465bbe-ee99-36af-9bdd-3c4b2ac1ca56 | -19.6063 | -56.7108 | 2024-10-26 01:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 3a9e2325-3a57-3e52-8a9f-8ea713eefd30 | -19.6067 | -56.6898 | 2024-10-26 01:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 129.7 |
| 435677f2-5787-3f49-91fd-bf5a06b3b58a | -19.6071 | -56.6688 | 2024-10-26 01:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.1 |
| da644ede-8e76-3010-afe6-3eb6054fa168 | -19.6268 | -56.6869 | 2024-10-26 01:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 103.5 |
| 6b728278-82fd-31cb-b5dc-1cc58a9c2ca1 | -19.6272 | -56.6659 | 2024-10-26 01:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.4 |
| e7d773e0-a73e-3a43-8ad5-2ac5fc0399c7 | -2.1929 | -53.7234 | 2024-10-26 01:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 106f21ba-c632-3144-b741-ac30498bc661 | -2.9501 | -52.5708 | 2024-10-26 01:45:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| c2aab939-74a6-3b58-89f1-881361bab597 | -2.9501 | -52.5504 | 2024-10-26 01:45:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| d7dd7361-81df-3b02-b965-37d8b6a58adf | -2.9944 | -50.5025 | 2024-10-26 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 3c0a4487-e565-3e25-9e8d-d7c262c4117b | -2.9945 | -50.4816 | 2024-10-26 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 165.1 |
| 2b3ccae5-4d7b-3101-af2f-af4654e03b32 | -3.0129 | -50.502 | 2024-10-26 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 48d4b79e-1984-3797-96b7-2c2cba666196 | -3.013 | -50.481 | 2024-10-26 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 198.2 |
| a026dbbf-553a-3c9b-a924-cebc656a4ea3 | -3.0314 | -50.4805 | 2024-10-26 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 4ce07266-f6e4-3371-abf5-71c8967a64f4 | -3.1116 | -53.7234 | 2024-10-26 01:45:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 5f229656-2d84-3e5e-9874-f9130c6a0bd1 | -3.2393 | -45.2918 | 2024-10-26 01:45:23 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 8384b4a4-1547-35ba-acf1-6998fb861860 | -3.2553 | -45.807 | 2024-10-26 01:45:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 3521e6ef-5b1a-3562-b2e7-d6874f7d2709 | -3.4729 | -43.3377 | 2024-10-26 01:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| c5e7f023-28e4-3ccf-a90b-14e41eba2581 | -3.473 | -43.3144 | 2024-10-26 01:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| ea62dc83-8ef6-3536-8730-b82f3714eee5 | -3.4915 | -43.3368 | 2024-10-26 01:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| e9f55c04-55cd-3ac4-afd5-b57c3a02a5b9 | -3.4917 | -43.3136 | 2024-10-26 01:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 5f03e4cb-43aa-33a0-b1fa-a44dd3d1350a | -4.5613 | -48.0358 | 2024-10-26 01:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| a4fedb75-2f55-364b-bcd4-de12f7fbc8c8 | -4.5614 | -48.0141 | 2024-10-26 01:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 8548170d-2164-3b01-94ae-3291d3d4ed09 | -4.5799 | -48.0349 | 2024-10-26 01:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 279.5 |
| 1ebaa7ad-ea4d-3645-823f-fa2d3b07a2be | -4.58 | -48.0132 | 2024-10-26 01:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 260.9 |
| 3a39c63f-30c4-3df6-b7ab-7d886511b05d | -7.6474 | -63.4584 | 2024-10-26 01:45:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| d921e172-4023-340c-b0e9-2a8eacbf33e2 | -10.499 | -36.7749 | 2024-10-26 01:46:03 | GOES-16 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 85.0 |
| 0c269df2-f2d4-3c7e-b313-76e687825484 | -16.9207 | -57.5086 | 2024-10-26 01:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| c7010586-9fa4-3f4c-9a52-d99f8f768559 | -17.219 | -57.228 | 2024-10-26 01:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.6 |
| e2414bfa-490a-33a9-9b37-ee7e90539bf6 | -17.2537 | -57.5108 | 2024-10-26 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.1 |
| fd05e9fd-6bed-3d8f-b152-97602d22d47e | -17.254 | -57.4903 | 2024-10-26 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| fee8e916-36fa-3284-b9b6-1eb9aa707ea6 | -17.2733 | -57.5085 | 2024-10-26 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 86ed4153-d41e-3541-9a32-08d37daff921 | -17.2737 | -57.488 | 2024-10-26 01:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.9 |
| 9dde24bf-4f24-3f04-aeb3-42afe4e53d7f | -17.6667 | -57.4822 | 2024-10-26 01:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| e02d01bb-4960-32df-9e64-840d00331540 | -17.6861 | -57.5004 | 2024-10-26 01:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.9 |
| c95825e1-bbd9-359d-acbe-5980f96a3c67 | -17.6865 | -57.4798 | 2024-10-26 01:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.6 |
| 6bcf1e9f-fb48-3ff4-8d8c-fa8dd3aedf65 | -17.7062 | -57.4774 | 2024-10-26 01:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.0 |
| 0397d52f-722c-367d-8913-99791f94dac2 | -17.7831 | -57.5914 | 2024-10-26 01:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.8 |
| dadabdbc-e130-37b4-97ac-c9d8b1ab4b6b | -17.7868 | -57.3649 | 2024-10-26 01:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.0 |
| f6c48122-2088-3643-8516-f333fd4f40a0 | -17.7872 | -57.3443 | 2024-10-26 01:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.5 |
| e3769c1f-4e2d-303a-839e-b9c3e5d30f17 | -18.2645 | -56.0184 | 2024-10-26 01:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.9 |
| 02b6c7db-2fcc-3746-a580-6eb136c1b87a | -18.2649 | -55.9975 | 2024-10-26 01:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| 4fc2e95d-0eea-32e7-b3d1-eef700b31c80 | -2.1929 | -53.7234 | 2024-10-26 01:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 53631686-f3d2-335d-8731-0d465ba6dc90 | -2.9501 | -52.5708 | 2024-10-26 01:55:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| c168918f-5469-3462-ae5d-cbb94cbf51d5 | -2.9501 | -52.5504 | 2024-10-26 01:55:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 96174173-d0d6-3b6e-a2d5-1b5c8be332bd | -2.9944 | -50.5025 | 2024-10-26 01:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| f5ee320c-5aec-3670-be4f-fc4d4c82ee5c | -2.9945 | -50.4816 | 2024-10-26 01:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 165.4 |
| d8f4cdcc-2031-3076-a3ae-018c457dceb5 | -3.0129 | -50.502 | 2024-10-26 01:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 6d1d3765-3b76-3547-9447-c506561809ec | -3.013 | -50.481 | 2024-10-26 01:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 182.3 |
| e924c216-e86f-3a71-9147-8b4293389cf0 | -3.1116 | -53.7234 | 2024-10-26 01:55:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| d1407794-741a-305e-8727-701b696e7fa1 | -3.4729 | -43.3377 | 2024-10-26 01:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 140.2 |
| bb950f7e-acc0-301e-bf96-5cb5b401bc5d | -3.473 | -43.3144 | 2024-10-26 01:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| a396b936-5036-3d18-9056-9cfc97253736 | -3.4915 | -43.3368 | 2024-10-26 01:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| c30ce736-d259-348a-afca-e36e972e8db6 | -3.4917 | -43.3136 | 2024-10-26 01:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 5cf4c3ee-61ba-311d-ab14-abdf12e38e48 | -4.5613 | -48.0358 | 2024-10-26 01:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| d46ee308-b9d8-38ac-bfdb-7078beae34ac | -4.5614 | -48.0141 | 2024-10-26 01:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 78ca5779-3322-3649-bef3-3cc4c6a6c358 | -4.5799 | -48.0349 | 2024-10-26 01:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 260.7 |
| ca6a4701-9ce9-3448-bac6-ef53453f9088 | -4.58 | -48.0132 | 2024-10-26 01:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 249.2 |
| 94c9c451-7a24-39e8-b808-8dfab84c6548 | -7.6474 | -63.4584 | 2024-10-26 01:55:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c24ad171-8fc1-36ed-98e6-65d2cfbdb822 | -16.9012 | -57.5108 | 2024-10-26 01:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.6 |
| e1e26812-c2b1-3b7b-85f3-fce6d6891cfd | -16.9207 | -57.5086 | 2024-10-26 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| 1a839582-1c6b-34f8-b28f-07eafe8a9049 | -17.254 | -57.4903 | 2024-10-26 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 64ccd482-2c61-36f6-9fae-ead9d8f2af5d | -17.219 | -57.228 | 2024-10-26 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.5 |
| d834f9e4-1b79-39ad-8ab8-1ccfc21152d3 | -17.2537 | -57.5108 | 2024-10-26 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.4 |
| 013fccc2-284b-3c28-8124-19ac19f4ab7f | -17.2733 | -57.5085 | 2024-10-26 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.4 |


[Clique aqui para ver as próximas entradas](README21.md)
