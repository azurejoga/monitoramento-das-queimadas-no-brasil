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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| adc94ef1-1795-3974-9407-2b656de719e5 | -10.91173 | -52.43462 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49ed2ec7-1d9a-3f5f-ab5c-3a675fbb2177 | -10.91172 | -52.4363 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b76f0f0b-e426-3703-ad63-382c5a879b18 | -10.90691 | -52.43152 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01ad92a8-eeaa-3875-a172-a58ea1a5e94f | -10.90621 | -52.43362 | 2024-10-04 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a5be5dd6-e038-30a4-b61c-fc2bbdd48737 | -10.24373 | -52.73812 | 2024-10-04 04:10:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8589e36c-6c85-37fd-aa67-7685066649c9 | -10.24295 | -52.74215 | 2024-10-04 04:10:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5246ceac-4538-37bc-8779-49f7c953953e | -10.23806 | -52.73692 | 2024-10-04 04:10:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cef6b10-a9ab-30e4-99c3-721d47e837b4 | -10.23729 | -52.74096 | 2024-10-04 04:10:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f325f6d8-487a-395d-a941-027b1c29dd31 | -10.23651 | -52.74501 | 2024-10-04 04:10:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fbd42574-51bf-3887-b113-38e4cbc92250 | -12.66049 | -54.05574 | 2024-10-04 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3c78a2ed-ceb7-3233-a778-5e80ce0d7c82 | -12.65696 | -54.07364 | 2024-10-04 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9778b409-6dbe-3007-8f9a-8530ba65b64e | -12.6537 | -54.05898 | 2024-10-04 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ecb2ec0-6450-38fc-a8bf-6522fda9df66 | -12.61457 | -53.4965 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16d21117-88f1-3606-b1f4-40ac5aaa4f16 | -12.60885 | -53.49535 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c333d30a-83e7-3750-87f8-dd0680638398 | -12.59795 | -53.12007 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 349d2c30-da86-3d01-a5fd-aa42b5d1514d | -12.5972 | -53.12394 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| ca252530-81a0-39de-90df-31158cdff71a | -12.59645 | -53.12778 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4223157b-317c-3a79-86fb-13ad9b333443 | -12.5957 | -53.13161 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1f3ed38d-b498-3579-944a-70c6a07ce9a1 | -12.59237 | -53.11898 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 89111689-838c-3e03-8501-fa7811e0c528 | -12.5916 | -53.12287 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 67b15b95-44c4-3cc0-93d0-ca2882c7dfd5 | -12.59085 | -53.12672 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8c86e564-068c-3aa6-8b81-d056d050aa1b | -12.5901 | -53.13053 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 14ab4d3a-9dec-3346-8bfa-a3ccaf9ddebc | -12.58937 | -53.13428 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a74f50f5-8df7-3b58-8db7-f3416403b46f | -12.58678 | -53.11787 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fd62fdb9-570e-3ef9-b830-0b2f1baa6b0a | -12.58601 | -53.12178 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 859fdf48-92cc-335d-ac6c-cbed378d4b62 | -12.58526 | -53.12563 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fb820550-4b55-36cc-ae94-f6f9f59898f6 | -12.58119 | -53.11675 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 78365664-8602-3a3c-bcd7-538dfaa38e1a | -12.58043 | -53.12066 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7170e71e-5524-3793-94d4-f42f99a53d08 | -12.57967 | -53.12451 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 444edc89-5450-3cc4-a01f-0cb297905c63 | -12.57892 | -53.12834 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58217516-d5bb-3671-8581-77de7f86ed20 | -12.57561 | -53.11564 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2a6487a6-908b-3308-93f4-e43620cda8c2 | -12.57484 | -53.11954 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| cd17cc0d-3a10-3ebe-a629-47ae473b52e5 | -12.57408 | -53.12341 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ff3c27c9-28a5-34d5-90d4-5e8f1fedd240 | -12.57332 | -53.12725 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1c674b25-632e-390d-9ddd-5eefa2d3ef05 | -12.57184 | -53.13477 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 677875fd-5a9f-3218-a453-6366622ea304 | -12.55354 | -53.13915 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ea704d9b-addb-3d76-a812-e03a94ed9b82 | -12.54794 | -53.13802 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e73035f-69bd-3078-9e88-6693d9d2cfe1 | -12.5146 | -53.14154 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35bdaa98-1adc-3946-89f9-23fabae9940c | -12.51286 | -53.13882 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4adcece9-8897-365e-b6cb-3b8082e1c68e | -12.51209 | -53.14264 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c10313b3-e729-3ef7-9d2e-f98ee356bca0 | -12.50972 | -53.1367 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| edf39482-ca38-3bec-a23c-490cc433c0ec | -12.50898 | -53.14053 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7f131ad-29d4-3ae5-b613-1c2445d69ced | -12.50336 | -53.13952 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec3da48f-a4bb-3b99-a025-189c6e6e8de4 | -12.50085 | -53.1406 | 2024-10-04 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 760bb598-87ed-3e4e-86b1-023deeaa0774 | -12.31921 | -54.09348 | 2024-10-04 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f2cdfb40-bc7a-343c-b2d4-4446fed17720 | -12.31678 | -54.09242 | 2024-10-04 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 42ab1026-29cc-3e3a-b4bf-5134d76ace00 | -11.58506 | -54.48447 | 2024-10-04 04:10:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6b7c46b3-13ed-3e22-8be7-e7adb7c68e04 | -11.58415 | -54.48193 | 2024-10-04 04:10:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3a94f0d6-3ce2-3aeb-83d4-7141f369eff6 | -11.58314 | -54.48689 | 2024-10-04 04:10:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 05ac0302-528d-3f7c-8650-dcfb7d6e9815 | -16.14483 | -55.91866 | 2024-10-04 04:10:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cf6eff88-2dbd-3bed-88e6-483bb492351b | -16.14016 | -55.91904 | 2024-10-04 04:10:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 4281895d-c555-3a3a-89a3-43115fd300f4 | -16.1385 | -55.91787 | 2024-10-04 04:10:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 312b25e0-9f89-3e19-a821-8df7c158b3c1 | -15.88433 | -57.15039 | 2024-10-04 04:10:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f325b04-6d87-3ebb-82ef-0107861ff7cc | -15.88123 | -57.14679 | 2024-10-04 04:10:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 847b998e-89cc-36ee-88b3-62767efdd71a | -15.88021 | -57.15126 | 2024-10-04 04:10:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae515346-f2ff-3227-a5d4-dc75bbfe6ec4 | -15.87898 | -57.14292 | 2024-10-04 04:10:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d958fcf4-69b1-36de-b06a-299c2f43e997 | -15.87795 | -57.14757 | 2024-10-04 04:10:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08438c1d-f334-32bb-bfcc-3326b9325223 | -15.8759 | -57.13938 | 2024-10-04 04:10:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aceedea2-7e48-350b-82c7-492531174621 | -15.79258 | -57.33999 | 2024-10-04 04:10:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d5a998a-47be-3c21-b1d8-b5a775a2e18e | -15.79158 | -57.34443 | 2024-10-04 04:10:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de6aa46f-5199-3b7d-b7c6-8ba6d90e5b64 | -18.42199 | -45.07938 | 2024-10-04 04:12:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d7f3cfef-cbcd-3ebf-bafe-55c93fadc72e | -20.76764 | -46.29468 | 2024-10-04 04:12:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 959c057f-1993-36c2-ae52-b089d18bdf6b | -20.76701 | -46.29847 | 2024-10-04 04:12:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16adffd3-3e43-30c9-bc9d-6dba89c5a234 | -20.76491 | -46.2903 | 2024-10-04 04:12:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5f76bbe-2028-32b9-ac7a-632a1c9eff5b | -20.76155 | -46.2897 | 2024-10-04 04:12:00 | NOAA-21 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d60a47f9-72c7-3b02-9752-c47591887551 | -20.51253 | -46.299 | 2024-10-04 04:12:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ccd2113-87fd-31b7-938d-949e7fabb5eb | -20.50887 | -46.38421 | 2024-10-04 04:12:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d345f12-0555-3328-87b4-ffd017039114 | -20.50823 | -46.38809 | 2024-10-04 04:12:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e8340de-76a2-38f5-bcd9-2b9e6dd92ef7 | -20.50631 | -46.39975 | 2024-10-04 04:12:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d585d53-5824-3c8b-a43e-bcac3889eb88 | -20.50614 | -46.37971 | 2024-10-04 04:12:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c045171a-4bc2-392d-878e-b41410af9e6a | -20.50551 | -46.38355 | 2024-10-04 04:12:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 679237d4-9dac-3c78-931b-4ba22d4f3451 | -20.50295 | -46.39906 | 2024-10-04 04:12:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14950aa9-75f6-3d84-9438-9227189c6c33 | -20.50214 | -46.38293 | 2024-10-04 04:12:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f95f1e5-ce54-3c17-81ca-67f1c4f7631d | -20.37725 | -45.60281 | 2024-10-04 04:12:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39fc0738-c8e5-3b56-b5b7-391b4544ad6f | -20.35723 | -45.51545 | 2024-10-04 04:12:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35d723e7-1fca-3475-8a11-e318ec896464 | -20.31225 | -45.58404 | 2024-10-04 04:12:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 912feb09-fc69-3c66-a399-b34daed6fe2c | -20.36284 | -45.31152 | 2024-10-04 04:12:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 792c4850-8e3c-3a31-8b94-1f377576a12b | -20.24066 | -45.49875 | 2024-10-04 04:12:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8e7a1fba-5537-3d92-a30d-1a612bb97220 | -19.89949 | -45.98586 | 2024-10-04 04:12:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d86df74-f440-3c9e-8620-74f93897518d | -21.76448 | -45.55047 | 2024-10-04 04:12:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 32f066d8-261a-31a0-86ae-3b1af30d069c | -21.76118 | -45.54988 | 2024-10-04 04:12:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 66ff7473-3f7c-3469-ac8a-64f384a1c0e9 | -21.52084 | -45.7743 | 2024-10-04 04:12:00 | NOAA-21 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8838e9ee-4c6b-37ca-8b67-1e89e3a26685 | -21.50487 | -45.76753 | 2024-10-04 04:12:00 | NOAA-21 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5ebb4c0b-444b-388e-a656-7dc27044c646 | -21.44662 | -46.56424 | 2024-10-04 04:12:00 | NOAA-21 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 87b8f67e-f07e-3b18-9c56-423bca0d9a6e | -21.44597 | -46.56813 | 2024-10-04 04:12:00 | NOAA-21 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 84dd9f76-f1b3-3604-9f22-ee6b286ead9b | -21.44262 | -46.56744 | 2024-10-04 04:12:00 | NOAA-21 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c7f8b09b-f014-3678-90a4-3de9feb03c18 | -21.27842 | -45.63134 | 2024-10-04 04:12:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8582766e-0120-3a70-a848-cae8c7294c21 | -21.20441 | -46.56308 | 2024-10-04 04:12:00 | NOAA-21 | JURUAIA | MINAS GERAIS | Brasil | 3136900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a626433a-61b4-3684-adb9-1fca5b6b3cee | -20.9606 | -46.09984 | 2024-10-04 04:12:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 48f2981b-4f25-3e98-a85b-fd712e0393be | -22.73407 | -47.03589 | 2024-10-04 04:12:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 1ea8c1f5-11d1-3cf2-8c4a-ef6805cdd56b | -18.79869 | -46.63992 | 2024-10-04 04:12:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2451a7a8-60d9-394a-a521-1f8b8b75fa27 | -18.79459 | -46.64325 | 2024-10-04 04:12:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16e3e97d-bd8c-3a0b-9272-c934c2089bc8 | -18.79391 | -46.64724 | 2024-10-04 04:12:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99939464-7fdc-3769-8719-3854dc367e1a | -18.79115 | -46.64258 | 2024-10-04 04:12:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 852c3ad6-2dd2-39d5-9b23-63f6dbab2e1e | -18.79049 | -46.64655 | 2024-10-04 04:12:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c195126b-53e9-3a9b-bbec-1b67de11389f | -18.57453 | -46.44495 | 2024-10-04 04:12:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15342af5-b9a2-339c-940c-f33be645d91e | -18.57388 | -46.44883 | 2024-10-04 04:12:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33a19019-6201-35a4-b075-a95ea27d7fbf | -20.19341 | -47.46373 | 2024-10-04 04:12:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 54151a7c-7c15-3057-9205-24193bc5fc94 | -20.19268 | -47.46803 | 2024-10-04 04:12:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8b92e3d2-6603-334e-bb30-511033c82182 | -20.18994 | -47.46297 | 2024-10-04 04:12:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README80.md)
