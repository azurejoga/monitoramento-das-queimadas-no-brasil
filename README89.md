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
| 669174b4-1972-3bf1-bb7a-98f6ffb33104 | -12.85196 | -53.51591 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b56db9e-5a80-30db-bf6e-a46ed1ddd80d | -12.84909 | -53.51155 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c897852-fe34-3106-8144-af73ce061e77 | -12.84564 | -53.51101 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8d71e1b-5e45-370a-bca0-3638ebb63ba5 | -12.84508 | -53.51484 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dca4596d-bc2a-32b1-a0fd-38ac7c9bd5b3 | -12.84396 | -53.5225 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 015a9338-967c-3faa-b5b7-9d9c07b773f8 | -12.84339 | -53.52631 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc65898f-fcb4-36f0-ba33-89394f4e4051 | -12.8422 | -53.51047 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9d6e642-e3be-3c4a-8cd5-7c680823fddf | -12.84164 | -53.51431 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a31b212-20d2-3939-af85-e810a70c985a | -12.84108 | -53.51814 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed2fec11-d5e9-390d-99e8-8fa053f6631c | -12.84052 | -53.52196 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f67c6a96-4a78-345b-985d-cad2903b2ab0 | -12.83995 | -53.52578 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a606018-7065-32f9-a4a8-d65b129b2fdd | -12.83932 | -53.50609 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d10a922-9abd-3e6e-9f95-0aa16a63fff7 | -12.83876 | -53.50993 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75c885b4-e3f7-3fae-a74f-4763df7fa1bc | -12.8382 | -53.51377 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61e135b8-5cf0-3b3a-ac07-b6dc02f243f4 | -12.83764 | -53.5176 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52ea530c-364e-3470-9076-1dc06e564bc1 | -12.83707 | -53.52142 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6025b8f7-2ab8-3940-97b7-b6ffa3322d09 | -12.83651 | -53.52524 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b19c8a3c-1302-3fb8-9780-90878d741cdc | -12.83644 | -53.50171 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 213a10ba-801a-35fd-a121-2a2b692b5b65 | -12.83631 | -53.50597 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38cea5dd-d325-3924-bf22-043c2b1d2169 | -12.83588 | -53.50556 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ae17e5c-82a5-3fa1-8af1-d1dedadb5dd8 | -12.83573 | -53.5098 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e5924f2-1034-34cb-8a79-aa5d954d40f6 | -12.83532 | -53.5094 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b85b722-84e2-3cf2-a2d1-01b4ffe63afe | -12.83516 | -53.51364 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2cf74b26-08c8-3572-a58e-fb7ca4b02590 | -12.83475 | -53.51323 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9eed425c-c943-39d5-8947-2504bf1fc64c | -12.83458 | -53.51746 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57861070-25fa-30f5-abde-fcd87d012a85 | -12.83419 | -53.51706 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e0e7feb-2ec4-3ac0-a668-5d8f230e4114 | -12.83401 | -53.52128 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 824df69d-d491-385a-ade4-4c0cec093dd3 | -12.83363 | -53.52088 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c43c7034-82a5-3791-b3f5-efdb89ea0847 | -12.83345 | -53.5016 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70c15ee0-6ab7-362c-93e6-81b5572cb317 | -12.83343 | -53.52509 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2867df4d-b5d0-32f0-8ba2-bb58833e4b85 | -12.83287 | -53.50544 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8c9c1ba-31d9-3ff6-b033-afda4fd86b17 | -12.83286 | -53.5289 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2416e03f-d9e2-3cc3-b8e7-443d827b762c | -12.83251 | -53.52852 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9937e3b2-35d1-3ab9-8351-853a6b036132 | -12.83229 | -53.50927 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a41ad96e-a364-3f52-8cea-fafdd557426a | -12.83172 | -53.5131 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28711fb8-4199-349a-b266-4cc02c7f9ced | -12.83114 | -53.51692 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5e4c1f1-a70a-332b-ab42-e3a8da3a44bc | -12.83058 | -53.49722 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4131b470-c666-3a84-ac9c-4d722319c475 | -12.83057 | -53.52074 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64db6e6a-901f-3e76-bd2c-1c808a3e555f | -12.83 | -53.50106 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c05d2d73-ff77-3b5f-b01b-c0b72626ba7f | -12.82999 | -53.52455 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85bfde58-c322-331e-9feb-c60a8696ed32 | -12.82943 | -53.5049 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30224416-30bf-3eb6-8ae7-a633875bf34e | -12.82942 | -53.52836 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c758c856-ccfd-30de-88c5-adb516f98568 | -12.82885 | -53.50873 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c517824-a6d7-378c-b1b8-2ccbff07a0aa | -12.82828 | -53.51256 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55f6a07c-4342-3126-bb8e-230aca0833a2 | -12.8277 | -53.51638 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e598dbf2-00fa-3968-9e37-1da4b4b30e42 | -12.82713 | -53.5202 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e029f6e6-2afd-3b22-b77a-738dabe2d8d5 | -12.82656 | -53.52402 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da3a1682-0a50-386b-954c-afa47219e31b | -12.82656 | -53.50052 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbd92224-de0e-361b-aa49-9c673aaf2db0 | -12.82599 | -53.50436 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef42dba7-5c7f-32ae-b800-0ca8598842c6 | -12.82541 | -53.50819 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b718847f-1602-3762-9c18-55505bee92f4 | -12.82484 | -53.51202 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12b3e2de-4004-36fc-b0cf-4d211e572eb9 | -13.01724 | -53.46574 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fa38e89-3a2e-3c2d-b2cb-924c70d33c5d | -13.01667 | -53.46963 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8661bf49-7735-3144-954d-b779d451fe44 | -13.01609 | -53.47352 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e9b0666b-25e6-39fd-b2e9-3da05f204429 | -13.01379 | -53.46519 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5acda87e-da52-3cc8-af7e-e8feb3167415 | -13.01322 | -53.46908 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 00f46939-96cd-39c2-ab5c-dd140e24e30b | -13.01264 | -53.47297 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a54b1acd-0ba6-30e1-9f00-69528f617c83 | -12.89727 | -53.49543 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8af54089-a536-3a6b-9f5b-93b37f456820 | -12.8967 | -53.49928 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ca72be3-4ade-39c7-aec1-5d8edb3a3cf4 | -12.89439 | -53.49104 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3989f953-a18c-35a1-9d6b-fb7c2f681299 | -12.89325 | -53.49874 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0556080e-6dcb-3039-963f-4640fd08664b | -12.89095 | -53.4905 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24009047-dede-3d2e-9ccb-63ca9150a683 | -12.89038 | -53.49435 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48cea618-12c9-39f4-b223-49ab1679e35e | -12.88636 | -53.49766 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f288958c-26b4-3be0-8716-66b4d8cf55a7 | -12.87201 | -53.49937 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 408993a4-86ff-3908-97bc-4034571cb177 | -12.83116 | -53.49337 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cca523b5-0398-36f9-850b-40ef4260407d | -12.82829 | -53.48899 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e34fdf37-7f32-3e07-a1b3-a942234e336d | -12.82771 | -53.49284 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e28779c5-a48e-3574-a130-2abb1bcb5032 | -12.82714 | -53.49668 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 059c7f2b-79e9-3fb9-ab95-8a925c9e1312 | -12.82485 | -53.48845 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 693ef0da-95a6-3a83-8d7f-905cefa64d6d | -12.82427 | -53.4923 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9ae497e-7a59-33ff-92e2-d8ecfcbdaf9c | -12.82312 | -53.49998 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| caf7dd40-0484-3d4d-a115-21ca0bd61fa4 | -12.82256 | -53.48021 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b1bd5dd-4b13-3660-bff8-d905a95db164 | -12.81739 | -53.49121 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6754c621-56a8-3c40-b300-8ddea1f72376 | -12.81395 | -53.49066 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d647547-eb90-30da-a8c1-ceb5d87eafd3 | -12.8128 | -53.49835 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c26d9def-db71-348b-abb0-d2935a5e4b2a | -12.67225 | -53.18734 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd61bb80-628f-300e-ae80-6d2f6f6750b3 | -12.6431 | -53.10751 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7af39574-2ba0-3e0f-b09e-cd2900beb433 | -12.63961 | -53.10697 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bfb64caf-871d-3fd7-979b-daeb414e0fb8 | -12.63903 | -53.11093 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e027abe-3744-313e-aa69-a5bacd37913b | -12.63612 | -53.10644 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9c650c7-a7bd-31a1-aa36-228527045a10 | -12.63019 | -53.29015 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63bc18e5-af28-3fb9-ba4c-0d3676d2f24b | -12.62961 | -53.29404 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f89f78b-fa4c-3a5a-8504-034f8ed1c344 | -12.62447 | -53.13702 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 363af225-8d43-31d0-9287-f89465f0014a | -12.62331 | -53.02326 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a1b07e8-f6d0-3241-9f1e-b186987fabb7 | -12.60756 | -53.03301 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0445b05b-9a8f-3734-a4c0-ee26b4c002ab | -12.59128 | -53.0712 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ac727f90-8a55-368f-9dca-2643a38b0248 | -12.58429 | -53.07011 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18bc35dd-35b8-32e6-8cd9-d7b2bafdecbe | -12.57787 | -53.06505 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79580787-55d9-3bf3-b91a-46fb5d974e49 | -12.5773 | -53.06902 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86deed53-c594-3803-831d-8737eacc311a | -12.57499 | -53.08495 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a6fd98b-8f4f-3fe0-8d28-77226da0e7d3 | -12.57438 | -53.0645 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4618079e-bd7b-397c-847b-411a0efa504b | -12.57413 | -53.08187 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66d86b5b-9f7e-3381-863b-51e85405c526 | -12.5715 | -53.08441 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 356e8338-1561-3ec0-a364-6dea065b8f7e | -12.57093 | -53.08837 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4799425d-24ab-32e2-b604-94f16fa084ae | -12.56952 | -53.06487 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fa25d716-17b8-3441-af1e-2b0650b813ca | -12.56945 | -53.08926 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6226dcf9-e789-3170-8e11-abe930669a20 | -12.56715 | -53.0808 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ef8cefe-3d50-3a15-89f8-3195d7b8f712 | -12.56655 | -53.08476 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d0b33dd-4745-3be1-98a7-80be75de15f2 | -12.56425 | -53.07629 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README90.md)
