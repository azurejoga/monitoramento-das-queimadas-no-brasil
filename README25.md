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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a01f5efb-5ef1-39ce-97a2-e84efbb3f182 | -2.28155 | -47.91777 | 2024-11-16 04:23:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 72b563db-6e57-3295-aeee-95dc3eb64150 | -4.99498 | -44.32265 | 2024-11-16 04:23:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a63f3033-a13a-3693-8ea9-dd6353ed55bc | -2.58467 | -48.94049 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 32f3cedd-7f45-38c2-b0b0-fc1237c6de73 | -2.14644 | -46.55586 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56673f7c-1e17-3f70-bcbf-f056dcd7382b | -2.3484 | -47.46984 | 2024-11-16 04:23:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f7321490-49a3-3f68-b85e-5b348d2c1877 | -2.17878 | -47.95158 | 2024-11-16 04:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4378da84-ede8-3344-a64c-e7a356caa39d | -2.64518 | -48.47457 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cc694091-4ddf-3893-bcfe-ccb5ec205b21 | -2.66575 | -46.18377 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9b525fd1-fe42-3913-9c42-8437403c7d25 | -3.25086 | -46.52737 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07b77646-da4c-39ae-a7ed-2745674b840e | -4.00394 | -44.34019 | 2024-11-16 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b25101a-6805-33eb-9548-e3209a7d5035 | -3.58144 | -50.52868 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 709d8420-9b6c-31eb-992d-9fbe693453d9 | -3.39519 | -51.57531 | 2024-11-16 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1eadece-c98b-3d99-8f8c-7d80a59af83d | -1.99705 | -46.57637 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a44eb894-ca34-3e32-a0ac-ca315d6727a8 | -2.07538 | -46.47485 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3053a680-00bf-30c5-b208-a203b32b3619 | -4.13444 | -47.23803 | 2024-11-16 04:23:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44eb4112-f732-3476-8089-55f816346d81 | -3.99859 | -46.39989 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 762f1d05-bb17-3671-b1ef-08210c0fb93c | -3.68499 | -40.77917 | 2024-11-16 04:23:00 | NPP-375D | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c79cff9a-09d3-3b0e-a48e-822ef8599611 | -3.89447 | -46.47977 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9966f70c-2d34-3caf-a9ed-1ad54a710f00 | -3.46367 | -51.62293 | 2024-11-16 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 068eefc5-96a9-3156-9f02-d4c670561f06 | -2.65179 | -46.16364 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d94abd1-0a69-3d6a-9574-8f038ab2b310 | -4.23077 | -46.56192 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 202d8326-7e81-3a4d-9830-3e0bc0403f7c | -2.66854 | -46.18779 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1918e12-4bda-3517-8262-0b40b7d814c2 | -3.76899 | -50.78325 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19b73afe-8efd-3abb-9fd0-29d9deb9667e | -5.00627 | -44.31699 | 2024-11-16 04:23:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08a05821-bfb3-394e-bc98-8e4bf7b4cd35 | -3.32777 | -43.8213 | 2024-11-16 04:23:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30154ae5-282f-3866-b6fd-e0f888e6eac5 | -2.59853 | -48.32434 | 2024-11-16 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3ed540f-0d05-3749-914c-d199c741b614 | -5.43338 | -42.88588 | 2024-11-16 04:23:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 497e4c33-2f00-3b43-afdb-e79aab07be3c | -2.8252 | -46.66481 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e07232e-3592-3a3a-bbcb-b89614c7d366 | -2.7917 | -48.56166 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f66f7f5-e529-3dd5-9247-c6801b095f65 | -3.10691 | -45.98095 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cbac14e-2b1f-30f3-8374-23236bd9727f | -2.45184 | -48.02503 | 2024-11-16 04:23:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c951a273-aa3d-3f6f-8b4b-9ef40f0b7637 | -4.72795 | -48.11511 | 2024-11-16 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2defc128-10cd-3eab-a80c-088c257f3e9f | -3.22933 | -45.39832 | 2024-11-16 04:23:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d58e5703-e197-3196-b85f-8ebeabe126e2 | -2.7919 | -46.64877 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ca649ed-8dfd-34fb-a600-f90e8aab6047 | -2.66464 | -46.19077 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3c97a24-a188-383c-8260-698a5187c205 | -1.08804 | -53.17645 | 2024-11-16 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b31bc9f0-c57f-3820-9b4b-e30b6359eecf | -2.7874 | -48.56525 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 573b305c-6675-3861-8703-42c021d0b0be | -2.60938 | -46.81193 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa53bb68-d472-3cdc-98bd-2ec4e0fde883 | -3.09966 | -45.96204 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95559f69-c1f4-31f7-b418-df198602e3c4 | -4.81344 | -42.91597 | 2024-11-16 04:23:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ec567579-269f-30fb-bc2c-33cb7b1abd81 | -4.09376 | -49.97844 | 2024-11-16 04:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c4fd24c-0dcb-359e-ad9d-1acb311554ca | -2.65124 | -46.16714 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9341922-2dec-3c17-b7df-723ffe987a6f | -4.6623 | -44.08216 | 2024-11-16 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c516fc07-dc11-3f1e-afa8-07c052fbd5a3 | -4.15438 | -45.4342 | 2024-11-16 04:23:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d6b74b0-00cd-3eea-85e9-bf4e5854010d | -3.69221 | -50.1077 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 61998277-6616-32e9-b6b9-d1659848b11f | -4.30035 | -45.99123 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efe2921f-d2e4-3eca-8501-026735d3b4d3 | -2.15998 | -46.42638 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d9cedf3-4fad-3df8-aca1-2c7a1ccb939b | -4.64932 | -45.12766 | 2024-11-16 04:23:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd533e28-eebc-36c8-b9e2-4ce316dd1f0a | -3.959 | -50.01912 | 2024-11-16 04:23:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 025dc091-dec5-3892-9a2e-36f3da713d74 | -3.72991 | -45.65738 | 2024-11-16 04:23:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dc201307-218f-3aad-96f0-e232f6d92fcb | -2.67378 | -46.8444 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70d4ba6e-9358-3a1d-a350-368fd0009680 | -4.22993 | -50.67755 | 2024-11-16 04:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd55f910-b525-3c19-8ae6-23129a0a160e | -3.99526 | -46.39935 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 043b1e2b-b7d2-3d1a-95e0-bc014cbb53b5 | -2.6348 | -46.82698 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45be7184-92e8-3970-ba10-2ef67871295e | -2.64382 | -48.48294 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 12c515cf-29c3-3fb8-9606-43c91eabece4 | -2.65072 | -46.19217 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21849e90-34f4-3baf-917d-20bef654bc96 | -2.89644 | -45.34317 | 2024-11-16 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6575e897-675a-3d1e-807d-902206b5db6f | -2.78569 | -45.95957 | 2024-11-16 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05e302cb-d57f-357a-9b6a-65f65841aef6 | -2.47794 | -46.36303 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bba78e6-b02b-3993-90d6-2ac0a1c7a56a | -1.08691 | -54.21271 | 2024-11-16 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26d3606e-33af-3e48-bf15-1d1c44eea12b | -5.00176 | -44.32369 | 2024-11-16 04:23:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0262e0bb-ef9e-3c88-a995-5fb1ff565922 | -3.58028 | -50.53592 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 35460dcf-94c0-3c2f-8449-59ba4ae06202 | -3.6122 | -44.79169 | 2024-11-16 04:23:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72a15bf1-0b36-328c-ba71-67e3ea8776ac | -5.67808 | -35.64283 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 61079634-d9be-3c0e-96f6-980c4d4f9046 | -3.95066 | -46.70218 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa178309-0030-3dac-afed-5034f32b7b5e | -0.65351 | -49.39437 | 2024-11-16 04:23:00 | NPP-375D | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bce4991-0c84-371c-84a4-c5bdb600d102 | -2.63122 | -46.18552 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c9b01c7-7e7a-3022-a73d-2199038de60e | -3.2707 | -45.50072 | 2024-11-16 04:23:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 2b5fd881-998a-39f2-b6ad-271dd765a038 | -2.82354 | -46.65357 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cb59ef2-68b0-3663-aec5-f3a9593b3374 | -2.25453 | -48.75192 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25206f95-1fd0-3d81-812b-916f74e007cc | -2.19695 | -46.34494 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34e6ded6-be1c-3f6f-ad92-b4cae71b55fb | -1.81386 | -46.95816 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 088230d5-e43d-30a0-b210-06297fff0efc | -3.98997 | -45.8535 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3c79796-448e-38bc-a3a4-7c3918defe66 | -3.91568 | -46.51912 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63525e6c-e4f4-307f-a110-5a6488dd32f6 | -3.85208 | -46.63903 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58a387e9-0337-369c-8eec-6ff931d31dba | -3.89586 | -43.29982 | 2024-11-16 04:23:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93519f40-53cd-368b-8595-8c0afb54e192 | -3.0849 | -47.76537 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c8db1df-fa8a-3f24-92d2-c7d98f0b7424 | -2.64651 | -46.55694 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05c14350-0c9f-3843-a06b-da76a721aa85 | -3.56332 | -51.64679 | 2024-11-16 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26a83979-bf39-3a55-8be0-56c26d6deee6 | -2.6827 | -46.83405 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 990decf1-ef68-3d30-a373-797a8fb3e696 | -5.24601 | -44.18904 | 2024-11-16 04:23:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0df32d54-868c-3f42-a899-ae36386db4cc | -4.73724 | -44.09364 | 2024-11-16 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b108a50c-aecf-3df2-81f6-97de37e95cf2 | -1.68041 | -48.46502 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3593e86a-fe99-34cb-bb76-8cbe45016cff | -2.39337 | -47.93902 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56d477ae-b5dc-3c95-98ed-f6f7b1f634d9 | -3.24413 | -46.43947 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c6c39c9-3faf-3631-887a-3c8d4e59a36e | -2.16091 | -48.90865 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f505356-f05e-367d-a8f5-b073ef3029ca | -4.37849 | -45.6248 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 884c8725-4c81-3b98-b802-a146df49f7a1 | -2.36009 | -49.11118 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e491a0b-fa85-3165-b8a0-c3b6c61b0a8d | -5.00288 | -44.31647 | 2024-11-16 04:23:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e53f5f81-a016-3ad5-a7fa-1a6d24fc0cc0 | -1.69149 | -47.97382 | 2024-11-16 04:23:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c7797bb-b893-347e-89c8-f8b991e4722d | -2.66072 | -46.17221 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 103b963e-ee9d-3908-90ea-a1ff27bcfa93 | -4.8154 | -42.91475 | 2024-11-16 04:23:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b17ad58f-e9f4-3589-b9df-15e9c85104e0 | -2.81903 | -46.66018 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 80db7a2a-82ae-3daf-af14-f41acd4f290e | -3.94619 | -46.70869 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5278d6b2-fbd1-3053-a558-6516e7d0cc8f | -2.09907 | -46.59249 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86fb9907-d089-30f4-b4e5-84223d274c31 | -3.91537 | -45.85606 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c235fb69-7dff-38c8-a2b8-06b77e29d407 | -3.53864 | -51.49098 | 2024-11-16 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44354665-947b-3516-943b-8bb9360fd9b3 | -2.35559 | -49.11509 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0667a217-a6f2-3ddf-aadb-a1602d62d84b | -2.11285 | -46.41897 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cb7f458-65e9-3d74-8d41-944a79d81c09 | -4.90764 | -43.35342 | 2024-11-16 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README26.md)
