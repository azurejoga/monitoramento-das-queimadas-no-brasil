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
| 3f7f56f6-7971-3d63-ac59-545d17bc340c | 1.5047 | -59.9116 | 2026-03-03 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 5e96a791-08a9-3fe2-b74c-76c6e4934a8f | 1.4864 | -59.9117 | 2026-03-03 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 1048adf7-98c5-3407-8fcc-1e23c4cf180e | 1.4864 | -59.9117 | 2026-03-03 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 2df5e8fd-fca9-3d13-b497-ba8657db75f5 | -21.6365 | -48.9883 | 2026-03-03 00:10:00 | GOES-19 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 3eaa7a53-e1be-3683-9360-f45ad2a8f15a | 1.5047 | -59.9116 | 2026-03-03 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 8993c425-fa08-33ab-8a3d-0ef2e3213428 | -18.7915 | -57.6312 | 2026-03-03 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.7 |
| a36b4b62-0685-3731-923f-9a6a2440a54a | -18.7915 | -57.6312 | 2026-03-03 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 9b2b3a32-7778-30b5-ab5e-da43fafa256f | 1.5047 | -59.9116 | 2026-03-03 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 479c1aa7-9ae2-3163-b714-174f1eb25f24 | -18.7915 | -57.6312 | 2026-03-03 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.3 |
| d9516ed3-702d-3264-a045-ae81515a0b53 | 1.5047 | -59.9116 | 2026-03-03 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 0d60d13a-4dc9-329d-ba9f-dd4046488392 | 1.4864 | -59.9117 | 2026-03-03 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 322bf04e-8348-35f1-b556-4637b2886931 | 1.5047 | -59.9116 | 2026-03-03 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e679e0a9-db45-37e0-8e4c-d8203e9a5a7d | -18.8115 | -57.6286 | 2026-03-03 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.2 |
| f319e899-c7be-387c-813c-7ab165469e8d | -18.7915 | -57.6312 | 2026-03-03 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.0 |
| 38882f7f-0842-371d-852c-493ef77de2a0 | 1.5047 | -59.9116 | 2026-03-03 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| fac893a4-2385-358b-a03e-e8f38e977898 | -18.7915 | -57.6312 | 2026-03-03 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.1 |
| a7eb9931-0c5f-3b03-a1fc-5f3baecf43fc | 1.5047 | -59.9116 | 2026-03-03 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6d73ab04-d14b-38de-849d-e0a8be9fe2cc | 1.5047 | -59.9116 | 2026-03-03 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 21adf798-7337-3d8e-95f9-3313bd823537 | -18.7915 | -57.6312 | 2026-03-03 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 158.4 |
| 4fe54b76-8529-3fec-8215-2b0fcad99a60 | -18.7912 | -57.6519 | 2026-03-03 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.7 |
| 2b3bcb2a-f635-3337-b229-4a6de3786587 | -18.8111 | -57.6493 | 2026-03-03 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.2 |
| dfeea593-2c6b-3e95-82b3-ab43f78578ef | 1.5047 | -59.9116 | 2026-03-03 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.6 |
| c7176605-ca2f-3fb2-bc62-48f5d5c493f1 | -18.7915 | -57.6312 | 2026-03-03 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.2 |
| f385dccc-ab2b-3f2b-bfa5-e44122fee50a | -18.7912 | -57.6519 | 2026-03-03 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.1 |
| c2936a74-a1f3-3cb9-b88a-a4c52181364b | -18.8115 | -57.6286 | 2026-03-03 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.1 |
| db1b3dff-bc8d-3c5f-9f6e-05bf2a9caabc | -18.79768 | -57.62368 | 2026-03-03 01:21:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 724e9dd4-43bc-3fda-a6b0-18c367961721 | -13.67756 | -60.64241 | 2026-03-03 01:21:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 79507103-4d65-388a-a68a-c433d4a6d585 | -13.65671 | -60.63958 | 2026-03-03 01:21:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 92e36486-ca23-36a5-bf63-561218a127f4 | -13.6594 | -60.65743 | 2026-03-03 01:21:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 594fc654-fe60-31ff-988c-48b905ae98b6 | -18.78848 | -57.63204 | 2026-03-03 01:21:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.6 |
| 173c5636-261c-33b0-86a9-b57da07938c5 | -18.79981 | -57.62988 | 2026-03-03 01:21:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.0 |
| bcaa4ce0-6ad5-3119-919b-d2667728c86a | -18.7911 | -57.64792 | 2026-03-03 01:21:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.0 |
| 4f66d1ac-4454-39ff-867c-85ef92699c5e | -13.65847 | -60.65135 | 2026-03-03 01:21:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1812c515-7279-3688-95d2-f9d5ae59a7f1 | 0.09275 | -60.61963 | 2026-03-03 01:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 24.6 |
| de5e3d55-a061-32f3-bce3-bb3afac37620 | 1.4995 | -59.91462 | 2026-03-03 01:26:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.5 |
| c48ac2a0-104a-3756-a3fe-5b4fa4c8eb12 | 0.31379 | -60.44255 | 2026-03-03 01:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 9828acf5-1a7a-3120-b7f6-24afd04032c8 | 1.51321 | -59.91691 | 2026-03-03 01:26:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 4228c844-9cea-3f55-9bfb-24cc1bb3b563 | 1.51006 | -59.93939 | 2026-03-03 01:26:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 7d0df56b-ac29-36a3-9e23-09798bc448f8 | 1.77938 | -60.53623 | 2026-03-03 01:26:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 15.5 |
| a7a1e54b-2086-3608-9e9b-aaabe8abda64 | 1.12609 | -60.52877 | 2026-03-03 01:26:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 65d56764-4108-3150-b1c0-30946b10293c | 0.46411 | -60.39359 | 2026-03-03 01:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 1cf4e3c7-73ab-3bce-907c-a6536a2b862f | 4.27076 | -59.90439 | 2026-03-03 01:26:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 65db9dda-5357-30f4-b1f1-467e3f39cac4 | 1.50574 | -59.92118 | 2026-03-03 01:26:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.5 |
| bfc155fb-dd4a-311b-9e14-4d180089aeea | 1.65048 | -60.24491 | 2026-03-03 01:26:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 15f5d2df-d013-36ce-b2fc-88075cc494b1 | 1.78955 | -60.54332 | 2026-03-03 01:26:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 1976df60-b505-3596-b902-26794bfa3323 | 0.09008 | -60.63881 | 2026-03-03 01:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 97c685c0-5806-373e-a362-c509ff740f4a | 0.87213 | -60.47525 | 2026-03-03 01:26:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 37099683-4664-3c8a-a023-89b68c787f4e | 1.48574 | -59.91259 | 2026-03-03 01:26:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 27.6 |
| fc02c3e8-6698-35cb-9857-8aabc1892d66 | -0.48924 | -64.60599 | 2026-03-03 01:26:00 | TERRA_M-M | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e50901a1-716b-3465-a96e-107a7f6ece1c | 4.27286 | -59.91037 | 2026-03-03 01:26:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 8220d28a-83bf-30ca-942d-380d930ca273 | 3.15565 | -60.70833 | 2026-03-03 01:26:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 34f1715a-6e5c-36d5-ba9f-757a70541627 | -18.8115 | -57.6286 | 2026-03-03 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.8 |
| 5ddd770f-58e7-3fe1-8a4e-c36d25fb353a | -18.7915 | -57.6312 | 2026-03-03 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 183.9 |
| ede2ec52-aed6-30e1-8859-00b9d41561bb | -18.7912 | -57.6519 | 2026-03-03 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.2 |
| 1c781b70-019a-3663-bbcf-b18b079a2b21 | -18.8111 | -57.6493 | 2026-03-03 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.2 |
| fe0540c5-dda4-31c6-b72e-3d3ba20bde55 | 1.5047 | -59.9116 | 2026-03-03 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 634d6f1a-a72c-3914-ae3a-22442dc1f500 | -18.8111 | -57.6493 | 2026-03-03 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.8 |
| d5a1bdf9-e52b-34d9-a8db-52d37b45a46f | -18.7912 | -57.6519 | 2026-03-03 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.0 |
| 19f81bfe-f735-3ade-8db9-d2957803a5cd | -18.8115 | -57.6286 | 2026-03-03 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.5 |
| 083f01a6-6f50-3cd8-ac96-bd67b3a6b083 | 1.5047 | -59.9116 | 2026-03-03 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 63f96ae1-e612-389d-a1ce-c8db53e740ad | -18.7915 | -57.6312 | 2026-03-03 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.5 |
| 8df6cfe2-212d-3ee7-974b-a18bc68fe053 | -18.8115 | -57.6286 | 2026-03-03 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 3ac114a2-09f6-33f9-8509-bf337bf59ccf | 1.5047 | -59.9116 | 2026-03-03 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 3c032797-4538-30e5-bd2a-67b39c632c49 | -18.7915 | -57.6312 | 2026-03-03 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.6 |
| 8dccba1a-90fd-35ed-a00d-0c90b4168a31 | -18.7912 | -57.6519 | 2026-03-03 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.4 |
| 1fde1061-0654-3920-96bf-56228aa352aa | -18.8111 | -57.6493 | 2026-03-03 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.1 |
| 5c8aa1a7-58bc-3fe8-aa20-f4dd7671b4de | -18.7912 | -57.6519 | 2026-03-03 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.0 |
| 3a7c24bc-3145-30ba-b8e6-f34030cdc506 | 1.5047 | -59.9116 | 2026-03-03 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 74dd6fa3-4c44-34ad-976f-61f853ffbea8 | -18.8115 | -57.6286 | 2026-03-03 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.9 |
| 565fff6e-6e88-336c-b56b-602b393f3657 | -18.8111 | -57.6493 | 2026-03-03 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.7 |
| 6e12541a-e0ba-37a5-938f-276f75c852df | -18.7915 | -57.6312 | 2026-03-03 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.6 |
| 2436e9d9-470d-3dbc-a09e-79f7a88f661a | -18.7915 | -57.6312 | 2026-03-03 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 4781add5-7731-3e99-82e3-8db264895604 | -18.8111 | -57.6493 | 2026-03-03 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 19ea026b-daa1-39bc-9524-167d88517f1e | -18.8115 | -57.6286 | 2026-03-03 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.6 |
| e19997ad-1e05-3079-ade1-3ab6dea9f934 | 1.5047 | -59.9116 | 2026-03-03 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a2a47f08-f315-3f27-a4f7-045c4a56aecb | -18.7912 | -57.6519 | 2026-03-03 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.7 |
| a29da791-d198-39aa-8324-2fef61057b90 | -18.7912 | -57.6519 | 2026-03-03 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.9 |
| 2c760903-a45d-304e-a469-7c517c95f351 | 1.5047 | -59.9116 | 2026-03-03 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 01bfb676-b2e9-384d-bf06-f72970b86b92 | 1.5047 | -59.9116 | 2026-03-03 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.9 |
| d7fe5bac-a017-334e-9aee-c9aa7bbfd287 | 1.5047 | -59.9116 | 2026-03-03 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| f9091d8b-357a-3ed2-a3d4-ce494a12c60c | 1.5047 | -59.9116 | 2026-03-03 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 879f905d-3af6-393f-963a-63ac721ce98c | 1.5047 | -59.9116 | 2026-03-03 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 45afa3b2-3c4b-3d4e-afa8-06031311d278 | 1.5047 | -59.9116 | 2026-03-03 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 720033a5-23e3-3b8f-98af-a732d7623e08 | -20.1828 | -45.41302 | 2026-03-03 03:17:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 3d7ab78f-e2b4-3174-af36-a17de1c4eea1 | -20.17873 | -45.41196 | 2026-03-03 03:17:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 0f3df810-76db-3f8a-b3b8-3839e9877c93 | -18.7915 | -57.6312 | 2026-03-03 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 142.9 |
| de6fa31f-9d3f-38f7-8b5b-2e8b6644ae35 | -18.7912 | -57.6519 | 2026-03-03 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 241.8 |
| fef2ff87-a632-3322-bf81-30e4413894f6 | -18.8115 | -57.6286 | 2026-03-03 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.0 |
| 73f43686-9f79-38bf-90ef-abf7b4fc9458 | 1.5047 | -59.9116 | 2026-03-03 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 35af15c3-844b-3935-85de-ccdbaf330515 | -18.8111 | -57.6493 | 2026-03-03 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 149.4 |
| c3a25c85-a647-3e25-8b83-8f51984a7dbf | -18.7912 | -57.6519 | 2026-03-03 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 263.9 |
| 10e705b5-7c05-36f7-936b-81564652c6e8 | -18.8111 | -57.6493 | 2026-03-03 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 180.2 |
| 72e7cb62-df30-3d7d-87fb-286c31eb7c95 | -18.7915 | -57.6312 | 2026-03-03 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 194.3 |
| 20f8dac7-8c9c-35b1-80e8-60ff42d2e881 | 1.5047 | -59.9116 | 2026-03-03 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| ced66c19-c343-3b2b-a4e6-70caabe16f2c | -18.8115 | -57.6286 | 2026-03-03 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 136.1 |
| b36e8da6-5160-326b-ac39-2474c8713dbb | -18.8111 | -57.6493 | 2026-03-03 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 189.2 |
| eb8cd90a-5223-3f1f-83fb-efa31c584da4 | -18.8115 | -57.6286 | 2026-03-03 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 146.6 |
| 60ee0632-e3c2-362c-a88f-d3b5d8fdc087 | -18.7915 | -57.6312 | 2026-03-03 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 214.8 |
| 4e9bd8ba-d75d-3b4c-b959-288c9b52edba | -18.7912 | -57.6519 | 2026-03-03 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 274.0 |
| 3d220c66-e950-3aca-9b55-fb9157a2b135 | 1.5047 | -59.9116 | 2026-03-03 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.7 |


[Clique aqui para ver as próximas entradas](README2.md)
