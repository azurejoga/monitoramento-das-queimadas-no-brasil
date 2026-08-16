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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7de13dcd-1063-3da2-9100-37d0ded86e93 | -8.89942 | -60.60546 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b119859-f53d-308c-851c-6725622c0787 | -8.97612 | -60.52244 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fb4c1815-eeea-387f-8d04-ff98579e00b2 | -8.89602 | -60.55754 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| bce623b7-ebe2-3e74-9991-6df05d837bab | -8.96747 | -60.50919 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cce00291-02e6-31fa-ba59-7b86182e02da | -9.13745 | -68.19913 | 2026-08-16 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c32bf97c-b9a7-33e6-8e2d-8a86a7b8cf32 | -6.84658 | -58.97395 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f071ba05-dd31-3f2f-a1af-3ea9fabfad0d | -6.615 | -58.999 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 543c6544-bdf6-3669-bdcf-d89dd6cb5d33 | -7.4207 | -60.03032 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ba4cc69-83a7-3db0-b2d0-768a78234803 | -7.4196 | -60.01426 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e381ca9d-4977-38a8-8943-09d2152a7735 | -7.42577 | -60.02625 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b13a8d7-5e01-3498-a056-d951839ac526 | -8.95176 | -60.51868 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 76951bbe-c62e-3e48-860a-52f337243713 | -7.58177 | -60.88823 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3d59d54b-068f-3a6e-98c4-c1ce8c911452 | -7.55744 | -61.17835 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d46ae0b1-1165-3795-b9e4-30019ad320d0 | -10.07627 | -60.49599 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0af53b0-2b72-3456-bc46-bb95c5e61218 | -9.20697 | -59.67498 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8a09b71-8091-37ee-a070-88b9f3882467 | -6.63225 | -59.05801 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4c2904dd-64b5-31d7-a5c6-803673526070 | -11.32609 | -61.26516 | 2026-08-16 05:36:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b54b1a80-e2af-300b-bfb7-0b90a037dff0 | -6.63462 | -59.06701 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ab32398-177f-3773-9650-08e1aad8ed18 | -9.29712 | -56.82056 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b18c2f4-51ee-3995-b222-040d96c795a5 | -9.30265 | -56.81295 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2c7e2728-bcba-348c-8cd2-0c87150c569f | -8.97261 | -60.53332 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9fcaf7ef-8fae-3cd6-8588-a41d34dcb3c7 | -6.70684 | -58.96035 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dab5ba63-65ea-36c6-a257-300c314d53c7 | -7.42519 | -60.03013 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97e741aa-9dd8-3951-98b1-b3e4ae95d13f | -6.8606 | -58.98046 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0b1d305f-2655-3739-830b-fd332d7a606d | -8.65478 | -54.72353 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71d51a8a-ecaf-3ff1-a54f-f2ee57d20f66 | -6.60914 | -58.98697 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2db25ba2-97b7-35c1-bac5-e78ab89a2a08 | -7.78798 | -56.29419 | 2026-08-16 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de6e2b49-b682-38a8-9257-85b7f863ebcb | -7.49688 | -60.07687 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d2fbf0d4-953a-3c3b-bbec-d62b0026c10a | -6.72587 | -58.93063 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 398c5df4-bc9d-39f8-a8f1-32a5286b04bc | -6.85649 | -58.95782 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fae046f-8968-37d4-8820-5f7169ac3150 | -6.62117 | -59.08227 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fae3dce7-b2ce-310e-aedd-59f34e7c6f49 | -8.90289 | -60.60599 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4f0ade7-9569-39a5-8a39-6057c628601c | -8.95465 | -60.52309 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e4d923e1-9a5b-3992-bf76-2258b9f15092 | -6.83495 | -58.97655 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 80cab629-1296-3ab0-a524-ade8ee56c1e9 | -8.89832 | -60.56581 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d31c487-d5d5-3c9d-b189-77da39dc6781 | -7.60064 | -70.35564 | 2026-08-16 05:36:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8528cd0e-93a2-3dbd-9af1-970e3194045f | -8.97609 | -60.53386 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 721c85c4-817e-3efd-a8a2-81f262eb97f2 | -6.62323 | -59.0437 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e69370e-61c7-3735-b347-7c34b35bf97b | -8.97434 | -60.52172 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9f2712b2-dc85-34da-abb5-33c9eb6a2fee | -11.20691 | -54.80984 | 2026-08-16 05:36:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0d68954-c3cf-3473-8f36-608f7e085e2c | -6.60717 | -58.99973 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b3108bf-b8e9-3a97-8c17-6e9b7003a01f | -8.96458 | -60.50476 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0d2969b-dc26-3fa4-b5da-8a5044ccffd7 | -9.29937 | -56.81564 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32b4c79b-89a6-39ba-8767-23ee658495ca | -7.41853 | -59.99798 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97ecd484-5247-3a7a-8dd1-c16b972e71dc | -8.97782 | -60.52225 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e8962337-34d8-3fc1-948a-2918f7bb319a | -7.83648 | -61.34683 | 2026-08-16 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bc17bee-748b-35ee-9396-40e12b9fc1ec | -8.81163 | -66.76405 | 2026-08-16 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b30cb3a-8957-3918-9735-d109406a2120 | -9.46692 | -60.53372 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9bd3db8-7f16-3905-b41a-aef1278524da | -6.8552 | -58.96645 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2e314a8c-5d13-33a6-865a-b4f8e1f32e19 | -8.9425 | -60.50932 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36e63031-1867-3cc4-804c-a94b8b736bde | -9.08965 | -61.40186 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea54f5a3-598e-3a3c-bc6c-1b3ae2f70106 | -9.0857 | -61.40498 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ab76cd5-499e-35cd-86f5-e75a5ec5e93f | -8.89771 | -60.59334 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60d696de-c282-3d7f-8248-5d3c25579ebc | -9.13683 | -68.20279 | 2026-08-16 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0473d401-ab4a-3596-806e-e5ac0b0e2a26 | -8.43046 | -62.67049 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcb548a9-3713-3eae-bc60-ea7b48b7f107 | -6.86145 | -58.94972 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55ea28d0-d253-3b26-830b-acd558f2034a | -9.47748 | -60.51125 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43f65180-1e6e-359e-9c4c-64d8abfd60e8 | -8.95153 | -60.58979 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84532cbc-fb5b-3aa6-9c8f-808e8e21eb70 | -6.59754 | -58.98952 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79121e5c-b598-30c3-9bc6-9efa1da51776 | -7.426 | -60.01922 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4a8bf51-56d1-301f-9b93-5118f008aaac | -6.62798 | -59.06166 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 47a990b0-a37f-39df-bf22-e2a15c39e2fb | -8.97672 | -60.51857 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3c3f9847-240e-31ac-81ec-884f225d92c6 | -7.4202 | -60.01034 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e510c74-d0fe-369f-b511-f6fc4e4dc23e | -8.95524 | -60.51922 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f1e21138-5fc8-310f-9f6f-82fc0fc36f87 | -9.42587 | -60.32587 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bbf9bc4-1d79-348f-ae91-1976ca11708a | -8.90118 | -60.59388 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e8678ac-29ae-3c04-bfdb-a03e5713d9e0 | -8.98421 | -60.52719 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d4df5507-0b48-3d2c-a887-313962e5d40f | -6.62497 | -59.05692 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bff95b69-6416-39dc-b863-e43e49efac96 | -8.6151 | -54.67593 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6df7903-2d89-3889-8b21-a1153f948f70 | -6.97877 | -59.01411 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c878f08f-f839-3f83-aa2c-57c1f0bd5e88 | -9.29994 | -56.81144 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc0e9eba-0dda-39ef-9fb5-97403f4946c8 | -7.58234 | -60.88457 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29102d91-4228-305c-9dd4-7cececb666c5 | -6.70213 | -58.94214 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0268184-eff5-3f07-bd32-fb8055a60c4f | -8.60774 | -54.69226 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16747c96-6798-3f62-9703-73064ff83637 | -9.29894 | -56.80794 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c00c64c-329f-3b56-beb1-777b9ffb506d | -6.63162 | -59.06223 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3dd242c2-09a6-3316-9568-70afb13eb7e0 | -6.61453 | -58.97708 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e4064601-de49-3f5e-b753-04465ddb9c22 | -9.47629 | -60.51912 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b439c56-0427-33c9-9ec5-3fca35ca6dec | -6.70882 | -58.94744 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f6e9ce4e-2666-3b7e-bb26-4deac4987d2d | -7.55519 | -61.17064 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18d8cc75-7945-32a3-9d62-b913797d171c | -8.96449 | -60.52858 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 50f687a9-728c-37bc-825c-b9de794dec3c | -9.34819 | -62.36237 | 2026-08-16 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c60b0621-d6f7-338d-b925-2acbf45135bb | -7.58516 | -60.88877 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2569c2fa-bc24-30c2-9bef-db820d6f045a | -8.54021 | -54.59092 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e8d44fb-ceed-3150-9fdc-c37503835d47 | -8.89888 | -60.58563 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5f7e7275-1e01-3487-846a-539c4c7d8951 | -6.84292 | -58.97338 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 359484ac-1f98-3f5c-8a8a-8e7193954180 | -6.62244 | -59.07381 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b6b7d17b-c2a4-3733-b160-d5e762dec726 | -8.9628 | -60.51641 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4d1cedcd-78d9-365e-812d-d6c27ea1fed4 | -6.71748 | -58.93987 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e8883d0e-284a-3342-8875-ceaf4f5e3f33 | -8.97725 | -60.52612 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ffef9d39-116c-3317-a39d-49faa3b9fb91 | -8.89138 | -60.56472 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d6e2366-0d6f-36a4-b45d-f1232c57c4a7 | -8.94821 | -60.54187 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5ecb511-c35c-3a25-a9e7-eb9784ea1a6b | -6.61135 | -58.99845 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f465f9e-ae8e-3b91-b132-3f665b400feb | -8.6425 | -54.69752 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 036d478a-6488-30f3-8b09-67d52fe7fdea | -6.72284 | -58.92576 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a7cf5f4-808f-318f-8639-4e7bb7533db0 | -8.98247 | -60.51503 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6192dc3-dd82-3cef-b740-0104ea157e0b | -6.60279 | -59.00582 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f4397f4-baf5-323f-8d3d-60a5b480a5b4 | -8.26406 | -57.34809 | 2026-08-16 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 937c755e-16e2-32ea-87c0-72d7e54cd246 | -6.70948 | -58.94312 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 70a65796-26f8-3b00-b100-bf4f88d30f6a | -8.98073 | -60.52665 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README51.md)
