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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e80aea2-dacd-3ad9-8524-a5971bfd43eb | -12.8399 | -54.812099 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 730ab7f3-ffd4-3aa6-9f9f-99e28ea8e3ec | -12.8431 | -54.826698 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83c40a19-dd1f-35cc-8f93-5432daa1d1e0 | -13.1269 | -51.8764 | 2025-09-05 00:36:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd04a77e-09f1-3f22-9404-8feb8f0c0a88 | -12.8529 | -54.824501 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bcbbf379-f69d-3496-b0fe-9d03776e08f7 | -12.8576 | -54.8465 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8654f4c9-2dbb-373a-a1f1-d0ddff984cf8 | -13.1253 | -51.869099 | 2025-09-05 00:36:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e49d2bf1-d4d4-3593-8759-e5b7b7415842 | -12.8244 | -48.084702 | 2025-09-05 00:36:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3841d8f8-2c90-3fed-968d-883306e57046 | -11.2417 | -43.611698 | 2025-09-05 00:36:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 54021b0b-e33b-3fa7-8e81-b9c83e27b9e7 | -12.1456 | -50.0425 | 2025-09-05 00:36:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a82e08f7-0c1b-3725-937d-610af6eecbe3 | -12.8494 | -54.855999 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 156dd4fa-f51f-371b-a2cf-08755c990970 | -12.8462 | -54.8414 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e0771438-6a01-377d-b7e6-cdc4622bbce3 | -12.3645 | -53.8577 | 2025-09-05 00:36:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92e1741e-70fd-32c3-891d-777135a294c7 | -12.175 | -47.079899 | 2025-09-05 00:36:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c7ae4af-c89e-3042-a82c-ae491a46b429 | -12.1718 | -47.067001 | 2025-09-05 00:36:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e5bcf013-c5e9-3bd9-85d7-ecd7b1704cda | -10.8745 | -45.1054 | 2025-09-05 00:36:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0d7b261f-c635-3e65-a3fb-224796b2e448 | -15.8299 | -51.7498 | 2025-09-05 00:40:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 377cf6be-fb37-3bbb-84b3-20b6d91d5331 | -15.8494 | -51.7469 | 2025-09-05 00:40:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 358460b9-16ec-3fc3-8b9e-1c7aa9393944 | -5.6079 | -45.0265 | 2025-09-05 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 189.9 |
| e3abf6e8-0aa3-357f-a3bd-7c6ca2996610 | -5.5894 | -45.0051 | 2025-09-05 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| eafa805a-b19c-3d65-a068-d632a3620b3d | -5.7227 | -49.2842 | 2025-09-05 00:40:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 5aefde6d-9e32-36ef-b6ef-6db4b4890655 | -9.2288 | -57.0906 | 2025-09-05 00:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 3c9fe3ce-3e88-36c7-bc3a-071495f87841 | -14.2892 | -45.2134 | 2025-09-05 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 1c8984c9-1d34-3e59-8999-4f406434ef4d | -5.6081 | -45.0038 | 2025-09-05 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 1c79b0ac-7d9c-39e1-91a2-05cbcc14434a | -11.6409 | -54.5315 | 2025-09-05 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 5636aa4a-e381-3606-adfc-d606bddc6f1a | -5.4917 | -60.138 | 2025-09-05 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| f65b8323-6905-3fa6-8cb6-7e5978a861f4 | -9.2102 | -57.0918 | 2025-09-05 00:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 1215781e-afa9-3bf6-8b76-0aaea69d987b | -9.2477 | -57.0697 | 2025-09-05 00:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| a81b6bc7-39b5-3a00-a5c7-105c53392260 | -6.5856 | -44.564 | 2025-09-05 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 4b8062a7-a447-32f7-98f3-1d4099aad077 | -9.0762 | -47.0113 | 2025-09-05 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 483c3e76-cf59-3e93-b52f-988e8bad9206 | -5.5892 | -45.0278 | 2025-09-05 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 86903907-20d2-3edc-9ae1-9052a7a945f4 | -5.4918 | -60.1189 | 2025-09-05 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 270cc56f-deda-3dda-afcd-c26a3b9ab17c | -15.8294 | -51.7714 | 2025-09-05 00:40:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 53de8c85-b33d-3299-a941-a79d5e5282c2 | -13.1079 | -57.1109 | 2025-09-05 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 111.7 |
| c276a6dd-2b95-3451-80f9-4d1ec553e5f8 | -15.849 | -51.7685 | 2025-09-05 00:40:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 48658aae-94b7-390f-9606-10c5ebcd1d0b | -5.5608 | -46.1988 | 2025-09-05 00:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 5a08191a-52b0-3a3d-96f8-1472e9cb9d37 | -5.4918 | -60.1189 | 2025-09-05 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 38a213d7-385a-3795-8736-6a2e5846c3fc | -5.6079 | -45.0265 | 2025-09-05 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| eedf5831-4bf9-3c7b-86be-ee1dcd4f9865 | -5.5892 | -45.0278 | 2025-09-05 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 6dd0402a-d794-3fa3-897e-32222a1fdcc0 | -9.2102 | -57.0918 | 2025-09-05 00:50:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 206606b9-d777-3c80-8dc3-a6aecefede6a | -5.4917 | -60.138 | 2025-09-05 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 2a98374a-015c-3f54-b095-c585ffe7c4a0 | -9.0765 | -46.9891 | 2025-09-05 00:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 2907ee3d-30fe-3d61-a658-468c71e427f0 | -9.2288 | -57.0906 | 2025-09-05 00:50:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 4d6526df-60e6-35d2-95ba-7db310eb5f1d | -5.7227 | -49.2842 | 2025-09-05 00:50:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 3b1422af-314e-3c78-a15b-447b79638f6f | -5.5608 | -46.1988 | 2025-09-05 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 27eb234e-856e-3342-b88f-8ade080c1ddc | -14.2892 | -45.2134 | 2025-09-05 00:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 5958df36-09f3-3f35-bcfb-2a54b77f208b | -5.6081 | -45.0038 | 2025-09-05 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 20edd090-71d2-38f1-933c-05dd95b7fda7 | -15.8299 | -51.7498 | 2025-09-05 00:50:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 67949529-5eb4-3d85-86b4-ffe41b0126e7 | -9.2477 | -57.0697 | 2025-09-05 00:50:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 7971395a-0930-3a78-adb4-95373ef685ad | -5.5894 | -45.0051 | 2025-09-05 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 42680955-fdd0-3084-b87d-3beed539f7d0 | -6.5856 | -44.564 | 2025-09-05 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 41d04bef-e79c-3ee1-abcb-142278187f4f | -15.8494 | -51.7469 | 2025-09-05 00:50:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 45.6 |
| fe535b50-dd57-3c44-b37b-5c8759a37b46 | -13.1079 | -57.1109 | 2025-09-05 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| faf6ef41-d746-39c8-b416-89dbf4e3d2fd | -5.6266 | -45.0252 | 2025-09-05 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 2e0a2207-6bc0-3351-a50d-05272811b960 | -8.5187 | -51.3293 | 2025-09-05 01:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| e7a73e78-3ab7-3909-b4fb-63f752c7af77 | -5.5101 | -60.1183 | 2025-09-05 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c1b1d949-a9db-39ba-9fcb-d6c150414df9 | -5.6081 | -45.0038 | 2025-09-05 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 2c0f008a-5cc7-3a5e-8026-60d8c21c2ae7 | -6.5856 | -44.564 | 2025-09-05 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 64838362-1381-337e-9fea-5f2124d23e1d | -7.8921 | -45.312 | 2025-09-05 01:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 13212bfb-3d95-3634-aaac-90472e82da5d | -9.0762 | -47.0113 | 2025-09-05 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| dfadf800-c3e8-3907-9707-90bbbba3710e | -5.6079 | -45.0265 | 2025-09-05 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 43c382a0-63d7-34f6-9b33-47f0e816df17 | -5.5892 | -45.0278 | 2025-09-05 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 706f3fba-81e4-3723-a79f-749458f9c808 | -22.483 | -52.7706 | 2025-09-05 01:00:00 | GOES-19 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.3 |
| a035df92-6c37-3512-8a37-7d9452d11130 | -9.2102 | -57.0918 | 2025-09-05 01:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 269427ab-6f3f-3927-b551-158978e8508c | -5.4918 | -60.1189 | 2025-09-05 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 1f4fae91-dd81-3afc-9df0-fdd39b2c785a | -7.8923 | -45.2893 | 2025-09-05 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.0 |
| b23c7a1b-aa82-39db-bca5-78d0b3c9e5e0 | -11.6409 | -54.5315 | 2025-09-05 01:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 970b364b-5c9f-3348-b711-3a112fba6635 | -5.5894 | -45.0051 | 2025-09-05 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 849715df-4dc7-30ef-a465-83dfc136b3c9 | -9.4683 | -62.3476 | 2025-09-05 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 17140962-63d0-31b2-95b7-4679a6bfb579 | -14.2892 | -45.2134 | 2025-09-05 01:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| b12664bc-c407-341b-932a-7bbdd40ddda2 | -13.1079 | -57.1109 | 2025-09-05 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 54c959b3-5df2-3f34-b9ed-6cf7709da82d | -8.5374 | -51.3278 | 2025-09-05 01:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 396465a8-bccb-364b-a93d-fb7c812e7712 | -22.483 | -52.7706 | 2025-09-05 01:10:00 | GOES-19 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.7 |
| e5d90281-578a-3a2d-b39a-ea0141923840 | -9.0762 | -47.0113 | 2025-09-05 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 0d3efeb7-5db2-373e-b607-1d47a83b4137 | -4.0789 | -48.0369 | 2025-09-05 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f3715376-bba3-362c-9489-61c670f663c0 | -13.1079 | -57.1109 | 2025-09-05 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 36371563-ee19-31e4-9c76-dc5884795d0a | -5.6079 | -45.0265 | 2025-09-05 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 128.6 |
| f5f58637-a1ec-3078-be8b-e1d9bfc7ca67 | -8.5374 | -51.3278 | 2025-09-05 01:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| b298d312-49d6-3a7c-a47f-3bfbad4e45c9 | -14.2892 | -45.2134 | 2025-09-05 01:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 3ece02c6-4dbf-30c1-9162-7b861fe039b7 | -9.2477 | -57.0697 | 2025-09-05 01:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a9d1a27a-9d11-3e67-8b23-74a6d337cb14 | -6.6044 | -44.5624 | 2025-09-05 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 3d834928-e0b9-3e07-a547-75f131765043 | -5.4918 | -60.1189 | 2025-09-05 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 8c36b155-2d2b-3534-a50b-36ea47673b4d | -5.5892 | -45.0278 | 2025-09-05 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 525ad162-6379-3d03-8336-3f020c8813b9 | -5.5894 | -45.0051 | 2025-09-05 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 581695c1-abd8-36ca-a5ae-ae7fc00d7332 | -8.5187 | -51.3293 | 2025-09-05 01:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 1fb3b680-144d-32f1-98f8-cd2422b74402 | -9.2102 | -57.0918 | 2025-09-05 01:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 342777f0-fa3b-3fd6-9ada-30160627b63a | -5.4917 | -60.138 | 2025-09-05 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 6789a2b7-21cf-3fda-ad86-2d67f082fa15 | -11.6409 | -54.5315 | 2025-09-05 01:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6a753356-9788-375f-9bde-4171c5764c97 | -22.5995 | -47.9351 | 2025-09-05 01:10:00 | GOES-19 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 33f3ddaf-e58e-391f-be25-04f87189d48e | -6.5856 | -44.564 | 2025-09-05 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| e1b44705-b36e-3a51-8278-ac635df98ce7 | -5.6081 | -45.0038 | 2025-09-05 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 1164037b-73a4-3cd1-ac2b-716d69dd5144 | -22.6197 | -47.9535 | 2025-09-05 01:10:00 | GOES-19 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 215398d4-05e0-36ed-bfb9-d075194724f8 | -22.6205 | -47.9297 | 2025-09-05 01:10:00 | GOES-19 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 95410280-457b-37bf-8b03-74c6cf7ca7a8 | -5.5101 | -60.1183 | 2025-09-05 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 1b674949-83e3-3ef4-b798-45b007a3f156 | -13.1079 | -57.1109 | 2025-09-05 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 9612c65c-2eff-3cb7-a2c6-4e3a34cd0f79 | -9.0765 | -46.9891 | 2025-09-05 01:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 292a3686-1952-36af-b7f4-a002c8a84d0b | -6.6044 | -44.5624 | 2025-09-05 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 6571cdf2-6ba1-339d-b1fa-a10c70e49242 | -5.6081 | -45.0038 | 2025-09-05 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 8c53b162-8186-3d28-8c08-4262667ff308 | -5.5892 | -45.0278 | 2025-09-05 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| ac1a4e10-0bcd-3194-971c-1fdbcec842a3 | -4.0789 | -48.0369 | 2025-09-05 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0d60f446-1549-3d6b-8f82-4e45f1b27cad | -16.5494 | -55.12 | 2025-09-05 01:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 50.6 |


[Clique aqui para ver as próximas entradas](README11.md)
