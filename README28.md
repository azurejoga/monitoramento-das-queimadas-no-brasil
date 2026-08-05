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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8dbb77f-d023-3cce-9188-386bbd6bf772 | -11.183 | -54.8991 | 2026-08-05 06:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 38ff77a8-b28a-3563-b3d1-ec502a3b3cb1 | -11.1642 | -54.9007 | 2026-08-05 06:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| b55e97cd-1b91-3a69-b998-eb973836b5e0 | -11.1828 | -54.9194 | 2026-08-05 06:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 0f8c068a-8ff1-3185-a1dc-02916783eccb | -12.5947 | -46.9301 | 2026-08-05 06:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 15955482-7e5c-3ee5-9b9c-84e3f366485a | -11.183 | -54.8991 | 2026-08-05 06:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 88742fa1-cbac-3fc1-b68a-ad35d0a8987d | -11.1828 | -54.9194 | 2026-08-05 06:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| aec65b85-8edb-3561-81fe-d8022148b302 | -11.1642 | -54.9007 | 2026-08-05 06:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| af94eec4-9fee-3d02-a6ba-448703e45cd7 | -9.95501 | -67.19886 | 2026-08-05 06:27:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21bbe5aa-7ce4-3d40-8bf8-3aad6b63e5e1 | -11.183 | -54.8991 | 2026-08-05 06:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 8016c023-fca8-39aa-b3f7-30dfa092a617 | -11.1642 | -54.9007 | 2026-08-05 06:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 8c36266b-9337-3b17-8506-77c657d79338 | -11.1828 | -54.9194 | 2026-08-05 06:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| baafc165-aa74-389b-b6e8-4ecc9863da90 | -12.5754 | -46.9329 | 2026-08-05 06:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| cd2fb3ce-56e4-3853-b181-f90dca0ac8d6 | -11.183 | -54.8991 | 2026-08-05 06:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 5d2da3bb-3410-370e-ad33-21741cd9777f | -11.1828 | -54.9194 | 2026-08-05 06:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 93200275-7600-3296-becd-f9b53f1659c7 | -11.1642 | -54.9007 | 2026-08-05 06:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| b59cf2bb-f0ee-3f34-a507-dff1f442822a | -12.5947 | -46.9301 | 2026-08-05 06:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 40174b0a-216b-34fb-9633-0bbea773fa29 | -12.59252 | -46.94476 | 2026-08-05 06:44:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c3f8bf56-23eb-319c-ac1c-bb9106d89cf4 | -12.57925 | -46.93697 | 2026-08-05 06:44:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ec97ce9d-01e3-385c-ba91-d5e143bfe092 | -7.62912 | -45.31058 | 2026-08-05 06:44:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| aae237e0-4db5-3c31-be6b-fad148de2f98 | -11.16774 | -54.9086 | 2026-08-05 06:44:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| d813976d-6489-3c1b-b709-8c8e1aa5a678 | -11.16028 | -54.90158 | 2026-08-05 06:44:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| fa8f90e5-387f-369f-a2ca-ad9f6196ca70 | -8.34397 | -45.97642 | 2026-08-05 06:44:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 3308ac70-5826-3c6f-8db2-cf35bed0c9e3 | -12.57769 | -46.94788 | 2026-08-05 06:44:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 929aa0bb-75e0-358f-aa3d-9b1ddfe83f8a | -6.54488 | -55.16384 | 2026-08-05 06:44:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| b610e0ff-d4ff-3885-a9ec-dbe25f41e6f4 | -4.46176 | -47.91888 | 2026-08-05 06:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9617d2d3-0c87-3f08-93fc-f9aedf9c8d6f | -11.17204 | -54.90365 | 2026-08-05 06:44:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 6a7bb710-f967-3e6d-896a-92bfed25567d | -2.89263 | -48.01792 | 2026-08-05 06:44:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 50bcad49-4d87-3322-a1f6-2696417d4d6e | -6.89806 | -42.40951 | 2026-08-05 06:44:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 6b78fe06-479a-3c4e-b0c1-c0090a74a8bd | -12.58881 | -46.93856 | 2026-08-05 06:44:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 51332c32-1487-3e1f-9bc7-1d85b753da9f | -12.58083 | -46.9259 | 2026-08-05 06:44:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 84b5d229-e378-3ff5-b194-36e8c66578b0 | -9.60656 | -47.76569 | 2026-08-05 06:44:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9d40a2cb-741a-3def-ba35-656fe0b8259f | -6.54839 | -55.14261 | 2026-08-05 06:44:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 4e488307-71c8-3327-b93b-bb15e5f0588e | -12.58726 | -46.94941 | 2026-08-05 06:44:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 6796c40c-3ac1-3ab4-ae2b-37f7f6daa652 | -8.35358 | -45.97786 | 2026-08-05 06:44:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| f9192720-f158-35e0-960e-309bfa99d45c | -4.36633 | -47.76451 | 2026-08-05 06:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7cf7cd00-e6af-3360-ac9f-62df564e3b7d | -12.44825 | -50.37555 | 2026-08-05 06:44:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 884906ab-1528-3cde-8194-9f749bdaaea4 | -11.17071 | -54.89153 | 2026-08-05 06:44:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 4f4b9e90-0936-3bb5-b52a-f8926fb21094 | -12.3161 | -53.17666 | 2026-08-05 06:46:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 77d644a8-5873-353c-8e42-46cd29d62bbe | -13.24295 | -54.2747 | 2026-08-05 06:46:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 86871365-f62b-3788-bc61-faf1ce343eb3 | -13.24534 | -54.2607 | 2026-08-05 06:46:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 33.1 |
| b03e3812-78ab-36b4-9769-5eb7271969f9 | -11.1642 | -54.9007 | 2026-08-05 06:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| e5e465e6-fd23-3854-ac41-a31343f48a00 | -11.183 | -54.8991 | 2026-08-05 06:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| fa469288-a474-3681-b24a-0d3b12d8a71b | -12.5947 | -46.9301 | 2026-08-05 06:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| a6871028-19dd-31f5-a596-63c43617bf66 | -11.1828 | -54.9194 | 2026-08-05 06:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 2eee4410-07e7-3767-954b-8efb811b8e9d | -12.5942 | -46.9527 | 2026-08-05 07:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| b37347fa-1d93-3ebf-9dcc-cf38a91252b0 | -12.5947 | -46.9301 | 2026-08-05 07:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 408e825d-1e25-38c9-866f-210d59946667 | -11.1642 | -54.9007 | 2026-08-05 07:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| aba1dd57-77ef-3e60-88e0-3b23fdcac18a | -11.1828 | -54.9194 | 2026-08-05 07:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| c8853acf-11ba-3856-96fd-9fe5ab8b8509 | -11.183 | -54.8991 | 2026-08-05 07:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c3573fa4-e024-3e5b-b16d-9df8382bcdd6 | -11.1828 | -54.9194 | 2026-08-05 07:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| b00f563c-a4cf-3fb5-aca9-28a90295f61f | -12.5754 | -46.9329 | 2026-08-05 07:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| ddf7bd1f-90fe-30e2-ae43-4ae9b3a387b2 | -12.5947 | -46.9301 | 2026-08-05 07:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 4ad77d2a-f606-32bf-990a-14750fbcc56d | -11.183 | -54.8991 | 2026-08-05 07:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| e202b3c2-2541-30e7-a856-111c13c16881 | -11.183 | -54.8991 | 2026-08-05 07:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 49861ba6-6e33-3d53-9eb0-b84fa62c0e7c | -11.183 | -54.8991 | 2026-08-05 07:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| e10c1b7a-b818-3fa5-9907-4c555f0e7ad1 | -11.1642 | -54.9007 | 2026-08-05 07:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 66b84147-a36e-39c9-94ea-9b96619bdd2c | -11.183 | -54.8991 | 2026-08-05 07:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 8ec81676-0ddd-3a24-b81c-6eb1596eaa4b | -11.183 | -54.8991 | 2026-08-05 07:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 40919001-7632-351f-9b5c-04328dc8b2d6 | -11.183 | -54.8991 | 2026-08-05 08:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| dbebecf3-dc38-3cf2-ac89-2d606cda12b6 | -11.183 | -54.8991 | 2026-08-05 08:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 279c42fb-ffaf-3177-b1e4-d6e0772fdd27 | -12.5942 | -46.9527 | 2026-08-05 08:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| e586463f-b137-37e6-ad60-9f254bad10e1 | -12.5754 | -46.9329 | 2026-08-05 08:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| fe7ed361-1ec8-30ae-8952-d7cca1ca92b8 | -12.5947 | -46.9301 | 2026-08-05 08:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 77b7bdc2-42c6-3345-a298-7e9d9e3c630d | -12.575 | -46.9555 | 2026-08-05 08:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| d7bcf79d-edf2-37a9-944a-8c4e12826b4b | -12.575 | -46.9555 | 2026-08-05 08:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 3e5ddb33-5876-35cc-8b3d-d4666ea05a1e | -12.6135 | -46.9499 | 2026-08-05 08:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 2a139bca-7c6a-347f-a580-724dcd71dcb9 | -12.5754 | -46.9329 | 2026-08-05 08:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 74f27a45-3ddc-3c0a-a9cd-5ad52436d059 | -12.5947 | -46.9301 | 2026-08-05 08:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 025ec283-4602-3348-b69c-23c933dc0922 | -12.5942 | -46.9527 | 2026-08-05 08:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 155.4 |
| f4afad01-0dfd-38bf-8fc1-8f2d83801603 | -11.183 | -54.8991 | 2026-08-05 08:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 2b3fd0b5-0db7-3193-aa93-0bf457a5ea6f | -12.5942 | -46.9527 | 2026-08-05 08:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| dea28d24-8ccc-30a3-94c7-fad57373f64f | -11.183 | -54.8991 | 2026-08-05 08:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| a78f153c-cff5-34bc-929e-884bfca90759 | -12.5754 | -46.9329 | 2026-08-05 08:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 6543f290-5c60-3d27-be7a-101f77e67065 | -12.5947 | -46.9301 | 2026-08-05 08:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| d616eb94-71f9-3567-aa76-96c19123ca36 | -12.575 | -46.9555 | 2026-08-05 08:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3ea0c266-835b-3393-9410-ca90ec728aa0 | -12.5947 | -46.9301 | 2026-08-05 08:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| d1227433-1931-3817-848b-4d6820aea16c | -12.5754 | -46.9329 | 2026-08-05 08:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| e2e51d27-087c-3a62-a91f-98436fd1caa6 | -11.183 | -54.8991 | 2026-08-05 08:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 49e3da4a-8450-3e07-8cbb-4c0bb8696ff7 | -12.5942 | -46.9527 | 2026-08-05 08:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| bf90b443-13ff-3cb7-b195-4c11c658b623 | -11.183 | -54.8991 | 2026-08-05 08:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 00c0ac31-41cb-3605-be93-44aba14dcd09 | -11.1642 | -54.9007 | 2026-08-05 08:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 1835e597-cfab-3972-9f11-46b051262a51 | -11.183 | -54.8991 | 2026-08-05 09:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| cff9c9a8-b692-37ec-98ba-4a65a32230d8 | -11.183 | -54.8991 | 2026-08-05 09:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 8602b1f1-a518-3616-8ce9-a4017333360d | -12.5942 | -46.9527 | 2026-08-05 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| a9a22550-2e06-3e3b-bfd8-1d9bfac25496 | -12.5754 | -46.9329 | 2026-08-05 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 152.5 |
| e2105181-98a7-38e5-af65-8e995daa7964 | -12.575 | -46.9555 | 2026-08-05 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| e6153534-d12d-31f6-9e12-52851203c887 | -12.5947 | -46.9301 | 2026-08-05 11:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| fcc03fd9-3986-3de0-910c-0e432c3ff10c | -12.5942 | -46.9527 | 2026-08-05 11:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 914f1404-8b8d-3760-9d01-99a126fbfdae | -12.5942 | -46.9527 | 2026-08-05 11:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 124.7 |
| e7bd6b8a-4f45-3a9d-abda-caf50c0140c8 | -14.2682 | -45.287 | 2026-08-05 11:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| c1a4170d-8500-3c21-9d09-ad5f80a47923 | -5.13195 | -41.91595 | 2026-08-05 11:36:00 | TERRA_M-M | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 8a420dac-9204-3aa2-bd5f-be1b6cd4d94e | -3.10324 | -40.22541 | 2026-08-05 11:36:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 26.3 |
| ce6079d5-dfa8-3e5b-aa81-338f46fd0cea | -5.12582 | -41.91901 | 2026-08-05 11:36:00 | TERRA_M-M | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a0028b81-25cd-3a20-9fd8-3c5f4219b461 | -4.01491 | -38.26157 | 2026-08-05 11:36:00 | TERRA_M-M | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| a4296940-4ec6-38f0-ad89-669bc3aa7cff | -8.3546 | -45.98834 | 2026-08-05 11:38:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8dd8c309-ad31-340e-8b46-cd7ff02a20e3 | -7.21874 | -43.34891 | 2026-08-05 11:38:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| c752c4a5-9896-356b-8e29-aaa2a1a2e5a9 | -6.09542 | -43.67136 | 2026-08-05 11:38:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e61272dc-da40-342c-b85a-695619d8f741 | -5.73868 | -46.07733 | 2026-08-05 11:38:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5778247c-c0ec-3987-8cf4-cc02f810968f | -8.35041 | -46.39495 | 2026-08-05 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5473a1e5-ad7f-36b7-8283-6fcef4abf885 | -8.35177 | -46.38557 | 2026-08-05 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |


[Clique aqui para ver as próximas entradas](README29.md)
