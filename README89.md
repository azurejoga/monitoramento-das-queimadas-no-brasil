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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed9f9c22-22f3-3fd8-82b4-f503bb09c84f | -16.96388 | -56.78561 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5a41a6fe-f96b-3ebc-8fe8-e1dcf218a27d | -16.98385 | -56.74243 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f78b3d90-8a00-3b79-a8ed-8ea0e67a764b | -16.98314 | -56.74594 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| d9b69bc2-0f43-3646-9a42-7ff3640d9462 | -16.98171 | -56.75292 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| af8bd225-979d-3c89-b099-73bc7dd71658 | -16.981 | -56.75642 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 7fa3b2c2-44b2-34dc-97bd-d0ce01c43372 | -16.98029 | -56.75993 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 153d7e78-c9c6-36f8-903b-c65dddb85841 | -16.97352 | -56.76575 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 9be59cd4-206c-3b4a-984c-f44fe266c02a | -16.9682 | -56.76452 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 78ccbd4a-40cf-396a-8529-d1d823375ab7 | -16.96072 | -56.77383 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 5534106b-57f7-3eb0-898c-d033df949d94 | -16.86094 | -56.73111 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 321dc858-a379-380f-a80a-bb4d3165a2df | -16.86021 | -56.73464 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8740275d-103c-3364-a8c0-95abf1f12598 | -16.84956 | -56.73219 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 10199754-5096-3ab1-ba5c-463406ad0996 | -16.84884 | -56.7357 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1f28e57f-4a34-3895-b200-303747d3c348 | -17.026 | -56.74186 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 04c8d508-9315-31d3-a976-2e8d48451e65 | -17.02433 | -56.72323 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 384125d6-0ad8-30c1-b738-0b857369b391 | -17.02338 | -56.70118 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| de800a93-9b81-32ce-8b01-0d999b0b4cc2 | -17.02287 | -56.73018 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 60282e9d-f97b-35a8-923d-7ed63a04a0d3 | -17.02193 | -56.70813 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4f750492-1d6f-36a6-899e-e042b7412cce | -17.0212 | -56.71161 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e4ec5331-7d40-3914-92d6-3a0f7dae2501 | -17.02047 | -56.71508 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e3b3a495-3b6a-39ea-aa8f-3b71d12004dc | -17.02031 | -56.69962 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 18a2c6e0-3650-3b88-b43c-919f7272fddb | -17.01974 | -56.71856 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b6a4790a-e3f6-3686-aeb0-665962349bc6 | -17.01961 | -56.70309 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7f1ce848-6a28-3bf9-802d-6c999c834233 | -17.0189 | -56.70659 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 24fff77b-6deb-3c1f-b54f-95c6527ba8c4 | -17.01819 | -56.71008 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 676a2234-f242-3b69-a49e-8008ef93a387 | -17.01808 | -56.69997 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 54e006e1-de1b-3a0d-8090-52ae4514ef43 | -17.01756 | -56.72897 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| cf7b299a-4ec0-3e4f-8746-5bca1ed05480 | -17.01749 | -56.71358 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 529ee9b1-7445-3206-baad-c27e3c8f38fb | -17.01663 | -56.70692 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 28fc9f5b-63e1-39b0-94bf-18eca2e3de60 | -17.0159 | -56.7104 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 5db92422-416f-3dde-90c6-c46b0e198195 | -17.01538 | -56.72403 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| ee225128-8b6f-3760-8c12-cd91a3adb310 | -17.01468 | -56.72752 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| dc79db4e-abd7-375f-a787-1bed2fd3654e | -17.0143 | -56.70189 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b4553db9-5aa5-370c-b238-6c96b51cb2fe | -17.01397 | -56.73101 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6ed05ba7-00a9-390a-9c02-fdac3f7eebd6 | -17.01278 | -56.69876 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a83260d1-6144-335b-8947-00d0173a0e2b | -17.01219 | -56.71236 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 933585de-53f9-3e6f-b8cb-fc6ec14ec8d4 | -17.01205 | -56.70224 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 851e0ac2-07d9-34f9-9bbb-26a69470e528 | -17.01153 | -56.73125 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 7ebfcd0c-6322-3346-ab9c-0dbaa0d9fbe5 | -17.01148 | -56.71584 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 0c21b283-48e9-3188-85aa-6c1674bc4baf | -17.01132 | -56.70572 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c1dd71f7-4784-3ca0-a9da-6081309bf093 | -17.01078 | -56.71932 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 9539f1a3-7e02-3f23-a9bc-e697bb087f69 | -17.01059 | -56.70919 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| ad19f529-95bf-3181-a07c-2137ecfbab4c | -17.01008 | -56.72281 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| cec7d8fa-e367-390e-abb4-aaaa1547d735 | -17.00986 | -56.71267 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| b6edf356-4d57-3eb5-9f87-efaabeb70667 | -17.00971 | -56.69717 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b1fa0b15-abc9-3a77-86fb-4d70790e5d11 | -17.00937 | -56.7263 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| e2f084e3-b1bd-3461-a203-260ee908eb26 | -17.00914 | -56.71614 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 70aca042-ff2f-38d4-8557-f825d5453681 | -17.00841 | -56.71961 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| e7c05298-5281-3b5e-b8d7-5d86a7bc51c0 | -17.00768 | -56.72308 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 6c037b30-9d5d-31d8-a44c-b5de3f863d43 | -17.00675 | -56.70103 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5354e95e-62a9-3be7-8e36-b2ab30c8b46b | -17.00622 | -56.73003 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d94a4984-07ce-33ac-95cd-9f323502bdb9 | -17.00603 | -56.7045 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| fbece1ec-d273-324f-a4c9-c5baf521c911 | -17.00475 | -56.73702 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| dc417baf-369b-3279-86f8-32e09579725e | -17.00406 | -56.72507 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e7715b04-0071-3737-8251-3f573c2d69f5 | -17.00336 | -56.72857 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| fe966052-5a71-3226-98e7-f5b145618c90 | -17.00265 | -56.73207 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 36c32c6e-0bd9-335f-920b-6ac56e300537 | -17.00229 | -56.70642 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| af4a11b8-8a3b-30ad-95c7-fa5140e8499f | -17.00193 | -56.73557 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 9ec8be1b-59bd-3ad4-b066-08def9c906bb | -17.00091 | -56.72883 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| bb7d0def-3bde-3be3-b495-7e3cb888e0ac | -17.00018 | -56.73232 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 84a3c150-373f-39b7-924f-680e0c7670db | -16.99944 | -56.73581 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 1935867a-3b87-3f28-ae09-29f962d2718e | -16.99662 | -56.73436 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 8fda0fe8-b374-3184-93c6-5fca4e2551a3 | -16.99628 | -56.7087 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 4e04f763-6151-30cd-90dc-9d2c0f350f55 | -16.99591 | -56.73786 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 8ce53598-2bfc-31b6-9392-c5dc5823e1d0 | -16.99486 | -56.73112 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 616b03ff-0084-39c0-9d0e-b3ec11c1f8ef | -16.99339 | -56.73811 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 5d0a2b89-de33-3a9f-abf0-a1bf9ef97adb | -16.99097 | -56.70748 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 5c111ec9-a3cc-351f-a44a-a9f4f1d40843 | -16.9906 | -56.73664 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c556fc01-c218-347c-98ed-5c26fde56c38 | -16.99027 | -56.71096 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| adc1b91f-c533-3524-afe3-5bdc04a405be | -16.98917 | -56.74364 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1f25fb94-6c0d-3ca6-b11d-50ca10f9ee4a | -18.8803 | -57.69338 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| ea76199c-2fe1-35ec-8222-9468fc704548 | -18.87997 | -57.69422 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 890b4328-30c9-3048-90fc-eb9c0f6a31db | -18.87843 | -57.72837 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 08d93335-7cb3-3b33-8e6e-315981edcf71 | -19.11027 | -57.47195 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 176ffe89-5213-34a7-ad18-34e49af38ab4 | -19.10962 | -57.47501 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 51043901-01be-3aa2-9be7-509acee9b92a | -19.10785 | -57.48338 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ab5b8506-42ab-3c93-8767-3c447975dd3d | -19.10247 | -57.48224 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f687fcdd-8a7e-33eb-a9fd-9242a03d7471 | -18.72276 | -57.36184 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2ac5b7a9-3525-3e23-8bc1-91165ad1b708 | -18.72063 | -57.36187 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| f48d6ae2-8647-3165-90b1-2b269b97af08 | -18.71989 | -57.36546 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| d059dd41-5c8c-3c26-8768-a209c591040b | -18.71742 | -57.36057 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| d1eddc2d-1a12-3d96-a6af-49d42ee76b3b | -18.71665 | -57.36414 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| a56dbe12-3024-3dab-9494-098ee0311204 | -18.71529 | -57.36059 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| c9e9dce9-8851-36ac-b218-bca6b6421c2b | -18.71454 | -57.36417 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 4d76333d-6830-3459-975c-e3d356719107 | -18.7138 | -57.36775 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| f6cf2c97-cf90-3e9a-831b-3bf0f04e68ba | -18.7113 | -57.36288 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| c6ab5b9f-1158-3bbe-bb28-005993b17bdb | -18.71053 | -57.36645 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| a5918f73-82df-312c-800e-7bf9fc6523fa | -18.7059 | -57.29843 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0670c026-db4b-34f2-b254-1f932ba5ba84 | -18.7043 | -57.27942 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1a84711d-11b4-306f-8c94-60deef184221 | -18.70356 | -57.28296 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 49e805b9-9b5b-35dc-bed3-8f30edf093bf | -18.70282 | -57.2865 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 57bef9b7-4081-3748-bc92-d5b322835b30 | -18.70207 | -57.29005 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 26c14da4-5cd1-3151-b9fa-42ff30fa8299 | -18.70058 | -57.29715 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f4d0eb73-581a-3dcc-afc6-54705d912e45 | -18.69983 | -57.3007 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e2a53076-6c9b-3683-bf7a-46613ff907f6 | -18.69973 | -57.27462 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 488e88f8-b86c-355d-a4ca-b6c9981cccd0 | -18.69441 | -57.27336 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 33363beb-54eb-3b4b-b316-0110f5e99700 | -18.68985 | -57.26855 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 63b30c15-d8a3-364b-b3e3-27209ca30f10 | -18.6891 | -57.27209 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 52a82e65-24dd-340b-8063-4ad53546e433 | -18.68453 | -57.26728 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b350f2b7-3489-3bff-9ea0-869bd04bf0d9 | -18.67922 | -57.26602 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |


[Clique aqui para ver as próximas entradas](README90.md)
