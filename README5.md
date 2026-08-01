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
| 1db1b9e8-f5f6-31b2-b938-a1577f51a884 | -11.2588 | -54.8721 | 2026-08-01 02:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 166.2 |
| 1b7de8a8-646a-305b-8c61-8cad5fdf4304 | -14.0725 | -46.2899 | 2026-08-01 02:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 88.1 |
| ae51d790-4b42-39b5-8b60-07e7efe428a0 | -11.2402 | -54.8534 | 2026-08-01 02:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 410.0 |
| 24802e83-d1e5-3b37-a058-d929f58d5374 | -11.2404 | -54.833 | 2026-08-01 02:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f907bfce-4503-3b94-9025-29cada2fb3b1 | -14.092 | -46.2866 | 2026-08-01 02:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 22018351-cab1-3b75-a046-8859b67381aa | -14.073 | -46.2669 | 2026-08-01 02:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 68e63fe7-df6f-3eb4-b46c-daa1741c13bf | -14.0925 | -46.2637 | 2026-08-01 02:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 195.3 |
| 1bb05db9-03ed-3f89-a87c-81079986e402 | -11.2399 | -54.8737 | 2026-08-01 02:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 232.3 |
| a886128f-9ab2-3d13-a0ed-ae6134b27d37 | -11.2591 | -54.8517 | 2026-08-01 02:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 302.3 |
| ee6b7614-0799-33c2-b213-837833eb7423 | -14.0735 | -46.2439 | 2026-08-01 02:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 3bc81aa6-b18d-319a-896a-ccfe346cea5b | -11.2402 | -54.8534 | 2026-08-01 02:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 313.4 |
| 896b5af1-e5d4-3ea0-83e4-5662695a2120 | -11.2593 | -54.8313 | 2026-08-01 02:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| dfc0ca09-a1fc-31cf-be39-a03a1ef76a0d | -14.0725 | -46.2899 | 2026-08-01 02:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 6528bfb0-96cc-32ba-9bf0-115e3b388dc5 | -11.2588 | -54.8721 | 2026-08-01 02:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 216.3 |
| 09060c48-77bf-3215-97d0-6cfe9c44a82e | -14.0925 | -46.2637 | 2026-08-01 02:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 47759a9a-b6fe-3b1d-a347-176f1f42e2ca | -11.2404 | -54.833 | 2026-08-01 02:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 1316c80e-fac1-38f6-957d-147f96b5c3c3 | -14.092 | -46.2866 | 2026-08-01 02:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 562e154d-029d-31b2-a3cb-8d7e61ba0e60 | -14.073 | -46.2669 | 2026-08-01 02:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ad94e2aa-d4ab-30e9-b6ef-5b04d2a2b937 | -11.2591 | -54.8517 | 2026-08-01 02:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 343.0 |
| 4aecf960-6486-3e18-9f80-f92825438514 | -11.2399 | -54.8737 | 2026-08-01 02:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 214.5 |
| 31566c7b-bb7e-317a-86ea-e9d260d4f12e | -10.4731 | -48.4901 | 2026-08-01 02:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| ddcf6545-bae4-3e53-a893-720c7fb83cb3 | -14.0925 | -46.2637 | 2026-08-01 02:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 79daa4a9-35be-36f6-92fa-13d2a9ad59b4 | -14.0725 | -46.2899 | 2026-08-01 02:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 2695cce7-13c3-3a36-84f6-5a09adf83ec0 | -14.0735 | -46.2439 | 2026-08-01 02:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 290a1f81-0052-3576-9645-1b6f97cd9ff0 | -11.2402 | -54.8534 | 2026-08-01 02:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 210.0 |
| 898f3e84-93fd-36c5-9396-f6e50f2e693d | -14.073 | -46.2669 | 2026-08-01 02:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 90.4 |
| c9135b48-5e96-31ea-845a-14bebe9d8b17 | -4.2578 | -38.0284 | 2026-08-01 02:40:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 1050e2fa-d52d-3400-b534-499e2c211375 | -11.2588 | -54.8721 | 2026-08-01 02:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 176.8 |
| d4398bf0-b167-32cb-b7c0-dc8c8ea3fbd5 | -11.2591 | -54.8517 | 2026-08-01 02:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 315.3 |
| d3a7afd0-fc80-3cb2-99b4-80088b1fcbab | -11.2399 | -54.8737 | 2026-08-01 02:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 7aae6e26-d067-3685-8fa2-e7e7d4a53e6d | -11.2593 | -54.8313 | 2026-08-01 02:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| cac77e2b-6efc-3b2d-9cc6-dd7093b3ef90 | -20.528 | -51.4475 | 2026-08-01 02:50:00 | GOES-19 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.1 |
| cb1331a3-3b52-387c-a934-68c4ebe73d76 | -14.073 | -46.2669 | 2026-08-01 02:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 2f5fbfef-a22c-326f-a9eb-c58ccc65ace5 | -11.2591 | -54.8517 | 2026-08-01 02:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 303.6 |
| f3d3e1ee-9db8-35df-84fe-5ed48959e26b | -11.2588 | -54.8721 | 2026-08-01 02:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 156.0 |
| 1f367124-9804-39a7-8029-24a5ca7609ce | -11.2399 | -54.8737 | 2026-08-01 02:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 124.1 |
| aca800a2-906a-3a6a-9bcf-69dab6c9b995 | -14.0735 | -46.2439 | 2026-08-01 02:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 9f5bb9cc-eddc-3d3f-8657-9c6c2c7e286a | -14.0725 | -46.2899 | 2026-08-01 02:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 48e0e0f8-3fdb-3a9e-85a6-5eb2d87d66fd | -11.2402 | -54.8534 | 2026-08-01 02:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 211.9 |
| 93866cb3-3968-3caf-8e2a-98ba79cae67f | -20.5286 | -51.4252 | 2026-08-01 02:50:00 | GOES-19 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.4 |
| b9b518a5-396c-3e14-aaba-0a615d0db707 | -4.2578 | -38.0284 | 2026-08-01 02:50:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 113.3 |
| 532212ee-cfa6-3243-9a74-0c4f8076afb6 | -4.2578 | -38.0284 | 2026-08-01 03:00:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 113.2 |
| 141dd6c6-0bbf-3169-b5d1-cea8e6702eb0 | -4.2576 | -38.0541 | 2026-08-01 03:00:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 4ecff40f-d5bd-36f4-ba93-0725e64233dc | -11.2399 | -54.8737 | 2026-08-01 03:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 131.9 |
| daa0e036-9ecf-3c7d-99c0-ef07a8154cc3 | -11.2402 | -54.8534 | 2026-08-01 03:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 212.9 |
| 4c9bd2f8-b44f-3c9a-a5fd-6163032e9381 | -14.073 | -46.2669 | 2026-08-01 03:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 19c96356-c79b-3840-91eb-b44602b45568 | -14.0725 | -46.2899 | 2026-08-01 03:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| ae7910c6-9797-38c4-84da-3546c531dc6c | -11.2588 | -54.8721 | 2026-08-01 03:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 152.6 |
| b26e7fe1-72fa-319f-a27c-022644f3a0ac | -14.0735 | -46.2439 | 2026-08-01 03:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| fd044014-85ef-3786-806f-6e427fb17909 | -11.2591 | -54.8517 | 2026-08-01 03:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 265.9 |
| 058cff1b-b5d3-3911-8ec3-6e8df4dfa8be | -14.073 | -46.2669 | 2026-08-01 03:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 93.8 |
| b35de8f9-0b1e-3930-bcb3-a7af549d6d27 | -4.2767 | -38.0271 | 2026-08-01 03:10:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 16e3f823-95dd-3500-8dec-ed3a206a69c6 | -4.2578 | -38.0284 | 2026-08-01 03:10:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 110.6 |
| de5db655-c781-34fb-a2b7-ba38b07fa24c | -14.0925 | -46.2637 | 2026-08-01 03:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 73fd46e0-f5ca-3cf6-86f5-0cfa26cae1fa | -11.2402 | -54.8534 | 2026-08-01 03:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 149.8 |
| b405f439-9d8c-39cc-98df-fedc42793f9e | -14.0725 | -46.2899 | 2026-08-01 03:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 56.3 |
| a0eb28ab-3a23-33ee-a7c1-5db15e8b9423 | -11.2399 | -54.8737 | 2026-08-01 03:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| f25ea726-29c8-3203-9a54-7905c0bbfe2d | -11.2591 | -54.8517 | 2026-08-01 03:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 216.0 |
| 5b23a52a-a4b7-3559-a56f-55bdadad8ce1 | -11.2588 | -54.8721 | 2026-08-01 03:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 132.5 |
| a5f9d6cf-c4c3-3498-83bc-0db2442c630f | -14.0735 | -46.2439 | 2026-08-01 03:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 1357ebf7-9a2e-35fb-aad0-de77bf118a34 | -4.2554 | -38.03005 | 2026-08-01 03:13:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 8f729ebc-b37d-3246-a270-d6342ae51c7c | -4.25927 | -38.02961 | 2026-08-01 03:13:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 387aa20b-b33f-3994-ae4d-37f6205821ef | -4.25434 | -38.03593 | 2026-08-01 03:13:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 23.0 |
| c6fe21fa-cbf0-3798-a1ab-b1b2296b5dba | -4.26103 | -38.0371 | 2026-08-01 03:13:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 7ac18177-f69d-3856-a93a-430f1a2f3cb1 | -4.26209 | -38.03122 | 2026-08-01 03:13:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 021369e2-5bbe-3e0a-97df-5df08f08b50e | -4.25997 | -38.043 | 2026-08-01 03:13:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 4b9040fa-473f-3dfd-a970-96d2c6f53d6f | -4.25825 | -38.0355 | 2026-08-01 03:13:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 17.7 |
| dbe082fe-b838-3ad9-89ab-1692e8123a50 | -4.26493 | -38.03672 | 2026-08-01 03:13:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 4b718259-2832-3f3d-ba65-3aa0221e83e3 | -4.26595 | -38.03085 | 2026-08-01 03:13:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 24e3f258-1d8e-37c5-b970-9451b883b7a1 | -4.25723 | -38.04139 | 2026-08-01 03:13:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 36.5 |
| 92ce0490-3076-3ba3-b075-f9fedb0e6631 | -11.25 | -54.85 | 2026-08-01 03:15:00 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| abccd86a-1452-358f-b4a5-92f6307e1381 | -7.62648 | -38.80278 | 2026-08-01 03:15:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2d931401-ac6b-32f8-8aed-cd34cfd6d0c4 | -4.52194 | -38.55091 | 2026-08-01 03:15:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a281de05-6eda-37cd-bf7e-59c2b12ee5e7 | -13.17826 | -38.92173 | 2026-08-01 03:17:00 | NPP-375D | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dacf45f8-39cb-370a-bffe-bcadc8fee28d | -13.17925 | -38.917 | 2026-08-01 03:17:00 | NPP-375D | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b9fe5ae8-6c25-37e3-b672-177f41c9007d | -22.2332 | -43.11826 | 2026-08-01 03:19:00 | NPP-375D | AREAL | RIO DE JANEIRO | Brasil | 3300225 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 096cbec1-9715-3aa1-8e88-366740a8e81e | -18.51072 | -42.90183 | 2026-08-01 03:19:00 | NPP-375D | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 96e43791-cd49-32ca-8cb2-c4d3ecd649e7 | -4.2576 | -38.0541 | 2026-08-01 03:20:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 64.9 |
| a5ae6842-454f-3a85-9b55-334bfea4a84a | -4.2578 | -38.0284 | 2026-08-01 03:20:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 108.6 |
| beab4de0-07e1-30d7-a26d-99a83ca3464e | -11.2399 | -54.8737 | 2026-08-01 03:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| f98e9b08-96db-3bbc-93de-1bd02834418e | -11.2591 | -54.8517 | 2026-08-01 03:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 137.5 |
| ce00a7b8-4a38-38c5-940f-adcf94131b9a | -11.2402 | -54.8534 | 2026-08-01 03:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 204.4 |
| 8d7c09e4-ab43-3617-ae83-4917ab34693f | -14.0925 | -46.2637 | 2026-08-01 03:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 53.5 |
| be6f22c5-c826-36dc-8256-11126d2be47c | -11.2588 | -54.8721 | 2026-08-01 03:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 738a14cf-690a-3c40-b329-15ee9619adab | -14.073 | -46.2669 | 2026-08-01 03:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 7a968548-b763-3f5c-9c02-1daa35fe32e3 | -14.0735 | -46.2439 | 2026-08-01 03:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 4974e445-e491-325f-8676-36b935559f87 | -11.2402 | -54.8534 | 2026-08-01 03:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| bdf07783-2389-3116-b798-e2a67c41bcd7 | -4.2578 | -38.0284 | 2026-08-01 03:30:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 101.7 |
| 125341cc-31d3-38ba-8cca-5389564140e5 | -11.2588 | -54.8721 | 2026-08-01 03:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 943dcbea-08f4-3f4d-9065-790cd106ab0b | -14.073 | -46.2669 | 2026-08-01 03:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 41cf4ead-e651-32f5-9485-6fc4888dfb35 | -14.0725 | -46.2899 | 2026-08-01 03:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 59.7 |
| c7486ec4-f864-3a70-baf8-cb47ce5a0502 | -11.2591 | -54.8517 | 2026-08-01 03:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 580ed34e-b542-3375-80b9-7f50740dbc94 | -14.0929 | -46.2407 | 2026-08-01 03:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 8a3d9ff7-c942-3174-8a29-d5620373583a | -14.0925 | -46.2637 | 2026-08-01 03:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 81.7 |
| d2f6dadd-b519-360d-8b3c-bf65ec9b6411 | -11.2399 | -54.8737 | 2026-08-01 03:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| cc7f55f1-821a-350b-8b50-c30ac58e7cbe | -4.2576 | -38.0541 | 2026-08-01 03:30:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 87ac6d03-6967-33cb-a8c5-e3ca856d15c6 | -6.6464 | -43.91324 | 2026-08-01 03:34:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 73f5f654-644a-3e10-b81a-ab700074a337 | -6.65166 | -43.91974 | 2026-08-01 03:34:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1104af79-2bff-3e27-ab81-9c82324d85e3 | -7.24804 | -42.13352 | 2026-08-01 03:34:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| dac3e147-15a8-3bda-bcd6-dff2e94cf431 | -5.75477 | -43.26506 | 2026-08-01 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README6.md)
