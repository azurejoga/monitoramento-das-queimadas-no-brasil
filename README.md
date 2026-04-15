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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db7eff87-6738-3b58-ab81-8b29ceca1a42 | -20.5379 | -49.4871 | 2026-04-15 00:00:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 70.2 |
| e764d7ad-a11f-35d7-a000-53662e01d03f | -20.5373 | -49.51 | 2026-04-15 00:10:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 0599ef23-63f7-3261-9656-2056f4bcd1cb | -20.5379 | -49.4871 | 2026-04-15 00:10:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 1edcb7f0-a629-3946-a821-50506c5f06dc | -20.5379 | -49.4871 | 2026-04-15 00:20:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 55c185e9-f1c2-3eaf-8e61-957b77d4b439 | 2.5621 | -60.5458 | 2026-04-15 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 7e1648c3-ce58-3712-b64a-d1a0a4668463 | -20.5373 | -49.51 | 2026-04-15 00:20:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 514a2ca7-4b9c-3b56-bcff-2a865cdd7442 | 2.5803 | -60.5456 | 2026-04-15 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| f3275163-6284-3f81-be46-40721b7e80f6 | -20.5379 | -49.4871 | 2026-04-15 00:30:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 105.6 |
| a4134b50-6dbe-31f8-9bf3-f518f0e3a50d | -20.5373 | -49.51 | 2026-04-15 00:30:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 2325bc01-f895-38ec-a1e0-ae484e4c27ca | -20.5379 | -49.4871 | 2026-04-15 00:40:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 31459007-2c63-33e8-8313-5331db6c9d59 | -20.5379 | -49.4871 | 2026-04-15 00:50:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 672920e8-7447-30b2-8830-cdbc4a0380b5 | -20.5373 | -49.51 | 2026-04-15 00:50:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 3febcf07-9d12-3f30-86f1-54e7bd763648 | 2.9617 | -61.341702 | 2026-04-15 00:58:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| da7fd572-46c0-349a-89eb-4b16b3bcd0a2 | 1.8543 | -60.638699 | 2026-04-15 00:58:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a74ac576-a8f1-3600-9c0b-e5d84224feb2 | 3.2279 | -61.2099 | 2026-04-15 00:58:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e94a5a2f-e7b9-3fd3-aec6-8c5d02725177 | 3.2296 | -61.202301 | 2026-04-15 00:58:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0d4cf3cc-52e0-316e-b231-0030a6589505 | 3.2394 | -61.204399 | 2026-04-15 00:58:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 806eb7d8-836d-37f1-99f2-9d2e78df3b59 | 1.9065 | -61.092201 | 2026-04-15 00:58:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dd6cb728-1c0a-3d23-9f1b-25097788d34a | 1.1009 | -60.512501 | 2026-04-15 00:58:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 450cfee4-6e7e-3bd5-8146-085cadb76d1f | 2.3849 | -60.8866 | 2026-04-15 00:58:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2c08f7d6-7205-33fb-ba92-7dbfc37ffd6a | 2.9459 | -60.173599 | 2026-04-15 00:58:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3f4ec1f3-aa0b-35ae-9f90-4189e8bca829 | 2.576 | -60.310501 | 2026-04-15 00:58:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5ee21e8e-d577-3a05-87fd-5503481ff779 | 3.2377 | -61.212002 | 2026-04-15 00:58:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 35816547-8cbd-35a3-b84c-c1b1f7530e07 | 1.4824 | -60.919102 | 2026-04-15 00:58:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3e42b2e0-0309-3d83-a783-627ebf17f84b | 1.9082 | -61.084702 | 2026-04-15 00:58:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 435994b9-99df-3a30-8bc7-230a4225255d | 1.4841 | -60.911598 | 2026-04-15 00:58:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 469abd9e-6982-3823-b1dc-ec82b0341655 | 1.0991 | -60.520302 | 2026-04-15 00:58:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 92737de4-2b3a-3658-af72-36b7d56645e9 | 2.9478 | -60.165199 | 2026-04-15 00:58:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fb9e955c-c167-3170-8797-282109aa1949 | 1.1107 | -60.514599 | 2026-04-15 00:58:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 80d8c743-d79b-351b-b694-d3fb62fea858 | 2.9361 | -60.171398 | 2026-04-15 00:58:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1c9b7cf4-06de-3892-a3eb-49fad0aa3500 | 1.1089 | -60.5224 | 2026-04-15 00:58:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 20e2a87d-35e9-3528-9da0-2820fdd9ec8b | 2.5742 | -60.318699 | 2026-04-15 00:58:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8c3c05eb-1f2e-3058-8521-6227f66665ca | 1.8169 | -60.439899 | 2026-04-15 00:58:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1c92f37c-8eb0-32c6-b100-bd38f58ec545 | -20.5373 | -49.51 | 2026-04-15 01:00:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 88.8 |
| ac8495f1-4a91-320c-bb63-ef8f9031d2f3 | -20.5379 | -49.4871 | 2026-04-15 01:00:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 93.4 |
| f1aac1f2-0095-312a-8945-89383ae3fde9 | -20.5373 | -49.51 | 2026-04-15 01:10:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 2e6dbf90-70df-36f2-afff-2a0315417fa9 | -20.5379 | -49.4871 | 2026-04-15 01:10:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 102.4 |
| b41cd40c-0cbb-34ef-9e41-693572ccab0d | -20.5578 | -49.5056 | 2026-04-15 01:20:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 58.1 |
| a95f9640-0a46-3d6b-8477-18449dcdc8fe | -20.5379 | -49.4871 | 2026-04-15 01:20:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 81.3 |
| d798349b-c072-37a5-8361-edfed56cbc9c | -20.5373 | -49.51 | 2026-04-15 01:20:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 74ed32d5-990b-3b4f-9e09-7219a6fd2538 | -20.5373 | -49.51 | 2026-04-15 01:30:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 85.8 |
| e9cb1784-5da8-3345-a44b-0506fa8ee8f6 | -20.5379 | -49.4871 | 2026-04-15 01:30:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 6c3aed3e-2811-30d3-8572-02a8cab02d91 | -20.5379 | -49.4871 | 2026-04-15 01:40:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 902b5303-925d-3dde-b080-71a806b4050a | -20.5373 | -49.51 | 2026-04-15 01:40:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 9146f433-5908-34ff-bb20-8cbfa6f55de0 | -20.5373 | -49.51 | 2026-04-15 01:50:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 6ab4bda0-eecf-3630-af18-279fa7b34d34 | -20.5379 | -49.4871 | 2026-04-15 01:50:00 | GOES-19 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 1a5c3b33-8824-33aa-869d-0656c3a2c169 | -19.58798 | -40.06854 | 2026-04-15 03:10:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1dc9c28d-3e51-34a3-815c-faf89b3f92eb | -19.58698 | -40.073 | 2026-04-15 03:10:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1c5ea4ef-266e-39e4-ba7e-76bfbee93cfe | -19.59184 | -40.07883 | 2026-04-15 03:10:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f339e3cd-a47a-3f99-bc08-73302d859230 | -19.59769 | -40.08024 | 2026-04-15 03:10:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 41e6cbf1-dbd6-3a45-95d2-3c723254f4bd | -19.59284 | -40.07437 | 2026-04-15 03:10:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 47a7083e-6a30-36c3-8c7e-511cf5567be3 | -11.78329 | -43.62155 | 2026-04-15 03:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f4bc1a13-05a4-3c4b-9ca8-9082046c5b28 | -11.78246 | -43.61634 | 2026-04-15 03:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c421407f-61fc-39a5-ab5a-1e6577bcf37d | -11.78662 | -43.62534 | 2026-04-15 03:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 094c32cb-001c-3b77-957e-aaf3e5063fb6 | -11.79304 | -43.62256 | 2026-04-15 03:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ee38840b-eb09-3373-ba3c-5162f0d5623c | -11.70811 | -44.74411 | 2026-04-15 03:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58b32e3f-fbc6-32a1-b4b6-0edac72aa621 | -11.79379 | -43.61866 | 2026-04-15 03:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7bddcc6f-2bfc-362d-8be2-699d77835a76 | -11.79541 | -43.61989 | 2026-04-15 03:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8ec0abde-badb-3c56-b943-07f5cca74333 | -11.78486 | -43.61369 | 2026-04-15 03:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e831249-e5df-3da0-aae7-faa081d70c65 | -11.7817 | -43.62029 | 2026-04-15 03:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2748d5b8-8083-38c0-ab81-d1486e2817d6 | -11.79308 | -43.63159 | 2026-04-15 03:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7e95da30-77dd-3eb5-8c1a-3a076c022fe7 | -11.79229 | -43.62647 | 2026-04-15 03:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 10f51981-2f78-34d8-9ea4-fbf81c68d836 | -11.79154 | -43.63039 | 2026-04-15 03:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 84071479-a11d-332b-976f-679be0592d43 | -11.78737 | -43.62142 | 2026-04-15 03:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2029fd99-8b2b-33d9-bba3-56544a53dbbb | -11.80107 | -43.62102 | 2026-04-15 03:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f10fe9d-df7c-3d8e-8ffd-f49eeaa40796 | -11.78407 | -43.61763 | 2026-04-15 03:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f880983-21cc-3ae9-8787-5c4615203eab | -11.79463 | -43.62378 | 2026-04-15 03:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 20bca59a-21a9-3883-a8df-ceda1c25cc12 | -11.79385 | -43.62768 | 2026-04-15 03:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 55729839-1cd9-3356-a9e2-3cecedc4ef3e | -11.70717 | -44.74877 | 2026-04-15 03:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e345749b-5c4c-33dc-9919-28bfed0ddaac | -11.78896 | -43.62267 | 2026-04-15 03:38:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f6174d25-959c-3a21-8602-379e83d09d57 | -19.58877 | -40.07661 | 2026-04-15 03:40:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bb19d51b-5ad3-31f3-9025-c9775ea3609d | -15.55311 | -43.15032 | 2026-04-15 03:40:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d28a6a15-5869-36d9-8f89-b21b3e8d7ccf | -19.59663 | -40.07822 | 2026-04-15 03:40:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 85e7d284-4a58-34ac-a794-3b02f9ff0e19 | -18.7364 | -49.79715 | 2026-04-15 03:40:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d62729dd-5e08-3616-8b2f-5e1e969bdec6 | -15.66036 | -43.31414 | 2026-04-15 03:40:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1ff0074b-1adf-347b-b0f3-8931124a4eb7 | -19.59566 | -40.08351 | 2026-04-15 03:40:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 33ed5cbd-1120-30a6-ac3f-2c344e453175 | -15.55249 | -43.15337 | 2026-04-15 03:40:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 743e96bb-98d9-3c14-8c6f-df3f45bcbde1 | -15.55116 | -43.15218 | 2026-04-15 03:40:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 95849a4d-f8f5-3ff8-aba6-41f08743cb2e | -19.5927 | -40.07741 | 2026-04-15 03:40:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ccc7a0d7-44c6-376e-bd08-df8dc741c2a1 | -13.44195 | -43.85178 | 2026-04-15 03:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7416a311-f9ce-3531-8e19-59fe7d781a2d | -13.4412 | -43.85559 | 2026-04-15 03:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b86c84c4-e43f-3cc3-9cc4-7abbba3ac4ad | -18.7292 | -49.79575 | 2026-04-15 03:40:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4172ac09-f86b-39da-a1c5-5ec1a911145e | -17.33819 | -43.58644 | 2026-04-15 03:40:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f1684ddf-c921-32f1-8e63-d7da3aecb1df | -15.65971 | -43.31734 | 2026-04-15 03:40:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f796fe15-f703-3d06-8d41-47c8aab52721 | -15.28731 | -43.06866 | 2026-04-15 03:40:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b94d2614-3fde-36e7-bb2a-852050847cdf | -15.2822 | -43.06748 | 2026-04-15 03:40:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 33aa999b-da3f-3fec-bd36-6df8116853c4 | -15.55176 | -43.14912 | 2026-04-15 03:40:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 607d2eef-8a49-3e8c-8f10-72a2353beeb2 | -19.58974 | -40.07133 | 2026-04-15 03:40:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 61cc9195-0e59-35a8-815d-72150af92f2c | -15.28284 | -43.06431 | 2026-04-15 03:40:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8adeed61-9481-32d5-8b2b-520c835d6e74 | -17.33757 | -43.58945 | 2026-04-15 03:40:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f3c20d5b-3177-3b84-8949-c886cb2df153 | -15.28795 | -43.06548 | 2026-04-15 03:40:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ac95254a-95a8-39f3-bfe6-e003bf7d9a71 | -22.87561 | -48.64217 | 2026-04-15 03:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a546460-8bfc-3711-85bc-1f7a6534fbcf | -20.18867 | -46.57347 | 2026-04-15 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96ffe846-94d2-3d5c-9d4f-83a20f011507 | -22.88043 | -48.64941 | 2026-04-15 03:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc245772-bc62-33ac-8035-4ebf77656a00 | -20.18235 | -46.60155 | 2026-04-15 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00eb9e44-0832-307e-9852-dd2176f3e9e7 | -20.18344 | -46.59671 | 2026-04-15 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b53cd63-e87b-3f71-9f8f-011c8fed0915 | -22.87855 | -48.64425 | 2026-04-15 03:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 49b44aa3-04cb-397c-af82-3d769f943e06 | -20.54207 | -49.49672 | 2026-04-15 03:42:00 | NPP-375D | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dcdd48ab-4afb-3366-9ab1-658ad4bc063f | -20.5333 | -49.50334 | 2026-04-15 03:42:00 | NPP-375D | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e7ea9a57-9b44-3157-89e2-d3edc46293b6 | -20.54165 | -49.49868 | 2026-04-15 03:42:00 | NPP-375D | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README2.md)
