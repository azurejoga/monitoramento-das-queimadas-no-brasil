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
| 8bd86d94-bb75-33f3-bded-edf946d121bb | -23.8738 | -49.99398 | 2026-03-04 04:38:00 | NOAA-21 | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b9f4c649-d1a0-3337-867a-7375fc1d2d97 | -21.60619 | -56.62733 | 2026-03-04 04:38:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1f7cec4-b5d8-358b-a18e-7e0491fa5659 | -20.94426 | -48.71367 | 2026-03-04 04:38:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7130346d-2dfd-3afa-bfa0-96aeca938ad8 | -21.31603 | -48.53613 | 2026-03-04 04:38:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a313192b-ab35-3489-b35a-5ec1f4cb916b | -18.54198 | -55.04827 | 2026-03-04 04:38:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0289e1d6-5cd6-395d-aa93-63618a8a08de | -22.91633 | -48.60674 | 2026-03-04 04:38:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f24566ac-035e-3203-a7fb-578d8f1d503f | -22.91572 | -48.61116 | 2026-03-04 04:38:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37ac07c5-2eaa-3d34-9f9c-3e56e286a783 | -20.30421 | -49.58205 | 2026-03-04 04:38:00 | NOAA-21 | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3addc78a-528b-39a4-891f-a7fd8c4588d0 | -17.96364 | -52.66103 | 2026-03-04 04:38:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| cb1f9e58-49a7-3ed9-a964-ed320821c52c | -18.81013 | -51.60208 | 2026-03-04 04:38:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfd80607-1fc0-3dac-9f02-6dabaca4a0be | -24.73246 | -48.58157 | 2026-03-04 04:38:00 | NOAA-21 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 22c5ef1e-7ccc-3852-a965-6d9f9986991a | -18.81345 | -51.60266 | 2026-03-04 04:38:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c27f8b87-7146-3584-b774-6627414666d6 | -18.80622 | -51.60516 | 2026-03-04 04:38:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5c188b2-feb0-3924-8a5a-46c7c00dc20a | -22.40261 | -48.13747 | 2026-03-04 04:38:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 364000f3-02ed-3be5-8965-0c88196bc739 | -18.70051 | -42.9821 | 2026-03-04 04:38:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4e2c8819-31d2-3e92-ae08-068f4cbc14aa | -18.80895 | -51.60941 | 2026-03-04 04:38:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f70f987-a78c-305e-825e-5bb3bb60d37f | -23.03964 | -47.88038 | 2026-03-04 04:38:00 | NOAA-21 | LARANJAL PAULISTA | SÃO PAULO | Brasil | 3526407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0a994fdb-beec-3f94-9cb4-af763fc0c06b | -20.80984 | -49.83598 | 2026-03-04 04:38:00 | NOAA-21 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 75ca4a58-9842-333b-897c-8bca28cf5f40 | -23.87322 | -49.99807 | 2026-03-04 04:38:00 | NOAA-21 | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| be79cd78-5145-36a9-8ba0-913330124dd2 | -21.70408 | -56.32072 | 2026-03-04 04:38:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f917fa09-c542-38cc-a6f8-c3197f08be53 | -16.58604 | -58.21827 | 2026-03-04 04:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 0caa5c75-4d65-388d-838b-fcb89362d994 | -20.82068 | -48.28151 | 2026-03-04 04:38:00 | NOAA-21 | TERRA ROXA | SÃO PAULO | Brasil | 3554409 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ace42491-1c14-3b83-a6f4-5f79579a090d | -18.80954 | -51.60574 | 2026-03-04 04:38:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4be6e364-7a94-3fbe-9b07-19527bb4b940 | -19.27314 | -49.42205 | 2026-03-04 04:38:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b054933e-209a-343f-9835-f308fa6f79e2 | -20.24971 | -50.53835 | 2026-03-04 04:38:00 | NOAA-21 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bff4ade1-3aba-3a2b-b48f-7af1d528339a | -20.30759 | -49.5826 | 2026-03-04 04:38:00 | NOAA-21 | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 159557c4-c9fe-318b-b619-117d77286119 | 1.5047 | -59.9116 | 2026-03-04 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.6 |
| aa7037d1-ee30-37b6-a0cd-36b448b9f22d | -29.95221 | -51.61868 | 2026-03-04 04:40:00 | NOAA-21 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 0653d47e-1eef-32d0-bfbe-381dc5587666 | -28.35048 | -49.10679 | 2026-03-04 04:40:00 | NOAA-21 | BRAÇO DO NORTE | SANTA CATARINA | Brasil | 4202800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ec2a6221-750f-3b78-a051-0cd2ed356470 | -25.21933 | -53.28574 | 2026-03-04 04:40:00 | NOAA-21 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2818e2d0-2240-3775-a634-9216c0a18a6d | -26.99597 | -50.58626 | 2026-03-04 04:40:00 | NOAA-21 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dd4c86a2-65dd-3cfa-a67e-051bf8b7c3bd | -25.00999 | -49.30167 | 2026-03-04 04:40:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 597cf153-53bb-3587-8fb6-c25bcb62cd7b | -29.79939 | -51.50955 | 2026-03-04 04:40:00 | NOAA-21 | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| e1a43235-9a9f-3b6e-b670-1cecb252725e | -27.18991 | -51.7678 | 2026-03-04 04:40:00 | NOAA-21 | JABORÁ | SANTA CATARINA | Brasil | 4208609 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 38889700-45c4-33da-8b44-91a4482c4622 | -27.19049 | -51.76385 | 2026-03-04 04:40:00 | NOAA-21 | JABORÁ | SANTA CATARINA | Brasil | 4208609 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d2bd7411-89b1-3bf3-a62e-d83ae34f0209 | -26.99538 | -50.59046 | 2026-03-04 04:40:00 | NOAA-21 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5f6a6db8-4190-3c81-a67d-1a25365701bd | -27.34901 | -51.44775 | 2026-03-04 04:40:00 | NOAA-21 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 595fa5c8-3046-3ee7-86a6-5c7da9ba924d | -29.80282 | -51.51018 | 2026-03-04 04:40:00 | NOAA-21 | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 9c7e7b3e-486c-3b6c-8e6d-fa2b5efcfcf1 | -29.92826 | -53.02862 | 2026-03-04 04:40:00 | NOAA-21 | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 4703dfc4-586e-30fb-8d02-5b1bbef2b7fa | -26.5006 | -52.17395 | 2026-03-04 04:40:00 | NOAA-21 | ABELARDO LUZ | SANTA CATARINA | Brasil | 4200101 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a36f1bf7-8e1a-3425-8c16-128bb3f9b06b | -25.09806 | -49.16227 | 2026-03-04 04:40:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5f98a309-73eb-3532-9126-9a078e25c9ed | -31.6972 | -52.63251 | 2026-03-04 04:40:00 | NOAA-21 | MORRO REDONDO | RIO GRANDE DO SUL | Brasil | 4312450 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 78513a99-12be-386c-a398-0b1303c29b70 | -31.32511 | -52.49134 | 2026-03-04 04:40:00 | NOAA-21 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| d7e848da-43f4-32aa-9e12-a42b7f73cd39 | 0.0455 | -60.9988 | 2026-03-04 04:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 68977013-3965-32fd-925c-3daa87204949 | 1.5047 | -59.9116 | 2026-03-04 04:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| d97fe2f1-fe2a-372b-a450-ab7659fb61a6 | 0.0638 | -60.961 | 2026-03-04 04:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 44.9 |
| c687b662-8d8f-3b06-ab62-ff9c77aecdfe | 0.0455 | -60.961 | 2026-03-04 04:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 157.2 |
| cdf5c76e-49d6-37f0-8131-47d6745516de | 0.0455 | -60.9799 | 2026-03-04 04:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 424.9 |
| 513a490e-3911-34f6-8adb-358ce04a4dfc | 0.0638 | -60.9799 | 2026-03-04 04:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 88.5 |
| a85c0029-581f-3665-a095-ab22ccc34fdd | 0.0273 | -60.9799 | 2026-03-04 04:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 52e970ce-bc93-3be8-8396-b2b32f356604 | 1.5047 | -59.9116 | 2026-03-04 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 39f46cbd-9381-3028-9d4e-4d307c941cf2 | 2.92893 | -60.46365 | 2026-03-04 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6113bf86-85b3-38d6-94b2-d7cda2779951 | 0.16269 | -60.4904 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1555a956-96d0-37f8-b0bd-ee2c1d8bf29a | 0.06274 | -60.99205 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8887d388-1f36-3978-bb99-23401b490b0a | 2.65672 | -60.10447 | 2026-03-04 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06798a11-24f9-3bc0-a4fc-0379e0a76d28 | 0.08659 | -60.62692 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b8ede28-400a-36f9-8ada-2e600d7e22a9 | 0.49748 | -60.51035 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f472868-107d-36bd-b874-f6530a2bdef4 | 0.30437 | -60.4561 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e03c903b-a42c-3131-8bb7-919383418a43 | 0.9497 | -59.44838 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81e93040-cfa1-3878-a9f0-081c2c8a0b27 | 0.73057 | -59.90551 | 2026-03-04 05:01:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e40a0c98-9af5-3612-95ed-ef4be8a3209c | 1.07324 | -59.25408 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5602f64-bc21-3be2-824f-79cd45afdad6 | 1.34988 | -60.02468 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f11f1721-cc4c-3d7f-9fea-8337158dbd2c | 0.65366 | -60.37286 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 577cd02c-bc83-3927-9e7f-aeafc05b49b3 | 1.5152 | -59.92995 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 152da6ce-1ab3-3265-9afc-50a2af32760a | 0.05579 | -60.98087 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 41362820-7e63-3740-8dc8-c60ee51970c3 | 1.11105 | -59.19487 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d342271-c486-3ad8-bd2b-2927ca1365bb | 0.04668 | -60.98864 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 9f182482-e669-3075-9b85-4640f8d1ce03 | 0.04211 | -60.99247 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 82eab4d0-14a1-3e1c-88eb-9fc40c692137 | 0.49343 | -60.5167 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0cfc516-5c0a-3784-84c5-77af5a148a92 | 2.9234 | -60.46145 | 2026-03-04 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48363c31-40fd-385d-916e-b9bd22c058d8 | 3.05594 | -60.64476 | 2026-03-04 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2a7e0da-46a2-37b3-b4e3-8004bcdf2958 | 3.02026 | -60.65333 | 2026-03-04 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3f0dab5-0115-372d-af14-e1f9f1b5294c | 0.04072 | -60.98363 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 8352ed79-e4b5-35b3-8077-2af077567231 | 0.96726 | -60.2398 | 2026-03-04 05:01:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32ca9e55-5dcb-35ca-99ba-53daba5c8e38 | 0.93077 | -60.53782 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4febb981-92d1-3ecb-9ab2-0c211f13bdc3 | 3.0513 | -60.64215 | 2026-03-04 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49bd08df-e5e2-31ca-b22e-5f2bba014535 | 3.03528 | -60.64791 | 2026-03-04 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5795b680-17a8-3ebc-90c6-b721fc7f8787 | 2.92606 | -60.46501 | 2026-03-04 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 293eaa77-6bc9-3834-8988-23ec6a66d74f | 0.16184 | -60.48492 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5273417e-19e6-3c0a-9c81-ff0f2608278d | 1.11174 | -59.19943 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8b68d3c-1daa-3da6-aaf9-b9fd84b15f4d | 0.49257 | -60.51119 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69b0a8fe-e6af-3d16-9d4b-040ddab55993 | 1.34505 | -60.02538 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 483f9c4b-a0e3-3bda-a8b9-d2f69ae4c1fe | 2.92384 | -60.46443 | 2026-03-04 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cc9b0724-c56c-3e48-ac50-c5a615f943ab | 0.03613 | -60.98736 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 1cfca4ed-8aa7-3e2b-b738-6c989f972fcc | 0.09151 | -60.62613 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbfba687-0006-378c-bec9-df41caa544f4 | 1.11596 | -59.20056 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98bfb1d9-c142-37fc-8212-56aebcd14bf1 | 3.04514 | -60.64327 | 2026-03-04 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cba13c6-088d-36e3-87f9-c79a20b803dc | 0.05534 | -60.97798 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e5b3a6b3-4b4b-3a83-8f7e-b2e3eaee02cb | 1.11523 | -59.19601 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52222fc2-1443-39b2-912c-979ca4a532d1 | 3.0503 | -60.64248 | 2026-03-04 05:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b12ad39-2619-3474-b8e1-bf42153d85a9 | 0.05996 | -60.97454 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77df83d2-8767-3dd5-a203-b1ae6bfed8f8 | 0.06323 | -60.99512 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6c013c5-ba8d-3d43-a083-5944fc3519ec | 0.65064 | -60.37239 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e9891db-c56a-3ace-9af8-ac2881c906f7 | 4.04392 | -59.8686 | 2026-03-04 05:01:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ed5a989-b529-3703-9c8a-8985368cb872 | 1.02105 | -59.79627 | 2026-03-04 05:01:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e045759f-7f6c-3cf1-bb7b-8118dbb4ba5c | 1.49758 | -59.91137 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8910292a-d6ad-32f9-b55c-f0a4255e018a | 0.28415 | -60.61596 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 932220be-c4cd-3f3c-8e9d-d9a6f3fbbfde | 0.0366 | -60.99036 | 2026-03-04 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| e8b11c3c-3ec3-3fd7-a243-16dce06fb076 | 1.07779 | -59.25335 | 2026-03-04 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4ee5a77-ef63-355e-a6e1-1f86c3a842b0 | 1.51121 | -59.93589 | 2026-03-04 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README5.md)
