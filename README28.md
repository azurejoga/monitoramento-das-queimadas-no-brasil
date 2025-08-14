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
| 5e9e01f6-5eb2-38c1-86ea-f5d528f41e4d | -7.07487 | -59.19917 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b796c53e-833c-3794-a210-f6063d2dee26 | -7.23636 | -59.99892 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49237b6c-1464-3aed-a1ba-e2246c91bff1 | -6.90123 | -59.14242 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ed3a479d-f121-390a-845b-0d559c82a9c6 | -7.31981 | -60.62084 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9b0fbcd-896c-366e-941f-897bdaa39988 | -6.94042 | -59.63657 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f84eb657-2c5f-38f2-8b05-45559da36126 | -7.33051 | -60.62262 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b45cfcc9-e2f4-3a4d-8fc5-874f0ae44b08 | -7.87417 | -61.81683 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d064303b-9819-38b1-b333-d8f8992069e1 | -6.08619 | -59.93898 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a3160ae-d797-3781-8a49-590a97960820 | -6.09196 | -59.93137 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 524e8ff5-e476-37f3-b10c-8813fc2d6f2f | -8.10671 | -61.19003 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3fe06444-3412-3bfc-838d-6f294b38382a | -6.9024 | -59.13516 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cf986ae-cad2-3458-b48d-8ff86e1a51fc | -6.92094 | -59.14931 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 32118deb-a484-34c2-8c1a-087e099f7847 | -7.72264 | -55.20546 | 2025-08-14 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5214c3f9-4535-342d-9eea-3bbcbc33785c | -6.56331 | -60.06089 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1eda0639-8d22-3ee4-a53e-0fd7a77459f6 | -5.76045 | -59.89299 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37573893-271c-3ea4-a6d6-e61076b45134 | -6.53369 | -56.20334 | 2025-08-14 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da0e2124-c0a2-3a78-a91d-17b50ebe2185 | -7.33407 | -60.62321 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53d6ae5e-4263-3689-a53c-a1f61833420c | -6.91476 | -59.14459 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ee8c72b-64e3-3d90-bf75-abf5da71bcc9 | -7.60546 | -63.52094 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1f549ed4-952a-3be7-a15d-839919ae24a9 | -7.07369 | -59.20645 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09d3962f-6d2b-3ed9-9d6f-f8a6f5ca98ad | -5.75531 | -59.88012 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e51c540d-da88-3d33-bf50-f591138a9d22 | -7.55963 | -63.48465 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da01bdea-baae-3163-ba20-7c6d8da43b6c | -7.12314 | -59.63405 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ed9a596c-e57c-3b69-bb5f-52d18a83cd0c | -9.1584 | -59.67215 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e915b955-c746-31d0-9f18-8c143405fae2 | -6.88094 | -59.13913 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7aa6157f-8e33-3e15-8184-b9115c17c4ac | -5.81141 | -59.22194 | 2025-08-14 05:10:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f56476b6-6623-35ef-922e-cf402803795f | -7.26068 | -60.00285 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2375549-5ee8-38fe-aec1-8dc4cf899b9c | -7.86962 | -61.8208 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e335ada-8031-3221-9f12-a15bd86d634e | -7.12596 | -59.63836 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8885f66-da6e-3341-b0aa-192f145637a7 | -9.19705 | -59.65533 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c4b362f-da82-392a-a572-3440d53571b3 | -6.88653 | -59.8807 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcdfdfda-81e4-3303-899a-76ab837fa4be | -6.77355 | -59.47583 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42a6ee5a-cf0d-319b-ae33-1c8d47b8fbc8 | -9.19686 | -59.67783 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38cd1815-2ba3-302c-ae70-22bb59fafa15 | -7.88249 | -61.81351 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1483346a-ac5c-36ed-b3a0-056e0c09503b | -5.73776 | -59.87737 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faf1e555-2be3-36c8-b8ce-7bcae0a12e61 | -6.08874 | -59.95094 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2124cb5-47f9-354c-afb9-34905ee88381 | -9.16178 | -59.6727 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c6c2a5b-f0d5-3e11-8a95-0262bd16a466 | -5.7518 | -59.87956 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0781dc6c-5830-31ee-8d40-1461a91a88f4 | -9.3147 | -63.53484 | 2025-08-14 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 807b5b35-5187-3486-b0ea-d67eeb691453 | -9.15152 | -59.4142 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c420c35-ca4b-3e59-ad51-7dc0756d7f4e | -6.08494 | -59.94679 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 85dac6a5-de81-30f6-b7bd-d8e3fb2f6f71 | -7.26477 | -59.99955 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccae2e6c-6bb8-387f-ac69-a7371e22ebbf | -9.19645 | -59.65899 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc3f1ae8-b82d-3017-8511-1565c42a2a22 | -6.88479 | -59.63585 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c307abc5-b7d6-319b-a066-6103a70040ff | -9.14487 | -59.66991 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46a39c29-6fe9-3846-a8de-29886d35dfda | -9.18293 | -59.65676 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3c53fc16-5f33-31a6-83c7-9ddc448b223d | -6.89212 | -59.15583 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 622029b9-1033-31f0-8406-0ceae3f9eae3 | -7.87195 | -61.80702 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e855e22-0f8f-33b2-ab15-7028ece82757 | -6.66113 | -59.08905 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aea27159-983b-3f90-839b-f7b3d9c145f5 | -6.91313 | -59.13316 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8832da02-6950-35ec-836c-9069c8fb9ac1 | -8.92208 | -60.7303 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49daad3c-a5ca-3dad-91ab-991b484c1702 | -6.90799 | -59.14351 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 233b286a-bd86-3959-9d4f-a231042147f5 | -9.34311 | -60.32955 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f7e62be-ab7a-30e1-a1cb-d7077a586e26 | -6.89388 | -59.14496 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9f071689-4341-31df-9680-2e1723d72aff | -9.15398 | -59.6564 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1957ba89-1853-39d8-beb1-c866bacaf056 | -7.26037 | -60.63289 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 292c029b-d6cd-3546-a75a-d932c85bf2b6 | -7.13562 | -59.64382 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e94ed79c-ae03-3b9f-93b8-824d1df37198 | -6.07156 | -59.94049 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9312cc7-4fc4-3e7d-af9b-64f92eab252f | -6.878 | -59.15727 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 289f0f70-5890-39ea-b823-02a24316982b | -7.86817 | -61.80639 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13214788-f2ee-3b4e-8bb3-c31c240c78de | -5.74578 | -59.89467 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b4b2b63-7fb8-3478-aa5a-685df3f3b0fd | -7.09435 | -60.02747 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79ed8dc9-7c06-31aa-9d90-bd596192f6f8 | -7.88172 | -61.8181 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73adca24-0805-3e59-8238-a5a157c77264 | -9.1506 | -59.65584 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a1c87be-62a4-3087-900e-7c3b232ae678 | -9.50016 | -60.5244 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7951c5ad-f372-3464-a0e7-6ce8c332a489 | -9.06281 | -60.64668 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c87d9a31-5722-3cdb-87e4-d70923254ca1 | -7.46436 | -59.88984 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4ec547f-e061-3f60-9d6d-0a59d411242c | -9.20777 | -59.6534 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db36b4af-282c-384a-9835-f10986bd4a89 | -6.90519 | -59.13934 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0215c2a8-faa1-3d68-8564-1c373cf2c3f2 | -6.11204 | -59.9185 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1768f77-b6d7-3003-8c74-097bbc5aecc2 | -7.07707 | -59.207 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad7829a1-1d2b-3b13-b677-416ad9c2f605 | -5.80979 | -59.21025 | 2025-08-14 05:10:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f05510f-52e5-3411-9663-74c39fb1c9df | -9.18274 | -59.67924 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f9c0388-3ca1-3354-9507-f6ff4852c481 | -6.88947 | -59.12934 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbcc4f40-7cca-369a-be03-78a3430ac36a | -9.50172 | -60.53662 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4310807c-c32a-3d4a-825a-bc18970f33c2 | -7.76282 | -61.57334 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2984f50a-4b3e-34e3-9d48-af496fa79ae3 | -10.00786 | -59.22275 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9d00752-ab15-37d2-a89e-696444d6454b | -7.14126 | -59.65247 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d260613f-8fa2-3401-a119-485d846b469b | -6.65746 | -58.82225 | 2025-08-14 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fec836c1-090f-3a26-973c-b9d62781d2bc | -6.06806 | -59.93991 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76272311-6857-319b-b5ef-0e2d806386ff | -6.91358 | -59.15187 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9b338dac-f8cc-3700-af21-fbcbd26e48b6 | -5.74253 | -59.87009 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12333a6c-a3ba-33c0-9df3-b381877c6dac | -7.45213 | -57.64789 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 213e4c0c-cd88-31ee-8a48-b153856d7faa | -6.88653 | -59.14749 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c15929d1-0c68-32e3-8d9d-7ec25c1446ad | -9.14148 | -59.66936 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac5d7828-4167-34eb-a516-ae0d488aff84 | -6.10375 | -59.92521 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4eead689-7c0c-377c-93f6-14573173288b | -6.88244 | -59.88396 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 561fe8a5-2df8-36c9-8b02-ce72d676f5fc | -7.12661 | -59.41778 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 629db1d1-d7b7-32ab-ac8e-d799e71eec31 | -6.88991 | -59.14804 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ffbd5e6e-3ff5-38dc-acd1-c6953388cfe4 | -6.77415 | -59.4721 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5311f13c-cc64-366b-848f-dd531d337ae9 | -9.15516 | -59.6491 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab093a03-dfcd-336a-83e0-b70fa6e01390 | -10.05066 | -59.36118 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a6b9830-74c9-36d8-b7dd-2527bb2fce4d | -6.79277 | -58.78554 | 2025-08-14 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 339b2460-d39f-3c5e-b977-8c0fc7342a50 | -9.15178 | -59.64854 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e820f4b-7f0f-3cf9-8b28-5ae40f5cbbca | -9.19129 | -59.66939 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9215c51-4169-3a03-a7c3-5235f7586b60 | -7.12721 | -59.41408 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bdfe5c1-c657-3e41-bc88-306678361287 | -6.90962 | -59.15496 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e593409c-ff1e-30ea-946b-2ec813bd33a4 | -7.12094 | -59.62601 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 39812436-f8ef-31ad-9b4a-967461ab9181 | -7.12032 | -59.62976 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7ff7e556-2d27-3156-b520-e8532fd1151a | -9.49953 | -60.52827 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |


[Clique aqui para ver as próximas entradas](README29.md)
