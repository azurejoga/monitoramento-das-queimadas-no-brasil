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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24110ab6-dda5-3bdc-81a8-128515055d35 | -3.0645 | -50.50782 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a92befb-a5cf-322f-92f1-25faaa889607 | -3.05295 | -50.41866 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0817ffeb-50c5-35d4-8ca3-c3c70ce0f966 | -3.05141 | -50.41534 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c3739b3f-59d4-3610-874b-29f2d35ace38 | -3.04751 | -50.41368 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e56f5ceb-9187-3df5-a01f-2f20d571bb85 | -3.04625 | -50.42237 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 962530ee-497a-363a-96e4-eea03501926c | -3.04563 | -50.42663 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd4c8879-7de0-3dcb-a041-c88f5ca92b3d | -3.04537 | -50.41452 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7e28dd5c-3a5b-36cc-adc2-cb6d87819f3c | -3.0447 | -50.41891 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 774c0e01-5a64-3fd2-8b70-21fd27dfe1f6 | -3.0434 | -50.42747 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc330c4f-d568-34e5-a365-5ee7ca79da1a | -3.04148 | -50.41277 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b9b23abe-cb20-3f6d-ae4f-c4aa92588ba3 | -3.04084 | -50.41716 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 478ec8a8-bcac-3708-a27b-2af1a9556c78 | -3.03933 | -50.41365 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9b7be3f6-d684-323f-a119-843c5d72c5ec | -3.03867 | -50.41803 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1468e8f7-c917-3418-adcb-c02f85f05209 | -3.03801 | -50.42238 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ca713c94-a36c-3065-83d5-3694fd9cb2a4 | -3.03738 | -50.42651 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a7ce2e0-1191-3932-8ea2-da4e401a4f46 | -3.03416 | -50.42078 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 487ddd2c-22e5-3548-b25b-aa18a568f820 | -3.03354 | -50.42506 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4146a290-a3c5-3fa6-a486-2bc935b51a34 | -3.03195 | -50.42168 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ebe2ebfa-b569-37fd-9377-4764c82bbdd9 | -3.03131 | -50.42594 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c53aed34-5814-346d-b803-f2251ca561c1 | -3.02875 | -50.41552 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd12c2fb-574e-30c7-9434-625833fcbd32 | -3.02749 | -50.42429 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56f2b17f-fce7-3d11-931c-092c6dc07eaf | -3.02336 | -50.41019 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f04aef4-fb9b-3378-ae06-fba1f57cd0f9 | -3.02272 | -50.41467 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2b41d49-dcc8-3a78-8ee5-0aa16b8a96ba | -3.02121 | -50.41117 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c837a71-2667-34d8-a188-4b30a338a589 | -3.02054 | -50.41563 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a67999d9-9e3e-33c1-9d76-67254646ddd9 | -2.97986 | -50.48206 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d859e413-8a69-3dc7-85ab-4d6f9c75c7a5 | -2.97516 | -50.4724 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| af6a3193-93b4-3a61-8855-4c3d90bf5a44 | -2.97386 | -50.48116 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2ad00e72-7265-3eb6-842f-665b6236a08b | -2.95761 | -50.42469 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 702fad76-2461-3b9a-8dfe-8643ec9e19e2 | -2.91559 | -50.28153 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dadb3527-fac8-3bf0-b1b9-dd918168e8a4 | -2.91493 | -50.286 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c0f1440-e92b-3e92-b051-d9818cad08c1 | -2.91425 | -50.29049 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a0c9b5e-a17b-3c7c-9bef-1e08f83843a0 | -2.9136 | -50.29486 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54b28af2-e784-3178-92fc-630eacef2152 | -2.90884 | -50.28522 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd813c94-5492-3554-a082-9216757bb898 | -3.51393 | -50.4773 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bffeef1b-3ef9-3bd7-a612-9ef3886471e7 | -3.46561 | -50.33936 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ee976b5-7815-3cdd-93db-df6cba38aab1 | -3.45953 | -50.33834 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cff1ee9-2993-30d2-8182-a25c21faaa35 | -3.33136 | -49.92184 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b65f19de-cb15-3f64-abb2-b1d7dd344347 | -3.32668 | -49.92321 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83b8ae36-97f7-313d-902f-440673d4a118 | -3.32053 | -50.30052 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a7d61db2-d914-3aed-b634-1cdfff6c84bc | -3.31985 | -50.30512 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb089c15-8444-366b-9b93-f3cbff86b343 | -3.31447 | -50.2993 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c85bd769-6fa9-3db8-8913-a08bec4f234e | -3.31379 | -50.30397 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0f8726a5-4967-3f84-af29-9667dfbcdb96 | -3.18274 | -50.38529 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ac477322-6def-3d8b-a6c6-60b46f11a7d1 | -3.18207 | -50.38989 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7da59cdb-b05f-3c4d-9697-e31b2626613a | -3.18141 | -50.39441 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ab7e347c-59b1-3a00-8c20-d7b9e7ae8d07 | -3.17669 | -50.38436 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 15e3fda4-1389-3ed0-9f51-5ef2d4ba64af | -3.17602 | -50.38898 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 26154a91-4437-38ce-b8c8-252709e51497 | -3.17536 | -50.39351 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cf789b37-199d-3d3d-9665-c916940a6d51 | -3.1747 | -50.39801 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8c20b44f-b81c-3aef-98c0-1c86eda146bc | -3.16996 | -50.38806 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 87fe5298-ceca-30e8-9c45-a92dbade0c25 | -3.16526 | -50.58841 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d44dd81-08d0-36d4-a597-edac6e6116ca | -3.11865 | -50.35009 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f55a475-c40f-3193-a86b-5d136303ee5e | -3.11799 | -50.35458 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8428bdeb-133f-3d9e-aae1-84685436f60c | -3.06516 | -50.50338 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddc844f1-4e89-3c11-935c-14546b74fc2f | -3.05077 | -50.41953 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 36a167d7-b04e-3277-9f58-f56218d3e38f | -3.04688 | -50.41805 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 741c50c0-588e-3d18-8f3e-24b6f79ff175 | -3.04405 | -50.42323 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 284a07b9-b984-3990-93fa-8a75d386d650 | -3.04021 | -50.42155 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 31ec7878-8d9a-35dc-83dd-d874c9a9080d | -3.0396 | -50.42573 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb7cc430-6a41-3113-b728-b07b9eb91139 | -3.0294 | -50.41101 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 203d7eee-a4d8-372c-bf02-22debba5c535 | -3.0281 | -50.42007 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0612be17-990f-3245-9c37-a589da37628a | -3.02726 | -50.41196 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0e818370-c110-3a9e-8f17-8f84d1a649e2 | -3.02658 | -50.41647 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8fac221-1c86-3137-968e-68bda0905a9f | -3.00977 | -50.4872 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72a5505c-1e65-33d5-be34-c780e6b42c2e | -2.98054 | -50.47749 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 563b9126-b118-3eeb-a27c-5f6063a3af49 | -2.97451 | -50.47676 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e04e3499-ad3d-33a2-b3ec-fedaed3ed81c | -2.95695 | -50.42918 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d1d007c-5ce8-3ec6-8d72-0a35ae8c6336 | -2.92235 | -50.27787 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a11a9363-6232-34d7-9dcc-9a19ee91cf3e | -4.10265 | -50.52668 | 2024-10-29 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0dd1eca7-faf4-3ef3-b258-32b0592528eb | -4.10199 | -50.53131 | 2024-10-29 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb9818be-2733-3e35-aba9-d25457b66d30 | -4.10131 | -50.52776 | 2024-10-29 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 619b5ba2-903f-3af1-a4cd-a3369b7ccf4c | -4.10063 | -50.53233 | 2024-10-29 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| badbb51b-1364-3078-882a-59c4b523cc82 | -4.09716 | -49.99358 | 2024-10-29 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 05301a8f-9d5d-3c1f-bba3-0054fd89e4b3 | -4.09529 | -50.53481 | 2024-10-29 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57dc1610-6361-3e89-bc73-74a716ad9f68 | -4.06851 | -50.03328 | 2024-10-29 05:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c12f74da-146d-3016-bd07-64994dcacd0d | -4.06639 | -50.02975 | 2024-10-29 05:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03b36605-65b5-37ea-a42d-001fce932a6f | -4.06568 | -50.03475 | 2024-10-29 05:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7c63e59-a663-3faa-9fcc-5abbe4ce18e9 | -4.0622 | -50.03268 | 2024-10-29 05:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 192539a7-8f42-3be6-9a7d-78274312a0dd | -3.93685 | -49.96872 | 2024-10-29 05:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d034b0a7-2daf-354d-8499-0b2666491753 | -3.672 | -50.29532 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af2de5c8-f88f-32eb-b653-8d8d55a198ff | -3.66626 | -50.11964 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7071d47f-8a12-358f-90eb-f6bdb0eb38c7 | -3.66554 | -50.12458 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86f80984-ecbb-365d-8919-eca7828dc828 | -4.0966 | -50.52558 | 2024-10-29 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 506a86ef-fc11-3796-a70a-e82170e23f91 | -4.09595 | -50.53016 | 2024-10-29 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c92c54b-0a95-3d89-8ea2-b6abb4367122 | -3.88808 | -50.05749 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 15d674d0-344b-36f1-8b9d-710a09440c8d | -3.87654 | -49.95981 | 2024-10-29 05:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3fe9a675-afaf-3fd0-8254-3572eea9cc13 | -3.6713 | -50.30008 | 2024-10-29 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23d44066-f702-3106-805f-961522091b1b | 2.36033 | -50.77632 | 2024-10-29 05:25:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0804f7b-ef8a-35ad-a235-763a585deda0 | 2.35977 | -50.77285 | 2024-10-29 05:25:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12b166b0-d125-3c71-8ba0-ffb7c278a2f1 | -2.19201 | -50.5928 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ee35d863-7a43-39f8-b9d5-d1bd19655a0d | -2.08458 | -51.42301 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 92e406c8-1c01-3c9e-846c-c7f67397403b | -2.079 | -51.42226 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da85bfb4-e547-392d-82f8-1d8c8b9cda04 | -2.1979 | -50.5937 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 62613854-fd50-3d6f-966c-656473d16d5a | -2.19138 | -50.59701 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 58d52dd5-ee09-321a-a402-ff8bb906c1a3 | -2.15144 | -51.43303 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b12acecc-9955-32f0-aefa-2bd87da77062 | -3.27369 | -50.70159 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f8c988a-81c3-3329-9f72-e7d60130c5e7 | -3.25568 | -50.65879 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| daa39e85-67be-37bb-a30a-7e591a524f87 | -3.25164 | -50.64474 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96737f60-315d-3095-8825-7fd9a5dd5cb9 | -3.25099 | -50.64918 | 2024-10-29 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README100.md)
