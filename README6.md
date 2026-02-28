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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f44d078-c241-3e01-864d-4d17ff75f9b1 | 1.47489 | -59.91512 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f64cc2c7-71d2-3a08-b8ce-b64b1558d8ff | 1.47787 | -59.93343 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 2ccd22f8-f5c8-38d7-b885-4100b7eb58e7 | 1.4913 | -59.93877 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f768943-7620-3540-add5-cd19658407a7 | 1.4678 | -59.92003 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8a7fb1c-2d43-343f-913c-7d380cfee3cc | 1.75231 | -61.17281 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f6f378bc-8323-38ba-9c41-2bf971c657b3 | 1.48009 | -59.91825 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f9b15a2-4e26-3df5-a7ee-d2ecd0af4fda | 1.48893 | -59.92414 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 0356e050-7aec-3d15-92e3-a71a051103ca | 1.47669 | -59.92614 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 78770f00-8380-37be-ade4-f61e4d3f003d | 0.2373 | -60.51294 | 2026-02-28 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ecc39fc9-a747-3402-9869-a912fc9a2999 | 0.96563 | -60.39093 | 2026-02-28 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ba32e76-12e4-3318-ac5f-9efce5f73218 | 1.476 | -59.91889 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32b83dfc-7c71-3397-b75d-046a0848e4d6 | 1.83732 | -61.11982 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 53baa330-2893-3d45-a5de-3f5eb027d559 | 1.47475 | -59.93782 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5c6ea56-1f53-3c43-a913-145671d4e238 | 0.66869 | -60.01601 | 2026-02-28 05:48:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9adeccac-27e6-323f-901d-8612611c4c00 | 1.51052 | -59.92815 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9057805a-dde8-38a5-aab9-11f88df00442 | 2.87745 | -60.60076 | 2026-02-28 05:48:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4847cde-f01a-3ae1-a286-b03b24758269 | 1.47897 | -59.91442 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cce46f0f-89e4-3474-ae36-e7fa1bb4df5b | 1.5076 | -59.93603 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e119a11c-b2a6-3cfd-b990-707359176143 | 1.48774 | -59.91676 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51017098-faad-3857-a3f0-c7a79f3c4ce9 | 2.87211 | -60.59183 | 2026-02-28 05:48:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 708dff9c-fb88-3143-a004-8d3000f07c8b | 1.50179 | -59.9259 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d0ec4338-3673-3864-b5a1-118b40636bf1 | 1.49183 | -59.91611 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cc75971-7724-3a3b-9dc4-7fead7d2dd05 | 1.46427 | -59.92428 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0b09a3e-5fac-31f2-89c5-a537621f8ebb | 1.50059 | -59.9185 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 264cead8-af47-34ef-bb99-82df15e600bb | 0.22875 | -60.51076 | 2026-02-28 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf5fa754-5f84-3685-a6ca-bebddf30339b | 0.6728 | -60.01536 | 2026-02-28 05:48:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 64434ed5-4f14-33c0-92cd-93a572ff4cd2 | 0.91915 | -60.33062 | 2026-02-28 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54a0467e-bfc3-35b0-81a3-8d59c25b11e3 | 1.48255 | -59.93645 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2175150-8dca-3902-9c51-a13db6eef089 | 2.11677 | -60.80114 | 2026-02-28 05:48:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4cc0435-a457-3827-96e1-1da3aca79acc | 1.47549 | -59.91878 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2caf98ed-d7c7-3ada-b481-6b5fc53080e5 | 1.51575 | -59.93461 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 58cb4356-dc9c-302b-8069-348d5e598e87 | 1.50995 | -59.92456 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b54ac500-8dc7-3be5-9e94-4b9ddb3d1692 | 1.50238 | -59.9296 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f153dbfb-88a2-3f9d-8db3-6042751e240e | 1.48067 | -59.92197 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 8b9a1610-0a5b-347b-b3ca-34b6e7f455ad | 1.49709 | -59.92277 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 72433c10-cb5c-341e-ae52-b1e9f884d84c | 1.50527 | -59.92155 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 78dcd4e9-bca9-3412-b351-32fddebcb4c7 | 1.47487 | -59.91155 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37ce0599-5874-3351-97f6-122225282f6f | 1.47715 | -59.92628 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 675a2b54-da61-36dc-bf68-dfcfdbb3ab99 | 1.47905 | -59.94067 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e924c46d-7cb7-3590-9e22-973f35bb278b | 1.5041 | -59.9403 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 465d0435-00e8-34c3-be19-b74bfa2ef4b9 | 1.50003 | -59.94098 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 278ff109-da1b-373c-9509-010da590d5b6 | 1.48018 | -59.92186 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 66d7da3c-2b38-3526-9595-07a03eb59a8f | 1.49301 | -59.92344 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 63304a94-03d1-333e-aaad-900e897733b8 | 1.47543 | -59.91523 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f518220-c36f-3195-a5f6-910472950774 | 1.5111 | -59.93173 | 2026-02-28 05:48:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 450f4210-c894-3ad6-862b-a4d6316b3ff7 | 0.96163 | -60.23384 | 2026-02-28 05:48:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f94c7167-8b19-3ec8-b7c6-93ce9564136a | -11.94729 | -64.02386 | 2026-02-28 05:52:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55d559b3-5c30-35be-88de-25708d322721 | -21.68996 | -56.32033 | 2026-02-28 05:54:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8f039415-c590-3712-b65b-c58a3ef24890 | -21.68296 | -56.31964 | 2026-02-28 05:54:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb05a182-e109-3ccc-a757-aa8a7f7da119 | -21.6895 | -56.32714 | 2026-02-28 05:54:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 728ea0b5-9dcc-3bbc-8a01-70d7a1fc1970 | -21.69113 | -56.32344 | 2026-02-28 05:54:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cf5292bc-f734-3f12-91f3-b6b0d286ff2e | -21.68411 | -56.32297 | 2026-02-28 05:54:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 839cf039-a2cc-37fe-b305-3b8e75b6a9d4 | -21.6825 | -56.32642 | 2026-02-28 05:54:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9e0f47e-b029-3d57-b1fa-9e48048f28e6 | 3.37128 | -60.54519 | 2026-02-28 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35aa64f3-38c9-307a-9535-30cdc80d8d9e | 3.42991 | -59.86882 | 2026-02-28 06:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 813e3d23-ffe8-36fd-9f93-b81462bfe8a4 | 3.15495 | -59.90956 | 2026-02-28 06:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1d4e4cb-e85d-3b68-9ad7-6f7a87e2199b | 4.80822 | -60.16393 | 2026-02-28 06:16:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6be2697-df74-3765-b538-cad77d6888d6 | 4.44263 | -60.74992 | 2026-02-28 06:16:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dedde72f-e6e1-3057-b8d6-7cfd1bc8909d | 3.15415 | -59.9049 | 2026-02-28 06:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa01a3e8-e9b0-34f6-8fc9-86b6b1c4c9f4 | 3.37762 | -60.61658 | 2026-02-28 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b18d4fc-835b-3739-a11a-447c221f5ca1 | 3.37878 | -60.61425 | 2026-02-28 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86a52a53-f154-36e1-89ae-6721aaaee602 | 3.43077 | -59.87048 | 2026-02-28 06:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e20e456-1d66-381a-adb4-2ab01f9ee52c | 3.37296 | -60.6153 | 2026-02-28 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae44c6b6-2b4c-3dfe-9b97-94b1677b2b8f | 3.42467 | -59.87157 | 2026-02-28 06:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0ba8cf9-0617-3951-8d46-2d57daf3ee02 | 3.37433 | -60.62359 | 2026-02-28 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1181105d-4e95-371b-a87d-8691a72b4f99 | 3.06696 | -60.27834 | 2026-02-28 06:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b4f52f7-120f-3604-be34-c27429f09900 | 3.15456 | -59.90673 | 2026-02-28 06:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 629f2e76-e503-3cb8-80e6-767029458e1f | 3.37365 | -60.61945 | 2026-02-28 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1485d3dd-9d43-3090-9996-acbe17b7bd51 | 4.809 | -60.16833 | 2026-02-28 06:16:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 63174298-5f7b-379d-abf0-c177093b4766 | 3.37617 | -60.60821 | 2026-02-28 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6832d95-508a-3eb4-a607-368b94f17a6d | 3.04902 | -60.28149 | 2026-02-28 06:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ca7405d-1d50-3f1d-a9da-8c74a3f0d912 | 4.43793 | -60.76523 | 2026-02-28 06:16:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80718409-5c2a-331b-9b1a-5a098a2a1b2c | 4.43166 | -60.76274 | 2026-02-28 06:16:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d05a865-d425-3261-9ec2-4a3d26d35336 | 3.06023 | -60.27493 | 2026-02-28 06:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba11cb59-3b52-3cf0-bedb-882db70d0b6e | 4.44819 | -60.74831 | 2026-02-28 06:16:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 684b0e49-b4aa-36fa-a52b-3fe26e1384a4 | 3.05425 | -60.276 | 2026-02-28 06:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7602913c-ef6a-3275-8b61-2d8ccf61fae6 | 4.43736 | -60.76192 | 2026-02-28 06:16:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 594ed654-48fc-3db3-8c42-77327e9a641b | 3.37713 | -60.54419 | 2026-02-28 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e178bcf9-1040-3df4-8d5d-fc28c3a53d55 | 3.04977 | -60.28593 | 2026-02-28 06:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0f62061-b99f-3574-bbc7-385169da7075 | 3.42828 | -59.85958 | 2026-02-28 06:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5379fdb-8be9-3181-b210-862cab2d2cc3 | 3.3769 | -60.61242 | 2026-02-28 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b7e2aaf-feb3-335e-a0df-b89173ff59f0 | 3.37642 | -60.54002 | 2026-02-28 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9350123a-99fb-32ce-9b23-492df50a2c34 | 3.4292 | -59.86122 | 2026-02-28 06:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e689dbc4-647e-320d-8503-bf4012a1b126 | 3.37808 | -60.61004 | 2026-02-28 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aab894eb-87ff-3506-bdc0-c881e8f889ca | 4.43107 | -60.75931 | 2026-02-28 06:16:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 172f7c92-2aa9-3b79-93d5-930c8eb60500 | 3.37226 | -60.61112 | 2026-02-28 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34e2d901-bea6-37a3-8a1f-54b54fb8ee5d | 3.37252 | -60.62175 | 2026-02-28 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4a440cb2-662e-3d65-8c5f-12806d571010 | 3.42841 | -59.85659 | 2026-02-28 06:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82af92a7-a86f-3b29-9f9f-aec3789c3b58 | 3.37108 | -60.61346 | 2026-02-28 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c11b1aa1-e539-30b7-8704-a124581eb7e7 | 3.3718 | -60.61761 | 2026-02-28 06:16:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| acc1e8c6-790b-3ed5-bfde-0650f18fa2fa | 4.80234 | -60.16487 | 2026-02-28 06:16:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a103e3d-8052-3cb2-a602-feb068c41666 | 3.055 | -60.28041 | 2026-02-28 06:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d86f4079-f1e1-3b02-b462-5201f5f2f1a3 | 1.49236 | -59.93328 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 604f02a1-9b8a-3af1-b500-ec8f3652fdae | 1.47184 | -59.92606 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| eb57b359-c2a0-316a-aab2-42a277056917 | 1.48444 | -59.92434 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 1c0a612e-2602-3b7d-bf46-c8b97621fc4f | 1.49613 | -59.91706 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b09aa357-2801-3fef-b312-a29d6aea4023 | 1.5049 | -59.93127 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 05d73a9e-ac72-3969-833f-7d770b4c649d | 1.47517 | -59.94606 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 73427104-fbe6-3bfd-ac7b-cd289019e70e | 1.51189 | -59.9346 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 129e57e7-609e-32d7-8ab5-be952d627313 | 1.47982 | -59.93531 | 2026-02-28 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.3 |


[Clique aqui para ver as próximas entradas](README7.md)
