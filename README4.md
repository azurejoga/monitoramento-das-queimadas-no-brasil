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
| a047c7c4-e09d-39ce-88e3-85fa0208b4fe | -10.6725 | -58.749 | 2024-10-23 00:46:07 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| ed92185d-57b1-3def-90dd-8439de937058 | -11.0262 | -48.2724 | 2024-10-23 00:46:08 | GOES-16 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| c16c5c12-e6ee-3845-b9ec-5896adf6b4f1 | -11.3217 | -54.3564 | 2024-10-23 00:46:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 59577997-0ff3-3e85-bd86-4f2ae2583f84 | -11.322 | -54.3359 | 2024-10-23 00:46:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 9f6ffedc-b767-39e1-a0fd-30db57a5ee11 | -11.3406 | -54.3547 | 2024-10-23 00:46:11 | GOES-16 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 655eef5e-ce1c-3ca4-8c58-d24366b5542b | -17.6671 | -57.4616 | 2024-10-23 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.3 |
| f0b79955-e027-3917-8c30-45211b95a06c | -17.6674 | -57.4411 | 2024-10-23 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.1 |
| c3091560-6af0-38cd-b174-ff3cc602e57b | -17.6868 | -57.4593 | 2024-10-23 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 52f1f6a0-45d1-3edf-ba4c-96b4608301be | -17.6871 | -57.4387 | 2024-10-23 00:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 3e5f86f1-72f7-309a-8cfa-62444ee1d0fe | -5.7661 | -45.55742 | 2024-10-23 00:48:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| a0649789-e801-3c27-99d7-8f70d797160d | -5.75981 | -50.22301 | 2024-10-23 00:48:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| eeda53d6-c783-3433-a51c-01d87ccef256 | -5.75848 | -45.56757 | 2024-10-23 00:48:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6cf0de78-ee20-3de5-8139-b7d3cb8cb4cf | -5.75724 | -45.55869 | 2024-10-23 00:48:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 605a2693-1c15-363a-b15a-bc08987260e8 | -5.74912 | -50.22452 | 2024-10-23 00:48:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e62e4778-6011-3aa1-906f-4b6db2ca515c | -5.74192 | -48.32962 | 2024-10-23 00:48:00 | TERRA_M-M | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 445a5c30-3cd7-3e78-8db8-72a9ab819c7f | -5.71364 | -44.72776 | 2024-10-23 00:48:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2b98c37f-5c2b-35c9-9482-e2ad0fda2edb | -5.70693 | -45.00675 | 2024-10-23 00:48:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0cb708d9-3773-3c28-9749-ded515b9c9ad | -5.70565 | -44.99761 | 2024-10-23 00:48:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 750a99a4-fe79-39d3-ac70-4710897a8d33 | -5.66531 | -46.34988 | 2024-10-23 00:48:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 139027d5-0b3e-3b3f-93c2-7bbe5f9fffe4 | -5.61934 | -44.84175 | 2024-10-23 00:48:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0158f6ba-64dc-3e1e-9509-3ef596ea85f0 | -5.61802 | -44.8325 | 2024-10-23 00:48:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 6d468102-9fb1-3ffb-993d-6562732046f0 | -5.57881 | -44.88219 | 2024-10-23 00:48:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1fbcbbc9-741d-3d7b-b90e-20946d571623 | -5.50854 | -46.48336 | 2024-10-23 00:48:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 9f6da13f-6fc5-39d7-850d-9058c993f1b6 | -5.49063 | -49.51061 | 2024-10-23 00:48:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 397800c4-5662-3010-a70e-d8069e9d08c1 | -5.45235 | -46.35352 | 2024-10-23 00:48:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 22b6a7ab-bada-33e5-9304-012aef49d276 | -5.43818 | -46.91368 | 2024-10-23 00:48:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| db03857e-dfa6-3a05-9d03-be9f317e0bef | -5.42029 | -44.80413 | 2024-10-23 00:48:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a08b493c-6137-327d-9b96-6eefe8ef4ad6 | -5.41898 | -44.79483 | 2024-10-23 00:48:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 581c2a60-0f3c-36c7-818c-9ed6a9439f30 | -5.4108 | -47.11014 | 2024-10-23 00:48:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 450fe919-bf2b-3a65-a21d-07cd9cf117f6 | -5.37341 | -44.28284 | 2024-10-23 00:48:00 | TERRA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 092c73b4-3b94-3ae3-9676-3f2d3ad03ab1 | -5.36813 | -45.08915 | 2024-10-23 00:48:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d12d02a9-6828-3b91-8f31-2dcba66e9e2d | -5.36686 | -45.08009 | 2024-10-23 00:48:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2017ed61-170a-37a2-9ed4-c1c7daae44d3 | -5.3579 | -45.08136 | 2024-10-23 00:48:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 145ffcf5-37cc-38d4-a74f-99199b6de683 | -5.32026 | -45.92273 | 2024-10-23 00:48:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e31fcb8c-63be-3c31-8bd3-4de6a7ed6be0 | -5.29309 | -44.30075 | 2024-10-23 00:48:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 41d1b5dc-03be-38c8-88b2-6ae23cbb5ba7 | -5.27282 | -46.17815 | 2024-10-23 00:48:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| fe63c6c8-0a0c-39ca-bd72-95fa09113be5 | -5.27159 | -46.16935 | 2024-10-23 00:48:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 244c7111-8882-38a4-af6c-1f62130bcbe4 | -5.24009 | -50.88631 | 2024-10-23 00:48:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d9bef09a-9e20-35e9-bbb1-0dd2a7ff5578 | -5.24007 | -50.88058 | 2024-10-23 00:48:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c714291f-73a8-37ef-b35d-1af2aa719b7e | -5.22369 | -46.16451 | 2024-10-23 00:48:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fe4d8a81-87ec-399b-a08a-934ed91cb9ff | -5.21946 | -45.92502 | 2024-10-23 00:48:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 65ab2232-c22b-30c0-9edc-f0656ecac3ad | -5.16583 | -46.13681 | 2024-10-23 00:48:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d90a5984-1d1d-39fb-988c-ffebb23fa1be | -5.1645 | -44.36138 | 2024-10-23 00:48:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| c4714621-90df-3f7c-b749-3453ca0b5740 | -5.15461 | -45.2711 | 2024-10-23 00:48:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 58b6d776-0362-34e4-ab9f-313dbe161f26 | -5.14178 | -46.17308 | 2024-10-23 00:48:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a17229fe-edde-31a7-a054-fdf07f8af3da | -5.10384 | -45.75839 | 2024-10-23 00:48:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9a824ae3-0a1b-3760-91ef-65bba54ec98a | -5.09746 | -44.2219 | 2024-10-23 00:48:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e6952e38-b379-37d3-a258-8eea91489c5e | -5.00097 | -46.74527 | 2024-10-23 00:48:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2a820f1a-1c84-3838-9e1f-dd83722a2ea0 | -4.99189 | -46.48509 | 2024-10-23 00:48:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 644dbe14-d2f3-3c6e-8be2-fa57b28df556 | -4.96374 | -45.88095 | 2024-10-23 00:48:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0515ba1b-246f-3338-ba0f-a187db67289c | -4.91009 | -45.49878 | 2024-10-23 00:48:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8113ff8d-1f3f-3d76-8ed3-3fcbf9528bf1 | -4.90884 | -45.48988 | 2024-10-23 00:48:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 498777be-3e6e-3e01-ad55-10b041ccb224 | -4.9012 | -45.50008 | 2024-10-23 00:48:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3010d89f-be8f-3c41-b2fb-cabda6fdb683 | -4.89994 | -45.49113 | 2024-10-23 00:48:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c908b1d2-347d-3d6a-a146-f6f7c11810b9 | -4.86929 | -45.86432 | 2024-10-23 00:48:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7ff924d1-2ea2-3e7d-9dff-71c6f8477dda | -4.84854 | -45.52272 | 2024-10-23 00:48:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| eeaeaafc-00e4-316b-ae06-764edfa9475c | -4.80043 | -45.7087 | 2024-10-23 00:48:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f03d0396-3e75-3f11-ad3f-a9d7f7d4def0 | -4.79919 | -45.69981 | 2024-10-23 00:48:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d3288bd1-a1cb-330b-ac95-54e50544c88c | -4.78245 | -45.11735 | 2024-10-23 00:48:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| d1af09e1-3b8a-3725-afd6-5a88bca7f99d | -4.77347 | -45.11864 | 2024-10-23 00:48:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| c723dd8f-6173-3814-bc99-ea7baac24d1e | -4.76441 | -46.62836 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 28fad958-e65f-3368-9387-63be729fc063 | -4.7636 | -45.76831 | 2024-10-23 00:48:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1a9d89fc-6ea5-3108-88d9-775c7f5d8356 | -4.76319 | -46.61952 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 30.8 |
| ee9eb10b-de30-34bd-b0d2-6b00ae79b7fa | -4.75557 | -45.18627 | 2024-10-23 00:48:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3301c6af-8a95-38a2-a91a-6c9bd7066cea | -4.75474 | -45.76957 | 2024-10-23 00:48:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 28a16408-b977-318b-9a30-24a02202083d | -4.6393 | -46.06857 | 2024-10-23 00:48:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5732d6c8-7c33-3ac5-9f1d-882a1858efca | -4.75315 | -46.62725 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 793987fa-a0d1-3e0d-8a93-46a7025cd61b | -4.75192 | -46.61841 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 226cafb6-761d-3115-a736-52e80e7b768f | -4.74161 | -46.6739 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 6dbcf958-a1cb-3323-9245-59d3eba271fc | -4.74038 | -46.66504 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| ff7cccbe-9f08-3483-a5fb-707c8d781a21 | -4.734 | -46.68397 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 96feb1d8-bd5e-328f-b09c-4e1cad399c28 | -4.73277 | -46.67513 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 17da6994-48bd-3278-895a-60d565bdcba8 | -4.73154 | -46.66629 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a5135004-6111-3022-bbd5-639f96065821 | -4.73077 | -45.72765 | 2024-10-23 00:48:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4fd29356-2230-336e-880c-b9828b14831f | -4.72227 | -45.74382 | 2024-10-23 00:48:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 23.8 |
| ef5ab0dd-d042-3024-a03f-d04d6b62cbe0 | -4.72103 | -45.73498 | 2024-10-23 00:48:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 0e739b29-992b-3bbf-9189-55252448fc14 | -4.71979 | -45.72609 | 2024-10-23 00:48:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 73157c0b-3ce4-3cb4-8a77-840a9ad64ba1 | -4.7134 | -45.74508 | 2024-10-23 00:48:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| b7dc3b89-4df1-3d86-84fe-60d97cab55dc | -4.71216 | -45.73621 | 2024-10-23 00:48:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 3c7c847d-d795-331d-a082-7e1ff59766f3 | -4.70862 | -45.64602 | 2024-10-23 00:48:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c7653923-ab67-31e1-9420-c7ae3432b113 | -4.69865 | -47.49057 | 2024-10-23 00:48:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 83edb9ea-61f2-3784-9103-7d965fe4a443 | -4.69534 | -45.87421 | 2024-10-23 00:48:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9ae6554e-4f68-3726-809b-06b1bf7cfeb9 | -4.6865 | -45.87548 | 2024-10-23 00:48:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 774eabeb-41ac-318c-a522-a657d46cc96c | -4.68526 | -45.86661 | 2024-10-23 00:48:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| c7e26ebb-cf6d-3ffc-bd8b-104c2be68481 | -4.68381 | -44.61778 | 2024-10-23 00:48:00 | TERRA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b89909ce-8b1c-3651-acf3-b8a4637304a3 | -4.68244 | -44.60822 | 2024-10-23 00:48:00 | TERRA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 8f49f55f-5805-34ee-948e-2b1ee6039aed | -4.68108 | -44.59866 | 2024-10-23 00:48:00 | TERRA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b4183cd4-3563-3803-9c0c-09c2c5e2aeb7 | -4.67466 | -44.61913 | 2024-10-23 00:48:00 | TERRA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 97edf84f-a509-3fcd-9859-12275251c3a2 | -4.67329 | -44.60957 | 2024-10-23 00:48:00 | TERRA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 907cf2fa-8fa8-3b17-85c0-8b58ca597115 | -4.67191 | -44.59999 | 2024-10-23 00:48:00 | TERRA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| b0ec2ba0-22dd-378d-a7c8-31de63729fe4 | -4.6655 | -44.62043 | 2024-10-23 00:48:00 | TERRA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 479a47f8-4e8f-3708-a968-d27f920a600a | -4.66412 | -44.61089 | 2024-10-23 00:48:00 | TERRA_M-M | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 31bd2194-58d7-334c-983c-0e3c0f5e0dc7 | -4.65773 | -46.20067 | 2024-10-23 00:48:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 920e4fec-4494-38c7-ab57-32734a91cd57 | -4.63884 | -46.53244 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 3fcef9db-37ef-32fb-9784-66e320ea314d | -4.63656 | -50.91547 | 2024-10-23 00:48:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4a266339-5474-32ad-ada0-6b58a07cfcc0 | -4.63001 | -46.53368 | 2024-10-23 00:48:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 7e44c31b-c00c-3633-a4fc-65e0d71aeae4 | -4.61437 | -50.91842 | 2024-10-23 00:48:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| e1bc38af-35a4-3c4c-8f03-212f9160f18b | -4.61373 | -50.92479 | 2024-10-23 00:48:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| b8f3484b-c4ac-3719-b75f-e746567e26cb | -4.61285 | -47.53711 | 2024-10-23 00:48:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d50959e8-7ab3-35d1-b39b-73b063a4bf43 | -4.61175 | -50.91047 | 2024-10-23 00:48:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |


[Clique aqui para ver as próximas entradas](README5.md)
