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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f664cef-3266-38cf-a6a1-e6ef8883824d | -9.5006 | -55.9588 | 2025-09-13 02:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 87cade4d-d15b-31ee-93c6-90537ecdc920 | -12.1232 | -47.6013 | 2025-09-13 02:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 6cf5c8d8-ed1a-3046-b8f5-42b48587a957 | -16.0796 | -49.993 | 2025-09-13 02:10:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 8bc108cb-cf06-3639-85f9-b68652546cfc | -12.006 | -47.7505 | 2025-09-13 02:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| b53699d8-d350-3f18-af3e-702f3fe4594a | -9.5135 | -54.6494 | 2025-09-13 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 411efcf7-75e9-3b94-8d9e-10f32863d7cf | -9.2658 | -59.3997 | 2025-09-13 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 229.3 |
| fa4469b5-b98e-3315-ac8e-806ed1c5645d | -9.5137 | -54.6292 | 2025-09-13 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 703da591-82bb-3212-b3f2-49a22f46c1e6 | -3.2282 | -47.6371 | 2025-09-13 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| b7145ac9-36d8-3047-a7ab-4c7ae1699400 | -11.8468 | -50.5813 | 2025-09-13 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| f59fbbce-be98-3a44-a4a6-5ccdffbf0a82 | -12.1236 | -47.579 | 2025-09-13 02:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 39313065-907f-3fc4-837e-8f11099764f1 | -9.2503 | -51.2472 | 2025-09-13 02:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| a1635233-956f-3189-8fba-07a4ec978ea6 | -9.2656 | -59.4191 | 2025-09-13 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 238.0 |
| 1a0746ae-a207-3b45-a2e6-a5bc03ddca11 | -11.1494 | -45.317 | 2025-09-13 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 523915ee-15f8-37e8-99e4-336eaecc3e73 | -11.4076 | -50.7378 | 2025-09-13 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 7c11209d-9d4a-3b4c-9835-80e573167eda | -17.8434 | -50.4201 | 2025-09-13 02:10:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 3755ead7-2c36-3df1-bdf2-222d41321b18 | -9.2472 | -59.4007 | 2025-09-13 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 2051e322-f328-35fa-ac4f-d1c05410c63c | -12.9292 | -54.7538 | 2025-09-13 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 0470ee95-6595-3fd3-b585-81bbbdfaa626 | -11.8659 | -50.5791 | 2025-09-13 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| f1a89628-1af6-3678-84fe-af76871ab324 | -9.5004 | -55.9788 | 2025-09-13 02:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 5942a388-3622-3f6d-b75e-904017751165 | -16.0257 | -47.9294 | 2025-09-13 02:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 51.1 |
| d688eec9-7f9e-39ce-ad93-425f30720efe | -9.5324 | -54.6277 | 2025-09-13 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 24660df4-0ad8-3ff3-a226-4dc786d2e7d6 | -17.8439 | -50.3979 | 2025-09-13 02:10:00 | GOES-19 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 235.4 |
| 62ed7da6-84ea-3689-a7a0-194d4f98a0f5 | -16.0599 | -49.9962 | 2025-09-13 02:10:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| c6fd56ee-7ad4-337e-a132-0ceee6100359 | -9.247 | -59.4201 | 2025-09-13 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| a9dac411-c5d7-3613-aaac-e3f4b84c4f23 | -11.1896 | -51.419 | 2025-09-13 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 105.7 |
| bdb716bc-2e42-3b2a-a237-e8cd96125f8e | -11.7388 | -46.6005 | 2025-09-13 02:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 5af0636c-7ecd-3195-89b6-2a0a5e7182c1 | -11.1706 | -51.4209 | 2025-09-13 02:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 9faa2f5d-d051-3103-8f7e-623fe8215ca1 | -3.2321 | -46.7836 | 2025-09-13 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 4aa99881-8716-32c4-9d28-452c062d3e63 | -17.824 | -50.4014 | 2025-09-13 02:10:00 | GOES-19 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 7ab0d783-e429-378a-b393-a1d16619515d | -21.6187 | -46.8115 | 2025-09-13 02:10:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.1 |
| 1ba8d99a-673f-345e-8466-5f8e5edcfe57 | -11.1706 | -51.4209 | 2025-09-13 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 13377a89-9fae-3143-8cde-253cb5c51c72 | -16.3614 | -51.5403 | 2025-09-13 02:20:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 501b3a30-d87d-3871-b204-338ed1144494 | -9.5137 | -54.6292 | 2025-09-13 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| cc3ffa2f-fac6-3391-8cbf-51f9be1335e8 | -11.0752 | -51.4731 | 2025-09-13 02:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 21863f2d-88d2-33ac-b03b-252a1190f79f | -9.232 | -51.2067 | 2025-09-13 02:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| a21e467e-6e9a-3dc7-afa5-287db3e873aa | -9.2472 | -59.4007 | 2025-09-13 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 2d255a41-178b-35f5-a099-402c172fbdbb | -6.3503 | -35.1871 | 2025-09-13 02:20:00 | GOES-19 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 74.0 |
| 878d9c70-e7df-3d18-b85f-134691f615f3 | -13.0891 | -48.2663 | 2025-09-13 02:20:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| ccd4c7ae-c8c7-3cbe-8888-ea5e849637bc | -16.0796 | -49.993 | 2025-09-13 02:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| ae8b8c3b-8e84-3a0a-b992-d822b6481611 | -9.247 | -59.4201 | 2025-09-13 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| e65b1d3e-93e4-346e-904f-b734b44f29f7 | -3.2321 | -46.7836 | 2025-09-13 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| c4823da0-9176-32c6-8344-9eb769073db4 | -11.0942 | -51.4711 | 2025-09-13 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| b1c92503-e8c3-37e9-9841-414e6e3bcc95 | -16.3422 | -51.5217 | 2025-09-13 02:20:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| de821090-7298-3cd3-9cc3-d273655409f5 | -9.2656 | -59.4191 | 2025-09-13 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 213.5 |
| 358b7f81-d7e5-39f1-b1aa-ec1bf717f753 | 0.6904 | -50.6481 | 2025-09-13 02:20:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 082bf28b-0140-37c6-a713-acde31114125 | -9.2658 | -59.3997 | 2025-09-13 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 190.0 |
| bb2f590e-8657-3c38-b670-3768c56a6191 | -9.2843 | -59.418 | 2025-09-13 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 2a94056e-b536-3165-bd6c-66fb09f1a95e | -11.8468 | -50.5813 | 2025-09-13 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 6612719e-bc7f-37a8-9b1a-70ecd029641c | -3.2282 | -47.6371 | 2025-09-13 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 2140c434-5010-392f-a0cf-d672b5f706cf | -12.0056 | -47.7728 | 2025-09-13 02:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 649a308f-5c27-344f-a6bc-23fd133b80a9 | -9.5324 | -54.6277 | 2025-09-13 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| c84dd9ba-1b8c-3b90-b742-d46b85baf34c | -9.2317 | -51.2278 | 2025-09-13 02:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 193f783f-10d1-320a-baa0-37353ecc6e40 | -16.3418 | -51.5434 | 2025-09-13 02:20:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 8b6dc037-8ba6-3540-bf7b-6bd07cbb983f | -9.2505 | -51.2261 | 2025-09-13 02:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 4e9f013c-62fe-345a-9b54-e810d1ba4f76 | -17.8434 | -50.4201 | 2025-09-13 02:20:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 2d091ea3-ebb1-3035-907a-3d3ffce7cc44 | -11.4076 | -50.7378 | 2025-09-13 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 80a428eb-c714-3ef7-95ee-787274e61a71 | -16.2546 | -50.0524 | 2025-09-13 02:20:00 | GOES-19 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 9918dc73-8f2f-3cbf-8f24-72122303e23a | -9.5139 | -54.6089 | 2025-09-13 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 2cd484f5-627e-3730-91d8-0f47d57cbb1c | -9.5004 | -55.9788 | 2025-09-13 02:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 3a73633a-82f3-3801-b808-9deaf6ab0402 | -9.2503 | -51.2472 | 2025-09-13 02:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 8905a042-306b-349d-831f-92a4a5b7eea9 | -11.9869 | -47.7531 | 2025-09-13 02:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 666060d1-594f-3eb1-9691-50211190a54f | -3.2283 | -47.6154 | 2025-09-13 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| e64c858f-bfc1-3817-9999-ec9c76bdd07a | -11.0945 | -51.45 | 2025-09-13 02:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 3eb67627-278d-35c4-bb27-25f888212b4a | -15.1165 | -52.4918 | 2025-09-13 02:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 4f11efcf-08dc-3572-9e22-ac489df7c3f0 | -3.2305 | -47.135 | 2025-09-13 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 34ebc755-f1a5-3d73-8917-34c63d2607c7 | -12.006 | -47.7505 | 2025-09-13 02:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 6a6d3b53-661b-3026-8a07-13803bd921e5 | -9.2844 | -59.3986 | 2025-09-13 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| a70a2480-cbcf-3cb9-bf8b-75816f7b734f | -9.5006 | -55.9588 | 2025-09-13 02:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 3db7a92b-6fa8-37b2-926a-4d5127a4a225 | -9.5137 | -54.6292 | 2025-09-13 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 7c13458f-f820-33d5-919a-f2d19bc50037 | -9.2503 | -51.2472 | 2025-09-13 02:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| a800f000-17da-30f1-9c6c-9e390d977aaf | -15.1165 | -52.4918 | 2025-09-13 02:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 344ab1cd-e287-3d22-8b6c-6d22cc1bf3f6 | 0.6904 | -50.6481 | 2025-09-13 02:30:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 218b189a-a9ed-31df-b9a8-33d384336453 | -10.7664 | -50.5299 | 2025-09-13 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 0199d6ff-daac-3eaf-8a70-e021b0ef58b9 | -11.8659 | -50.5791 | 2025-09-13 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 1a35875f-e2ee-34e6-accf-738a80fe0873 | -11.9869 | -47.7531 | 2025-09-13 02:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| f9735dd7-fc06-3095-a5d1-5e770d40fc42 | -15.2036 | -56.6803 | 2025-09-13 02:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| d989eea2-5b7b-3517-8559-6bdbfb61b16c | -16.3418 | -51.5434 | 2025-09-13 02:30:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 8f7cb1f5-c2e1-3bcc-a2e3-ea27dcabbe2b | -9.2844 | -59.3986 | 2025-09-13 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 2132861e-5056-3c0a-af12-969c496c1355 | -9.2656 | -59.4191 | 2025-09-13 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 229.9 |
| 5f8bdf22-c112-3aff-8968-9fab79cc801f | -8.1004 | -50.1821 | 2025-09-13 02:30:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 6042fb66-41de-3311-a6d9-65d86097ec79 | -11.8465 | -50.6027 | 2025-09-13 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| e513cb74-cd41-3a80-a193-d2b64e0dd794 | -11.0942 | -51.4711 | 2025-09-13 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 0fccfcff-1af2-3fa3-bc38-9dae165711b2 | -15.2229 | -56.6782 | 2025-09-13 02:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 7fc45f31-2e50-32f4-b79c-021371a3bf85 | -14.2932 | -45.0261 | 2025-09-13 02:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 5f8f1ee0-542e-31be-b4ed-4449684e864d | -21.6187 | -46.8115 | 2025-09-13 02:30:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.1 |
| 03b3cb01-8bff-36bd-b8ca-29c970e70cc6 | -9.2843 | -59.418 | 2025-09-13 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 995d22f8-aba7-3692-bd51-479ad9473d54 | -12.006 | -47.7505 | 2025-09-13 02:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 2d6a97db-9bb0-3aa3-89d7-d6dfc7ed150d | -11.4119 | -45.6012 | 2025-09-13 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| fa79946b-475f-3a27-989e-b21fb49372e8 | -11.1508 | -51.4863 | 2025-09-13 02:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 6b4a35ad-0f51-3a50-a423-c47787c02d73 | -13.0891 | -48.2663 | 2025-09-13 02:30:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| dd77e7e6-cc07-3f40-a5e5-abe0cabece1f | -9.247 | -59.4201 | 2025-09-13 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 397f3402-caf7-3a68-877a-7efe5ed4f592 | -12.9292 | -54.7538 | 2025-09-13 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 83079879-6167-30e3-968f-5890fba20c7c | -9.5135 | -54.6494 | 2025-09-13 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 73435268-28d9-301f-ab6b-c7c1f9f8fef8 | -12.0056 | -47.7728 | 2025-09-13 02:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 2b01e20a-bbf5-33e3-b072-17c6b753195d | -9.2472 | -59.4007 | 2025-09-13 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| a2b1225e-c10a-3df9-a1f0-ab3741614444 | -11.8468 | -50.5813 | 2025-09-13 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 262.8 |
| 9fe6418f-efcd-3aea-a0e7-f4f801a67c29 | -3.2507 | -46.7829 | 2025-09-13 02:30:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 31639d30-b121-36dc-8df4-f5b177e0d8fd | -10.785 | -50.5493 | 2025-09-13 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| bd3b2ae0-f44e-306b-8ea3-fbf56756a087 | -11.431 | -45.5985 | 2025-09-13 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 174.6 |
| ef960de6-7b00-3dc5-b15b-28411eb37513 | -9.5004 | -55.9788 | 2025-09-13 02:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |


[Clique aqui para ver as próximas entradas](README16.md)
