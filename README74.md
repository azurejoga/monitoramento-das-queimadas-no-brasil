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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24a865b7-b1bb-36d2-baee-bc00130b2183 | -7.0166 | -44.6184 | 2026-09-15 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| f771b1c1-0c47-39fd-ac70-4f11647483a0 | -13.3062 | -51.2808 | 2026-09-15 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| ed8e6e56-17b1-3ee8-a35f-d3b292331b8b | -11.5041 | -45.7939 | 2026-09-15 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.6 |
| df0712ad-1bcf-36ef-9a54-e049ab2b0a27 | -18.1714 | -51.7466 | 2026-09-15 12:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 193.8 |
| b8801fb5-6831-3999-97df-2ed0ac1d2b19 | -10.9875 | -48.3209 | 2026-09-15 12:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 99ebdbd0-0ff6-315c-ae87-3e04ffcca62a | -5.1255 | -55.955 | 2026-09-15 12:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e899317e-24fc-363e-b513-1713d46fb3a1 | -11.4857 | -45.7508 | 2026-09-15 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| a6032a81-db00-3dbd-bdcc-0e4525e2656d | -9.7687 | -46.1067 | 2026-09-15 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 179.2 |
| ef47aa5c-c25a-38ac-ab8e-e8688672ec11 | -7.0164 | -44.6413 | 2026-09-15 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 5d1407fe-c6bc-355b-9108-119a03842425 | -10.8661 | -46.3331 | 2026-09-15 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| fbbed240-6abb-31ae-95cc-23e24811dbfb | -11.5049 | -45.7481 | 2026-09-15 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 3ae8950a-d8f7-3790-af9e-a8cbd557748a | -8.638 | -44.4567 | 2026-09-15 12:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 6c230ee5-922b-3458-ab71-641c2ad0614c | -11.5045 | -45.771 | 2026-09-15 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 0888dc76-8df5-3579-94e0-291442da8703 | -10.8665 | -46.3105 | 2026-09-15 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 269.7 |
| 6267b970-2908-3b5c-b89a-2e33ee6e7cf2 | -7.0164 | -44.6413 | 2026-09-15 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 152.5 |
| d5c6a456-e6ed-3196-b3d2-c1ff738d9105 | -11.5045 | -45.771 | 2026-09-15 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 2d5d26e7-5046-31a2-82c3-669e20f14ba1 | -8.8459 | -45.8713 | 2026-09-15 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 190.5 |
| b6da77c2-54bc-382b-81a6-da612364df8c | -9.4234 | -47.8588 | 2026-09-15 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| e2248800-d284-3f20-81fd-93585fa2a7c1 | -10.312 | -45.2907 | 2026-09-15 12:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 126.1 |
| b47beece-51c2-3a3a-9b7e-0d232a04bdf6 | -18.1714 | -51.7466 | 2026-09-15 12:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 200.6 |
| eb907ba5-9fe1-31c8-aaa3-707b5d26138a | -10.3116 | -45.3136 | 2026-09-15 12:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 612c51e4-6aed-3556-b333-ca50f9dc12e3 | -18.1709 | -51.7685 | 2026-09-15 12:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 90b65eff-37e6-365a-b0cb-5aeb6b22fc5d | -5.1256 | -55.9352 | 2026-09-15 12:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 8904c4e3-cdbc-36ac-ab17-54e453e81003 | -8.827 | -45.8733 | 2026-09-15 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| c36266f3-9365-35ea-ab57-6b72836f3951 | -8.6191 | -44.4588 | 2026-09-15 12:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 8482ddd6-e92f-3b6c-a7a4-3bdc90778202 | -15.5763 | -48.8144 | 2026-09-15 12:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 464b4222-ee25-3401-958f-cfb5c3280024 | -7.0166 | -44.6184 | 2026-09-15 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 5c75cf4d-89ae-3da1-afe4-428e027e2ecc | -8.638 | -44.4567 | 2026-09-15 12:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 622de8d1-8ca3-3b64-83db-b673a9b7ea7d | -13.287 | -51.2832 | 2026-09-15 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 37aea0b8-a21b-3974-8f18-c84a95581273 | -10.792 | -46.2071 | 2026-09-15 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| c03129f5-3b04-3f85-b4d0-ec074ec52519 | -10.8665 | -46.3105 | 2026-09-15 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 351.7 |
| 6492bd2f-822c-31a1-9fbe-5242e244fae9 | -11.9033 | -43.8112 | 2026-09-15 12:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| c3869cb4-4992-31a4-b992-14f6c10cc680 | -10.4769 | -50.9846 | 2026-09-15 12:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 71ca912b-7faa-37d0-872d-d925029cf7c5 | -6.8405 | -43.5254 | 2026-09-15 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.2 |
| f352db6f-0f24-3e1f-971b-696db20ae931 | -9.3575 | -50.1156 | 2026-09-15 12:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 70bf86c1-a346-3e56-be64-36efdde2b58f | -11.5049 | -45.7481 | 2026-09-15 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 43afbcc0-d583-37b6-b97e-c295c5ca0bfe | -11.5041 | -45.7939 | 2026-09-15 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 65f9a891-0011-398b-bbcd-ef3f9b67facb | -10.9875 | -48.3209 | 2026-09-15 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| c316a043-e2db-3a90-b0f8-edf261417a22 | -13.7006 | -51.8061 | 2026-09-15 12:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| dd056784-cfc7-3c5d-a9a1-ad59902b4a84 | -11.884 | -43.8142 | 2026-09-15 12:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| f6d42c6c-e5a5-3625-9e27-e16f7e167740 | -13.7002 | -51.8274 | 2026-09-15 12:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 406999f4-902e-36b1-8821-b2dc6743cb8c | -10.8661 | -46.3331 | 2026-09-15 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 3b2598b2-0480-3de7-80c3-ea48d914aa80 | -15.5763 | -48.8144 | 2026-09-15 13:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 977e94bd-9f84-37cd-908f-0d231e1c70c3 | -5.1256 | -55.9352 | 2026-09-15 13:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 907e98ae-09dc-3cbf-8a99-bd053ff75899 | -8.8137 | -46.905 | 2026-09-15 13:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| b5cb174f-a589-3791-b118-09b6b71b7b8e | -2.9025 | -50.4214 | 2026-09-15 13:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| da6bb0ed-f7d0-3a77-94e4-fcbb9c3d1277 | -6.8405 | -43.5254 | 2026-09-15 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 1bcba435-6a62-3e3c-8e87-61e92932a55a | -7.0164 | -44.6413 | 2026-09-15 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 143.2 |
| a63d1aff-48b7-368b-8b79-0325aadc8b91 | -8.6191 | -44.4588 | 2026-09-15 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c94d5078-8976-31de-af7f-b9dcffda04a5 | -11.5045 | -45.771 | 2026-09-15 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 173.3 |
| f963ff17-d548-3af1-a18d-eb3eb57069ce | -10.7916 | -46.2298 | 2026-09-15 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 0a5d08b0-6593-3a54-9167-82d0ed291960 | -13.287 | -51.2832 | 2026-09-15 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 2fad4dba-4ce2-38a2-aadd-342b917bdd01 | -8.5656 | -50.4407 | 2026-09-15 13:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| f91c6fba-fdf0-36ed-9d64-45ff01adfc8e | -13.7006 | -51.8061 | 2026-09-15 13:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| b4069bf9-e536-3ef8-bb9e-34f1ba39981b | -10.8665 | -46.3105 | 2026-09-15 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 425.1 |
| cfcf3161-e106-392f-8d29-2aa10e290509 | -11.884 | -43.8142 | 2026-09-15 13:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 83fa9df2-f525-3036-9c32-f1ccb188b1b6 | -10.0432 | -45.4843 | 2026-09-15 13:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| dde50262-9e50-3110-9212-87b1abb5c21e | -8.8134 | -46.9272 | 2026-09-15 13:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 1ccda2ad-b7ae-34f9-b8cb-d6d953510e5c | -9.7687 | -46.1067 | 2026-09-15 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 251.3 |
| 78527a85-fa35-3601-bda9-7efc5aac82dc | -11.5049 | -45.7481 | 2026-09-15 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| f8359cc4-424a-3e78-a6ac-c143631cece8 | -18.1714 | -51.7466 | 2026-09-15 13:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 258.2 |
| 67c7d113-8c37-3be7-816f-811a24d0b416 | -5.1255 | -55.955 | 2026-09-15 13:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| a0354442-3e29-3522-88b0-848765b04581 | -11.5041 | -45.7939 | 2026-09-15 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 91cca794-e436-3d68-a5e7-1d9d3d21a909 | -9.4234 | -47.8588 | 2026-09-15 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 751e56fd-ffec-3077-a458-0120386b63ee | -8.7949 | -46.9069 | 2026-09-15 13:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 6d73d3df-791a-311d-a56d-04585b1d13ff | -8.638 | -44.4567 | 2026-09-15 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 79202638-c6a9-3a01-ab0b-0beea610be4e | -9.3575 | -50.1156 | 2026-09-15 13:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| d289eb3e-9951-3c40-a770-5234a81109e1 | -10.8661 | -46.3331 | 2026-09-15 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 6656311c-02ab-3de7-9b32-787e78d32c2d | -8.5468 | -50.4423 | 2026-09-15 13:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 157.8 |
| c14b47ef-b109-363f-98af-5cc1a1100d68 | -2.9209 | -50.4208 | 2026-09-15 13:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 0643bbce-6e31-3db9-9840-6a61691a6f94 | -8.7946 | -46.9291 | 2026-09-15 13:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| c2cc2f76-de45-39fa-bf26-e53cce493ec3 | -18.1709 | -51.7685 | 2026-09-15 13:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 335b58b3-94bd-3a77-88b4-de9aa296e82c | -10.792 | -46.2071 | 2026-09-15 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| f88ef998-1311-3e8f-b2ff-184e496110e2 | -13.7002 | -51.8274 | 2026-09-15 13:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| d3b4df0a-8557-3a8c-b0ab-12a869f54c3e | -10.4769 | -50.9846 | 2026-09-15 13:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 437c81a3-794a-3271-9647-1815a0a3fcae | -7.0166 | -44.6184 | 2026-09-15 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 5473f114-1aaa-37be-9723-1c041ff20729 | -8.827 | -45.8733 | 2026-09-15 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 630fd2fb-9426-3dbd-a7e8-11dec3b974f8 | -8.4852 | -44.5885 | 2026-09-15 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 8e5071c5-008d-3786-a790-6bf053b046bd | -8.8459 | -45.8713 | 2026-09-15 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| a7a931bf-aa77-34eb-ab25-3936bd54548f | -7.0823 | -42.1107 | 2026-09-15 13:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 105.2 |
| d46d047e-639f-360d-ae33-d44404660e43 | -4.5229 | -54.9639 | 2026-09-15 13:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 93ce45b5-fe6e-3c7a-b84a-98ab5dcb3329 | -10.0622 | -45.4819 | 2026-09-15 13:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| dc26fad1-242a-3f6b-82e1-c3af78ce4987 | -13.7002 | -51.8274 | 2026-09-15 13:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| cb56e6ab-8582-3c5b-8491-77518bfd9c3a | -13.2867 | -51.3046 | 2026-09-15 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 2bc169bc-94f0-3cee-84b0-5055d3702bd6 | -11.8154 | -46.5899 | 2026-09-15 13:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 2e71de40-8087-39d4-bdea-3f7c42e77ad1 | -11.5041 | -45.7939 | 2026-09-15 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 159.8 |
| ede1fd49-a83b-349c-9f70-922b16f0da26 | -11.5045 | -45.771 | 2026-09-15 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 7f47b833-0d98-3afb-b1f6-01603f11d9e9 | -9.7687 | -46.1067 | 2026-09-15 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 3c1d839b-601b-3058-8910-325d68bb2b8f | -18.1714 | -51.7466 | 2026-09-15 13:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 226.2 |
| 406b1194-819b-371e-9234-42279fc81780 | -10.8661 | -46.3331 | 2026-09-15 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 6b52866a-bfc1-3317-9c8b-26ca96645b2d | -5.144 | -55.9345 | 2026-09-15 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 4d6a9d93-cd6d-3270-8f1b-9d1c0887f0d0 | -8.8459 | -45.8713 | 2026-09-15 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 83b88cb4-a913-3001-9897-2d87aba1aff4 | -7.082 | -42.1346 | 2026-09-15 13:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| 0228355d-eb31-3774-b09b-1c390fd89e2f | -14.4048 | -45.2626 | 2026-09-15 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 393.6 |
| 327b2b0b-5f85-3144-b621-4c22c124c51f | -2.9025 | -50.4214 | 2026-09-15 13:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| e23ca5f9-11ab-31a5-b542-f4a7cb1f1cbb | -5.1439 | -55.9543 | 2026-09-15 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| a06c6f39-fa47-3438-ba88-788b71fa83cf | -10.0988 | -45.5685 | 2026-09-15 13:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 2414e341-8ad7-3581-ab34-ff06b055251c | -13.7006 | -51.8061 | 2026-09-15 13:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 06b6f4b1-55bb-3a93-93db-90b59b95fb21 | -10.792 | -46.2071 | 2026-09-15 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| d4b502d4-a14b-3326-8fdb-d18843ceb36c | -2.7768 | -49.4553 | 2026-09-15 13:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |


[Clique aqui para ver as próximas entradas](README75.md)
