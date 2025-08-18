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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d983d824-a685-393d-9fd7-b26c49f6403a | -15.0199 | -54.7905 | 2025-08-18 08:30:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 7dba18ff-dc7a-3692-8ec6-553dd67db7f3 | -13.1558 | -54.9151 | 2025-08-18 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| ddaa0fcb-46b4-313d-bab8-c87c7b48915c | -13.1555 | -54.9357 | 2025-08-18 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 82b64bd4-6b09-389e-aeb0-0c779e6411db | -13.1746 | -54.9337 | 2025-08-18 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| b49cbdb7-7e2c-3602-b08c-db2a6d6efaec | -13.1749 | -54.9132 | 2025-08-18 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 8c87d15a-5626-3dba-9f58-0cccf6e37d3e | -13.1555 | -54.9357 | 2025-08-18 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 107cd1fd-8585-3967-bb70-c8bcea81d531 | -13.1558 | -54.9151 | 2025-08-18 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| a8812c13-c850-315d-ad25-b8221ed26650 | -13.1746 | -54.9337 | 2025-08-18 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 175.4 |
| 025d018c-9799-3578-b797-c62b6535098d | -13.1749 | -54.9132 | 2025-08-18 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| f07e06cb-c504-3d07-8894-f276b0dccdef | -15.0199 | -54.7905 | 2025-08-18 08:40:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| d43eddbe-ddc2-35b8-9d71-06a54057b22a | -13.1558 | -54.9151 | 2025-08-18 08:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 63fad0a9-c9dc-3e6f-b85d-9c1c37cc63fe | -13.1749 | -54.9132 | 2025-08-18 08:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 151.7 |
| a24e9cb5-cc7f-319e-b7d6-c083e505eaa8 | -13.1555 | -54.9357 | 2025-08-18 08:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 7157bb47-f922-3abc-bd5f-c0c5e58fae99 | -13.1746 | -54.9337 | 2025-08-18 08:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 165.2 |
| ff999581-2c6a-3800-8760-08a243ed706b | -15.0199 | -54.7905 | 2025-08-18 08:50:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 8406751a-6a47-3c02-8d0b-cdd50f322913 | -13.1555 | -54.9357 | 2025-08-18 09:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 04f31b4b-ef13-3a32-92ff-ea6b9b9f6927 | -13.1558 | -54.9151 | 2025-08-18 09:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 318919f0-6468-39ba-970e-a04315237f3a | -13.1749 | -54.9132 | 2025-08-18 09:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| d89d52d4-8f82-3a8d-8eab-337be07820e8 | -13.1746 | -54.9337 | 2025-08-18 09:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 194.2 |
| 234cd4c5-94a5-35c6-86c3-85fd3f96d473 | -13.1558 | -54.9151 | 2025-08-18 09:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 06f20c72-5d7b-3ad2-b123-05c60354ad6f | -13.1746 | -54.9337 | 2025-08-18 09:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 5aeb7457-7d89-3c8c-ae63-f96bb0e0af3b | -13.1555 | -54.9357 | 2025-08-18 09:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 845b3c9c-542e-38c3-80f3-05d65b7f4f1e | -15.0199 | -54.7905 | 2025-08-18 09:10:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| bec61450-6fab-3acf-bed5-fdc542dd3532 | -13.1749 | -54.9132 | 2025-08-18 09:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| c091326a-e0ac-3b3b-9e55-5013cf6156a9 | -13.1746 | -54.9337 | 2025-08-18 11:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 2915abfe-51de-309a-994b-46e83afc114a | -13.1746 | -54.9337 | 2025-08-18 11:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 6f7194d3-5000-342a-b3f6-651c3d0dbc1b | -13.1746 | -54.9337 | 2025-08-18 11:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 65b8d8b7-2187-348d-8775-98bf55627ccb | -13.1555 | -54.9357 | 2025-08-18 11:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 15c33de8-2c30-31a9-b640-6e243b024474 | -13.1746 | -54.9337 | 2025-08-18 11:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 1cc517ec-3272-38f5-9d37-f855e446d7f4 | -13.1555 | -54.9357 | 2025-08-18 11:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| d0fc5da5-feb3-3464-a6b0-94ce55f39a6c | -13.1746 | -54.9337 | 2025-08-18 11:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 145.9 |
| b1ed0733-dda0-348d-980a-45acd2c1c542 | -13.1555 | -54.9357 | 2025-08-18 11:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 0b0a87cb-a3cb-3184-bafc-ff8e3ebf3fcd | -7.5711 | -45.4333 | 2025-08-18 11:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 4dce0788-338b-3b43-986f-2d46e94ae6bc | -13.1749 | -54.9132 | 2025-08-18 11:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 51f76fe0-ff15-3800-bbc6-f67197b9a304 | -13.8748 | -45.5411 | 2025-08-18 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 45865ece-7e52-3aef-9c07-3a6bb0ea87b3 | -13.1555 | -54.9357 | 2025-08-18 11:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| c2f8fcfc-8058-308e-98c0-0495ef230ac0 | -13.1746 | -54.9337 | 2025-08-18 11:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 151.6 |
| b99225b4-69ef-395a-aa3c-7f9664a5ec1c | -14.9815 | -54.7743 | 2025-08-18 11:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 91b9f769-b0c9-3bbe-b619-f005fbe6ee5f | -7.5711 | -45.4333 | 2025-08-18 12:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| d6d804a6-fc31-36e3-a762-3ca36efbf57a | -13.1555 | -54.9357 | 2025-08-18 12:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 220.9 |
| 4c1c83f7-ebcd-362b-b319-38d2e1ef7b0c | -13.1749 | -54.9132 | 2025-08-18 12:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| deb56c8c-03e3-3adc-93f7-138fa7c01358 | -13.2183 | -50.7996 | 2025-08-18 12:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| d3a25084-5420-3c12-b6d5-0ba4820481d2 | -13.1746 | -54.9337 | 2025-08-18 12:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 152.6 |
| d0eb2a68-a83c-37df-b06c-dbc84254c412 | -13.8748 | -45.5411 | 2025-08-18 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 1c2d47d6-cfac-31b5-ba23-079d2fd53879 | -13.1558 | -54.9151 | 2025-08-18 12:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 115.3 |
| fa1c701c-1b70-3b55-941b-920a6973a931 | -13.2183 | -50.7996 | 2025-08-18 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| e7a8f093-1af9-3bd2-a5a2-bcccb9a68f56 | -13.1746 | -54.9337 | 2025-08-18 12:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 255.6 |
| 5a548780-a7c6-3bd4-81b3-0cc9570fdbc4 | -13.1555 | -54.9357 | 2025-08-18 12:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 271.9 |
| fb298669-7159-37c2-b391-42cba6e173fe | -13.2186 | -50.7781 | 2025-08-18 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 8d3c032f-c761-3c88-b2c5-9918f2168b8f | -7.5711 | -45.4333 | 2025-08-18 12:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| fe9c612c-6f57-3245-a659-a8bff45f45c0 | -13.1749 | -54.9132 | 2025-08-18 12:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 125.1 |
| a817602f-fc19-3653-98eb-3b7cb27b1d83 | -13.1558 | -54.9151 | 2025-08-18 12:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 3348744d-a4ae-3754-8945-c139af3c2a9e | -12.6435 | -45.3269 | 2025-08-18 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 94738890-15ae-33ef-8ad4-167c597cb9cf | -13.1555 | -54.9357 | 2025-08-18 12:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 320.3 |
| 11b9a51e-0e74-386f-84af-04a3f51d0542 | -14.1897 | -45.3241 | 2025-08-18 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| cb334f77-37db-3129-a243-fbc273d63140 | -13.1558 | -54.9151 | 2025-08-18 12:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 152.1 |
| b942ebd8-ff2c-3b58-8521-2e2ae42c9306 | -13.1749 | -54.9132 | 2025-08-18 12:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 173.9 |
| 0276aaa4-f645-3f16-9bf5-36579376af7f | -13.1746 | -54.9337 | 2025-08-18 12:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 371.8 |
| 7956e8a5-6ff9-3508-8655-1d772f6b22fb | -13.1743 | -54.9542 | 2025-08-18 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| ef02d923-cdc4-3c77-aff8-dc4e993682f7 | -13.1746 | -54.9337 | 2025-08-18 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 326.3 |
| fe1cc994-7cc0-359c-81a2-bb2acb809a7c | -13.1749 | -54.9132 | 2025-08-18 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| d0b09f7e-b19e-3d49-bd69-5bb2b06c9a1c | -13.8748 | -45.5411 | 2025-08-18 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 58bd8c32-1266-3591-af44-44a555d36840 | -14.1897 | -45.3241 | 2025-08-18 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 2fa6c16d-9b24-3875-a824-651445cdff17 | -13.1558 | -54.9151 | 2025-08-18 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 120.7 |
| fb0e4a2e-e584-3547-86e3-6409c8c88bc4 | -13.1555 | -54.9357 | 2025-08-18 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 329.1 |
| d770bc14-025a-38e1-a768-61e6a9bb3fd4 | -13.2375 | -50.7972 | 2025-08-18 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 7f21fcda-7a5b-3095-ac18-76903032bcf8 | -14.1702 | -45.3276 | 2025-08-18 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 06f7c258-5ac2-3a27-9e37-74a47b67e7dd | -2.96038 | -40.40149 | 2025-08-18 12:32:00 | TERRA_M-T | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 4b2c9fb0-54ed-3396-8f3f-c0ce89cc4e36 | -2.95427 | -40.40728 | 2025-08-18 12:32:00 | TERRA_M-T | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 38.0 |
| e9469fb0-c945-3459-ae77-4dc70357aadc | -4.96582 | -43.09343 | 2025-08-18 12:32:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 4d2a5748-d48f-3d56-8aea-58cde64400e5 | -3.98184 | -42.52375 | 2025-08-18 12:32:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 50.9 |
| 70d6ee49-3174-34d1-8f88-226529812197 | -4.09107 | -47.32441 | 2025-08-18 12:32:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 31.7 |
| dc42c7f4-e156-3834-90aa-e3e5776ad9c2 | -4.09249 | -47.31435 | 2025-08-18 12:32:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 30.1 |
| f62c52da-4255-3627-946f-86906fdeb09d | -9.38884 | -48.30448 | 2025-08-18 12:34:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f0da9a1c-28d2-30c1-b60e-8f5472d8e059 | -9.39026 | -48.29415 | 2025-08-18 12:34:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 21fb9dff-a1ee-3d5c-8397-57a6a47acec7 | -11.14797 | -46.92221 | 2025-08-18 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 429.0 |
| c15ba07b-02cf-37bc-b665-bf9563b1ef67 | -13.17513 | -54.94573 | 2025-08-18 12:34:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 40d12a84-b6fb-3c9c-86fe-9c818f06daaa | -14.6257 | -54.91782 | 2025-08-18 12:34:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5fc1956e-3996-3a84-897c-c0f3b7c0fd33 | -8.06998 | -47.71186 | 2025-08-18 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2acd997f-7a77-355a-a414-a082694b8bed | -10.61248 | -46.29073 | 2025-08-18 12:34:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5aefa110-25ba-307b-8bfe-939c8d2f1133 | -14.18573 | -45.33293 | 2025-08-18 12:34:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 3d5a2355-f6c6-35a3-ab2f-6ea7acb12c7e | -13.96061 | -43.33747 | 2025-08-18 12:34:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 22.5 |
| f0471720-d1df-3453-a1ac-8351399664ad | -12.93412 | -46.10971 | 2025-08-18 12:34:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| fab995c8-165f-3a19-b272-128465c56232 | -12.64534 | -45.3308 | 2025-08-18 12:34:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 6bbd7f36-06ef-3f88-abd5-c689d2b006f7 | -13.46895 | -47.0704 | 2025-08-18 12:34:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 773b058a-213e-3f67-b4df-9bd0bbfe2a15 | -7.97699 | -49.95491 | 2025-08-18 12:34:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 895f6c3d-2898-3a7e-8fa0-daeb4ea3c974 | -7.80399 | -45.15299 | 2025-08-18 12:34:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e94f06f4-05e6-33f9-a8f5-e3a370af7720 | -13.87272 | -45.54595 | 2025-08-18 12:34:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 25b6a64f-4125-303d-90bc-91797b288edd | -12.30005 | -50.02615 | 2025-08-18 12:34:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ddd88fbe-6eb1-3a79-ac4d-1928b2cc2a60 | -8.3891 | -44.97987 | 2025-08-18 12:34:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 4eb27382-14ef-3150-b467-91f8482186c0 | -14.18795 | -45.31294 | 2025-08-18 12:34:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 6dbbc4a1-c51b-366d-a3db-ca8fbe84f2da | -13.70185 | -51.97462 | 2025-08-18 12:34:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| aa373bbc-3d4b-36c8-916e-a0006a302692 | -14.18563 | -45.32636 | 2025-08-18 12:34:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 51d3a02e-80ba-3aa6-a50f-77e48a800f40 | -14.17526 | -45.30488 | 2025-08-18 12:34:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 765755bd-94e9-363d-9a3c-24ba970520f5 | -12.99376 | -56.84538 | 2025-08-18 12:34:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| a6053105-73fd-3f9c-99ad-17d4cdb91b22 | -8.33687 | -47.6336 | 2025-08-18 12:34:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 443b1102-c3d3-36d4-9af0-3e3a338cd01b | -13.14124 | -42.54866 | 2025-08-18 12:34:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 717c17fd-0e25-3eb7-a097-49da9a820dea | -13.23218 | -50.74351 | 2025-08-18 12:34:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 2e149532-6475-3cb4-bd67-1b240804534c | -5.67323 | -43.36739 | 2025-08-18 12:34:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 85cbe675-0e5a-31db-be6f-9f31b85cac30 | -11.13916 | -47.28359 | 2025-08-18 12:34:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |


[Clique aqui para ver as próximas entradas](README35.md)
