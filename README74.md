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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6ce0ec6-e94b-38c4-849b-73bc19ccd721 | -12.7017 | -54.6744 | 2025-09-14 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 148.3 |
| 1f74d38e-dd77-3691-b040-c0c5ec687539 | -12.6826 | -54.6763 | 2025-09-14 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 132.9 |
| a6526440-cfa9-349e-8efd-fa85f9a747c7 | -12.6824 | -54.6968 | 2025-09-14 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 734b134d-b32b-33ac-b1be-5fa266ed8096 | -11.8294 | -50.4763 | 2025-09-14 07:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| a5a85cdb-a638-3de6-87f3-ac63bd0b6947 | -14.2102 | -46.1979 | 2025-09-14 07:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 7e146cbb-3b26-349f-9549-5f6126ba42b8 | -12.9292 | -54.7538 | 2025-09-14 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 86c8f072-4b5a-32f3-9eaf-4676e13218ff | -12.9485 | -54.7313 | 2025-09-14 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| a9317032-890f-3a65-b047-ea844bdf5cf1 | -12.7014 | -54.6949 | 2025-09-14 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 53141e86-0a9f-3fba-a997-1fa7be1265a7 | -14.2107 | -46.1749 | 2025-09-14 07:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 3e7d76d5-70a2-365a-bb7b-525e0370a831 | -18.0303 | -50.9385 | 2025-09-14 07:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 49.5 |
| f6512ec5-9da3-31b8-991f-37284b394798 | -11.8103 | -50.4785 | 2025-09-14 07:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 06225a25-a114-3c69-8a19-8fff3d69d3ba | -12.6636 | -54.6782 | 2025-09-14 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| c44afd5a-5431-3cd7-b689-291c96b59718 | -12.9294 | -54.7333 | 2025-09-14 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 179.7 |
| 2f9571ab-1ebb-35a9-97c3-7ea4ac51acec | -14.7721 | -60.2107 | 2025-09-14 07:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| db12cc0f-7c70-340c-8ef6-9a5bb3864714 | -18.0308 | -50.9164 | 2025-09-14 07:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| e16a0dc2-7d59-3b60-9bd6-9a8b3c95d74b | -18.0502 | -50.935 | 2025-09-14 07:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 8879c28f-3bd9-3c82-ba06-7542341f0021 | -12.9294 | -54.7333 | 2025-09-14 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 186.8 |
| 5d1b89d9-b6b9-325b-81d5-38c2b0860390 | -12.9485 | -54.7313 | 2025-09-14 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| b3201186-594e-365f-961f-b8d9e048d990 | -12.7017 | -54.6744 | 2025-09-14 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 91455b77-c0e2-39b3-8726-49e36686a720 | -12.6826 | -54.6763 | 2025-09-14 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 90c29115-32e7-3b35-a410-5c71a0a03662 | -11.8294 | -50.4763 | 2025-09-14 07:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| dc159f7f-c7e4-39cd-b8f0-5a240c036729 | -12.7014 | -54.6949 | 2025-09-14 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 82f79255-929f-3e2d-a745-76078841497c | -12.9292 | -54.7538 | 2025-09-14 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 8638da32-6184-3b6e-a43f-abeaee79a8db | -12.6636 | -54.6782 | 2025-09-14 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a0cfa945-af71-32e5-8256-6be453f4b476 | -12.6824 | -54.6968 | 2025-09-14 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| df230ab3-33c8-3cc0-aa60-def55ada4f9c | -14.2107 | -46.1749 | 2025-09-14 07:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| e1a94393-f1e0-35cf-b6d6-2861b9977356 | -14.2102 | -46.1979 | 2025-09-14 07:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 7eeb31e0-fce3-364a-8173-5ebc10cbed4c | -14.2107 | -46.1749 | 2025-09-14 07:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 109.6 |
| fbdd1fd0-56c4-3055-a206-f3f704bff75c | -14.2111 | -46.1518 | 2025-09-14 07:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 29159300-f0ed-3032-9bdb-7881838b7ecf | -12.9294 | -54.7333 | 2025-09-14 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 230.5 |
| 4c14ed72-88a0-3d0e-ba96-aa5e176b1375 | -12.7014 | -54.6949 | 2025-09-14 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 22d9ec6c-e2b5-3399-a40c-2186927617c5 | -12.6636 | -54.6782 | 2025-09-14 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 68a4b091-d689-3787-8e1d-f20bb0555f2f | -12.9485 | -54.7313 | 2025-09-14 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 517f8aea-643c-3a11-be73-f24de4e5ed5c | -17.7176 | -50.7291 | 2025-09-14 07:50:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 2c8efa85-8c71-3e3c-bc75-a15efa397ccf | -12.7017 | -54.6744 | 2025-09-14 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 8f94a266-cc3b-36aa-adbd-3f6f45c25fe8 | -12.6824 | -54.6968 | 2025-09-14 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 6ad27908-9b5d-3c32-b5ea-6deaf390b3da | -12.6826 | -54.6763 | 2025-09-14 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 8de53607-a21e-3c6c-91fa-3be48acfe284 | -12.9292 | -54.7538 | 2025-09-14 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 1e4c4949-28ae-327c-b66e-93133cb2200e | -12.9103 | -54.7352 | 2025-09-14 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| f93f0a08-2be2-36d8-90b8-141a9d039ea1 | -12.9294 | -54.7333 | 2025-09-14 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 268.5 |
| 38e8945b-a7aa-31ae-b78c-0baf2ec53a8c | -12.9485 | -54.7313 | 2025-09-14 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| af29f95d-3140-3f29-a2c2-d50b6a0d4103 | -12.9297 | -54.7127 | 2025-09-14 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| caf9f300-d791-3173-8f4b-8fa0b4766eb6 | -12.6826 | -54.6763 | 2025-09-14 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 7c4ee781-0b0e-3de7-87ef-550c5df1bcb4 | -12.9292 | -54.7538 | 2025-09-14 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 9a61943e-cf72-3911-b423-3052b2a76f61 | -14.2107 | -46.1749 | 2025-09-14 08:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| b12ff9e7-7197-3805-9dc1-ad3869914670 | -12.6824 | -54.6968 | 2025-09-14 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 4b4c6b88-4f68-3288-b62f-d95afbab8be8 | -12.7017 | -54.6744 | 2025-09-14 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| ecff9f1a-8f53-3aed-8929-318e1b898259 | -12.7014 | -54.6949 | 2025-09-14 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| e9b8b1a9-55b7-3d48-9114-a518b4f0bd30 | -12.6636 | -54.6782 | 2025-09-14 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 05564f09-657c-3906-94d2-48273fa6539a | -14.2102 | -46.1979 | 2025-09-14 08:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 7ffbdf58-75b1-3bd1-bbb0-74405ed8224c | -12.9294 | -54.7333 | 2025-09-14 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| d6431746-9898-337e-9b6f-5bcac8da5e3e | -12.7014 | -54.6949 | 2025-09-14 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 9d9694a9-e03f-3e16-8e2f-7f3d4b8f7a68 | -12.6636 | -54.6782 | 2025-09-14 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 5925a85f-c82e-3bd8-951e-1f420ac7ffc8 | -12.7017 | -54.6744 | 2025-09-14 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 48dd82e4-00be-37d0-97b5-ac1800d165f1 | -12.6826 | -54.6763 | 2025-09-14 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 2b31d371-ee4c-3405-9512-5a382771d2ef | -15.8836 | -48.1574 | 2025-09-14 08:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 62.5 |
| ef50afd9-9ab5-3468-b877-eba3a5fecca4 | -12.9292 | -54.7538 | 2025-09-14 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| ff4e7ccf-1f3e-36d8-bbc1-2574037c66d1 | -12.7017 | -54.6744 | 2025-09-14 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 49ec111e-8478-31ac-852f-7fd8716adc8d | -12.7014 | -54.6949 | 2025-09-14 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 7115f54e-1a98-3982-8d4a-5591150f5b23 | -12.9485 | -54.7313 | 2025-09-14 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| e91f27c6-ae7d-3982-bd5e-1852f504f1fb | -12.6826 | -54.6763 | 2025-09-14 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| cd4e986e-1302-33a1-9941-498379f949c5 | -15.9032 | -48.154 | 2025-09-14 08:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 87.3 |
| adab4577-4407-3235-add4-1f1b98111207 | -12.9294 | -54.7333 | 2025-09-14 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 189.7 |
| 5d1fb846-1381-3f33-923d-41bd39c028a8 | -12.6824 | -54.6968 | 2025-09-14 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 4d0c0e65-401c-3604-9e5c-b1cf38a4ed91 | -12.7011 | -54.7155 | 2025-09-14 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 0d340868-9a27-39ec-ac2c-5382f9e57abc | -12.7017 | -54.6744 | 2025-09-14 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| c3f206fe-f18b-30ab-b61b-075174ed7f5b | -12.6824 | -54.6968 | 2025-09-14 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 8ded526c-7673-3e9c-9292-6d90de19df63 | -12.6826 | -54.6763 | 2025-09-14 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 047f1239-6799-3028-bb34-c7d5ad32d926 | -12.7014 | -54.6949 | 2025-09-14 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| f088c019-0317-339f-b04b-1dadc97e9946 | -12.9485 | -54.7313 | 2025-09-14 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ea76892f-a1e3-39cd-8224-f8979dc4190b | -12.9294 | -54.7333 | 2025-09-14 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 138.5 |
| c7f79c2c-953a-30de-8be2-dc22db266b45 | -23.758 | -51.8917 | 2025-09-14 08:30:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 54.3 |
| 6ae9050e-621a-3300-a8a1-96910a15d3a8 | -23.7574 | -51.9145 | 2025-09-14 08:30:00 | GOES-19 | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 150.3 |
| 27cd377c-cca2-3ad6-8c51-c45ab7a7dff5 | -12.6636 | -54.6782 | 2025-09-14 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| bf509b17-457d-347e-80de-5990173f18fd | -12.9292 | -54.7538 | 2025-09-14 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 6896b39c-cb2a-3359-8e41-367cef20f0f2 | -12.7017 | -54.6744 | 2025-09-14 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 5294ad03-368e-3493-9a81-cbc59b0bdf36 | -12.6826 | -54.6763 | 2025-09-14 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 5801e563-a96c-3780-9d46-f02078da6c87 | -12.6636 | -54.6782 | 2025-09-14 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| f9f885dc-8497-3471-af82-ed8b70686633 | -14.7721 | -60.2107 | 2025-09-14 08:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 23892680-cec0-387f-8238-2db24b9694f1 | -12.6826 | -54.6763 | 2025-09-14 08:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 500c70e0-f34a-3454-a87d-7768c9ec03b1 | -12.7017 | -54.6744 | 2025-09-14 08:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| a1c1f39b-b130-3879-8b4a-1f31a25971b5 | -14.7721 | -60.2107 | 2025-09-14 09:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 9a511cfe-0839-3f5f-89f0-7a3ace6b6475 | -14.7721 | -60.2107 | 2025-09-14 09:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 7fc10947-4b7f-341f-86e2-56b76bc882e3 | -7.1909 | -44.1426 | 2025-09-14 09:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 130.8 |
| e6df81b3-dfd1-3964-bc60-e123e641db9b | -12.7671 | -48.0236 | 2025-09-14 09:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 215.7 |
| 113d66be-4d0a-35bb-af11-be46f58de99a | -12.7675 | -48.0013 | 2025-09-14 09:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 41fdc142-1930-3db5-8b51-2df04b677183 | -7.1912 | -44.1195 | 2025-09-14 09:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 5166d3e1-80d6-3cf7-8380-b0d55ac590e1 | -12.7863 | -48.0209 | 2025-09-14 09:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 3bcdd4ef-0801-35a4-92a4-9c4cd5a5a8c5 | -12.7863 | -48.0209 | 2025-09-14 09:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 164.1 |
| f602346a-b1c3-3c14-afac-8605fc41a85a | -12.7671 | -48.0236 | 2025-09-14 09:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 279.4 |
| 693f535a-42c8-3035-9d48-631ddec1a3c1 | -12.7667 | -48.0459 | 2025-09-14 10:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| d5867397-d5bf-3473-a7d6-44f22c9ecf92 | -12.7859 | -48.0432 | 2025-09-14 10:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 3df4cee4-371f-3660-a395-6ecc21fd4fc6 | -15.9032 | -48.154 | 2025-09-14 10:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 101.9 |
| b6773d4c-3b79-3e04-91d5-4acc4bcfa67f | -12.7863 | -48.0209 | 2025-09-14 10:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 256.4 |
| a058c9a9-0946-3d04-ab74-895c5576a071 | -12.7671 | -48.0236 | 2025-09-14 10:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 259.7 |
| 33211b99-69ce-3ab3-8a6c-00a999bd402b | -15.9032 | -48.154 | 2025-09-14 10:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 439aa464-569d-337c-a11f-6d89b6cbf63c | -10.7503 | -46.4381 | 2025-09-14 10:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 541b04db-aea9-3965-b753-7e23afe58351 | -10.7503 | -46.4381 | 2025-09-14 10:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| bdcdebc2-95c7-350a-9aa9-cf8db708e752 | -11.7716 | -50.5258 | 2025-09-14 10:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 0f5f102a-978c-3bb4-9df2-63ebb24efe72 | -11.7522 | -50.5494 | 2025-09-14 10:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |


[Clique aqui para ver as próximas entradas](README75.md)
