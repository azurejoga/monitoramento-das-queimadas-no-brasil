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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbab10d5-aaed-3abc-91c7-5507c14d8e34 | -8.2719 | -48.1893 | 2026-06-29 10:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 223.1 |
| de1f0183-ed5c-35e5-849e-a8482d7304d8 | -8.2907 | -48.1876 | 2026-06-29 10:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 2b837463-053c-399e-9cd0-746c53b758cd | -8.2905 | -48.2094 | 2026-06-29 10:40:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| ef9640f2-a930-3174-8d93-afc5b0d156da | -8.2907 | -48.1876 | 2026-06-29 10:40:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 296.5 |
| c7f39c5b-e326-3ccd-980a-4d4070b2e9b1 | -8.2719 | -48.1893 | 2026-06-29 10:40:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 4cb2daf1-626e-362d-b8d0-a7b9de115be6 | -8.2719 | -48.1893 | 2026-06-29 10:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 230.7 |
| 0b6faee5-c952-38e0-ae68-777d976e11f2 | -8.2907 | -48.1876 | 2026-06-29 10:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 224.2 |
| 3f73691e-c1a3-3966-9302-40932a160048 | -8.2907 | -48.1876 | 2026-06-29 11:00:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 233.7 |
| 89ae90de-4d67-33fc-9fb3-359cdbeedf09 | -8.2907 | -48.1876 | 2026-06-29 11:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 156.9 |
| e5498455-a114-3418-b4ff-0ec84a333b55 | -11.9533 | -58.6192 | 2026-06-29 11:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 4b5ffa6d-70c5-310b-a1cb-fe76b428fd27 | -8.2907 | -48.1876 | 2026-06-29 11:20:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 4dc05a14-8fd8-3186-85cf-30e6d21293f6 | -11.9533 | -58.6192 | 2026-06-29 11:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 80a592bb-8a14-3f8b-941b-1a91afbf038a | -9.0684 | -44.7765 | 2026-06-29 11:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| f2cda3d7-ce40-3595-b5fe-5acbfdf28a1e | -8.2907 | -48.1876 | 2026-06-29 11:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 6bef7815-bf24-3f28-9837-08d3a9168b05 | -12.4651 | -58.5009 | 2026-06-29 11:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| fdd772b1-255f-3a2a-96ab-d8ca211eb97a | -12.4462 | -58.5023 | 2026-06-29 11:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 4a5bcd7e-cfc3-3712-8bdd-309e021f633a | -9.0684 | -44.7765 | 2026-06-29 11:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 124d79bd-d535-3aca-b1af-7aeb1f94ce66 | -12.4464 | -58.4825 | 2026-06-29 11:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 733c1bb7-0f81-3713-84c5-124fd157fc55 | -12.4654 | -58.481 | 2026-06-29 11:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 4ec38485-8de4-347a-b01b-972bd7a5976d | -11.9533 | -58.6192 | 2026-06-29 11:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 0112c5fa-2cf2-326e-98e2-38b0827d466e | -12.4462 | -58.5023 | 2026-06-29 11:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 0fb9c5a4-332f-3548-bc9f-b4bb3598b5fb | -12.4651 | -58.5009 | 2026-06-29 11:40:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 17a04af2-1dca-3933-9ded-82deca96eb08 | -8.2907 | -48.1876 | 2026-06-29 11:40:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 2524638c-ea79-3d90-92f9-ea272bc8f059 | -9.0684 | -44.7765 | 2026-06-29 11:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 7cad4c2b-5817-3f80-bdee-0c665da0a249 | -12.4654 | -58.481 | 2026-06-29 11:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| eb45ba3f-2424-30c3-a10b-abc4910930fa | -12.4462 | -58.5023 | 2026-06-29 11:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 239.8 |
| ec8f8d14-c48c-359a-a5f6-42593beab6e5 | -12.4464 | -58.4825 | 2026-06-29 11:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 114.1 |
| ba81977f-c26a-3953-87e7-08ecdd65ae51 | -12.4651 | -58.5009 | 2026-06-29 11:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 641c60be-1fe7-3dde-b910-b90ad6c60f08 | -8.2907 | -48.1876 | 2026-06-29 11:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 3e58bdeb-10cc-336e-bd50-328d8a5e786f | -12.4651 | -58.5009 | 2026-06-29 12:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 3e548665-c28e-38b9-a27e-013fef6a56c0 | -12.4462 | -58.5023 | 2026-06-29 12:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 303.9 |
| 8d54229b-45f6-30db-8c1b-51bcc3ff66e2 | -12.4464 | -58.4825 | 2026-06-29 12:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 01a619c6-9e9b-38b7-ac65-89eaa71ee851 | -9.0684 | -44.7765 | 2026-06-29 12:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 5a684429-650a-35d6-a80f-8cf5005fffea | -8.2907 | -48.1876 | 2026-06-29 12:00:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 324bd45f-bb50-37d0-a511-36da27583cf3 | -9.07864 | -44.75322 | 2026-06-29 12:06:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 2f0f5f04-9493-359f-94ff-b469c9e3ee87 | -8.93933 | -45.64799 | 2026-06-29 12:06:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 6365d634-0488-3184-9071-d77270479302 | -6.15473 | -45.63825 | 2026-06-29 12:06:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 79b0fc7b-c0f6-3dfb-8863-015c7ae53d65 | -6.93 | -47.86848 | 2026-06-29 12:06:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| a674f7a6-ecd9-3928-a6fb-d3d0fe291571 | -9.07467 | -44.78001 | 2026-06-29 12:06:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 07040cac-4314-3ad5-a998-0ea2fe220c45 | -8.27777 | -48.18451 | 2026-06-29 12:06:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| dfc9feab-1177-320f-810a-47d2ea76d5e2 | -9.25989 | -49.26008 | 2026-06-29 12:06:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 397ef15d-ed63-3de1-99ab-b36b4e5c3361 | -9.0771 | -44.7597 | 2026-06-29 12:06:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| c200ea61-26c8-3dc5-a801-1e134f8797db | -8.984 | -45.72968 | 2026-06-29 12:06:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| a918763a-2a50-3a6c-ba53-2e2c8de1c322 | -8.27914 | -48.19131 | 2026-06-29 12:06:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| c3e7af5f-64d4-3102-965c-15a26ee51018 | -6.93154 | -47.85734 | 2026-06-29 12:06:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| bb0d24a4-d3cd-3532-9cda-90519dfb37dd | -8.27624 | -48.19557 | 2026-06-29 12:06:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e4308090-0580-3fc6-80c2-1b7e7d2510d2 | -9.06311 | -44.77219 | 2026-06-29 12:06:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 49.7 |
| a22fed16-8589-37bd-a3ef-c3a8b9fe3c00 | -8.02387 | -46.2571 | 2026-06-29 12:06:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 751b836d-b2d4-3911-b2ac-12041966ec54 | -8.93713 | -45.66522 | 2026-06-29 12:06:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 07783656-5eb6-35f4-b1df-1148ce5a4dd0 | -5.80039 | -45.11812 | 2026-06-29 12:06:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| a2de1326-bdb0-307d-8726-2c3caa4c8bf7 | -9.07606 | -44.77352 | 2026-06-29 12:06:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 1c409b41-0d0c-3363-8d48-b80ee5773342 | -8.99593 | -45.73118 | 2026-06-29 12:06:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2dba439b-0ce6-309c-bda0-579963a92c7f | -8.28061 | -48.18019 | 2026-06-29 12:06:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| ed8e8e27-ba65-30d3-93e9-17f8e69dd325 | -8.28893 | -48.19254 | 2026-06-29 12:06:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 3e0bad3c-bb27-30b0-9114-d701af0a8d4d | -6.89988 | -47.94234 | 2026-06-29 12:06:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d8d0ba88-aa2a-3d87-b690-7315b0aab59f | -8.2904 | -48.18147 | 2026-06-29 12:06:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 8843957c-9fa8-3eb7-8afa-cab52ba6aa6e | -12.64905 | -51.41641 | 2026-06-29 12:08:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 52ee6e78-23ac-39eb-b6c6-d1913df8eab4 | -11.77866 | -47.56844 | 2026-06-29 12:08:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6e33cec9-9ecd-36f8-8184-244c65d7ada1 | -12.45645 | -44.7016 | 2026-06-29 12:08:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| ebe51b99-0018-3400-bc80-3cd234d54667 | -12.51346 | -48.29095 | 2026-06-29 12:08:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fe59d7c4-445d-372a-afe6-0c050cffe168 | -10.9785 | -49.55912 | 2026-06-29 12:08:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 56c9b4bf-49d1-36c1-a642-bd885df1099a | -11.8939 | -57.13262 | 2026-06-29 12:08:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 9165a7c8-22d4-3200-8034-cb6599896605 | -14.54904 | -53.66167 | 2026-06-29 12:08:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| df0ac7dc-c580-30e8-bf58-a5b9493ed4b2 | -11.31152 | -53.94749 | 2026-06-29 12:08:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 793bf687-ea82-324d-a0b2-a13781a3306f | -12.52378 | -48.29228 | 2026-06-29 12:08:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 21fd1029-be40-329c-9b99-b0f389009e1a | -10.31452 | -50.17203 | 2026-06-29 12:08:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 334f586e-0003-388e-9d89-9033b99d8608 | -10.31323 | -50.1814 | 2026-06-29 12:08:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6f67ef56-3e13-3f60-a50e-d64826409159 | -14.19679 | -57.45072 | 2026-06-29 12:08:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 4f7912d3-0ee6-3238-a010-e2c84ea1c15f | -13.94422 | -53.93867 | 2026-06-29 12:08:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| c78b88bc-b41d-39c6-bb90-0786f9da9da5 | -12.45935 | -58.50317 | 2026-06-29 12:08:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 917bef54-0354-34a8-b6fd-02769ddfc6b5 | -11.21686 | -53.83509 | 2026-06-29 12:08:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3ac3aaca-bd13-330a-bcae-82a40b4711f8 | -12.45959 | -58.4964 | 2026-06-29 12:08:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 4d5754f5-7825-33cd-bcdd-51d58cdf0346 | -13.71124 | -47.86297 | 2026-06-29 12:08:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 08e99c63-e954-3670-ad66-fc89f31e524d | -11.04962 | -55.74683 | 2026-06-29 12:08:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 56e96dbe-4f95-30e0-98e5-4443b9d5deca | -11.52414 | -56.11813 | 2026-06-29 12:08:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 60d67bad-f0f8-3f9e-b9f4-4bdaae54031b | -12.44692 | -58.49424 | 2026-06-29 12:08:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 412.9 |
| 940a5c96-c6b2-3142-ac29-2235dd2b91dc | -11.91692 | -57.41021 | 2026-06-29 12:08:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| dad1dcaa-9226-3e18-b783-37a2186549ff | -14.19814 | -57.44131 | 2026-06-29 12:08:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 09e2bb1a-2912-359c-ad2e-be0f3d7e9aba | -14.53411 | -47.03445 | 2026-06-29 12:08:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 22.8 |
| d610ace1-dd2c-3f91-b368-86b6f37cd0e6 | -15.04604 | -53.03749 | 2026-06-29 12:08:00 | TERRA_M-T | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ea7dc351-5e59-3cd9-a948-0a2afc00d6f4 | -10.80499 | -48.56247 | 2026-06-29 12:08:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 34d9c6cb-9ba9-3d8c-b45d-4787fd63a0fc | -12.46328 | -44.69677 | 2026-06-29 12:08:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| fe9b6e87-fe7e-35cf-9946-3fd382615ddf | -11.48691 | -47.40919 | 2026-06-29 12:08:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0518d135-e4e2-36ff-8108-4e90e5f74c27 | -14.19922 | -57.43559 | 2026-06-29 12:08:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 31e9773f-a678-3521-adb9-30f670f36a9e | -10.9118 | -56.85352 | 2026-06-29 12:08:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| db054591-4c42-3098-ab2e-11caca56aa18 | -12.44361 | -58.51443 | 2026-06-29 12:08:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 121a1e0f-d568-37bd-a540-0ac4336713c4 | -14.55041 | -53.65237 | 2026-06-29 12:08:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 027878d1-8e4e-3b2f-b74e-13b44e659239 | -12.44667 | -58.50105 | 2026-06-29 12:08:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 312.1 |
| 1ec21457-9df8-33ab-8787-0180e27ce1cd | -14.70419 | -46.14583 | 2026-06-29 12:08:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 53.2 |
| fe1d477c-b142-3840-9e91-83ba72c33656 | -12.45017 | -58.47446 | 2026-06-29 12:08:00 | TERRA_M-T | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 189a52cd-b5bd-3738-a87d-f2e3e970f132 | -11.24084 | -49.44774 | 2026-06-29 12:08:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 35354639-3b9d-3675-81fb-b5faa3aa310a | -15.04472 | -53.0466 | 2026-06-29 12:08:00 | TERRA_M-T | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 59fa6e29-520d-3929-b91d-1a0e6480015b | -10.97985 | -49.54907 | 2026-06-29 12:08:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4c17de1b-340a-308b-a6a0-e513964d46f6 | -11.51133 | -56.12996 | 2026-06-29 12:08:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8232146b-709e-31e7-a952-9e757c1ac058 | -14.55935 | -53.65379 | 2026-06-29 12:08:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 5d0a7068-f854-37ac-8bba-9be59ba43cb9 | -10.37467 | -52.53802 | 2026-06-29 12:08:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 26a2994a-ba53-3745-b73a-b311877fb999 | -11.52395 | -54.79276 | 2026-06-29 12:08:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6151335b-48ba-3033-a486-4abbbafa6f02 | -12.51505 | -48.2784 | 2026-06-29 12:08:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| aaa407f9-0aa8-3aa3-b2ee-9b8b7af548db | -12.55618 | -54.62319 | 2026-06-29 12:08:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 51435207-a2b5-3bd1-adba-c78da5a054a9 | -11.21332 | -54.34353 | 2026-06-29 12:08:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |


[Clique aqui para ver as próximas entradas](README11.md)
