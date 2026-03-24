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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d407a794-a1ef-3d42-a251-000ade9aa129 | 2.65165 | -61.29391 | 2026-03-24 05:27:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56144ed6-79bf-33b9-b217-428252426f21 | 3.36374 | -60.14023 | 2026-03-24 05:27:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 068ac96b-7712-3b61-bfc4-3e494c565089 | 0.98116 | -59.38158 | 2026-03-24 05:27:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 365fa19f-55ed-3583-b62c-5f8eca7b0429 | 2.03485 | -61.10524 | 2026-03-24 05:27:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5c4d1c42-8193-387a-9d41-eeb249ef56f7 | 1.88671 | -60.67086 | 2026-03-24 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5086a33e-8c8f-3553-959b-0c40fb80d46b | 2.64513 | -61.29897 | 2026-03-24 05:27:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5be3cb2f-1e5a-39c8-bf93-34bb0a208663 | 1.98803 | -60.60622 | 2026-03-24 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1272a50-a750-3c47-a72d-59ac1b34a01b | 0.9424 | -60.46491 | 2026-03-24 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c1adb58-3d88-3259-bf02-bb9cc510c9a3 | -2.32033 | -57.83722 | 2026-03-24 05:27:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36551f51-2be9-3095-b36e-702929cbb677 | 0.51567 | -60.26574 | 2026-03-24 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b479323-38ea-3246-ab48-44b32c45a3b1 | 0.14779 | -60.41013 | 2026-03-24 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b2295b9-4bee-3eb5-9e95-a23fe04285d6 | 1.08291 | -60.64854 | 2026-03-24 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5361bbd2-bd18-33bd-996c-03ce350a0f0b | 1.84458 | -60.42731 | 2026-03-24 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03fd0b43-9db7-32e2-adbd-1c0648f148b5 | 3.36317 | -60.13654 | 2026-03-24 05:27:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2eca65b-35de-3a82-a07e-d54db9c61041 | 0.51961 | -60.2688 | 2026-03-24 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3113880d-2e9b-3367-9e0a-cfa903d8a73b | 0.68165 | -60.33866 | 2026-03-24 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4c99ab39-b70f-37ee-a093-150e2993d02b | 3.35291 | -60.13813 | 2026-03-24 05:27:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec3f6985-e606-3c0b-b310-31480054d030 | 3.35006 | -60.14234 | 2026-03-24 05:27:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86b41923-35c7-3760-8c40-ab718483f580 | 4.16942 | -60.4735 | 2026-03-24 05:27:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd40e01e-46ea-3ea0-83fc-89083a2b67af | 0.63354 | -60.05468 | 2026-03-24 05:27:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1e715d2-f36a-3746-ba82-e172cb77b403 | 1.84683 | -60.41946 | 2026-03-24 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd7d0f5d-20fa-391b-8e15-b1643435c694 | 0.98061 | -59.37813 | 2026-03-24 05:27:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6a7a26f-3f13-36de-b7c7-e25dc3540865 | 1.84058 | -60.42417 | 2026-03-24 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 346ddf99-58ff-3a88-924f-ae6c551bb0de | 1.13367 | -60.08576 | 2026-03-24 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22616077-5ebe-3beb-b7b1-e95be41d11ce | 0.94198 | -60.17768 | 2026-03-24 05:27:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02aeaa47-dd95-35b3-9328-9c8b74804f53 | 2.78881 | -60.30288 | 2026-03-24 05:27:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 433c92d3-4136-3737-ac88-d8a8c62603ac | 0.77347 | -60.5462 | 2026-03-24 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93a01849-e829-36fb-aacc-19b80b9fc56b | 0.77547 | -59.87772 | 2026-03-24 05:27:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0e79595-bc68-369f-871c-badb95d9a5e5 | 0.73284 | -59.60904 | 2026-03-24 05:27:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4be904c1-3427-3b34-8366-51bcf0eec4c7 | 0.94523 | -60.46077 | 2026-03-24 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c31d5021-084d-34e5-ba43-46d992065cb8 | -10.6708 | -54.29466 | 2026-03-24 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb671599-6e5d-3b63-a3b4-af878025b9ac | -10.67014 | -54.29952 | 2026-03-24 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e919ec4-012d-3417-97ee-77d6f31f479e | 0.6345 | -60.05653 | 2026-03-24 05:48:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed3a591a-6efd-3c42-bc08-544aaeb8578e | 0.98218 | -59.38103 | 2026-03-24 05:48:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce52a476-6c85-34f6-9d07-8644dd2be170 | 0.68323 | -60.33759 | 2026-03-24 05:48:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5795ac17-4b33-3057-b751-9f3b1f6da161 | 2.79091 | -60.30505 | 2026-03-24 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f6e9002-b594-37e4-8f40-31dde7641180 | 0.98646 | -59.38035 | 2026-03-24 05:48:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc13007a-ff06-307b-875d-3770b13e739f | 2.03345 | -61.1043 | 2026-03-24 05:48:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5568a36c-9657-3194-93d7-bc4667690915 | 3.36217 | -60.13408 | 2026-03-24 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 964ad84b-c643-3bf7-8e61-e7b559974e02 | 2.6517 | -61.30307 | 2026-03-24 05:48:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9183c354-5574-3ce5-b94f-c0768c1005ad | 0.98282 | -59.38506 | 2026-03-24 05:48:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36caf290-83ff-3823-9766-c1ddf9a53908 | 0.77654 | -60.65025 | 2026-03-24 05:48:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8968b16-9a1e-3aea-bbc3-3d12935eef38 | 0.64221 | -59.99838 | 2026-03-24 05:48:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9945f0b-b903-3f0a-a472-b87eabc94765 | 1.84473 | -60.42051 | 2026-03-24 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7e036fcc-ebbf-3d59-8e28-a4c439d24fe1 | 2.79046 | -60.30311 | 2026-03-24 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f024aa7-775f-3c19-9bb2-0fd35323d729 | 0.94404 | -60.46054 | 2026-03-24 05:48:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0bc232f-d1c7-3afe-80e4-befd4bf82d6a | 0.57698 | -59.90898 | 2026-03-24 05:48:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcc6cd4f-35eb-3cec-a045-8c1248149c7a | 0.98582 | -59.37628 | 2026-03-24 05:48:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf90d47e-6c1f-3059-836b-9178f7d73f5c | 3.3512 | -60.141 | 2026-03-24 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 060a73cf-5cea-3731-b252-7781c34f9e5e | 3.36298 | -60.13908 | 2026-03-24 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6d0a51e2-76a6-3668-9338-4acd3a9ae719 | 3.84573 | -60.0672 | 2026-03-24 05:48:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f55a155-8423-3bf5-941d-4fae04304a92 | 1.98722 | -60.60485 | 2026-03-24 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8686fb0-e388-3879-802f-62b78bbf1001 | 0.14421 | -60.40675 | 2026-03-24 05:48:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8b9284e-4b18-3e5b-99d9-983d4ae76446 | 1.13476 | -60.08391 | 2026-03-24 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21d714be-36ef-37f0-9880-4b809cd80b37 | 3.45048 | -60.15867 | 2026-03-24 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02fd0f56-0ab6-347b-bd97-c6ad6ea9019a | 0.94459 | -60.46398 | 2026-03-24 05:48:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dec4487f-d9c7-30d2-b8e1-e3458b47e7f3 | 2.03722 | -61.10371 | 2026-03-24 05:48:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1394e9ac-ac52-3efe-93e2-f9e17e0fdd77 | 1.84161 | -60.42619 | 2026-03-24 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c30e1173-85d4-339f-9391-47ef71375fd5 | 0.7754 | -59.87461 | 2026-03-24 05:48:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0496f7e7-4776-3803-a511-a5b349a23b17 | 1.08223 | -60.64947 | 2026-03-24 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67ef0fac-8859-3fb2-bc45-873b11b66fcb | 0.6298 | -60.0535 | 2026-03-24 05:48:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db37289c-1285-31e3-8cab-6d40a2539c1f | 2.64955 | -61.28985 | 2026-03-24 05:48:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ea25342-1a92-3b0c-81a0-5c3cc741fa6a | 2.03774 | -61.10587 | 2026-03-24 05:48:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1fa31fcf-44b8-3a47-8872-7a684b155bd0 | 4.24269 | -59.91077 | 2026-03-24 05:48:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91b2d448-745f-395b-b21e-1cde88d46191 | 2.78621 | -60.30071 | 2026-03-24 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c061753-8cb3-396f-a709-f591a28c6f1f | 0.77895 | -59.87023 | 2026-03-24 05:48:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfebdbda-24d9-396d-ad75-fa078c3a92c1 | 0.63391 | -60.05286 | 2026-03-24 05:48:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b5d3100-4b90-376f-9f59-ec48dc70e74d | 0.9871 | -59.38439 | 2026-03-24 05:48:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7b684d5-87fb-3019-9d37-b3ae8a9448d4 | 0.58114 | -59.90831 | 2026-03-24 05:48:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28c32f7e-a7a2-3b4b-82ef-2b0b825a2c96 | 1.88976 | -60.67241 | 2026-03-24 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a5863e2-cc2b-3ec1-babe-e0736131f10e | 1.84556 | -60.42556 | 2026-03-24 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82d9916c-8d83-3eb7-8f62-fb3db28835a2 | 0.68491 | -59.98431 | 2026-03-24 05:48:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f86ef80-699d-3ac2-b6e8-8fdda0b2629c | 2.03417 | -61.10888 | 2026-03-24 05:48:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4f924c6c-ba33-34ea-b8b3-25c1f944c688 | 2.64728 | -61.29926 | 2026-03-24 05:48:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6167823-d977-3788-aa22-a946cec3c033 | 0.5182 | -60.26831 | 2026-03-24 05:48:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1666fdf8-1eaf-3a21-be1d-095a2be71cbe | 3.35432 | -60.13536 | 2026-03-24 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4700459-a236-3f0c-a2bb-06b07fd0596b | 1.08616 | -60.64886 | 2026-03-24 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee271ba3-1232-3099-b44c-1d40237b980d | 1.84079 | -60.42115 | 2026-03-24 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1dffb890-b341-3b57-84b9-1e8b478d587d | 1.88588 | -60.67303 | 2026-03-24 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e78d82cc-f947-3c2b-9e25-762112ea55d0 | 0.69633 | -60.08078 | 2026-03-24 05:48:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8a8c09f-b0ff-388b-bfc5-797846df61a6 | 0.14477 | -60.41032 | 2026-03-24 05:48:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ef55138-652a-364b-9fba-fa23550d35f6 | 2.64358 | -61.29985 | 2026-03-24 05:48:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83a344bd-cf4a-336f-8db8-b7792264192c | 0.94533 | -60.17592 | 2026-03-24 05:48:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 288c61ec-2741-31f8-abd3-65bb6ae46c60 | 0.96797 | -60.16124 | 2026-03-24 05:48:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25e8008a-afd2-38df-b727-c0dcc6033880 | 2.78654 | -60.30373 | 2026-03-24 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33d4e818-9e52-306c-b069-2edc0825bb2e | 2.03794 | -61.10828 | 2026-03-24 05:48:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0ce15663-c903-37df-8a7c-91fa28890fd1 | 1.5212 | -60.0238 | 2026-03-24 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53457353-63df-3af4-8c4f-3fc651eeecfb | 1.83996 | -60.41609 | 2026-03-24 05:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f08f9e1e-c320-3d68-84ea-a6ccb3fddcb7 | 0.93942 | -60.32605 | 2026-03-24 05:48:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04a75496-e964-3335-a975-7bbf36fd055a | 0.94059 | -60.32545 | 2026-03-24 05:48:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e488858-e03b-3c8d-89bb-fab533f69d22 | 0.77834 | -59.86647 | 2026-03-24 05:48:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfaa61c4-018f-3953-94b5-38a4d206bfad | 4.80479 | -60.62872 | 2026-03-24 05:48:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 048faaf6-6ea2-3ad3-aef3-bfa501e20d8f | 0.77479 | -59.87086 | 2026-03-24 05:48:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 416fbdb2-a6bf-35ce-9d89-bd7db3a1cefc | 3.44574 | -60.15432 | 2026-03-24 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70f5b389-a3fd-3464-b4a9-7a3e091ceebb | 2.79013 | -60.30009 | 2026-03-24 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 874250b7-41cf-3187-b379-fd4c6ca722b0 | 0.98154 | -59.37697 | 2026-03-24 05:48:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed07537e-f128-31ac-803e-47320d3b398e | 3.98554 | -60.0363 | 2026-03-24 05:48:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e513b0a-1dcb-32c7-9fce-e581a9669a8c | 3.24153 | -61.24057 | 2026-03-24 05:48:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29afba04-b0b1-310b-a906-049e5dd01001 | 0.51762 | -60.26474 | 2026-03-24 05:48:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a34dcfe-b1b9-34fe-ab22-710a6b81c6bc | 3.35513 | -60.14035 | 2026-03-24 05:48:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README6.md)
