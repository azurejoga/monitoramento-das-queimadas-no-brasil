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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd4b7829-bef3-3cdb-9565-50569bfe124b | -3.2174 | -50.139 | 2025-12-01 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 839789cb-3454-3842-abf9-c80b85065d0e | -4.3702 | -43.1741 | 2025-12-01 02:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| baa58c94-f03f-3daa-9116-bb3b87c153f7 | -4.3703 | -43.1508 | 2025-12-01 02:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 171.2 |
| a15a020b-6edd-3c88-992b-f34aac5caa7f | -3.7009 | -45.9 | 2025-12-01 02:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 105.6 |
| a149223c-3e0e-369a-8b64-bd2946380b3f | -4.3877 | -43.3362 | 2025-12-01 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 192.6 |
| b31496de-e39a-317a-9fd9-2193af49a0a6 | -17.5144 | -57.1719 | 2025-12-01 02:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.4 |
| 632906bf-ebd4-3248-8c10-9481ed9ba726 | -8.051 | -43.1237 | 2025-12-01 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 26e81cca-dc68-37ff-8223-d5864c929bcb | -4.3703 | -43.1508 | 2025-12-01 02:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 0757c766-36db-3235-97a0-6cc8218a38c5 | -4.3877 | -43.3362 | 2025-12-01 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 896ffb03-d9f7-36e8-ae57-f526937c7b0e | -4.3879 | -43.3129 | 2025-12-01 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| f449aef8-57f3-3229-bd9e-8e830561c38a | -3.7009 | -45.9 | 2025-12-01 02:20:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 92981294-979d-3507-9768-41dcbde12f36 | -17.5341 | -57.1695 | 2025-12-01 02:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 95ae7531-7c33-32be-a22d-92c1af91161b | -4.4064 | -43.3351 | 2025-12-01 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 427c43c5-4b65-30ec-9fe9-33f6005593d3 | -3.2174 | -50.139 | 2025-12-01 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 33ca13be-7889-3146-9549-0e1a581db7cb | -4.389 | -43.1497 | 2025-12-01 02:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| d20da2ad-ce33-3ed9-a680-58d2a68a0e61 | -17.5144 | -57.1719 | 2025-12-01 02:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.7 |
| 7b241b33-eb05-3831-802c-f19faffcd872 | -4.3702 | -43.1741 | 2025-12-01 02:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| b0b134e6-10e1-3e7e-a083-18cbfa3b5f08 | -20.0142 | -57.4484 | 2025-12-01 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.9 |
| 645c1736-addd-39a5-981f-13fed060f093 | -19.9746 | -57.4121 | 2025-12-01 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 527e187e-d946-3b3b-adce-3e574b257a67 | -20.0145 | -57.4275 | 2025-12-01 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.4 |
| 5d2c995d-7a3f-376f-b2fa-5ed397199fb1 | -4.4064 | -43.3351 | 2025-12-01 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 35493d89-206d-3a2e-9a41-f59f447792c7 | -19.9548 | -57.394 | 2025-12-01 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.1 |
| 27ab6bfe-f21f-3765-a44c-431795f0fc8a | -20.0347 | -57.4247 | 2025-12-01 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| f1e20e65-9458-3dce-be3b-fc0548d38997 | -4.389 | -43.1497 | 2025-12-01 02:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 54174899-d817-3356-8490-93f4207d3ed3 | -4.3877 | -43.3362 | 2025-12-01 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 2e76fab5-b7c4-3690-9101-877d8df8f937 | -19.975 | -57.3912 | 2025-12-01 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.4 |
| 444a38db-61c2-3f31-b927-23b6edde89c2 | -3.7195 | -45.8992 | 2025-12-01 02:30:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 7b7fab64-9a3b-310a-b3df-5c5169ebff13 | -4.3702 | -43.1741 | 2025-12-01 02:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 32835f10-e852-3e98-969c-484cec0d0d2f | -3.7009 | -45.9 | 2025-12-01 02:30:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| c7188e8c-20e3-350e-822a-41ca24455cdd | -3.2174 | -50.139 | 2025-12-01 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 655cc287-c281-3416-a23c-a8f99ebe7d22 | -4.3879 | -43.3129 | 2025-12-01 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| a17bd82c-fc6c-3ead-9078-190fb6c71f0b | -17.5144 | -57.1719 | 2025-12-01 02:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 5dd54ff0-6bab-3f0b-beac-e299a3f48c5a | -20.0343 | -57.4457 | 2025-12-01 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 21a8bb88-ab39-37e8-8bf8-bdb7eea1d0b3 | -17.5341 | -57.1695 | 2025-12-01 02:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.1 |
| c2603313-de1c-3e78-8d72-b84d5698b09c | -4.3703 | -43.1508 | 2025-12-01 02:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 165.5 |
| dd107b6f-cbbc-3032-9e15-93e0d04c84c6 | -4.3889 | -43.173 | 2025-12-01 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| c9b16a00-7445-32e4-8aab-796d057b50c7 | -4.3877 | -43.3362 | 2025-12-01 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 68dc8585-2342-36f3-b232-64f012e19ec8 | -20.0142 | -57.4484 | 2025-12-01 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.8 |
| 9eb07464-be4d-3a15-ba3a-227852ca0460 | -3.7195 | -45.8992 | 2025-12-01 02:40:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 0c018fb9-a929-3c83-adac-ac85112a0a54 | -4.3879 | -43.3129 | 2025-12-01 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 5d33b0bd-a733-3f6c-889d-56ed427c9ef9 | -4.389 | -43.1497 | 2025-12-01 02:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 1143600c-0820-3528-a58c-33ab894d852f | -20.0343 | -57.4457 | 2025-12-01 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 310580ee-6c2e-3eaf-a6ae-13fccc7f96b5 | -4.3703 | -43.1508 | 2025-12-01 02:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 56f59fa7-e9a2-3319-a7e4-c48ef5f21766 | -4.3702 | -43.1741 | 2025-12-01 02:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| b4d6361e-86a1-333b-8ce4-386cd0d15471 | -3.6008 | -47.2739 | 2025-12-01 02:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| fdee00b3-8ea6-357f-8dfb-3c72bed6e057 | -20.0145 | -57.4275 | 2025-12-01 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.4 |
| cf6a472d-4f66-3e76-a437-5d46a2ce7b82 | -4.4064 | -43.3351 | 2025-12-01 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| f917c9cd-e745-3ef6-b87a-9e3ba82ac1ce | -3.2174 | -50.139 | 2025-12-01 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 6277c55f-91ec-3980-9c23-5a31c951bc92 | -20.0347 | -57.4247 | 2025-12-01 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 7de124c4-582a-33a7-b343-52e16682c7f9 | -3.7009 | -45.9 | 2025-12-01 02:40:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 3f6ba829-63d9-3f35-823f-6bbceebb84de | -3.7195 | -45.8992 | 2025-12-01 02:50:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 808d5a73-6b25-3e16-8702-b5699f1f8fbf | -4.3703 | -43.1508 | 2025-12-01 02:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 9ff4473c-0686-325e-8cce-a9fb311cc33e | -4.3877 | -43.3362 | 2025-12-01 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 233.8 |
| 1b1155ca-a6ef-3b0e-af8e-284684e0d06f | -20.0145 | -57.4275 | 2025-12-01 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 1a18ebfa-18f5-3d2d-bcad-cee057f2ea68 | -4.3889 | -43.173 | 2025-12-01 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 98b857b5-3588-3fcd-b08e-6c8de7db63cc | -20.0343 | -57.4457 | 2025-12-01 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 769bf197-2b4e-366b-af91-b3a98f3580d5 | -20.0142 | -57.4484 | 2025-12-01 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.6 |
| 896f33ee-1512-3117-94d0-fe3701ac5ef6 | -4.4064 | -43.3351 | 2025-12-01 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 850e3420-48ba-3fa1-8aee-383a52a6633c | -20.0347 | -57.4247 | 2025-12-01 02:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 000bc33f-073d-3d78-871e-49f81a1526e9 | -4.389 | -43.1497 | 2025-12-01 02:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 95b1fe20-9eb6-360c-afd4-2aeef599dc34 | -3.2174 | -50.139 | 2025-12-01 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 0e71fe05-1efc-35dd-bd30-42eb66ee2885 | -4.4066 | -43.3118 | 2025-12-01 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 33d942f1-12f1-38ab-9271-61be6a122588 | -4.3876 | -43.3595 | 2025-12-01 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| db0f277b-9b56-3d87-98cf-eef8d0d2dbd9 | -4.3879 | -43.3129 | 2025-12-01 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 6178cbab-48a9-318a-8ee6-2bea6bf2bb03 | -4.3702 | -43.1741 | 2025-12-01 02:50:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 2c4bf43b-962a-3856-bf24-96d62b941652 | -3.6008 | -47.2739 | 2025-12-01 02:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| f6093c42-3218-37ab-b933-58070ee48a6a | -3.7009 | -45.9 | 2025-12-01 02:50:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 83.5 |
| f4ea4a80-963a-3b2c-b95b-f4071c35fb80 | -3.7195 | -45.8992 | 2025-12-01 03:00:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| c14cd279-4047-306a-a46e-02f42d64da1d | -4.4064 | -43.3351 | 2025-12-01 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 233.8 |
| 87e4a847-f0b5-3701-90cf-b0c166aab5ca | -4.3702 | -43.1741 | 2025-12-01 03:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| e6c2899a-b8f1-3faf-8f30-f1b419f47cbc | -3.2174 | -50.139 | 2025-12-01 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 29a6bce4-3ac2-3f32-8b56-3c766af25b6c | -3.7009 | -45.9 | 2025-12-01 03:00:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 9a2d178a-528a-39e5-8bc1-70524218eb57 | -4.3876 | -43.3595 | 2025-12-01 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 1b5afae0-fd43-34a9-bcf7-f4046358ce29 | -4.389 | -43.1497 | 2025-12-01 03:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| ba2eb227-680b-3c50-9c39-bb0b47348306 | -4.3877 | -43.3362 | 2025-12-01 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 542.0 |
| 5c1dbad8-7208-3c13-a4ff-816050c20961 | -4.369 | -43.3373 | 2025-12-01 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 95b69aad-3942-3bfe-9ae1-bc4a8a2292a0 | -4.3889 | -43.173 | 2025-12-01 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 4bfd0f05-62e9-3c44-ab3b-b3bb00c2db96 | -4.3703 | -43.1508 | 2025-12-01 03:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 0832d965-4beb-35d7-badb-89b6165dc35a | -4.4062 | -43.3584 | 2025-12-01 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 759ec2e0-3dea-3efb-8407-8cf81f0c5aee | -4.3879 | -43.3129 | 2025-12-01 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 301.4 |
| 69bd51cc-2b3f-3f4e-adb6-f77da12a5549 | -4.4066 | -43.3118 | 2025-12-01 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 9f65479d-db30-35b2-8f91-d75e3621a1a6 | -3.6008 | -47.2739 | 2025-12-01 03:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| f03634de-2b58-3b24-a629-ed189ae40320 | -4.3876 | -43.3595 | 2025-12-01 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| f4648887-89e8-3cf4-9279-9922049add78 | -4.3877 | -43.3362 | 2025-12-01 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 329.9 |
| a3bc102f-318a-3b54-aa58-8dc7cc2682ca | -3.7195 | -45.8992 | 2025-12-01 03:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| b30fc235-75f1-3bd5-bb95-9391ad169915 | -5.3398 | -43.5535 | 2025-12-01 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 4b42c001-5f12-3f9b-958b-44c45f8dd6d3 | -4.3703 | -43.1508 | 2025-12-01 03:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 8fada812-ae90-30d1-b494-0fcf238eb786 | -5.3396 | -43.5768 | 2025-12-01 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 63d77faf-d095-3fac-88f0-89c762c3e136 | -4.3879 | -43.3129 | 2025-12-01 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 182.9 |
| caf5eecc-ba86-3801-9f77-50b6bcd32957 | -3.6008 | -47.2739 | 2025-12-01 03:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| e1d7f289-fd0d-37de-94f0-7c8f4728f40f | -4.3702 | -43.1741 | 2025-12-01 03:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| def9c01b-ff53-3246-bc1d-74a2ebc1ce27 | -3.7009 | -45.9 | 2025-12-01 03:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 4eb17baf-3aec-32a9-958d-996ead572242 | -4.4064 | -43.3351 | 2025-12-01 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 97e7075f-a88c-337a-960b-49b3caae7cc5 | -4.389 | -43.1497 | 2025-12-01 03:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 03449ff4-86ad-3020-b9bd-415de871c4cf | -4.4066 | -43.3118 | 2025-12-01 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 83353a66-e10d-3111-8424-74002ee600a4 | -4.369 | -43.3373 | 2025-12-01 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| f00ec713-6fec-372e-8957-6394ab3df1f6 | -4.3889 | -43.173 | 2025-12-01 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 8bb6eac8-d3cf-334d-862e-2d399e019363 | -4.3889 | -43.173 | 2025-12-01 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 4b8f2e7a-8305-396b-8616-5996353139e9 | -4.389 | -43.1497 | 2025-12-01 03:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 5c1ef4ea-410a-31c2-b19f-a71e4d06267f | -4.3877 | -43.3362 | 2025-12-01 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 252.8 |


[Clique aqui para ver as próximas entradas](README7.md)
