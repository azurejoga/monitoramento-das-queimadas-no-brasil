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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 785531fa-ef2d-322b-9642-abf521c9f6df | -6.00188 | -49.34474 | 2024-09-28 05:08:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52e7a988-b2a7-3915-959c-7cccfa5a50e7 | -5.99702 | -49.34398 | 2024-09-28 05:08:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0ef5b4c-b3af-369a-99d9-78c0d027da73 | -5.99623 | -49.34938 | 2024-09-28 05:08:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4231d8d2-75f8-3156-97b7-de531320c4c5 | -5.94221 | -49.18956 | 2024-09-28 05:08:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 16a7dd21-2242-3068-8601-4cfc3a2cbd56 | -5.9414 | -49.19505 | 2024-09-28 05:08:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a1b1cf59-c455-3f1e-8fe5-ba35d7a10172 | -5.93883 | -49.1904 | 2024-09-28 05:08:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b5d29859-68a6-3e41-b6a8-c649aba186e6 | -5.93806 | -49.19591 | 2024-09-28 05:08:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 36717a84-1585-3292-bc34-00d3a8b2cd00 | -5.93729 | -49.20143 | 2024-09-28 05:08:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f64390df-e06b-3919-adcb-451c1c3aef3d | -5.93649 | -49.19433 | 2024-09-28 05:08:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cee47dfd-efe5-3a20-8661-61afae83b76e | -5.93568 | -49.19984 | 2024-09-28 05:08:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d69dada-a2d5-3c9c-b242-c3297e984275 | -5.21983 | -49.24236 | 2024-09-28 05:08:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a70b8d5f-7346-3b8b-b4e8-3af5d6dd6899 | -5.21497 | -49.24165 | 2024-09-28 05:08:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77a60432-76a5-3252-a093-9cf710b4330b | -7.82107 | -49.16763 | 2024-09-28 05:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b5b49bd-ce3b-39f7-b9c0-305982a1d8ec | -7.82065 | -49.17068 | 2024-09-28 05:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b6b3627-1dbc-3be1-adaa-205e1436f856 | -7.76439 | -48.52224 | 2024-09-28 05:08:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bd5de7e-5805-3efb-a6e9-c01eab1e8a9b | -7.57743 | -49.19366 | 2024-09-28 05:08:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07dafa90-558a-3451-ba4d-4fa1d6664647 | -7.57241 | -49.19275 | 2024-09-28 05:08:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73017bd4-55dd-3bfc-ab96-708ea1110b6b | -6.54675 | -48.70652 | 2024-09-28 05:08:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba121499-09ae-3e90-b5dd-760e72d2e69f | -6.54633 | -48.70956 | 2024-09-28 05:08:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44bee5bf-c642-30cb-85d0-d154565a9f06 | -8.97555 | -49.82423 | 2024-09-28 05:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 421f2076-9ebd-38d8-b613-41937194e64f | -8.97478 | -49.82978 | 2024-09-28 05:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69350e0a-85cc-30ad-8098-d2f263d8a41d | -8.93854 | -49.30686 | 2024-09-28 05:08:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f65e9fb3-644d-3b0e-a3e5-9e06dc9db6fa | -8.75379 | -49.78154 | 2024-09-28 05:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d2dd47b9-16d0-3466-bba9-b48185abaa52 | -8.75305 | -49.78713 | 2024-09-28 05:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e928c743-c04b-3657-ad84-19b286cb8796 | -8.75216 | -49.77925 | 2024-09-28 05:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 845c3111-bc47-3b97-9345-89ab19774626 | -8.75138 | -49.78483 | 2024-09-28 05:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| a4c2ddb7-a309-3b52-91d4-60d1657a0f96 | -8.74814 | -49.78635 | 2024-09-28 05:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ae7d1408-7685-3c04-b249-c9ad7cd85476 | -8.55723 | -49.60936 | 2024-09-28 05:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e4667b7-3656-3f5f-81f5-051c420c9fba | -8.55654 | -49.60738 | 2024-09-28 05:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74183924-ead7-3042-9200-b05b8e601104 | -8.55226 | -49.60862 | 2024-09-28 05:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bfe0b9f3-5a82-3a6e-912b-b426e85c88f3 | -8.55157 | -49.60665 | 2024-09-28 05:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d566861f-3aef-3fb7-946f-be251467adcd | -8.55077 | -49.61244 | 2024-09-28 05:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4aa0fcdb-b4f5-315c-8660-0147d4f17c54 | -8.24022 | -49.38614 | 2024-09-28 05:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b6f168a-dbcc-38c8-b738-07b82db980ca | -8.23982 | -49.38901 | 2024-09-28 05:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87a4cb55-0063-308f-b49e-75ebe7503b52 | -8.23517 | -49.3856 | 2024-09-28 05:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d270e19b-707f-3c2f-af5e-e0f440f8022d | -8.23479 | -49.38839 | 2024-09-28 05:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21a98d44-5e33-39ab-a429-9d1e1df1a075 | -8.23438 | -49.39136 | 2024-09-28 05:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a7ddf41-847c-38b3-ba9d-28a276c3bf7d | -8.22975 | -49.38777 | 2024-09-28 05:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce626a12-c9ad-3256-8894-2dc431b82544 | -8.12214 | -49.53654 | 2024-09-28 05:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae946b55-3c4d-3752-9f92-cc8c815359d8 | -8.10384 | -49.52255 | 2024-09-28 05:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 25937cc0-c535-371b-b3e2-6494a994340e | -8.10305 | -49.52823 | 2024-09-28 05:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e32a58b3-c7aa-3763-b314-e731f271a5f4 | -8.09887 | -49.52186 | 2024-09-28 05:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fd6d4575-b062-3ece-9069-4cf689c5b760 | -8.09809 | -49.5275 | 2024-09-28 05:08:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5d4f4506-24c5-3d3b-801b-64a488cea9b2 | -3.19434 | -50.44121 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 7df145bb-7001-3969-bb5f-729ea6a82e61 | -3.34813 | -49.78036 | 2024-09-28 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e8593d3-ea1e-3379-9ef9-8bfa48768cf6 | -3.33121 | -50.30748 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6c075685-f430-3dab-aab9-882d8d340c2e | -3.33058 | -50.3117 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e4d8bee0-3e88-3f40-b948-c5bcd81d5c80 | -3.32684 | -50.30679 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 02e1acc5-999e-3c99-be9a-5ad406ea7f25 | -3.32622 | -50.311 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8697a90c-1abc-3c9a-aadf-1e8a353312d5 | -3.32185 | -50.31024 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56f2d723-d5e4-31ee-8d53-56aaa9f68dcd | -3.32124 | -50.3144 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2439c3e3-2abc-30ee-83ac-6d4745dd9692 | -3.31748 | -50.30954 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff86e8fd-c00a-328c-96dc-aa220f1586c2 | -3.23652 | -50.01519 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 952b677f-9167-39ff-98e7-534b739e1d4e | -3.23533 | -50.01194 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ce9eb4d-e363-3835-a462-9c2062d93803 | -3.23469 | -50.01628 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77fa99a7-5229-3bee-a35c-1cd02a397450 | -3.23408 | -50.32414 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 780bce1b-408d-31f5-9612-1abb9926a77d | -3.22971 | -50.3235 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 877fcde3-23a8-3647-aea4-8f49a67fedd1 | -3.22534 | -50.32284 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34d07b19-7510-3c59-a1de-b618a443e18a | -3.19925 | -50.43797 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6517aad-766a-3d3c-a8c7-cae5e4da5449 | -3.19866 | -50.44192 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 51c6531c-d135-3ec2-a220-6ebf1d504af1 | -3.19806 | -50.44591 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e6c0ef8-eb56-3ded-89fc-a9d11636b0a5 | -3.19745 | -50.45 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c191799-669c-3ac8-8d24-66ad5574c2b4 | -3.19493 | -50.43723 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 237b0213-174d-32b1-bd74-1ace919b7fab | -3.19374 | -50.44522 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 76a29820-26db-3ee5-a230-fd440102f28b | -3.19313 | -50.44933 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 109bc086-7bea-3097-8fbe-a8ebce590b42 | -3.19002 | -50.44049 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 5e0e9cd0-d6a1-3cc4-9bc9-950df3442bd7 | -3.18942 | -50.4445 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4bddbf5b-fdbf-3e4b-b56c-8b7dedecd9b1 | -3.14077 | -50.28699 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1db8f72d-a0b2-3a8b-a623-b5dd2ca50373 | -3.13767 | -50.27792 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2aec6aa-a7b5-3cbc-94a5-413dd302fc67 | -3.13704 | -50.28214 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56a48993-c596-343b-bf69-146c3170eed8 | -3.13266 | -50.28148 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d1aaae0-547b-3154-861a-967b0885201a | -3.107 | -50.48108 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 58443460-1bb0-3a01-b332-0f9ac0f674bd | -3.10638 | -50.48519 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7778d2f-9ad3-3f2b-a085-a7004637b7df | -3.08914 | -50.48265 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 5f7a4077-1eac-3fe7-bcd6-58982823d504 | -3.08545 | -50.4779 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7a564f65-287a-3c8a-9bde-57a4741070f6 | -3.08483 | -50.48201 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| ed7cbdc6-e034-3e4f-9980-8020933d1d0d | -3.08422 | -50.48611 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 029a6fdd-6e9a-3650-b993-d00a81b23462 | -3.08113 | -50.47727 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0f7a9f8b-ab93-371a-a5fb-807e5ffd08fc | -3.08052 | -50.48138 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 2bffea8a-2fc7-3934-949d-dec904e0028b | -3.07991 | -50.48547 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1a4e8512-b7d6-3592-812e-d5df4c5f46a8 | -3.07682 | -50.47663 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8afd7ff4-d2dc-34f4-a4a6-1770c26f3c99 | -3.07621 | -50.48073 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| acca34cb-1296-3f6f-bd9e-1e20fb0953e7 | -3.0756 | -50.48481 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 77514dc8-65be-3b06-b3c7-791df00d7688 | -3.07251 | -50.47598 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63929e7f-a17e-3b82-b767-e074f9c4b198 | -3.0719 | -50.48007 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 91f3b123-1264-3189-985a-d40ccae811e0 | -3.0713 | -50.48415 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 3c326333-8d1a-3aec-805e-4de3ca39b72a | -3.05822 | -49.56001 | 2024-09-28 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 32404752-af55-34fc-bf02-62cbf4bb7dd6 | -3.05751 | -49.56464 | 2024-09-28 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a3b70454-a092-3fee-835c-3b82b4922d38 | -3.05364 | -49.55927 | 2024-09-28 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0b0e1e5f-6b2d-3b67-b115-4fdc15f15ea4 | -3.05293 | -49.56392 | 2024-09-28 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e8ede9db-6690-34fb-9481-9ef5bc0257c9 | -3.04524 | -49.49048 | 2024-09-28 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0069aa2-e5b9-39a7-b6f8-911522f1aeb1 | -2.52249 | -49.03153 | 2024-09-28 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cec2c84d-6ccd-3835-9469-f46d918fa385 | -2.52148 | -49.02948 | 2024-09-28 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 423c2a7c-0acd-3066-975d-2f26de439faa | -2.47727 | -49.15977 | 2024-09-28 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e043f935-b5be-3486-ba06-5fedce12dd71 | -2.95282 | -49.35621 | 2024-09-28 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9607c5db-5596-38c2-be3f-aa3c60310aa3 | -2.9521 | -49.36101 | 2024-09-28 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24d9515b-f481-3d1c-a06e-bd0fe36073a6 | -2.95137 | -49.36583 | 2024-09-28 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77058c5b-6339-36ba-9b4a-dc29c84bdb98 | -2.94744 | -49.36035 | 2024-09-28 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af92f18d-0a5a-379d-ad94-dffaee4fafe1 | -2.89674 | -50.4721 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 54d76971-9963-3643-a257-79bc24a8e67c | -2.89613 | -50.47612 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README71.md)
