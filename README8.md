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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b48dd1b-441d-3ae4-88a3-aba554c628f2 | -2.7706 | -48.591 | 2024-11-16 00:47:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41964fc3-9a0b-32b2-a39c-c25b63e005d3 | -3.9145 | -45.8545 | 2024-11-16 00:47:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d99fd4e7-bcfd-3971-bc78-dbb3e7d97469 | -2.9852 | -43.931499 | 2024-11-16 00:47:00 | METOP-C | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1cb0f02b-05f7-3b54-aa36-efa91cb4e52b | -3.2994 | -43.827702 | 2024-11-16 00:47:00 | METOP-C | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07578693-c8ed-3991-b134-5d4740943e32 | -2.3926 | -54.637901 | 2024-11-16 00:47:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba79c4f6-3906-3fb7-a719-742d7c2fda9f | -3.7813 | -43.908798 | 2024-11-16 00:47:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 950f1411-e64b-30d2-83d9-a31974e4c6d6 | -4.5419 | -43.564701 | 2024-11-16 00:47:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0c020d8-ef76-3c9e-b581-c2f16fd6975e | -2.2037 | -48.815201 | 2024-11-16 00:47:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95bf4951-ab3f-3731-96ab-c5490e1457a7 | -3.5139 | -44.4259 | 2024-11-16 00:47:00 | METOP-C | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8518563e-85b1-3441-96e3-e98a40aff7eb | 0.4283 | -50.913399 | 2024-11-16 00:47:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| fee2ceff-5dc0-3b02-918c-0e953664e0f7 | -3.1978 | -45.0882 | 2024-11-16 00:47:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e8461eeb-fb6b-3d38-99d3-4d8c5ad97c57 | -4.2965 | -48.098099 | 2024-11-16 00:47:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaf8176b-f0b4-3fe0-ab3a-95b4221a6696 | -4.2825 | -48.215302 | 2024-11-16 00:47:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c9cfbc5-1d15-334d-a276-fd9f46a4f71b | -3.626 | -53.995701 | 2024-11-16 00:47:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7314b443-d603-3113-a124-38095d761820 | -2.2837 | -47.9146 | 2024-11-16 00:47:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03acf2ca-3210-3625-a430-fd130a4936fe | -17.5877 | -57.568699 | 2024-11-16 00:47:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ae2c991f-853b-3aa5-b982-75b511bd0a31 | -4.3766 | -48.575802 | 2024-11-16 00:47:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdc12306-d344-36cf-9a5a-0a78552a6724 | -3.5681 | -50.2575 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab430110-10ab-3665-babb-67d31d431985 | -9.401 | -40.345501 | 2024-11-16 00:47:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e341c730-cd3e-3bdf-8f88-6dfdf0b60bb0 | -0.7792 | -49.480999 | 2024-11-16 00:47:00 | METOP-C | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce6c3ba8-0c7a-3d41-bf14-fc0f90f943dc | -5.2374 | -44.916901 | 2024-11-16 00:47:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b4ff853-8450-3b5e-95a4-3cc25f07ae65 | -2.3534 | -47.1506 | 2024-11-16 00:47:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83c8585d-7c9f-319a-9ed0-492495c6d179 | -2.5542 | -54.035099 | 2024-11-16 00:47:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1603fd54-eab4-38b1-9e79-98f9a5986854 | -2.5696 | -54.420399 | 2024-11-16 00:47:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb512921-408c-3cbe-94e8-550a0f5fca3a | -1.2228 | -53.7075 | 2024-11-16 00:47:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 566dd8ac-0032-300f-922b-cb4dc978831c | -3.9633 | -45.7994 | 2024-11-16 00:47:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0b405f3b-e2a1-3a84-a0bb-877b1401dbab | -6.4405 | -47.865501 | 2024-11-16 00:47:00 | METOP-C | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e720b956-4ce4-3903-b2d3-c161aad8f230 | -3.256 | -53.679501 | 2024-11-16 00:47:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1854fa27-f4b4-394a-8b4e-449dd77f8920 | -3.5047 | -47.224998 | 2024-11-16 00:47:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11cf9b4a-923c-36e9-9c66-69769b4e5d5b | -3.4908 | -47.209702 | 2024-11-16 00:47:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52a746b3-16f3-3b16-92e3-31782b3025d2 | -2.1412 | -46.550201 | 2024-11-16 00:47:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae14ebcc-be6b-33ba-905d-5756377a1100 | -6.1641 | -41.1689 | 2024-11-16 00:47:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0a3add8c-c161-386d-9664-4e1df77400c5 | -3.7161 | -51.850101 | 2024-11-16 00:47:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a823941-f1e8-3081-a841-1ea3c565ae4b | 0.7995 | -50.734299 | 2024-11-16 00:47:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6e8d2496-ee98-3a10-bdd7-bad79baeb8b0 | -4.2789 | -48.199902 | 2024-11-16 00:47:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1567c07-00fc-3bd0-9dd6-0c92d4f5df8d | -5.9098 | -46.2239 | 2024-11-16 00:47:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5bd4bb33-6dac-3949-8434-49f5ba0541b0 | -2.7004 | -51.872398 | 2024-11-16 00:47:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b93f98d9-d4c8-3ac2-80fd-6a9e49ecb733 | -4.7234 | -48.114601 | 2024-11-16 00:47:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02319789-5513-3752-9f5c-3e5b054f9ac2 | -3.5164 | -49.9431 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 482e2d35-8a50-3041-b9ad-e536d9fa7f27 | -2.3671 | -54.661598 | 2024-11-16 00:47:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f2378a0-3489-3c74-9de6-ae8e666d41af | -4.9035 | -43.2314 | 2024-11-16 00:47:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb85a6f7-648f-3022-8cda-457f12e4fb02 | -6.305 | -39.489799 | 2024-11-16 00:47:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e2b7fe91-633e-3862-99ec-3426e5f5fd97 | -4.3762 | -50.722099 | 2024-11-16 00:47:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06c97b82-634b-36ad-be40-ae58ef083d08 | -3.8447 | -49.442699 | 2024-11-16 00:47:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37a961cc-665b-3b5a-ab7b-d8a8d2c0a42d | -10.6674 | -44.488899 | 2024-11-16 00:47:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 47b5a4c2-4cc2-3568-aa8e-eb207d4584e1 | -17.5819 | -57.592999 | 2024-11-16 00:47:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6ea8029f-aabd-3f00-af43-4d361437801c | -2.9296 | -45.608898 | 2024-11-16 00:47:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6b5db53b-d52c-3bd8-9acf-8615025b904e | -2.6637 | -46.186401 | 2024-11-16 00:47:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ee54ddcf-799b-3bf6-8280-1ac6dfdba653 | -2.1968 | -49.544498 | 2024-11-16 00:47:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 307a2e3c-ce39-32da-a8f1-1773cfe3b0ae | -4.0103 | -44.350498 | 2024-11-16 00:47:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9719e097-7111-30dc-a055-015707063a44 | -2.0825 | -50.4823 | 2024-11-16 00:47:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f7fafb7-b665-319d-9170-353149b6e7bb | -3.2383 | -53.510799 | 2024-11-16 00:47:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba963306-c715-36aa-815b-a9898c05fedd | -2.7867 | -48.571201 | 2024-11-16 00:47:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e140806-cae8-32d8-b89c-ae7a1e0e1779 | 0.5594 | -50.746498 | 2024-11-16 00:47:00 | METOP-C | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c31c607e-affd-3da2-a63d-acab30d6f522 | 0.4381 | -50.9156 | 2024-11-16 00:47:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e1e2133d-e195-35d9-9ace-b444b0726be1 | -2.3749 | -54.650799 | 2024-11-16 00:47:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35a41849-e4ce-39e4-b8e3-1bd5047b62ad | -3.7383 | -50.190399 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4aa97d33-6290-3391-8741-1affca3617eb | -2.9718 | -47.991199 | 2024-11-16 00:47:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 182712ce-4d71-3df6-8c01-4c1a1f71b4dd | -0.6902 | -48.557301 | 2024-11-16 00:47:00 | METOP-C | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8fe8d24-4f1a-36a3-8007-7744803655af | -10.5357 | -44.669998 | 2024-11-16 00:47:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ae2887b9-356c-3ccd-b104-724b23f0dc77 | -2.5677 | -54.411999 | 2024-11-16 00:47:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 746f1477-6588-3eab-b3d3-3521734399d9 | -2.5551 | -46.9109 | 2024-11-16 00:47:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bfbee6a-9cd2-3421-90e4-b50028e9c75d | -2.7769 | -48.573399 | 2024-11-16 00:47:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a435639d-ea95-3f81-b8fd-bc5c2d64adf3 | -4.3746 | -50.715302 | 2024-11-16 00:47:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f74bdff2-f16e-33c5-9aad-df6dc63c988f | -5.2401 | -44.9282 | 2024-11-16 00:47:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9a9652c-e02b-3877-b04c-d9bd5a70f2b3 | -3.5721 | -52.2136 | 2024-11-16 00:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83c683c8-fe53-348a-9fb7-1875513eea38 | -3.5705 | -52.206501 | 2024-11-16 00:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cec722b3-e885-3ffe-bdc0-4c821194b7e2 | -2.9699 | -47.983101 | 2024-11-16 00:47:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78ee547d-9e0d-3d0d-887e-6b13e58db80d | -2.5409 | -46.894501 | 2024-11-16 00:47:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e57c315-7dea-3d78-ba17-a07be67703c4 | -3.6064 | -52.228199 | 2024-11-16 00:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5e2baf6-24ff-3f73-9b4b-039f4e4b8918 | -3.7636 | -50.7948 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfa7817f-6104-30e3-959b-b999f64a0976 | -3.3892 | -53.267799 | 2024-11-16 00:47:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f835260d-f94f-3334-94e1-b6f7fbe27d67 | -1.2115 | -53.567799 | 2024-11-16 00:47:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8827c530-e95e-3750-be08-22744d9e75af | -3.1933 | -45.5481 | 2024-11-16 00:47:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ca989f77-6d29-3d53-ba96-bdc7e4fe5e22 | -1.6382 | -53.2705 | 2024-11-16 00:47:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5bbf900-9bda-337f-bbb9-e231d1168eb7 | -2.1393 | -53.704899 | 2024-11-16 00:47:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d13f53c-bbb9-340f-bcb4-5ca8100b6fb4 | -1.5191 | -47.107201 | 2024-11-16 00:47:00 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c427ceb-170a-32f2-870d-6b4b1222e2c5 | -2.5529 | -46.9016 | 2024-11-16 00:47:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 641919f5-4b5b-3afa-a5eb-c39495983e49 | -2.6161 | -54.534698 | 2024-11-16 00:47:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4af7c1d-9532-3310-99aa-635949379669 | -2.3476 | -47.479698 | 2024-11-16 00:47:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6206697e-5a2a-360f-96b1-673b9ae59c51 | 0.8203 | -51.1381 | 2024-11-16 00:47:00 | METOP-C | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 68e73fcb-10a1-39aa-8533-2efd01e334dd | -2.1435 | -46.560101 | 2024-11-16 00:47:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cb9e911-6271-3f54-a8ab-8b344d5b045e | -2.679 | -46.823502 | 2024-11-16 00:47:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 818df1fb-9701-3f57-b620-6b42db1e74d6 | -17.5411 | -57.530998 | 2024-11-16 00:47:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 40ad0f1f-d7ef-345a-a729-876122ae2f05 | -2.5716 | -54.428902 | 2024-11-16 00:47:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b46cf743-ace2-3713-83a7-edd73c0db426 | -2.6613 | -46.176102 | 2024-11-16 00:47:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 725feb6e-434f-39da-8383-9029226699a6 | -2.6988 | -51.865501 | 2024-11-16 00:47:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e5b2f11-fdea-3f33-868d-c5193c0593d0 | -1.6908 | -54.268398 | 2024-11-16 00:47:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af49f715-be86-3bda-82a8-d1e2fcfc47d8 | -3.7846 | -43.922699 | 2024-11-16 00:47:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 17022d9c-a573-3d55-8775-c53f5a8f84da | -5.9 | -46.2262 | 2024-11-16 00:47:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f47007d-8cc8-312e-a713-7ad27c1c4325 | -2.6521 | -48.480099 | 2024-11-16 00:47:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 157f70e2-8ee7-3885-bbda-d33d153a581a | -4.5574 | -48.022202 | 2024-11-16 00:47:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1abed119-c76c-37f5-a76e-02fcf24faa66 | -3.391 | -53.275398 | 2024-11-16 00:47:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 487e7ca0-737b-3e67-b827-4f9e1498587d | -4.149 | -50.7658 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f33c099-dba5-32bf-94f6-35d30d6ccb82 | -4.2201 | -50.671001 | 2024-11-16 00:47:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbdeb430-f602-35cf-a525-c9db70fbae4d | -3.5756 | -50.514599 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e204b28-6cb5-35d4-8257-523c7ecaf46d | -3.039 | -45.112499 | 2024-11-16 00:47:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 510ff918-39a7-3684-aef3-8b33fde2a8e9 | -2.1779 | -47.9473 | 2024-11-16 00:47:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c84638b6-e3a8-3e7e-b91d-8520a74a3760 | -1.1318 | -54.165699 | 2024-11-16 00:47:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a216d96-cdbd-32c8-9dff-5596af1cbf7c | -2.6423 | -48.4823 | 2024-11-16 00:47:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
