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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2758ffe2-4d2c-35cb-807f-139d284cb8a4 | -8.9831 | -61.72049 | 2025-08-16 02:06:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 144.4 |
| 64f862d6-42cd-3f2d-bc5c-c574651bed35 | -7.67924 | -63.32102 | 2025-08-16 02:06:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 95007a37-b7fc-3ef4-9d37-3483767d1c64 | -8.96046 | -61.68759 | 2025-08-16 02:06:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| c4cf3f9a-b318-3c0c-9ac8-967b9b78ae37 | -14.9632 | -54.7143 | 2025-08-16 02:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 23a1d605-6bf1-347f-a77c-c0e6d0c9f6b3 | -8.9706 | -61.7224 | 2025-08-16 02:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| abf4d2ea-62cf-36b0-94e4-f48b34bd0a0f | -9.1711 | -59.618 | 2025-08-16 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 1c1142db-6ca7-3232-858a-7a8c71e6a973 | -11.2596 | -50.4767 | 2025-08-16 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| e818c79c-b248-3a87-97f6-73aefc406883 | -14.9628 | -54.7351 | 2025-08-16 02:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 110.7 |
| f8ef534e-b8cc-367e-b900-64762cda8f4a | -7.9149 | -61.7288 | 2025-08-16 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 485a298e-8caa-3c92-a272-3289a11269cd | -9.2082 | -59.6354 | 2025-08-16 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| c1bd9854-40b6-3e03-b653-3719f30ae63b | -13.4294 | -43.6733 | 2025-08-16 02:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| a24a2654-afa8-38a8-9467-ff601a460378 | -11.2599 | -50.4553 | 2025-08-16 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| ac1a8135-c995-34cc-afa1-a14af8b72555 | -8.9709 | -61.6842 | 2025-08-16 02:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 91.6 |
| f299a5b8-41b2-37f1-b3f1-c5e6362f51c7 | -14.9435 | -54.7374 | 2025-08-16 02:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 7a6b8292-688b-3d18-ae37-42732ec2d6db | -9.208 | -59.6548 | 2025-08-16 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| f927fac7-a94f-353b-bdb2-465863e06664 | -9.1708 | -59.6568 | 2025-08-16 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 4f0de3b4-8ed3-3784-8012-b4197dd8eeff | -9.4994 | -60.5278 | 2025-08-16 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 7d5b9c8c-7444-314f-bbc3-7692b5bb82a9 | -8.9893 | -61.7024 | 2025-08-16 02:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a755fda6-792d-3aef-92c7-04246c3724ef | -9.518 | -60.5268 | 2025-08-16 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| ce592408-088a-36fd-9acf-08d17273d493 | -14.9441 | -54.6959 | 2025-08-16 02:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 76a36490-5448-38be-bd0c-45b39b7152d3 | -9.1709 | -59.6374 | 2025-08-16 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 0a79c23b-4230-3b31-9af7-f59ff4ee1ec1 | -7.9148 | -61.7478 | 2025-08-16 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 64ad1236-6458-35ac-bd92-15b562a87998 | -9.5179 | -60.5461 | 2025-08-16 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 50b95890-71f1-324a-9a7d-a91c166a5d29 | -6.9487 | -59.5297 | 2025-08-16 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 908337c4-c72f-34aa-bae9-5a5256d46162 | -9.4992 | -60.547 | 2025-08-16 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| ffd49425-bba7-3d1d-9305-860722ce4677 | -6.9486 | -59.549 | 2025-08-16 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 9aaf5b93-45db-3655-84cb-e877e6307af5 | -4.9118 | -43.257 | 2025-08-16 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 1d010085-6fb5-3a54-b869-013fcc509d29 | -7.9333 | -61.7471 | 2025-08-16 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| ee93edbf-ee8c-3aae-9baa-a8cda02aba08 | -14.9438 | -54.7166 | 2025-08-16 02:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 174.9 |
| f808b268-f60f-397a-8b39-d6210200db15 | -8.9708 | -61.7033 | 2025-08-16 02:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 87.8 |
| a44e1170-b811-301a-9bcd-26473a733950 | -11.2406 | -50.4788 | 2025-08-16 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 82da1254-0d6e-31a1-bd76-bbb5e8e84b47 | -11.3466 | -55.4326 | 2025-08-16 02:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 294bbd4b-0cd5-34d7-b16d-594364226bee | -7.9334 | -61.7281 | 2025-08-16 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 5d9c2c28-5bef-3af3-b37a-7972942770c7 | -14.9245 | -54.7189 | 2025-08-16 02:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| bf26b61a-9d11-3072-af26-db2ad216c886 | -6.9302 | -59.5497 | 2025-08-16 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 71b9a1f3-5fba-3ac5-acb2-7938bf054837 | -14.9435 | -54.7374 | 2025-08-16 02:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 33cb0f72-39e8-3b5d-8bca-d88d64056f67 | -13.4294 | -43.6733 | 2025-08-16 02:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| f9bf348e-2e05-3461-ae8e-3180cb0c4339 | -14.5828 | -47.905 | 2025-08-16 02:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 867808ba-9bc2-31bd-9fed-fe71a3edce73 | -9.1709 | -59.6374 | 2025-08-16 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.3 |
| df14cc02-231f-3000-9a9d-c8c656edd26c | -6.9486 | -59.549 | 2025-08-16 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 0865815b-a409-3074-9e48-969f0fa330b5 | -9.4994 | -60.5278 | 2025-08-16 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| e1d75eb6-d9a9-3cfe-a528-6c2cb4687031 | -8.9708 | -61.7033 | 2025-08-16 02:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 2241784a-2d51-3010-8350-2c15ae051b05 | -14.9632 | -54.7143 | 2025-08-16 02:20:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 68a110e4-d49c-3f7a-a140-2b0f7b5b62e1 | -9.4992 | -60.547 | 2025-08-16 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 296d3817-2fd0-3c14-9b04-b179b128eff4 | -7.9334 | -61.7281 | 2025-08-16 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| ed0f6e76-fd7c-314b-8e6d-09fe9ffbcf15 | -6.9487 | -59.5297 | 2025-08-16 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| a140e3a2-ea34-3fef-8544-c6e3504500c1 | -9.5179 | -60.5461 | 2025-08-16 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 031a3e42-533b-37e6-83e1-af31b92902f8 | -8.9706 | -61.7224 | 2025-08-16 02:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.8 |
| bea9d695-2dd2-32bb-8049-cb85aebce447 | -8.9709 | -61.6842 | 2025-08-16 02:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 94707e18-cd01-3431-a3e1-8cce9163e401 | -9.1708 | -59.6568 | 2025-08-16 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 6ee57ddd-6326-3bd8-80a8-a5d36d237b81 | -14.9441 | -54.6959 | 2025-08-16 02:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| bd62d3b0-66d5-3c23-8c57-9d8097a9fe1f | -7.9149 | -61.7288 | 2025-08-16 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| aca83b80-458e-3f3e-b444-304f4cf0f43a | -8.9892 | -61.7215 | 2025-08-16 02:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 07774bc3-528e-39b1-a3ec-f0809a709229 | -14.9438 | -54.7166 | 2025-08-16 02:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 0768c158-858a-3798-a53a-261a264a516e | -8.9893 | -61.7024 | 2025-08-16 02:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 8e42d70d-2794-39c8-8bd2-dfc7762cae10 | -7.9148 | -61.7478 | 2025-08-16 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 3fe36c8c-f9ae-3aea-9074-d4aee5f88974 | -14.9628 | -54.7351 | 2025-08-16 02:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 39a824b6-70d2-3dd1-b540-c8985a68d53d | -11.3466 | -55.4326 | 2025-08-16 02:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 08adb801-591c-396e-b6f2-1ece3e2e5e4a | -6.5638 | -43.0357 | 2025-08-16 02:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| cc0cdc67-66d1-331b-8aa4-dd5e534ca439 | -7.9333 | -61.7471 | 2025-08-16 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| bbf96efc-b0a3-3cb0-ab8a-549253719819 | -9.518 | -60.5268 | 2025-08-16 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 064b6b62-9981-3df9-afcc-dad805cd0a2d | -9.5179 | -60.5461 | 2025-08-16 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 4f2f172a-c866-3c50-9cb0-2d844a0a520c | -6.9487 | -59.5297 | 2025-08-16 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| c8b48996-1c78-335e-9c7f-d69153458820 | -7.9148 | -61.7478 | 2025-08-16 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3d91a58d-cb40-3e22-a76d-4a29cedbeccf | -6.5638 | -43.0357 | 2025-08-16 02:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 389b5e65-7f4d-39e3-ba44-0567802e1482 | -6.9302 | -59.5497 | 2025-08-16 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| fa6a6f9d-23fe-3f35-8e55-aa104fb2f06e | -7.9334 | -61.7281 | 2025-08-16 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 7b4a2557-3df6-3e91-a637-1588e12aa2d0 | -11.3466 | -55.4326 | 2025-08-16 02:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 82de72fb-747c-32b1-9c38-cb63a1a3b8e9 | -8.9708 | -61.7033 | 2025-08-16 02:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 83.1 |
| f8184f7f-7a2f-3b51-968d-b79b2d2cf45b | -13.4294 | -43.6733 | 2025-08-16 02:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| e62336ec-df01-3454-b0b0-98367999f20c | -14.9435 | -54.7374 | 2025-08-16 02:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| cd2d4526-03e8-394b-9817-9eb891c83fee | -8.9893 | -61.7024 | 2025-08-16 02:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 93ae454b-b209-371f-aa26-b1fb6ff1b629 | -9.518 | -60.5268 | 2025-08-16 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| f9513ef6-fa0e-3148-a1c7-912245e76ea8 | -8.9709 | -61.6842 | 2025-08-16 02:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 6cf2a1dd-5683-3442-b286-0a8fd059907a | -14.9441 | -54.6959 | 2025-08-16 02:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 7f4cf947-5b5e-34b1-bf28-5eb82efd0962 | -7.9149 | -61.7288 | 2025-08-16 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 5a4a0742-a279-34aa-bbc2-f24fc3530512 | -17.615 | -46.684 | 2025-08-16 02:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 38.0 |
| a73640dc-dc73-35b4-bd9b-90d599b81dc6 | -11.2596 | -50.4767 | 2025-08-16 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 7b269c24-b27b-39f2-b823-7f4e066d582e | -14.9628 | -54.7351 | 2025-08-16 02:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 58717fbc-9a97-3645-9427-ae4323934c00 | -6.9486 | -59.549 | 2025-08-16 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 73ea7327-1e7d-3e4e-9631-0f9b45eecb8b | -14.9438 | -54.7166 | 2025-08-16 02:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 152.3 |
| e38b69bf-7d93-39a5-9a8f-aa4ea89c8704 | -14.9632 | -54.7143 | 2025-08-16 02:30:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 619b8d4a-6fa4-367d-9e20-d50083cf63c2 | -9.4994 | -60.5278 | 2025-08-16 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| f156a0bc-48b8-3c90-9c8a-04f251bd8017 | -8.9706 | -61.7224 | 2025-08-16 02:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 6ecf0177-02b0-3d9f-9dfd-7769fe776b8c | -9.4992 | -60.547 | 2025-08-16 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 71f29622-f7d8-3ec5-94df-3d90f5bde935 | -9.1709 | -59.6374 | 2025-08-16 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| c31fd4d5-343c-3204-8808-0be9aff053af | -9.1708 | -59.6568 | 2025-08-16 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 944f0da0-9024-3f05-b6ff-d8d8b89ed20f | -11.2593 | -50.4981 | 2025-08-16 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 63c4a7eb-d218-370a-8867-a7847044bee3 | -7.9333 | -61.7471 | 2025-08-16 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| a83519d5-af13-3a84-b79a-9f10303e04f9 | -14.9628 | -54.7351 | 2025-08-16 02:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| cabb95d6-b759-36f2-b0e7-60b784eae8ec | -6.9487 | -59.5297 | 2025-08-16 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| b1940e46-e6db-33af-aad4-925e2823566e | -9.4994 | -60.5278 | 2025-08-16 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 9eb62805-79ec-3c00-a115-64dc9571bba8 | -16.1974 | -49.9737 | 2025-08-16 02:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| e965ea9a-7e84-3a85-afbc-1cc8f9871f2e | -9.1709 | -59.6374 | 2025-08-16 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| a71367b7-6748-3c46-9e2e-501fb26d1702 | -6.545 | -43.0373 | 2025-08-16 02:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 59502934-857d-3d70-b70c-636a50298e38 | -14.9441 | -54.6959 | 2025-08-16 02:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 3e4d9912-824a-3b9c-ace0-ed6261f88618 | -7.0796 | -59.2351 | 2025-08-16 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 9d19cb40-274d-3199-9f6c-758566fb250e | -6.9303 | -59.5305 | 2025-08-16 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 98a86dfd-96e6-3575-8918-7daf2c1e9246 | -16.2171 | -49.9705 | 2025-08-16 02:40:00 | GOES-19 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 60725c56-6639-3c9a-aadd-5c8cf8e99715 | -9.1708 | -59.6568 | 2025-08-16 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |


[Clique aqui para ver as próximas entradas](README17.md)
