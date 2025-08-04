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
| daab0bfd-9b2f-3fd6-8b19-0006aa745d76 | -9.4196 | -40.3447 | 2025-08-04 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 49.7 |
| f4a87860-b90e-361f-910b-371091b2f4c4 | -6.6329 | -59.9649 | 2025-08-04 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 808bffce-57c5-3c91-8c31-5bf50f5696fa | -22.5648 | -42.159 | 2025-08-04 00:50:00 | GOES-19 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 91.6 |
| f592a5a1-a257-3ad2-87f6-84c248a51568 | -6.6144 | -59.9656 | 2025-08-04 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 7ca2871e-416f-3e1b-9002-ec92c4652350 | -9.3989 | -45.4928 | 2025-08-04 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| ea4f0266-246d-36f9-ab77-49dd64f7fe75 | -5.2812 | -44.87512 | 2025-08-04 00:50:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 6acc5b77-0054-3a0e-9116-5a1970957139 | -6.14738 | -57.90268 | 2025-08-04 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a1f4f2b6-a127-3bb7-874d-59265659b89b | -4.12629 | -47.65578 | 2025-08-04 00:50:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| f6be57ce-e81b-380b-a757-92fb370e7c51 | -4.1276 | -47.64993 | 2025-08-04 00:50:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 63c128c6-6ecb-3805-bb24-266102f9dbd0 | -4.12435 | -47.64206 | 2025-08-04 00:50:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| fbc069d7-6d0d-3698-b6f0-bbccc2b9159a | -6.62612 | -59.96322 | 2025-08-04 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 7fb44d65-3091-312c-9a0a-56c0d127c58b | -5.28465 | -44.89731 | 2025-08-04 00:50:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 94c09523-5326-3ae8-95e4-53fc7f6bed98 | -6.62481 | -59.95692 | 2025-08-04 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 16391b1e-c00d-3f06-93bb-b2ff3cdf3dd4 | -7.02162 | -59.85443 | 2025-08-04 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 9f27e9f5-9572-3ab9-b379-1ff8a3f39db9 | -6.65641 | -59.12218 | 2025-08-04 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |
| e38e365b-f6ec-32fe-8797-18bb1bd1a7b3 | -4.77554 | -45.34096 | 2025-08-04 00:50:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| f46ee8fb-dfe9-3605-9c77-98961f29b879 | -5.87493 | -50.14889 | 2025-08-04 00:50:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| dfebbdcc-ba0f-3470-88cd-eeadfd4fd14f | -3.77457 | -52.18389 | 2025-08-04 00:50:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3a17cc24-2311-3429-8dd4-ff6dd9119d6d | -6.65336 | -59.09818 | 2025-08-04 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 8da910b2-45f8-311a-a097-ee70d2f78e97 | -6.62984 | -59.99192 | 2025-08-04 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| f3abe7c7-c4dc-3dbe-b241-8df56445f65e | -4.12556 | -47.63618 | 2025-08-04 00:50:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 55f5fd08-f873-313e-9050-f865f59ce78b | -7.01806 | -59.82589 | 2025-08-04 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 8aa068a3-e573-3d3b-958c-be39058a6e6a | -6.14985 | -57.92154 | 2025-08-04 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 0943bdab-c0da-3cff-9dd9-be0cbbff70ed | -5.28671 | -44.88075 | 2025-08-04 00:50:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| aa6db3ec-6304-3498-8d65-07ad9e6d07d8 | -4.12967 | -47.66385 | 2025-08-04 00:50:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dcc4b8aa-2dd1-325a-addd-7d23ba84c92a | -4.74074 | -44.44198 | 2025-08-04 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 132.4 |
| ccad436a-e295-3285-9730-606512c2b34e | -4.11666 | -47.65179 | 2025-08-04 00:50:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c59a9265-e0ad-36cb-85c8-b37900472a2f | -6.16245 | -57.91973 | 2025-08-04 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| f2fe24e3-1172-3dcb-a497-536597fc1faa | -4.73668 | -44.44818 | 2025-08-04 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| b012c96c-b905-3647-b1b5-1e4a8ca54931 | -4.73299 | -44.42347 | 2025-08-04 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| fc7eb14c-68b6-3363-a4e7-1344bf190f0c | -6.62832 | -59.98567 | 2025-08-04 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 39fb8d43-5792-3ec1-bd5f-0f8bf42d1b6c | -4.75078 | -44.44613 | 2025-08-04 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 6a8872ae-97e4-319d-8d57-facd957a6e8e | -22.5648 | -42.159 | 2025-08-04 01:00:00 | GOES-19 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 80.8 |
| 46c50a23-7483-30b0-a7bd-77da611ce754 | -6.6144 | -59.9656 | 2025-08-04 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 1909f6f8-6865-313e-87ba-d103e4e234b8 | -8.0123 | -43.1984 | 2025-08-04 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 139.3 |
| 7b198380-6e89-3ee9-89b4-3ad63a68e6bb | -7.994 | -43.1534 | 2025-08-04 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| 6761783b-c516-310d-8869-ae080711d827 | -8.0126 | -43.1749 | 2025-08-04 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.9 |
| dee0c1bf-c4cb-33d9-9a81-9673cec5bb64 | -6.1465 | -57.9165 | 2025-08-04 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 60d84bb8-5bc5-362c-943e-478cf7e6669f | -8.0129 | -43.1513 | 2025-08-04 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.1 |
| 5098b5ae-f59d-37fa-8a54-10d9987e249a | -10.7677 | -60.7279 | 2025-08-04 01:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| f89003ed-d284-32d3-904f-f91f1cf7fea1 | -4.1368 | -47.6435 | 2025-08-04 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| c723b151-68de-3ad0-b691-a1ba6d6a328f | -7.9931 | -43.224 | 2025-08-04 01:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| dc12bcfa-4f0c-3772-a6a4-1fb5f22e919a | -9.3989 | -45.4928 | 2025-08-04 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| c242488b-a894-3ff7-8c08-1c7e42a4b9d1 | -7.9934 | -43.2005 | 2025-08-04 01:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 141.2 |
| 59e5e5a5-03e7-3c92-9040-f3b9c9dfcd1b | -8.0132 | -43.1278 | 2025-08-04 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| 020a39a1-853f-3b67-bb21-455b896006c7 | -4.7346 | -44.4457 | 2025-08-04 01:00:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 87f2b22f-03b7-3ff0-9ca7-84c207147d25 | -8.012 | -43.2219 | 2025-08-04 01:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| dc0ab934-7393-3989-9e1b-e35073f15bee | -6.6329 | -59.9649 | 2025-08-04 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| c8a2d634-26c1-3443-ac41-d215b6ec4cb9 | -6.6559 | -59.1174 | 2025-08-04 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 8719ad38-556d-35c7-937a-8e3f8075da91 | -6.656 | -59.0981 | 2025-08-04 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 07ea255a-e6b4-31da-8160-7490417b25ae | -4.7346 | -44.4457 | 2025-08-04 01:10:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 0fdece68-524e-3424-9c86-3d761ccfeba9 | -8.0132 | -43.1278 | 2025-08-04 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| ce605b69-e060-3a5d-9fba-e1a3a87c9f6d | -7.9931 | -43.224 | 2025-08-04 01:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 9945ae0b-d169-3d83-ada9-0c591a689361 | -8.0129 | -43.1513 | 2025-08-04 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.3 |
| b7f9f091-71c2-362a-8d51-80fe7834003e | -9.3989 | -45.4928 | 2025-08-04 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 3b338dbb-e226-3236-a874-dc228b482373 | -6.1465 | -57.9165 | 2025-08-04 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 71e5959d-4be8-3224-8912-cc9975964f6f | -19.9733 | -45.7002 | 2025-08-04 01:10:00 | GOES-19 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 9bd9b816-2248-32c6-9d2f-d29a5b1e6ea6 | -6.656 | -59.0981 | 2025-08-04 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| bee88e21-a474-38af-9cc1-17e66bcf5ced | -6.6329 | -59.9649 | 2025-08-04 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| bc7ef1cd-ad2a-3502-a691-e660cf1a67e4 | -6.1649 | -57.9157 | 2025-08-04 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 2e1a794f-0000-32ce-afe0-b854ef11e01b | -8.0123 | -43.1984 | 2025-08-04 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 1fb6bd4d-ba56-304f-88d3-c0fa7e84c34d | -8.0126 | -43.1749 | 2025-08-04 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 7ee49f2c-6ea8-33c6-8357-4430b7b729bc | -6.6144 | -59.9656 | 2025-08-04 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 124b71b6-a292-35c7-ba25-57c8da1e86b7 | -7.994 | -43.1534 | 2025-08-04 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 8bfe569b-b5bd-37ad-a1ff-8ba795f61c0c | -4.7533 | -44.4445 | 2025-08-04 01:10:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 78b1f11f-03bb-3d39-923e-fe15f2572fe2 | -7.9934 | -43.2005 | 2025-08-04 01:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 113.5 |
| 8f7c678e-c48f-3bda-a7e6-69cd6c37675c | -21.1624 | -49.0512 | 2025-08-04 01:20:00 | GOES-19 | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.8 |
| efd4af63-1a86-3c6a-8533-b8af94733bb8 | -6.6559 | -59.1174 | 2025-08-04 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 8a57aaed-837b-3b50-87c1-f031cb84263b | -6.656 | -59.0981 | 2025-08-04 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 12cb2eac-fd0c-39a4-a811-10b4a115ee9a | -8.0123 | -43.1984 | 2025-08-04 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| c9939fc0-1e82-33a6-bc0a-954c6cf3bb44 | -8.0126 | -43.1749 | 2025-08-04 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| ac3c87b8-5c1b-391c-b8cf-bf07255c2239 | -8.0129 | -43.1513 | 2025-08-04 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 131.1 |
| 369a940c-eef6-34a8-86cb-db5e5c6086e2 | -7.9931 | -43.224 | 2025-08-04 01:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 60.9 |
| 9807654e-bdac-3e61-b881-507117e35445 | -9.3989 | -45.4928 | 2025-08-04 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 51bf97b3-c7d2-3a59-bc98-0e14db676b24 | -6.6329 | -59.9649 | 2025-08-04 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| a3abcd74-8501-385c-b161-b7c44ce68798 | -4.7346 | -44.4457 | 2025-08-04 01:20:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 4beee26c-d781-39ea-81b1-061f2863e140 | -7.994 | -43.1534 | 2025-08-04 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 101.3 |
| 7a82c679-6cf3-3162-8058-ff99dd3a8fa1 | -8.0132 | -43.1278 | 2025-08-04 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 9470dd65-5327-39fb-9be0-a831b087f52d | -6.1465 | -57.9165 | 2025-08-04 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| ec143d84-b6d2-3d78-8150-39a7e4432aad | -7.9934 | -43.2005 | 2025-08-04 01:20:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| f36d17be-1e91-32c1-98a6-5b2a0721ce3b | -6.6144 | -59.9656 | 2025-08-04 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 235492cb-d918-3a6c-a864-53d3157b7797 | -4.7346 | -44.4457 | 2025-08-04 01:30:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| d6165d97-45d2-374b-b336-14db7bea9a50 | -8.0129 | -43.1513 | 2025-08-04 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 132.8 |
| 926138fb-9bb0-39b4-86d2-d70eed98fdc6 | -8.0123 | -43.1984 | 2025-08-04 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| f50e764a-5710-3020-9ff0-a4ed3fbc7557 | -7.9934 | -43.2005 | 2025-08-04 01:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 737a8138-a722-3874-9463-47bfea18f0a1 | -6.6329 | -59.9649 | 2025-08-04 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| bebf0210-4cdb-370a-b747-418375fc7e22 | -6.656 | -59.0981 | 2025-08-04 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 98e2669a-6d63-36af-8252-2caf1ff612fd | -8.0132 | -43.1278 | 2025-08-04 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 606e69d2-ae9b-360d-8ac3-1077255ef715 | -8.0126 | -43.1749 | 2025-08-04 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 95e91697-a706-3136-90f8-229e603cf8a9 | -7.994 | -43.1534 | 2025-08-04 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| f022f4f8-947a-365f-9d2e-54f080468d26 | -4.7533 | -44.4445 | 2025-08-04 01:30:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 58f5ba85-82ab-3ef4-9978-74dd63bc0dba | -7.9931 | -43.224 | 2025-08-04 01:30:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| f5a41c1f-f6bb-387b-91e4-713f26cb5055 | -6.576 | -59.965599 | 2025-08-04 01:38:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0a65d7ba-d2b5-328e-b6c5-6ecd0230f322 | -6.1042 | -57.919102 | 2025-08-04 01:38:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a511e40-82ce-3c57-aa73-213703e4df86 | -6.5815 | -59.987999 | 2025-08-04 01:38:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 754ffc42-933f-3deb-8bc9-85d5be60d9af | -6.6101 | -59.117699 | 2025-08-04 01:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bf174886-5adf-382d-87ee-c3709950e118 | -6.5856 | -59.9632 | 2025-08-04 01:38:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87f92031-b2e7-3f06-8a62-8b19a49e4267 | -8.0129 | -43.1513 | 2025-08-04 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.6 |
| f92a2513-fb78-3e1a-91c1-2ad891068878 | -7.9931 | -43.224 | 2025-08-04 01:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 90c106c2-1e5d-3481-bb47-7f8f94ff1c4b | -7.994 | -43.1534 | 2025-08-04 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |


[Clique aqui para ver as próximas entradas](README5.md)
